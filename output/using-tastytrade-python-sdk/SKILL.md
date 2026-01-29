---
name: using-tastytrade-python-sdk
description: "Provides guidance for the tastytrade (tastyworks) Python SDK (sessions, accounts, orders, instruments, market data, and streaming APIs)."
---

# Using Tastytrade Python SDK Skill

## Purpose
Use this skill to verify exact SDK usage (imports, class names, parameters, and async patterns) from the docs before producing code.

## When to Use This Skill
- You need confirmed names or call patterns in the tastytrade Python SDK.
- You are working with Sessions, Accounts, Watchlists, or streamers.
- You need async usage details for streaming APIs.

## Do Not Use This When
- The question is about the tastytrade web UI, pricing, or account policies.
- The question is about a non-Python SDK or an unofficial wrapper.

## Required Inputs
- The user goal (sessions, accounts, watchlists, streamers, orders, instruments, or market data).
- Whether the user needs account-level streaming or market data streaming.

## Workflow
1. Open `references/index.md` to locate the category.
2. Open `references/api.md` and jump to the relevant section.
3. Copy exact names and call patterns from the docs.
4. Return short, directly usable Python snippets.

## Output Rules
- Keep examples aligned with the docs and avoid inventing APIs.
- Streamers must be initialized with `async with ...` or `await ...` as shown in the docs.
- Watchlists require a production session.

## Examples (from docs)

### Create an OAuth session
```python
from tastytrade import Session

session = Session('client_secret', 'refresh_token')
``` 

### List accounts for a session
```python
from tastytrade import Account

accounts = Account.get(session)
``` 

### Refresh a session when expired
```python
from tastytrade import Account
from tastytrade.utils import now_in_new_york

if now_in_new_york() > session.session_expiration:
    session.refresh()
    print(Account.get(session))
``` 

### Fetch a private watchlist
```python
from tastytrade import Session, PrivateWatchlist

session = Session(user, password)
watchlist = PrivateWatchlist.get(session, 'MyWatchlist')
print(watchlist.watchlist_entries)
``` 

### Stream account updates (async)
```python
from tastytrade import Account, AlertStreamer, Watchlist

async with AlertStreamer(session) as streamer:
    accounts = Account.get(session)

    await streamer.subscribe_accounts(accounts)
    await streamer.subscribe_public_watchlists()
    await streamer.subscribe_quote_alerts()

    async for wl in streamer.listen(Watchlist):
        print(wl)
``` 

### Create a data streamer (async)
```python
from tastytrade import DXLinkStreamer

async with DXLinkStreamer(session) as streamer:
    pass
``` 

## References
- `references/index.md`
- `references/api.md`
