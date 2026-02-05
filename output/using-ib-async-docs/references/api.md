# ib_async API Quick Reference (api.html)

Source: ib-api-reloaded.github.io/ib_async/api.html (Release 2.1.0)

## Canonical rules
- IB is the main interface. Request method names/parameters mirror EClient, except reqId is not used.
- Async variants add an Async suffix to the blocking method name.
- Do not block the event loop; use IB.sleep(...) to yield or delay.

## Core IB entry points

### IB.connect
Signature:
IB.connect(
    host="127.0.0.1",
    port=7497,
    clientId=1,
    timeout=4,
    readonly=False,
    account="",
    raiseSyncErrors=False,
    fetchFields=StartupFetchALL,
)

Notes:
- connect() blocks until the client is in sync.
- Disconnect with IB.disconnect().

### IB.placeOrder / IB.cancelOrder
- placeOrder(contract, order) -> Trade
- cancelOrder(order, manualCancelOrderTime="") -> Trade | None

### IB.qualifyContracts
- qualifyContracts(*contracts) -> list[Contract]

## Contracts
- Contract(**kwargs) can define any field explicitly.
- Helper classes with typed constructors include:
  - Stock(symbol, exchange, currency)
  - Forex(pair, exchange="IDEALPRO")
  - CFD(symbol, exchange, currency)
  - Future(symbol, lastTradeDateOrContractMonth, exchange, currency="")
  - Option(symbol, lastTradeDateOrContractMonth, strike, right, exchange, currency="", multiplier="", tradingClass="")
  - Bond(conId)
  - Crypto(symbol, exchange, currency)

## Orders
- MarketOrder(action, totalQuantity, **kwargs)
- LimitOrder(action, totalQuantity, lmtPrice, **kwargs)
- StopOrder(action, totalQuantity, stopPrice, **kwargs)
- StopLimitOrder(action, totalQuantity, lmtPrice, stopPrice, **kwargs)

## Events (common)
- connectedEvent, disconnectedEvent, updateEvent, pendingTickersEvent, barUpdateEvent, errorEvent
- Avoid placing new requests inside event handlers (risk of recursion)

## Watchdog (optional)
- Watchdog(
    controller,
    ib,
    host="127.0.0.1",
    port=7497,
    clientId=1,
    connectTimeout=2,
    appStartupTime=30,
    appTimeout=20,
    retryDelay=2,
    readonly=False,
    account="",
    raiseSyncErrors=False,
    probeContract=Forex("EURUSD", exchange="IDEALPRO"),
    probeTimeout=4,
  )
- Intended for event-driven, long-running apps; not for notebooks.
