---
name: using-ib-async-docs
description: "Provides guidance for the ib_async documentation (IBKR API library) at ib-api-reloaded.github.io/ib_async/"
---

# Using-Ib-Async-Docs Skill

Practical guidance for the ib_async Python library and its official documentation set.
This skill synthesizes multiple reference files (index + API/guide content) into one
actionable view, with clear navigation cues and common patterns.

## Source Synthesis (Multi-Source)

This skill combines **multiple documentation sources** from the `references/` folder:

- **`references/ib_async.md`** (source type: unknown, confidence: medium)
  - Primary, long-form documentation: overview, installation notes, API docs, events,
    contracts/orders/tickers/objects, IBC/Watchdog, and utility notes.
- **`references/index.md`** (source type: unknown, confidence: medium)
  - Documentation index that confirms the canonical entry point and page grouping.

**Agreements:** The index points directly to the ib_async documentation; the API and
concepts listed in `ib_async.md` are consistent with the index’s structure.

**Discrepancies:** None detected in the provided sources.

**If a conflict appears later:** Prefer the priority order defined in this repo:
1) codebase analysis, 2) official docs, 3) GitHub issues, 4) PDFs.

## When to Use This Skill

Trigger this skill when you need to:

- Build or maintain Python tooling that connects to **Interactive Brokers TWS or IB Gateway**.
- Understand **ib_async** core API objects (IB, Contract, Order, Ticker, Objects).
- Decide between **blocking vs. async** request methods or prevent event-loop blocking.
- Use **market data** and **historical data** requests (`reqMktData`, `reqHistoricalData`).
- Place, modify, or cancel **orders** programmatically.
- Work with **account/portfolio state** (positions, account summary, PnL).
- Automate TWS/Gateway using **IBC** or monitor with **Watchdog**.
- Resolve errors related to timeouts, connection sync, or event-driven updates.

## Key Concepts

- **IB class (central API):** The main interface to IBKR. It exposes blocking request
  methods and async counterparts (suffix `Async`). Blocking methods keep the client
  state synced while they wait.
- **Do not block the event loop:** The docs explicitly warn against `time.sleep()` and
  long computations in the main thread. Use `sleep()` or `IB.sleep(0)` to yield.
- **Event-driven updates:** The IB instance emits events like `connectedEvent`,
  `updateEvent`, and `pendingTickersEvent`, which power reactive patterns.
- **Contracts & Orders:** Contracts represent instruments (Stock, Option, Future, Forex,
  Index, Bond). Orders are Market/Limit/Stop variants; `Trade` tracks lifecycle.
- **Market data vs. historical data:** Real-time updates flow through `Ticker` objects;
  historical data comes back as `BarDataList`.
- **IBC & Watchdog:** IBC starts and manages TWS/Gateway; Watchdog monitors connectivity
  and restarts if the app stalls. Both are meant for event-driven apps, not notebooks.

## Quick Reference (Practical Patterns)

Short patterns derived from the official docs and API descriptions in
`references/ib_async.md`. These are minimal, documentation-aligned templates.

### 1) Non-blocking delay and yielding (source: ib_async.md)

```python
from ib_async import IB, util

# Always avoid time.sleep(); yield to the network loop instead
IB.sleep(0)
# or use the library sleep for actual delays
util.sleep(1.0)
``` 

### 2) Connect and disconnect cleanly (source: ib_async.md)

```python
from ib_async import IB

ib = IB()
ib.connect("127.0.0.1", 7497, clientId=1)
# ... work with requests and state ...
ib.disconnect()
``` 

### 3) Request market data and read a ticker (source: ib_async.md)

```python
from ib_async import IB, Stock

ib = IB()
ib.connect("127.0.0.1", 7497, clientId=1)
contract = Stock("AAPL", "SMART", "USD")
ticker = ib.reqMktData(contract)
IB.sleep(0)  # allow updates to flow
print(ticker.bid, ticker.ask, ticker.last)
``` 

### 4) Historical data request with documented duration strings (source: ib_async.md)

```python
from ib_async import IB, Stock

ib = IB()
ib.connect("127.0.0.1", 7497, clientId=1)
contract = Stock("AAPL", "SMART", "USD")
# durationStr examples in docs: '60 S', '30 D', '13 W', '6 M', '10 Y'
bars = ib.reqHistoricalData(contract, durationStr="30 D")
``` 

### 5) Place and cancel an order (source: ib_async.md)

```python
from ib_async import IB, Stock, MarketOrder

ib = IB()
ib.connect("127.0.0.1", 7497, clientId=1)
contract = Stock("AAPL", "SMART", "USD")
order = MarketOrder("BUY", 100)
trade = ib.placeOrder(contract, order)
ib.cancelOrder(order)
``` 

### 6) Account and portfolio state (source: ib_async.md)

```python
from ib_async import IB

ib = IB()
ib.connect("127.0.0.1", 7497, clientId=1)
positions = ib.positions()
summary = ib.accountSummary()
pnl = ib.reqPnL()
``` 

### 7) Start TWS/Gateway with IBC (source: ib_async.md)

```python
from ib_async import IBC

ibc = IBC(
    twsVersion=976,
    gateway=True,
    tradingMode="paper",
    userid="YOUR_USER",
    password="YOUR_PASS",
)
ibc.start()
``` 

### 8) Watchdog with IBC + IB (source: ib_async.md)

```python
from ib_async import IB, IBC, Watchdog

ib = IB()
ibc = IBC(twsVersion=976, gateway=True, tradingMode="paper")
watchdog = Watchdog(controller=ibc, ib=ib, host="127.0.0.1", port=4002, clientId=1)
watchdog.start()
``` 

## Working with This Skill

### Beginners
- Start with **`references/ib_async.md`** and read the Introduction + Installation
  sections to understand required setup (TWS/IBG, API port, memory settings).
- Focus on the **IB class** and the warnings about **not blocking the event loop**.
- Use the Quick Reference examples to scaffold your first connection and data request.

### Intermediate Users
- Use the API sections in `references/ib_async.md` to identify the right module:
  `ib_async.ib.IB`, `ib_async.contract`, `ib_async.order`, `ib_async.ticker`,
  `ib_async.objects`, and `ib_async.utilities`.
- Prefer blocking methods for straightforward scripts; switch to `*Async` methods
  when you need fine-grained asyncio control.
- Validate event usage (e.g., `pendingTickersEvent`, `barUpdateEvent`) when you need
  reactive designs.

### Advanced Users
- Use **IBC + Watchdog** for long-running, production-like systems.
- Combine `FlexReport` (account statements) with automated workflows when you need
  end-of-day reconciliation or reporting.
- Tune behavior with documented parameters like `RequestTimeout`, `RaiseRequestErrors`,
  and `TimezoneTWS` when debugging sync/timezone or timeout issues.

### Resolving Conflicts
- No conflicts are present in current sources. If you encounter differences later:
  prefer real code behavior (codebase analysis) over docs, and docs over community notes.

## Reference Files (What’s Inside)

- **`references/ib_async.md`** (source type: unknown, confidence: medium)
  - Full documentation dump from the ib_async site, including:
    - Overview and installation requirements
    - Core API: IB class, blocking vs async requests
    - Contracts, orders, tickers, objects, and utilities
    - Events and non-blocking guidance (`sleep()`, `IB.sleep(0)`)
    - IBC automation and Watchdog lifecycle notes
- **`references/index.md`** (source type: unknown, confidence: medium)
  - Minimal index that confirms the canonical documentation scope and page grouping.

Use `view` to open a specific reference file when you need more detail.

## Known Discrepancies

None detected in the provided sources.

## Notes

- The docs emphasize **not blocking the event loop**; avoid `time.sleep()` and use
  the provided `sleep()`/`IB.sleep(0)` utilities.
- ib_async implements the full IBKR API protocol internally; the `ibapi` package
  is not required.
- IBC/Watchdog are intended for event-driven, long-running apps, not notebooks.

## Updating This Skill

To refresh this skill with updated documentation:
1. Re-run the scraper with the same configuration.
2. Regenerate references under `references/`.
3. Re-synthesize this SKILL.md with the updated sources.
