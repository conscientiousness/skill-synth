---
name: using-ib-async-docs
description: Guides ib_async (Interactive Brokers API) usage and API patterns; use when building or debugging Python code that connects to TWS/IB Gateway, requests market or historical data, places orders, or handles ib_async async/event behavior.
---

# ib_async Docs Skill

## Quick Reference (start here)
- IB is the main entry point. Request method names/parameters mirror EClient (no reqId). Async variants end with Async.
- Do not block the event loop. Avoid time.sleep; use IB.sleep(...) to yield or delay.
- Prefer contract helper classes (Stock, Forex, Future, Option, Crypto, etc) and order helper classes (MarketOrder, LimitOrder, StopOrder, StopLimitOrder).
- If you need exact signatures, open references/api.md (canonical).

### Minimal patterns

```python
from ib_async import IB, Stock, MarketOrder

ib = IB()
ib.connect("127.0.0.1", 7497, clientId=1)

contract = Stock("AAPL", "SMART", "USD")
order = MarketOrder("BUY", 10)
trade = ib.placeOrder(contract, order)

IB.sleep(0)  # yield so updates/events can flow
ib.cancelOrder(order)
ib.disconnect()
```

### Event hooks (common)
- connectedEvent, disconnectedEvent, updateEvent, pendingTickersEvent, barUpdateEvent, errorEvent
- Avoid placing new requests inside event handlers (risk of recursion)

## Where to Look Next
- references/api.md: Canonical API signatures and class constructors from api.html.
- references/ib_async.md: Full narrative docs and extended API detail.
- references/index.md: Navigation map for the doc set.

## Conflict Resolution
- Prefer references/api.md (API docs) over references/ib_async.md if signatures differ.
