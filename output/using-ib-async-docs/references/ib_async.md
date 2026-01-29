# Using-Ib-Async-Docs - Ib Async

**Pages:** 8

---

## Contents — ib_async 2.1.0 documentation

**URL:** https://ib-api-reloaded.github.io/ib_async/index.html

**Contents:**
- Contents
- ib_async
  - Update
  - Introduction
    - What You Can Build
    - Key Features
  - Installation
  - Build Manually
    - Installing Only Library
    - Install Everything (enable docs + dev testing)

ib_async is a Python library that provides a clean, modern interface to Interactive Brokers’ Trader Workstation (TWS) and IB Gateway. It handles the complexities of the IBKR API so you can focus on building trading applications, research tools, and market data analysis.

Market Data Applications: Stream live quotes, historical data, and market depth

Trading Systems: Place, modify, and monitor orders programmatically

Portfolio Tools: Track positions, account balances, and P&L in real-time

Research Platforms: Analyze contract details, option chains, and fundamental data

Risk Management: Monitor exposures and implement automated controls

Simple and Intuitive: Write straightforward Python code without dealing with callback complexity

Automatic Synchronization: The IB component stays in sync with TWS/Gateway automatically

Async-Ready: Built on asyncio and eventkit for high-performance applications

Jupyter-Friendly: Interactive development with live data in notebooks

Production-Ready: Robust error handling, reconnection logic, and comprehensive logging

Be sure to take a look at the notebooks, the recipes and the API docs.

Python 3.10 or higher

We plan to support Python releases 2 years back which allows us to continue adding newer features and performance improvements over time.

A running IB Gateway application (or TWS with API mode enabled)

stable gateway — updated every few months

latest gateway — updated weekly

Make sure the API port is enabled and ‘Download open orders on connection’ is checked.

You may also want to increase the Java memory usage under Configure->Settings->Memory Allocation to 4096 MB minimum to prevent gateway crashes when loading bulk data.

The ibapi package from IB is not needed. ib_async implements the full IBKR API binary protocol internally.

First, install poetry:

IB Gateway (Stable) — Updated every few months, more stable

IB Gateway (Latest) — Updated weekly, newest features

Trader Workstation (TWS) — Full trading platform

Enable API: Go to Configure → API → Settings and check “Enable ActiveX and Socket Clients”

Set Port: Default ports are 7497 (TWS) and 4001 (Gateway). You can change these if needed.

Allow Connections: Add 127.0.0.1 to “Trusted IPs” if connecting locally

Download Orders: Check “Download open orders on connection” to see existing orders

Memory: Go to Configure → Settings → Memory Allocation and set to 4096 MB minimum to prevent crashes with bulk data

Timeouts: Increase API timeout settings if you experience disconnections during large data requests

ib_async.ib.IB - Main interface class

Connection management (connect(), disconnect(), connectAsync())

Market data requests (reqMktData(), reqHistoricalData())

Order management (placeOrder(), cancelOrder())

Account data (positions(), accountSummary(), reqPnL())

ib_async.contract - Financial instruments

Stock, Option, Future, Forex, Index, Bond

Contract - Base class for all instruments

ComboLeg, DeltaNeutralContract - Complex instruments

ib_async.order - Order types and management

MarketOrder, LimitOrder, StopOrder, StopLimitOrder

Order - Base order class with all parameters

OrderStatus, OrderState - Order execution tracking

Trade - Complete order lifecycle tracking

ib_async.ticker - Real-time market data

Ticker - Live quotes, trades, and market data

Automatic field updates (bid, ask, last, volume, etc.)

Event-driven updates via updateEvent

ib_async.objects - Data structures

BarData - Historical price bars

Position - Portfolio positions

PortfolioItem - Portfolio details with P&L

AccountValue - Account metrics

Synchronous vs Asynchronous

The complete API documentation.

Clone the repository:

Install dependencies:

Make your changes and run tests:

Submit a pull request with:

Clear description of changes

Tests for new functionality

Updated documentation if needed

Follow existing code style (enforced by ruff)

Add tests for new features

Update documentation for user-facing changes

Keep commits focused and well-described

Be responsive to code review feedback

If you have other public work related to ib_async or ib_insync open an issue and we can keep an active list here.

Projects below are not endorsed by any entity and are purely for reference or entertainment purposes.

Adi’s livestream VODs about using IBKR APIs: Interactive Brokers API in Python

Matt’s IBKR python CLI: icli

Corporate data parsing via IBKR API: ib_fundamental

The software is provided on the conditions of the simplified BSD license.

This project is not affiliated with Interactive Brokers Group, Inc.

Official Interactive Brokers API Docs

This library was originally created by Ewald de Wit as tws_async in early-2017 then became the more prominent ib_insync library in mid-2017. He maintained and improved the library for the world to use for free until his unexpected passing in early 2024. Afterward, we decided to rename the project to ib_async under a new github organization since we lost access to modify anything in the original repos and packaging and docs infrastructure.

The library is currently maintained by Matt Stancliff and we are open to adding more committers and org contributors if people show interest in helping out.

---

## API docs — ib_async 2.1.0 documentation

**URL:** https://ib-api-reloaded.github.io/ib_async/api.html

**Contents:**
- API docs
- IB
- Client
- Order
- Contract
- Ticker
- Objects
- Utilities
- FlexReport
- IBC

Also see the official Python API documentation from IB.

High-level interface to Interactive Brokers.

Provides both a blocking and an asynchronous interface to the IB API, using asyncio networking and event loop.

The IB class offers direct access to the current state, such as orders, executions, positions, tickers etc. This state is automatically kept in sync with the TWS/IBG application.

This class has most request methods of EClient, with the same names and parameters (except for the reqId parameter which is not needed anymore). Request methods that return a result come in two versions:

Blocking: Will block until complete and return the result. The current state will be kept updated while the request is ongoing;

Asynchronous: All methods that have the “Async” postfix. Implemented as coroutines or methods that return a Future and intended for advanced users.

While some of the request methods are blocking from the perspective of the user, the framework will still keep spinning in the background and handle all messages received from TWS/IBG. It is important to not block the framework from doing its work. If, for example, the user code spends much time in a calculation, or uses time.sleep() with a long delay, the framework will stop spinning, messages accumulate and things may go awry.

The one rule when working with the IB class is therefore that

user code may not block for too long.

To be clear, the IB request methods are okay to use and do not count towards the user operation time, no matter how long the request takes to finish.

So what is “too long”? That depends on the situation. If, for example, the timestamp of tick data is to remain accurate within a millisecond, then the user code must not spend longer than a millisecond. If, on the other extreme, there is very little incoming data and there is no desire for accurate timestamps, then the user code can block for hours.

If a user operation takes a long time then it can be farmed out to a different process. Alternatively the operation can be made such that it periodically calls IB.sleep(0); This will let the framework handle any pending work and return when finished. The operation should be aware that the current state may have been updated during the sleep(0) call.

For introducing a delay, never use time.sleep() but use sleep() instead.

RequestTimeout (float) – Timeout (in seconds) to wait for a blocking request to finish before raising asyncio.TimeoutError. The default value of 0 will wait indefinitely. Note: This timeout is not used for the *Async methods.

RaiseRequestErrors (bool) – Specifies the behaviour when certain API requests fail: False: Silently return an empty result; True: Raise a RequestError.

Specifies the behaviour when certain API requests fail:

False: Silently return an empty result;

True: Raise a RequestError.

MaxSyncedSubAccounts (int) – Do not use sub-account updates if the number of sub-accounts exceeds this number (50 by default).

TimezoneTWS (str) – Specifies what timezone TWS (or gateway) is using. The default is to assume local system timezone.

connectedEvent (): Is emitted after connecting and synchronzing with TWS/gateway.

disconnectedEvent (): Is emitted after disconnecting from TWS/gateway.

updateEvent (): Is emitted after a network packet has been handled.

pendingTickersEvent (tickers: Set[Ticker]): Emits the set of tickers that have been updated during the last update and for which there are new ticks, tickByTicks or domTicks.

barUpdateEvent (bars: BarDataList, hasNewBar: bool): Emits the bar list that has been updated in real time. If a new bar has been added then hasNewBar is True, when the last bar has changed it is False.

newOrderEvent (trade: Trade): Emits a newly placed trade.

orderModifyEvent (trade: Trade): Emits when order is modified.

cancelOrderEvent (trade: Trade): Emits a trade directly after requesting for it to be cancelled.

openOrderEvent (trade: Trade): Emits the trade with open order.

orderStatusEvent (trade: Trade): Emits the changed order status of the ongoing trade.

execDetailsEvent (trade: Trade, fill: Fill): Emits the fill together with the ongoing trade it belongs to.

commissionReportEvent (trade: Trade, fill: Fill, report: CommissionReport): The commission report is emitted after the fill that it belongs to.

updatePortfolioEvent (item: PortfolioItem): A portfolio item has changed.

positionEvent (position: Position): A position has changed.

accountValueEvent (value: AccountValue): An account value has changed.

accountSummaryEvent (value: AccountValue): An account value has changed.

pnlEvent (entry: PnL): A profit- and loss entry is updated.

pnlSingleEvent (entry: PnLSingle): A profit- and loss entry for a single position is updated.

tickNewsEvent (news: NewsTick): Emit a new news headline.

newsBulletinEvent (bulletin: NewsBulletin): Emit a new news bulletin.

scannerDataEvent (data: ScanDataList): Emit data from a scanner subscription.

wshMetaEvent (dataJson: str): Emit WSH metadata.

wshEvent (dataJson: str): Emit WSH event data (such as earnings dates, dividend dates, options expiration dates, splits, spinoffs and conferences).

errorEvent (reqId: int, errorCode: int, errorString: str, contract: Contract): Emits the reqId/orderId and TWS error code and string (see https://interactivebrokers.github.io/tws-api/message_codes.html) together with the contract the error applies to (or None if no contract applies).

timeoutEvent (idlePeriod: float): Is emitted if no data is received for longer than the timeout period specified with setTimeout(). The value emitted is the period in seconds since the last update.

Note that it is not advisable to place new requests inside an event handler as it may lead to too much recursion.

Connect to a running TWS or IB gateway application. After the connection is made the client is fully synchronized and ready to serve requests.

This method is blocking.

host (str) – Host name or IP address.

port (int) – Port number.

clientId (int) – ID number to use for this client; must be unique per connection. Setting clientId=0 will automatically merge manual TWS trading with this client.

timeout (float) – If establishing the connection takes longer than timeout seconds then the asyncio.TimeoutError exception is raised. Set to 0 to disable timeout.

readonly (bool) – Set to True when API is in read-only mode.

account (str) – Main account to receive updates for.

raiseSyncErrors (bool) – When True this will cause an initialsync request error to raise a ConnectionError`. When False the error will only be logged at error level. fetchFields: By default, all account data is loaded and cachedwhen a new connection is made. You can optionally disable all or some of the account attribute fetching during a connection using the StartupFetch field flags. See StartupFetch in ib.py for member details. There is also StartupFetchNONE and StartupFetchALL as shorthand. Individual flag field members can be added or removed to the fetchFields parameter as needed.

sync request error to raise a ConnectionError`. When False the error will only be logged at error level.

when a new connection is made. You can optionally disable all or some of the account attribute fetching during a connection using the StartupFetch field flags. See StartupFetch in ib.py for member details. There is also StartupFetchNONE and StartupFetchALL as shorthand. Individual flag field members can be added or removed to the fetchFields parameter as needed.

Disconnect from a TWS or IB gateway application. This will clear all session state.

Is there an API connection to TWS or IB gateway?

By default run the event loop forever.

When awaitables (like Tasks, Futures or coroutines) are given then run the event loop until each has completed and return their results.

An optional timeout (in seconds) can be given that will raise asyncio.TimeoutError if the awaitables are not ready within the timeout period.

Schedule the callback to be run at the given time with the given arguments. This will return the Event Handle.

time (time | datetime) – Time to run callback. If given as datetime.time then use today as date.

callback (Callable) – Callable scheduled to run.

args – Arguments for to call callback with.

Wait for the given amount of seconds while everything still keeps processing in the background. Never use time.sleep().

secs (float) – Time in seconds to wait.

Iterator that waits periodically until certain time points are reached while yielding those time points.

start (time | datetime) – Start time, can be specified as datetime.datetime, or as datetime.time in which case today is used as the date

end (time | datetime) – End time, can be specified as datetime.datetime, or as datetime.time in which case today is used as the date

step (float) – The number of seconds of each period

Async version of timeRange().

AsyncIterator[datetime]

Wait until the given time t is reached.

t (time | datetime) – The time t can be specified as datetime.datetime, or as datetime.time in which case today is used as the date.

Wait on any new update to arrive from the network.

timeout (float) – Maximum time in seconds to wait. If 0 then no timeout is used.

A loop with waitOnUpdate should not be used to harvest tick data from tickers, since some ticks can go missing. This happens when multiple updates occur almost simultaneously; The ticks from the first update are then cleared. Use events instead to prevent this.

True if not timed-out, False otherwise.

Iterate until condition is met, with optional timeout in seconds. The yielded value is that of the condition or False when timed out.

condition – Predicate function that is tested after every network

timeout (float) – Maximum time in seconds to wait. If 0 then no timeout is used.

Set a timeout for receiving messages from TWS/IBG, emitting timeoutEvent if there is no incoming data for too long.

The timeout fires once per connected session but can be set again after firing or after a reconnect.

timeout (float) – Timeout in seconds.

List of account names.

List of account values for the given account, or of all accounts if account is left blank.

account (str) – If specified, filter for this account name.

List of account values for the given account, or of all accounts if account is left blank.

This method is blocking on first run, non-blocking after that.

account (str) – If specified, filter for this account name.

List of portfolio items for the given account, or of all retrieved portfolio items if account is left blank.

account (str) – If specified, filter for this account name.

List of positions for the given account, or of all accounts if account is left blank.

account (str) – If specified, filter for this account name.

List of subscribed PnL objects (profit and loss), optionally filtered by account and/or modelCode.

The PnL objects are kept live updated.

account – If specified, filter for this account name.

modelCode – If specified, filter for this account model.

List of subscribed PnLSingle objects (profit and loss for single positions).

The PnLSingle objects are kept live updated.

account (str) – If specified, filter for this account name.

modelCode (str) – If specified, filter for this account model.

conId (int) – If specified, filter for this contract ID.

List of all order trades from this session.

List of all open order trades.

List of all orders from this session.

List of all open orders.

List of all fills from this session.

List of all executions from this session.

Get ticker of the given contract. It must have been requested before with reqMktData with the same contract object. The ticker may not be ready yet if called directly after reqMktData().

contract (Contract) – Contract to get ticker for.

Get a list of all tickers.

Get a list of all tickers that have pending ticks or domTicks.

Get a list of all live updated bars. These can be 5 second realtime bars or live updated historical bars.

list[BarDataList | RealTimeBarList]

List of ticks with headline news. The article itself can be retrieved with reqNewsArticle().

List of IB news bulletins.

Request and return a list of snapshot tickers. The list is returned when all tickers are ready.

This method is blocking.

contracts (Contract) – Contracts to get tickers for.

regulatorySnapshot (bool) – Request NBBO snapshots (may incur a fee).

Fully qualify the given contracts in-place. This will fill in the missing fields in the contract, especially the conId.

Returns a list of contracts that have been successfully qualified.

This method is blocking.

contracts (Contract) – Contracts to qualify.

Create a limit order that is bracketed by a take-profit order and a stop-loss order. Submit the bracket like:

https://interactivebrokers.github.io/tws-api/bracket_order.html

action (str) – ‘BUY’ or ‘SELL’.

quantity (float) – Size of order.

limitPrice (float) – Limit price of entry order.

takeProfitPrice (float) – Limit price of profit order.

stopLossPrice (float) – Stop price of loss order.

Place the trades in the same One Cancels All (OCA) group.

https://interactivebrokers.github.io/tws-api/oca.html

orders (list[Order]) – The orders that are to be placed together.

Retrieve commission and margin impact without actually placing the order. The given order will not be modified in any way.

This method is blocking.

contract (Contract) – Contract to test.

order (Order) – Order to test.

Place a new order or modify an existing order. Returns a Trade that is kept live updated with status changes, fills, etc.

contract (Contract) – Contract to use for order.

order (Order) – The order to be placed.

Cancel the order and return the Trade it belongs to.

order (Order) – The order to be canceled.

manualCancelOrderTime (str) – For audit trail.

Cancel all active trades including those placed by other clients or TWS/IB gateway.

Request TWS current time.

This method is blocking.

This is called at startup - no need to call again.

Request account and portfolio values of the account and keep updated. Returns when both account values and portfolio are filled.

This method is blocking.

account (str) – If specified, filter for this account name.

It is recommended to use accountValues() instead.

Request account values of multiple accounts and keep updated.

This method is blocking.

account (str) – If specified, filter for this account name.

modelCode (str) – If specified, filter for this account model.

It is recommended to use accountSummary() instead.

Request account values for all accounts and keep them updated. Returns when account summary is filled.

This method is blocking.

Bind manual TWS orders so that they can be managed from this client. The clientId must be 0 and the TWS API setting “Use negative numbers to bind automatic orders” must be checked.

This request is automatically called when clientId=0.

https://interactivebrokers.github.io/tws-api/open_orders.html https://interactivebrokers.github.io/tws-api/modifying_orders.html

autoBind (bool) – Set binding on or off.

Request and return a list of open orders.

This method can give stale information where a new open order is not reported or an already filled or cancelled order is reported as open. It is recommended to use the more reliable and much faster openTrades() or openOrders() methods instead.

This method is blocking.

Request and return a list of all open orders over all clients. Note that the orders of other clients will not be kept in sync, use the master clientId mechanism instead to see other client’s orders that are kept in sync.

Request and return a list of completed trades.

apiOnly (bool) – Request only API orders (not manually placed TWS orders).

It is recommended to use fills() or executions() instead.

Request and return a list of fills.

This method is blocking.

execFilter (ExecutionFilter | None) – If specified, return executions that match the filter.

It is recommended to use positions() instead.

Request and return a list of positions for all accounts.

This method is blocking.

Start a subscription for profit and loss events.

Returns a PnL object that is kept live updated. The result can also be queried from pnl().

https://interactivebrokers.github.io/tws-api/pnl.html

account (str) – Subscribe to this account.

modelCode (str) – If specified, filter for this account model.

Cancel PnL subscription.

account – Cancel for this account.

modelCode (str) – If specified, cancel for this account model.

Start a subscription for profit and loss events for single positions.

Returns a PnLSingle object that is kept live updated. The result can also be queried from pnlSingle().

https://interactivebrokers.github.io/tws-api/pnl.html

account (str) – Subscribe to this account.

modelCode (str) – Filter for this account model.

conId (int) – Filter for this contract ID.

Cancel PnLSingle subscription for the given account, modelCode and conId.

account (str) – Cancel for this account name.

modelCode (str) – Cancel for this account model.

conId (int) – Cancel for this contract ID.

Get a list of contract details that match the given contract. If the returned list is empty then the contract is not known; If the list has multiple values then the contract is ambiguous.

The fully qualified contract is available in the the ContractDetails.contract attribute.

This method is blocking.

https://interactivebrokers.github.io/tws-api/contract_details.html

contract (Contract) – The contract to get details for.

list[ContractDetails]

Request contract descriptions of contracts that match a pattern.

This method is blocking.

https://interactivebrokers.github.io/tws-api/matching_symbols.html

pattern (str) – The first few letters of the ticker symbol, or for longer strings a character sequence matching a word in the security name.

list[ContractDescription]

Request price increments rule.

https://interactivebrokers.github.io/tws-api/minimum_increment.html

marketRuleId (int) – ID of market rule. The market rule IDs for a contract can be obtained via reqContractDetails() from ContractDetails.marketRuleIds, which contains a comma separated string of market rule IDs.

Request realtime 5 second bars.

https://interactivebrokers.github.io/tws-api/realtime_bars.html

contract (Contract) – Contract of interest.

barSize (int) – Must be 5.

whatToShow (str) – Specifies the source for constructing bars. Can be ‘TRADES’, ‘MIDPOINT’, ‘BID’ or ‘ASK’.

useRTH (bool) – If True then only show data from within Regular Trading Hours, if False then show all data.

realTimeBarsOptions (list[TagValue]) – Unknown.

Cancel the realtime bars subscription.

bars (RealTimeBarList) – The bar list that was obtained from reqRealTimeBars.

Request historical bar data.

This method is blocking.

https://interactivebrokers.github.io/tws-api/historical_bars.html

contract (Contract) – Contract of interest.

endDateTime (datetime | date | str | None) – Can be set to ‘’ to indicate the current time, or it can be given as a datetime.date or datetime.datetime, or it can be given as a string in ‘yyyyMMdd HH:mm:ss’ format. If no timezone is given then the TWS login timezone is used.

durationStr (str) – Time span of all the bars. Examples: ‘60 S’, ‘30 D’, ‘13 W’, ‘6 M’, ‘10 Y’.

barSizeSetting (str) – Time period of one bar. Must be one of: ‘1 secs’, ‘5 secs’, ‘10 secs’ 15 secs’, ‘30 secs’, ‘1 min’, ‘2 mins’, ‘3 mins’, ‘5 mins’, ‘10 mins’, ‘15 mins’, ‘20 mins’, ‘30 mins’, ‘1 hour’, ‘2 hours’, ‘3 hours’, ‘4 hours’, ‘8 hours’, ‘1 day’, ‘1 week’, ‘1 month’.

whatToShow (str) – Specifies the source for constructing bars. Must be one of: ‘TRADES’, ‘MIDPOINT’, ‘BID’, ‘ASK’, ‘BID_ASK’, ‘ADJUSTED_LAST’, ‘HISTORICAL_VOLATILITY’, ‘OPTION_IMPLIED_VOLATILITY’, ‘REBATE_RATE’, ‘FEE_RATE’, ‘YIELD_BID’, ‘YIELD_ASK’, ‘YIELD_BID_ASK’, ‘YIELD_LAST’. For ‘SCHEDULE’ use reqHistoricalSchedule().

useRTH (bool) – If True then only show data from within Regular Trading Hours, if False then show all data.

formatDate (int) – For an intraday request setting to 2 will cause the returned date fields to be timezone-aware datetime.datetime with UTC timezone, instead of local timezone as used by TWS.

keepUpToDate (bool) – If True then a realtime subscription is started to keep the bars updated; endDateTime must be set empty (‘’) then.

chartOptions (list[TagValue]) – Unknown.

timeout (float) – Timeout in seconds after which to cancel the request and return an empty bar series. Set to 0 to wait indefinitely.

Cancel the update subscription for the historical bars.

bars (BarDataList) – The bar list that was obtained from reqHistoricalData with a keepUpToDate subscription.

Request historical schedule.

This method is blocking.

contract (Contract) – Contract of interest.

numDays (int) – Number of days.

endDateTime (datetime | date | str | None) – Can be set to ‘’ to indicate the current time, or it can be given as a datetime.date or datetime.datetime, or it can be given as a string in ‘yyyyMMdd HH:mm:ss’ format. If no timezone is given then the TWS login timezone is used.

useRTH (bool) – If True then show schedule for Regular Trading Hours, if False then for extended hours.

Request historical ticks. The time resolution of the ticks is one second.

This method is blocking.

https://interactivebrokers.github.io/tws-api/historical_time_and_sales.html

contract (Contract) – Contract to query.

startDateTime (str | date) – Can be given as a datetime.date or datetime.datetime, or it can be given as a string in ‘yyyyMMdd HH:mm:ss’ format. If no timezone is given then the TWS login timezone is used.

endDateTime (str | date) – One of startDateTime or endDateTime can be given, the other must be blank.

numberOfTicks (int) – Number of ticks to request (1000 max). The actual result can contain a bit more to accommodate all ticks in the latest second.

whatToShow (str) – One of ‘Bid_Ask’, ‘Midpoint’ or ‘Trades’.

useRTH – If True then only show data from within Regular Trading Hours, if False then show all data.

ignoreSize (bool) – Ignore bid/ask ticks that only update the size.

miscOptions (list[TagValue]) – Unknown.

Set the market data type used for reqMktData().

marketDataType (int) – One of: 1 = Live 2 = Frozen 3 = Delayed 4 = Delayed frozen

https://interactivebrokers.github.io/tws-api/market_data_type.html

Get the datetime of earliest available historical data for the contract.

contract (Contract) – Contract of interest.

useRTH (bool) – If True then only show data from within Regular Trading Hours, if False then show all data.

formatDate (int) – If set to 2 then the result is returned as a timezone-aware datetime.datetime with UTC timezone.

Subscribe to tick data or request a snapshot. Returns the Ticker that holds the market data. The ticker will initially be empty and gradually (after a couple of seconds) be filled.

https://interactivebrokers.github.io/tws-api/md_request.html

contract (Contract) – Contract of interest.

genericTickList (str) – Comma separated IDs of desired generic ticks that will cause corresponding Ticker fields to be filled: ID Ticker fields 100 putVolume, callVolume (for options) 101 putOpenInterest, callOpenInterest (for options) 104 histVolatility (for options) 105 avOptionVolume (for options) 106 impliedVolatility (for options) 162 indexFuturePremium 165 low13week, high13week, low26week, high26week, low52week, high52week, avVolume 221 markPrice 225 auctionVolume, auctionPrice, auctionImbalance 233 last, lastSize, rtVolume, rtTime, vwap (Time & Sales) 236 shortableShares 258 fundamentalRatios (of type ib_async.objects.FundamentalRatios) 293 tradeCount 294 tradeRate 295 volumeRate 375 rtTradeVolume 411 rtHistVolatility 456 dividends (of type ib_async.objects.Dividends) 588 futuresOpenInterest

Comma separated IDs of desired generic ticks that will cause corresponding Ticker fields to be filled:

putVolume, callVolume (for options)

putOpenInterest, callOpenInterest (for options)

histVolatility (for options)

avOptionVolume (for options)

impliedVolatility (for options)

low13week, high13week, low26week, high26week, low52week, high52week, avVolume

auctionVolume, auctionPrice, auctionImbalance

last, lastSize, rtVolume, rtTime, vwap (Time & Sales)

fundamentalRatios (of type ib_async.objects.FundamentalRatios)

dividends (of type ib_async.objects.Dividends)

snapshot (bool) – If True then request a one-time snapshot, otherwise subscribe to a stream of realtime tick data.

regulatorySnapshot (bool) – Request NBBO snapshot (may incur a fee).

mktDataOptions (list[TagValue]) – Unknown

Unsubscribe from realtime streaming tick data.

contract (Contract) – The contract of a previously subscribed ticker to unsubscribe.

Returns True if cancel was successful. Returns False if ‘contract’ was not found.

Subscribe to tick-by-tick data and return the Ticker that holds the ticks in ticker.tickByTicks.

https://interactivebrokers.github.io/tws-api/tick_data.html

contract (Contract) – Contract of interest.

tickType (str) – One of ‘Last’, ‘AllLast’, ‘BidAsk’ or ‘MidPoint’.

numberOfTicks (int) – Number of ticks or 0 for unlimited.

ignoreSize (bool) – Ignore bid/ask ticks that only update the size.

Unsubscribe from tick-by-tick data

contract (Contract) – The contract of a previously subscribed ticker to unsubscribe.

Returns True if cancel was successful. Returns False if ‘contract’ was not found.

Obtain mapping from single letter codes to exchange names.

Note: The exchanges must be open when using this request, otherwise an empty list is returned.

Get those exchanges that have have multiple market makers (and have ticks returned with marketMaker info).

list[DepthMktDataDescription]

Subscribe to market depth data (a.k.a. DOM, L2 or order book).

https://interactivebrokers.github.io/tws-api/market_depth.html

contract (Contract) – Contract of interest.

numRows (int) – Number of depth level on each side of the order book (5 max).

isSmartDepth (bool) – Consolidate the order book across exchanges.

mktDepthOptions – Unknown.

The Ticker that holds the market depth in ticker.domBids and ticker.domAsks and the list of MktDepthData in ticker.domTicks.

Unsubscribe from market depth data.

contract (Contract) – The exact contract object that was used to subscribe with.

Request histogram data.

This method is blocking.

https://interactivebrokers.github.io/tws-api/histograms.html

contract (Contract) – Contract to query.

useRTH (bool) – If True then only show data from within Regular Trading Hours, if False then show all data.

period (str) – Period of which data is being requested, for example ‘3 days’.

Get fundamental data of a contract in XML format.

This method is blocking.

https://interactivebrokers.github.io/tws-api/fundamentals.html

contract (Contract) – Contract to query.

reportType (str) – ‘ReportsFinSummary’: Financial summary ’ReportsOwnership’: Company’s ownership ’ReportSnapshot’: Company’s financial overview ’ReportsFinStatements’: Financial Statements ’RESC’: Analyst Estimates ’CalendarReport’: Company’s calendar

‘ReportsFinSummary’: Financial summary

’ReportsOwnership’: Company’s ownership

’ReportSnapshot’: Company’s financial overview

’ReportsFinStatements’: Financial Statements

’RESC’: Analyst Estimates

’CalendarReport’: Company’s calendar

fundamentalDataOptions (list[TagValue]) – Unknown

Do a blocking market scan by starting a subscription and canceling it after the initial list of results are in.

This method is blocking.

https://interactivebrokers.github.io/tws-api/market_scanners.html

subscription (ScannerSubscription) – Basic filters.

scannerSubscriptionOptions (list[TagValue]) – Unknown.

scannerSubscriptionFilterOptions (list[TagValue]) – Advanced generic filters.

Subscribe to market scan data.

https://interactivebrokers.github.io/tws-api/market_scanners.html

subscription (ScannerSubscription) – What to scan for.

scannerSubscriptionOptions (list[TagValue]) – Unknown.

scannerSubscriptionFilterOptions (list[TagValue]) – Unknown.

Cancel market data subscription.

https://interactivebrokers.github.io/tws-api/market_scanners.html

dataList (ScanDataList) – The scan data list that was obtained from reqScannerSubscription().

Requests an XML list of scanner parameters.

This method is blocking.

Calculate the volatility given the option price.

This method is blocking.

https://interactivebrokers.github.io/tws-api/option_computations.html

contract (Contract) – Option contract.

optionPrice (float) – Option price to use in calculation.

underPrice (float) – Price of the underlier to use in calculation

implVolOptions (list[TagValue]) – Unknown

Calculate the option price given the volatility.

This method is blocking.

https://interactivebrokers.github.io/tws-api/option_computations.html

contract (Contract) – Option contract.

volatility (float) – Option volatility to use in calculation.

underPrice (float) – Price of the underlier to use in calculation

implVolOptions – Unknown

Get the option chain.

This method is blocking.

https://interactivebrokers.github.io/tws-api/options.html

underlyingSymbol (str) – Symbol of underlier contract.

futFopExchange (str) – Exchange (only for FuturesOption, otherwise leave blank).

underlyingSecType (str) – The type of the underlying security, like ‘STK’ or ‘FUT’.

underlyingConId (int) – conId of the underlying contract.

Exercise an options contract.

https://interactivebrokers.github.io/tws-api/options.html

contract (Contract) – The option contract to be exercised.

exerciseAction (int) – 1 = exercise the option 2 = let the option lapse

1 = exercise the option

2 = let the option lapse

exerciseQuantity (int) – Number of contracts to be exercised.

account (str) – Destination account.

override (int) – 0 = no override 1 = override the system’s natural action

1 = override the system’s natural action

Get a list of news providers.

This method is blocking.

Get the body of a news article.

This method is blocking.

https://interactivebrokers.github.io/tws-api/news.html

providerCode (str) – Code indicating news provider, like ‘BZ’ or ‘FLY’.

articleId (str) – ID of the specific article.

newsArticleOptions (list[TagValue]) – Unknown.

Get historical news headline.

https://interactivebrokers.github.io/tws-api/news.html

This method is blocking.

conId (int) – Search news articles for contract with this conId.

providerCodes (str) – A ‘+’-separated list of provider codes, like ‘BZ+FLY’.

startDateTime (str | date) – The (exclusive) start of the date range. Can be given as a datetime.date or datetime.datetime, or it can be given as a string in ‘yyyyMMdd HH:mm:ss’ format. If no timezone is given then the TWS login timezone is used.

endDateTime (str | date) – The (inclusive) end of the date range. Can be given as a datetime.date or datetime.datetime, or it can be given as a string in ‘yyyyMMdd HH:mm:ss’ format. If no timezone is given then the TWS login timezone is used.

totalResults (int) – Maximum number of headlines to fetch (300 max).

historicalNewsOptions (list[TagValue]) – Unknown.

Subscribe to IB news bulletins.

https://interactivebrokers.github.io/tws-api/news.html

allMessages (bool) – If True then fetch all messages for the day.

Cancel subscription to IB news bulletins.

Requests to change the FA configuration.

This method is blocking.

faDataType (int) – 1 = Groups: Offer traders a way to create a group of accounts and apply a single allocation method to all accounts in the group. 2 = Profiles: Let you allocate shares on an account-by-account basis using a predefined calculation value. 3 = Account Aliases: Let you easily identify the accounts by meaningful names rather than account numbers.

1 = Groups: Offer traders a way to create a group of accounts and apply a single allocation method to all accounts in the group.

2 = Profiles: Let you allocate shares on an account-by-account basis using a predefined calculation value.

3 = Account Aliases: Let you easily identify the accounts by meaningful names rather than account numbers.

Replaces Financial Advisor’s settings.

faDataType (int) – See requestFA().

xml (str) – The XML-formatted configuration string.

Request Wall Street Horizon metadata.

https://interactivebrokers.github.io/tws-api/fundamentals.html

Request Wall Street Horizon event data.

reqWshMetaData() must have been called first before using this method.

data (WshEventData) – Filters for selecting the corporate event data.

https://interactivebrokers.github.io/tws-api/wshe_filters.html

Cancel active WHS event data.

Blocking convenience method that returns the WSH metadata (that is the available filters and event types) as a JSON string.

Please note that a Wall Street Horizon subscription is required.

Blocking convenience method that returns the WSH event data as a JSON string. getWshMetaData() must have been called first before using this method.

Please note that a Wall Street Horizon subscription is required.

Get the White Branding ID of the user.

Looks up all contract details, but only returns matching Contract objects.

If ‘returnAll’ is True, instead of returning ‘None’ on an ambiguous contract request, the return slot will have a list of the matching contracts. Previously the conflicts were only sent to the log, which isn’t useful if you are logging to a file and not watching immediately.

list[Contract | list[Contract | None] | None]

cannot be qualified (bad values, ambiguous), the return value for the contract position in the result is None.

Awaitable[OrderState]

Awaitable[list[Trade]]

Awaitable[list[Trade]]

Awaitable[list[Trade]]

Awaitable[list[Fill]]

Awaitable[list[Position]]

Awaitable[list[ContractDetails]]

list[ContractDescription] | None

list[PriceIncrement] | None

Awaitable[HistoricalSchedule]

Awaitable[list[DepthMktDataDescription]]

Awaitable[list[HistogramData]]

OptionComputation | None

OptionComputation | None

Awaitable[list[OptionChain]]

Awaitable[list[NewsProvider]]

Awaitable[NewsArticle]

HistoricalNews | None

Socket client for communicating with Interactive Brokers.

Replacement for ibapi.client.EClient that uses asyncio.

The client is fully asynchronous and has its own event-driven networking code that replaces the networking code of the standard EClient. It also replaces the infinite loop of EClient.run() with the asyncio event loop. It can be used as a drop-in replacement for the standard EClient as provided by IBAPI.

Compared to the standard EClient this client has the following additional features:

client.connect() will block until the client is ready to serve requests; It is not necessary to wait for nextValidId to start requests as the client has already done that. The reqId is directly available with getReqId().

client.connectAsync() is a coroutine for connecting asynchronously.

When blocking, client.connect() can be made to time out with the timeout parameter (default 2 seconds).

Optional wrapper.priceSizeTick(reqId, tickType, price, size) that combines price and size instead of the two wrapper methods priceTick and sizeTick.

Automatic request throttling.

Optional wrapper.tcpDataArrived() method; If the wrapper has this method it is invoked directly after a network packet has arrived. A possible use is to timestamp all data in the packet with the exact same time.

Optional wrapper.tcpDataProcessed() method; If the wrapper has this method it is invoked after the network packet’s data has been handled. A possible use is to write or evaluate the newly arrived data in one batch instead of item by item.

MaxRequests (int) – Throttle the number of requests to MaxRequests per RequestsInterval seconds. Set to 0 to disable throttling.

RequestsInterval (float) – Time interval (in seconds) for request throttling.

MinClientVersion (int) – Client protocol version.

MaxClientVersion (int) – Client protocol version.

apiError (errorMsg: str)

Is the API connection up and running?

Get statistics about the connection.

Update the next reqId to be at least minReqId.

Get the list of account names that are under management.

Set additional connect options.

connectOptions (str) – Use “+PACEAPI” to use request-pacing built into TWS/gateway 974+ (obsolete).

Connect to a running TWS or IB gateway application.

host (str) – Host name or IP address.

port (int) – Port number.

clientId (int) – ID number to use for this client; must be unique per connection.

timeout (float | None) – If establishing the connection takes longer than timeout seconds then the asyncio.TimeoutError exception is raised. Set to 0 to disable timeout.

Disconnect from IB connection.

Serialize and send the given fields using the IB socket protocol.

if ‘makeEmpty’ is True (default), then the IBKR values representing “no value” become the empty string.

Order types used by Interactive Brokers.

Order for trading contracts.

https://interactivebrokers.github.io/tws-api/available_orders.html

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Helper property to return the total size of this requested order.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Convert the numeric values of this OrderState into a new OrderState transformed by ‘using’

Return a new OrderState with the current values values to floats instead of strings as returned from IBKR directly.

Return a new OrderState with the current values as formatted strings.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Just a type helper for mypy to check against if you convert OrderState to .numeric().

state_numeric: OrderStateNumeric = state.numeric(digits=2)

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Trade keeps track of an order, its status and all its fills.

statusEvent (trade: Trade)

modifyEvent (trade: Trade)

fillEvent (trade: Trade, fill: Fill)

commissionReportEvent (trade: Trade, fill: Fill, commissionReport: CommissionReport)

filledEvent (trade: Trade)

cancelEvent (trade: Trade)

cancelledEvent (trade: Trade)

True if sent to IBKR but not “Submitted” for live execution yet.

True if sent to IBKR but not “Submitted” for live execution yet.

True if eligible for execution, false otherwise.

True if completely filled or cancelled, false otherwise.

Number of shares filled.

Number of shares remaining to be filled.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Create new instance of BracketOrder(parent, takeProfit, stopLoss)

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Financial instrument types used by Interactive Brokers.

Contract(**kwargs) can create any contract using keyword arguments. To simplify working with contracts, there are also more specialized contracts that take optional positional arguments. Some examples:

conId (int) – The unique IB contract identifier.

symbol (str) – The contract (or its underlying) symbol.

secType (str) – The security type: ’STK’ = Stock (or ETF) ’OPT’ = Option ’FUT’ = Future ’IND’ = Index ’FOP’ = Futures option ’CASH’ = Forex pair ’CFD’ = CFD ’BAG’ = Combo ’WAR’ = Warrant ’BOND’ = Bond ’CMDTY’ = Commodity ’NEWS’ = News ’FUND’ = Mutual fund ’CRYPTO’ = Crypto currency ’EVENT’ = Bet on an event

’STK’ = Stock (or ETF)

’FOP’ = Futures option

’CRYPTO’ = Crypto currency

’EVENT’ = Bet on an event

lastTradeDateOrContractMonth (str) – The contract’s last trading day or contract month (for Options and Futures). Strings with format YYYYMM will be interpreted as the Contract Month whereas YYYYMMDD will be interpreted as Last Trading Day.

strike (float) – The option’s strike price.

right (str) – Put or Call. Valid values are ‘P’, ‘PUT’, ‘C’, ‘CALL’, or ‘’ for non-options.

multiplier (str) – The instrument’s multiplier (i.e. options, futures).

exchange (str) – The destination exchange.

currency (str) – The underlying’s currency.

localSymbol (str) – The contract’s symbol within its primary exchange. For options, this will be the OCC symbol.

primaryExchange (str) – The contract’s primary exchange. For smart routed contracts, used to define contract in case of ambiguity. Should be defined as native exchange of contract, e.g. ISLAND for MSFT. For exchanges which contain a period in name, will only be part of exchange name prior to period, i.e. ENEXT for ENEXT.BE.

tradingClass (str) – The trading class name for this contract. Available in TWS contract description window as well. For example, GBL Dec ‘13 future’s trading class is “FGBL”.

includeExpired (bool) – If set to true, contract details requests and historical data queries can be performed pertaining to expired futures contracts. Expired options or other instrument types are not available.

secIdType (str) – Security identifier type. Examples for Apple: secIdType=’ISIN’, secId=’US0378331005’ secIdType=’CUSIP’, secId=’037833100’

Security identifier type. Examples for Apple:

secIdType=’ISIN’, secId=’US0378331005’

secIdType=’CUSIP’, secId=’037833100’

secId (str) – Security identifier.

comboLegsDescription (str) – Description of the combo legs.

comboLegs (List[ComboLeg]) – The legs of a combined contract definition.

deltaNeutralContract (DeltaNeutralContract) – Delta and underlying price for Delta-Neutral combo orders.

Create and a return a specialized contract based on the given secType, or a general Contract if secType is not given.

Comply an existing generic Contract into its most specific type.

See if this contract can be hashed by conId.

but we generate a synthetic hash for them based on leg details instead.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

symbol (str) – Symbol name.

exchange (str) – Destination exchange.

currency (str) – Underlying currency.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

symbol (str) – Symbol name.

lastTradeDateOrContractMonth (str) – The option’s last trading day or contract month. YYYYMM format: To specify last month YYYYMMDD format: To specify last trading day

The option’s last trading day or contract month.

YYYYMM format: To specify last month

YYYYMMDD format: To specify last trading day

strike (float) – The option’s strike price.

right (str) – Put or call option. Valid values are ‘P’, ‘PUT’, ‘C’ or ‘CALL’.

exchange (str) – Destination exchange.

multiplier (str) – The contract multiplier.

currency (str) – Underlying currency.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

symbol (str) – Symbol name.

lastTradeDateOrContractMonth (str) – The option’s last trading day or contract month. YYYYMM format: To specify last month YYYYMMDD format: To specify last trading day

The option’s last trading day or contract month.

YYYYMM format: To specify last month

YYYYMMDD format: To specify last trading day

exchange (str) – Destination exchange.

localSymbol (str) – The contract’s symbol within its primary exchange.

multiplier (str) – The contract multiplier.

currency (str) – Underlying currency.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Continuous future contract.

symbol (str) – Symbol name.

exchange (str) – Destination exchange.

localSymbol (str) – The contract’s symbol within its primary exchange.

multiplier (str) – The contract multiplier.

currency (str) – Underlying currency.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Foreign exchange currency pair.

pair (str) – Shortcut for specifying symbol and currency, like ‘EURUSD’.

exchange (str) – Destination exchange.

symbol (str) – Base currency.

currency (str) – Quote currency.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

symbol (str) – Symbol name.

exchange (str) – Destination exchange.

currency (str) – Underlying currency.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Contract For Difference.

symbol (str) – Symbol name.

exchange (str) – Destination exchange.

currency (str) – Underlying currency.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

symbol (str) – Symbol name.

exchange (str) – Destination exchange.

currency (str) – Underlying currency.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Option on a futures contract.

symbol (str) – Symbol name.

lastTradeDateOrContractMonth (str) – The option’s last trading day or contract month. YYYYMM format: To specify last month YYYYMMDD format: To specify last trading day

The option’s last trading day or contract month.

YYYYMM format: To specify last month

YYYYMMDD format: To specify last trading day

strike (float) – The option’s strike price.

right (str) – Put or call option. Valid values are ‘P’, ‘PUT’, ‘C’ or ‘CALL’.

exchange (str) – Destination exchange.

multiplier (str) – The contract multiplier.

currency (str) – Underlying currency.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Crypto currency contract.

symbol (str) – Symbol name.

exchange (str) – Destination exchange.

currency (str) – Underlying currency.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Create new instance of TagValue(tag, value)

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Create new instance of TradingSession(start, end)

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Access to realtime market information.

Current market data such as bid, ask, last price, etc. for a contract.

Streaming level-1 ticks of type TickData are stored in the ticks list.

Streaming level-2 ticks of type MktDepthData are stored in the domTicks list. The order book (DOM) is available as lists of DOMLevel in domBids and domAsks.

Streaming tick-by-tick ticks are stored in tickByTicks.

For options the OptionComputation values for the bid, ask, resp. last price are stored in the bidGreeks, askGreeks resp. lastGreeks attributes. There is also modelGreeks that conveys the greeks as calculated by Interactive Brokers’ option model.

updateEvent (ticker: Ticker)

See if this ticker has a valid bid and ask.

Return average of bid and ask, or defaults.unset if no valid bid and ask are available.

Return the first available one of :rtype: float

last price if within current bid/ask or no bid/ask available;

average of bid and ask (midpoint).

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Emit bid and ask ticks.

Tick filtering event operators that emit(time, price, size).

Emit a new value to all connected listeners.

args – Argument values to emit to listeners.

Aggregate ticks into time bars, where the timing of new bars is derived from a timer event. Emits a completed Bar.

This event stores a BarList of all created bars in the bars property.

timer (Event) – Event for timing when a new bar starts.

Aggregate ticks into bars that have the same number of ticks. Emits a completed Bar.

This event stores a BarList of all created bars in the bars property.

count (int) – Number of ticks to use to form one bar.

Aggregate ticks into bars that have the same volume. Emits a completed Bar.

This event stores a BarList of all created bars in the bars property.

count – Number of ticks to use to form one bar.

Emit a new value to all connected listeners.

args – Argument values to emit to listeners.

Aggregate ticks into time bars, where the timing of new bars is derived from a timer event. Emits a completed Bar.

This event stores a BarList of all created bars in the bars property.

timer – Event for timing when a new bar starts.

Emit a new value to all connected listeners.

args – Argument values to emit to listeners.

Aggregate ticks into bars that have the same number of ticks. Emits a completed Bar.

This event stores a BarList of all created bars in the bars property.

count – Number of ticks to use to form one bar.

Emit a new value to all connected listeners.

args – Argument values to emit to listeners.

Aggregate ticks into bars that have the same volume. Emits a completed Bar.

This event stores a BarList of all created bars in the bars property.

count – Number of ticks to use to form one bar.

Emit a new value to all connected listeners.

args – Argument values to emit to listeners.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Create new instance of AccountValue(account, tag, value, currency, modelCode)

Create new instance of TickData(time, tickType, price, size)

Create new instance of HistoricalTick(time, price, size)

Create new instance of HistoricalTickBidAsk(time, tickAttribBidAsk, priceBid, priceAsk, sizeBid, sizeAsk)

Create new instance of HistoricalTickLast(time, tickAttribLast, price, size, exchange, specialConditions)

Create new instance of TickByTickAllLast(tickType, time, price, size, tickAttribLast, exchange, specialConditions)

Create new instance of TickByTickBidAsk(time, bidPrice, askPrice, bidSize, askSize, tickAttribBidAsk)

Create new instance of TickByTickMidPoint(time, midPoint)

Create new instance of MktDepthData(time, position, marketMaker, operation, side, price, size)

Create new instance of DOMLevel(price, size, marketMaker)

Create new instance of PriceIncrement(lowEdge, increment)

Create new instance of PortfolioItem(contract, position, marketPrice, marketValue, averageCost, unrealizedPNL, realizedPNL, account)

Create new instance of Position(account, contract, position, avgCost)

Create new instance of Fill(contract, execution, commissionReport, time)

Exchange for Physical (EFP) futures data.

EFP allows trading a position in a single stock for a position in the corresponding single stock future.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

List of BarData that also stores all request parameters.

updateEvent (bars: BarDataList, hasNewBar: bool)

List of RealTimeBar that also stores all request parameters.

updateEvent (bars: RealTimeBarList, hasNewBar: bool)

List of ScanData that also stores all request parameters.

updateEvent (ScanDataList)

See: https://web.archive.org/web/20200725010343/https://interactivebrokers.github.io/tws-api/fundamental_ratios_tags.html

A simple way to provide default values when populating API data.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Exception to raise when the API reports an error that can be tied to a single request.

reqId (int) – Original request ID.

code (int) – Original error code.

message (str) – Original error message.

Event to emit global exceptions.

Create pandas DataFrame from the sequence of same-type objects.

labels (list[str] | None) – If supplied, retain only the given labels and drop the rest.

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

For a dataclass instance get the fields that are different from the default values and return as dict.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Provide a culled representation of the given dataclass instance, showing only the fields with a non-default value.

From https://stackoverflow.com/a/2166841/6067848

Convert object to a tree of lists, dicts and simple values. The result can be serialized to JSON.

Create candlestick plot for the given bars. The bars can be given as a DataFrame or as a list of bar objects.

Allow Control-C to end program.

Create a log handler that logs to the given file.

Create a log handler that logs to the console.

Format the integer or float n to 3 significant digits + SI prefix.

Context manager for timing.

By default run the event loop forever.

When awaitables (like Tasks, Futures or coroutines) are given then run the event loop until each has completed and return their results.

An optional timeout (in seconds) can be given that will raise asyncio.TimeoutError if the awaitables are not ready within the timeout period.

Schedule the callback to be run at the given time with the given arguments. This will return the Event Handle.

time (time | datetime) – Time to run callback. If given as datetime.time then use today as date.

callback (Callable) – Callable scheduled to run.

args – Arguments for to call callback with.

Wait for the given amount of seconds while everything still keeps processing in the background. Never use time.sleep().

secs (float) – Time in seconds to wait.

Iterator that waits periodically until certain time points are reached while yielding those time points.

start (time | datetime) – Start time, can be specified as datetime.datetime, or as datetime.time in which case today is used as the date

end (time | datetime) – End time, can be specified as datetime.datetime, or as datetime.time in which case today is used as the date

step (float) – The number of seconds of each period

Wait until the given time t is reached.

t (time | datetime) – The time t can be specified as datetime.datetime, or as datetime.time in which case today is used as the date.

Async version of timeRange().

AsyncIterator[datetime]

Async version of waitUntil().

Patch asyncio to allow nested event loops.

Get asyncio event loop with smart fallback handling.

This function is designed for use in synchronous contexts or when the execution context is unknown. It will: 1. Try to get the currently running event loop (if in async context) 2. Fall back to getting the current thread’s event loop via policy 3. Create a new event loop if none exists or if the existing one is closed

For performance-critical async code paths, prefer using asyncio.get_running_loop() directly instead of this function.

Note: This function does NOT cache the loop to avoid stale loop bugs when loops are closed and recreated (e.g., in testing, Jupyter notebooks).

Use nested asyncio event loop for Jupyter notebooks.

Run combined Qt5/asyncio event loop.

qtLib (str) – Name of Qt library to use: PyQt5 PyQt6 PySide2 PySide6

Name of Qt library to use:

period (float) – Period in seconds to poll Qt.

Format date or datetime to string that IB uses.

Parse string in IB date or datetime format to datetime.

Access to account statement webservice.

//www.interactivebrokers.com/campus/ibkr-api-page/flex-web-service/#flex-generate-report

Click on “Configure Flex Web Service”

Download a report by giving a valid token and queryId, or load from file by giving a valid path.

To overwrite default URL, set env variable IB_FLEXREPORT_URL.

Get the set of topics that can be extracted from this report.

Extract items of given topic and return as list of objects.

The topic is a string like TradeConfirm, ChangeInDividendAccrual, Order, etc.

Same as extract but return the result as a pandas DataFrame.

Generate flexreport URL.

Download report for the given token and queryId.

Load report from XML file.

Save report to XML file.

Programmatic control over starting and stopping TWS/Gateway using IBC (https://github.com/IbcAlpha/IBC).

twsVersion (int) – (required) The major version number for TWS or gateway.

gateway (bool) – True = gateway False = TWS

tradingMode (str) – ‘live’ or ‘paper’.

userid (str) – IB account username. It is recommended to set the real username/password in a secured IBC config file.

password (str) – IB account password.

twsPath (str) – Path to the TWS installation folder. Defaults: Linux: ~/Jts OS X: ~/Applications Windows: C:\Jts

Path to the TWS installation folder. Defaults:

twsSettingsPath (str) – Path to the TWS settings folder. Defaults: Linux: ~/Jts OS X: ~/Jts Windows: Not available

Path to the TWS settings folder. Defaults:

Windows: Not available

ibcPath (str) – Path to the IBC installation folder. Defaults: Linux: /opt/ibc OS X: /opt/ibc Windows: C:\IBC

Path to the IBC installation folder. Defaults:

ibcIni (str) – Path to the IBC configuration file. Defaults: Linux: ~/ibc/config.ini OS X: ~/ibc/config.ini Windows: %%HOMEPATH%%\DocumentsIBC\config.ini

Path to the IBC configuration file. Defaults:

Linux: ~/ibc/config.ini

OS X: ~/ibc/config.ini

Windows: %%HOMEPATH%%\DocumentsIBC\config.ini

javaPath (str) – Path to Java executable. Default is to use the Java VM included with TWS/gateway.

fixuserid (str) – FIX account user id (gateway only).

fixpassword (str) – FIX account password (gateway only).

on2fatimeout (str) – What to do if 2-factor authentication times out; Can be ‘restart’ or ‘exit’.

This is not intended to be run in a notebook.

To use IBC on Windows, the proactor (or quamash) event loop must have been set:

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

Start, connect and watch over the TWS or gateway app and try to keep it up and running. It is intended to be used in an event-driven application that properly initializes itself upon (re-)connect.

It is not intended to be used in a notebook or in imperative-style code. Do not expect Watchdog to magically shield you from reality. Do not use Watchdog unless you understand what it does and doesn’t do.

controller (IBC) – (required) IBC instance.

ib (IB) – (required) IB instance to be used. Do not connect this instance as Watchdog takes care of that.

host (str) – Used for connecting IB instance.

port (int) – Used for connecting IB instance.

clientId (int) – Used for connecting IB instance.

connectTimeout (float) – Used for connecting IB instance.

readonly (bool) – Used for connecting IB instance.

appStartupTime (float) – Time (in seconds) that the app is given to start up. Make sure that it is given ample time.

appTimeout (float) – Timeout (in seconds) for network traffic idle time.

retryDelay (float) – Time (in seconds) to restart app after a previous failure.

probeContract (Contract) – Contract to use for historical data probe requests (default is EURUSD).

probeTimeout (float); Timeout (in seconds)

The idea is to wait until there is no traffic coming from the app for a certain amount of time (the appTimeout parameter). This triggers a historical request to be placed just to see if the app is still alive and well. If yes, then continue, if no then restart the whole app and reconnect. Restarting will also occur directly on errors 1100 and 100.

startingEvent (watchdog: Watchdog)

startedEvent (watchdog: Watchdog)

stoppingEvent (watchdog: Watchdog)

stoppedEvent (watchdog: Watchdog)

softTimeoutEvent (watchdog: Watchdog)

hardTimeoutEvent (watchdog: Watchdog)

Return dataclass values as dict. This is a non-recursive variant of dataclasses.asdict.

For a dataclass instance get the fields that are different from the default values and return as dict.

Return dataclass values as tuple. This is a non-recursive variant of dataclasses.astuple.

Update fields of the given dataclass object from zero or more dataclass source objects and/or from keyword arguments.

---

## ib_async — ib_async 2.1.0 documentation

**URL:** https://ib-api-reloaded.github.io/ib_async/readme.html

**Contents:**
- ib_async
- Update
- Introduction
  - What You Can Build
  - Key Features
- Installation
- Build Manually
  - Installing Only Library
  - Install Everything (enable docs + dev testing)
- Generate Docs

ib_async is a Python library that provides a clean, modern interface to Interactive Brokers’ Trader Workstation (TWS) and IB Gateway. It handles the complexities of the IBKR API so you can focus on building trading applications, research tools, and market data analysis.

Market Data Applications: Stream live quotes, historical data, and market depth

Trading Systems: Place, modify, and monitor orders programmatically

Portfolio Tools: Track positions, account balances, and P&L in real-time

Research Platforms: Analyze contract details, option chains, and fundamental data

Risk Management: Monitor exposures and implement automated controls

Simple and Intuitive: Write straightforward Python code without dealing with callback complexity

Automatic Synchronization: The IB component stays in sync with TWS/Gateway automatically

Async-Ready: Built on asyncio and eventkit for high-performance applications

Jupyter-Friendly: Interactive development with live data in notebooks

Production-Ready: Robust error handling, reconnection logic, and comprehensive logging

Be sure to take a look at the notebooks, the recipes and the API docs.

Python 3.10 or higher

We plan to support Python releases 2 years back which allows us to continue adding newer features and performance improvements over time.

A running IB Gateway application (or TWS with API mode enabled)

stable gateway — updated every few months

latest gateway — updated weekly

Make sure the API port is enabled and ‘Download open orders on connection’ is checked.

You may also want to increase the Java memory usage under Configure->Settings->Memory Allocation to 4096 MB minimum to prevent gateway crashes when loading bulk data.

The ibapi package from IB is not needed. ib_async implements the full IBKR API binary protocol internally.

First, install poetry:

IB Gateway (Stable) — Updated every few months, more stable

IB Gateway (Latest) — Updated weekly, newest features

Trader Workstation (TWS) — Full trading platform

Enable API: Go to Configure → API → Settings and check “Enable ActiveX and Socket Clients”

Set Port: Default ports are 7497 (TWS) and 4001 (Gateway). You can change these if needed.

Allow Connections: Add 127.0.0.1 to “Trusted IPs” if connecting locally

Download Orders: Check “Download open orders on connection” to see existing orders

Memory: Go to Configure → Settings → Memory Allocation and set to 4096 MB minimum to prevent crashes with bulk data

Timeouts: Increase API timeout settings if you experience disconnections during large data requests

ib_async.ib.IB - Main interface class

Connection management (connect(), disconnect(), connectAsync())

Market data requests (reqMktData(), reqHistoricalData())

Order management (placeOrder(), cancelOrder())

Account data (positions(), accountSummary(), reqPnL())

ib_async.contract - Financial instruments

Stock, Option, Future, Forex, Index, Bond

Contract - Base class for all instruments

ComboLeg, DeltaNeutralContract - Complex instruments

ib_async.order - Order types and management

MarketOrder, LimitOrder, StopOrder, StopLimitOrder

Order - Base order class with all parameters

OrderStatus, OrderState - Order execution tracking

Trade - Complete order lifecycle tracking

ib_async.ticker - Real-time market data

Ticker - Live quotes, trades, and market data

Automatic field updates (bid, ask, last, volume, etc.)

Event-driven updates via updateEvent

ib_async.objects - Data structures

BarData - Historical price bars

Position - Portfolio positions

PortfolioItem - Portfolio details with P&L

AccountValue - Account metrics

Synchronous vs Asynchronous

The complete API documentation.

Clone the repository:

Install dependencies:

Make your changes and run tests:

Submit a pull request with:

Clear description of changes

Tests for new functionality

Updated documentation if needed

Follow existing code style (enforced by ruff)

Add tests for new features

Update documentation for user-facing changes

Keep commits focused and well-described

Be responsive to code review feedback

If you have other public work related to ib_async or ib_insync open an issue and we can keep an active list here.

Projects below are not endorsed by any entity and are purely for reference or entertainment purposes.

Adi’s livestream VODs about using IBKR APIs: Interactive Brokers API in Python

Matt’s IBKR python CLI: icli

Corporate data parsing via IBKR API: ib_fundamental

The software is provided on the conditions of the simplified BSD license.

This project is not affiliated with Interactive Brokers Group, Inc.

Official Interactive Brokers API Docs

This library was originally created by Ewald de Wit as tws_async in early-2017 then became the more prominent ib_insync library in mid-2017. He maintained and improved the library for the world to use for free until his unexpected passing in early 2024. Afterward, we decided to rename the project to ib_async under a new github organization since we lost access to modify anything in the original repos and packaging and docs infrastructure.

The library is currently maintained by Matt Stancliff and we are open to adding more committers and org contributors if people show interest in helping out.

---

## Contents — ib_async 2.1.0 documentation

**URL:** https://ib-api-reloaded.github.io/ib_async/

**Contents:**
- Contents
- ib_async
  - Update
  - Introduction
    - What You Can Build
    - Key Features
  - Installation
  - Build Manually
    - Installing Only Library
    - Install Everything (enable docs + dev testing)

ib_async is a Python library that provides a clean, modern interface to Interactive Brokers’ Trader Workstation (TWS) and IB Gateway. It handles the complexities of the IBKR API so you can focus on building trading applications, research tools, and market data analysis.

Market Data Applications: Stream live quotes, historical data, and market depth

Trading Systems: Place, modify, and monitor orders programmatically

Portfolio Tools: Track positions, account balances, and P&L in real-time

Research Platforms: Analyze contract details, option chains, and fundamental data

Risk Management: Monitor exposures and implement automated controls

Simple and Intuitive: Write straightforward Python code without dealing with callback complexity

Automatic Synchronization: The IB component stays in sync with TWS/Gateway automatically

Async-Ready: Built on asyncio and eventkit for high-performance applications

Jupyter-Friendly: Interactive development with live data in notebooks

Production-Ready: Robust error handling, reconnection logic, and comprehensive logging

Be sure to take a look at the notebooks, the recipes and the API docs.

Python 3.10 or higher

We plan to support Python releases 2 years back which allows us to continue adding newer features and performance improvements over time.

A running IB Gateway application (or TWS with API mode enabled)

stable gateway — updated every few months

latest gateway — updated weekly

Make sure the API port is enabled and ‘Download open orders on connection’ is checked.

You may also want to increase the Java memory usage under Configure->Settings->Memory Allocation to 4096 MB minimum to prevent gateway crashes when loading bulk data.

The ibapi package from IB is not needed. ib_async implements the full IBKR API binary protocol internally.

First, install poetry:

IB Gateway (Stable) — Updated every few months, more stable

IB Gateway (Latest) — Updated weekly, newest features

Trader Workstation (TWS) — Full trading platform

Enable API: Go to Configure → API → Settings and check “Enable ActiveX and Socket Clients”

Set Port: Default ports are 7497 (TWS) and 4001 (Gateway). You can change these if needed.

Allow Connections: Add 127.0.0.1 to “Trusted IPs” if connecting locally

Download Orders: Check “Download open orders on connection” to see existing orders

Memory: Go to Configure → Settings → Memory Allocation and set to 4096 MB minimum to prevent crashes with bulk data

Timeouts: Increase API timeout settings if you experience disconnections during large data requests

ib_async.ib.IB - Main interface class

Connection management (connect(), disconnect(), connectAsync())

Market data requests (reqMktData(), reqHistoricalData())

Order management (placeOrder(), cancelOrder())

Account data (positions(), accountSummary(), reqPnL())

ib_async.contract - Financial instruments

Stock, Option, Future, Forex, Index, Bond

Contract - Base class for all instruments

ComboLeg, DeltaNeutralContract - Complex instruments

ib_async.order - Order types and management

MarketOrder, LimitOrder, StopOrder, StopLimitOrder

Order - Base order class with all parameters

OrderStatus, OrderState - Order execution tracking

Trade - Complete order lifecycle tracking

ib_async.ticker - Real-time market data

Ticker - Live quotes, trades, and market data

Automatic field updates (bid, ask, last, volume, etc.)

Event-driven updates via updateEvent

ib_async.objects - Data structures

BarData - Historical price bars

Position - Portfolio positions

PortfolioItem - Portfolio details with P&L

AccountValue - Account metrics

Synchronous vs Asynchronous

The complete API documentation.

Clone the repository:

Install dependencies:

Make your changes and run tests:

Submit a pull request with:

Clear description of changes

Tests for new functionality

Updated documentation if needed

Follow existing code style (enforced by ruff)

Add tests for new features

Update documentation for user-facing changes

Keep commits focused and well-described

Be responsive to code review feedback

If you have other public work related to ib_async or ib_insync open an issue and we can keep an active list here.

Projects below are not endorsed by any entity and are purely for reference or entertainment purposes.

Adi’s livestream VODs about using IBKR APIs: Interactive Brokers API in Python

Matt’s IBKR python CLI: icli

Corporate data parsing via IBKR API: ib_fundamental

The software is provided on the conditions of the simplified BSD license.

This project is not affiliated with Interactive Brokers Group, Inc.

Official Interactive Brokers API Docs

This library was originally created by Ewald de Wit as tws_async in early-2017 then became the more prominent ib_insync library in mid-2017. He maintained and improved the library for the world to use for free until his unexpected passing in early 2024. Afterward, we decided to rename the project to ib_async under a new github organization since we lost access to modify anything in the original repos and packaging and docs infrastructure.

The library is currently maintained by Matt Stancliff and we are open to adding more committers and org contributors if people show interest in helping out.

---

## Code recipes — ib_async 2.1.0 documentation

**URL:** https://ib-api-reloaded.github.io/ib_async/recipes.html

**Contents:**
- Code recipes
- Fetching consecutive historical data
- Scanner data (blocking)
- Scanner data (streaming)
- Option calculations
- Order book
- Minimum price increments
- News articles
- News bulletins
- WSH Event Calendar

Collection of useful patterns, snippets and recipes.

When using the recipes in a notebook, don’t forget to use util.startLoop().

Suppose we want to get the 1 min bar data of Tesla since the very beginning up until now. The best way is to start with now and keep requesting further and further back in time until there is no more data returned.

A Wall Street Horizon subscription is needed to get corporate event data.

This IB socket protocol is designed to be used for a long-lived connection, lasting a day or so. For short connections, where for example just a few orders are fired of, it is best to add one second of delay before closing the connection. This gives the connection some time to flush the data that has not been sent yet.

This example of a ticker table shows how to integrate both realtime streaming and synchronous API requests in a single-threaded Qt application. The API requests in this example are connect and ib.qualifyContracts(); The latter is used to get the conId of a contract and use that as a unique key.

The Qt interface will not freeze when a request is ongoing and it is even possible to have multiple outstanding requests at the same time.

This example depends on PyQt5:

pip3 install -U PyQt5.

It’s also possible to use PySide2 instead; To do so uncomment the PySide2 import and util.useQt lines in the example and comment out their PyQt5 counterparts.

To integrate with the Tkinter event loop, take a look at this example app.

By calling ib.sleep from within the PyGame run loop, ib_async can periodically run for short whiles and keep up to date:

---

## Notebooks — ib_async 2.1.0 documentation

**URL:** https://ib-api-reloaded.github.io/ib_async/notebooks.html

**Contents:**
- Notebooks

IB-insync can be used in a fully interactive, exploratory way with live data from within a Jupyter notebook. Here are some recipe notebooks:

---

## Links — ib_async 2.1.0 documentation

**URL:** https://ib-api-reloaded.github.io/ib_async/links.html

**Contents:**
- Links

Interactive Brokers Python API

IBC for hands-free operation of TWS or gateway

---

## ib_async Changelog — ib_async 2.1.0 documentation

**URL:** https://ib-api-reloaded.github.io/ib_async/changelog.html

**Contents:**
- ib_async Changelog
- 2.0
  - Version 2.1.0 (2025-12-06)
  - Version 2.0.1 (2025-06-22)
  - Version 2.0.0 (2025-06-13)
- 1.0
  - Version 1.0.3 (2024-07-06)
  - Version 1.0.2 (2024-06-29)
  - Version 1.0.1 (2024-03-20)
  - Version 1.0.0 (2024-03-18)

This release includes several bug fixes, performance improvements, and new features based on recent development work.

New EFP Data Support: Added Exchange for Physical (EFP) data structures and ticker fields for futures trading

New EfpData dataclass with fields for basis points, implied future price, dividend impact, and expiration data

New ticker fields: bidEfp, askEfp, lastEfp, openEfp, highEfp, lowEfp, closeEfp

Support for EFP tick types in the wrapper

Additional Ticker Fields: New fields for enhanced market data access

openInterest, lastRthTrade, lastRegTime, optionBidExch, optionAskExch, bondFactorMultiplier, creditmanMarkPrice, creditmanSlowMarkPrice, delayedLastTimestamp, delayedHalted, reutersMutualFunds, etfNavClose, etfNavPriorClose, etfNavBid, etfNavAsk, etfNavLast, etfFrozenNavLast, etfNavHigh, etfNavLow, socialMarketAnalytics, estimatedIpoMidpoint, finalIpoLast

New custGreeks option computation field

Enhanced ETF NAV (Net Asset Value) tracking fields

Environment Variable Configuration: Added ability to override flexReport URL with environment variable

New IB_FLEXREPORT_URL environment variable support

URL validation for custom endpoints

Updated documentation for flexible endpoint configuration

Improved Event Loop Handling: Better event loop retrieval with fallback mechanisms

Non-cached event loop access to avoid stale loop issues

Enhanced fallback for synchronous contexts

Better handling of closed event loops

Missing Tick Types: Implemented various tick types that were missing from the library

Support for tick types 57, 78, 79, 92-102, 22, 60, 90, 53, 38-44, 25, 26, 32, 33, 84, 85, 91, 100, 45, 88, 48, 77

Optimized tick processing with lookup maps instead of if/else chains

New helper methods for timestamp and RT volume tick processing

Modern Python Syntax: Updated type annotations to use modern Python 3.10+ syntax

Replaced Optional[Type] with Type | None union syntax

Converted Union[TypeA, TypeB] to TypeA | TypeB syntax

Updated imports to use more efficient organization

Ruff Configuration: Improved code quality with expanded linter exclusions

Added notebooks/, upstream_api_architecture/, and examples/ to exclude list

Updated ruff rules for modern Python patterns

Dependency Management: Added explicit tzdata dependency for timezone support

Removed conditional import guard for zoneinfo since Python 3.9+ guarantees availability

Ensured timezone functionality works across all platforms

Performance Improvements: Optimized tick processing with O(1) dictionary lookups

Replaced sequential if/else chains with lookup maps for tick types

Added helper methods for timestamp and RT volume processing

More efficient string-to-datetime conversion

Timebars Typo: Fixed isUnset to isNan helper function in TimeBars class (issue 197)

FlexReport URL: Fixed flexReport URL endpoint and added environment variable override support (issue 199, issue 172)

Setuptools Warning: Fixed deprecation warnings for modern setuptools (issue 198)

Event Loop Caching: Fixed stale event loop bugs that occurred in complex async contexts (issue 160, issue 186, issue 159)

Empty Ticker Fields: Fixed initialization of additional ticker fields to proper unset values

Tick Type Processing: Improved handling of various tick types with proper validation and processing

URL Validation: Added proper URL validation for flexReport requests

Added explicit tzdata dependency to ensure timezone functionality across platforms (issue 188)

Updated pyproject.toml to include license files and remove deprecated classifier (issue 182)

Minor dependency change to fix pypi package building.

The eventkit dependency is now aeventkit because eventkit is locked behind a closed account and pypi doesn’t allow dependencies with direct github URL tags.

This major release includes significant new features, performance improvements, and critical bug fixes. The most notable addition is the custom defaults system, allowing users to customize how ib_async handles empty values and timestamps throughout the library.

Custom Default Values: Major new feature allowing customization of default values used throughout the library via IBDefaults object passed to IB() constructor

Customize emptyPrice, emptySize, unset values, and timezone settings

Replace IBKR’s default values (emptyPrice=-1, emptySize=0, unset=nan) with your preferred defaults (e.g., None)

Set custom timezone for timestamp display (e.g., pytz.timezone("US/Eastern") instead of UTC)

Enhanced Ticker Data: New ticker fields for improved market data analysis

timestamp: Float format timestamp for easier mathematical operations alongside existing time field

shortable: Shortability score (0-3) for instruments

volumeRate3Min, volumeRate5Min, volumeRate10Min: IBKR-provided volume acceleration metrics

lastTimestamp: Timestamp of the last trade event

OrderStatus Enhancements: Extended order management capabilities

New API status states added to OrderStatus enum

totalQuantity() method to report total order quantity

Additional helper methods for reading order states

OrderState Conversion Helpers: New utility methods for OrderState objects

numeric(): Convert string values to numbers with optional digit rounding

formatted(): Convert values to comma-separated formatted strings

Both methods handle UNSET_DOUBLE values automatically

OptionComputation Mathematical Operations: Options can now be added, subtracted, and multiplied

Enables direct calculation of Greeks for spreads (e.g., vertical spreads: longGreeks - shortGreeks)

Contract-from-params Abstraction: Centralized logic for converting generic Contract objects to specific subclass types (e.g., Contract(secType="OPT") → Option())

Enhanced Contract Support:

Event Contracts (“EC” security type) recognition for binary event betting

Bag contracts can now be hashed using leg details, symbol, and exchange

Improved Market Data Subscription Management:

cancelMktData() now returns success/failure status instead of just logging

Contract lookups now use hash(contract) instead of id(contract), allowing reuse of equivalent contract objects

Breaking: qualifyContractsAsync() behavior significantly improved

Now returns N results for N input contracts (previously returned fewer results if some failed)

Failed qualifications return None in corresponding position

New returnAll parameter: when True, returns all possible matches as a list instead of failing for ambiguous contracts

Enables reliable zip(requestContracts, resultContracts) usage

Ticker Previous Value Logic: Simplified and more accurate tracking

Previous price/size now always reflects the truly previous values, regardless of whether they match current values

Removed conditional updating that caused inaccurate “previous” data representation

Better performance by eliminating unnecessary comparisons

Type System Modernization: Extensive type annotation improvements

Dict → dict, List → list, FrozenSet → frozenset throughout codebase

Enhanced Order class with proper type annotations and Decimal support for price/quantity fields

Converted NamedTuple instances to frozen dataclasses for better extensibility

Event Loop Handling: Updated for modern Python compatibility (recent asyncio API changes)

Critical Order Management Bug: Fixed order cache deletion issues that caused “phantom orders”

Orders are no longer incorrectly deleted from client state when modification validation fails

Warning messages are now logged to order history instead of causing state corruption

Prevents situation where orders appear cancelled locally but remain active at broker

Order Modification Bug Prevention: Added API-level validation to prevent common modification errors

Automatic handling of IBKR API field overwrites that conflict with user data

Prevents submission of unintended order updates from cached order objects

TWS API Contract Matching Bug Workaround: Fixed cross-instrument contract suggestions

When requesting FOP contracts, IBKR was incorrectly also returning Event Contracts

Now filters results to only return contracts matching the requested security type

Bulk Data Tick Types: Fixed default value handling in bulk tick processing

Last Trade Timestamp Validation: Improved handling of invalid ‘0’ timestamps from ticker startup

Volatility Order Type: Corrected “VOL” → “VOLAT” order type specification

Missing Import: Added missing import that was causing import errors

False Order Cache Deletion: Additional fix for orders being incorrectly removed during modification validation

Tick Processing Optimization: Significant performance improvements for market data handling

Replaced multi-case if/else branches with lookup maps for tick type processing

More efficient handling of generic ticks and Greek ticks

Added explicit error handling for unknown tick types to aid future development

Ticker Update Performance: Eliminated unnecessary comparison operations during ticker updates

Always replace fields instead of conditionally checking for changes

Faster processing of instruments with frequent same-price trades

Enhanced Error Handling: Better error messages and logging throughout

Unknown tick types now generate explicit error messages for easier debugging

More verbose validation error reporting

Code Style: Comprehensive formatting and linting improvements

Applied ruff format and ufmt formatting across entire codebase

Fixed various style warnings and modernized code patterns

Variable naming improvements (fixed illegal variable names like ‘l’)

Disconnection Logic: Improved connection state management

Full state reset on disconnect/reconnect cycles

Returns connection status string with session details

Utility Functions: Modernized util.py with updated Python patterns and async compatibility

Migration Notes for v2.0.0:

qualifyContractsAsync() users: The return value now always contains the same number of elements as input contracts. Check for None values to detect failed qualifications.

Custom defaults users: Consider using IBDefaults() to customize empty values if you’ve been manually handling -1 prices or 0 sizes.

Ticker previous value users: The logic for previousPrice/previousSize is now more accurate but may show different values if you were relying on the old conditional update behavior.

Order management users: Order validation errors are now logged to order history instead of causing order deletions. Check order event logs for validation details.

General improvements and minor correctness fixes.

Fixed issue 42: Order preview requests would often fail for non-limit-order types due to incorrect value comparison. This has previous attempted fixes over the years, but we finally found the proper fix to the other fixes. Now order preview requests work properly for all order types.

Now market depth data is removed from the Ticker object when a market depth request is stopped because the data isn’t being live updated anymore.

Added ib_fundamental to community utility listing in README

General improvements and minor correctness fixes.

Fixed issue 28: Add ability to optionally disable account data synchronization on startup. If you are an advanced user, you may not need all your data synchronized on startup (which can slow down the initial connections due to the multiple sequential request loading) or you may want to control when the account data is loaded on your own schedule.

Fixed issue 33: Improved reliability of L2 depth of market reporting

Fixed issue 10 and issue 11: Fixed links in documentation

Fixed issue 16: Fixed documentation typo

Fixed issue 32: Use delayed data instead of denied data in example notebooks

Improved error logging if a wrapped method fails

Removed a potential exception when shutting down the event loop from within a larger system

Fixed issue 4: Messaging sending bug for unresolved contracts due to cleanup in 1.0.0

Solved this messaging sending bug by refactoring message parsing logic to be more stable. Also added a test case verifying it works as expected now.

This is the first version under new management after the unexpected passing of Ewald de Wit on March 11, 2024. We wish to maintain his legacy while continuing to improve the project going forward. We are resetting the project name, development practices, modernization levels, and project structure to hopefully grow more contributors over time.

This version update does not include any feature improvements and is functionally equivalent to the final version of ib_insync 0.9.86.

Reformatted all code with ruff and improved readability throughout

Now uses sets for membership checking everywhere

Fixed a technical error around API message formatting

Renamed ib_insync to ib_async everywhere

Increased minimum Python version from 3.6 (2016) to 3.10 (2021)

Removed dependencies for supporting Python versions less than 3.9

Converted README.rst to README.md

Updated IBKR API links to new ibkrcampus instead of old github docs

Removed setup.{py,cfg} to use Poetry for installing, docs, packaging

Converted links from /erdewit/ account to new /ib-api-reloaded/ org

Removed helper scripts for packaging and building docs

Removed docs-generated HTML from repository

Auto-build docs and update github docs site on every push

Documentation now auto-builds and is hosted on github pages instead of readthedocs

Note: due to the project moving to a github organization, all auto-generated links below to mentioned issues and PRs don’t work anymore. You can use the issue numbers in the original ib_insync repo for historical reference.

Fixed: issue 588: Fixed account summary tag.

Fixed: issue 589: Fixed more account summary tags.

pull:598: Year updates

Fixed: issue 586: Revert socket protocol back to version 176.

Potential fix for reqWshEventData.

Added support for WSH (Wall Street Horizon) requests plus the (blocking) convenience methods getWshMetaData and getWshEventData.

Updated socket protocol to version 177.

Added support for Event security type.

Fixed: issue 534: Session parsing for Forex contracts.

Fixed: issue 536: Handle empty session field.

Fixed: issue 541: Remove superfluous closing bracket.

Fixed: issue 542: Use float size for pnlSingle.

Fixed: issue 544: Cancel head-time request after completion.

Fixed: issue 545: Return Trade instead of Order for reqOpenOrders and reqAllOpenOrders.

pull 553: Volume bar added.

Add ContractDetails.tradingSessions() and ContractDetails.liquidSessions() to parse session times.

Fix IBC.on2fatimeout command line argument for Unix.

Fix ib.reqMatchingSymbols to handle bond contracts.

Fix datetime parsing.

Added account parameter to ib.portfolio().

Added IBC.on2fatimeout field.

Removed obsolete IBController.

Fixed: issue 530: Use explicit timezone in requests as per new API requirement.

pull 528: Fixes regression in client.py.

Fixed: issue 525: For whatIf request treat error 110 as failure.

Fixed: issue 524: Use fix from Papakipos for issue with FlexReport downloading.

Fix reqContractDetails bug in combination with latest TWS.

Update the code to comply with stricter MyPy checks.

pull 523: Fix completedOrder parsing for new socket protocol.

pull 507: Fixes bondContractDetails request.

Fixed: issue 502: Treat error 110 as a warning.

Added manualOrderTime and manualCancelOrderTime for audit trails.

Added PEG MID and PEG BEST order types.

Added contract fields description and issuerId.

Added IB.reqUserInfo().

Support socket protocol version 176.

pull 453: Added support for bidExchange and askExchange fields to Ticker.

pull 489: Watchdog.start() now returns a Future.

Fixed: issue 439: Set marketDataType directly on Ticker.

Fixed: issue 441: Add explicit timezone of None to accomodate pandas Timestamp.

Fixed: issue 471: Revised Ticker.marketPrice() calculation.

Added minTick, bboExchange and snapshotPermissions fields to Ticker.

Added minSize, sizeIncrement and suggestedSizeIncrement fields to ContractDetails.

Added IB.reqHistoricalSchedule request.

Added IB.reqSmartComponents request.

Added Order.advancedErrorOverride field. Any advanced error message is made availble from Trade.advancedError.

Added a recipe for integration with PyGame.

Minimum required TWSAPI client protocol version is 157 now.

Fixed: issue 413: Set the appropriate events as done on disconnect.

Exported symbols are now static so that the VSCode/PyLance code analyzer can understand it.

Fixed: issue 403: Change validity test for whatIfOrder response.

Fixed: issue 402: Downloading historical ticks for crypto currencies.

Crypto security class added. To accommodate fractional crypto currency sizes, all the various size and volume fields that were of type int are now of type float.

pull 385: Get day trades remaining for next four days in IB.accountSummary.

Fixed: issue 361: Prevent util.logToConsole and util.logToFile from messing with the root logger.

Fixed: issue 370: Catch asyncio.CancelledError during connect.

Fixed: issue 371: Fix type annotation for reqMarketRuleAsync.

Fixed: issue 380: Reject bogus whatIf order response.

Fixed: issue 389: Add TradeLogEntry.errorCode field.

Fixed: issue 360: Improved disconnect.

Fixed issue with duplicate orderId.

Update Order default values to work with the latest beta TWS/gateway.

pull 348: Added PySide6 support.

pull 317: Update and order’s totalQuantity, lmtPrice, auxPrice and orderType when the order is modified externally.

Fixed: issue 309: Aggregate past fills into the Trade they belong to upon connect.

ContFut objects are now hashable (issue 310).

Added Watchdog.probeTimeout parameter (issue 307).

Fixed issue 282: util.Qt() also works with the ProactorEventLoop (default on Windows) now.

Fixed issue 303: A regression in TWS 480.4l+ is bypassed now to avoid IB.connect() timeouts. Request timeouts during syncing are logged as errors but will let the connect proceed.

IB.TimezoneTWS field added, for when the TWS timezone differs from the local system timezone (issue 287).

IB.RaiseRequestErrors field added, can be set to True to raise RequestError when certain requests fail, instead of returning empty data (pull 296).

IB.accountSummaryAsync() method added (issue 267).

Watchdog.probeContract field added, to use a contract other then EURUSD for probing the data connection (issue 298).

Ticker.rtTime added (issue 274, pull 275). Please note that this timestamp appears to be mostly bogus.

Fixed issue 270: Clear ticker depth data when canceling market depth subscription.

Fixed issue with duplicate order IDs.

Ticker.marketDataType added to indicate the delayed/frozen status of the reqMktData ticks.

IB.reqHistoricalData() has a new timeout parameter that automatically cancels the request after timing out.

BracketOrder is iterable again.

IB.waitOnUpdate() returns False on timeout now.

pull 210: Fix decoding of execDetails time.

pull 215: New scanner notebook added, courtesy of C. Valcarcel.

pull 220: Added readonly option for Watchdog.

Fixed issue 221: Delayed close ticks handling by Ticker.

Fixed issue 224: Added timeout for completedOrders request during connect.

Fixed issue 227: IB.MaxSyncedSubAccounts added.

Fixed issue 230: Fixed IB.reqHistogramData method.

Fixed issue 235: Order.discretionaryAmt is now of type float (was int).

Fixed issue 236: ticker.updateEvent is now fired for any change made to the ticker.

Fixed issue 245: Emit trade.statusEvent when order is implicitly canceled by a problem.

You can now sponsor the development of IB-insync!

PR #205 adds more typing annotations.

dataclasses are now used for objects (instead of inheriting from a base Object). For Python 3.6.* install it with pip install dataclasses

PR #196 treats error 492 as a warning so that scanner results can still be used.

PR #184, #185 and #186 add the new Ticker fields rtTradeVolume, auctionVolume, auctionPrice and auctionImbalance.

PR #191 lets util.schedule return a handle that can be canceled.

PR #192 adds throttleStart and throttleEnd events to the Client.

PR #194 adds better JSON support for namedtuple objects.

Fix bug #178: Order.totalQuantity is now float.

Sphinx update for documentation.

ContractDetails.stockType added.

Fixed Trade.filled() for combo (BAG) contracts.

Server version check added to make sure TWS/gateway version is at least 972.

Fix bug #155 (IB.commissionReportEvent not firing).

Help editors with the code completion for Events.

Fix Client.exerciseOptions (bug #152).

Fix ib.placeOrder for older TWS/gateway versions.

Better handling of unclean disconnects.

Fix execDetailsEvent regression.

Added readonly argument to ib.connect method. Set this to True when the API is in read-only mode.

ib.reqCompletedOrders() request added (requires TWS/gateway >= 976). Completed orders are automatically synced on connect and are available from ib.trades(), complete with fills and commission info.

Ticker.halted field added.

Client.reqFundamentalData fixed.

ibapi package from IB is no longer needed, ib_async handles its own socket protocol encoding and decoding now.

Documentation moved to readthedocs as rawgit will cease operation later this year.

Blocking requests will now raise ConnectionError on a connection failure. This also goes for util.run, util.timeRange, etc.

Event class has been replaced with the one from eventkit.

Event-driven bar construction from ticks added (via Ticker.updateEvent)

Default request throttling is now 45 requests/s for compatibility with TWS/gateway 974 and higher.

TagValue serialization fixed.

Event.any() and Event.all() added.

Ticker fields added: tradeCount, tradeRate, volumeRate, avOptionVolume, markPrice, histVolatility, impliedVolatility, rtHistVolatility and indexFuturePremium.

Parse ticker.fundamentalRatios into FundamentalRatios object.

util.timeRangeAsync() and waitUntilAsync() added.

ib.pendingTickersEvent now emits a set of Tickers instead of a list.

Tick handling has been streamlined.

For harvesting tick data, an imperative code style with a waitOnUpdate loop should not be used anymore!

Event.aiter() added, all events can now be used as asynchronous iterators.

Event.wait() added, all events are now also awaitable.

Decreased default throttling to 95 requests per 2 sec.

Ticker.shortableShares added (for use with generic tick 236).

ib.reqAllOpenOrders() request added.

tickByTick subscription will update ticker’s bid, ask, last, etc.

Drop redundant bid/ask ticks from reqMktData.

Fixed occasional “Group name cannot be null” error message on connect.

Watchdog code rewritten to not need util.patchAsyncio.

Watchdog.start() is no longer blocking.

Fixed order modifications with TWS/gateway 974.

Ticker.fundamentalRatios added (for use with generic tick 258).

Fixed reqHistoricalTicks with MIDPOINT.

Handle partially filled dividend data.

Use secType='WAR' for warrants.

ibapi v97.4 is now required.

fixed tickByTick wrappers.

Backward compatibility with older ibapi restored.

Compatibility with ibapi v974.

Client.setConnectOptions() added (for PACEAPI).

Ticker.hasBidAsk() added.

IB.newsBulletinEvent added.

Old event system (ib.setCallback) removed.

Compatibility fix with previous ibapi version.

Market scanner subscription improved.

IB.scannerDataEvent now emits the full list of ScanData.

Autocompletion with Jedi plugin as used in Spyder and VS Code working again.

Request results will return specialized contract types (like Stock) instead of generic Contract.

IB.scannerDataEvent added.

ContractDetails field summary renamed to contract.

isSmartDepth parameter added for reqMktDepth.

Event loop nesting is now handled by the nest_asyncio project.

util.useQt is rewritten so that it can be used with any asyncio event loop, with support for both PyQt5 and PySide2. It does not use quamash anymore.

Various fixes, extensive documentation overhaul and flake8-compliant code formatting.

Watchdog.stop() will not trigger restart now.

util.patchAsyncio() updated for Python 3.7.

IB.RequestTimeout added.

util.schedule() accepts tz-aware datetimes now.

Let client.disconnect() complete when no event loop is running.

PR #74 merged (ib.reqCurrentTime() method added).

Fixed bug with order error handling.

Default throttling rate now compatible with reqTickers.

Fixed issue with ib.waitOnUpdate() in combination. with ib.pendingTickersEvent.

Added timeout parameter for ib.waitOnUpdate().

ticker.futuresOpenInterest added.

execution.time was string, is now parsed to UTC datetime.

ib.reqMarketRule() request added.

Compatability with Tornado 5 as used in new Jupyter notebook server.

updated ib.reqNewsArticle and ib.reqHistoricalNews to ibapi v9.73.07.

updated ib.reqTickByTickData() signature to ibapi v9.73.07 while keeping backward compatibility.

Don’t overwrite exchange='SMART' in qualifyContracts.

Merged PR #65 (Fix misnamed event).

New IB events disconnectedEvent, newOrderEvent, orderModifyEvent and cancelOrderEvent.

Watchdog improvements.

New event system that will supersede IB.setCallback().

Notebooks updated to use events.

Watchdog must now be given an IB instance.

Fixed bug in default order conditions.

Fixed regression from v0.9.13 in placeOrder.

Fixed orderStatus callback regression.

Log handling improvements.

Client with clientId=0 can now manage manual TWS orders.

Client with master clientId can now monitor manual TWS orders.

Run IBC and IBController directly instead of via shell.

Fixed bug when collecting ticks using ib.waitOnUpdate().

Added ContFuture class (continuous futures).

Added Ticker.midpoint().

ib.accountValues() fixed for use with multiple accounts.

Fix for ib.reqPnLSingle().

Profit and Loss (PnL) funcionality added.

PR #53 (delayed greeks) merged.

Ticker.futuresOpenInterest field removed.

Fixed canceling bar and tick subscriptions.

Watchdog class added.

ib.setTimeout() added.

Ticker.dividends added for use with genericTickList 456.

Errors and warnings will now log the contract they apply to.

IB error() callback signature changed to include contract.

Historical ticks and realtime bars now return time in UTC.

openOrder callback added.

default arguments for ib.connect() and ib.reqMktData().

minimum API version is v9.73.06.

automatic request throttling.

ib.accountValues() now works for multiple accounts.

AccountValue.modelCode added.

Ticker.rtVolume added.

workaround for IBAPI v9.73.06 for Contract.lastTradeDateOrContractMonth format.

util.tree() method added.

error callback signature changed to (reqId, errorCode, errorString).

accountValue and accountSummary callbacks added.

util.useQt() fixed for use with Windows.

Fix for ib.schedule().

Import order conditions into ib_async namespace.

util.useQtAlt() added for using nested event loops on Windows with Qtl

Fixed conditional orders.

Ticker.vwap field added (for use with generic tick 233).

Client with master clientId can now monitor orders and trades of other clients.

barUpdate event now used also for reqRealTimeBars responses

reqRealTimeBars will return RealTimeBarList instead of list.

realtime bars example added to bar data notebook.

fixed event handling bug in Wrapper.execDetails.

BarDataList now used with reqHistoricalData; it also stores the request parameters.

updated the typing annotations.

added barUpdate event to IB.

bar- and tick-data notebooks updated to use callbacks for realtime data.

ticker.marketPrice adjusted to ignore price of -1.

ticker.avVolume handling fixed.

realtimeBar wrapper fix.

context manager for IB and IB.connect().

compatibility with upcoming ibapi changes.

added error event to IB.

notebooks updated to use loopUntil.

small fixes and performance improvements.

new IB.reqHistoricalTicks() API method.

new IB.loopUntil() method.

fixed issues #4, #6, #7.

fixed swapped ticker.putOpenInterest vs ticker.callOpenInterest.

fixed wrapper.tickSize regression.

support for realtime bars and keepUpToDate for historical bars

added option greeks to Ticker.

new IB.waitUntil() and IB.timeRange() scheduling methods.

notebooks no longer depend on PyQt5 for live updates.

notebooks can be run in one go (‘run all’).

tick handling bypasses ibapi decoder for more efficiency.

IB.whatIfOrder() added.

Added detection and warning about common setup problems.

Removed import from ipykernel.

Removed dependencies for installing via pip.

added lots of request methods.

order book (DOM) added.

Added UTC timezone to some timestamps.

---
