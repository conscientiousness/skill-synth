#!/usr/bin/env python3
"""Build a Skill Seekers-aligned enhancement prompt.

This script mirrors the prompt structure used by Skill Seekers' local
enhance flow (enhance_skill_local.py), but keeps output ASCII-only.
"""

from __future__ import annotations

import argparse
from pathlib import Path

LOCAL_CONTENT_LIMIT = 50000
LOCAL_PREVIEW_LIMIT = 20000
SUMMARY_THRESHOLD = 30000


def _determine_source_metadata(relative_path: Path) -> tuple[str, str, str | None]:
    """Determine source type, confidence level, and repo_id from path."""
    path_str = str(relative_path)
    repo_id: str | None = None

    if path_str.startswith("documentation/"):
        return "documentation", "high", None
    if path_str.startswith("github/"):
        if "README" in path_str or "releases" in path_str:
            return "github", "medium", None
        if "issues" in path_str:
            return "github", "low", None
        return "github", "medium", None
    if path_str.startswith("pdf/"):
        return "pdf", "high", None
    if path_str.startswith("api/"):
        return "api", "high", None
    if path_str.startswith("codebase_analysis/"):
        parts = Path(path_str).parts
        if len(parts) >= 2:
            repo_id = parts[1]
        if "ARCHITECTURE" in path_str:
            return "codebase_analysis", "high", repo_id
        if "patterns" in path_str or "examples" in path_str:
            return "codebase_analysis", "medium", repo_id
        if "configuration" in path_str:
            return "codebase_analysis", "high", repo_id
        return "codebase_analysis", "medium", repo_id
    if "conflicts" in path_str:
        return "conflicts", "medium", None
    return "unknown", "medium", None


def read_reference_files(skill_dir: Path, max_chars: int, preview_limit: int) -> dict[str, dict]:
    references_dir = skill_dir / "references"
    references: dict[str, dict] = {}

    if not references_dir.exists():
        return references

    total_chars = 0
    for ref_file in sorted(references_dir.rglob("*.md")):
        content = ref_file.read_text(encoding="utf-8")

        truncated = False
        if len(content) > preview_limit:
            content = content[:preview_limit] + "\n\n[Content truncated...]"
            truncated = True

        relative_path = ref_file.relative_to(references_dir)
        source_type, confidence, repo_id = _determine_source_metadata(relative_path)

        references[str(relative_path)] = {
            "content": content,
            "source": source_type,
            "confidence": confidence,
            "path": str(relative_path),
            "truncated": truncated,
            "size": len(content),
            "repo_id": repo_id,
        }

        total_chars += len(content)
        if total_chars > max_chars:
            break

    return references


def summarize_reference(content: str, target_ratio: float = 0.3) -> str:
    """Summarize reference content to reduce size.

    Strategy (mirrors Skill Seekers local enhance):
    - Keep first 20%
    - Extract up to 5 code blocks
    - Keep up to 10 headings with their first paragraph
    """
    lines = content.split("\n")
    intro_lines = int(len(lines) * 0.2)
    result_lines = lines[:intro_lines]

    in_code_block = False
    code_blocks: list[list[str]] = []
    current_block: list[str] = []

    for line in lines[intro_lines:]:
        if line.strip().startswith("```"):
            if in_code_block:
                current_block.append(line)
                code_blocks.append(current_block)
                current_block = []
                in_code_block = False
            else:
                in_code_block = True
                current_block = [line]
        elif in_code_block:
            current_block.append(line)

    result = result_lines.copy()
    for block in code_blocks[:5]:
        result.append("")
        result.extend(block)

    i = intro_lines
    headings_added = 0
    while i < len(lines) and headings_added < 10:
        line = lines[i]
        if line.startswith("#"):
            chunk = lines[i : min(i + 4, len(lines))]
            result.extend(chunk)
            headings_added += 1
            i += 4
        else:
            i += 1

    result.append("\n\n[Content intelligently summarized - full details in reference files]")
    return "\n".join(result)


def build_prompt(skill_dir: Path, use_summarization: bool, summarization_ratio: float) -> str:
    references = read_reference_files(skill_dir, max_chars=LOCAL_CONTENT_LIMIT, preview_limit=LOCAL_PREVIEW_LIMIT)
    if not references:
        return ""

    sources_found = {meta["source"] for meta in references.values()}
    total_ref_size = sum(meta["size"] for meta in references.values())

    if use_summarization or total_ref_size > SUMMARY_THRESHOLD:
        for key, meta in references.items():
            summarized = summarize_reference(meta["content"], target_ratio=summarization_ratio)
            meta["content"] = summarized
            meta["size"] = len(summarized)

    current_skill_md = ""
    skill_md_path = skill_dir / "SKILL.md"
    if skill_md_path.exists():
        current_skill_md = skill_md_path.read_text(encoding="utf-8")

    has_conflicts = any("conflicts" in meta["path"] for meta in references.values())

    by_source: dict[tuple[str, str | None], list[tuple[str, dict]]] = {}
    for filename, metadata in references.items():
        source = metadata["source"]
        repo_id = metadata.get("repo_id")
        key = (source, repo_id) if repo_id else (source, None)
        by_source.setdefault(key, []).append((filename, metadata))

    prompt = f"""I need you to enhance the SKILL.md file for the {skill_dir.name} skill.

SKILL OVERVIEW:
- Name: {skill_dir.name}
- Source Types: {', '.join(sorted(sources_found))}
- Multi-Source: {'Yes' if len(sources_found) > 1 else 'No'}
- Conflicts Detected: {'Yes - see conflicts.md in references' if has_conflicts else 'No'}

CURRENT SKILL.MD:
{'-' * 60}
{current_skill_md if current_skill_md else '(No existing SKILL.md - create from scratch)'}
{'-' * 60}

SOURCE ANALYSIS:
{'-' * 60}
This skill combines knowledge from {len(sources_found)} source type(s):

"""

    for source, repo_id in sorted(by_source.keys()):
        files = by_source[(source, repo_id)]
        if repo_id:
            prompt += f"\n**{source.upper()} - {repo_id} ({len(files)} file(s))**\n"
        else:
            prompt += f"\n**{source.upper()} ({len(files)} file(s))**\n"
        for filename, metadata in files[:5]:
            prompt += f"- {filename} (confidence: {metadata['confidence']}, {metadata['size']:,} chars)\n"
        if len(files) > 5:
            prompt += f"- ... and {len(files) - 5} more\n"

    prompt += f"""
{'-' * 60}

REFERENCE DOCUMENTATION:
{'-' * 60}
"""

    for source, repo_id in sorted(by_source.keys()):
        if repo_id:
            prompt += f"\n### {source.upper()} SOURCES - {repo_id}\n\n"
        else:
            prompt += f"\n### {source.upper()} SOURCES\n\n"

        for filename, metadata in by_source[(source, repo_id)]:
            content = metadata["content"]
            max_per_file = 12000
            if len(content) > max_per_file:
                content = content[:max_per_file] + "\n\n[Content truncated for size...]"

            prompt += f"\n#### {filename}\n"
            if repo_id:
                prompt += f"*Source: {metadata['source']} ({repo_id}), Confidence: {metadata['confidence']}*\n\n"
            else:
                prompt += f"*Source: {metadata['source']}, Confidence: {metadata['confidence']}*\n\n"
            prompt += f"{content}\n"

    prompt += f"""
{'-' * 60}

REFERENCE PRIORITY (when sources differ):
1. Code patterns (codebase_analysis): Ground truth - what the code actually does
2. Official documentation: Intended API and usage patterns
3. GitHub issues: Real-world usage and known problems
4. PDF documentation: Additional context and tutorials

MULTI-REPOSITORY HANDLING:
"""

    repo_ids = {meta.get("repo_id") for meta in references.values() if meta.get("repo_id")}
    if len(repo_ids) > 1:
        prompt += f"""
WARNING: MULTIPLE REPOSITORIES DETECTED: {', '.join(sorted(repo_ids))}

This skill combines codebase analysis from {len(repo_ids)} different repositories.
Each repo has its own ARCHITECTURE.md, patterns, examples, and configuration.

When synthesizing:
- Clearly identify which content comes from which repo
- Compare and contrast patterns across repos
- Highlight relationships
- Present examples from BOTH repos to show different use cases
- If repos serve different purposes, explain when to use each
"""
    else:
        prompt += "\nSingle repository - standard synthesis applies.\n"

    prompt += """

YOUR TASK:
Create an EXCELLENT SKILL.md file that synthesizes knowledge from multiple sources.

Requirements:
1. Multi-Source Synthesis
   - Acknowledge that this skill combines multiple sources
   - Highlight agreements between sources (builds confidence)
   - Note discrepancies transparently (if present)
   - Use source priority when synthesizing conflicting information

2. Clear "When to Use This Skill" section
   - Be SPECIFIC about trigger conditions
   - List concrete use cases
   - Include perspective from both docs AND real-world usage (if GitHub/codebase data available)

3. Excellent Quick Reference section
   - Extract 5-10 of the BEST, most practical code examples
   - Prefer examples from HIGH CONFIDENCE sources first
   - If code examples exist from codebase analysis, prioritize those (real usage)
   - If docs examples exist, include those too (official patterns)
   - Choose SHORT, clear examples (5-20 lines max)
   - Use proper language tags (cpp, python, javascript, json, etc.)
   - Add clear descriptions noting the source (e.g., "From official docs" or "From codebase")

4. Detailed Reference Files description
   - Explain what's in each reference file
   - Note the source type and confidence level
   - Help users navigate multi-source documentation

5. Practical "Working with This Skill" section
   - Clear guidance for beginners, intermediate, and advanced users
   - Navigation tips for multi-source references
   - How to resolve conflicts if present

6. Key Concepts section (if applicable)
   - Explain core concepts
   - Define important terminology
   - Reconcile differences between sources if needed

7. Conflict Handling (if conflicts detected)
   - Add a "Known Discrepancies" section
   - Explain major conflicts transparently
   - Provide guidance on which source to trust in each case

IMPORTANT:
- Extract REAL examples from the reference docs above
- Prioritize HIGH CONFIDENCE sources when synthesizing
- Note source attribution when helpful
- Make discrepancies transparent, not hidden
- Prioritize SHORT, clear examples
- Make it actionable and practical
- Keep the frontmatter (---\nname: ...\n---) intact
- Ensure YAML frontmatter is valid YAML (quote the description if needed)
- Use proper markdown formatting

SAVE THE RESULT:
You MUST save the complete enhanced SKILL.md file.

CRITICAL INSTRUCTIONS:
1. First, create a backup: Write the current SKILL.md content to SKILL.md.backup
2. Then, write the enhanced content to: SKILL.md

This is NOT a read-only task - you have permission to modify SKILL.md.
Even if running from within another agent session, this modification is ALLOWED and EXPECTED.

VERIFICATION:
After writing, the file SKILL.md should:
- Exist in the current directory
- Be larger than the original (200-1000+ lines)
- Contain all the enhancements from the references above
"""

    return prompt


def main() -> int:
    parser = argparse.ArgumentParser(description="Build Skill Seekers enhancement prompt")
    parser.add_argument("skill_dir", help="Path to skill directory")
    parser.add_argument("--summarize", action="store_true", help="Force summarization")
    parser.add_argument("--summarization-ratio", type=float, default=0.3)
    args = parser.parse_args()

    skill_dir = Path(args.skill_dir)
    prompt = build_prompt(skill_dir, use_summarization=args.summarize, summarization_ratio=args.summarization_ratio)
    print(prompt)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
