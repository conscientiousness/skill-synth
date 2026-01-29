# Tastyworks-Api - Api

**Pages:** 23

---

## tastytrade.metrics - tastytrade 11.1.0 documentation

**URL:** https://tastyworks-api.readthedocs.io/en/latest/api/metrics.html

**Contents:**
- tastytrade.metrics¶

Bases: TastytradeData

Dataclass representing dividend information for a given symbol.

Show JSON schema{ "title": "DividendInfo", "description": "Dataclass representing dividend information for a given symbol.", "type": "object", "properties": { "occurred-date": { "format": "date", "title": "Occurred-Date", "type": "string" }, "amount": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Amount" } }, "required": [ "occurred-date", "amount" ] }

amount (decimal.Decimal)

occurred_date (datetime.date)

Bases: TastytradeData

Dataclass representing earnings information for a given symbol.

Show JSON schema{ "title": "EarningsInfo", "description": "Dataclass representing earnings information for a given symbol.", "type": "object", "properties": { "occurred-date": { "format": "date", "title": "Occurred-Date", "type": "string" }, "eps": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Eps" } }, "required": [ "occurred-date", "eps" ] }

eps (decimal.Decimal)

occurred_date (datetime.date)

Bases: TastytradeData

Dataclass containing information about a recent earnings report, or the expected date of the next one.

Show JSON schema{ "title": "EarningsReport", "description": "Dataclass containing information about a recent earnings report, or the\nexpected date of the next one.", "type": "object", "properties": { "estimated": { "title": "Estimated", "type": "boolean" }, "late-flag": { "title": "Late-Flag", "type": "integer" }, "visible": { "title": "Visible", "type": "boolean" }, "actual-eps": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Actual-Eps" }, "consensus-estimate": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Consensus-Estimate" }, "expected-report-date": { "anyOf": [ { "format": "date", "type": "string" }, { "type": "null" } ], "default": null, "title": "Expected-Report-Date" }, "quarter-end-date": { "anyOf": [ { "format": "date", "type": "string" }, { "type": "null" } ], "default": null, "title": "Quarter-End-Date" }, "time-of-day": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Time-Of-Day" }, "updated-at": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "Updated-At" } }, "required": [ "estimated", "late-flag", "visible" ] }

actual_eps (decimal.Decimal | None)

consensus_estimate (decimal.Decimal | None)

expected_report_date (datetime.date | None)

quarter_end_date (datetime.date | None)

time_of_day (str | None)

updated_at (datetime.datetime | None)

Bases: TastytradeData

Dataclass representing liquidity information for a given symbol.

Show JSON schema{ "title": "Liquidity", "description": "Dataclass representing liquidity information for a given symbol.", "type": "object", "properties": { "sum": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Sum" }, "count": { "title": "Count", "type": "integer" }, "started-at": { "format": "date-time", "title": "Started-At", "type": "string" }, "updated-at": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "Updated-At" } }, "required": [ "sum", "count", "started-at" ] }

started_at (datetime.datetime)

sum (decimal.Decimal)

updated_at (datetime.datetime | None)

Bases: TastytradeData

Dataclass representing market metrics for a given symbol.

Contains lots of useful information, like IV rank, IV percentile and beta.

Show JSON schema{ "title": "MarketMetricInfo", "description": "Dataclass representing market metrics for a given symbol.\n\nContains lots of useful information, like IV rank, IV percentile and beta.", "type": "object", "properties": { "symbol": { "title": "Symbol", "type": "string" }, "implied-volatility-index": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Implied-Volatility-Index" }, "implied-volatility-index-5-day-change": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Implied-Volatility-Index-5-Day-Change" }, "implied-volatility-index-rank": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Implied-Volatility-Index-Rank" }, "tos-implied-volatility-index-rank": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Tos-Implied-Volatility-Index-Rank" }, "tw-implied-volatility-index-rank": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Tw-Implied-Volatility-Index-Rank" }, "tos-implied-volatility-index-rank-updated-at": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "Tos-Implied-Volatility-Index-Rank-Updated-At" }, "implied-volatility-index-rank-source": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Implied-Volatility-Index-Rank-Source" }, "implied-volatility-percentile": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Implied-Volatility-Percentile" }, "implied-volatility-updated-at": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "Implied-Volatility-Updated-At" }, "liquidity-rating": { "anyOf": [ { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Liquidity-Rating" }, "updated-at": { "format": "date-time", "title": "Updated-At", "type": "string" }, "option-expiration-implied-volatilities": { "anyOf": [ { "items": { "$ref": "#/$defs/OptionExpirationImpliedVolatility" }, "type": "array" }, { "type": "null" } ], "default": null, "title": "Option-Expiration-Implied-Volatilities" }, "beta": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Beta" }, "corr-spy-3month": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Corr-Spy-3Month" }, "market-cap": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Market-Cap" }, "earnings": { "anyOf": [ { "$ref": "#/$defs/EarningsReport" }, { "type": "null" } ], "default": null }, "price-earnings-ratio": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Price-Earnings-Ratio" }, "earnings-per-share": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Earnings-Per-Share" }, "dividend-rate-per-share": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Dividend-Rate-Per-Share" }, "implied-volatility-30-day": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Implied-Volatility-30-Day" }, "historical-volatility-30-day": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Historical-Volatility-30-Day" }, "historical-volatility-60-day": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Historical-Volatility-60-Day" }, "historical-volatility-90-day": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Historical-Volatility-90-Day" }, "iv-hv-30-day-difference": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Iv-Hv-30-Day-Difference" }, "beta-updated-at": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "Beta-Updated-At" }, "created-at": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "Created-At" }, "dividend-ex-date": { "anyOf": [ { "format": "date", "type": "string" }, { "type": "null" } ], "default": null, "title": "Dividend-Ex-Date" }, "dividend-next-date": { "anyOf": [ { "format": "date", "type": "string" }, { "type": "null" } ], "default": null, "title": "Dividend-Next-Date" }, "dividend-pay-date": { "anyOf": [ { "format": "date", "type": "string" }, { "type": "null" } ], "default": null, "title": "Dividend-Pay-Date" }, "dividend-updated-at": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "Dividend-Updated-At" }, "liquidity-value": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Liquidity-Value" }, "liquidity-rank": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Liquidity-Rank" }, "liquidity-running-state": { "anyOf": [ { "$ref": "#/$defs/Liquidity" }, { "type": "null" } ], "default": null }, "dividend-yield": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Dividend-Yield" }, "listed-market": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Listed-Market" }, "lendability": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Lendability" }, "borrow-rate": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Borrow-Rate" } }, "$defs": { "EarningsReport": { "description": "Dataclass containing information about a recent earnings report, or the\nexpected date of the next one.", "properties": { "estimated": { "title": "Estimated", "type": "boolean" }, "late-flag": { "title": "Late-Flag", "type": "integer" }, "visible": { "title": "Visible", "type": "boolean" }, "actual-eps": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Actual-Eps" }, "consensus-estimate": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Consensus-Estimate" }, "expected-report-date": { "anyOf": [ { "format": "date", "type": "string" }, { "type": "null" } ], "default": null, "title": "Expected-Report-Date" }, "quarter-end-date": { "anyOf": [ { "format": "date", "type": "string" }, { "type": "null" } ], "default": null, "title": "Quarter-End-Date" }, "time-of-day": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Time-Of-Day" }, "updated-at": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "Updated-At" } }, "required": [ "estimated", "late-flag", "visible" ], "title": "EarningsReport", "type": "object" }, "Liquidity": { "description": "Dataclass representing liquidity information for a given symbol.", "properties": { "sum": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Sum" }, "count": { "title": "Count", "type": "integer" }, "started-at": { "format": "date-time", "title": "Started-At", "type": "string" }, "updated-at": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "Updated-At" } }, "required": [ "sum", "count", "started-at" ], "title": "Liquidity", "type": "object" }, "OptionExpirationImpliedVolatility": { "description": "Dataclass containing implied volatility information for a given symbol\nand expiration date.", "properties": { "expiration-date": { "format": "date", "title": "Expiration-Date", "type": "string" }, "settlement-type": { "title": "Settlement-Type", "type": "string" }, "option-chain-type": { "title": "Option-Chain-Type", "type": "string" }, "implied-volatility": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Implied-Volatility" } }, "required": [ "expiration-date", "settlement-type", "option-chain-type" ], "title": "OptionExpirationImpliedVolatility", "type": "object" } }, "required": [ "symbol", "updated-at", "market-cap" ] }

beta (decimal.Decimal | None)

beta_updated_at (datetime.datetime | None)

borrow_rate (decimal.Decimal | None)

corr_spy_3month (decimal.Decimal | None)

created_at (datetime.datetime | None)

dividend_ex_date (datetime.date | None)

dividend_next_date (datetime.date | None)

dividend_pay_date (datetime.date | None)

dividend_rate_per_share (decimal.Decimal | None)

dividend_updated_at (datetime.datetime | None)

dividend_yield (decimal.Decimal | None)

earnings (tastytrade.metrics.EarningsReport | None)

earnings_per_share (decimal.Decimal | None)

historical_volatility_30_day (decimal.Decimal | None)

historical_volatility_60_day (decimal.Decimal | None)

historical_volatility_90_day (decimal.Decimal | None)

implied_volatility_30_day (decimal.Decimal | None)

implied_volatility_index (decimal.Decimal | None)

implied_volatility_index_5_day_change (decimal.Decimal | None)

implied_volatility_index_rank (str | None)

implied_volatility_index_rank_source (str | None)

implied_volatility_percentile (str | None)

implied_volatility_updated_at (datetime.datetime | None)

iv_hv_30_day_difference (decimal.Decimal | None)

lendability (str | None)

liquidity_rank (decimal.Decimal | None)

liquidity_rating (int | None)

liquidity_running_state (tastytrade.metrics.Liquidity | None)

liquidity_value (decimal.Decimal | None)

listed_market (str | None)

market_cap (decimal.Decimal)

option_expiration_implied_volatilities (list[tastytrade.metrics.OptionExpirationImpliedVolatility] | None)

price_earnings_ratio (decimal.Decimal | None)

tos_implied_volatility_index_rank (decimal.Decimal | None)

tos_implied_volatility_index_rank_updated_at (datetime.datetime | None)

tw_implied_volatility_index_rank (decimal.Decimal | None)

updated_at (datetime.datetime)

Bases: TastytradeData

Dataclass containing implied volatility information for a given symbol and expiration date.

Show JSON schema{ "title": "OptionExpirationImpliedVolatility", "description": "Dataclass containing implied volatility information for a given symbol\nand expiration date.", "type": "object", "properties": { "expiration-date": { "format": "date", "title": "Expiration-Date", "type": "string" }, "settlement-type": { "title": "Settlement-Type", "type": "string" }, "option-chain-type": { "title": "Option-Chain-Type", "type": "string" }, "implied-volatility": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Implied-Volatility" } }, "required": [ "expiration-date", "settlement-type", "option-chain-type" ] }

expiration_date (datetime.date)

implied_volatility (decimal.Decimal | None)

option_chain_type (str)

settlement_type (str)

Retrieves dividend information for the given symbol.

active user session to use

symbol to retrieve dividend information for

Retrieves earnings information for the given symbol.

active user session to use

symbol to retrieve earnings information for

limits earnings to those on or after the given date

Retrieves market metrics for the given symbols.

active user session to use

list of symbols to retrieve metrics for

Retrieves the current risk-free rate.

active user session to use

Retrieves dividend information for the given symbol.

active user session to use

symbol to retrieve dividend information for

Retrieves earnings information for the given symbol.

active user session to use

symbol to retrieve earnings information for

limits earnings to those on or after the given date

Retrieves market metrics for the given symbols.

active user session to use

list of symbols to retrieve metrics for

Retrieves the current risk-free rate.

active user session to use

**Examples:**

Example 1 (json):
```json
{
   "title": "DividendInfo",
   "description": "Dataclass representing dividend information for a given symbol.",
   "type": "object",
   "properties": {
      "occurred-date": {
         "format": "date",
         "title": "Occurred-Date",
         "type": "string"
      },
      "amount": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Amount"
      }
   },
   "required": [
      "occurred-date",
      "amount"
   ]
}
```

Example 2 (json):
```json
{
   "title": "EarningsInfo",
   "description": "Dataclass representing earnings information for a given symbol.",
   "type": "object",
   "properties": {
      "occurred-date": {
         "format": "date",
         "title": "Occurred-Date",
         "type": "string"
      },
      "eps": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Eps"
      }
   },
   "required": [
      "occurred-date",
      "eps"
   ]
}
```

Example 3 (json):
```json
{
   "title": "EarningsReport",
   "description": "Dataclass containing information about a recent earnings report, or the\nexpected date of the next one.",
   "type": "object",
   "properties": {
      "estimated": {
         "title": "Estimated",
         "type": "boolean"
      },
      "late-flag": {
         "title": "Late-Flag",
         "type": "integer"
      },
      "visible": {
         "title": "Visible",
         "type": "boolean"
      },
      "actual-eps": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Actual-Eps"
      },
      "consensus-estimate": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Consensus-Estimate"
      },
      "expected-report-date": {
         "anyOf": [
            {
               "format": "date",
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Expected-Report-Date"
      },
      "quarter-end-date": {
         "anyOf": [
            {
               "format": "date",
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Quarter-End-Date"
      },
      "time-of-day": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Time-Of-Day"
      },
      "updated-at": {
         "anyOf": [
            {
               "format": "date-time",
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Updated-At"
      }
   },
   "required": [
      "estimated",
      "late-flag",
      "visible"
   ]
}
```

Example 4 (json):
```json
{
   "title": "Liquidity",
   "description": "Dataclass representing liquidity information for a given symbol.",
   "type": "object",
   "properties": {
      "sum": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Sum"
      },
      "count": {
         "title": "Count",
         "type": "integer"
      },
      "started-at": {
         "format": "date-time",
         "title": "Started-At",
         "type": "string"
      },
      "updated-at": {
         "anyOf": [
            {
               "format": "date-time",
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Updated-At"
      }
   },
   "required": [
      "sum",
      "count",
      "started-at"
   ]
}
```

---

## Account Streamer - tastytrade 11.1.0 documentation

**URL:** https://tastyworks-api.readthedocs.io/en/latest/account-streamer.html

**Contents:**
- Account Streamer¶
- Basic usage¶
- Disconnect callback¶
- Retry callback¶

The account streamer is used to track account-level updates, such as order fills, watchlist updates and quote alerts. Typically, you’ll want a separate task running for the account streamer, which can then notify your application about important events.

Here’s an example of setting up an account streamer to continuously wait for events and print them:

Probably the most important information the account streamer handles is order fills. We can listen just for orders like so:

The disconnect callback can be used to run arbitrary code when the websocket connection has been disconnected. This is useful for notification purposes in your application when you need high availability. The callback function should look something like this:

The requirements are that the first parameter be the AlertStreamer instance, and the function should be asynchronous. This callback can then be used when creating the streamer:

The account streamer has a special “callback” function which can be used to execute arbitrary code whenever the websocket reconnects. This is useful for re-subscribing to whatever alerts you wanted to subscribe to initially (in fact, you can probably use the same function/code you use when initializing the connection). The callback function should look something like this:

The requirements are that the first parameter be the AlertStreamer instance, and the function should be asynchronous. Other than that, you have the flexibility to decide what arguments you want to use. This callback can then be used when creating the streamer:

The reconnection uses websockets’ exponential backoff algorithm, which can be configured through environment variables here. The difference between the disconnect and reconnect callbacks is that the disconnect will be called immediately when the connection is broken, whereas the reconnect callback will only be called once the connection is re-established.

**Examples:**

Example 1 (python):
```python
from tastytrade import Account, AlertStreamer, Watchlist

async with AlertStreamer(session) as streamer:
    accounts = Account.get(session)

    # updates to balances, orders, and positions
    await streamer.subscribe_accounts(accounts)
    # changes in public watchlists
    await streamer.subscribe_public_watchlists()
    # quote alerts configured by the user
    await streamer.subscribe_quote_alerts()

    async for wl in streamer.listen(Watchlist):
        print(wl)
```

Example 2 (swift):
```swift
from tastytrade.order import PlacedOrder

async with AlertStreamer(session) as streamer:
    accounts = Account.get(session)
    await streamer.subscribe_accounts(accounts)

    async for order in streamer.listen(PlacedOrder):
        print(order)
```

Example 3 (python):
```python
async def disconnect_callback(streamer: AlertStreamer):
    print("Disconnected!")
```

Example 4 (typescript):
```typescript
async with AlertStreamer(session, disconnect_fn=disconnect_callback) as streamer:
    # ...
```

---

## tastytrade.account - tastytrade 11.1.0 documentation

**URL:** https://tastyworks-api.readthedocs.io/en/latest/api/account.html

**Contents:**
- tastytrade.account¶

Bases: TastytradeData

Dataclass that represents a Tastytrade account object, containing methods for retrieving information about the account, placing orders, and retrieving past transactions.

Show JSON schema{ "title": "Account", "description": "Dataclass that represents a Tastytrade account object, containing\nmethods for retrieving information about the account, placing orders,\nand retrieving past transactions.", "type": "object", "properties": { "account-number": { "title": "Account-Number", "type": "string" }, "opened-at": { "format": "date-time", "title": "Opened-At", "type": "string" }, "nickname": { "title": "Nickname", "type": "string" }, "account-type-name": { "title": "Account-Type-Name", "type": "string" }, "is-closed": { "title": "Is-Closed", "type": "boolean" }, "day-trader-status": { "anyOf": [ { "type": "string" }, { "type": "boolean" } ], "title": "Day-Trader-Status" }, "is-firm-error": { "title": "Is-Firm-Error", "type": "boolean" }, "is-firm-proprietary": { "title": "Is-Firm-Proprietary", "type": "boolean" }, "is-futures-approved": { "title": "Is-Futures-Approved", "type": "boolean" }, "is-test-drive": { "default": false, "title": "Is-Test-Drive", "type": "boolean" }, "margin-or-cash": { "title": "Margin-Or-Cash", "type": "string" }, "is-foreign": { "title": "Is-Foreign", "type": "boolean" }, "created-at": { "format": "date-time", "title": "Created-At", "type": "string" }, "external-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "External-Id" }, "closed-at": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Closed-At" }, "funding-date": { "anyOf": [ { "format": "date", "type": "string" }, { "type": "null" } ], "default": null, "title": "Funding-Date" }, "investment-objective": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Investment-Objective" }, "liquidity-needs": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Liquidity-Needs" }, "risk-tolerance": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Risk-Tolerance" }, "investment-time-horizon": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Investment-Time-Horizon" }, "futures-account-purpose": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Futures-Account-Purpose" }, "external-fdid": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "External-Fdid" }, "suitable-options-level": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Suitable-Options-Level" }, "submitting-user-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Submitting-User-Id" } }, "required": [ "account-number", "opened-at", "nickname", "account-type-name", "is-closed", "day-trader-status", "is-firm-error", "is-firm-proprietary", "is-futures-approved", "margin-or-cash", "is-foreign", "created-at" ] }

account_type_name (str)

closed_at (str | None)

created_at (datetime.datetime)

day_trader_status (str | bool)

external_fdid (str | None)

external_id (str | None)

funding_date (datetime.date | None)

futures_account_purpose (str | None)

investment_objective (str | None)

investment_time_horizon (str | None)

is_firm_proprietary (bool)

is_futures_approved (bool)

liquidity_needs (str | None)

opened_at (datetime.datetime)

risk_tolerance (str | None)

submitting_user_id (str | None)

suitable_options_level (str | None)

Delete a complex order by ID.

the session to use for the request.

the ID of the order to delete.

Delete an order by ID.

the session to use for the request.

the ID of the order to delete.

Gets all trading accounts associated with the Tastytrade user, or a specific one if given an account ID.

the session to use for the request.

the account ID to get.

whether to include closed accounts in the results

Returns a list of balance snapshots. This list will just have a few snapshots if you don’t pass a start date; otherwise, it will be each day’s balances in the given range.

the session to use for the request.

the number of results to return per page.

provide a specific page to get; if None, get all pages

the currency to show balances in.

the starting date of the range.

the ending date of the range.

the date of the snapshot to get.

the time of day of the snapshots to get, either ‘EOD’ (End Of Day) or ‘BOD’ (Beginning Of Day).

Get the current balances of the account.

the session to use for the request

the currency to state balances in

Gets a complex order with the given ID.

the session to use for the request.

the ID of the order to fetch.

Get order history of the account.

the session to use for the request.

the number of results to return per page.

provide a specific page to get; if None, get all pages

Get transaction history of the account.

the session to use for the request.

the number of results to return per page.

provide a specific page to get; if None, get all pages

the order to sort results in, either ‘Desc’ or ‘Asc’.

the type of transaction.

a list of transaction types to filter by.

an array of transaction subtypes to filter by.

the start date of transactions to query.

the end date of transactions to query.

the type of instrument.

the underlying symbol.

the action of the transaction: ‘Sell to Open’, ‘Sell to Close’, ‘Buy to Open’, ‘Buy to Close’, ‘Sell’ or ‘Buy’.

account partition key.

the full TW Future Symbol, e.g. /ESZ9, /NGZ19.

datetime start range for filtering transactions in full date-time.

datetime end range for filtering transactions in full date-time.

Get complex orders placed today for the account.

the session to use for the request.

Get orders placed today for the account.

the session to use for the request.

Get the margin report for the account, with total margin requirements as well as a breakdown per symbol/instrument.

the session to use for the request.

Returns a list of account net liquidating value snapshots over the specified time period.

the session to use for the request, can’t be certification.

the time period to get net liquidating value snapshots for. This param is required if start_time is not given. Possible values are: ‘1d’, ‘1m’, ‘3m’, ‘6m’, ‘1y’, ‘all’.

the start point for the query. This param is required is time-back is not given. If given, will take precedence over time-back.

Gets an order with the given ID.

the session to use for the request.

the ID of the order to fetch.

Get order history of the account.

the session to use for the request.

the number of results to return per page.

provide a specific page to get; if None, get all pages

the start date of orders to query.

the end date of orders to query.

underlying symbol to filter by.

a list of statuses to filter by.

Tastytrade future symbol for futures and future options.

the type of instrument to filter by

the order to sort results in, either ‘Desc’ or ‘Asc’.

datetime start range for filtering transactions in full date-time.

datetime end range for filtering transactions in full date-time.

Get the current positions of the account.

the session to use for the request.

an array of underlying symbols for positions.

the type of instrument.

if closed positions should be included in the query.

the underlying future’s product code.

account partition keys.

returns net positions grouped by instrument type and symbol.

include current quote mark (note: can decrease performance).

Get the total fees for a given date.

the session to use for the request.

the date to get fees for.

Get the trading status of the account.

the session to use for the request.

Get a single transaction by ID.

the session to use for the request.

the ID of the transaction to fetch.

Place the given order.

the session to use for the request.

whether this is a test order or not.

Place the given order.

the session to use for the request.

whether this is a test order or not.

Replace an order with a new order with different characteristics (but same legs).

the session to use for the request.

the ID of the order to replace.

the new order to replace the old order with.

Delete a complex order by ID.

the session to use for the request.

the ID of the order to delete.

Delete an order by ID.

the session to use for the request.

the ID of the order to delete.

Gets all trading accounts associated with the Tastytrade user, or a specific one if given an account ID.

the session to use for the request.

the account ID to get.

whether to include closed accounts in the results

Returns a list of balance snapshots. This list will just have a few snapshots if you don’t pass a start date; otherwise, it will be each day’s balances in the given range.

the session to use for the request.

the number of results to return per page.

provide a specific page to get; if None, get all pages

the currency to show balances in.

the starting date of the range.

the ending date of the range.

the date of the snapshot to get.

the time of day of the snapshots to get, either ‘EOD’ (End Of Day) or ‘BOD’ (Beginning Of Day).

Get the current balances of the account.

the session to use for the request

the currency to state balances in

Gets a complex order with the given ID.

the session to use for the request.

the ID of the order to fetch.

Get order history of the account.

the session to use for the request.

the number of results to return per page.

provide a specific page to get; if None, get all pages

Get transaction history of the account.

the session to use for the request.

the number of results to return per page.

provide a specific page to get; if None, get all pages

the order to sort results in, either ‘Desc’ or ‘Asc’.

the type of transaction.

a list of transaction types to filter by.

an array of transaction subtypes to filter by.

the start date of transactions to query.

the end date of transactions to query.

the type of instrument.

the underlying symbol.

the action of the transaction: ‘Sell to Open’, ‘Sell to Close’, ‘Buy to Open’, ‘Buy to Close’, ‘Sell’ or ‘Buy’.

account partition key.

the full TW Future Symbol, e.g. /ESZ9, /NGZ19.

datetime start range for filtering transactions in full date-time.

datetime end range for filtering transactions in full date-time.

Get complex orders placed today for the account.

the session to use for the request.

Get orders placed today for the account.

the session to use for the request.

Get the margin report for the account, with total margin requirements as well as a breakdown per symbol/instrument.

the session to use for the request.

Returns a list of account net liquidating value snapshots over the specified time period.

the session to use for the request, can’t be certification.

the time period to get net liquidating value snapshots for. This param is required if start_time is not given. Possible values are: ‘1d’, ‘1m’, ‘3m’, ‘6m’, ‘1y’, ‘all’.

the start point for the query. This param is required is time-back is not given. If given, will take precedence over time-back.

Gets an order with the given ID.

the session to use for the request.

the ID of the order to fetch.

Get order history of the account.

the session to use for the request.

the number of results to return per page.

provide a specific page to get; if None, get all pages

the start date of orders to query.

the end date of orders to query.

underlying symbol to filter by.

a list of statuses to filter by.

Tastytrade future symbol for futures and future options.

the type of instrument to filter by

the order to sort results in, either ‘Desc’ or ‘Asc’.

datetime start range for filtering transactions in full date-time.

datetime end range for filtering transactions in full date-time.

Get the current positions of the account.

the session to use for the request.

an array of underlying symbols for positions.

the type of instrument.

if closed positions should be included in the query.

the underlying future’s product code.

account partition keys.

returns net positions grouped by instrument type and symbol.

include current quote mark (note: can decrease performance).

Get the total fees for a given date.

the session to use for the request.

the date to get fees for.

Get the trading status of the account.

the session to use for the request.

Get a single transaction by ID.

the session to use for the request.

the ID of the transaction to fetch.

Place the given order.

the session to use for the request.

whether this is a test order or not.

Place the given order.

the session to use for the request.

whether this is a test order or not.

Replace an order with a new order with different characteristics (but same legs).

the session to use for the request.

the ID of the order to replace.

the new order to replace the old order with.

Bases: TastytradeData

Dataclass containing account balance information.

Show JSON schema{ "title": "AccountBalance", "description": "Dataclass containing account balance information.", "type": "object", "properties": { "account-number": { "title": "Account-Number", "type": "string" }, "cash-balance": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Cash-Balance" }, "long-equity-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Long-Equity-Value" }, "short-equity-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Short-Equity-Value" }, "long-derivative-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Long-Derivative-Value" }, "short-derivative-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Short-Derivative-Value" }, "long-futures-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Long-Futures-Value" }, "short-futures-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Short-Futures-Value" }, "long-futures-derivative-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Long-Futures-Derivative-Value" }, "short-futures-derivative-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Short-Futures-Derivative-Value" }, "long-margineable-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Long-Margineable-Value" }, "short-margineable-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Short-Margineable-Value" }, "margin-equity": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Margin-Equity" }, "equity-buying-power": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Equity-Buying-Power" }, "derivative-buying-power": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Derivative-Buying-Power" }, "day-trading-buying-power": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Day-Trading-Buying-Power" }, "futures-margin-requirement": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Futures-Margin-Requirement" }, "available-trading-funds": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Available-Trading-Funds" }, "maintenance-requirement": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Maintenance-Requirement" }, "maintenance-call-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Maintenance-Call-Value" }, "reg-t-call-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Reg-T-Call-Value" }, "day-trading-call-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Day-Trading-Call-Value" }, "day-equity-call-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Day-Equity-Call-Value" }, "net-liquidating-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Net-Liquidating-Value" }, "cash-available-to-withdraw": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Cash-Available-To-Withdraw" }, "day-trade-excess": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Day-Trade-Excess" }, "pending-cash": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Pending-Cash" }, "long-cryptocurrency-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Long-Cryptocurrency-Value" }, "short-cryptocurrency-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Short-Cryptocurrency-Value" }, "cryptocurrency-margin-requirement": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Cryptocurrency-Margin-Requirement" }, "unsettled-cryptocurrency-fiat-amount": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Unsettled-Cryptocurrency-Fiat-Amount" }, "closed-loop-available-balance": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Closed-Loop-Available-Balance" }, "equity-offering-margin-requirement": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Equity-Offering-Margin-Requirement" }, "long-bond-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Long-Bond-Value" }, "bond-margin-requirement": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Bond-Margin-Requirement" }, "used-derivative-buying-power": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Used-Derivative-Buying-Power" }, "snapshot-date": { "format": "date", "title": "Snapshot-Date", "type": "string" }, "reg-t-margin-requirement": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Reg-T-Margin-Requirement" }, "futures-overnight-margin-requirement": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Futures-Overnight-Margin-Requirement" }, "futures-intraday-margin-requirement": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Futures-Intraday-Margin-Requirement" }, "maintenance-excess": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Maintenance-Excess" }, "pending-margin-interest": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Pending-Margin-Interest" }, "effective-cryptocurrency-buying-power": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Effective-Cryptocurrency-Buying-Power" }, "updated-at": { "format": "date-time", "title": "Updated-At", "type": "string" }, "apex-starting-day-margin-equity": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Apex-Starting-Day-Margin-Equity" }, "buying-power-adjustment": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Buying-Power-Adjustment" }, "time-of-day": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Time-Of-Day" } }, "required": [ "account-number", "cash-balance", "long-equity-value", "short-equity-value", "long-derivative-value", "short-derivative-value", "long-futures-value", "short-futures-value", "long-futures-derivative-value", "short-futures-derivative-value", "long-margineable-value", "short-margineable-value", "margin-equity", "equity-buying-power", "derivative-buying-power", "day-trading-buying-power", "futures-margin-requirement", "available-trading-funds", "maintenance-requirement", "maintenance-call-value", "reg-t-call-value", "day-trading-call-value", "day-equity-call-value", "net-liquidating-value", "cash-available-to-withdraw", "day-trade-excess", "pending-cash", "long-cryptocurrency-value", "short-cryptocurrency-value", "cryptocurrency-margin-requirement", "unsettled-cryptocurrency-fiat-amount", "closed-loop-available-balance", "equity-offering-margin-requirement", "long-bond-value", "bond-margin-requirement", "used-derivative-buying-power", "snapshot-date", "reg-t-margin-requirement", "futures-overnight-margin-requirement", "futures-intraday-margin-requirement", "maintenance-excess", "pending-margin-interest", "effective-cryptocurrency-buying-power", "updated-at" ] }

apex_starting_day_margin_equity (decimal.Decimal | None)

available_trading_funds (decimal.Decimal)

bond_margin_requirement (decimal.Decimal)

buying_power_adjustment (decimal.Decimal | None)

cash_available_to_withdraw (decimal.Decimal)

cash_balance (decimal.Decimal)

closed_loop_available_balance (decimal.Decimal)

cryptocurrency_margin_requirement (decimal.Decimal)

day_equity_call_value (decimal.Decimal)

day_trade_excess (decimal.Decimal)

day_trading_buying_power (decimal.Decimal)

day_trading_call_value (decimal.Decimal)

derivative_buying_power (decimal.Decimal)

effective_cryptocurrency_buying_power (decimal.Decimal)

equity_buying_power (decimal.Decimal)

equity_offering_margin_requirement (decimal.Decimal)

futures_intraday_margin_requirement (decimal.Decimal)

futures_margin_requirement (decimal.Decimal)

futures_overnight_margin_requirement (decimal.Decimal)

long_bond_value (decimal.Decimal)

long_cryptocurrency_value (decimal.Decimal)

long_derivative_value (decimal.Decimal)

long_equity_value (decimal.Decimal)

long_futures_derivative_value (decimal.Decimal)

long_futures_value (decimal.Decimal)

long_margineable_value (decimal.Decimal)

maintenance_call_value (decimal.Decimal)

maintenance_excess (decimal.Decimal)

maintenance_requirement (decimal.Decimal)

margin_equity (decimal.Decimal)

net_liquidating_value (decimal.Decimal)

pending_cash (decimal.Decimal)

pending_margin_interest (decimal.Decimal)

reg_t_call_value (decimal.Decimal)

reg_t_margin_requirement (decimal.Decimal)

short_cryptocurrency_value (decimal.Decimal)

short_derivative_value (decimal.Decimal)

short_equity_value (decimal.Decimal)

short_futures_derivative_value (decimal.Decimal)

short_futures_value (decimal.Decimal)

short_margineable_value (decimal.Decimal)

snapshot_date (datetime.date)

time_of_day (str | None)

unsettled_cryptocurrency_fiat_amount (decimal.Decimal)

updated_at (datetime.datetime)

used_derivative_buying_power (decimal.Decimal)

validate_price_effects » all fields

Bases: TastytradeData

Dataclass containing account balance for a moment in time (snapshot).

Show JSON schema{ "title": "AccountBalanceSnapshot", "description": "Dataclass containing account balance for a moment in time (snapshot).", "type": "object", "properties": { "account-number": { "title": "Account-Number", "type": "string" }, "cash-balance": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Cash-Balance" }, "long-equity-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Long-Equity-Value" }, "short-equity-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Short-Equity-Value" }, "long-derivative-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Long-Derivative-Value" }, "short-derivative-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Short-Derivative-Value" }, "long-futures-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Long-Futures-Value" }, "short-futures-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Short-Futures-Value" }, "long-futures-derivative-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Long-Futures-Derivative-Value" }, "short-futures-derivative-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Short-Futures-Derivative-Value" }, "long-margineable-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Long-Margineable-Value" }, "short-margineable-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Short-Margineable-Value" }, "margin-equity": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Margin-Equity" }, "equity-buying-power": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Equity-Buying-Power" }, "derivative-buying-power": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Derivative-Buying-Power" }, "day-trading-buying-power": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Day-Trading-Buying-Power" }, "futures-margin-requirement": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Futures-Margin-Requirement" }, "available-trading-funds": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Available-Trading-Funds" }, "maintenance-requirement": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Maintenance-Requirement" }, "maintenance-call-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Maintenance-Call-Value" }, "reg-t-call-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Reg-T-Call-Value" }, "day-trading-call-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Day-Trading-Call-Value" }, "day-equity-call-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Day-Equity-Call-Value" }, "net-liquidating-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Net-Liquidating-Value" }, "cash-available-to-withdraw": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Cash-Available-To-Withdraw" }, "day-trade-excess": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Day-Trade-Excess" }, "pending-cash": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Pending-Cash" }, "snapshot-date": { "format": "date", "title": "Snapshot-Date", "type": "string" }, "time-of-day": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Time-Of-Day" }, "long-cryptocurrency-value": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Long-Cryptocurrency-Value" }, "short-cryptocurrency-value": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Short-Cryptocurrency-Value" }, "cryptocurrency-margin-requirement": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Cryptocurrency-Margin-Requirement" }, "unsettled-cryptocurrency-fiat-amount": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Unsettled-Cryptocurrency-Fiat-Amount" }, "closed-loop-available-balance": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Closed-Loop-Available-Balance" }, "equity-offering-margin-requirement": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Equity-Offering-Margin-Requirement" }, "long-bond-value": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Long-Bond-Value" }, "bond-margin-requirement": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Bond-Margin-Requirement" }, "used-derivative-buying-power": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Used-Derivative-Buying-Power" } }, "required": [ "account-number", "cash-balance", "long-equity-value", "short-equity-value", "long-derivative-value", "short-derivative-value", "long-futures-value", "short-futures-value", "long-futures-derivative-value", "short-futures-derivative-value", "long-margineable-value", "short-margineable-value", "margin-equity", "equity-buying-power", "derivative-buying-power", "day-trading-buying-power", "futures-margin-requirement", "available-trading-funds", "maintenance-requirement", "maintenance-call-value", "reg-t-call-value", "day-trading-call-value", "day-equity-call-value", "net-liquidating-value", "cash-available-to-withdraw", "day-trade-excess", "pending-cash", "snapshot-date" ] }

available_trading_funds (decimal.Decimal)

bond_margin_requirement (decimal.Decimal | None)

cash_available_to_withdraw (decimal.Decimal)

cash_balance (decimal.Decimal)

closed_loop_available_balance (decimal.Decimal | None)

cryptocurrency_margin_requirement (decimal.Decimal | None)

day_equity_call_value (decimal.Decimal)

day_trade_excess (decimal.Decimal)

day_trading_buying_power (decimal.Decimal)

day_trading_call_value (decimal.Decimal)

derivative_buying_power (decimal.Decimal)

equity_buying_power (decimal.Decimal)

equity_offering_margin_requirement (decimal.Decimal | None)

futures_margin_requirement (decimal.Decimal)

long_bond_value (decimal.Decimal | None)

long_cryptocurrency_value (decimal.Decimal | None)

long_derivative_value (decimal.Decimal)

long_equity_value (decimal.Decimal)

long_futures_derivative_value (decimal.Decimal)

long_futures_value (decimal.Decimal)

long_margineable_value (decimal.Decimal)

maintenance_call_value (decimal.Decimal)

maintenance_requirement (decimal.Decimal)

margin_equity (decimal.Decimal)

net_liquidating_value (decimal.Decimal)

pending_cash (decimal.Decimal)

reg_t_call_value (decimal.Decimal)

short_cryptocurrency_value (decimal.Decimal | None)

short_derivative_value (decimal.Decimal)

short_equity_value (decimal.Decimal)

short_futures_derivative_value (decimal.Decimal)

short_futures_value (decimal.Decimal)

short_margineable_value (decimal.Decimal)

snapshot_date (datetime.date)

time_of_day (str | None)

unsettled_cryptocurrency_fiat_amount (decimal.Decimal | None)

used_derivative_buying_power (decimal.Decimal | None)

validate_price_effects » all fields

Bases: TastytradeData

Dataclass containing imformation about an individual position in a portfolio.

Show JSON schema{ "title": "CurrentPosition", "description": "Dataclass containing imformation about an individual position in a\nportfolio.", "type": "object", "properties": { "account-number": { "title": "Account-Number", "type": "string" }, "symbol": { "title": "Symbol", "type": "string" }, "instrument-type": { "$ref": "#/$defs/InstrumentType" }, "underlying-symbol": { "title": "Underlying-Symbol", "type": "string" }, "quantity": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Quantity" }, "quantity-direction": { "title": "Quantity-Direction", "type": "string" }, "close-price": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Close-Price" }, "average-open-price": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Average-Open-Price" }, "multiplier": { "title": "Multiplier", "type": "integer" }, "cost-effect": { "title": "Cost-Effect", "type": "string" }, "is-suppressed": { "title": "Is-Suppressed", "type": "boolean" }, "is-frozen": { "title": "Is-Frozen", "type": "boolean" }, "realized-day-gain": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Realized-Day-Gain" }, "realized-today": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Realized-Today" }, "created-at": { "format": "date-time", "title": "Created-At", "type": "string" }, "updated-at": { "format": "date-time", "title": "Updated-At", "type": "string" }, "mark": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Mark" }, "mark-price": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Mark-Price" }, "restricted-quantity": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Restricted-Quantity" }, "expires-at": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "Expires-At" }, "fixing-price": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Fixing-Price" }, "deliverable-type": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Deliverable-Type" }, "average-yearly-market-close-price": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Average-Yearly-Market-Close-Price" }, "average-daily-market-close-price": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Average-Daily-Market-Close-Price" }, "realized-day-gain-date": { "anyOf": [ { "format": "date", "type": "string" }, { "type": "null" } ], "default": null, "title": "Realized-Day-Gain-Date" }, "realized-today-date": { "anyOf": [ { "format": "date", "type": "string" }, { "type": "null" } ], "default": null, "title": "Realized-Today-Date" } }, "$defs": { "InstrumentType": { "description": "This is an :class:`~enum.Enum` that contains the valid types of instruments\nand their representation in the API.", "enum": [ "Bond", "Cryptocurrency", "Currency Pair", "Equity", "Equity Offering", "Equity Option", "Fixed Income Security", "Future", "Future Option", "Index", "Liquidity Pool", "Unknown", "Warrant" ], "title": "InstrumentType", "type": "string" } }, "required": [ "account-number", "symbol", "instrument-type", "underlying-symbol", "quantity", "quantity-direction", "close-price", "average-open-price", "multiplier", "cost-effect", "is-suppressed", "is-frozen", "realized-day-gain", "realized-today", "created-at", "updated-at" ] }

average_daily_market_close_price (decimal.Decimal | None)

average_open_price (decimal.Decimal)

average_yearly_market_close_price (decimal.Decimal | None)

close_price (decimal.Decimal)

created_at (datetime.datetime)

deliverable_type (str | None)

expires_at (datetime.datetime | None)

fixing_price (decimal.Decimal | None)

instrument_type (tastytrade.order.InstrumentType)

mark (decimal.Decimal | None)

mark_price (decimal.Decimal | None)

quantity (decimal.Decimal)

quantity_direction (str)

realized_day_gain (decimal.Decimal)

realized_day_gain_date (datetime.date | None)

realized_today (decimal.Decimal)

realized_today_date (datetime.date | None)

restricted_quantity (decimal.Decimal | None)

underlying_symbol (str)

updated_at (datetime.datetime)

validate_price_effects » all fields

Show JSON schema{ "title": "EmptyDict", "type": "object", "properties": {}, "additionalProperties": false }

Bases: TastytradeData

Show JSON schema{ "title": "FeesInfo", "type": "object", "properties": { "total-fees": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Total-Fees" } }, "required": [ "total-fees" ] }

total_fees (decimal.Decimal)

validate_price_effects » all fields

Bases: TastytradeData

Dataclass containing information about the lot of a position.

Show JSON schema{ "title": "Lot", "description": "Dataclass containing information about the lot of a position.", "type": "object", "properties": { "id": { "title": "Id", "type": "string" }, "transaction-id": { "title": "Transaction-Id", "type": "integer" }, "quantity": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Quantity" }, "price": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Price" }, "quantity-direction": { "title": "Quantity-Direction", "type": "string" }, "executed-at": { "format": "date-time", "title": "Executed-At", "type": "string" }, "transaction-date": { "format": "date", "title": "Transaction-Date", "type": "string" } }, "required": [ "id", "transaction-id", "quantity", "price", "quantity-direction", "executed-at", "transaction-date" ] }

executed_at (datetime.datetime)

price (decimal.Decimal)

quantity (decimal.Decimal)

quantity_direction (str)

transaction_date (datetime.date)

Bases: TastytradeData

Dataclass containing an overall portfolio margin report.

Show JSON schema{ "title": "MarginReport", "description": "Dataclass containing an overall portfolio margin report.", "type": "object", "properties": { "account-number": { "title": "Account-Number", "type": "string" }, "description": { "title": "Description", "type": "string" }, "margin-calculation-type": { "title": "Margin-Calculation-Type", "type": "string" }, "option-level": { "title": "Option-Level", "type": "string" }, "margin-requirement": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Margin-Requirement" }, "maintenance-requirement": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Maintenance-Requirement" }, "margin-equity": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Margin-Equity" }, "option-buying-power": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Option-Buying-Power" }, "reg-t-margin-requirement": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Reg-T-Margin-Requirement" }, "reg-t-option-buying-power": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Reg-T-Option-Buying-Power" }, "maintenance-excess": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Maintenance-Excess" }, "last-state-timestamp": { "title": "Last-State-Timestamp", "type": "integer" }, "groups": { "items": { "anyOf": [ { "$ref": "#/$defs/MarginReportEntry" }, { "$ref": "#/$defs/EmptyDict" } ] }, "title": "Groups", "type": "array" }, "initial-requirement": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Initial-Requirement" } }, "$defs": { "EmptyDict": { "additionalProperties": false, "properties": {}, "title": "EmptyDict", "type": "object" }, "MarginReportEntry": { "description": "Dataclass containing an individual entry (relating to a specific position)\nas part of the overall margin report.", "properties": { "description": { "title": "Description", "type": "string" }, "code": { "title": "Code", "type": "string" }, "buying-power": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Buying-Power" }, "margin-calculation-type": { "title": "Margin-Calculation-Type", "type": "string" }, "margin-requirement": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Margin-Requirement" }, "expected-price-range-up-percent": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Expected-Price-Range-Up-Percent" }, "expected-price-range-down-percent": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Expected-Price-Range-Down-Percent" }, "groups": { "anyOf": [ { "items": { "additionalProperties": true, "type": "object" }, "type": "array" }, { "type": "null" } ], "default": null, "title": "Groups" }, "initial-requirement": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Initial-Requirement" }, "maintenance-requirement": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Maintenance-Requirement" }, "point-of-no-return-percent": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Point-Of-No-Return-Percent" }, "price-increase-percent": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Price-Increase-Percent" }, "price-decrease-percent": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Price-Decrease-Percent" }, "underlying-symbol": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Underlying-Symbol" }, "underlying-type": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Underlying-Type" } }, "required": [ "description", "code", "buying-power", "margin-calculation-type", "margin-requirement" ], "title": "MarginReportEntry", "type": "object" } }, "required": [ "account-number", "description", "margin-calculation-type", "option-level", "margin-requirement", "maintenance-requirement", "margin-equity", "option-buying-power", "reg-t-margin-requirement", "reg-t-option-buying-power", "maintenance-excess", "last-state-timestamp", "groups" ] }

groups (list[tastytrade.account.MarginReportEntry | tastytrade.account.EmptyDict])

initial_requirement (decimal.Decimal | None)

last_state_timestamp (int)

maintenance_excess (decimal.Decimal)

maintenance_requirement (decimal.Decimal)

margin_calculation_type (str)

margin_equity (decimal.Decimal)

margin_requirement (decimal.Decimal)

option_buying_power (decimal.Decimal)

reg_t_margin_requirement (decimal.Decimal)

reg_t_option_buying_power (decimal.Decimal)

validate_price_effects » all fields

Bases: TastytradeData

Dataclass containing an individual entry (relating to a specific position) as part of the overall margin report.

Show JSON schema{ "title": "MarginReportEntry", "description": "Dataclass containing an individual entry (relating to a specific position)\nas part of the overall margin report.", "type": "object", "properties": { "description": { "title": "Description", "type": "string" }, "code": { "title": "Code", "type": "string" }, "buying-power": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Buying-Power" }, "margin-calculation-type": { "title": "Margin-Calculation-Type", "type": "string" }, "margin-requirement": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Margin-Requirement" }, "expected-price-range-up-percent": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Expected-Price-Range-Up-Percent" }, "expected-price-range-down-percent": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Expected-Price-Range-Down-Percent" }, "groups": { "anyOf": [ { "items": { "additionalProperties": true, "type": "object" }, "type": "array" }, { "type": "null" } ], "default": null, "title": "Groups" }, "initial-requirement": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Initial-Requirement" }, "maintenance-requirement": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Maintenance-Requirement" }, "point-of-no-return-percent": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Point-Of-No-Return-Percent" }, "price-increase-percent": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Price-Increase-Percent" }, "price-decrease-percent": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Price-Decrease-Percent" }, "underlying-symbol": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Underlying-Symbol" }, "underlying-type": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Underlying-Type" } }, "required": [ "description", "code", "buying-power", "margin-calculation-type", "margin-requirement" ] }

buying_power (decimal.Decimal)

expected_price_range_down_percent (decimal.Decimal | None)

expected_price_range_up_percent (decimal.Decimal | None)

groups (list[dict[str, Any]] | None)

initial_requirement (decimal.Decimal | None)

maintenance_requirement (decimal.Decimal | None)

margin_calculation_type (str)

margin_requirement (decimal.Decimal)

point_of_no_return_percent (decimal.Decimal | None)

price_decrease_percent (decimal.Decimal | None)

price_increase_percent (decimal.Decimal | None)

underlying_symbol (str | None)

underlying_type (str | None)

validate_price_effects » all fields

Bases: TastytradeData

Dataclass containing historical net liquidation data in OHLC format (open, high, low, close), with a timestamp.

Show JSON schema{ "title": "NetLiqOhlc", "description": "Dataclass containing historical net liquidation data in OHLC format\n(open, high, low, close), with a timestamp.", "type": "object", "properties": { "open": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Open" }, "high": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "High" }, "low": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Low" }, "close": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Close" }, "pending-cash-open": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Pending-Cash-Open" }, "pending-cash-high": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Pending-Cash-High" }, "pending-cash-low": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Pending-Cash-Low" }, "pending-cash-close": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Pending-Cash-Close" }, "total-open": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Total-Open" }, "total-high": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Total-High" }, "total-low": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Total-Low" }, "total-close": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Total-Close" }, "time": { "title": "Time", "type": "string" } }, "required": [ "open", "high", "low", "close", "pending-cash-open", "pending-cash-high", "pending-cash-low", "pending-cash-close", "total-open", "total-high", "total-low", "total-close", "time" ] }

close (decimal.Decimal)

high (decimal.Decimal)

low (decimal.Decimal)

open (decimal.Decimal)

pending_cash_close (decimal.Decimal)

pending_cash_high (decimal.Decimal)

pending_cash_low (decimal.Decimal)

pending_cash_open (decimal.Decimal)

total_close (decimal.Decimal)

total_high (decimal.Decimal)

total_low (decimal.Decimal)

total_open (decimal.Decimal)

Bases: TastytradeData

Dataclass containing information about an account’s trading status, such as what types of trades are allowed (e.g. margin, crypto, futures)

Show JSON schema{ "title": "TradingStatus", "description": "Dataclass containing information about an account's trading status, such\nas what types of trades are allowed (e.g. margin, crypto, futures)", "type": "object", "properties": { "account-number": { "title": "Account-Number", "type": "string" }, "equities-margin-calculation-type": { "title": "Equities-Margin-Calculation-Type", "type": "string" }, "fee-schedule-name": { "title": "Fee-Schedule-Name", "type": "string" }, "futures-margin-rate-multiplier": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Futures-Margin-Rate-Multiplier" }, "has-intraday-equities-margin": { "title": "Has-Intraday-Equities-Margin", "type": "boolean" }, "id": { "title": "Id", "type": "integer" }, "is-aggregated-at-clearing": { "title": "Is-Aggregated-At-Clearing", "type": "boolean" }, "is-closed": { "title": "Is-Closed", "type": "boolean" }, "is-closing-only": { "title": "Is-Closing-Only", "type": "boolean" }, "is-cryptocurrency-enabled": { "title": "Is-Cryptocurrency-Enabled", "type": "boolean" }, "is-frozen": { "title": "Is-Frozen", "type": "boolean" }, "is-full-equity-margin-required": { "title": "Is-Full-Equity-Margin-Required", "type": "boolean" }, "is-futures-closing-only": { "title": "Is-Futures-Closing-Only", "type": "boolean" }, "is-futures-intra-day-enabled": { "title": "Is-Futures-Intra-Day-Enabled", "type": "boolean" }, "is-futures-enabled": { "title": "Is-Futures-Enabled", "type": "boolean" }, "is-in-day-trade-equity-maintenance-call": { "title": "Is-In-Day-Trade-Equity-Maintenance-Call", "type": "boolean" }, "is-in-margin-call": { "title": "Is-In-Margin-Call", "type": "boolean" }, "is-pattern-day-trader": { "title": "Is-Pattern-Day-Trader", "type": "boolean" }, "is-small-notional-futures-intra-day-enabled": { "title": "Is-Small-Notional-Futures-Intra-Day-Enabled", "type": "boolean" }, "is-roll-the-day-forward-enabled": { "title": "Is-Roll-The-Day-Forward-Enabled", "type": "boolean" }, "are-far-otm-net-options-restricted": { "title": "Are-Far-Otm-Net-Options-Restricted", "type": "boolean" }, "options-level": { "title": "Options-Level", "type": "string" }, "short-calls-enabled": { "title": "Short-Calls-Enabled", "type": "boolean" }, "small-notional-futures-margin-rate-multiplier": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Small-Notional-Futures-Margin-Rate-Multiplier" }, "is-equity-offering-enabled": { "title": "Is-Equity-Offering-Enabled", "type": "boolean" }, "is-equity-offering-closing-only": { "title": "Is-Equity-Offering-Closing-Only", "type": "boolean" }, "updated-at": { "format": "date-time", "title": "Updated-At", "type": "string" }, "is-portfolio-margin-enabled": { "anyOf": [ { "type": "boolean" }, { "type": "null" } ], "default": null, "title": "Is-Portfolio-Margin-Enabled" }, "is-risk-reducing-only": { "anyOf": [ { "type": "boolean" }, { "type": "null" } ], "default": null, "title": "Is-Risk-Reducing-Only" }, "day-trade-count": { "anyOf": [ { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Day-Trade-Count" }, "autotrade-account-type": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Autotrade-Account-Type" }, "clearing-account-number": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Clearing-Account-Number" }, "clearing-aggregation-identifier": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Clearing-Aggregation-Identifier" }, "is-cryptocurrency-closing-only": { "anyOf": [ { "type": "boolean" }, { "type": "null" } ], "default": null, "title": "Is-Cryptocurrency-Closing-Only" }, "pdt-reset-on": { "anyOf": [ { "format": "date", "type": "string" }, { "type": "null" } ], "default": null, "title": "Pdt-Reset-On" }, "cmta-override": { "anyOf": [ { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Cmta-Override" }, "enhanced-fraud-safeguards-enabled-at": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "Enhanced-Fraud-Safeguards-Enabled-At" } }, "required": [ "account-number", "equities-margin-calculation-type", "fee-schedule-name", "futures-margin-rate-multiplier", "has-intraday-equities-margin", "id", "is-aggregated-at-clearing", "is-closed", "is-closing-only", "is-cryptocurrency-enabled", "is-frozen", "is-full-equity-margin-required", "is-futures-closing-only", "is-futures-intra-day-enabled", "is-futures-enabled", "is-in-day-trade-equity-maintenance-call", "is-in-margin-call", "is-pattern-day-trader", "is-small-notional-futures-intra-day-enabled", "is-roll-the-day-forward-enabled", "are-far-otm-net-options-restricted", "options-level", "short-calls-enabled", "small-notional-futures-margin-rate-multiplier", "is-equity-offering-enabled", "is-equity-offering-closing-only", "updated-at" ] }

are_far_otm_net_options_restricted (bool)

autotrade_account_type (str | None)

clearing_account_number (str | None)

clearing_aggregation_identifier (str | None)

cmta_override (int | None)

day_trade_count (int | None)

enhanced_fraud_safeguards_enabled_at (datetime.datetime | None)

equities_margin_calculation_type (str)

fee_schedule_name (str)

futures_margin_rate_multiplier (decimal.Decimal)

has_intraday_equities_margin (bool)

is_aggregated_at_clearing (bool)

is_closing_only (bool)

is_cryptocurrency_closing_only (bool | None)

is_cryptocurrency_enabled (bool)

is_equity_offering_closing_only (bool)

is_equity_offering_enabled (bool)

is_full_equity_margin_required (bool)

is_futures_closing_only (bool)

is_futures_enabled (bool)

is_futures_intra_day_enabled (bool)

is_in_day_trade_equity_maintenance_call (bool)

is_in_margin_call (bool)

is_pattern_day_trader (bool)

is_portfolio_margin_enabled (bool | None)

is_risk_reducing_only (bool | None)

is_roll_the_day_forward_enabled (bool)

is_small_notional_futures_intra_day_enabled (bool)

pdt_reset_on (datetime.date | None)

short_calls_enabled (bool)

small_notional_futures_margin_rate_multiplier (decimal.Decimal)

updated_at (datetime.datetime)

Bases: TastytradeData

Dataclass containing information about a past transaction.

Show JSON schema{ "title": "Transaction", "description": "Dataclass containing information about a past transaction.", "type": "object", "properties": { "id": { "title": "Id", "type": "integer" }, "account-number": { "title": "Account-Number", "type": "string" }, "transaction-type": { "title": "Transaction-Type", "type": "string" }, "transaction-sub-type": { "title": "Transaction-Sub-Type", "type": "string" }, "description": { "title": "Description", "type": "string" }, "executed-at": { "format": "date-time", "title": "Executed-At", "type": "string" }, "transaction-date": { "format": "date", "title": "Transaction-Date", "type": "string" }, "value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Value" }, "net-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Net-Value" }, "is-estimated-fee": { "title": "Is-Estimated-Fee", "type": "boolean" }, "symbol": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Symbol" }, "instrument-type": { "anyOf": [ { "$ref": "#/$defs/InstrumentType" }, { "type": "null" } ], "default": null }, "underlying-symbol": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Underlying-Symbol" }, "action": { "anyOf": [ { "$ref": "#/$defs/OrderAction" }, { "type": "null" } ], "default": null }, "quantity": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Quantity" }, "price": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Price" }, "regulatory-fees": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Regulatory-Fees" }, "clearing-fees": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Clearing-Fees" }, "commission": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Commission" }, "proprietary-index-option-fees": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Proprietary-Index-Option-Fees" }, "ext-exchange-order-number": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Ext-Exchange-Order-Number" }, "ext-global-order-number": { "anyOf": [ { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Ext-Global-Order-Number" }, "ext-group-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Ext-Group-Id" }, "ext-group-fill-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Ext-Group-Fill-Id" }, "ext-exec-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Ext-Exec-Id" }, "exec-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Exec-Id" }, "exchange": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Exchange" }, "order-id": { "anyOf": [ { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Order-Id" }, "exchange-affiliation-identifier": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Exchange-Affiliation-Identifier" }, "leg-count": { "anyOf": [ { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Leg-Count" }, "destination-venue": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Destination-Venue" }, "other-charge": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Other-Charge" }, "other-charge-description": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Other-Charge-Description" }, "reverses-id": { "anyOf": [ { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Reverses-Id" }, "cost-basis-reconciliation-date": { "anyOf": [ { "format": "date", "type": "string" }, { "type": "null" } ], "default": null, "title": "Cost-Basis-Reconciliation-Date" }, "lots": { "anyOf": [ { "items": { "$ref": "#/$defs/Lot" }, "type": "array" }, { "type": "null" } ], "default": null, "title": "Lots" }, "agency-price": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Agency-Price" }, "principal-price": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Principal-Price" } }, "$defs": { "InstrumentType": { "description": "This is an :class:`~enum.Enum` that contains the valid types of instruments\nand their representation in the API.", "enum": [ "Bond", "Cryptocurrency", "Currency Pair", "Equity", "Equity Offering", "Equity Option", "Fixed Income Security", "Future", "Future Option", "Index", "Liquidity Pool", "Unknown", "Warrant" ], "title": "InstrumentType", "type": "string" }, "Lot": { "description": "Dataclass containing information about the lot of a position.", "properties": { "id": { "title": "Id", "type": "string" }, "transaction-id": { "title": "Transaction-Id", "type": "integer" }, "quantity": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Quantity" }, "price": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Price" }, "quantity-direction": { "title": "Quantity-Direction", "type": "string" }, "executed-at": { "format": "date-time", "title": "Executed-At", "type": "string" }, "transaction-date": { "format": "date", "title": "Transaction-Date", "type": "string" } }, "required": [ "id", "transaction-id", "quantity", "price", "quantity-direction", "executed-at", "transaction-date" ], "title": "Lot", "type": "object" }, "OrderAction": { "description": "This is an :class:`~enum.Enum` that contains the valid order actions.", "enum": [ "Buy to Open", "Buy to Close", "Sell to Open", "Sell to Close", "Buy", "Sell" ], "title": "OrderAction", "type": "string" } }, "required": [ "id", "account-number", "transaction-type", "transaction-sub-type", "description", "executed-at", "transaction-date", "value", "net-value", "is-estimated-fee" ] }

action (tastytrade.order.OrderAction | None)

agency_price (decimal.Decimal | None)

clearing_fees (decimal.Decimal | None)

commission (decimal.Decimal | None)

cost_basis_reconciliation_date (datetime.date | None)

destination_venue (str | None)

exchange (str | None)

exchange_affiliation_identifier (str | None)

executed_at (datetime.datetime)

ext_exchange_order_number (str | None)

ext_exec_id (str | None)

ext_global_order_number (int | None)

ext_group_fill_id (str | None)

ext_group_id (str | None)

instrument_type (tastytrade.order.InstrumentType | None)

is_estimated_fee (bool)

leg_count (int | None)

lots (list[tastytrade.account.Lot] | None)

net_value (decimal.Decimal)

order_id (int | None)

other_charge (decimal.Decimal | None)

other_charge_description (str | None)

price (decimal.Decimal | None)

principal_price (decimal.Decimal | None)

proprietary_index_option_fees (decimal.Decimal | None)

quantity (decimal.Decimal | None)

regulatory_fees (decimal.Decimal | None)

reverses_id (int | None)

transaction_date (datetime.date)

transaction_sub_type (str)

transaction_type (str)

underlying_symbol (str | None)

value (decimal.Decimal)

validate_price_effects » all fields

**Examples:**

Example 1 (json):
```json
{
   "title": "Account",
   "description": "Dataclass that represents a Tastytrade account object, containing\nmethods for retrieving information about the account, placing orders,\nand retrieving past transactions.",
   "type": "object",
   "properties": {
      "account-number": {
         "title": "Account-Number",
         "type": "string"
      },
      "opened-at": {
         "format": "date-time",
         "title": "Opened-At",
         "type": "string"
      },
      "nickname": {
         "title": "Nickname",
         "type": "string"
      },
      "account-type-name": {
         "title": "Account-Type-Name",
         "type": "string"
      },
      "is-closed": {
         "title": "Is-Closed",
         "type": "boolean"
      },
      "day-trader-status": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "boolean"
            }
         ],
         "title": "Day-Trader-Status"
      },
      "is-firm-error": {
         "title": "Is-Firm-Error",
         "type": "boolean"
      },
      "is-firm-proprietary": {
         "title": "Is-Firm-Proprietary",
         "type": "boolean"
      },
      "is-futures-approved": {
         "title": "Is-Futures-Approved",
         "type": "boolean"
      },
      "is-test-drive": {
         "default": false,
         "title": "Is-Test-Drive",
         "type": "boolean"
      },
      "margin-or-cash": {
         "title": "Margin-Or-Cash",
         "type": "string"
      },
      "is-foreign": {
         "title": "Is-Foreign",
         "type": "boolean"
      },
      "created-at": {
         "format": "date-time",
         "title": "Created-At",
         "type": "string"
      },
      "external-id": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "External-Id"
      },
      "closed-at": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Closed-At"
      },
      "funding-date": {
         "anyOf": [
            {
               "format": "date",
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Funding-Date"
      },
      "investment-objective": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Investment-Objective"
      },
      "liquidity-needs": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Liquidity-Needs"
      },
      "risk-tolerance": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Risk-Tolerance"
      },
      "investment-time-horizon": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Investment-Time-Horizon"
      },
      "futures-account-purpose": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Futures-Account-Purpose"
      },
      "external-fdid": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "External-Fdid"
      },
      "suitable-options-level": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Suitable-Options-Level"
      },
      "submitting-user-id": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Submitting-User-Id"
      }
   },
   "required": [
      "account-number",
      "opened-at",
      "nickname",
      "account-type-name",
      "is-closed",
      "day-trader-status",
      "is-firm-error",
      "is-firm-proprietary",
      "is-futures-approved",
      "margin-or-cash",
      "is-foreign",
      "created-at"
   ]
}
```

Example 2 (json):
```json
{
   "title": "AccountBalance",
   "description": "Dataclass containing account balance information.",
   "type": "object",
   "properties": {
      "account-number": {
         "title": "Account-Number",
         "type": "string"
      },
      "cash-balance": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Cash-Balance"
      },
      "long-equity-value": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Long-Equity-Value"
      },
      "short-equity-value": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Short-Equity-Value"
      },
      "long-derivative-value": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Long-Derivative-Value"
      },
      "short-derivative-value": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Short-Derivative-Value"
      },
      "long-futures-value": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Long-Futures-Value"
      },
      "short-futures-value": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Short-Futures-Value"
      },
      "long-futures-derivative-value": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Long-Futures-Derivative-Value"
      },
      "short-futures-derivative-value": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Short-Futures-Derivative-Value"
      },
      "long-margineable-value": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Long-Margineable-Value"
      },
      "short-margineable-value": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Short-Margineable-Value"
      },
      "margin-equity": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Margin-Equity"
      },
      "equity-buying-power": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Equity-Buying-Power"
      },
      "derivative-buying-power": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Derivative-Buying-Power"
      },
      "day-trading-buying-power": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Day-Trading-Buying-Power"
      },
      "futures-margin-requirement": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Futures-Margin-Requirement"
      },
      "available-trading-funds": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Available-Trading-Funds"
      },
      "maintenance-requirement": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Maintenance-Requirement"
      },
      "maintenance-call-value": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Maintenance-Call-Value"
      },
      "reg-t-call-value": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Reg-T-Call-Value"
      },
      "day-trading-call-value": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Day-Trading-Call-Value"
      },
      "day-equity-call-value": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Day-Equity-Call-Value"
      },
      "net-liquidating-value": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Net-Liquidating-Value"
      },
      "cash-available-to-withdraw": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Cash-Available-To-Withdraw"
      },
      "day-trade-excess": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Day-Trade-Excess"
      },
      "pending-cash": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Pending-Cash"
      },
      "long-cryptocurrency-value": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Long-Cryptocurrency-Value"
      },
      "short-cryptocurrency-value": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Short-Cryptocurrency-Value"
      },
      "cryptocurrency-margin-requirement": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Cryptocurrency-Margin-Requirement"
      },
      "unsettled-cryptocurrency-fiat-amount": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Unsettled-Cryptocurrency-Fiat-Amount"
      },
      "closed-loop-available-balance": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Closed-Loop-Available-Balance"
      },
      "equity-offering-margin-requirement": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Equity-Offering-Margin-Requirement"
      },
      "long-bond-value": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Long-Bond-Value"
      },
      "bond-margin-requirement": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Bond-Margin-Requirement"
      },
      "used-derivative-buying-power": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Used-Derivative-Buying-Power"
      },
      "snapshot-date": {
         "format": "date",
         "title": "Snapshot-Date",
         "type": "string"
      },
      "reg-t-margin-requirement": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Reg-T-Margin-Requirement"
      },
      "futures-overnight-margin-requirement": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Futures-Overnight-Margin-Requirement"
      },
      "futures-intraday-margin-requirement": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Futures-Intraday-Margin-Requirement"
      },
      "maintenance-excess": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Maintenance-Excess"
      },
      "pending-margin-interest": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Pending-Margin-Interest"
      },
      "effective-cryptocurrency-buying-power": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Effective-Cryptocurrency-Buying-Power"
      },
      "updated-at": {
         "format": "date-time",
         "title": "Updated-At",
         "type": "string"
      },
      "apex-starting-day-margin-equity": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Apex-Starting-Day-Margin-Equity"
      },
      "buying-power-adjustment": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Buying-Power-Adjustment"
      },
      "time-of-day": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Time-Of-Day"
      }
   },
   "required": [
      "account-number",
      "cash-balance",
      "long-equity-value",
      "short-equity-value",
      "long-derivative-value",
      "short-derivative-value",
      "long-futures-value",
      "short-futures-value",
      "long-futures-derivative-value",
      "short-futures-derivative-value",
      "long-margineable-value",
      "short-margineable-value",
      "margin-equity",
      "equity-buying-power",
      "derivative-buying-power",
      "day-trading-buying-power",
      "futures-margin-requirement",
      "available-trading-funds",
      "maintenance-requirement",
      "maintenance-call-value",
      "reg-t-call-value",
      "day-trading-call-value",
      "day-equity-call-value",
      "net-liquidating-value",
      "cash-available-to-withdraw",
      "day-trade-excess",
      "pending-cash",
      "long-cryptocurrency-value",
      "short-cryptocurrency-value",
      "cryptocurrency-margin-requirement",
      "unsettled-cryptocurrency-fiat-amount",
      "closed-loop-available-balance",
      "equity-offering-margin-requirement",
      "long-bond-value",
      "bond-margin-requirement",
      "used-derivative-buying-power",
      "snapshot-date",
      "reg-t-margin-requirement",
      "futures-overnight-margin-requirement",
      "futures-intraday-margin-requirement",
      "maintenance-excess",
      "pending-margin-interest",
      "effective-cryptocurrency-buying-power",
      "updated-at"
   ]
}
```

Example 3 (json):
```json
{
   "title": "AccountBalanceSnapshot",
   "description": "Dataclass containing account balance for a moment in time (snapshot).",
   "type": "object",
   "properties": {
      "account-number": {
         "title": "Account-Number",
         "type": "string"
      },
      "cash-balance": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Cash-Balance"
      },
      "long-equity-value": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Long-Equity-Value"
      },
      "short-equity-value": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Short-Equity-Value"
      },
      "long-derivative-value": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Long-Derivative-Value"
      },
      "short-derivative-value": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Short-Derivative-Value"
      },
      "long-futures-value": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Long-Futures-Value"
      },
      "short-futures-value": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Short-Futures-Value"
      },
      "long-futures-derivative-value": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Long-Futures-Derivative-Value"
      },
      "short-futures-derivative-value": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Short-Futures-Derivative-Value"
      },
      "long-margineable-value": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Long-Margineable-Value"
      },
      "short-margineable-value": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Short-Margineable-Value"
      },
      "margin-equity": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Margin-Equity"
      },
      "equity-buying-power": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Equity-Buying-Power"
      },
      "derivative-buying-power": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Derivative-Buying-Power"
      },
      "day-trading-buying-power": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Day-Trading-Buying-Power"
      },
      "futures-margin-requirement": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Futures-Margin-Requirement"
      },
      "available-trading-funds": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Available-Trading-Funds"
      },
      "maintenance-requirement": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Maintenance-Requirement"
      },
      "maintenance-call-value": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Maintenance-Call-Value"
      },
      "reg-t-call-value": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Reg-T-Call-Value"
      },
      "day-trading-call-value": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Day-Trading-Call-Value"
      },
      "day-equity-call-value": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Day-Equity-Call-Value"
      },
      "net-liquidating-value": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Net-Liquidating-Value"
      },
      "cash-available-to-withdraw": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Cash-Available-To-Withdraw"
      },
      "day-trade-excess": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Day-Trade-Excess"
      },
      "pending-cash": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Pending-Cash"
      },
      "snapshot-date": {
         "format": "date",
         "title": "Snapshot-Date",
         "type": "string"
      },
      "time-of-day": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Time-Of-Day"
      },
      "long-cryptocurrency-value": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Long-Cryptocurrency-Value"
      },
      "short-cryptocurrency-value": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Short-Cryptocurrency-Value"
      },
      "cryptocurrency-margin-requirement": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Cryptocurrency-Margin-Requirement"
      },
      "unsettled-cryptocurrency-fiat-amount": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Unsettled-Cryptocurrency-Fiat-Amount"
      },
      "closed-loop-available-balance": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Closed-Loop-Available-Balance"
      },
      "equity-offering-margin-requirement": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Equity-Offering-Margin-Requirement"
      },
      "long-bond-value": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Long-Bond-Value"
      },
      "bond-margin-requirement": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Bond-Margin-Requirement"
      },
      "used-derivative-buying-power": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Used-Derivative-Buying-Power"
      }
   },
   "required": [
      "account-number",
      "cash-balance",
      "long-equity-value",
      "short-equity-value",
      "long-derivative-value",
      "short-derivative-value",
      "long-futures-value",
      "short-futures-value",
      "long-futures-derivative-value",
      "short-futures-derivative-value",
      "long-margineable-value",
      "short-margineable-value",
      "margin-equity",
      "equity-buying-power",
      "derivative-buying-power",
      "day-trading-buying-power",
      "futures-margin-requirement",
      "available-trading-funds",
      "maintenance-requirement",
      "maintenance-call-value",
      "reg-t-call-value",
      "day-trading-call-value",
      "day-equity-call-value",
      "net-liquidating-value",
      "cash-available-to-withdraw",
      "day-trade-excess",
      "pending-cash",
      "snapshot-date"
   ]
}
```

Example 4 (json):
```json
{
   "title": "CurrentPosition",
   "description": "Dataclass containing imformation about an individual position in a\nportfolio.",
   "type": "object",
   "properties": {
      "account-number": {
         "title": "Account-Number",
         "type": "string"
      },
      "symbol": {
         "title": "Symbol",
         "type": "string"
      },
      "instrument-type": {
         "$ref": "#/$defs/InstrumentType"
      },
      "underlying-symbol": {
         "title": "Underlying-Symbol",
         "type": "string"
      },
      "quantity": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Quantity"
      },
      "quantity-direction": {
         "title": "Quantity-Direction",
         "type": "string"
      },
      "close-price": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Close-Price"
      },
      "average-open-price": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Average-Open-Price"
      },
      "multiplier": {
         "title": "Multiplier",
         "type": "integer"
      },
      "cost-effect": {
         "title": "Cost-Effect",
         "type": "string"
      },
      "is-suppressed": {
         "title": "Is-Suppressed",
         "type": "boolean"
      },
      "is-frozen": {
         "title": "Is-Frozen",
         "type": "boolean"
      },
      "realized-day-gain": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Realized-Day-Gain"
      },
      "realized-today": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Realized-Today"
      },
      "created-at": {
         "format": "date-time",
         "title": "Created-At",
         "type": "string"
      },
      "updated-at": {
         "format": "date-time",
         "title": "Updated-At",
         "type": "string"
      },
      "mark": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Mark"
      },
      "mark-price": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Mark-Price"
      },
      "restricted-quantity": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Restricted-Quantity"
      },
      "expires-at": {
         "anyOf": [
            {
               "format": "date-time",
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Expires-At"
      },
      "fixing-price": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Fixing-Price"
      },
      "deliverable-type": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Deliverable-Type"
      },
      "average-yearly-market-close-price": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Average-Yearly-Market-Close-Price"
      },
      "average-daily-market-close-price": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Average-Daily-Market-Close-Price"
      },
      "realized-day-gain-date": {
         "anyOf": [
            {
               "format": "date",
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Realized-Day-Gain-Date"
      },
      "realized-today-date": {
         "anyOf": [
            {
               "format": "date",
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Realized-Today-Date"
      }
   },
   "$defs": {
      "InstrumentType": {
         "description": "This is an :class:`~enum.Enum` that contains the valid types of instruments\nand their representation in the API.",
         "enum": [
            "Bond",
            "Cryptocurrency",
            "Currency Pair",
            "Equity",
            "Equity Offering",
            "Equity Option",
            "Fixed Income Security",
            "Future",
            "Future Option",
            "Index",
            "Liquidity Pool",
            "Unknown",
            "Warrant"
         ],
         "title": "InstrumentType",
         "type": "string"
      }
   },
   "required": [
      "account-number",
      "symbol",
      "instrument-type",
      "underlying-symbol",
      "quantity",
      "quantity-direction",
      "close-price",
      "average-open-price",
      "multiplier",
      "cost-effect",
      "is-suppressed",
      "is-frozen",
      "realized-day-gain",
      "realized-today",
      "created-at",
      "updated-at"
   ]
}
```

---

## tastytrade.market_sessions - tastytrade 11.1.0 documentation

**URL:** https://tastyworks-api.readthedocs.io/en/latest/api/market-sessions.html

**Contents:**
- tastytrade.market_sessions¶

Contains the valid exchanges to get futures market sessions for.

Valid values are as follows:

Bases: TastytradeData

Dataclass containing information about market holidays and shortened days.

Show JSON schema{ "title": "MarketCalendar", "description": "Dataclass containing information about market holidays and shortened days.", "type": "object", "properties": { "market-half-days": { "items": { "format": "date", "type": "string" }, "title": "Market-Half-Days", "type": "array" }, "market-holidays": { "items": { "format": "date", "type": "string" }, "title": "Market-Holidays", "type": "array" } }, "required": [ "market-half-days", "market-holidays" ] }

half_days (list[datetime.date])

holidays (list[datetime.date])

Bases: TastytradeData

Dataclass representing the current, next, and previous sessions.

Show JSON schema{ "title": "MarketSession", "description": "Dataclass representing the current, next, and previous sessions.", "type": "object", "properties": { "close-at": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "Close-At" }, "close-at-ext": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "Close-At-Ext" }, "instrument-collection": { "title": "Instrument-Collection", "type": "string" }, "open-at": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "Open-At" }, "start-at": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "Start-At" }, "next-session": { "anyOf": [ { "$ref": "#/$defs/MarketSessionSnapshot" }, { "type": "null" } ], "default": null }, "previous-session": { "anyOf": [ { "$ref": "#/$defs/MarketSessionSnapshot" }, { "type": "null" } ], "default": null }, "state": { "$ref": "#/$defs/MarketStatus" } }, "$defs": { "MarketSessionSnapshot": { "description": "Dataclass containing information about the upcoming or previous market session.", "properties": { "close-at": { "format": "date-time", "title": "Close-At", "type": "string" }, "close-at-ext": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "Close-At-Ext" }, "instrument-collection": { "title": "Instrument-Collection", "type": "string" }, "open-at": { "format": "date-time", "title": "Open-At", "type": "string" }, "session-date": { "format": "date", "title": "Session-Date", "type": "string" }, "start-at": { "format": "date-time", "title": "Start-At", "type": "string" } }, "required": [ "close-at", "instrument-collection", "open-at", "session-date", "start-at" ], "title": "MarketSessionSnapshot", "type": "object" }, "MarketStatus": { "description": "Contains the valid market status values.", "enum": [ "Open", "Closed", "Pre-market", "Extended" ], "title": "MarketStatus", "type": "string" } }, "required": [ "instrument-collection", "state" ] }

close_at (datetime.datetime | None)

close_at_ext (datetime.datetime | None)

instrument_collection (str)

next_session (tastytrade.market_sessions.MarketSessionSnapshot | None)

open_at (datetime.datetime | None)

previous_session (tastytrade.market_sessions.MarketSessionSnapshot | None)

start_at (datetime.datetime | None)

status (tastytrade.market_sessions.MarketStatus)

Bases: TastytradeData

Dataclass containing information about the upcoming or previous market session.

Show JSON schema{ "title": "MarketSessionSnapshot", "description": "Dataclass containing information about the upcoming or previous market session.", "type": "object", "properties": { "close-at": { "format": "date-time", "title": "Close-At", "type": "string" }, "close-at-ext": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "Close-At-Ext" }, "instrument-collection": { "title": "Instrument-Collection", "type": "string" }, "open-at": { "format": "date-time", "title": "Open-At", "type": "string" }, "session-date": { "format": "date", "title": "Session-Date", "type": "string" }, "start-at": { "format": "date-time", "title": "Start-At", "type": "string" } }, "required": [ "close-at", "instrument-collection", "open-at", "session-date", "start-at" ] }

close_at (datetime.datetime)

close_at_ext (datetime.datetime | None)

instrument_collection (str)

open_at (datetime.datetime)

session_date (datetime.date)

start_at (datetime.datetime)

Contains the valid market status values.

Valid values are as follows:

Retrieves market calendar for half days and holidays for a futures exchange.

active user session to use

exchange to fetch calendar for

Retrieves market calendar for half days and holidays.

active user session to use

Retrieves a list of session timings for the given exchanges.

active user session to use

the list of exchanges to get market sessions for

Retrieves market calendar for half days and holidays for a futures exchange.

active user session to use

exchange to fetch calendar for

Retrieves market calendar for half days and holidays.

active user session to use

Retrieves a list of session timings for the given exchanges.

active user session to use

the list of exchanges to get market sessions for

**Examples:**

Example 1 (json):
```json
{
   "title": "MarketCalendar",
   "description": "Dataclass containing information about market holidays and shortened days.",
   "type": "object",
   "properties": {
      "market-half-days": {
         "items": {
            "format": "date",
            "type": "string"
         },
         "title": "Market-Half-Days",
         "type": "array"
      },
      "market-holidays": {
         "items": {
            "format": "date",
            "type": "string"
         },
         "title": "Market-Holidays",
         "type": "array"
      }
   },
   "required": [
      "market-half-days",
      "market-holidays"
   ]
}
```

Example 2 (json):
```json
{
   "title": "MarketSession",
   "description": "Dataclass representing the current, next, and previous sessions.",
   "type": "object",
   "properties": {
      "close-at": {
         "anyOf": [
            {
               "format": "date-time",
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Close-At"
      },
      "close-at-ext": {
         "anyOf": [
            {
               "format": "date-time",
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Close-At-Ext"
      },
      "instrument-collection": {
         "title": "Instrument-Collection",
         "type": "string"
      },
      "open-at": {
         "anyOf": [
            {
               "format": "date-time",
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Open-At"
      },
      "start-at": {
         "anyOf": [
            {
               "format": "date-time",
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Start-At"
      },
      "next-session": {
         "anyOf": [
            {
               "$ref": "#/$defs/MarketSessionSnapshot"
            },
            {
               "type": "null"
            }
         ],
         "default": null
      },
      "previous-session": {
         "anyOf": [
            {
               "$ref": "#/$defs/MarketSessionSnapshot"
            },
            {
               "type": "null"
            }
         ],
         "default": null
      },
      "state": {
         "$ref": "#/$defs/MarketStatus"
      }
   },
   "$defs": {
      "MarketSessionSnapshot": {
         "description": "Dataclass containing information about the upcoming or previous market session.",
         "properties": {
            "close-at": {
               "format": "date-time",
               "title": "Close-At",
               "type": "string"
            },
            "close-at-ext": {
               "anyOf": [
                  {
                     "format": "date-time",
                     "type": "string"
                  },
                  {
                     "type": "null"
                  }
               ],
               "default": null,
               "title": "Close-At-Ext"
            },
            "instrument-collection": {
               "title": "Instrument-Collection",
               "type": "string"
            },
            "open-at": {
               "format": "date-time",
               "title": "Open-At",
               "type": "string"
            },
            "session-date": {
               "format": "date",
               "title": "Session-Date",
               "type": "string"
            },
            "start-at": {
               "format": "date-time",
               "title": "Start-At",
               "type": "string"
            }
         },
         "required": [
            "close-at",
            "instrument-collection",
            "open-at",
            "session-date",
            "start-at"
         ],
         "title": "MarketSessionSnapshot",
         "type": "object"
      },
      "MarketStatus": {
         "description": "Contains the valid market status values.",
         "enum": [
            "Open",
            "Closed",
            "Pre-market",
            "Extended"
         ],
         "title": "MarketStatus",
         "type": "string"
      }
   },
   "required": [
      "instrument-collection",
      "state"
   ]
}
```

Example 3 (json):
```json
{
   "title": "MarketSessionSnapshot",
   "description": "Dataclass containing information about the upcoming or previous market session.",
   "type": "object",
   "properties": {
      "close-at": {
         "format": "date-time",
         "title": "Close-At",
         "type": "string"
      },
      "close-at-ext": {
         "anyOf": [
            {
               "format": "date-time",
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Close-At-Ext"
      },
      "instrument-collection": {
         "title": "Instrument-Collection",
         "type": "string"
      },
      "open-at": {
         "format": "date-time",
         "title": "Open-At",
         "type": "string"
      },
      "session-date": {
         "format": "date",
         "title": "Session-Date",
         "type": "string"
      },
      "start-at": {
         "format": "date-time",
         "title": "Start-At",
         "type": "string"
      }
   },
   "required": [
      "close-at",
      "instrument-collection",
      "open-at",
      "session-date",
      "start-at"
   ]
}
```

---

## Orders - tastytrade 11.1.0 documentation

**URL:** https://tastyworks-api.readthedocs.io/en/latest/orders.html

**Contents:**
- Orders¶
- Placing an order¶
- Managing orders¶
- Complex Orders¶
- Notional market orders¶
- Cryptocurrency market orders¶

Notice the use of the dry_run parameter in the call to place_order. This is used to calculate the effects that an order would have on the account’s buying power and the fees that would be charged without actually placing the order. This is typically used to provide an order confirmation screen before sending the order. To send the order, pass dry_run=False, and the response will be populated with a PlacedOrderResponse, which contains information about the order and account. Also, rather than using an explicit credit/debit toggle like the Tastytrade platform, the SDK simply assumes negative numbers are debits and positive ones are credits.

Once we’ve placed an order, it’s often necessary to modify or cancel the order for a variety of reasons. Thankfully, this is easy and handled through the Account object:

Cancelling an order is similar:

Placed orders are assigned a status, like “Received”, “Cancelled”, or “Filled”. To watch for status changes in real time, you can use the Account Streamer. To get current order status, you can just call get_live_orders. (The name is somewhat misleading! It returns not only live orders, but also cancelled and filled ones over the past 24 hours.)

For less recent orders, we can get the full order history with get_order_history.

Tastytrade supports two kinds of complex orders, “OCO” and “OTOCO”, which are explained here.

To create an OTOCO order, you need an entry point order, a stop loss order, and a profit-taking order:

An OCO order is similar, but has no trigger order. It’s used to add a profit-taking and a stop loss order to an existing position. Here’s an example, assuming the account already has an open position of 10 long shares of SPY:

Note that to cancel complex orders, you need to use the delete_complex_order function, NOT delete_order.

Notional orders are slightly different from normal orders. Since the market will determine both the quantity and the price for you, you need to pass value instead of price, and pass None for the quantity parameter to build_leg.

Cryptocurrency market orders should use the special IOC TIF:

**Examples:**

Example 1 (swift):
```swift
from decimal import Decimal
from tastytrade import Account
from tastytrade.instruments import Equity
from tastytrade.order import *

account = Account.get(session, '5WX01234')
symbol = Equity.get(session, 'USO')
leg = symbol.build_leg(Decimal('5'), OrderAction.BUY_TO_OPEN)  # buy to open 5 shares

order = NewOrder(
    time_in_force=OrderTimeInForce.DAY,
    order_type=OrderType.LIMIT,
    legs=[leg],  # you can have multiple legs in an order
    price=Decimal('-10')  # limit price, $10/share debit for a total value of $50
)
response = account.place_order(session, order, dry_run=True)  # a test order
print(response)
```

Example 2 (rust):
```rust
>>> PlacedOrderResponse(buying_power_effect=BuyingPowerEffect(change_in_margin_requirement=Decimal('125.0'), change_in_margin_requirement_effect=<PriceEffect.DEBIT: 'Debit'>, change_in_buying_power=Decimal('125.004'), change_in_buying_power_effect=<PriceEffect.DEBIT: 'Debit'>, current_buying_power=Decimal('1000.0'), current_buying_power_effect=<PriceEffect.CREDIT: 'Credit'>, new_buying_power=Decimal('874.996'), new_buying_power_effect=<PriceEffect.CREDIT: 'Credit'>, isolated_order_margin_requirement=Decimal('125.0'), isolated_order_margin_requirement_effect=<PriceEffect.DEBIT: 'Debit'>, is_spread=False, impact=Decimal('125.004'), effect=<PriceEffect.DEBIT: 'Debit'>), fee_calculation=FeeCalculation(regulatory_fees=Decimal('0.0'), regulatory_fees_effect=<PriceEffect.NONE: 'None'>, clearing_fees=Decimal('0.004'), clearing_fees_effect=<PriceEffect.DEBIT: 'Debit'>, commission=Decimal('0.0'), commission_effect=<PriceEffect.NONE: 'None'>, proprietary_index_option_fees=Decimal('0.0'), proprietary_index_option_fees_effect=<PriceEffect.NONE: 'None'>, total_fees=Decimal('0.004'), total_fees_effect=<PriceEffect.DEBIT: 'Debit'>), order=PlacedOrder(account_number='5WV69754', time_in_force=<OrderTimeInForce.DAY: 'Day'>, order_type=<OrderType.LIMIT: 'Limit'>, size='5', underlying_symbol='USO', underlying_instrument_type=<InstrumentType.EQUITY: 'Equity'>, status=<OrderStatus.RECEIVED: 'Received'>, cancellable=True, editable=True, edited=False, updated_at=datetime.datetime(1970, 1, 1, 0, 0, tzinfo=datetime.timezone.utc), legs=[Leg(instrument_type=<InstrumentType.EQUITY: 'Equity'>, symbol='USO', action=<OrderAction.BUY_TO_OPEN: 'Buy to Open'>, quantity=Decimal('5'), remaining_quantity=Decimal('5'), fills=[])], id=None, price=Decimal('50.0'), price_effect=<PriceEffect.DEBIT: 'Debit'>, gtc_date=None, value=None, value_effect=None, stop_trigger=None, contingent_status=None, confirmation_status=None, cancelled_at=None, cancel_user_id=None, cancel_username=None, replacing_order_id=None, replaces_order_id=None, in_flight_at=None, live_at=None, received_at=None, reject_reason=None, user_id=None, username=None, terminal_at=None, complex_order_id=None, complex_order_tag=None, preflight_id=None, order_rule=None), complex_order=None, warnings=[Message(code='tif_next_valid_sesssion', message='Your order will begin working during next valid session.', preflight_id=None)], errors=None)
```

Example 3 (unknown):
```unknown
previous_order.price = Decimal('-10.05')  # let's pay more to get a fill!
response = account.replace_order(session, previous_response.order.id, previous_order)
```

Example 4 (unknown):
```unknown
account.delete_order(session, placed_order.id)
```

---

## Watchlists - tastytrade 11.1.0 documentation

**URL:** https://tastyworks-api.readthedocs.io/en/latest/watchlists.html

**Contents:**
- Watchlists¶

To use watchlists you’ll need a production session:

Let’s fetch an existing watchlist:

To add a symbol to the watchlist:

In this case, the symbol is present locally, but not remotely, so we need to update the remote list:

We can also create a new watchlist from scratch, then publish it to the Tastytrade server:

You can also fetch public watchlists:

**Examples:**

Example 1 (python):
```python
from tastytrade import Session
session = Session(user, password)
```

Example 2 (python):
```python
from tastytrade import PrivateWatchlist
watchlist = PrivateWatchlist.get(session, 'MyWatchlist')
print(watchlist.watchlist_entries)
```

Example 3 (unknown):
```unknown
>>> [{'symbol': 'AAPL', 'instrument-type': 'Equity'}, {'symbol': 'MSFT', 'instrument-type': 'Equity'}]
```

Example 4 (sql):
```sql
from tastytrade.instruments import InstrumentType
watchlist.add_symbol('SPY', InstrumentType.EQUITY)
```

---

## tastytrade.order - tastytrade 11.1.0 documentation

**URL:** https://tastyworks-api.readthedocs.io/en/latest/api/order.html

**Contents:**
- tastytrade.order¶

Bases: TastytradeData

Dataclass containing advanced order rules.

Show JSON schema{ "title": "AdvancedInstructions", "description": "Dataclass containing advanced order rules.", "type": "object", "properties": { "strict-position-effect-validation": { "default": false, "title": "Strict-Position-Effect-Validation", "type": "boolean" } } }

strict_position_effect_validation (bool)

By default, if a position meant to be closed by a closing order is no longer open, the API will turn it into an opening order. With this flag, the API would instead discard the closing order.

Bases: TastytradeData

Dataclass containing information about the effect of a trade on buying power.

Show JSON schema{ "title": "BuyingPowerEffect", "description": "Dataclass containing information about the effect of a trade on buying\npower.", "type": "object", "properties": { "change-in-margin-requirement": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Change-In-Margin-Requirement" }, "change-in-buying-power": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Change-In-Buying-Power" }, "current-buying-power": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Current-Buying-Power" }, "new-buying-power": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "New-Buying-Power" }, "isolated-order-margin-requirement": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Isolated-Order-Margin-Requirement" }, "is-spread": { "title": "Is-Spread", "type": "boolean" }, "impact": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Impact" }, "effect": { "$ref": "#/$defs/PriceEffect" } }, "$defs": { "PriceEffect": { "description": "This is an :class:`~enum.Enum` that shows the sign of a price effect, since\nTastytrade is apparently against negative numbers.", "enum": [ "Credit", "Debit", "None" ], "title": "PriceEffect", "type": "string" } }, "required": [ "change-in-margin-requirement", "change-in-buying-power", "current-buying-power", "new-buying-power", "isolated-order-margin-requirement", "is-spread", "impact", "effect" ] }

change_in_buying_power (decimal.Decimal)

change_in_margin_requirement (decimal.Decimal)

current_buying_power (decimal.Decimal)

effect (tastytrade.utils.PriceEffect)

impact (decimal.Decimal)

isolated_order_margin_requirement (decimal.Decimal)

new_buying_power (decimal.Decimal)

validate_price_effects » all fields

This is an Enum that contains the valid complex order types.

Valid values are as follows:

Bases: TastytradeData

Dataclass containing information about the fees associated with a trade.

Show JSON schema{ "title": "FeeCalculation", "description": "Dataclass containing information about the fees associated with a trade.", "type": "object", "properties": { "regulatory-fees": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Regulatory-Fees" }, "clearing-fees": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Clearing-Fees" }, "commission": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Commission" }, "proprietary-index-option-fees": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Proprietary-Index-Option-Fees" }, "total-fees": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Total-Fees" } }, "required": [ "regulatory-fees", "clearing-fees", "commission", "proprietary-index-option-fees", "total-fees" ] }

clearing_fees (decimal.Decimal)

commission (decimal.Decimal)

proprietary_index_option_fees (decimal.Decimal)

regulatory_fees (decimal.Decimal)

total_fees (decimal.Decimal)

validate_price_effects » all fields

Bases: TastytradeData

Dataclass that contains information about an order fill.

Show JSON schema{ "title": "FillInfo", "description": "Dataclass that contains information about an order fill.", "type": "object", "properties": { "fill-id": { "title": "Fill-Id", "type": "string" }, "quantity": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Quantity" }, "fill-price": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Fill-Price" }, "filled-at": { "format": "date-time", "title": "Filled-At", "type": "string" }, "destination-venue": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Destination-Venue" }, "ext-group-fill-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Ext-Group-Fill-Id" }, "ext-exec-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Ext-Exec-Id" } }, "required": [ "fill-id", "quantity", "fill-price", "filled-at" ] }

destination_venue (str | None)

ext_exec_id (str | None)

ext_group_fill_id (str | None)

fill_price (decimal.Decimal)

filled_at (datetime.datetime)

quantity (decimal.Decimal)

This is an Enum that contains the valid types of instruments and their representation in the API.

Valid values are as follows:

Bases: TastytradeData

Dataclass that represents an order leg.

Classes that inherit from TradeableTastytradeData can call build_leg() to build a leg from the dataclass.

Show JSON schema{ "title": "Leg", "description": "Dataclass that represents an order leg.\n\nClasses that inherit from :class:`TradeableTastytradeData` can\ncall :meth:`build_leg` to build a leg from the dataclass.", "type": "object", "properties": { "instrument-type": { "$ref": "#/$defs/InstrumentType" }, "symbol": { "title": "Symbol", "type": "string" }, "action": { "$ref": "#/$defs/OrderAction" }, "quantity": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Quantity" }, "remaining-quantity": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Remaining-Quantity" }, "fills": { "anyOf": [ { "items": { "$ref": "#/$defs/FillInfo" }, "type": "array" }, { "type": "null" } ], "default": null, "title": "Fills" } }, "$defs": { "FillInfo": { "description": "Dataclass that contains information about an order fill.", "properties": { "fill-id": { "title": "Fill-Id", "type": "string" }, "quantity": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Quantity" }, "fill-price": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Fill-Price" }, "filled-at": { "format": "date-time", "title": "Filled-At", "type": "string" }, "destination-venue": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Destination-Venue" }, "ext-group-fill-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Ext-Group-Fill-Id" }, "ext-exec-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Ext-Exec-Id" } }, "required": [ "fill-id", "quantity", "fill-price", "filled-at" ], "title": "FillInfo", "type": "object" }, "InstrumentType": { "description": "This is an :class:`~enum.Enum` that contains the valid types of instruments\nand their representation in the API.", "enum": [ "Bond", "Cryptocurrency", "Currency Pair", "Equity", "Equity Offering", "Equity Option", "Fixed Income Security", "Future", "Future Option", "Index", "Liquidity Pool", "Unknown", "Warrant" ], "title": "InstrumentType", "type": "string" }, "OrderAction": { "description": "This is an :class:`~enum.Enum` that contains the valid order actions.", "enum": [ "Buy to Open", "Buy to Close", "Sell to Open", "Sell to Close", "Buy", "Sell" ], "title": "OrderAction", "type": "string" } }, "required": [ "instrument-type", "symbol", "action" ] }

action (tastytrade.order.OrderAction)

fills (list[tastytrade.order.FillInfo] | None)

instrument_type (tastytrade.order.InstrumentType)

quantity (decimal.Decimal | int | None)

remaining_quantity (decimal.Decimal | None)

Bases: TastytradeData

Dataclass that represents a message from the Tastytrade API, usually a warning or an error.

Show JSON schema{ "title": "Message", "description": "Dataclass that represents a message from the Tastytrade API, usually\na warning or an error.", "type": "object", "properties": { "code": { "title": "Code", "type": "string" }, "message": { "title": "Message", "type": "string" }, "preflight-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Preflight-Id" } }, "required": [ "code", "message" ] }

preflight_id (str | None)

Bases: TastytradeData

Dataclass containing information about a new OTOCO order. Also used for modifying existing orders.

Show JSON schema{ "title": "NewComplexOrder", "description": "Dataclass containing information about a new OTOCO order.\nAlso used for modifying existing orders.", "type": "object", "properties": { "orders": { "items": { "$ref": "#/$defs/NewOrder" }, "title": "Orders", "type": "array" }, "source": { "default": "tastyware/tastytrade:v11.1.0", "title": "Source", "type": "string" }, "trigger-order": { "anyOf": [ { "$ref": "#/$defs/NewOrder" }, { "type": "null" } ], "default": null }, "type": { "$ref": "#/$defs/ComplexOrderType", "default": "OCO" } }, "$defs": { "AdvancedInstructions": { "description": "Dataclass containing advanced order rules.", "properties": { "strict-position-effect-validation": { "default": false, "title": "Strict-Position-Effect-Validation", "type": "boolean" } }, "title": "AdvancedInstructions", "type": "object" }, "ComplexOrderType": { "description": "This is an :class:`~enum.Enum` that contains the valid complex order types.", "enum": [ "OCO", "OTOCO" ], "title": "ComplexOrderType", "type": "string" }, "FillInfo": { "description": "Dataclass that contains information about an order fill.", "properties": { "fill-id": { "title": "Fill-Id", "type": "string" }, "quantity": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Quantity" }, "fill-price": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Fill-Price" }, "filled-at": { "format": "date-time", "title": "Filled-At", "type": "string" }, "destination-venue": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Destination-Venue" }, "ext-group-fill-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Ext-Group-Fill-Id" }, "ext-exec-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Ext-Exec-Id" } }, "required": [ "fill-id", "quantity", "fill-price", "filled-at" ], "title": "FillInfo", "type": "object" }, "InstrumentType": { "description": "This is an :class:`~enum.Enum` that contains the valid types of instruments\nand their representation in the API.", "enum": [ "Bond", "Cryptocurrency", "Currency Pair", "Equity", "Equity Offering", "Equity Option", "Fixed Income Security", "Future", "Future Option", "Index", "Liquidity Pool", "Unknown", "Warrant" ], "title": "InstrumentType", "type": "string" }, "Leg": { "description": "Dataclass that represents an order leg.\n\nClasses that inherit from :class:`TradeableTastytradeData` can\ncall :meth:`build_leg` to build a leg from the dataclass.", "properties": { "instrument-type": { "$ref": "#/$defs/InstrumentType" }, "symbol": { "title": "Symbol", "type": "string" }, "action": { "$ref": "#/$defs/OrderAction" }, "quantity": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Quantity" }, "remaining-quantity": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Remaining-Quantity" }, "fills": { "anyOf": [ { "items": { "$ref": "#/$defs/FillInfo" }, "type": "array" }, { "type": "null" } ], "default": null, "title": "Fills" } }, "required": [ "instrument-type", "symbol", "action" ], "title": "Leg", "type": "object" }, "NewOrder": { "additionalProperties": true, "description": "Dataclass containing information about a new order. Also used for\nmodifying existing orders.", "properties": { "time-in-force": { "$ref": "#/$defs/OrderTimeInForce" }, "order-type": { "$ref": "#/$defs/OrderType" }, "source": { "default": "tastyware/tastytrade:v11.1.0", "title": "Source", "type": "string" }, "legs": { "items": { "$ref": "#/$defs/Leg" }, "title": "Legs", "type": "array" }, "gtc-date": { "anyOf": [ { "format": "date", "type": "string" }, { "type": "null" } ], "default": null, "title": "Gtc-Date" }, "stop-trigger": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Stop-Trigger" }, "price": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Price" }, "value": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Value" }, "partition-key": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Partition-Key" }, "preflight-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Preflight-Id" }, "rules": { "anyOf": [ { "$ref": "#/$defs/OrderRule" }, { "type": "null" } ], "default": null }, "advanced-instructions": { "anyOf": [ { "$ref": "#/$defs/AdvancedInstructions" }, { "type": "null" } ], "default": null }, "external-identifier": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "External-Identifier" } }, "required": [ "time-in-force", "order-type", "legs" ], "title": "NewOrder", "type": "object" }, "OrderAction": { "description": "This is an :class:`~enum.Enum` that contains the valid order actions.", "enum": [ "Buy to Open", "Buy to Close", "Sell to Open", "Sell to Close", "Buy", "Sell" ], "title": "OrderAction", "type": "string" }, "OrderCondition": { "description": "Dataclass that represents an order condition for an order rule.", "properties": { "id": { "title": "Id", "type": "string" }, "action": { "title": "Action", "type": "string" }, "symbol": { "title": "Symbol", "type": "string" }, "instrument-type": { "$ref": "#/$defs/InstrumentType" }, "indicator": { "title": "Indicator", "type": "string" }, "comparator": { "title": "Comparator", "type": "string" }, "threshold": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Threshold" }, "is-threshold-based-on-notional": { "title": "Is-Threshold-Based-On-Notional", "type": "boolean" }, "triggered-at": { "format": "date-time", "title": "Triggered-At", "type": "string" }, "triggered-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Triggered-Value" }, "price-components": { "items": { "$ref": "#/$defs/OrderConditionPriceComponent" }, "title": "Price-Components", "type": "array" } }, "required": [ "id", "action", "symbol", "instrument-type", "indicator", "comparator", "threshold", "is-threshold-based-on-notional", "triggered-at", "triggered-value", "price-components" ], "title": "OrderCondition", "type": "object" }, "OrderConditionPriceComponent": { "description": "Dataclass that represents a price component of an order condition.", "properties": { "symbol": { "title": "Symbol", "type": "string" }, "instrument-type": { "$ref": "#/$defs/InstrumentType" }, "quantity": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Quantity" }, "quantity-direction": { "title": "Quantity-Direction", "type": "string" } }, "required": [ "symbol", "instrument-type", "quantity", "quantity-direction" ], "title": "OrderConditionPriceComponent", "type": "object" }, "OrderRule": { "description": "Dataclass that represents an order rule for a complex order.", "properties": { "route-after": { "format": "date-time", "title": "Route-After", "type": "string" }, "routed-at": { "format": "date-time", "title": "Routed-At", "type": "string" }, "cancel-at": { "format": "date-time", "title": "Cancel-At", "type": "string" }, "cancelled-at": { "format": "date-time", "title": "Cancelled-At", "type": "string" }, "order-conditions": { "items": { "$ref": "#/$defs/OrderCondition" }, "title": "Order-Conditions", "type": "array" } }, "required": [ "route-after", "routed-at", "cancel-at", "cancelled-at", "order-conditions" ], "title": "OrderRule", "type": "object" }, "OrderTimeInForce": { "description": "This is an :class:`~enum.Enum` that contains the valid TIFs for orders.", "enum": [ "Day", "GTC", "GTD", "Ext", "GTC Ext", "IOC" ], "title": "OrderTimeInForce", "type": "string" }, "OrderType": { "description": "This is an :class:`~enum.Enum` that contains the valid types of orders.", "enum": [ "Limit", "Market", "Marketable Limit", "Stop", "Stop Limit", "Notional Market" ], "title": "OrderType", "type": "string" } }, "required": [ "orders" ] }

orders (list[tastytrade.order.NewOrder])

trigger_order (tastytrade.order.NewOrder | None)

type (tastytrade.order.ComplexOrderType)

Bases: TastytradeData

Dataclass containing information about a new order. Also used for modifying existing orders.

Show JSON schema{ "title": "NewOrder", "description": "Dataclass containing information about a new order. Also used for\nmodifying existing orders.", "type": "object", "properties": { "time-in-force": { "$ref": "#/$defs/OrderTimeInForce" }, "order-type": { "$ref": "#/$defs/OrderType" }, "source": { "default": "tastyware/tastytrade:v11.1.0", "title": "Source", "type": "string" }, "legs": { "items": { "$ref": "#/$defs/Leg" }, "title": "Legs", "type": "array" }, "gtc-date": { "anyOf": [ { "format": "date", "type": "string" }, { "type": "null" } ], "default": null, "title": "Gtc-Date" }, "stop-trigger": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Stop-Trigger" }, "price": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Price" }, "value": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Value" }, "partition-key": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Partition-Key" }, "preflight-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Preflight-Id" }, "rules": { "anyOf": [ { "$ref": "#/$defs/OrderRule" }, { "type": "null" } ], "default": null }, "advanced-instructions": { "anyOf": [ { "$ref": "#/$defs/AdvancedInstructions" }, { "type": "null" } ], "default": null }, "external-identifier": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "External-Identifier" } }, "$defs": { "AdvancedInstructions": { "description": "Dataclass containing advanced order rules.", "properties": { "strict-position-effect-validation": { "default": false, "title": "Strict-Position-Effect-Validation", "type": "boolean" } }, "title": "AdvancedInstructions", "type": "object" }, "FillInfo": { "description": "Dataclass that contains information about an order fill.", "properties": { "fill-id": { "title": "Fill-Id", "type": "string" }, "quantity": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Quantity" }, "fill-price": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Fill-Price" }, "filled-at": { "format": "date-time", "title": "Filled-At", "type": "string" }, "destination-venue": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Destination-Venue" }, "ext-group-fill-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Ext-Group-Fill-Id" }, "ext-exec-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Ext-Exec-Id" } }, "required": [ "fill-id", "quantity", "fill-price", "filled-at" ], "title": "FillInfo", "type": "object" }, "InstrumentType": { "description": "This is an :class:`~enum.Enum` that contains the valid types of instruments\nand their representation in the API.", "enum": [ "Bond", "Cryptocurrency", "Currency Pair", "Equity", "Equity Offering", "Equity Option", "Fixed Income Security", "Future", "Future Option", "Index", "Liquidity Pool", "Unknown", "Warrant" ], "title": "InstrumentType", "type": "string" }, "Leg": { "description": "Dataclass that represents an order leg.\n\nClasses that inherit from :class:`TradeableTastytradeData` can\ncall :meth:`build_leg` to build a leg from the dataclass.", "properties": { "instrument-type": { "$ref": "#/$defs/InstrumentType" }, "symbol": { "title": "Symbol", "type": "string" }, "action": { "$ref": "#/$defs/OrderAction" }, "quantity": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Quantity" }, "remaining-quantity": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Remaining-Quantity" }, "fills": { "anyOf": [ { "items": { "$ref": "#/$defs/FillInfo" }, "type": "array" }, { "type": "null" } ], "default": null, "title": "Fills" } }, "required": [ "instrument-type", "symbol", "action" ], "title": "Leg", "type": "object" }, "OrderAction": { "description": "This is an :class:`~enum.Enum` that contains the valid order actions.", "enum": [ "Buy to Open", "Buy to Close", "Sell to Open", "Sell to Close", "Buy", "Sell" ], "title": "OrderAction", "type": "string" }, "OrderCondition": { "description": "Dataclass that represents an order condition for an order rule.", "properties": { "id": { "title": "Id", "type": "string" }, "action": { "title": "Action", "type": "string" }, "symbol": { "title": "Symbol", "type": "string" }, "instrument-type": { "$ref": "#/$defs/InstrumentType" }, "indicator": { "title": "Indicator", "type": "string" }, "comparator": { "title": "Comparator", "type": "string" }, "threshold": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Threshold" }, "is-threshold-based-on-notional": { "title": "Is-Threshold-Based-On-Notional", "type": "boolean" }, "triggered-at": { "format": "date-time", "title": "Triggered-At", "type": "string" }, "triggered-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Triggered-Value" }, "price-components": { "items": { "$ref": "#/$defs/OrderConditionPriceComponent" }, "title": "Price-Components", "type": "array" } }, "required": [ "id", "action", "symbol", "instrument-type", "indicator", "comparator", "threshold", "is-threshold-based-on-notional", "triggered-at", "triggered-value", "price-components" ], "title": "OrderCondition", "type": "object" }, "OrderConditionPriceComponent": { "description": "Dataclass that represents a price component of an order condition.", "properties": { "symbol": { "title": "Symbol", "type": "string" }, "instrument-type": { "$ref": "#/$defs/InstrumentType" }, "quantity": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Quantity" }, "quantity-direction": { "title": "Quantity-Direction", "type": "string" } }, "required": [ "symbol", "instrument-type", "quantity", "quantity-direction" ], "title": "OrderConditionPriceComponent", "type": "object" }, "OrderRule": { "description": "Dataclass that represents an order rule for a complex order.", "properties": { "route-after": { "format": "date-time", "title": "Route-After", "type": "string" }, "routed-at": { "format": "date-time", "title": "Routed-At", "type": "string" }, "cancel-at": { "format": "date-time", "title": "Cancel-At", "type": "string" }, "cancelled-at": { "format": "date-time", "title": "Cancelled-At", "type": "string" }, "order-conditions": { "items": { "$ref": "#/$defs/OrderCondition" }, "title": "Order-Conditions", "type": "array" } }, "required": [ "route-after", "routed-at", "cancel-at", "cancelled-at", "order-conditions" ], "title": "OrderRule", "type": "object" }, "OrderTimeInForce": { "description": "This is an :class:`~enum.Enum` that contains the valid TIFs for orders.", "enum": [ "Day", "GTC", "GTD", "Ext", "GTC Ext", "IOC" ], "title": "OrderTimeInForce", "type": "string" }, "OrderType": { "description": "This is an :class:`~enum.Enum` that contains the valid types of orders.", "enum": [ "Limit", "Market", "Marketable Limit", "Stop", "Stop Limit", "Notional Market" ], "title": "OrderType", "type": "string" } }, "additionalProperties": true, "required": [ "time-in-force", "order-type", "legs" ] }

advanced_instructions (tastytrade.order.AdvancedInstructions | None)

external_identifier (str | None)

gtc_date (datetime.date | None)

legs (list[tastytrade.order.Leg])

order_type (tastytrade.order.OrderType)

partition_key (str | None)

preflight_id (str | None)

price (decimal.Decimal | None)

rules (tastytrade.order.OrderRule | None)

stop_trigger (decimal.Decimal | None)

time_in_force (tastytrade.order.OrderTimeInForce)

value (decimal.Decimal | None)

External identifier for the order, used to track orders across systems

The price of the order; negative = debit, positive = credit

For a stop/stop limit order. If the latter, use price for the limit price

The actual notional value of the order. Only for notional market orders!

This is an Enum that contains the valid order actions.

Valid values are as follows:

Bases: TastytradeData

Dataclass that represents an order condition for an order rule.

Show JSON schema{ "title": "OrderCondition", "description": "Dataclass that represents an order condition for an order rule.", "type": "object", "properties": { "id": { "title": "Id", "type": "string" }, "action": { "title": "Action", "type": "string" }, "symbol": { "title": "Symbol", "type": "string" }, "instrument-type": { "$ref": "#/$defs/InstrumentType" }, "indicator": { "title": "Indicator", "type": "string" }, "comparator": { "title": "Comparator", "type": "string" }, "threshold": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Threshold" }, "is-threshold-based-on-notional": { "title": "Is-Threshold-Based-On-Notional", "type": "boolean" }, "triggered-at": { "format": "date-time", "title": "Triggered-At", "type": "string" }, "triggered-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Triggered-Value" }, "price-components": { "items": { "$ref": "#/$defs/OrderConditionPriceComponent" }, "title": "Price-Components", "type": "array" } }, "$defs": { "InstrumentType": { "description": "This is an :class:`~enum.Enum` that contains the valid types of instruments\nand their representation in the API.", "enum": [ "Bond", "Cryptocurrency", "Currency Pair", "Equity", "Equity Offering", "Equity Option", "Fixed Income Security", "Future", "Future Option", "Index", "Liquidity Pool", "Unknown", "Warrant" ], "title": "InstrumentType", "type": "string" }, "OrderConditionPriceComponent": { "description": "Dataclass that represents a price component of an order condition.", "properties": { "symbol": { "title": "Symbol", "type": "string" }, "instrument-type": { "$ref": "#/$defs/InstrumentType" }, "quantity": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Quantity" }, "quantity-direction": { "title": "Quantity-Direction", "type": "string" } }, "required": [ "symbol", "instrument-type", "quantity", "quantity-direction" ], "title": "OrderConditionPriceComponent", "type": "object" } }, "required": [ "id", "action", "symbol", "instrument-type", "indicator", "comparator", "threshold", "is-threshold-based-on-notional", "triggered-at", "triggered-value", "price-components" ] }

instrument_type (tastytrade.order.InstrumentType)

is_threshold_based_on_notional (bool)

price_components (list[tastytrade.order.OrderConditionPriceComponent])

threshold (decimal.Decimal)

triggered_at (datetime.datetime)

triggered_value (decimal.Decimal)

Bases: TastytradeData

Dataclass that represents a price component of an order condition.

Show JSON schema{ "title": "OrderConditionPriceComponent", "description": "Dataclass that represents a price component of an order condition.", "type": "object", "properties": { "symbol": { "title": "Symbol", "type": "string" }, "instrument-type": { "$ref": "#/$defs/InstrumentType" }, "quantity": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Quantity" }, "quantity-direction": { "title": "Quantity-Direction", "type": "string" } }, "$defs": { "InstrumentType": { "description": "This is an :class:`~enum.Enum` that contains the valid types of instruments\nand their representation in the API.", "enum": [ "Bond", "Cryptocurrency", "Currency Pair", "Equity", "Equity Offering", "Equity Option", "Fixed Income Security", "Future", "Future Option", "Index", "Liquidity Pool", "Unknown", "Warrant" ], "title": "InstrumentType", "type": "string" } }, "required": [ "symbol", "instrument-type", "quantity", "quantity-direction" ] }

instrument_type (tastytrade.order.InstrumentType)

quantity (decimal.Decimal)

quantity_direction (str)

Bases: TastytradeData

Dataclass that represents an order rule for a complex order.

Show JSON schema{ "title": "OrderRule", "description": "Dataclass that represents an order rule for a complex order.", "type": "object", "properties": { "route-after": { "format": "date-time", "title": "Route-After", "type": "string" }, "routed-at": { "format": "date-time", "title": "Routed-At", "type": "string" }, "cancel-at": { "format": "date-time", "title": "Cancel-At", "type": "string" }, "cancelled-at": { "format": "date-time", "title": "Cancelled-At", "type": "string" }, "order-conditions": { "items": { "$ref": "#/$defs/OrderCondition" }, "title": "Order-Conditions", "type": "array" } }, "$defs": { "InstrumentType": { "description": "This is an :class:`~enum.Enum` that contains the valid types of instruments\nand their representation in the API.", "enum": [ "Bond", "Cryptocurrency", "Currency Pair", "Equity", "Equity Offering", "Equity Option", "Fixed Income Security", "Future", "Future Option", "Index", "Liquidity Pool", "Unknown", "Warrant" ], "title": "InstrumentType", "type": "string" }, "OrderCondition": { "description": "Dataclass that represents an order condition for an order rule.", "properties": { "id": { "title": "Id", "type": "string" }, "action": { "title": "Action", "type": "string" }, "symbol": { "title": "Symbol", "type": "string" }, "instrument-type": { "$ref": "#/$defs/InstrumentType" }, "indicator": { "title": "Indicator", "type": "string" }, "comparator": { "title": "Comparator", "type": "string" }, "threshold": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Threshold" }, "is-threshold-based-on-notional": { "title": "Is-Threshold-Based-On-Notional", "type": "boolean" }, "triggered-at": { "format": "date-time", "title": "Triggered-At", "type": "string" }, "triggered-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Triggered-Value" }, "price-components": { "items": { "$ref": "#/$defs/OrderConditionPriceComponent" }, "title": "Price-Components", "type": "array" } }, "required": [ "id", "action", "symbol", "instrument-type", "indicator", "comparator", "threshold", "is-threshold-based-on-notional", "triggered-at", "triggered-value", "price-components" ], "title": "OrderCondition", "type": "object" }, "OrderConditionPriceComponent": { "description": "Dataclass that represents a price component of an order condition.", "properties": { "symbol": { "title": "Symbol", "type": "string" }, "instrument-type": { "$ref": "#/$defs/InstrumentType" }, "quantity": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Quantity" }, "quantity-direction": { "title": "Quantity-Direction", "type": "string" } }, "required": [ "symbol", "instrument-type", "quantity", "quantity-direction" ], "title": "OrderConditionPriceComponent", "type": "object" } }, "required": [ "route-after", "routed-at", "cancel-at", "cancelled-at", "order-conditions" ] }

cancel_at (datetime.datetime)

cancelled_at (datetime.datetime)

order_conditions (list[tastytrade.order.OrderCondition])

route_after (datetime.datetime)

routed_at (datetime.datetime)

This is an Enum that contains different order statuses. A typical (successful) order follows a progression:

RECEIVED -> LIVE -> FILLED

Valid values are as follows:

This is an Enum that contains the valid TIFs for orders.

Valid values are as follows:

This is an Enum that contains the valid types of orders.

Valid values are as follows:

Bases: TastytradeData

Dataclass containing information about an already placed complex order.

Show JSON schema{ "title": "PlacedComplexOrder", "description": "Dataclass containing information about an already placed complex order.", "type": "object", "properties": { "account-number": { "title": "Account-Number", "type": "string" }, "type": { "title": "Type", "type": "string" }, "orders": { "items": { "$ref": "#/$defs/PlacedOrder" }, "title": "Orders", "type": "array" }, "id": { "default": -1, "title": "Id", "type": "integer" }, "trigger-order": { "anyOf": [ { "$ref": "#/$defs/PlacedOrder" }, { "type": "null" } ], "default": null }, "terminal-at": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Terminal-At" }, "ratio-price-threshold": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Ratio-Price-Threshold" }, "ratio-price-comparator": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Ratio-Price-Comparator" }, "ratio-price-is-threshold-based-on-notional": { "anyOf": [ { "type": "boolean" }, { "type": "null" } ], "default": null, "title": "Ratio-Price-Is-Threshold-Based-On-Notional" }, "related-orders": { "anyOf": [ { "items": { "additionalProperties": { "type": "string" }, "type": "object" }, "type": "array" }, { "type": "null" } ], "default": null, "title": "Related-Orders" } }, "$defs": { "FillInfo": { "description": "Dataclass that contains information about an order fill.", "properties": { "fill-id": { "title": "Fill-Id", "type": "string" }, "quantity": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Quantity" }, "fill-price": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Fill-Price" }, "filled-at": { "format": "date-time", "title": "Filled-At", "type": "string" }, "destination-venue": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Destination-Venue" }, "ext-group-fill-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Ext-Group-Fill-Id" }, "ext-exec-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Ext-Exec-Id" } }, "required": [ "fill-id", "quantity", "fill-price", "filled-at" ], "title": "FillInfo", "type": "object" }, "InstrumentType": { "description": "This is an :class:`~enum.Enum` that contains the valid types of instruments\nand their representation in the API.", "enum": [ "Bond", "Cryptocurrency", "Currency Pair", "Equity", "Equity Offering", "Equity Option", "Fixed Income Security", "Future", "Future Option", "Index", "Liquidity Pool", "Unknown", "Warrant" ], "title": "InstrumentType", "type": "string" }, "Leg": { "description": "Dataclass that represents an order leg.\n\nClasses that inherit from :class:`TradeableTastytradeData` can\ncall :meth:`build_leg` to build a leg from the dataclass.", "properties": { "instrument-type": { "$ref": "#/$defs/InstrumentType" }, "symbol": { "title": "Symbol", "type": "string" }, "action": { "$ref": "#/$defs/OrderAction" }, "quantity": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Quantity" }, "remaining-quantity": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Remaining-Quantity" }, "fills": { "anyOf": [ { "items": { "$ref": "#/$defs/FillInfo" }, "type": "array" }, { "type": "null" } ], "default": null, "title": "Fills" } }, "required": [ "instrument-type", "symbol", "action" ], "title": "Leg", "type": "object" }, "OrderAction": { "description": "This is an :class:`~enum.Enum` that contains the valid order actions.", "enum": [ "Buy to Open", "Buy to Close", "Sell to Open", "Sell to Close", "Buy", "Sell" ], "title": "OrderAction", "type": "string" }, "OrderCondition": { "description": "Dataclass that represents an order condition for an order rule.", "properties": { "id": { "title": "Id", "type": "string" }, "action": { "title": "Action", "type": "string" }, "symbol": { "title": "Symbol", "type": "string" }, "instrument-type": { "$ref": "#/$defs/InstrumentType" }, "indicator": { "title": "Indicator", "type": "string" }, "comparator": { "title": "Comparator", "type": "string" }, "threshold": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Threshold" }, "is-threshold-based-on-notional": { "title": "Is-Threshold-Based-On-Notional", "type": "boolean" }, "triggered-at": { "format": "date-time", "title": "Triggered-At", "type": "string" }, "triggered-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Triggered-Value" }, "price-components": { "items": { "$ref": "#/$defs/OrderConditionPriceComponent" }, "title": "Price-Components", "type": "array" } }, "required": [ "id", "action", "symbol", "instrument-type", "indicator", "comparator", "threshold", "is-threshold-based-on-notional", "triggered-at", "triggered-value", "price-components" ], "title": "OrderCondition", "type": "object" }, "OrderConditionPriceComponent": { "description": "Dataclass that represents a price component of an order condition.", "properties": { "symbol": { "title": "Symbol", "type": "string" }, "instrument-type": { "$ref": "#/$defs/InstrumentType" }, "quantity": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Quantity" }, "quantity-direction": { "title": "Quantity-Direction", "type": "string" } }, "required": [ "symbol", "instrument-type", "quantity", "quantity-direction" ], "title": "OrderConditionPriceComponent", "type": "object" }, "OrderRule": { "description": "Dataclass that represents an order rule for a complex order.", "properties": { "route-after": { "format": "date-time", "title": "Route-After", "type": "string" }, "routed-at": { "format": "date-time", "title": "Routed-At", "type": "string" }, "cancel-at": { "format": "date-time", "title": "Cancel-At", "type": "string" }, "cancelled-at": { "format": "date-time", "title": "Cancelled-At", "type": "string" }, "order-conditions": { "items": { "$ref": "#/$defs/OrderCondition" }, "title": "Order-Conditions", "type": "array" } }, "required": [ "route-after", "routed-at", "cancel-at", "cancelled-at", "order-conditions" ], "title": "OrderRule", "type": "object" }, "OrderStatus": { "description": "This is an :class:`~enum.Enum` that contains different order statuses.\nA typical (successful) order follows a progression:\n\nRECEIVED -> LIVE -> FILLED", "enum": [ "Received", "Cancelled", "Filled", "Expired", "Live", "Rejected", "Contingent", "Routed", "In Flight", "Cancel Requested", "Replace Requested", "Removed", "Partially Removed" ], "title": "OrderStatus", "type": "string" }, "OrderTimeInForce": { "description": "This is an :class:`~enum.Enum` that contains the valid TIFs for orders.", "enum": [ "Day", "GTC", "GTD", "Ext", "GTC Ext", "IOC" ], "title": "OrderTimeInForce", "type": "string" }, "OrderType": { "description": "This is an :class:`~enum.Enum` that contains the valid types of orders.", "enum": [ "Limit", "Market", "Marketable Limit", "Stop", "Stop Limit", "Notional Market" ], "title": "OrderType", "type": "string" }, "PlacedOrder": { "description": "Dataclass containing information about an existing order, whether it's\nbeen filled or not.", "properties": { "account-number": { "title": "Account-Number", "type": "string" }, "time-in-force": { "$ref": "#/$defs/OrderTimeInForce" }, "order-type": { "$ref": "#/$defs/OrderType" }, "underlying-symbol": { "title": "Underlying-Symbol", "type": "string" }, "underlying-instrument-type": { "$ref": "#/$defs/InstrumentType" }, "status": { "$ref": "#/$defs/OrderStatus" }, "cancellable": { "title": "Cancellable", "type": "boolean" }, "editable": { "title": "Editable", "type": "boolean" }, "edited": { "title": "Edited", "type": "boolean" }, "updated-at": { "format": "date-time", "title": "Updated-At", "type": "string" }, "legs": { "items": { "$ref": "#/$defs/Leg" }, "title": "Legs", "type": "array" }, "id": { "default": -1, "title": "Id", "type": "integer" }, "size": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Size" }, "price": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Price" }, "gtc-date": { "anyOf": [ { "format": "date", "type": "string" }, { "type": "null" } ], "default": null, "title": "Gtc-Date" }, "value": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Value" }, "stop-trigger": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Stop-Trigger" }, "contingent-status": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Contingent-Status" }, "confirmation-status": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Confirmation-Status" }, "cancelled-at": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "Cancelled-At" }, "cancel-user-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Cancel-User-Id" }, "cancel-username": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Cancel-Username" }, "replacing-order-id": { "anyOf": [ { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Replacing-Order-Id" }, "replaces-order-id": { "anyOf": [ { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Replaces-Order-Id" }, "in-flight-at": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "In-Flight-At" }, "live-at": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "Live-At" }, "received-at": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "Received-At" }, "reject-reason": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Reject-Reason" }, "user-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "User-Id" }, "username": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Username" }, "terminal-at": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "Terminal-At" }, "complex-order-id": { "anyOf": [ { "type": "string" }, { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Complex-Order-Id" }, "complex-order-tag": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Complex-Order-Tag" }, "preflight-id": { "anyOf": [ { "type": "string" }, { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Preflight-Id" }, "order-rule": { "anyOf": [ { "$ref": "#/$defs/OrderRule" }, { "type": "null" } ], "default": null }, "source": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Source" }, "external-identifier": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "External-Identifier" } }, "required": [ "account-number", "time-in-force", "order-type", "underlying-symbol", "underlying-instrument-type", "status", "cancellable", "editable", "edited", "updated-at", "legs" ], "title": "PlacedOrder", "type": "object" } }, "required": [ "account-number", "type", "orders" ] }

orders (list[tastytrade.order.PlacedOrder])

ratio_price_comparator (str | None)

ratio_price_is_threshold_based_on_notional (bool | None)

ratio_price_threshold (decimal.Decimal | None)

related_orders (list[dict[str, str]] | None)

terminal_at (str | None)

trigger_order (tastytrade.order.PlacedOrder | None)

the ID of the order; test orders placed with dry_run don’t have an ID

Bases: TastytradeData

Dataclass grouping together information about a placed complex order.

Show JSON schema{ "title": "PlacedComplexOrderResponse", "description": "Dataclass grouping together information about a placed complex order.", "type": "object", "properties": { "buying-power-effect": { "$ref": "#/$defs/BuyingPowerEffect" }, "complex-order": { "$ref": "#/$defs/PlacedComplexOrder" }, "fee-calculation": { "anyOf": [ { "$ref": "#/$defs/FeeCalculation" }, { "type": "null" } ], "default": null }, "warnings": { "anyOf": [ { "items": { "$ref": "#/$defs/Message" }, "type": "array" }, { "type": "null" } ], "default": null, "title": "Warnings" }, "errors": { "anyOf": [ { "items": { "$ref": "#/$defs/Message" }, "type": "array" }, { "type": "null" } ], "default": null, "title": "Errors" } }, "$defs": { "BuyingPowerEffect": { "description": "Dataclass containing information about the effect of a trade on buying\npower.", "properties": { "change-in-margin-requirement": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Change-In-Margin-Requirement" }, "change-in-buying-power": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Change-In-Buying-Power" }, "current-buying-power": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Current-Buying-Power" }, "new-buying-power": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "New-Buying-Power" }, "isolated-order-margin-requirement": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Isolated-Order-Margin-Requirement" }, "is-spread": { "title": "Is-Spread", "type": "boolean" }, "impact": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Impact" }, "effect": { "$ref": "#/$defs/PriceEffect" } }, "required": [ "change-in-margin-requirement", "change-in-buying-power", "current-buying-power", "new-buying-power", "isolated-order-margin-requirement", "is-spread", "impact", "effect" ], "title": "BuyingPowerEffect", "type": "object" }, "FeeCalculation": { "description": "Dataclass containing information about the fees associated with a trade.", "properties": { "regulatory-fees": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Regulatory-Fees" }, "clearing-fees": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Clearing-Fees" }, "commission": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Commission" }, "proprietary-index-option-fees": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Proprietary-Index-Option-Fees" }, "total-fees": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Total-Fees" } }, "required": [ "regulatory-fees", "clearing-fees", "commission", "proprietary-index-option-fees", "total-fees" ], "title": "FeeCalculation", "type": "object" }, "FillInfo": { "description": "Dataclass that contains information about an order fill.", "properties": { "fill-id": { "title": "Fill-Id", "type": "string" }, "quantity": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Quantity" }, "fill-price": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Fill-Price" }, "filled-at": { "format": "date-time", "title": "Filled-At", "type": "string" }, "destination-venue": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Destination-Venue" }, "ext-group-fill-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Ext-Group-Fill-Id" }, "ext-exec-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Ext-Exec-Id" } }, "required": [ "fill-id", "quantity", "fill-price", "filled-at" ], "title": "FillInfo", "type": "object" }, "InstrumentType": { "description": "This is an :class:`~enum.Enum` that contains the valid types of instruments\nand their representation in the API.", "enum": [ "Bond", "Cryptocurrency", "Currency Pair", "Equity", "Equity Offering", "Equity Option", "Fixed Income Security", "Future", "Future Option", "Index", "Liquidity Pool", "Unknown", "Warrant" ], "title": "InstrumentType", "type": "string" }, "Leg": { "description": "Dataclass that represents an order leg.\n\nClasses that inherit from :class:`TradeableTastytradeData` can\ncall :meth:`build_leg` to build a leg from the dataclass.", "properties": { "instrument-type": { "$ref": "#/$defs/InstrumentType" }, "symbol": { "title": "Symbol", "type": "string" }, "action": { "$ref": "#/$defs/OrderAction" }, "quantity": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Quantity" }, "remaining-quantity": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Remaining-Quantity" }, "fills": { "anyOf": [ { "items": { "$ref": "#/$defs/FillInfo" }, "type": "array" }, { "type": "null" } ], "default": null, "title": "Fills" } }, "required": [ "instrument-type", "symbol", "action" ], "title": "Leg", "type": "object" }, "Message": { "description": "Dataclass that represents a message from the Tastytrade API, usually\na warning or an error.", "properties": { "code": { "title": "Code", "type": "string" }, "message": { "title": "Message", "type": "string" }, "preflight-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Preflight-Id" } }, "required": [ "code", "message" ], "title": "Message", "type": "object" }, "OrderAction": { "description": "This is an :class:`~enum.Enum` that contains the valid order actions.", "enum": [ "Buy to Open", "Buy to Close", "Sell to Open", "Sell to Close", "Buy", "Sell" ], "title": "OrderAction", "type": "string" }, "OrderCondition": { "description": "Dataclass that represents an order condition for an order rule.", "properties": { "id": { "title": "Id", "type": "string" }, "action": { "title": "Action", "type": "string" }, "symbol": { "title": "Symbol", "type": "string" }, "instrument-type": { "$ref": "#/$defs/InstrumentType" }, "indicator": { "title": "Indicator", "type": "string" }, "comparator": { "title": "Comparator", "type": "string" }, "threshold": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Threshold" }, "is-threshold-based-on-notional": { "title": "Is-Threshold-Based-On-Notional", "type": "boolean" }, "triggered-at": { "format": "date-time", "title": "Triggered-At", "type": "string" }, "triggered-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Triggered-Value" }, "price-components": { "items": { "$ref": "#/$defs/OrderConditionPriceComponent" }, "title": "Price-Components", "type": "array" } }, "required": [ "id", "action", "symbol", "instrument-type", "indicator", "comparator", "threshold", "is-threshold-based-on-notional", "triggered-at", "triggered-value", "price-components" ], "title": "OrderCondition", "type": "object" }, "OrderConditionPriceComponent": { "description": "Dataclass that represents a price component of an order condition.", "properties": { "symbol": { "title": "Symbol", "type": "string" }, "instrument-type": { "$ref": "#/$defs/InstrumentType" }, "quantity": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Quantity" }, "quantity-direction": { "title": "Quantity-Direction", "type": "string" } }, "required": [ "symbol", "instrument-type", "quantity", "quantity-direction" ], "title": "OrderConditionPriceComponent", "type": "object" }, "OrderRule": { "description": "Dataclass that represents an order rule for a complex order.", "properties": { "route-after": { "format": "date-time", "title": "Route-After", "type": "string" }, "routed-at": { "format": "date-time", "title": "Routed-At", "type": "string" }, "cancel-at": { "format": "date-time", "title": "Cancel-At", "type": "string" }, "cancelled-at": { "format": "date-time", "title": "Cancelled-At", "type": "string" }, "order-conditions": { "items": { "$ref": "#/$defs/OrderCondition" }, "title": "Order-Conditions", "type": "array" } }, "required": [ "route-after", "routed-at", "cancel-at", "cancelled-at", "order-conditions" ], "title": "OrderRule", "type": "object" }, "OrderStatus": { "description": "This is an :class:`~enum.Enum` that contains different order statuses.\nA typical (successful) order follows a progression:\n\nRECEIVED -> LIVE -> FILLED", "enum": [ "Received", "Cancelled", "Filled", "Expired", "Live", "Rejected", "Contingent", "Routed", "In Flight", "Cancel Requested", "Replace Requested", "Removed", "Partially Removed" ], "title": "OrderStatus", "type": "string" }, "OrderTimeInForce": { "description": "This is an :class:`~enum.Enum` that contains the valid TIFs for orders.", "enum": [ "Day", "GTC", "GTD", "Ext", "GTC Ext", "IOC" ], "title": "OrderTimeInForce", "type": "string" }, "OrderType": { "description": "This is an :class:`~enum.Enum` that contains the valid types of orders.", "enum": [ "Limit", "Market", "Marketable Limit", "Stop", "Stop Limit", "Notional Market" ], "title": "OrderType", "type": "string" }, "PlacedComplexOrder": { "description": "Dataclass containing information about an already placed complex order.", "properties": { "account-number": { "title": "Account-Number", "type": "string" }, "type": { "title": "Type", "type": "string" }, "orders": { "items": { "$ref": "#/$defs/PlacedOrder" }, "title": "Orders", "type": "array" }, "id": { "default": -1, "title": "Id", "type": "integer" }, "trigger-order": { "anyOf": [ { "$ref": "#/$defs/PlacedOrder" }, { "type": "null" } ], "default": null }, "terminal-at": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Terminal-At" }, "ratio-price-threshold": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Ratio-Price-Threshold" }, "ratio-price-comparator": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Ratio-Price-Comparator" }, "ratio-price-is-threshold-based-on-notional": { "anyOf": [ { "type": "boolean" }, { "type": "null" } ], "default": null, "title": "Ratio-Price-Is-Threshold-Based-On-Notional" }, "related-orders": { "anyOf": [ { "items": { "additionalProperties": { "type": "string" }, "type": "object" }, "type": "array" }, { "type": "null" } ], "default": null, "title": "Related-Orders" } }, "required": [ "account-number", "type", "orders" ], "title": "PlacedComplexOrder", "type": "object" }, "PlacedOrder": { "description": "Dataclass containing information about an existing order, whether it's\nbeen filled or not.", "properties": { "account-number": { "title": "Account-Number", "type": "string" }, "time-in-force": { "$ref": "#/$defs/OrderTimeInForce" }, "order-type": { "$ref": "#/$defs/OrderType" }, "underlying-symbol": { "title": "Underlying-Symbol", "type": "string" }, "underlying-instrument-type": { "$ref": "#/$defs/InstrumentType" }, "status": { "$ref": "#/$defs/OrderStatus" }, "cancellable": { "title": "Cancellable", "type": "boolean" }, "editable": { "title": "Editable", "type": "boolean" }, "edited": { "title": "Edited", "type": "boolean" }, "updated-at": { "format": "date-time", "title": "Updated-At", "type": "string" }, "legs": { "items": { "$ref": "#/$defs/Leg" }, "title": "Legs", "type": "array" }, "id": { "default": -1, "title": "Id", "type": "integer" }, "size": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Size" }, "price": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Price" }, "gtc-date": { "anyOf": [ { "format": "date", "type": "string" }, { "type": "null" } ], "default": null, "title": "Gtc-Date" }, "value": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Value" }, "stop-trigger": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Stop-Trigger" }, "contingent-status": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Contingent-Status" }, "confirmation-status": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Confirmation-Status" }, "cancelled-at": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "Cancelled-At" }, "cancel-user-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Cancel-User-Id" }, "cancel-username": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Cancel-Username" }, "replacing-order-id": { "anyOf": [ { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Replacing-Order-Id" }, "replaces-order-id": { "anyOf": [ { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Replaces-Order-Id" }, "in-flight-at": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "In-Flight-At" }, "live-at": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "Live-At" }, "received-at": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "Received-At" }, "reject-reason": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Reject-Reason" }, "user-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "User-Id" }, "username": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Username" }, "terminal-at": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "Terminal-At" }, "complex-order-id": { "anyOf": [ { "type": "string" }, { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Complex-Order-Id" }, "complex-order-tag": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Complex-Order-Tag" }, "preflight-id": { "anyOf": [ { "type": "string" }, { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Preflight-Id" }, "order-rule": { "anyOf": [ { "$ref": "#/$defs/OrderRule" }, { "type": "null" } ], "default": null }, "source": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Source" }, "external-identifier": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "External-Identifier" } }, "required": [ "account-number", "time-in-force", "order-type", "underlying-symbol", "underlying-instrument-type", "status", "cancellable", "editable", "edited", "updated-at", "legs" ], "title": "PlacedOrder", "type": "object" }, "PriceEffect": { "description": "This is an :class:`~enum.Enum` that shows the sign of a price effect, since\nTastytrade is apparently against negative numbers.", "enum": [ "Credit", "Debit", "None" ], "title": "PriceEffect", "type": "string" } }, "required": [ "buying-power-effect", "complex-order" ] }

buying_power_effect (tastytrade.order.BuyingPowerEffect)

complex_order (tastytrade.order.PlacedComplexOrder)

errors (list[tastytrade.order.Message] | None)

fee_calculation (tastytrade.order.FeeCalculation | None)

warnings (list[tastytrade.order.Message] | None)

Bases: TastytradeData

Dataclass containing information about an existing order, whether it’s been filled or not.

Show JSON schema{ "title": "PlacedOrder", "description": "Dataclass containing information about an existing order, whether it's\nbeen filled or not.", "type": "object", "properties": { "account-number": { "title": "Account-Number", "type": "string" }, "time-in-force": { "$ref": "#/$defs/OrderTimeInForce" }, "order-type": { "$ref": "#/$defs/OrderType" }, "underlying-symbol": { "title": "Underlying-Symbol", "type": "string" }, "underlying-instrument-type": { "$ref": "#/$defs/InstrumentType" }, "status": { "$ref": "#/$defs/OrderStatus" }, "cancellable": { "title": "Cancellable", "type": "boolean" }, "editable": { "title": "Editable", "type": "boolean" }, "edited": { "title": "Edited", "type": "boolean" }, "updated-at": { "format": "date-time", "title": "Updated-At", "type": "string" }, "legs": { "items": { "$ref": "#/$defs/Leg" }, "title": "Legs", "type": "array" }, "id": { "default": -1, "title": "Id", "type": "integer" }, "size": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Size" }, "price": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Price" }, "gtc-date": { "anyOf": [ { "format": "date", "type": "string" }, { "type": "null" } ], "default": null, "title": "Gtc-Date" }, "value": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Value" }, "stop-trigger": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Stop-Trigger" }, "contingent-status": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Contingent-Status" }, "confirmation-status": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Confirmation-Status" }, "cancelled-at": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "Cancelled-At" }, "cancel-user-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Cancel-User-Id" }, "cancel-username": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Cancel-Username" }, "replacing-order-id": { "anyOf": [ { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Replacing-Order-Id" }, "replaces-order-id": { "anyOf": [ { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Replaces-Order-Id" }, "in-flight-at": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "In-Flight-At" }, "live-at": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "Live-At" }, "received-at": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "Received-At" }, "reject-reason": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Reject-Reason" }, "user-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "User-Id" }, "username": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Username" }, "terminal-at": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "Terminal-At" }, "complex-order-id": { "anyOf": [ { "type": "string" }, { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Complex-Order-Id" }, "complex-order-tag": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Complex-Order-Tag" }, "preflight-id": { "anyOf": [ { "type": "string" }, { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Preflight-Id" }, "order-rule": { "anyOf": [ { "$ref": "#/$defs/OrderRule" }, { "type": "null" } ], "default": null }, "source": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Source" }, "external-identifier": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "External-Identifier" } }, "$defs": { "FillInfo": { "description": "Dataclass that contains information about an order fill.", "properties": { "fill-id": { "title": "Fill-Id", "type": "string" }, "quantity": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Quantity" }, "fill-price": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Fill-Price" }, "filled-at": { "format": "date-time", "title": "Filled-At", "type": "string" }, "destination-venue": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Destination-Venue" }, "ext-group-fill-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Ext-Group-Fill-Id" }, "ext-exec-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Ext-Exec-Id" } }, "required": [ "fill-id", "quantity", "fill-price", "filled-at" ], "title": "FillInfo", "type": "object" }, "InstrumentType": { "description": "This is an :class:`~enum.Enum` that contains the valid types of instruments\nand their representation in the API.", "enum": [ "Bond", "Cryptocurrency", "Currency Pair", "Equity", "Equity Offering", "Equity Option", "Fixed Income Security", "Future", "Future Option", "Index", "Liquidity Pool", "Unknown", "Warrant" ], "title": "InstrumentType", "type": "string" }, "Leg": { "description": "Dataclass that represents an order leg.\n\nClasses that inherit from :class:`TradeableTastytradeData` can\ncall :meth:`build_leg` to build a leg from the dataclass.", "properties": { "instrument-type": { "$ref": "#/$defs/InstrumentType" }, "symbol": { "title": "Symbol", "type": "string" }, "action": { "$ref": "#/$defs/OrderAction" }, "quantity": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Quantity" }, "remaining-quantity": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Remaining-Quantity" }, "fills": { "anyOf": [ { "items": { "$ref": "#/$defs/FillInfo" }, "type": "array" }, { "type": "null" } ], "default": null, "title": "Fills" } }, "required": [ "instrument-type", "symbol", "action" ], "title": "Leg", "type": "object" }, "OrderAction": { "description": "This is an :class:`~enum.Enum` that contains the valid order actions.", "enum": [ "Buy to Open", "Buy to Close", "Sell to Open", "Sell to Close", "Buy", "Sell" ], "title": "OrderAction", "type": "string" }, "OrderCondition": { "description": "Dataclass that represents an order condition for an order rule.", "properties": { "id": { "title": "Id", "type": "string" }, "action": { "title": "Action", "type": "string" }, "symbol": { "title": "Symbol", "type": "string" }, "instrument-type": { "$ref": "#/$defs/InstrumentType" }, "indicator": { "title": "Indicator", "type": "string" }, "comparator": { "title": "Comparator", "type": "string" }, "threshold": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Threshold" }, "is-threshold-based-on-notional": { "title": "Is-Threshold-Based-On-Notional", "type": "boolean" }, "triggered-at": { "format": "date-time", "title": "Triggered-At", "type": "string" }, "triggered-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Triggered-Value" }, "price-components": { "items": { "$ref": "#/$defs/OrderConditionPriceComponent" }, "title": "Price-Components", "type": "array" } }, "required": [ "id", "action", "symbol", "instrument-type", "indicator", "comparator", "threshold", "is-threshold-based-on-notional", "triggered-at", "triggered-value", "price-components" ], "title": "OrderCondition", "type": "object" }, "OrderConditionPriceComponent": { "description": "Dataclass that represents a price component of an order condition.", "properties": { "symbol": { "title": "Symbol", "type": "string" }, "instrument-type": { "$ref": "#/$defs/InstrumentType" }, "quantity": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Quantity" }, "quantity-direction": { "title": "Quantity-Direction", "type": "string" } }, "required": [ "symbol", "instrument-type", "quantity", "quantity-direction" ], "title": "OrderConditionPriceComponent", "type": "object" }, "OrderRule": { "description": "Dataclass that represents an order rule for a complex order.", "properties": { "route-after": { "format": "date-time", "title": "Route-After", "type": "string" }, "routed-at": { "format": "date-time", "title": "Routed-At", "type": "string" }, "cancel-at": { "format": "date-time", "title": "Cancel-At", "type": "string" }, "cancelled-at": { "format": "date-time", "title": "Cancelled-At", "type": "string" }, "order-conditions": { "items": { "$ref": "#/$defs/OrderCondition" }, "title": "Order-Conditions", "type": "array" } }, "required": [ "route-after", "routed-at", "cancel-at", "cancelled-at", "order-conditions" ], "title": "OrderRule", "type": "object" }, "OrderStatus": { "description": "This is an :class:`~enum.Enum` that contains different order statuses.\nA typical (successful) order follows a progression:\n\nRECEIVED -> LIVE -> FILLED", "enum": [ "Received", "Cancelled", "Filled", "Expired", "Live", "Rejected", "Contingent", "Routed", "In Flight", "Cancel Requested", "Replace Requested", "Removed", "Partially Removed" ], "title": "OrderStatus", "type": "string" }, "OrderTimeInForce": { "description": "This is an :class:`~enum.Enum` that contains the valid TIFs for orders.", "enum": [ "Day", "GTC", "GTD", "Ext", "GTC Ext", "IOC" ], "title": "OrderTimeInForce", "type": "string" }, "OrderType": { "description": "This is an :class:`~enum.Enum` that contains the valid types of orders.", "enum": [ "Limit", "Market", "Marketable Limit", "Stop", "Stop Limit", "Notional Market" ], "title": "OrderType", "type": "string" } }, "required": [ "account-number", "time-in-force", "order-type", "underlying-symbol", "underlying-instrument-type", "status", "cancellable", "editable", "edited", "updated-at", "legs" ] }

cancel_user_id (str | None)

cancel_username (str | None)

cancelled_at (datetime.datetime | None)

complex_order_id (str | int | None)

complex_order_tag (str | None)

confirmation_status (str | None)

contingent_status (str | None)

external_identifier (str | None)

gtc_date (datetime.date | None)

in_flight_at (datetime.datetime | None)

legs (list[tastytrade.order.Leg])

live_at (datetime.datetime | None)

order_rule (tastytrade.order.OrderRule | None)

order_type (tastytrade.order.OrderType)

preflight_id (str | int | None)

price (decimal.Decimal | None)

received_at (datetime.datetime | None)

reject_reason (str | None)

replaces_order_id (int | None)

replacing_order_id (int | None)

size (decimal.Decimal | None)

status (tastytrade.order.OrderStatus)

stop_trigger (str | None)

terminal_at (datetime.datetime | None)

time_in_force (tastytrade.order.OrderTimeInForce)

underlying_instrument_type (tastytrade.order.InstrumentType)

underlying_symbol (str)

updated_at (datetime.datetime)

username (str | None)

value (decimal.Decimal | None)

validate_price_effects » all fields

External identifier for the order, used to track orders across systems

validate_price_effects

the ID of the order; test orders placed with dry_run don’t have an ID

validate_price_effects

Bases: TastytradeData

Dataclass grouping together information about a placed order.

Show JSON schema{ "title": "PlacedOrderResponse", "description": "Dataclass grouping together information about a placed order.", "type": "object", "properties": { "buying-power-effect": { "$ref": "#/$defs/BuyingPowerEffect" }, "order": { "$ref": "#/$defs/PlacedOrder" }, "fee-calculation": { "anyOf": [ { "$ref": "#/$defs/FeeCalculation" }, { "type": "null" } ], "default": null }, "warnings": { "anyOf": [ { "items": { "$ref": "#/$defs/Message" }, "type": "array" }, { "type": "null" } ], "default": null, "title": "Warnings" }, "errors": { "anyOf": [ { "items": { "$ref": "#/$defs/Message" }, "type": "array" }, { "type": "null" } ], "default": null, "title": "Errors" } }, "$defs": { "BuyingPowerEffect": { "description": "Dataclass containing information about the effect of a trade on buying\npower.", "properties": { "change-in-margin-requirement": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Change-In-Margin-Requirement" }, "change-in-buying-power": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Change-In-Buying-Power" }, "current-buying-power": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Current-Buying-Power" }, "new-buying-power": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "New-Buying-Power" }, "isolated-order-margin-requirement": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Isolated-Order-Margin-Requirement" }, "is-spread": { "title": "Is-Spread", "type": "boolean" }, "impact": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Impact" }, "effect": { "$ref": "#/$defs/PriceEffect" } }, "required": [ "change-in-margin-requirement", "change-in-buying-power", "current-buying-power", "new-buying-power", "isolated-order-margin-requirement", "is-spread", "impact", "effect" ], "title": "BuyingPowerEffect", "type": "object" }, "FeeCalculation": { "description": "Dataclass containing information about the fees associated with a trade.", "properties": { "regulatory-fees": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Regulatory-Fees" }, "clearing-fees": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Clearing-Fees" }, "commission": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Commission" }, "proprietary-index-option-fees": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Proprietary-Index-Option-Fees" }, "total-fees": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Total-Fees" } }, "required": [ "regulatory-fees", "clearing-fees", "commission", "proprietary-index-option-fees", "total-fees" ], "title": "FeeCalculation", "type": "object" }, "FillInfo": { "description": "Dataclass that contains information about an order fill.", "properties": { "fill-id": { "title": "Fill-Id", "type": "string" }, "quantity": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Quantity" }, "fill-price": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Fill-Price" }, "filled-at": { "format": "date-time", "title": "Filled-At", "type": "string" }, "destination-venue": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Destination-Venue" }, "ext-group-fill-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Ext-Group-Fill-Id" }, "ext-exec-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Ext-Exec-Id" } }, "required": [ "fill-id", "quantity", "fill-price", "filled-at" ], "title": "FillInfo", "type": "object" }, "InstrumentType": { "description": "This is an :class:`~enum.Enum` that contains the valid types of instruments\nand their representation in the API.", "enum": [ "Bond", "Cryptocurrency", "Currency Pair", "Equity", "Equity Offering", "Equity Option", "Fixed Income Security", "Future", "Future Option", "Index", "Liquidity Pool", "Unknown", "Warrant" ], "title": "InstrumentType", "type": "string" }, "Leg": { "description": "Dataclass that represents an order leg.\n\nClasses that inherit from :class:`TradeableTastytradeData` can\ncall :meth:`build_leg` to build a leg from the dataclass.", "properties": { "instrument-type": { "$ref": "#/$defs/InstrumentType" }, "symbol": { "title": "Symbol", "type": "string" }, "action": { "$ref": "#/$defs/OrderAction" }, "quantity": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Quantity" }, "remaining-quantity": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Remaining-Quantity" }, "fills": { "anyOf": [ { "items": { "$ref": "#/$defs/FillInfo" }, "type": "array" }, { "type": "null" } ], "default": null, "title": "Fills" } }, "required": [ "instrument-type", "symbol", "action" ], "title": "Leg", "type": "object" }, "Message": { "description": "Dataclass that represents a message from the Tastytrade API, usually\na warning or an error.", "properties": { "code": { "title": "Code", "type": "string" }, "message": { "title": "Message", "type": "string" }, "preflight-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Preflight-Id" } }, "required": [ "code", "message" ], "title": "Message", "type": "object" }, "OrderAction": { "description": "This is an :class:`~enum.Enum` that contains the valid order actions.", "enum": [ "Buy to Open", "Buy to Close", "Sell to Open", "Sell to Close", "Buy", "Sell" ], "title": "OrderAction", "type": "string" }, "OrderCondition": { "description": "Dataclass that represents an order condition for an order rule.", "properties": { "id": { "title": "Id", "type": "string" }, "action": { "title": "Action", "type": "string" }, "symbol": { "title": "Symbol", "type": "string" }, "instrument-type": { "$ref": "#/$defs/InstrumentType" }, "indicator": { "title": "Indicator", "type": "string" }, "comparator": { "title": "Comparator", "type": "string" }, "threshold": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Threshold" }, "is-threshold-based-on-notional": { "title": "Is-Threshold-Based-On-Notional", "type": "boolean" }, "triggered-at": { "format": "date-time", "title": "Triggered-At", "type": "string" }, "triggered-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Triggered-Value" }, "price-components": { "items": { "$ref": "#/$defs/OrderConditionPriceComponent" }, "title": "Price-Components", "type": "array" } }, "required": [ "id", "action", "symbol", "instrument-type", "indicator", "comparator", "threshold", "is-threshold-based-on-notional", "triggered-at", "triggered-value", "price-components" ], "title": "OrderCondition", "type": "object" }, "OrderConditionPriceComponent": { "description": "Dataclass that represents a price component of an order condition.", "properties": { "symbol": { "title": "Symbol", "type": "string" }, "instrument-type": { "$ref": "#/$defs/InstrumentType" }, "quantity": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Quantity" }, "quantity-direction": { "title": "Quantity-Direction", "type": "string" } }, "required": [ "symbol", "instrument-type", "quantity", "quantity-direction" ], "title": "OrderConditionPriceComponent", "type": "object" }, "OrderRule": { "description": "Dataclass that represents an order rule for a complex order.", "properties": { "route-after": { "format": "date-time", "title": "Route-After", "type": "string" }, "routed-at": { "format": "date-time", "title": "Routed-At", "type": "string" }, "cancel-at": { "format": "date-time", "title": "Cancel-At", "type": "string" }, "cancelled-at": { "format": "date-time", "title": "Cancelled-At", "type": "string" }, "order-conditions": { "items": { "$ref": "#/$defs/OrderCondition" }, "title": "Order-Conditions", "type": "array" } }, "required": [ "route-after", "routed-at", "cancel-at", "cancelled-at", "order-conditions" ], "title": "OrderRule", "type": "object" }, "OrderStatus": { "description": "This is an :class:`~enum.Enum` that contains different order statuses.\nA typical (successful) order follows a progression:\n\nRECEIVED -> LIVE -> FILLED", "enum": [ "Received", "Cancelled", "Filled", "Expired", "Live", "Rejected", "Contingent", "Routed", "In Flight", "Cancel Requested", "Replace Requested", "Removed", "Partially Removed" ], "title": "OrderStatus", "type": "string" }, "OrderTimeInForce": { "description": "This is an :class:`~enum.Enum` that contains the valid TIFs for orders.", "enum": [ "Day", "GTC", "GTD", "Ext", "GTC Ext", "IOC" ], "title": "OrderTimeInForce", "type": "string" }, "OrderType": { "description": "This is an :class:`~enum.Enum` that contains the valid types of orders.", "enum": [ "Limit", "Market", "Marketable Limit", "Stop", "Stop Limit", "Notional Market" ], "title": "OrderType", "type": "string" }, "PlacedOrder": { "description": "Dataclass containing information about an existing order, whether it's\nbeen filled or not.", "properties": { "account-number": { "title": "Account-Number", "type": "string" }, "time-in-force": { "$ref": "#/$defs/OrderTimeInForce" }, "order-type": { "$ref": "#/$defs/OrderType" }, "underlying-symbol": { "title": "Underlying-Symbol", "type": "string" }, "underlying-instrument-type": { "$ref": "#/$defs/InstrumentType" }, "status": { "$ref": "#/$defs/OrderStatus" }, "cancellable": { "title": "Cancellable", "type": "boolean" }, "editable": { "title": "Editable", "type": "boolean" }, "edited": { "title": "Edited", "type": "boolean" }, "updated-at": { "format": "date-time", "title": "Updated-At", "type": "string" }, "legs": { "items": { "$ref": "#/$defs/Leg" }, "title": "Legs", "type": "array" }, "id": { "default": -1, "title": "Id", "type": "integer" }, "size": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Size" }, "price": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Price" }, "gtc-date": { "anyOf": [ { "format": "date", "type": "string" }, { "type": "null" } ], "default": null, "title": "Gtc-Date" }, "value": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Value" }, "stop-trigger": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Stop-Trigger" }, "contingent-status": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Contingent-Status" }, "confirmation-status": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Confirmation-Status" }, "cancelled-at": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "Cancelled-At" }, "cancel-user-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Cancel-User-Id" }, "cancel-username": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Cancel-Username" }, "replacing-order-id": { "anyOf": [ { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Replacing-Order-Id" }, "replaces-order-id": { "anyOf": [ { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Replaces-Order-Id" }, "in-flight-at": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "In-Flight-At" }, "live-at": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "Live-At" }, "received-at": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "Received-At" }, "reject-reason": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Reject-Reason" }, "user-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "User-Id" }, "username": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Username" }, "terminal-at": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "Terminal-At" }, "complex-order-id": { "anyOf": [ { "type": "string" }, { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Complex-Order-Id" }, "complex-order-tag": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Complex-Order-Tag" }, "preflight-id": { "anyOf": [ { "type": "string" }, { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Preflight-Id" }, "order-rule": { "anyOf": [ { "$ref": "#/$defs/OrderRule" }, { "type": "null" } ], "default": null }, "source": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Source" }, "external-identifier": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "External-Identifier" } }, "required": [ "account-number", "time-in-force", "order-type", "underlying-symbol", "underlying-instrument-type", "status", "cancellable", "editable", "edited", "updated-at", "legs" ], "title": "PlacedOrder", "type": "object" }, "PriceEffect": { "description": "This is an :class:`~enum.Enum` that shows the sign of a price effect, since\nTastytrade is apparently against negative numbers.", "enum": [ "Credit", "Debit", "None" ], "title": "PriceEffect", "type": "string" } }, "required": [ "buying-power-effect", "order" ] }

buying_power_effect (tastytrade.order.BuyingPowerEffect)

errors (list[tastytrade.order.Message] | None)

fee_calculation (tastytrade.order.FeeCalculation | None)

order (tastytrade.order.PlacedOrder)

warnings (list[tastytrade.order.Message] | None)

Bases: TastytradeData

Dataclass that represents a tradeable instrument.

Classes that inherit from this class can call build_leg() to build a leg from the dataclass.

Show JSON schema{ "title": "TradeableTastytradeData", "description": "Dataclass that represents a tradeable instrument.\n\nClasses that inherit from this class can call :meth:`build_leg` to build a\nleg from the dataclass.", "type": "object", "properties": { "instrument-type": { "$ref": "#/$defs/InstrumentType" }, "symbol": { "title": "Symbol", "type": "string" } }, "$defs": { "InstrumentType": { "description": "This is an :class:`~enum.Enum` that contains the valid types of instruments\nand their representation in the API.", "enum": [ "Bond", "Cryptocurrency", "Currency Pair", "Equity", "Equity Offering", "Equity Option", "Fixed Income Security", "Future", "Future Option", "Index", "Liquidity Pool", "Unknown", "Warrant" ], "title": "InstrumentType", "type": "string" } }, "required": [ "instrument-type", "symbol" ] }

instrument_type (tastytrade.order.InstrumentType)

Builds an order Leg from the dataclass.

the quantity of the symbol to trade, set this as None for notional orders

OrderAction to perform, e.g. BUY_TO_OPEN

**Examples:**

Example 1 (json):
```json
{
   "title": "AdvancedInstructions",
   "description": "Dataclass containing advanced order rules.",
   "type": "object",
   "properties": {
      "strict-position-effect-validation": {
         "default": false,
         "title": "Strict-Position-Effect-Validation",
         "type": "boolean"
      }
   }
}
```

Example 2 (json):
```json
{
   "title": "BuyingPowerEffect",
   "description": "Dataclass containing information about the effect of a trade on buying\npower.",
   "type": "object",
   "properties": {
      "change-in-margin-requirement": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Change-In-Margin-Requirement"
      },
      "change-in-buying-power": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Change-In-Buying-Power"
      },
      "current-buying-power": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Current-Buying-Power"
      },
      "new-buying-power": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "New-Buying-Power"
      },
      "isolated-order-margin-requirement": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Isolated-Order-Margin-Requirement"
      },
      "is-spread": {
         "title": "Is-Spread",
         "type": "boolean"
      },
      "impact": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Impact"
      },
      "effect": {
         "$ref": "#/$defs/PriceEffect"
      }
   },
   "$defs": {
      "PriceEffect": {
         "description": "This is an :class:`~enum.Enum` that shows the sign of a price effect, since\nTastytrade is apparently against negative numbers.",
         "enum": [
            "Credit",
            "Debit",
            "None"
         ],
         "title": "PriceEffect",
         "type": "string"
      }
   },
   "required": [
      "change-in-margin-requirement",
      "change-in-buying-power",
      "current-buying-power",
      "new-buying-power",
      "isolated-order-margin-requirement",
      "is-spread",
      "impact",
      "effect"
   ]
}
```

Example 3 (json):
```json
{
   "title": "FeeCalculation",
   "description": "Dataclass containing information about the fees associated with a trade.",
   "type": "object",
   "properties": {
      "regulatory-fees": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Regulatory-Fees"
      },
      "clearing-fees": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Clearing-Fees"
      },
      "commission": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Commission"
      },
      "proprietary-index-option-fees": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Proprietary-Index-Option-Fees"
      },
      "total-fees": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Total-Fees"
      }
   },
   "required": [
      "regulatory-fees",
      "clearing-fees",
      "commission",
      "proprietary-index-option-fees",
      "total-fees"
   ]
}
```

Example 4 (json):
```json
{
   "title": "FillInfo",
   "description": "Dataclass that contains information about an order fill.",
   "type": "object",
   "properties": {
      "fill-id": {
         "title": "Fill-Id",
         "type": "string"
      },
      "quantity": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Quantity"
      },
      "fill-price": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Fill-Price"
      },
      "filled-at": {
         "format": "date-time",
         "title": "Filled-At",
         "type": "string"
      },
      "destination-venue": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Destination-Venue"
      },
      "ext-group-fill-id": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Ext-Group-Fill-Id"
      },
      "ext-exec-id": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Ext-Exec-Id"
      }
   },
   "required": [
      "fill-id",
      "quantity",
      "fill-price",
      "filled-at"
   ]
}
```

---

## Market Sessions - tastytrade 11.1.0 documentation

**URL:** https://tastyworks-api.readthedocs.io/en/latest/market-sessions.html

**Contents:**
- Market Sessions¶

A market time session object contains information about the current state of specific markets. It can be used to get the market opening and closing times and state.

The dataclass represents the current session and any nested ‘next’ or ‘previous’ session info.

The get_market_sessions function can be used to obtain information about the current session:

The get_market_holidays function can be used to obtain information about markets half days and holidays:

I case you only want to extract the market status, this is one way to do it:

**Examples:**

Example 1 (sql):
```sql
from tastytrade.market_sessions import ExchangeType, get_market_sessions
get_market_sessions(session, exchanges=[ExchangeType.NYSE])
```

Example 2 (rust):
```rust
>>> [MarketSession(close_at=None, close_at_ext=None, instrument_collection='Equity', open_at=None, start_at=None, next_session=MarketSessionSnapshot(close_at=datetime.datetime(2025, 2, 18, 21, 0, tzinfo=TzInfo(UTC)), close_at_ext=datetime.datetime(2025, 2, 19, 1, 0, tzinfo=TzInfo(UTC)), instrument_collection='Equity', open_at=datetime.datetime(2025, 2, 18, 14, 30, tzinfo=TzInfo(UTC)), session_date=datetime.date(2025, 2, 18), start_at=datetime.datetime(2025, 2, 18, 13, 15, tzinfo=TzInfo(UTC))), previous_session=MarketSessionSnapshot(close_at=datetime.datetime(2025, 2, 14, 21, 0, tzinfo=TzInfo(UTC)), close_at_ext=datetime.datetime(2025, 2, 15, 1, 0, tzinfo=TzInfo(UTC)), instrument_collection='Equity', open_at=datetime.datetime(2025, 2, 14, 14, 30, tzinfo=TzInfo(UTC)), session_date=datetime.date(2025, 2, 14), start_at=datetime.datetime(2025, 2, 14, 13, 15, tzinfo=TzInfo(UTC))), status=<MarketStatus.CLOSED: 'Closed'>)]
```

Example 3 (swift):
```swift
from tastytrade.market_sessions import get_market_holidays
calendar = Market.get_market_holidays(session)
print(calendar.half_days)
print(calendar.holidays)
```

Example 4 (unknown):
```unknown
>>> [datetime.date(2015, 12, 24), datetime.date(2016, 11, 25), datetime.date(2017, 7, 3), datetime.date(2017, 11, 24), datetime.date(2018, 7, 3), datetime.date(2018, 11, 23), datetime.date(2018, 12, 24), datetime.date(2019, 7, 3), datetime.date(2019, 11, 29), datetime.date(2019, 12, 24), datetime.date(2020, 11, 27), datetime.date(2020, 12, 24), datetime.date(2021, 11, 26), datetime.date(2022, 11, 25), datetime.date(2023, 7, 3), datetime.date(2023, 11, 24), datetime.date(2024, 7, 3), datetime.date(2024, 11, 29), datetime.date(2024, 12, 24), datetime.date(2025, 7, 3), datetime.date(2025, 11, 28), datetime.date(2025, 12, 24), datetime.date(2026, 11, 27), datetime.date(2026, 12, 24), datetime.date(2027, 7, 2), datetime.date(2027, 11, 26), datetime.date(2027, 12, 23), datetime.date(2028, 7, 3), datetime.date(2028, 11, 24), datetime.date(2028, 12, 22), datetime.date(2029, 7, 3)]
>>> [datetime.date(2015, 12, 25), datetime.date(2016, 1, 1), datetime.date(2016, 1, 18), datetime.date(2016, 2, 15), datetime.date(2016, 3, 25), datetime.date(2016, 5, 30), datetime.date(2016, 7, 4), datetime.date(2016, 9, 5), datetime.date(2016, 11, 24), datetime.date(2016, 12, 26), datetime.date(2017, 1, 2), datetime.date(2017, 1, 16), datetime.date(2017, 2, 20), datetime.date(2017, 4, 14), datetime.date(2017, 5, 29), datetime.date(2017, 7, 4), datetime.date(2017, 9, 4), datetime.date(2017, 11, 23), datetime.date(2017, 12, 25), datetime.date(2018, 1, 1), datetime.date(2018, 1, 15), datetime.date(2018, 2, 19), datetime.date(2018, 3, 30), datetime.date(2018, 5, 28), datetime.date(2018, 7, 4), datetime.date(2018, 9, 3), datetime.date(2018, 11, 22), datetime.date(2018, 12, 5), datetime.date(2018, 12, 25), datetime.date(2019, 1, 1), datetime.date(2019, 1, 21), datetime.date(2019, 2, 18), datetime.date(2019, 4, 19), datetime.date(2019, 5, 27), datetime.date(2019, 7, 4), datetime.date(2019, 9, 2), datetime.date(2019, 11, 28), datetime.date(2019, 12, 25), datetime.date(2020, 1, 1), datetime.date(2020, 1, 20), datetime.date(2020, 2, 17), datetime.date(2020, 4, 10), datetime.date(2020, 5, 25), datetime.date(2020, 7, 3), datetime.date(2020, 9, 7), datetime.date(2020, 11, 26), datetime.date(2020, 12, 25), datetime.date(2021, 1, 1), datetime.date(2021, 1, 18), datetime.date(2021, 2, 15), datetime.date(2021, 4, 2), datetime.date(2021, 5, 31), datetime.date(2021, 7, 5), datetime.date(2021, 9, 6), datetime.date(2021, 11, 25), datetime.date(2021, 12, 24), datetime.date(2022, 1, 17), datetime.date(2022, 2, 21), datetime.date(2022, 4, 15), datetime.date(2022, 5, 30), datetime.date(2022, 6, 20), datetime.date(2022, 7, 4), datetime.date(2022, 9, 5), datetime.date(2022, 11, 24), datetime.date(2022, 12, 26), datetime.date(2023, 1, 2), datetime.date(2023, 1, 16), datetime.date(2023, 2, 20), datetime.date(2023, 4, 7), datetime.date(2023, 5, 29), datetime.date(2023, 6, 19), datetime.date(2023, 7, 4), datetime.date(2023, 9, 4), datetime.date(2023, 11, 23), datetime.date(2023, 12, 25), datetime.date(2024, 1, 1), datetime.date(2024, 1, 15), datetime.date(2024, 2, 19), datetime.date(2024, 3, 29), datetime.date(2024, 5, 27), datetime.date(2024, 6, 19), datetime.date(2024, 7, 4), datetime.date(2024, 9, 2), datetime.date(2024, 11, 28), datetime.date(2024, 12, 25), datetime.date(2025, 1, 1), datetime.date(2025, 1, 9), datetime.date(2025, 1, 20), datetime.date(2025, 2, 17), datetime.date(2025, 4, 18), datetime.date(2025, 5, 26), datetime.date(2025, 6, 19), datetime.date(2025, 7, 4), datetime.date(2025, 9, 1), datetime.date(2025, 11, 27), datetime.date(2025, 12, 25), datetime.date(2026, 1, 1), datetime.date(2026, 1, 19), datetime.date(2026, 2, 16), datetime.date(2026, 4, 3), datetime.date(2026, 5, 25), datetime.date(2026, 6, 19), datetime.date(2026, 7, 3), datetime.date(2026, 9, 7), datetime.date(2026, 11, 26), datetime.date(2026, 12, 25), datetime.date(2027, 1, 1), datetime.date(2027, 1, 18), datetime.date(2027, 2, 15), datetime.date(2027, 3, 26), datetime.date(2027, 5, 31), datetime.date(2027, 6, 18), datetime.date(2027, 7, 5), datetime.date(2027, 9, 6), datetime.date(2027, 11, 25), datetime.date(2027, 12, 24), datetime.date(2028, 1, 17), datetime.date(2028, 2, 21), datetime.date(2028, 4, 14), datetime.date(2028, 5, 29), datetime.date(2028, 6, 19), datetime.date(2028, 7, 4), datetime.date(2028, 9, 4), datetime.date(2028, 11, 23), datetime.date(2028, 12, 25), datetime.date(2029, 1, 1), datetime.date(2029, 1, 15), datetime.date(2029, 2, 19), datetime.date(2029, 3, 30), datetime.date(2029, 5, 28), datetime.date(2029, 6, 19), datetime.date(2029, 7, 4), datetime.date(2029, 9, 3)]
```

---

## tastytrade.dxfeed - tastytrade 11.1.0 documentation

**URL:** https://tastyworks-api.readthedocs.io/en/latest/api/dxfeed.html

**Contents:**
- tastytrade.dxfeed¶
- Event¶
- Candle¶
- Greeks¶
- Profile¶
- Quote¶
- Summary¶
- TimeAndSale¶
- TheoPrice¶
- Trade¶

For general dxfeed symbology, go to Formats, where you’ll find information on various kinds of formatting.

For options on futures symbology, go to CME Group and look at the ‘Specs’ section for the given futures symbol.

If you want to double-check you typed the symbol right, or want to troubleshoot a hanging request, go to dxfeed Symbol Lookup and type in the same symbol.

Base class for dxfeed events received from the data streamer.

Show JSON schema{ "title": "Event", "description": "Base class for dxfeed events received from the data streamer.", "type": "object", "properties": { "eventSymbol": { "title": "Eventsymbol", "type": "string" }, "eventTime": { "title": "Eventtime", "type": "integer" } }, "required": [ "eventSymbol", "eventTime" ] }

change_nan_to_none » all fields

Makes a list of event objects from a list of raw trade data fetched by a DXFeedStreamer.

list of raw quote data from streamer

A dxfeed IndexedEvent with flags computed bitwise. For info see here.

Show JSON schema{ "title": "IndexedEvent", "description": "A dxfeed `IndexedEvent` with flags computed bitwise.\nFor info see `here <https://docs.dxfeed.com/dxfeed/api/com/dxfeed/event/IndexedEvent.html>`_.", "type": "object", "properties": { "eventSymbol": { "title": "Eventsymbol", "type": "string" }, "eventTime": { "title": "Eventtime", "type": "integer" }, "eventFlags": { "title": "Eventflags", "type": "integer" } }, "required": [ "eventSymbol", "eventTime", "eventFlags" ] }

TX_PENDING is an indicator of pending transactional update. When txPending is true it means, that an ongoing transaction update that spans multiple events is in process. All events with txPending true shall be put into a separate pending list for each source id and should be processed later when an event for this source id with txPending false comes.

REMOVE_EVENT is used to indicate that that the event with the corresponding index has to be removed.

SNAPSHOT_BEGIN is used to indicate when the loading of a snapshot starts. Snapshot load starts on new subscription and the first indexed event that arrives for each non-zero source id on new subscription may have snapshotBegin set to true. It means, that an ongoing snapshot consisting of multiple events is incoming. All events for this source id shall be put into a separate pending list for each source id.

SNAPSHOT_END or SNAPSHOT_SNIP are used to indicate the end of a snapshot. The last event of a snapshot is marked with either snapshotEnd or snapshotSnip. At this time, all events from a pending list for the corresponding source can be processed, unless txPending is also set to true. In the later case, the processing shall be further delayed due to ongoing transaction.

The difference between snapshotEnd and snapshotSnip is the following: snapshotEnd indicates that the data source had sent all the data pertaining to the subscription for the corresponding indexed event, while snapshotSnip indicates that some limit on the amount of data was reached and while there still might be more data available, it will not be provided.

SNAPSHOT_MODE is used to instruct dxFeed to use snapshot mode. It is intended to be used only for publishing to activate (if not yet activated) snapshot mode. The difference from SNAPSHOT_BEGIN flag is that SNAPSHOT_MODE only switches on snapshot mode without starting snapshot synchronization protocol. When a snapshot is empty or consists of a single event, then the event can have both snapshotBegin and snapshotEnd or snapshotSnip flags. In case of an empty snapshot, removeEvent on this event is also set to true.

SNAPSHOT_END or SNAPSHOT_SNIP are used to indicate the end of a snapshot. The last event of a snapshot is marked with either snapshotEnd or snapshotSnip. At this time, all events from a pending list for the corresponding source can be processed, unless txPending is also set to true. In the later case, the processing shall be further delayed due to ongoing transaction.

The difference between snapshotEnd and snapshotSnip is the following: snapshotEnd indicates that the data source had sent all the data pertaining to the subscription for the corresponding indexed event, while snapshotSnip indicates that some limit on the amount of data was reached and while there still might be more data available, it will not be provided.

A Candle event with open, high, low, close prices and other information for a specific period. Candles are build with a specified period using a specified price type with data taken from a specified exchange.

Show JSON schema{ "title": "Candle", "description": "A Candle event with open, high, low, close prices and other information\nfor a specific period. Candles are build with a specified period using a\nspecified price type with data taken from a specified exchange.", "type": "object", "properties": { "eventSymbol": { "title": "Eventsymbol", "type": "string" }, "eventTime": { "title": "Eventtime", "type": "integer" }, "eventFlags": { "title": "Eventflags", "type": "integer" }, "index": { "title": "Index", "type": "integer" }, "time": { "title": "Time", "type": "integer" }, "sequence": { "title": "Sequence", "type": "integer" }, "count": { "title": "Count", "type": "integer" }, "volume": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Volume" }, "vwap": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Vwap" }, "bidVolume": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Bidvolume" }, "askVolume": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Askvolume" }, "impVolatility": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Impvolatility" }, "openInterest": { "anyOf": [ { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Openinterest" }, "open": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Open" }, "high": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "High" }, "low": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Low" }, "close": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Close" } }, "required": [ "eventSymbol", "eventTime", "eventFlags", "index", "time", "sequence", "count", "open", "high", "low", "close" ] }

ask_volume (decimal.Decimal | None)

bid_volume (decimal.Decimal | None)

close (Annotated[decimal.Decimal, pydantic.functional_validators.WrapValidator(func=tastytrade.dxfeed.candle.zero_from_none, json_schema_input_type=PydanticUndefined)])

high (Annotated[decimal.Decimal, pydantic.functional_validators.WrapValidator(func=tastytrade.dxfeed.candle.zero_from_none, json_schema_input_type=PydanticUndefined)])

imp_volatility (decimal.Decimal | None)

low (Annotated[decimal.Decimal, pydantic.functional_validators.WrapValidator(func=tastytrade.dxfeed.candle.zero_from_none, json_schema_input_type=PydanticUndefined)])

open (Annotated[decimal.Decimal, pydantic.functional_validators.WrapValidator(func=tastytrade.dxfeed.candle.zero_from_none, json_schema_input_type=PydanticUndefined)])

open_interest (int | None)

volume (decimal.Decimal | None)

vwap (decimal.Decimal | None)

ask volume in the candle

bid volume in the candle

the last (close) price of the candle

func = <function zero_from_none at 0x701909e701f0>

json_schema_input_type = PydanticUndefined

total number of events in the candle

the maximal (high) price of the candle

func = <function zero_from_none at 0x701909e701f0>

json_schema_input_type = PydanticUndefined

implied volatility in the candle

unique per-symbol index of this candle event

the minimal (low) price of the candle

func = <function zero_from_none at 0x701909e701f0>

json_schema_input_type = PydanticUndefined

the first (open) price of the candle

func = <function zero_from_none at 0x701909e701f0>

json_schema_input_type = PydanticUndefined

open interest in the candle

sequence number of this event

timestamp of the candle in milliseconds

the total volume of the candle

volume-weighted average price

Greek ratios, or simply Greeks, are differential values that show how the price of an option depends on other market parameters: on the price of the underlying asset, its volatility, etc. Greeks are used to assess the risks of customer portfolios. Greeks are derivatives of the value of securities in different axes. If a derivative is very far from zero, then the portfolio has a risky sensitivity in this parameter.

Show JSON schema{ "title": "Greeks", "description": "Greek ratios, or simply Greeks, are differential values that show how the\nprice of an option depends on other market parameters: on the price of the\nunderlying asset, its volatility, etc. Greeks are used to assess the risks\nof customer portfolios. Greeks are derivatives of the value of securities\nin different axes. If a derivative is very far from zero, then the\nportfolio has a risky sensitivity in this parameter.", "type": "object", "properties": { "eventSymbol": { "title": "Eventsymbol", "type": "string" }, "eventTime": { "title": "Eventtime", "type": "integer" }, "eventFlags": { "title": "Eventflags", "type": "integer" }, "index": { "title": "Index", "type": "integer" }, "time": { "title": "Time", "type": "integer" }, "sequence": { "title": "Sequence", "type": "integer" }, "price": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Price" }, "volatility": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Volatility" }, "delta": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Delta" }, "gamma": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Gamma" }, "theta": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Theta" }, "rho": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Rho" }, "vega": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Vega" } }, "required": [ "eventSymbol", "eventTime", "eventFlags", "index", "time", "sequence", "price", "volatility", "delta", "gamma", "theta", "rho", "vega" ] }

delta (decimal.Decimal)

gamma (decimal.Decimal)

price (decimal.Decimal)

rho (decimal.Decimal)

theta (decimal.Decimal)

vega (decimal.Decimal)

volatility (decimal.Decimal)

unique per-symbol index of this event

sequence number to distinguish events that have the same time

timestamp of this event in milliseconds

Black-Scholes implied volatility of the option

A Profile event provides the security instrument description. It represents the most recent information that is available about the traded security on the market at any given moment of time.

Show JSON schema{ "title": "Profile", "description": "A Profile event provides the security instrument description. It\nrepresents the most recent information that is available about the\ntraded security on the market at any given moment of time.", "type": "object", "properties": { "eventSymbol": { "title": "Eventsymbol", "type": "string" }, "eventTime": { "title": "Eventtime", "type": "integer" }, "description": { "title": "Description", "type": "string" }, "shortSaleRestriction": { "title": "Shortsalerestriction", "type": "string" }, "tradingStatus": { "title": "Tradingstatus", "type": "string" }, "haltStartTime": { "title": "Haltstarttime", "type": "integer" }, "haltEndTime": { "title": "Haltendtime", "type": "integer" }, "exDividendDayId": { "title": "Exdividenddayid", "type": "integer" }, "statusReason": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Statusreason" }, "high52WeekPrice": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "High52Weekprice" }, "low52WeekPrice": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Low52Weekprice" }, "beta": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Beta" }, "shares": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Shares" }, "highLimitPrice": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Highlimitprice" }, "lowLimitPrice": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Lowlimitprice" }, "earningsPerShare": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Earningspershare" }, "exDividendAmount": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Exdividendamount" }, "dividendFrequency": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Dividendfrequency" }, "freeFloat": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Freefloat" } }, "required": [ "eventSymbol", "eventTime", "description", "shortSaleRestriction", "tradingStatus", "haltStartTime", "haltEndTime", "exDividendDayId" ] }

beta (decimal.Decimal | None)

dividend_frequency (decimal.Decimal | None)

earnings_per_share (decimal.Decimal | None)

ex_dividend_amount (decimal.Decimal | None)

ex_dividend_day_id (int)

free_float (decimal.Decimal | None)

halt_start_time (int)

high_52_week_price (decimal.Decimal | None)

high_limit_price (decimal.Decimal | None)

low_52_week_price (decimal.Decimal | None)

low_limit_price (decimal.Decimal | None)

shares (decimal.Decimal | None)

short_sale_restriction (str)

status_reason (str | None)

the correlation coefficient of the instrument to the S&P500 index

description of the security instrument

frequency of cash dividends payments per year (calculated)

the amount of the last paid dividend

identifier of the ex-dividend date

the number of shares that are available to the public for trade

ending time of the trading halt interval

starting time of the trading halt interval

maximal (high) price in last 52 weeks

maximal (high) allowed price

minimal (low) price in last 52 weeks

minimal (low) allowed price

short sale restriction of the security instrument possible values are ACTIVE | INACTIVE | UNDEFINED

description of the reason that trading was halted

trading status of the security instrument possible values are ACTIVE | HALTED | UNDEFINED

A Quote event is a snapshot of the best bid and ask prices, and other fields that change with each quote.

Show JSON schema{ "title": "Quote", "description": "A Quote event is a snapshot of the best bid and ask prices, and other\nfields that change with each quote.", "type": "object", "properties": { "eventSymbol": { "title": "Eventsymbol", "type": "string" }, "eventTime": { "title": "Eventtime", "type": "integer" }, "sequence": { "title": "Sequence", "type": "integer" }, "timeNanoPart": { "title": "Timenanopart", "type": "integer" }, "bidTime": { "title": "Bidtime", "type": "integer" }, "bidExchangeCode": { "title": "Bidexchangecode", "type": "string" }, "askTime": { "title": "Asktime", "type": "integer" }, "askExchangeCode": { "title": "Askexchangecode", "type": "string" }, "bidPrice": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Bidprice" }, "askPrice": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Askprice" }, "bidSize": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Bidsize" }, "askSize": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Asksize" } }, "required": [ "eventSymbol", "eventTime", "sequence", "timeNanoPart", "bidTime", "bidExchangeCode", "askTime", "askExchangeCode", "bidPrice", "askPrice" ] }

ask_exchange_code (str)

ask_price (decimal.Decimal)

ask_size (decimal.Decimal | None)

bid_exchange_code (str)

bid_price (decimal.Decimal)

bid_size (decimal.Decimal | None)

ask size as integer number (rounded toward zero) or decimal for cryptocurrencies

time of the last ask change

bid size as integer number (rounded toward zero) or decimal for cryptocurrencies

time of the last bid change

sequence of this quote

microseconds and nanoseconds part of time of the last bid or ask change

Summary is an information snapshot about the trading session including session highs, lows, etc. This record has two goals: Transmit OHLC values, and provide data for charting. OHLC is required for a daily chart, and if an exchange does not provide it, the charting services refer to the Summary event.

Before opening the bidding, the values are reset to N/A or NaN.

Show JSON schema{ "title": "Summary", "description": "Summary is an information snapshot about the trading session including\nsession highs, lows, etc. This record has two goals: Transmit OHLC\nvalues, and provide data for charting. OHLC is required for a daily chart,\nand if an exchange does not provide it, the charting services refer to the\nSummary event.\n\nBefore opening the bidding, the values are reset to N/A or NaN.", "type": "object", "properties": { "eventSymbol": { "title": "Eventsymbol", "type": "string" }, "eventTime": { "title": "Eventtime", "type": "integer" }, "dayId": { "title": "Dayid", "type": "integer" }, "dayClosePriceType": { "title": "Dayclosepricetype", "type": "string" }, "prevDayId": { "title": "Prevdayid", "type": "integer" }, "prevDayClosePriceType": { "title": "Prevdayclosepricetype", "type": "string" }, "openInterest": { "title": "Openinterest", "type": "integer" }, "dayOpenPrice": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Dayopenprice" }, "dayHighPrice": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Dayhighprice" }, "dayLowPrice": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Daylowprice" }, "dayClosePrice": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Daycloseprice" }, "prevDayClosePrice": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Prevdaycloseprice" }, "prevDayVolume": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Prevdayvolume" } }, "required": [ "eventSymbol", "eventTime", "dayId", "dayClosePriceType", "prevDayId", "prevDayClosePriceType", "openInterest" ] }

day_close_price (decimal.Decimal | None)

day_close_price_type (str)

day_high_price (decimal.Decimal | None)

day_low_price (decimal.Decimal | None)

day_open_price (decimal.Decimal | None)

prev_day_close_price (decimal.Decimal | None)

prev_day_close_price_type (str)

prev_day_volume (decimal.Decimal | None)

the last (close) price for the day

the price type of the last (close) price for the day possible values are FINAL | INDICATIVE | PRELIMINARY | REGULAR

the maximal (high) price for the day

identifier of the day that this summary represents

the minimal (low) price for the day

the first (open) price for the day

open interest of the symbol as the number of open contracts

the last (close) price for the previous day

the price type of the last (close) price for the previous day possible values are FINAL | INDICATIVE | PRELIMINARY | REGULAR

identifier of the previous day that this summary represents

total volume traded for the previous day

TimeAndSale event represents a trade or other market event with a price, like market open/close price. TimeAndSale events are intended to provide information about trades in a continuous-time slice (unlike Trade events which are supposed to provide snapshots about the most recent trade). TimeAndSale events have a unique index that can be used for later correction/cancellation processing.

Show JSON schema{ "title": "TimeAndSale", "description": "TimeAndSale event represents a trade or other market event with a price,\nlike market open/close price. TimeAndSale events are intended to provide\ninformation about trades in a continuous-time slice (unlike Trade events\nwhich are supposed to provide snapshots about the most recent trade).\nTimeAndSale events have a unique index that can be used for later\ncorrection/cancellation processing.", "type": "object", "properties": { "eventSymbol": { "title": "Eventsymbol", "type": "string" }, "eventTime": { "title": "Eventtime", "type": "integer" }, "eventFlags": { "title": "Eventflags", "type": "integer" }, "index": { "title": "Index", "type": "integer" }, "time": { "title": "Time", "type": "integer" }, "timeNanoPart": { "title": "Timenanopart", "type": "integer" }, "sequence": { "title": "Sequence", "type": "integer" }, "exchangeCode": { "title": "Exchangecode", "type": "string" }, "price": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Price" }, "size": { "title": "Size", "type": "integer" }, "bidPrice": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Bidprice" }, "askPrice": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Askprice" }, "exchangeSaleConditions": { "title": "Exchangesaleconditions", "type": "string" }, "tradeThroughExempt": { "title": "Tradethroughexempt", "type": "string" }, "aggressorSide": { "title": "Aggressorside", "type": "string" }, "spreadLeg": { "title": "Spreadleg", "type": "boolean" }, "extendedTradingHours": { "title": "Extendedtradinghours", "type": "boolean" }, "validTick": { "title": "Validtick", "type": "boolean" }, "type": { "title": "Type", "type": "string" }, "buyer": { "title": "Buyer", "type": "null" }, "seller": { "title": "Seller", "type": "null" } }, "required": [ "eventSymbol", "eventTime", "eventFlags", "index", "time", "timeNanoPart", "sequence", "exchangeCode", "price", "size", "bidPrice", "askPrice", "exchangeSaleConditions", "tradeThroughExempt", "aggressorSide", "spreadLeg", "extendedTradingHours", "validTick", "type", "buyer", "seller" ] }

ask_price (decimal.Decimal)

bid_price (decimal.Decimal)

exchange_sale_conditions (str)

extended_trading_hours (bool)

price (decimal.Decimal)

trade_through_exempt (str)

initiator of the trade

the ask price on the market when this time and sale event occured

the bid price on the market when this time and sale event occured

Undocumented; always None

exchange code of this time and sale event

sale conditions provided for this event by data feed

whether this transaction is completed during extended trading hours

unique per-symbol index of this time and sale event

price of this time and sale event

Undocumented; always None

sequence of this quote

size of this time and sale event as integer number (rounded toward zero)

whether this transaction is a part of a multi-leg order

timestamp of the original event

microseconds and nanoseconds part of time of the last bid or ask change

transaction is concluded by exempting from compliance with some rule

type of event - 0: new, 1: correction, 2: cancellation

normalized SaleCondition flag

Theo price is a snapshot of the theoretical option price computation that is periodically performed by dxPrice model-free computation. dxFeed does not send recalculations for all options at the same time, so we provide you with a formula so you can perform calculations based on values from this event.

Show JSON schema{ "title": "TheoPrice", "description": "Theo price is a snapshot of the theoretical option price computation that\nis periodically performed by dxPrice model-free computation. dxFeed does\nnot send recalculations for all options at the same time, so we provide\nyou with a formula so you can perform calculations based on values from\nthis event.", "type": "object", "properties": { "eventSymbol": { "title": "Eventsymbol", "type": "string" }, "eventTime": { "title": "Eventtime", "type": "integer" }, "eventFlags": { "title": "Eventflags", "type": "integer" }, "index": { "title": "Index", "type": "integer" }, "time": { "title": "Time", "type": "integer" }, "sequence": { "title": "Sequence", "type": "integer" }, "price": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Price" }, "underlyingPrice": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Underlyingprice" }, "delta": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Delta" }, "gamma": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Gamma" }, "dividend": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Dividend" }, "interest": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Interest" } }, "required": [ "eventSymbol", "eventTime", "eventFlags", "index", "time", "sequence", "price", "underlyingPrice", "delta", "gamma", "dividend", "interest" ] }

delta (decimal.Decimal)

dividend (decimal.Decimal)

gamma (decimal.Decimal)

interest (decimal.Decimal)

price (decimal.Decimal)

underlying_price (decimal.Decimal)

delta of the theoretical price

implied simple dividend return of the corresponding option series

gamma of the theoretical price

unique per-symbol index of this event

implied simple interest return of the corresponding option series

sequence number to distinguish events that have the same time

timestamp of this event in milliseconds

underlying price at the time of theo price computation

A Trade event provides prices and the volume of the last transaction in regular trading hours, as well as the total amount per day in the number of securities and in their value. This event does not contain information about all transactions, but only about the last transaction for a single instrument.

Show JSON schema{ "title": "Trade", "description": "A Trade event provides prices and the volume of the last transaction in\nregular trading hours, as well as the total amount per day in the number\nof securities and in their value. This event does not contain information\nabout all transactions, but only about the last transaction for a single\ninstrument.", "type": "object", "properties": { "eventSymbol": { "title": "Eventsymbol", "type": "string" }, "eventTime": { "title": "Eventtime", "type": "integer" }, "time": { "title": "Time", "type": "integer" }, "timeNanoPart": { "title": "Timenanopart", "type": "integer" }, "sequence": { "title": "Sequence", "type": "integer" }, "exchangeCode": { "title": "Exchangecode", "type": "string" }, "dayId": { "title": "Dayid", "type": "integer" }, "tickDirection": { "title": "Tickdirection", "type": "string" }, "extendedTradingHours": { "title": "Extendedtradinghours", "type": "boolean" }, "price": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Price" }, "change": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Change" }, "size": { "anyOf": [ { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Size" }, "dayVolume": { "anyOf": [ { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Dayvolume" }, "dayTurnover": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Dayturnover" } }, "required": [ "eventSymbol", "eventTime", "time", "timeNanoPart", "sequence", "exchangeCode", "dayId", "tickDirection", "extendedTradingHours", "price" ] }

change (decimal.Decimal | None)

day_turnover (decimal.Decimal | None)

day_volume (int | None)

extended_trading_hours (bool)

price (decimal.Decimal)

change of the last trade

identifier of the current trading day

total turnover traded for a day

total vlume traded for a day as integer number (rounded toward zero)

exchange code of the last trade

whether the last trade was in extended trading hours

price of the last trade

sequence of the last trade

size of the last trade as integer number (rounded toward zero)

tick direction of the last trade possible values are DOWN | UNDEFINED | UP | ZERO | ZERO_DOWN | ZERO_UP

time of the last trade

microseconds and nanoseconds time part of the last trade

Underlying event is a snapshot of computed values that are available for an option underlying symbol based on the option prices on the market. It represents the most recent information that is available about the corresponding values on the market at any given moment of time.

Show JSON schema{ "title": "Underlying", "description": "Underlying event is a snapshot of computed values that are available for\nan option underlying symbol based on the option prices on the market. It\nrepresents the most recent information that is available about the\ncorresponding values on the market at any given moment of time.", "type": "object", "properties": { "eventSymbol": { "title": "Eventsymbol", "type": "string" }, "eventTime": { "title": "Eventtime", "type": "integer" }, "eventFlags": { "title": "Eventflags", "type": "integer" }, "index": { "title": "Index", "type": "integer" }, "time": { "title": "Time", "type": "integer" }, "sequence": { "title": "Sequence", "type": "integer" }, "volatility": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Volatility" }, "frontVolatility": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Frontvolatility" }, "backVolatility": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Backvolatility" }, "callVolume": { "title": "Callvolume", "type": "integer" }, "putVolume": { "title": "Putvolume", "type": "integer" }, "optionVolume": { "title": "Optionvolume", "type": "integer" }, "putCallRatio": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Putcallratio" } }, "required": [ "eventSymbol", "eventTime", "eventFlags", "index", "time", "sequence", "volatility", "frontVolatility", "backVolatility", "callVolume", "putVolume", "optionVolume", "putCallRatio" ] }

back_volatility (decimal.Decimal)

front_volatility (decimal.Decimal)

put_call_ratio (decimal.Decimal)

volatility (decimal.Decimal)

back month implied volatility for the underlying using VIX methodology

call options traded volume for a day

front month implied volatility for the underlying using VIX methodology

unique per-symbol index of this event

options traded volume for a day

ratio of put options volume to call options volume for a day

put options traded volume for a day

sequence number of this event to distinguish events with the same time

timestamp of this event in milliseconds

30-day implied volatility for this underlying based on VIX methodology

**Examples:**

Example 1 (json):
```json
{
   "title": "Event",
   "description": "Base class for dxfeed events received from the data streamer.",
   "type": "object",
   "properties": {
      "eventSymbol": {
         "title": "Eventsymbol",
         "type": "string"
      },
      "eventTime": {
         "title": "Eventtime",
         "type": "integer"
      }
   },
   "required": [
      "eventSymbol",
      "eventTime"
   ]
}
```

Example 2 (json):
```json
{
   "title": "IndexedEvent",
   "description": "A dxfeed `IndexedEvent` with flags computed bitwise.\nFor info see `here <https://docs.dxfeed.com/dxfeed/api/com/dxfeed/event/IndexedEvent.html>`_.",
   "type": "object",
   "properties": {
      "eventSymbol": {
         "title": "Eventsymbol",
         "type": "string"
      },
      "eventTime": {
         "title": "Eventtime",
         "type": "integer"
      },
      "eventFlags": {
         "title": "Eventflags",
         "type": "integer"
      }
   },
   "required": [
      "eventSymbol",
      "eventTime",
      "eventFlags"
   ]
}
```

Example 3 (json):
```json
{
   "title": "Candle",
   "description": "A Candle event with open, high, low, close prices and other information\nfor a specific period. Candles are build with a specified period using a\nspecified price type with data taken from a specified exchange.",
   "type": "object",
   "properties": {
      "eventSymbol": {
         "title": "Eventsymbol",
         "type": "string"
      },
      "eventTime": {
         "title": "Eventtime",
         "type": "integer"
      },
      "eventFlags": {
         "title": "Eventflags",
         "type": "integer"
      },
      "index": {
         "title": "Index",
         "type": "integer"
      },
      "time": {
         "title": "Time",
         "type": "integer"
      },
      "sequence": {
         "title": "Sequence",
         "type": "integer"
      },
      "count": {
         "title": "Count",
         "type": "integer"
      },
      "volume": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Volume"
      },
      "vwap": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Vwap"
      },
      "bidVolume": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Bidvolume"
      },
      "askVolume": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Askvolume"
      },
      "impVolatility": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Impvolatility"
      },
      "openInterest": {
         "anyOf": [
            {
               "type": "integer"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Openinterest"
      },
      "open": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Open"
      },
      "high": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "High"
      },
      "low": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Low"
      },
      "close": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Close"
      }
   },
   "required": [
      "eventSymbol",
      "eventTime",
      "eventFlags",
      "index",
      "time",
      "sequence",
      "count",
      "open",
      "high",
      "low",
      "close"
   ]
}
```

Example 4 (json):
```json
{
   "title": "Greeks",
   "description": "Greek ratios, or simply Greeks, are differential values that show how the\nprice of an option depends on other market parameters: on the price of the\nunderlying asset, its volatility, etc. Greeks are used to assess the risks\nof customer portfolios. Greeks are derivatives of the value of securities\nin different axes. If a derivative is very far from zero, then the\nportfolio has a risky sensitivity in this parameter.",
   "type": "object",
   "properties": {
      "eventSymbol": {
         "title": "Eventsymbol",
         "type": "string"
      },
      "eventTime": {
         "title": "Eventtime",
         "type": "integer"
      },
      "eventFlags": {
         "title": "Eventflags",
         "type": "integer"
      },
      "index": {
         "title": "Index",
         "type": "integer"
      },
      "time": {
         "title": "Time",
         "type": "integer"
      },
      "sequence": {
         "title": "Sequence",
         "type": "integer"
      },
      "price": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Price"
      },
      "volatility": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Volatility"
      },
      "delta": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Delta"
      },
      "gamma": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Gamma"
      },
      "theta": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Theta"
      },
      "rho": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Rho"
      },
      "vega": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Vega"
      }
   },
   "required": [
      "eventSymbol",
      "eventTime",
      "eventFlags",
      "index",
      "time",
      "sequence",
      "price",
      "volatility",
      "delta",
      "gamma",
      "theta",
      "rho",
      "vega"
   ]
}
```

---

## tastytrade.instruments - tastytrade 11.1.0 documentation

**URL:** https://tastyworks-api.readthedocs.io/en/latest/api/instruments.html

**Contents:**
- tastytrade.instruments¶

Bases: TradeableTastytradeData

Dataclass that represents a Tastytrade cryptocurrency object. Contains information about the cryptocurrency and methods to populate that data using cryptocurrency symbol(s).

Show JSON schema{ "title": "Cryptocurrency", "description": "Dataclass that represents a Tastytrade cryptocurrency object. Contains\ninformation about the cryptocurrency and methods to populate that data\nusing cryptocurrency symbol(s).", "type": "object", "properties": { "instrument-type": { "$ref": "#/$defs/InstrumentType" }, "symbol": { "title": "Symbol", "type": "string" }, "id": { "title": "Id", "type": "integer" }, "short-description": { "title": "Short-Description", "type": "string" }, "description": { "title": "Description", "type": "string" }, "is-closing-only": { "title": "Is-Closing-Only", "type": "boolean" }, "active": { "title": "Active", "type": "boolean" }, "tick-size": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Tick-Size" }, "destination-venue-symbols": { "items": { "$ref": "#/$defs/DestinationVenueSymbol" }, "title": "Destination-Venue-Symbols", "type": "array" }, "streamer-symbol": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Streamer-Symbol" } }, "$defs": { "DestinationVenueSymbol": { "description": "Dataclass representing a specific destination venue symbol for a\ncryptocurrency.", "properties": { "id": { "title": "Id", "type": "integer" }, "symbol": { "title": "Symbol", "type": "string" }, "destination-venue": { "title": "Destination-Venue", "type": "string" }, "routable": { "title": "Routable", "type": "boolean" }, "max-quantity-precision": { "anyOf": [ { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Max-Quantity-Precision" }, "max-price-precision": { "anyOf": [ { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Max-Price-Precision" } }, "required": [ "id", "symbol", "destination-venue", "routable" ], "title": "DestinationVenueSymbol", "type": "object" }, "InstrumentType": { "description": "This is an :class:`~enum.Enum` that contains the valid types of instruments\nand their representation in the API.", "enum": [ "Bond", "Cryptocurrency", "Currency Pair", "Equity", "Equity Offering", "Equity Option", "Fixed Income Security", "Future", "Future Option", "Index", "Liquidity Pool", "Unknown", "Warrant" ], "title": "InstrumentType", "type": "string" } }, "required": [ "instrument-type", "symbol", "id", "short-description", "description", "is-closing-only", "active", "tick-size", "destination-venue-symbols" ] }

destination_venue_symbols (list[tastytrade.instruments.DestinationVenueSymbol])

is_closing_only (bool)

short_description (str)

streamer_symbol (str | None)

tick_size (decimal.Decimal)

Returns a list of cryptocurrency objects from the given symbols, or a single cryptocurrency if a list is not provided.

the session to use for the request.

the symbol(s) to get the cryptocurrencies for.

Returns a list of cryptocurrency objects from the given symbols, or a single cryptocurrency if a list is not provided.

the session to use for the request.

the symbol(s) to get the cryptocurrencies for.

Bases: TastytradeData

Dataclass representing the deliverable for an option.

Show JSON schema{ "title": "Deliverable", "description": "Dataclass representing the deliverable for an option.", "type": "object", "properties": { "id": { "title": "Id", "type": "integer" }, "root-symbol": { "title": "Root-Symbol", "type": "string" }, "deliverable-type": { "title": "Deliverable-Type", "type": "string" }, "description": { "title": "Description", "type": "string" }, "amount": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Amount" }, "percent": { "title": "Percent", "type": "string" }, "symbol": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Symbol" }, "instrument-type": { "anyOf": [ { "$ref": "#/$defs/InstrumentType" }, { "type": "null" } ], "default": null } }, "$defs": { "InstrumentType": { "description": "This is an :class:`~enum.Enum` that contains the valid types of instruments\nand their representation in the API.", "enum": [ "Bond", "Cryptocurrency", "Currency Pair", "Equity", "Equity Offering", "Equity Option", "Fixed Income Security", "Future", "Future Option", "Index", "Liquidity Pool", "Unknown", "Warrant" ], "title": "InstrumentType", "type": "string" } }, "required": [ "id", "root-symbol", "deliverable-type", "description", "amount", "percent" ] }

amount (decimal.Decimal)

deliverable_type (str)

instrument_type (tastytrade.order.InstrumentType | None)

Bases: TastytradeData

Dataclass representing a specific destination venue symbol for a cryptocurrency.

Show JSON schema{ "title": "DestinationVenueSymbol", "description": "Dataclass representing a specific destination venue symbol for a\ncryptocurrency.", "type": "object", "properties": { "id": { "title": "Id", "type": "integer" }, "symbol": { "title": "Symbol", "type": "string" }, "destination-venue": { "title": "Destination-Venue", "type": "string" }, "routable": { "title": "Routable", "type": "boolean" }, "max-quantity-precision": { "anyOf": [ { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Max-Quantity-Precision" }, "max-price-precision": { "anyOf": [ { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Max-Price-Precision" } }, "required": [ "id", "symbol", "destination-venue", "routable" ] }

destination_venue (str)

max_price_precision (int | None)

max_quantity_precision (int | None)

Bases: TradeableTastytradeData

Dataclass that represents a Tastytrade equity object. Contains information about the equity and methods to populate that data using equity symbol(s).

Show JSON schema{ "title": "Equity", "description": "Dataclass that represents a Tastytrade equity object. Contains information\nabout the equity and methods to populate that data using equity symbol(s).", "type": "object", "properties": { "instrument-type": { "$ref": "#/$defs/InstrumentType" }, "symbol": { "title": "Symbol", "type": "string" }, "id": { "title": "Id", "type": "integer" }, "is-index": { "title": "Is-Index", "type": "boolean" }, "description": { "title": "Description", "type": "string" }, "lendability": { "title": "Lendability", "type": "string" }, "market-time-instrument-collection": { "title": "Market-Time-Instrument-Collection", "type": "string" }, "is-closing-only": { "title": "Is-Closing-Only", "type": "boolean" }, "is-options-closing-only": { "title": "Is-Options-Closing-Only", "type": "boolean" }, "active": { "title": "Active", "type": "boolean" }, "is-illiquid": { "title": "Is-Illiquid", "type": "boolean" }, "is-etf": { "title": "Is-Etf", "type": "boolean" }, "streamer-symbol": { "title": "Streamer-Symbol", "type": "string" }, "borrow-rate": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Borrow-Rate" }, "cusip": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Cusip" }, "short-description": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Short-Description" }, "halted-at": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "Halted-At" }, "stops-trading-at": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "Stops-Trading-At" }, "is-fractional-quantity-eligible": { "anyOf": [ { "type": "boolean" }, { "type": "null" } ], "default": null, "title": "Is-Fractional-Quantity-Eligible" }, "tick-sizes": { "anyOf": [ { "items": { "$ref": "#/$defs/TickSize" }, "type": "array" }, { "type": "null" } ], "default": null, "title": "Tick-Sizes" }, "listed-market": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Listed-Market" }, "option-tick-sizes": { "anyOf": [ { "items": { "$ref": "#/$defs/TickSize" }, "type": "array" }, { "type": "null" } ], "default": null, "title": "Option-Tick-Sizes" } }, "$defs": { "InstrumentType": { "description": "This is an :class:`~enum.Enum` that contains the valid types of instruments\nand their representation in the API.", "enum": [ "Bond", "Cryptocurrency", "Currency Pair", "Equity", "Equity Offering", "Equity Option", "Fixed Income Security", "Future", "Future Option", "Index", "Liquidity Pool", "Unknown", "Warrant" ], "title": "InstrumentType", "type": "string" }, "TickSize": { "description": "Dataclass representing the tick size for an instrument.", "properties": { "value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Value" }, "threshold": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Threshold" }, "symbol": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Symbol" } }, "required": [ "value" ], "title": "TickSize", "type": "object" } }, "required": [ "instrument-type", "symbol", "id", "is-index", "description", "lendability", "market-time-instrument-collection", "is-closing-only", "is-options-closing-only", "active", "is-illiquid", "is-etf", "streamer-symbol" ] }

borrow_rate (decimal.Decimal | None)

halted_at (datetime.datetime | None)

is_closing_only (bool)

is_fractional_quantity_eligible (bool | None)

is_options_closing_only (bool)

listed_market (str | None)

market_time_instrument_collection (str)

option_tick_sizes (list[tastytrade.instruments.TickSize] | None)

short_description (str | None)

stops_trading_at (datetime.datetime | None)

streamer_symbol (str)

tick_sizes (list[tastytrade.instruments.TickSize] | None)

Returns a list of Equity objects from the given symbols, or a single Equity object if a list is not provided.

the session to use for the request.

the symbol(s) to get the equities for.

the number of options to get per page.

provide a specific page to get; if None, get all pages

the lendability of the equities; e.g. ‘Easy To Borrow’, ‘Locate Required’, ‘Preborrow’

whether the equities are indexes.

whether the equities are ETFs.

Returns a list of actively traded Equity objects.

the session to use for the request.

the number of equities to get per page.

provide a specific page to get; if None, get all pages

the lendability of the equities; e.g. ‘Easy To Borrow’, ‘Locate Required’, ‘Preborrow’

Returns a list of Equity objects from the given symbols, or a single Equity object if a list is not provided.

the session to use for the request.

the symbol(s) to get the equities for.

the number of options to get per page.

provide a specific page to get; if None, get all pages

the lendability of the equities; e.g. ‘Easy To Borrow’, ‘Locate Required’, ‘Preborrow’

whether the equities are indexes.

whether the equities are ETFs.

Returns a list of actively traded Equity objects.

the session to use for the request.

the number of equities to get per page.

provide a specific page to get; if None, get all pages

the lendability of the equities; e.g. ‘Easy To Borrow’, ‘Locate Required’, ‘Preborrow’

Bases: TradeableTastytradeData

Dataclass that represents a Tastytrade future object. Contains information about the future and methods to fetch futures for symbol(s).

Show JSON schema{ "title": "Future", "description": "Dataclass that represents a Tastytrade future object. Contains information\nabout the future and methods to fetch futures for symbol(s).", "type": "object", "properties": { "instrument-type": { "$ref": "#/$defs/InstrumentType", "default": "Future" }, "symbol": { "title": "Symbol", "type": "string" }, "product-code": { "title": "Product-Code", "type": "string" }, "tick-size": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Tick-Size" }, "notional-multiplier": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Notional-Multiplier" }, "display-factor": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Display-Factor" }, "last-trade-date": { "format": "date", "title": "Last-Trade-Date", "type": "string" }, "expiration-date": { "format": "date", "title": "Expiration-Date", "type": "string" }, "active": { "title": "Active", "type": "boolean" }, "active-month": { "title": "Active-Month", "type": "boolean" }, "next-active-month": { "title": "Next-Active-Month", "type": "boolean" }, "is-closing-only": { "title": "Is-Closing-Only", "type": "boolean" }, "stops-trading-at": { "format": "date-time", "title": "Stops-Trading-At", "type": "string" }, "expires-at": { "format": "date-time", "title": "Expires-At", "type": "string" }, "product-group": { "title": "Product-Group", "type": "string" }, "exchange": { "title": "Exchange", "type": "string" }, "streamer-exchange-code": { "title": "Streamer-Exchange-Code", "type": "string" }, "back-month-first-calendar-symbol": { "title": "Back-Month-First-Calendar-Symbol", "type": "boolean" }, "streamer-symbol": { "default": "", "title": "Streamer-Symbol", "type": "string" }, "closing-only-date": { "anyOf": [ { "format": "date", "type": "string" }, { "type": "null" } ], "default": null, "title": "Closing-Only-Date" }, "is-tradeable": { "anyOf": [ { "type": "boolean" }, { "type": "null" } ], "default": null, "title": "Is-Tradeable" }, "future-product": { "anyOf": [ { "$ref": "#/$defs/FutureProduct" }, { "type": "null" } ], "default": null }, "contract-size": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Contract-Size" }, "main-fraction": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Main-Fraction" }, "sub-fraction": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Sub-Fraction" }, "first-notice-date": { "anyOf": [ { "format": "date", "type": "string" }, { "type": "null" } ], "default": null, "title": "First-Notice-Date" }, "roll-target-symbol": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Roll-Target-Symbol" }, "true-underlying-symbol": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "True-Underlying-Symbol" }, "future-etf-equivalent": { "anyOf": [ { "$ref": "#/$defs/FutureEtfEquivalent" }, { "type": "null" } ], "default": null }, "tick-sizes": { "anyOf": [ { "items": { "$ref": "#/$defs/TickSize" }, "type": "array" }, { "type": "null" } ], "default": null, "title": "Tick-Sizes" }, "option-tick-sizes": { "anyOf": [ { "items": { "$ref": "#/$defs/TickSize" }, "type": "array" }, { "type": "null" } ], "default": null, "title": "Option-Tick-Sizes" }, "spread-tick-sizes": { "anyOf": [ { "items": { "$ref": "#/$defs/TickSize" }, "type": "array" }, { "type": "null" } ], "default": null, "title": "Spread-Tick-Sizes" } }, "$defs": { "FutureEtfEquivalent": { "description": "Dataclass that represents the ETF equivalent for a future (aka, the number\nof shares of the ETF that are equivalent to one future, leverage-wise).", "properties": { "symbol": { "title": "Symbol", "type": "string" }, "share-quantity": { "title": "Share-Quantity", "type": "integer" } }, "required": [ "symbol", "share-quantity" ], "title": "FutureEtfEquivalent", "type": "object" }, "FutureMonthCode": { "description": "This is an :class:`~enum.Enum` that contains the valid month codes for\nfutures.\n\nThis is really here for reference, as the API barely uses these codes.", "enum": [ "F", "G", "H", "J", "K", "M", "N", "Q", "U", "V", "X", "Z" ], "title": "FutureMonthCode", "type": "string" }, "FutureOptionProduct": { "description": "Dataclass that represents a Tastytrade future option product object.\nContains information about the future option product (deliverable for\nthe future option).", "properties": { "root-symbol": { "title": "Root-Symbol", "type": "string" }, "cash-settled": { "title": "Cash-Settled", "type": "boolean" }, "code": { "title": "Code", "type": "string" }, "display-factor": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Display-Factor" }, "exchange": { "title": "Exchange", "type": "string" }, "product-type": { "title": "Product-Type", "type": "string" }, "expiration-type": { "title": "Expiration-Type", "type": "string" }, "settlement-delay-days": { "title": "Settlement-Delay-Days", "type": "integer" }, "market-sector": { "title": "Market-Sector", "type": "string" }, "clearing-code": { "title": "Clearing-Code", "type": "string" }, "clearing-exchange-code": { "title": "Clearing-Exchange-Code", "type": "string" }, "clearing-price-multiplier": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Clearing-Price-Multiplier" }, "is-rollover": { "title": "Is-Rollover", "type": "boolean" }, "future-product": { "anyOf": [ { "$ref": "#/$defs/FutureProduct" }, { "type": "null" } ], "default": null }, "product-subtype": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Product-Subtype" }, "legacy-code": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Legacy-Code" }, "clearport-code": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Clearport-Code" } }, "required": [ "root-symbol", "cash-settled", "code", "display-factor", "exchange", "product-type", "expiration-type", "settlement-delay-days", "market-sector", "clearing-code", "clearing-exchange-code", "clearing-price-multiplier", "is-rollover" ], "title": "FutureOptionProduct", "type": "object" }, "FutureProduct": { "description": "Dataclass that represents a Tastytrade future product object. Contains\ninformation about the future product and a method to fetch one for a\nsymbol.\n\nUseful for fetching general information about a family of futures, without\nknowing the specific expirations or symbols.", "properties": { "root-symbol": { "title": "Root-Symbol", "type": "string" }, "code": { "title": "Code", "type": "string" }, "description": { "title": "Description", "type": "string" }, "exchange": { "title": "Exchange", "type": "string" }, "product-type": { "title": "Product-Type", "type": "string" }, "listed-months": { "items": { "$ref": "#/$defs/FutureMonthCode" }, "title": "Listed-Months", "type": "array" }, "active-months": { "items": { "$ref": "#/$defs/FutureMonthCode" }, "title": "Active-Months", "type": "array" }, "notional-multiplier": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Notional-Multiplier" }, "tick-size": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Tick-Size" }, "display-factor": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Display-Factor" }, "streamer-exchange-code": { "title": "Streamer-Exchange-Code", "type": "string" }, "small-notional": { "title": "Small-Notional", "type": "boolean" }, "back-month-first-calendar-symbol": { "title": "Back-Month-First-Calendar-Symbol", "type": "boolean" }, "first-notice": { "title": "First-Notice", "type": "boolean" }, "cash-settled": { "title": "Cash-Settled", "type": "boolean" }, "market-sector": { "title": "Market-Sector", "type": "string" }, "clearing-code": { "title": "Clearing-Code", "type": "string" }, "clearing-exchange-code": { "title": "Clearing-Exchange-Code", "type": "string" }, "roll": { "$ref": "#/$defs/Roll" }, "base-tick": { "anyOf": [ { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Base-Tick" }, "sub-tick": { "anyOf": [ { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Sub-Tick" }, "contract-limit": { "anyOf": [ { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Contract-Limit" }, "product-subtype": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Product-Subtype" }, "security-group": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Security-Group" }, "true-underlying-code": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "True-Underlying-Code" }, "clearport-code": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Clearport-Code" }, "legacy-code": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Legacy-Code" }, "legacy-exchange-code": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Legacy-Exchange-Code" }, "option-products": { "anyOf": [ { "items": { "$ref": "#/$defs/FutureOptionProduct" }, "type": "array" }, { "type": "null" } ], "default": null, "title": "Option-Products" } }, "required": [ "root-symbol", "code", "description", "exchange", "product-type", "listed-months", "active-months", "notional-multiplier", "tick-size", "display-factor", "streamer-exchange-code", "small-notional", "back-month-first-calendar-symbol", "first-notice", "cash-settled", "market-sector", "clearing-code", "clearing-exchange-code", "roll" ], "title": "FutureProduct", "type": "object" }, "InstrumentType": { "description": "This is an :class:`~enum.Enum` that contains the valid types of instruments\nand their representation in the API.", "enum": [ "Bond", "Cryptocurrency", "Currency Pair", "Equity", "Equity Offering", "Equity Option", "Fixed Income Security", "Future", "Future Option", "Index", "Liquidity Pool", "Unknown", "Warrant" ], "title": "InstrumentType", "type": "string" }, "Roll": { "description": "Dataclass representing a roll for a future.", "properties": { "name": { "title": "Name", "type": "string" }, "active-count": { "title": "Active-Count", "type": "integer" }, "cash-settled": { "title": "Cash-Settled", "type": "boolean" }, "business-days-offset": { "title": "Business-Days-Offset", "type": "integer" }, "first-notice": { "title": "First-Notice", "type": "boolean" } }, "required": [ "name", "active-count", "cash-settled", "business-days-offset", "first-notice" ], "title": "Roll", "type": "object" }, "TickSize": { "description": "Dataclass representing the tick size for an instrument.", "properties": { "value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Value" }, "threshold": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Threshold" }, "symbol": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Symbol" } }, "required": [ "value" ], "title": "TickSize", "type": "object" } }, "required": [ "symbol", "product-code", "tick-size", "notional-multiplier", "display-factor", "last-trade-date", "expiration-date", "active", "active-month", "next-active-month", "is-closing-only", "stops-trading-at", "expires-at", "product-group", "exchange", "streamer-exchange-code", "back-month-first-calendar-symbol" ] }

back_month_first_calendar_symbol (bool)

closing_only_date (datetime.date | None)

contract_size (decimal.Decimal | None)

display_factor (decimal.Decimal)

expiration_date (datetime.date)

expires_at (datetime.datetime)

first_notice_date (datetime.date | None)

future_etf_equivalent (tastytrade.instruments.FutureEtfEquivalent | None)

future_product (tastytrade.instruments.FutureProduct | None)

instrument_type (tastytrade.order.InstrumentType)

is_closing_only (bool)

is_tradeable (bool | None)

last_trade_date (datetime.date)

main_fraction (decimal.Decimal | None)

next_active_month (bool)

notional_multiplier (decimal.Decimal)

option_tick_sizes (list[tastytrade.instruments.TickSize] | None)

roll_target_symbol (str | None)

spread_tick_sizes (list[tastytrade.instruments.TickSize] | None)

stops_trading_at (datetime.datetime)

streamer_exchange_code (str)

streamer_symbol (str)

sub_fraction (decimal.Decimal | None)

tick_size (decimal.Decimal)

tick_sizes (list[tastytrade.instruments.TickSize] | None)

true_underlying_symbol (str | None)

Returns a list of Future objects from the given symbols or product codes.

the session to use for the request.

symbol(s) of the futures, e.g. ‘ESZ9’, ‘/ESZ9’.

the product codes of the futures, e.g. ‘ES’, ‘6A’. Ignored if symbols are provided.

the number of options to get per page.

provide a specific page to get; if None, get all pages

Returns a list of Future objects from the given symbols or product codes.

the session to use for the request.

symbol(s) of the futures, e.g. ‘ESZ9’, ‘/ESZ9’.

the product codes of the futures, e.g. ‘ES’, ‘6A’. Ignored if symbols are provided.

the number of options to get per page.

provide a specific page to get; if None, get all pages

Bases: TastytradeData

Dataclass that represents the ETF equivalent for a future (aka, the number of shares of the ETF that are equivalent to one future, leverage-wise).

Show JSON schema{ "title": "FutureEtfEquivalent", "description": "Dataclass that represents the ETF equivalent for a future (aka, the number\nof shares of the ETF that are equivalent to one future, leverage-wise).", "type": "object", "properties": { "symbol": { "title": "Symbol", "type": "string" }, "share-quantity": { "title": "Share-Quantity", "type": "integer" } }, "required": [ "symbol", "share-quantity" ] }

This is an Enum that contains the valid month codes for futures.

This is really here for reference, as the API barely uses these codes.

Valid values are as follows:

Bases: TradeableTastytradeData

Dataclass that represents a Tastytrade future option object. Contains information about the future option, and methods to get future options.

Show JSON schema{ "title": "FutureOption", "description": "Dataclass that represents a Tastytrade future option object. Contains\ninformation about the future option, and methods to get future options.", "type": "object", "properties": { "instrument-type": { "$ref": "#/$defs/InstrumentType", "default": "Future Option" }, "symbol": { "title": "Symbol", "type": "string" }, "underlying-symbol": { "title": "Underlying-Symbol", "type": "string" }, "product-code": { "title": "Product-Code", "type": "string" }, "expiration-date": { "format": "date", "title": "Expiration-Date", "type": "string" }, "root-symbol": { "title": "Root-Symbol", "type": "string" }, "option-root-symbol": { "title": "Option-Root-Symbol", "type": "string" }, "strike-price": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Strike-Price" }, "exchange": { "title": "Exchange", "type": "string" }, "streamer-symbol": { "title": "Streamer-Symbol", "type": "string" }, "option-type": { "$ref": "#/$defs/OptionType" }, "exercise-style": { "title": "Exercise-Style", "type": "string" }, "is-vanilla": { "title": "Is-Vanilla", "type": "boolean" }, "is-primary-deliverable": { "title": "Is-Primary-Deliverable", "type": "boolean" }, "future-price-ratio": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Future-Price-Ratio" }, "multiplier": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Multiplier" }, "underlying-count": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Underlying-Count" }, "is-confirmed": { "title": "Is-Confirmed", "type": "boolean" }, "notional-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Notional-Value" }, "display-factor": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Display-Factor" }, "settlement-type": { "title": "Settlement-Type", "type": "string" }, "strike-factor": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Strike-Factor" }, "maturity-date": { "format": "date", "title": "Maturity-Date", "type": "string" }, "is-exercisable-weekly": { "title": "Is-Exercisable-Weekly", "type": "boolean" }, "last-trade-time": { "title": "Last-Trade-Time", "type": "string" }, "days-to-expiration": { "title": "Days-To-Expiration", "type": "integer" }, "is-closing-only": { "title": "Is-Closing-Only", "type": "boolean" }, "active": { "title": "Active", "type": "boolean" }, "stops-trading-at": { "format": "date-time", "title": "Stops-Trading-At", "type": "string" }, "expires-at": { "format": "date-time", "title": "Expires-At", "type": "string" }, "exchange-symbol": { "title": "Exchange-Symbol", "type": "string" }, "security-exchange": { "title": "Security-Exchange", "type": "string" }, "sx-id": { "title": "Sx-Id", "type": "string" }, "future-option-product": { "anyOf": [ { "$ref": "#/$defs/FutureOptionProduct" }, { "type": "null" } ], "default": null } }, "$defs": { "FutureMonthCode": { "description": "This is an :class:`~enum.Enum` that contains the valid month codes for\nfutures.\n\nThis is really here for reference, as the API barely uses these codes.", "enum": [ "F", "G", "H", "J", "K", "M", "N", "Q", "U", "V", "X", "Z" ], "title": "FutureMonthCode", "type": "string" }, "FutureOptionProduct": { "description": "Dataclass that represents a Tastytrade future option product object.\nContains information about the future option product (deliverable for\nthe future option).", "properties": { "root-symbol": { "title": "Root-Symbol", "type": "string" }, "cash-settled": { "title": "Cash-Settled", "type": "boolean" }, "code": { "title": "Code", "type": "string" }, "display-factor": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Display-Factor" }, "exchange": { "title": "Exchange", "type": "string" }, "product-type": { "title": "Product-Type", "type": "string" }, "expiration-type": { "title": "Expiration-Type", "type": "string" }, "settlement-delay-days": { "title": "Settlement-Delay-Days", "type": "integer" }, "market-sector": { "title": "Market-Sector", "type": "string" }, "clearing-code": { "title": "Clearing-Code", "type": "string" }, "clearing-exchange-code": { "title": "Clearing-Exchange-Code", "type": "string" }, "clearing-price-multiplier": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Clearing-Price-Multiplier" }, "is-rollover": { "title": "Is-Rollover", "type": "boolean" }, "future-product": { "anyOf": [ { "$ref": "#/$defs/FutureProduct" }, { "type": "null" } ], "default": null }, "product-subtype": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Product-Subtype" }, "legacy-code": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Legacy-Code" }, "clearport-code": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Clearport-Code" } }, "required": [ "root-symbol", "cash-settled", "code", "display-factor", "exchange", "product-type", "expiration-type", "settlement-delay-days", "market-sector", "clearing-code", "clearing-exchange-code", "clearing-price-multiplier", "is-rollover" ], "title": "FutureOptionProduct", "type": "object" }, "FutureProduct": { "description": "Dataclass that represents a Tastytrade future product object. Contains\ninformation about the future product and a method to fetch one for a\nsymbol.\n\nUseful for fetching general information about a family of futures, without\nknowing the specific expirations or symbols.", "properties": { "root-symbol": { "title": "Root-Symbol", "type": "string" }, "code": { "title": "Code", "type": "string" }, "description": { "title": "Description", "type": "string" }, "exchange": { "title": "Exchange", "type": "string" }, "product-type": { "title": "Product-Type", "type": "string" }, "listed-months": { "items": { "$ref": "#/$defs/FutureMonthCode" }, "title": "Listed-Months", "type": "array" }, "active-months": { "items": { "$ref": "#/$defs/FutureMonthCode" }, "title": "Active-Months", "type": "array" }, "notional-multiplier": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Notional-Multiplier" }, "tick-size": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Tick-Size" }, "display-factor": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Display-Factor" }, "streamer-exchange-code": { "title": "Streamer-Exchange-Code", "type": "string" }, "small-notional": { "title": "Small-Notional", "type": "boolean" }, "back-month-first-calendar-symbol": { "title": "Back-Month-First-Calendar-Symbol", "type": "boolean" }, "first-notice": { "title": "First-Notice", "type": "boolean" }, "cash-settled": { "title": "Cash-Settled", "type": "boolean" }, "market-sector": { "title": "Market-Sector", "type": "string" }, "clearing-code": { "title": "Clearing-Code", "type": "string" }, "clearing-exchange-code": { "title": "Clearing-Exchange-Code", "type": "string" }, "roll": { "$ref": "#/$defs/Roll" }, "base-tick": { "anyOf": [ { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Base-Tick" }, "sub-tick": { "anyOf": [ { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Sub-Tick" }, "contract-limit": { "anyOf": [ { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Contract-Limit" }, "product-subtype": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Product-Subtype" }, "security-group": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Security-Group" }, "true-underlying-code": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "True-Underlying-Code" }, "clearport-code": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Clearport-Code" }, "legacy-code": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Legacy-Code" }, "legacy-exchange-code": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Legacy-Exchange-Code" }, "option-products": { "anyOf": [ { "items": { "$ref": "#/$defs/FutureOptionProduct" }, "type": "array" }, { "type": "null" } ], "default": null, "title": "Option-Products" } }, "required": [ "root-symbol", "code", "description", "exchange", "product-type", "listed-months", "active-months", "notional-multiplier", "tick-size", "display-factor", "streamer-exchange-code", "small-notional", "back-month-first-calendar-symbol", "first-notice", "cash-settled", "market-sector", "clearing-code", "clearing-exchange-code", "roll" ], "title": "FutureProduct", "type": "object" }, "InstrumentType": { "description": "This is an :class:`~enum.Enum` that contains the valid types of instruments\nand their representation in the API.", "enum": [ "Bond", "Cryptocurrency", "Currency Pair", "Equity", "Equity Offering", "Equity Option", "Fixed Income Security", "Future", "Future Option", "Index", "Liquidity Pool", "Unknown", "Warrant" ], "title": "InstrumentType", "type": "string" }, "OptionType": { "description": "This is an :class:`~enum.Enum` that contains the valid types of options\nand their abbreviations in the API.", "enum": [ "C", "P" ], "title": "OptionType", "type": "string" }, "Roll": { "description": "Dataclass representing a roll for a future.", "properties": { "name": { "title": "Name", "type": "string" }, "active-count": { "title": "Active-Count", "type": "integer" }, "cash-settled": { "title": "Cash-Settled", "type": "boolean" }, "business-days-offset": { "title": "Business-Days-Offset", "type": "integer" }, "first-notice": { "title": "First-Notice", "type": "boolean" } }, "required": [ "name", "active-count", "cash-settled", "business-days-offset", "first-notice" ], "title": "Roll", "type": "object" } }, "required": [ "symbol", "underlying-symbol", "product-code", "expiration-date", "root-symbol", "option-root-symbol", "strike-price", "exchange", "streamer-symbol", "option-type", "exercise-style", "is-vanilla", "is-primary-deliverable", "future-price-ratio", "multiplier", "underlying-count", "is-confirmed", "notional-value", "display-factor", "settlement-type", "strike-factor", "maturity-date", "is-exercisable-weekly", "last-trade-time", "days-to-expiration", "is-closing-only", "active", "stops-trading-at", "expires-at", "exchange-symbol", "security-exchange", "sx-id" ] }

days_to_expiration (int)

display_factor (decimal.Decimal)

exchange_symbol (str)

expiration_date (datetime.date)

expires_at (datetime.datetime)

future_option_product (tastytrade.instruments.FutureOptionProduct | None)

future_price_ratio (decimal.Decimal)

instrument_type (tastytrade.order.InstrumentType)

is_closing_only (bool)

is_exercisable_weekly (bool)

is_primary_deliverable (bool)

last_trade_time (str)

maturity_date (datetime.date)

multiplier (decimal.Decimal)

notional_value (decimal.Decimal)

option_root_symbol (str)

option_type (tastytrade.instruments.OptionType)

security_exchange (str)

settlement_type (str)

stops_trading_at (datetime.datetime)

streamer_symbol (str)

strike_factor (decimal.Decimal)

strike_price (decimal.Decimal)

underlying_count (decimal.Decimal)

underlying_symbol (str)

parse_date_with_utc » maturity_date

Returns a list of FutureOption objects from the given symbols.

NOTE: many of the parameters are bugged, maybe Tasty will fix?

the session to use for the request.

the Tastytrade symbol(s) to filter by.

the root symbol to get the future options for, e.g. ‘EW3’, ‘SO’

the expiration date for the future options.

the option type to filter by.

the strike price to filter by.

the number of options to get per page.

provide a specific page to get; if None, get all pages

Returns a list of FutureOption objects from the given symbols.

NOTE: many of the parameters are bugged, maybe Tasty will fix?

the session to use for the request.

the Tastytrade symbol(s) to filter by.

the root symbol to get the future options for, e.g. ‘EW3’, ‘SO’

the expiration date for the future options.

the option type to filter by.

the strike price to filter by.

the number of options to get per page.

provide a specific page to get; if None, get all pages

Bases: TastytradeData

Dataclass that represents a Tastytrade future option product object. Contains information about the future option product (deliverable for the future option).

Show JSON schema{ "$defs": { "FutureMonthCode": { "description": "This is an :class:`~enum.Enum` that contains the valid month codes for\nfutures.\n\nThis is really here for reference, as the API barely uses these codes.", "enum": [ "F", "G", "H", "J", "K", "M", "N", "Q", "U", "V", "X", "Z" ], "title": "FutureMonthCode", "type": "string" }, "FutureOptionProduct": { "description": "Dataclass that represents a Tastytrade future option product object.\nContains information about the future option product (deliverable for\nthe future option).", "properties": { "root-symbol": { "title": "Root-Symbol", "type": "string" }, "cash-settled": { "title": "Cash-Settled", "type": "boolean" }, "code": { "title": "Code", "type": "string" }, "display-factor": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Display-Factor" }, "exchange": { "title": "Exchange", "type": "string" }, "product-type": { "title": "Product-Type", "type": "string" }, "expiration-type": { "title": "Expiration-Type", "type": "string" }, "settlement-delay-days": { "title": "Settlement-Delay-Days", "type": "integer" }, "market-sector": { "title": "Market-Sector", "type": "string" }, "clearing-code": { "title": "Clearing-Code", "type": "string" }, "clearing-exchange-code": { "title": "Clearing-Exchange-Code", "type": "string" }, "clearing-price-multiplier": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Clearing-Price-Multiplier" }, "is-rollover": { "title": "Is-Rollover", "type": "boolean" }, "future-product": { "anyOf": [ { "$ref": "#/$defs/FutureProduct" }, { "type": "null" } ], "default": null }, "product-subtype": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Product-Subtype" }, "legacy-code": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Legacy-Code" }, "clearport-code": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Clearport-Code" } }, "required": [ "root-symbol", "cash-settled", "code", "display-factor", "exchange", "product-type", "expiration-type", "settlement-delay-days", "market-sector", "clearing-code", "clearing-exchange-code", "clearing-price-multiplier", "is-rollover" ], "title": "FutureOptionProduct", "type": "object" }, "FutureProduct": { "description": "Dataclass that represents a Tastytrade future product object. Contains\ninformation about the future product and a method to fetch one for a\nsymbol.\n\nUseful for fetching general information about a family of futures, without\nknowing the specific expirations or symbols.", "properties": { "root-symbol": { "title": "Root-Symbol", "type": "string" }, "code": { "title": "Code", "type": "string" }, "description": { "title": "Description", "type": "string" }, "exchange": { "title": "Exchange", "type": "string" }, "product-type": { "title": "Product-Type", "type": "string" }, "listed-months": { "items": { "$ref": "#/$defs/FutureMonthCode" }, "title": "Listed-Months", "type": "array" }, "active-months": { "items": { "$ref": "#/$defs/FutureMonthCode" }, "title": "Active-Months", "type": "array" }, "notional-multiplier": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Notional-Multiplier" }, "tick-size": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Tick-Size" }, "display-factor": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Display-Factor" }, "streamer-exchange-code": { "title": "Streamer-Exchange-Code", "type": "string" }, "small-notional": { "title": "Small-Notional", "type": "boolean" }, "back-month-first-calendar-symbol": { "title": "Back-Month-First-Calendar-Symbol", "type": "boolean" }, "first-notice": { "title": "First-Notice", "type": "boolean" }, "cash-settled": { "title": "Cash-Settled", "type": "boolean" }, "market-sector": { "title": "Market-Sector", "type": "string" }, "clearing-code": { "title": "Clearing-Code", "type": "string" }, "clearing-exchange-code": { "title": "Clearing-Exchange-Code", "type": "string" }, "roll": { "$ref": "#/$defs/Roll" }, "base-tick": { "anyOf": [ { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Base-Tick" }, "sub-tick": { "anyOf": [ { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Sub-Tick" }, "contract-limit": { "anyOf": [ { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Contract-Limit" }, "product-subtype": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Product-Subtype" }, "security-group": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Security-Group" }, "true-underlying-code": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "True-Underlying-Code" }, "clearport-code": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Clearport-Code" }, "legacy-code": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Legacy-Code" }, "legacy-exchange-code": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Legacy-Exchange-Code" }, "option-products": { "anyOf": [ { "items": { "$ref": "#/$defs/FutureOptionProduct" }, "type": "array" }, { "type": "null" } ], "default": null, "title": "Option-Products" } }, "required": [ "root-symbol", "code", "description", "exchange", "product-type", "listed-months", "active-months", "notional-multiplier", "tick-size", "display-factor", "streamer-exchange-code", "small-notional", "back-month-first-calendar-symbol", "first-notice", "cash-settled", "market-sector", "clearing-code", "clearing-exchange-code", "roll" ], "title": "FutureProduct", "type": "object" }, "Roll": { "description": "Dataclass representing a roll for a future.", "properties": { "name": { "title": "Name", "type": "string" }, "active-count": { "title": "Active-Count", "type": "integer" }, "cash-settled": { "title": "Cash-Settled", "type": "boolean" }, "business-days-offset": { "title": "Business-Days-Offset", "type": "integer" }, "first-notice": { "title": "First-Notice", "type": "boolean" } }, "required": [ "name", "active-count", "cash-settled", "business-days-offset", "first-notice" ], "title": "Roll", "type": "object" } }, "$ref": "#/$defs/FutureOptionProduct" }

clearing_exchange_code (str)

clearing_price_multiplier (decimal.Decimal)

clearport_code (str | None)

display_factor (decimal.Decimal)

expiration_type (str)

future_product (tastytrade.instruments.FutureProduct | None)

legacy_code (str | None)

product_subtype (str | None)

settlement_delay_days (int)

Returns a list of FutureOptionProduct objects available, or a single FutureOptionProduct object if a root symbol is provided.

the session to use for the request.

the root symbol of the future option

the exchange to get the product from

Returns a list of FutureOptionProduct objects available, or a single FutureOptionProduct object if a root symbol is provided.

the session to use for the request.

the root symbol of the future option

the exchange to get the product from

Bases: TastytradeData

Dataclass that represents a Tastytrade future product object. Contains information about the future product and a method to fetch one for a symbol.

Useful for fetching general information about a family of futures, without knowing the specific expirations or symbols.

Show JSON schema{ "$defs": { "FutureMonthCode": { "description": "This is an :class:`~enum.Enum` that contains the valid month codes for\nfutures.\n\nThis is really here for reference, as the API barely uses these codes.", "enum": [ "F", "G", "H", "J", "K", "M", "N", "Q", "U", "V", "X", "Z" ], "title": "FutureMonthCode", "type": "string" }, "FutureOptionProduct": { "description": "Dataclass that represents a Tastytrade future option product object.\nContains information about the future option product (deliverable for\nthe future option).", "properties": { "root-symbol": { "title": "Root-Symbol", "type": "string" }, "cash-settled": { "title": "Cash-Settled", "type": "boolean" }, "code": { "title": "Code", "type": "string" }, "display-factor": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Display-Factor" }, "exchange": { "title": "Exchange", "type": "string" }, "product-type": { "title": "Product-Type", "type": "string" }, "expiration-type": { "title": "Expiration-Type", "type": "string" }, "settlement-delay-days": { "title": "Settlement-Delay-Days", "type": "integer" }, "market-sector": { "title": "Market-Sector", "type": "string" }, "clearing-code": { "title": "Clearing-Code", "type": "string" }, "clearing-exchange-code": { "title": "Clearing-Exchange-Code", "type": "string" }, "clearing-price-multiplier": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Clearing-Price-Multiplier" }, "is-rollover": { "title": "Is-Rollover", "type": "boolean" }, "future-product": { "anyOf": [ { "$ref": "#/$defs/FutureProduct" }, { "type": "null" } ], "default": null }, "product-subtype": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Product-Subtype" }, "legacy-code": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Legacy-Code" }, "clearport-code": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Clearport-Code" } }, "required": [ "root-symbol", "cash-settled", "code", "display-factor", "exchange", "product-type", "expiration-type", "settlement-delay-days", "market-sector", "clearing-code", "clearing-exchange-code", "clearing-price-multiplier", "is-rollover" ], "title": "FutureOptionProduct", "type": "object" }, "FutureProduct": { "description": "Dataclass that represents a Tastytrade future product object. Contains\ninformation about the future product and a method to fetch one for a\nsymbol.\n\nUseful for fetching general information about a family of futures, without\nknowing the specific expirations or symbols.", "properties": { "root-symbol": { "title": "Root-Symbol", "type": "string" }, "code": { "title": "Code", "type": "string" }, "description": { "title": "Description", "type": "string" }, "exchange": { "title": "Exchange", "type": "string" }, "product-type": { "title": "Product-Type", "type": "string" }, "listed-months": { "items": { "$ref": "#/$defs/FutureMonthCode" }, "title": "Listed-Months", "type": "array" }, "active-months": { "items": { "$ref": "#/$defs/FutureMonthCode" }, "title": "Active-Months", "type": "array" }, "notional-multiplier": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Notional-Multiplier" }, "tick-size": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Tick-Size" }, "display-factor": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Display-Factor" }, "streamer-exchange-code": { "title": "Streamer-Exchange-Code", "type": "string" }, "small-notional": { "title": "Small-Notional", "type": "boolean" }, "back-month-first-calendar-symbol": { "title": "Back-Month-First-Calendar-Symbol", "type": "boolean" }, "first-notice": { "title": "First-Notice", "type": "boolean" }, "cash-settled": { "title": "Cash-Settled", "type": "boolean" }, "market-sector": { "title": "Market-Sector", "type": "string" }, "clearing-code": { "title": "Clearing-Code", "type": "string" }, "clearing-exchange-code": { "title": "Clearing-Exchange-Code", "type": "string" }, "roll": { "$ref": "#/$defs/Roll" }, "base-tick": { "anyOf": [ { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Base-Tick" }, "sub-tick": { "anyOf": [ { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Sub-Tick" }, "contract-limit": { "anyOf": [ { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Contract-Limit" }, "product-subtype": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Product-Subtype" }, "security-group": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Security-Group" }, "true-underlying-code": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "True-Underlying-Code" }, "clearport-code": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Clearport-Code" }, "legacy-code": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Legacy-Code" }, "legacy-exchange-code": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Legacy-Exchange-Code" }, "option-products": { "anyOf": [ { "items": { "$ref": "#/$defs/FutureOptionProduct" }, "type": "array" }, { "type": "null" } ], "default": null, "title": "Option-Products" } }, "required": [ "root-symbol", "code", "description", "exchange", "product-type", "listed-months", "active-months", "notional-multiplier", "tick-size", "display-factor", "streamer-exchange-code", "small-notional", "back-month-first-calendar-symbol", "first-notice", "cash-settled", "market-sector", "clearing-code", "clearing-exchange-code", "roll" ], "title": "FutureProduct", "type": "object" }, "Roll": { "description": "Dataclass representing a roll for a future.", "properties": { "name": { "title": "Name", "type": "string" }, "active-count": { "title": "Active-Count", "type": "integer" }, "cash-settled": { "title": "Cash-Settled", "type": "boolean" }, "business-days-offset": { "title": "Business-Days-Offset", "type": "integer" }, "first-notice": { "title": "First-Notice", "type": "boolean" } }, "required": [ "name", "active-count", "cash-settled", "business-days-offset", "first-notice" ], "title": "Roll", "type": "object" } }, "$ref": "#/$defs/FutureProduct" }

active_months (list[tastytrade.instruments.FutureMonthCode])

back_month_first_calendar_symbol (bool)

base_tick (int | None)

clearing_exchange_code (str)

clearport_code (str | None)

contract_limit (int | None)

display_factor (decimal.Decimal)

legacy_code (str | None)

legacy_exchange_code (str | None)

listed_months (list[tastytrade.instruments.FutureMonthCode])

notional_multiplier (decimal.Decimal)

option_products (list[FutureOptionProduct] | None)

product_subtype (str | None)

roll (tastytrade.instruments.Roll)

security_group (str | None)

small_notional (bool)

streamer_exchange_code (str)

sub_tick (int | None)

tick_size (decimal.Decimal)

true_underlying_code (str | None)

Returns a list of FutureProduct objects available, or a single FutureProduct object if a code is provided.

the session to use for the request.

the product code, e.g. ‘ES’

the exchange to fetch from: ‘CME’, ‘SMALLS’, ‘CFE’, ‘CBOED’

Returns a list of FutureProduct objects available, or a single FutureProduct object if a code is provided.

the session to use for the request.

the product code, e.g. ‘ES’

the exchange to fetch from: ‘CME’, ‘SMALLS’, ‘CFE’, ‘CBOED’

Bases: TastytradeData

Dataclass that represents a Tastytrade nested option chain object. Contains information about the option chain and a method to fetch one for a symbol.

This is cleaner than calling get_future_option_chain() but if you want to create actual FutureOption objects you’ll need to make an extra API request or two.

Show JSON schema{ "title": "NestedFutureOptionChain", "description": "Dataclass that represents a Tastytrade nested option chain object. Contains\ninformation about the option chain and a method to fetch one for a symbol.\n\nThis is cleaner than calling :meth:`get_future_option_chain` but if you\nwant to create actual :class:`FutureOption` objects you'll need to make an\nextra API request or two.", "type": "object", "properties": { "futures": { "items": { "$ref": "#/$defs/NestedFutureOptionFuture" }, "title": "Futures", "type": "array" }, "option-chains": { "items": { "$ref": "#/$defs/NestedFutureOptionSubchain" }, "title": "Option-Chains", "type": "array" } }, "$defs": { "NestedFutureOptionChainExpiration": { "description": "Dataclass representing an expiration in a nested future options chain.", "properties": { "root-symbol": { "title": "Root-Symbol", "type": "string" }, "notional-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Notional-Value" }, "underlying-symbol": { "title": "Underlying-Symbol", "type": "string" }, "strike-factor": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Strike-Factor" }, "days-to-expiration": { "title": "Days-To-Expiration", "type": "integer" }, "option-root-symbol": { "title": "Option-Root-Symbol", "type": "string" }, "expiration-date": { "format": "date", "title": "Expiration-Date", "type": "string" }, "expires-at": { "format": "date-time", "title": "Expires-At", "type": "string" }, "asset": { "title": "Asset", "type": "string" }, "expiration-type": { "title": "Expiration-Type", "type": "string" }, "display-factor": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Display-Factor" }, "option-contract-symbol": { "title": "Option-Contract-Symbol", "type": "string" }, "stops-trading-at": { "format": "date-time", "title": "Stops-Trading-At", "type": "string" }, "settlement-type": { "title": "Settlement-Type", "type": "string" }, "strikes": { "items": { "$ref": "#/$defs/Strike" }, "title": "Strikes", "type": "array" }, "tick-sizes": { "items": { "$ref": "#/$defs/TickSize" }, "title": "Tick-Sizes", "type": "array" } }, "required": [ "root-symbol", "notional-value", "underlying-symbol", "strike-factor", "days-to-expiration", "option-root-symbol", "expiration-date", "expires-at", "asset", "expiration-type", "display-factor", "option-contract-symbol", "stops-trading-at", "settlement-type", "strikes", "tick-sizes" ], "title": "NestedFutureOptionChainExpiration", "type": "object" }, "NestedFutureOptionFuture": { "description": "Dataclass representing an underlying future in a nested future options\nchain.", "properties": { "root-symbol": { "title": "Root-Symbol", "type": "string" }, "days-to-expiration": { "title": "Days-To-Expiration", "type": "integer" }, "expiration-date": { "format": "date", "title": "Expiration-Date", "type": "string" }, "expires-at": { "format": "date-time", "title": "Expires-At", "type": "string" }, "next-active-month": { "title": "Next-Active-Month", "type": "boolean" }, "symbol": { "title": "Symbol", "type": "string" }, "active-month": { "title": "Active-Month", "type": "boolean" }, "stops-trading-at": { "format": "date-time", "title": "Stops-Trading-At", "type": "string" }, "maturity-date": { "anyOf": [ { "format": "date", "type": "string" }, { "type": "null" } ], "default": null, "title": "Maturity-Date" } }, "required": [ "root-symbol", "days-to-expiration", "expiration-date", "expires-at", "next-active-month", "symbol", "active-month", "stops-trading-at" ], "title": "NestedFutureOptionFuture", "type": "object" }, "NestedFutureOptionSubchain": { "description": "Dataclass that represents a Tastytrade nested future option chain for a\nspecific futures underlying symbol.", "properties": { "underlying-symbol": { "title": "Underlying-Symbol", "type": "string" }, "root-symbol": { "title": "Root-Symbol", "type": "string" }, "exercise-style": { "title": "Exercise-Style", "type": "string" }, "expirations": { "items": { "$ref": "#/$defs/NestedFutureOptionChainExpiration" }, "title": "Expirations", "type": "array" } }, "required": [ "underlying-symbol", "root-symbol", "exercise-style", "expirations" ], "title": "NestedFutureOptionSubchain", "type": "object" }, "Strike": { "description": "Dataclass representing a specific strike in an options chain, containing\nthe symbols for the call and put options.", "properties": { "strike-price": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Strike-Price" }, "call": { "title": "Call", "type": "string" }, "put": { "title": "Put", "type": "string" }, "call-streamer-symbol": { "title": "Call-Streamer-Symbol", "type": "string" }, "put-streamer-symbol": { "title": "Put-Streamer-Symbol", "type": "string" } }, "required": [ "strike-price", "call", "put", "call-streamer-symbol", "put-streamer-symbol" ], "title": "Strike", "type": "object" }, "TickSize": { "description": "Dataclass representing the tick size for an instrument.", "properties": { "value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Value" }, "threshold": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Threshold" }, "symbol": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Symbol" } }, "required": [ "value" ], "title": "TickSize", "type": "object" } }, "required": [ "futures", "option-chains" ] }

futures (list[tastytrade.instruments.NestedFutureOptionFuture])

option_chains (list[tastytrade.instruments.NestedFutureOptionSubchain])

Gets the futures option chain for the given symbol in nested format.

the session to use for the request.

the symbol to get the option chain for.

Gets the futures option chain for the given symbol in nested format.

the session to use for the request.

the symbol to get the option chain for.

Bases: TastytradeData

Dataclass representing an expiration in a nested future options chain.

Show JSON schema{ "title": "NestedFutureOptionChainExpiration", "description": "Dataclass representing an expiration in a nested future options chain.", "type": "object", "properties": { "root-symbol": { "title": "Root-Symbol", "type": "string" }, "notional-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Notional-Value" }, "underlying-symbol": { "title": "Underlying-Symbol", "type": "string" }, "strike-factor": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Strike-Factor" }, "days-to-expiration": { "title": "Days-To-Expiration", "type": "integer" }, "option-root-symbol": { "title": "Option-Root-Symbol", "type": "string" }, "expiration-date": { "format": "date", "title": "Expiration-Date", "type": "string" }, "expires-at": { "format": "date-time", "title": "Expires-At", "type": "string" }, "asset": { "title": "Asset", "type": "string" }, "expiration-type": { "title": "Expiration-Type", "type": "string" }, "display-factor": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Display-Factor" }, "option-contract-symbol": { "title": "Option-Contract-Symbol", "type": "string" }, "stops-trading-at": { "format": "date-time", "title": "Stops-Trading-At", "type": "string" }, "settlement-type": { "title": "Settlement-Type", "type": "string" }, "strikes": { "items": { "$ref": "#/$defs/Strike" }, "title": "Strikes", "type": "array" }, "tick-sizes": { "items": { "$ref": "#/$defs/TickSize" }, "title": "Tick-Sizes", "type": "array" } }, "$defs": { "Strike": { "description": "Dataclass representing a specific strike in an options chain, containing\nthe symbols for the call and put options.", "properties": { "strike-price": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Strike-Price" }, "call": { "title": "Call", "type": "string" }, "put": { "title": "Put", "type": "string" }, "call-streamer-symbol": { "title": "Call-Streamer-Symbol", "type": "string" }, "put-streamer-symbol": { "title": "Put-Streamer-Symbol", "type": "string" } }, "required": [ "strike-price", "call", "put", "call-streamer-symbol", "put-streamer-symbol" ], "title": "Strike", "type": "object" }, "TickSize": { "description": "Dataclass representing the tick size for an instrument.", "properties": { "value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Value" }, "threshold": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Threshold" }, "symbol": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Symbol" } }, "required": [ "value" ], "title": "TickSize", "type": "object" } }, "required": [ "root-symbol", "notional-value", "underlying-symbol", "strike-factor", "days-to-expiration", "option-root-symbol", "expiration-date", "expires-at", "asset", "expiration-type", "display-factor", "option-contract-symbol", "stops-trading-at", "settlement-type", "strikes", "tick-sizes" ] }

days_to_expiration (int)

display_factor (decimal.Decimal)

expiration_date (datetime.date)

expiration_type (str)

expires_at (datetime.datetime)

notional_value (decimal.Decimal)

option_contract_symbol (str)

option_root_symbol (str)

settlement_type (str)

stops_trading_at (datetime.datetime)

strike_factor (decimal.Decimal)

strikes (list[tastytrade.instruments.Strike])

tick_sizes (list[tastytrade.instruments.TickSize])

underlying_symbol (str)

Bases: TastytradeData

Dataclass representing an underlying future in a nested future options chain.

Show JSON schema{ "title": "NestedFutureOptionFuture", "description": "Dataclass representing an underlying future in a nested future options\nchain.", "type": "object", "properties": { "root-symbol": { "title": "Root-Symbol", "type": "string" }, "days-to-expiration": { "title": "Days-To-Expiration", "type": "integer" }, "expiration-date": { "format": "date", "title": "Expiration-Date", "type": "string" }, "expires-at": { "format": "date-time", "title": "Expires-At", "type": "string" }, "next-active-month": { "title": "Next-Active-Month", "type": "boolean" }, "symbol": { "title": "Symbol", "type": "string" }, "active-month": { "title": "Active-Month", "type": "boolean" }, "stops-trading-at": { "format": "date-time", "title": "Stops-Trading-At", "type": "string" }, "maturity-date": { "anyOf": [ { "format": "date", "type": "string" }, { "type": "null" } ], "default": null, "title": "Maturity-Date" } }, "required": [ "root-symbol", "days-to-expiration", "expiration-date", "expires-at", "next-active-month", "symbol", "active-month", "stops-trading-at" ] }

days_to_expiration (int)

expiration_date (datetime.date)

expires_at (datetime.datetime)

maturity_date (datetime.date | None)

next_active_month (bool)

stops_trading_at (datetime.datetime)

parse_date_with_utc » maturity_date

Bases: TastytradeData

Dataclass that represents a Tastytrade nested future option chain for a specific futures underlying symbol.

Show JSON schema{ "title": "NestedFutureOptionSubchain", "description": "Dataclass that represents a Tastytrade nested future option chain for a\nspecific futures underlying symbol.", "type": "object", "properties": { "underlying-symbol": { "title": "Underlying-Symbol", "type": "string" }, "root-symbol": { "title": "Root-Symbol", "type": "string" }, "exercise-style": { "title": "Exercise-Style", "type": "string" }, "expirations": { "items": { "$ref": "#/$defs/NestedFutureOptionChainExpiration" }, "title": "Expirations", "type": "array" } }, "$defs": { "NestedFutureOptionChainExpiration": { "description": "Dataclass representing an expiration in a nested future options chain.", "properties": { "root-symbol": { "title": "Root-Symbol", "type": "string" }, "notional-value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Notional-Value" }, "underlying-symbol": { "title": "Underlying-Symbol", "type": "string" }, "strike-factor": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Strike-Factor" }, "days-to-expiration": { "title": "Days-To-Expiration", "type": "integer" }, "option-root-symbol": { "title": "Option-Root-Symbol", "type": "string" }, "expiration-date": { "format": "date", "title": "Expiration-Date", "type": "string" }, "expires-at": { "format": "date-time", "title": "Expires-At", "type": "string" }, "asset": { "title": "Asset", "type": "string" }, "expiration-type": { "title": "Expiration-Type", "type": "string" }, "display-factor": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Display-Factor" }, "option-contract-symbol": { "title": "Option-Contract-Symbol", "type": "string" }, "stops-trading-at": { "format": "date-time", "title": "Stops-Trading-At", "type": "string" }, "settlement-type": { "title": "Settlement-Type", "type": "string" }, "strikes": { "items": { "$ref": "#/$defs/Strike" }, "title": "Strikes", "type": "array" }, "tick-sizes": { "items": { "$ref": "#/$defs/TickSize" }, "title": "Tick-Sizes", "type": "array" } }, "required": [ "root-symbol", "notional-value", "underlying-symbol", "strike-factor", "days-to-expiration", "option-root-symbol", "expiration-date", "expires-at", "asset", "expiration-type", "display-factor", "option-contract-symbol", "stops-trading-at", "settlement-type", "strikes", "tick-sizes" ], "title": "NestedFutureOptionChainExpiration", "type": "object" }, "Strike": { "description": "Dataclass representing a specific strike in an options chain, containing\nthe symbols for the call and put options.", "properties": { "strike-price": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Strike-Price" }, "call": { "title": "Call", "type": "string" }, "put": { "title": "Put", "type": "string" }, "call-streamer-symbol": { "title": "Call-Streamer-Symbol", "type": "string" }, "put-streamer-symbol": { "title": "Put-Streamer-Symbol", "type": "string" } }, "required": [ "strike-price", "call", "put", "call-streamer-symbol", "put-streamer-symbol" ], "title": "Strike", "type": "object" }, "TickSize": { "description": "Dataclass representing the tick size for an instrument.", "properties": { "value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Value" }, "threshold": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Threshold" }, "symbol": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Symbol" } }, "required": [ "value" ], "title": "TickSize", "type": "object" } }, "required": [ "underlying-symbol", "root-symbol", "exercise-style", "expirations" ] }

expirations (list[tastytrade.instruments.NestedFutureOptionChainExpiration])

underlying_symbol (str)

Bases: TastytradeData

Dataclass that represents a Tastytrade nested option chain object. Contains information about the option chain and a method to fetch one for a symbol.

This is cleaner than calling get_option_chain() but if you want to create actual Option objects you’ll need to make an extra API request or two.

Show JSON schema{ "title": "NestedOptionChain", "description": "Dataclass that represents a Tastytrade nested option chain object.\nContains information about the option chain and a method to fetch one for\na symbol.\n\nThis is cleaner than calling :meth:`get_option_chain` but if you want to\ncreate actual :class:`Option` objects you'll need to make an extra API\nrequest or two.", "type": "object", "properties": { "underlying-symbol": { "title": "Underlying-Symbol", "type": "string" }, "root-symbol": { "title": "Root-Symbol", "type": "string" }, "option-chain-type": { "title": "Option-Chain-Type", "type": "string" }, "shares-per-contract": { "title": "Shares-Per-Contract", "type": "integer" }, "tick-sizes": { "items": { "$ref": "#/$defs/TickSize" }, "title": "Tick-Sizes", "type": "array" }, "expirations": { "items": { "$ref": "#/$defs/NestedOptionChainExpiration" }, "title": "Expirations", "type": "array" }, "deliverables": { "anyOf": [ { "items": { "$ref": "#/$defs/Deliverable" }, "type": "array" }, { "type": "null" } ], "default": null, "title": "Deliverables" } }, "$defs": { "Deliverable": { "description": "Dataclass representing the deliverable for an option.", "properties": { "id": { "title": "Id", "type": "integer" }, "root-symbol": { "title": "Root-Symbol", "type": "string" }, "deliverable-type": { "title": "Deliverable-Type", "type": "string" }, "description": { "title": "Description", "type": "string" }, "amount": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Amount" }, "percent": { "title": "Percent", "type": "string" }, "symbol": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Symbol" }, "instrument-type": { "anyOf": [ { "$ref": "#/$defs/InstrumentType" }, { "type": "null" } ], "default": null } }, "required": [ "id", "root-symbol", "deliverable-type", "description", "amount", "percent" ], "title": "Deliverable", "type": "object" }, "InstrumentType": { "description": "This is an :class:`~enum.Enum` that contains the valid types of instruments\nand their representation in the API.", "enum": [ "Bond", "Cryptocurrency", "Currency Pair", "Equity", "Equity Offering", "Equity Option", "Fixed Income Security", "Future", "Future Option", "Index", "Liquidity Pool", "Unknown", "Warrant" ], "title": "InstrumentType", "type": "string" }, "NestedOptionChainExpiration": { "description": "Dataclass representing an expiration in a nested options chain.", "properties": { "expiration-type": { "title": "Expiration-Type", "type": "string" }, "expiration-date": { "format": "date", "title": "Expiration-Date", "type": "string" }, "days-to-expiration": { "title": "Days-To-Expiration", "type": "integer" }, "settlement-type": { "title": "Settlement-Type", "type": "string" }, "strikes": { "items": { "$ref": "#/$defs/Strike" }, "title": "Strikes", "type": "array" } }, "required": [ "expiration-type", "expiration-date", "days-to-expiration", "settlement-type", "strikes" ], "title": "NestedOptionChainExpiration", "type": "object" }, "Strike": { "description": "Dataclass representing a specific strike in an options chain, containing\nthe symbols for the call and put options.", "properties": { "strike-price": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Strike-Price" }, "call": { "title": "Call", "type": "string" }, "put": { "title": "Put", "type": "string" }, "call-streamer-symbol": { "title": "Call-Streamer-Symbol", "type": "string" }, "put-streamer-symbol": { "title": "Put-Streamer-Symbol", "type": "string" } }, "required": [ "strike-price", "call", "put", "call-streamer-symbol", "put-streamer-symbol" ], "title": "Strike", "type": "object" }, "TickSize": { "description": "Dataclass representing the tick size for an instrument.", "properties": { "value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Value" }, "threshold": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Threshold" }, "symbol": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Symbol" } }, "required": [ "value" ], "title": "TickSize", "type": "object" } }, "required": [ "underlying-symbol", "root-symbol", "option-chain-type", "shares-per-contract", "tick-sizes", "expirations" ] }

deliverables (list[tastytrade.instruments.Deliverable] | None)

expirations (list[tastytrade.instruments.NestedOptionChainExpiration])

option_chain_type (str)

shares_per_contract (int)

tick_sizes (list[tastytrade.instruments.TickSize])

underlying_symbol (str)

Gets the option chain for the given symbol in nested format.

the session to use for the request.

the symbol to get the option chain for.

Gets the option chain for the given symbol in nested format.

the session to use for the request.

the symbol to get the option chain for.

Bases: TastytradeData

Dataclass representing an expiration in a nested options chain.

Show JSON schema{ "title": "NestedOptionChainExpiration", "description": "Dataclass representing an expiration in a nested options chain.", "type": "object", "properties": { "expiration-type": { "title": "Expiration-Type", "type": "string" }, "expiration-date": { "format": "date", "title": "Expiration-Date", "type": "string" }, "days-to-expiration": { "title": "Days-To-Expiration", "type": "integer" }, "settlement-type": { "title": "Settlement-Type", "type": "string" }, "strikes": { "items": { "$ref": "#/$defs/Strike" }, "title": "Strikes", "type": "array" } }, "$defs": { "Strike": { "description": "Dataclass representing a specific strike in an options chain, containing\nthe symbols for the call and put options.", "properties": { "strike-price": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Strike-Price" }, "call": { "title": "Call", "type": "string" }, "put": { "title": "Put", "type": "string" }, "call-streamer-symbol": { "title": "Call-Streamer-Symbol", "type": "string" }, "put-streamer-symbol": { "title": "Put-Streamer-Symbol", "type": "string" } }, "required": [ "strike-price", "call", "put", "call-streamer-symbol", "put-streamer-symbol" ], "title": "Strike", "type": "object" } }, "required": [ "expiration-type", "expiration-date", "days-to-expiration", "settlement-type", "strikes" ] }

days_to_expiration (int)

expiration_date (datetime.date)

expiration_type (str)

settlement_type (str)

strikes (list[tastytrade.instruments.Strike])

Bases: TradeableTastytradeData

Dataclass that represents a Tastytrade option object. Contains information about the option and methods to populate that data using option symbol(s).

Show JSON schema{ "title": "Option", "description": "Dataclass that represents a Tastytrade option object. Contains information\nabout the option and methods to populate that data using option symbol(s).", "type": "object", "properties": { "instrument-type": { "$ref": "#/$defs/InstrumentType" }, "symbol": { "title": "Symbol", "type": "string" }, "active": { "title": "Active", "type": "boolean" }, "strike-price": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Strike-Price" }, "root-symbol": { "title": "Root-Symbol", "type": "string" }, "underlying-symbol": { "title": "Underlying-Symbol", "type": "string" }, "expiration-date": { "format": "date", "title": "Expiration-Date", "type": "string" }, "exercise-style": { "title": "Exercise-Style", "type": "string" }, "shares-per-contract": { "title": "Shares-Per-Contract", "type": "integer" }, "option-type": { "$ref": "#/$defs/OptionType" }, "option-chain-type": { "title": "Option-Chain-Type", "type": "string" }, "expiration-type": { "title": "Expiration-Type", "type": "string" }, "settlement-type": { "title": "Settlement-Type", "type": "string" }, "stops-trading-at": { "format": "date-time", "title": "Stops-Trading-At", "type": "string" }, "market-time-instrument-collection": { "title": "Market-Time-Instrument-Collection", "type": "string" }, "days-to-expiration": { "title": "Days-To-Expiration", "type": "integer" }, "is-closing-only": { "title": "Is-Closing-Only", "type": "boolean" }, "expires-at": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "Expires-At" }, "streamer-symbol": { "default": "", "title": "Streamer-Symbol", "type": "string" }, "listed-market": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Listed-Market" }, "halted-at": { "anyOf": [ { "format": "date-time", "type": "string" }, { "type": "null" } ], "default": null, "title": "Halted-At" }, "old-security-number": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Old-Security-Number" } }, "$defs": { "InstrumentType": { "description": "This is an :class:`~enum.Enum` that contains the valid types of instruments\nand their representation in the API.", "enum": [ "Bond", "Cryptocurrency", "Currency Pair", "Equity", "Equity Offering", "Equity Option", "Fixed Income Security", "Future", "Future Option", "Index", "Liquidity Pool", "Unknown", "Warrant" ], "title": "InstrumentType", "type": "string" }, "OptionType": { "description": "This is an :class:`~enum.Enum` that contains the valid types of options\nand their abbreviations in the API.", "enum": [ "C", "P" ], "title": "OptionType", "type": "string" } }, "required": [ "instrument-type", "symbol", "active", "strike-price", "root-symbol", "underlying-symbol", "expiration-date", "exercise-style", "shares-per-contract", "option-type", "option-chain-type", "expiration-type", "settlement-type", "stops-trading-at", "market-time-instrument-collection", "days-to-expiration", "is-closing-only" ] }

days_to_expiration (int)

expiration_date (datetime.date)

expiration_type (str)

expires_at (datetime.datetime | None)

halted_at (datetime.datetime | None)

is_closing_only (bool)

listed_market (str | None)

market_time_instrument_collection (str)

old_security_number (str | None)

option_chain_type (str)

option_type (tastytrade.instruments.OptionType)

settlement_type (str)

shares_per_contract (int)

stops_trading_at (datetime.datetime)

streamer_symbol (str)

strike_price (decimal.Decimal)

underlying_symbol (str)

set_streamer_symbol » all fields

Returns a list of Option objects from the given symbols, or a single Option object if a list is not provided.

the session to use for the request.

the OCC symbol(s) to get the options for.

whether the options are active.

the number of options to get per page.

provide a specific page to get; if None, get all pages

whether to include expired options.

Returns a list of Option objects from the given symbols, or a single Option object if a list is not provided.

the session to use for the request.

the OCC symbol(s) to get the options for.

whether the options are active.

the number of options to get per page.

provide a specific page to get; if None, get all pages

whether to include expired options.

Returns the dxfeed symbol for use in the streamer from the given OCC 2010 symbol.

the OCC symbol to convert

Returns the OCC 2010 symbol equivalent to the given streamer symbol.

the streamer symbol to convert

This is an Enum that contains the valid types of options and their abbreviations in the API.

Valid values are as follows:

Bases: TastytradeData

Dataclass representing the decimal precision (number of places) for an instrument.

Show JSON schema{ "title": "QuantityDecimalPrecision", "description": "Dataclass representing the decimal precision (number of places) for an\ninstrument.", "type": "object", "properties": { "instrument-type": { "$ref": "#/$defs/InstrumentType" }, "value": { "title": "Value", "type": "integer" }, "minimum-increment-precision": { "title": "Minimum-Increment-Precision", "type": "integer" }, "symbol": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Symbol" } }, "$defs": { "InstrumentType": { "description": "This is an :class:`~enum.Enum` that contains the valid types of instruments\nand their representation in the API.", "enum": [ "Bond", "Cryptocurrency", "Currency Pair", "Equity", "Equity Offering", "Equity Option", "Fixed Income Security", "Future", "Future Option", "Index", "Liquidity Pool", "Unknown", "Warrant" ], "title": "InstrumentType", "type": "string" } }, "required": [ "instrument-type", "value", "minimum-increment-precision" ] }

instrument_type (tastytrade.order.InstrumentType)

minimum_increment_precision (int)

Bases: TastytradeData

Dataclass representing a roll for a future.

Show JSON schema{ "title": "Roll", "description": "Dataclass representing a roll for a future.", "type": "object", "properties": { "name": { "title": "Name", "type": "string" }, "active-count": { "title": "Active-Count", "type": "integer" }, "cash-settled": { "title": "Cash-Settled", "type": "boolean" }, "business-days-offset": { "title": "Business-Days-Offset", "type": "integer" }, "first-notice": { "title": "First-Notice", "type": "boolean" } }, "required": [ "name", "active-count", "cash-settled", "business-days-offset", "first-notice" ] }

business_days_offset (int)

Bases: TastytradeData

Dataclass representing a specific strike in an options chain, containing the symbols for the call and put options.

Show JSON schema{ "title": "Strike", "description": "Dataclass representing a specific strike in an options chain, containing\nthe symbols for the call and put options.", "type": "object", "properties": { "strike-price": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Strike-Price" }, "call": { "title": "Call", "type": "string" }, "put": { "title": "Put", "type": "string" }, "call-streamer-symbol": { "title": "Call-Streamer-Symbol", "type": "string" }, "put-streamer-symbol": { "title": "Put-Streamer-Symbol", "type": "string" } }, "required": [ "strike-price", "call", "put", "call-streamer-symbol", "put-streamer-symbol" ] }

call_streamer_symbol (str)

put_streamer_symbol (str)

strike_price (decimal.Decimal)

Bases: TastytradeData

Dataclass representing the tick size for an instrument.

Show JSON schema{ "title": "TickSize", "description": "Dataclass representing the tick size for an instrument.", "type": "object", "properties": { "value": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Value" }, "threshold": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Threshold" }, "symbol": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Symbol" } }, "required": [ "value" ] }

threshold (decimal.Decimal | None)

value (decimal.Decimal)

Bases: TastytradeData

Dataclass that represents a Tastytrade warrant object. Contains information about the warrant, and methods to get warrants.

Show JSON schema{ "title": "Warrant", "description": "Dataclass that represents a Tastytrade warrant object. Contains\ninformation about the warrant, and methods to get warrants.", "type": "object", "properties": { "symbol": { "title": "Symbol", "type": "string" }, "instrument-type": { "$ref": "#/$defs/InstrumentType" }, "listed-market": { "title": "Listed-Market", "type": "string" }, "description": { "title": "Description", "type": "string" }, "is-closing-only": { "title": "Is-Closing-Only", "type": "boolean" }, "active": { "title": "Active", "type": "boolean" }, "cusip": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Cusip" } }, "$defs": { "InstrumentType": { "description": "This is an :class:`~enum.Enum` that contains the valid types of instruments\nand their representation in the API.", "enum": [ "Bond", "Cryptocurrency", "Currency Pair", "Equity", "Equity Offering", "Equity Option", "Fixed Income Security", "Future", "Future Option", "Index", "Liquidity Pool", "Unknown", "Warrant" ], "title": "InstrumentType", "type": "string" } }, "required": [ "symbol", "instrument-type", "listed-market", "description", "is-closing-only", "active" ] }

instrument_type (tastytrade.order.InstrumentType)

is_closing_only (bool)

Returns a list of Warrant objects from the given symbols, or a single Warrant object if a list is not provided.

the session to use for the request.

symbol(s) of the warrants, e.g. ‘NKLAW’

Returns a list of Warrant objects from the given symbols, or a single Warrant object if a list is not provided.

the session to use for the request.

symbol(s) of the warrants, e.g. ‘NKLAW’

Returns a mapping of expiration date to a list of futures options objects representing the options chain for the given symbol.

In the case that there are two expiries on the same day (e.g. EW and ES options), both will be returned in the same list. If you just want one expiry, you’ll need to filter the list yourself, or use NestedFutureOptionChain instead.

the session to use for the request.

the symbol to get the option chain for.

Returns a mapping of expiration date to a list of option objects representing the options chain for the given symbol.

In the case that there are two expiries on the same day (e.g. SPXW and SPX AM options), both will be returned in the same list. If you just want one expiry, you’ll need to filter the list yourself, or use NestedOptionChain instead.

the session to use for the request.

the symbol to get the option chain for.

Returns a list of QuantityDecimalPrecision objects for different types of instruments.

the session to use for the request.

Returns a mapping of expiration date to a list of futures options objects representing the options chain for the given symbol.

In the case that there are two expiries on the same day (e.g. EW and ES options), both will be returned in the same list. If you just want one expiry, you’ll need to filter the list yourself, or use NestedFutureOptionChain instead.

the session to use for the request.

the symbol to get the option chain for.

Returns a mapping of expiration date to a list of option objects representing the options chain for the given symbol.

In the case that there are two expiries on the same day (e.g. SPXW and SPX AM options), both will be returned in the same list. If you just want one expiry, you’ll need to filter the list yourself, or use NestedOptionChain instead.

the session to use for the request.

the symbol to get the option chain for.

Returns a list of QuantityDecimalPrecision objects for different types of instruments.

the session to use for the request.

**Examples:**

Example 1 (json):
```json
{
   "title": "Cryptocurrency",
   "description": "Dataclass that represents a Tastytrade cryptocurrency object. Contains\ninformation about the cryptocurrency and methods to populate that data\nusing cryptocurrency symbol(s).",
   "type": "object",
   "properties": {
      "instrument-type": {
         "$ref": "#/$defs/InstrumentType"
      },
      "symbol": {
         "title": "Symbol",
         "type": "string"
      },
      "id": {
         "title": "Id",
         "type": "integer"
      },
      "short-description": {
         "title": "Short-Description",
         "type": "string"
      },
      "description": {
         "title": "Description",
         "type": "string"
      },
      "is-closing-only": {
         "title": "Is-Closing-Only",
         "type": "boolean"
      },
      "active": {
         "title": "Active",
         "type": "boolean"
      },
      "tick-size": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Tick-Size"
      },
      "destination-venue-symbols": {
         "items": {
            "$ref": "#/$defs/DestinationVenueSymbol"
         },
         "title": "Destination-Venue-Symbols",
         "type": "array"
      },
      "streamer-symbol": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Streamer-Symbol"
      }
   },
   "$defs": {
      "DestinationVenueSymbol": {
         "description": "Dataclass representing a specific destination venue symbol for a\ncryptocurrency.",
         "properties": {
            "id": {
               "title": "Id",
               "type": "integer"
            },
            "symbol": {
               "title": "Symbol",
               "type": "string"
            },
            "destination-venue": {
               "title": "Destination-Venue",
               "type": "string"
            },
            "routable": {
               "title": "Routable",
               "type": "boolean"
            },
            "max-quantity-precision": {
               "anyOf": [
                  {
                     "type": "integer"
                  },
                  {
                     "type": "null"
                  }
               ],
               "default": null,
               "title": "Max-Quantity-Precision"
            },
            "max-price-precision": {
               "anyOf": [
                  {
                     "type": "integer"
                  },
                  {
                     "type": "null"
                  }
               ],
               "default": null,
               "title": "Max-Price-Precision"
            }
         },
         "required": [
            "id",
            "symbol",
            "destination-venue",
            "routable"
         ],
         "title": "DestinationVenueSymbol",
         "type": "object"
      },
      "InstrumentType": {
         "description": "This is an :class:`~enum.Enum` that contains the valid types of instruments\nand their representation in the API.",
         "enum": [
            "Bond",
            "Cryptocurrency",
            "Currency Pair",
            "Equity",
            "Equity Offering",
            "Equity Option",
            "Fixed Income Security",
            "Future",
            "Future Option",
            "Index",
            "Liquidity Pool",
            "Unknown",
            "Warrant"
         ],
         "title": "InstrumentType",
         "type": "string"
      }
   },
   "required": [
      "instrument-type",
      "symbol",
      "id",
      "short-description",
      "description",
      "is-closing-only",
      "active",
      "tick-size",
      "destination-venue-symbols"
   ]
}
```

Example 2 (json):
```json
{
   "title": "Deliverable",
   "description": "Dataclass representing the deliverable for an option.",
   "type": "object",
   "properties": {
      "id": {
         "title": "Id",
         "type": "integer"
      },
      "root-symbol": {
         "title": "Root-Symbol",
         "type": "string"
      },
      "deliverable-type": {
         "title": "Deliverable-Type",
         "type": "string"
      },
      "description": {
         "title": "Description",
         "type": "string"
      },
      "amount": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Amount"
      },
      "percent": {
         "title": "Percent",
         "type": "string"
      },
      "symbol": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Symbol"
      },
      "instrument-type": {
         "anyOf": [
            {
               "$ref": "#/$defs/InstrumentType"
            },
            {
               "type": "null"
            }
         ],
         "default": null
      }
   },
   "$defs": {
      "InstrumentType": {
         "description": "This is an :class:`~enum.Enum` that contains the valid types of instruments\nand their representation in the API.",
         "enum": [
            "Bond",
            "Cryptocurrency",
            "Currency Pair",
            "Equity",
            "Equity Offering",
            "Equity Option",
            "Fixed Income Security",
            "Future",
            "Future Option",
            "Index",
            "Liquidity Pool",
            "Unknown",
            "Warrant"
         ],
         "title": "InstrumentType",
         "type": "string"
      }
   },
   "required": [
      "id",
      "root-symbol",
      "deliverable-type",
      "description",
      "amount",
      "percent"
   ]
}
```

Example 3 (json):
```json
{
   "title": "DestinationVenueSymbol",
   "description": "Dataclass representing a specific destination venue symbol for a\ncryptocurrency.",
   "type": "object",
   "properties": {
      "id": {
         "title": "Id",
         "type": "integer"
      },
      "symbol": {
         "title": "Symbol",
         "type": "string"
      },
      "destination-venue": {
         "title": "Destination-Venue",
         "type": "string"
      },
      "routable": {
         "title": "Routable",
         "type": "boolean"
      },
      "max-quantity-precision": {
         "anyOf": [
            {
               "type": "integer"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Max-Quantity-Precision"
      },
      "max-price-precision": {
         "anyOf": [
            {
               "type": "integer"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Max-Price-Precision"
      }
   },
   "required": [
      "id",
      "symbol",
      "destination-venue",
      "routable"
   ]
}
```

Example 4 (json):
```json
{
   "title": "Equity",
   "description": "Dataclass that represents a Tastytrade equity object. Contains information\nabout the equity and methods to populate that data using equity symbol(s).",
   "type": "object",
   "properties": {
      "instrument-type": {
         "$ref": "#/$defs/InstrumentType"
      },
      "symbol": {
         "title": "Symbol",
         "type": "string"
      },
      "id": {
         "title": "Id",
         "type": "integer"
      },
      "is-index": {
         "title": "Is-Index",
         "type": "boolean"
      },
      "description": {
         "title": "Description",
         "type": "string"
      },
      "lendability": {
         "title": "Lendability",
         "type": "string"
      },
      "market-time-instrument-collection": {
         "title": "Market-Time-Instrument-Collection",
         "type": "string"
      },
      "is-closing-only": {
         "title": "Is-Closing-Only",
         "type": "boolean"
      },
      "is-options-closing-only": {
         "title": "Is-Options-Closing-Only",
         "type": "boolean"
      },
      "active": {
         "title": "Active",
         "type": "boolean"
      },
      "is-illiquid": {
         "title": "Is-Illiquid",
         "type": "boolean"
      },
      "is-etf": {
         "title": "Is-Etf",
         "type": "boolean"
      },
      "streamer-symbol": {
         "title": "Streamer-Symbol",
         "type": "string"
      },
      "borrow-rate": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Borrow-Rate"
      },
      "cusip": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Cusip"
      },
      "short-description": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Short-Description"
      },
      "halted-at": {
         "anyOf": [
            {
               "format": "date-time",
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Halted-At"
      },
      "stops-trading-at": {
         "anyOf": [
            {
               "format": "date-time",
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Stops-Trading-At"
      },
      "is-fractional-quantity-eligible": {
         "anyOf": [
            {
               "type": "boolean"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Is-Fractional-Quantity-Eligible"
      },
      "tick-sizes": {
         "anyOf": [
            {
               "items": {
                  "$ref": "#/$defs/TickSize"
               },
               "type": "array"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Tick-Sizes"
      },
      "listed-market": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Listed-Market"
      },
      "option-tick-sizes": {
         "anyOf": [
            {
               "items": {
                  "$ref": "#/$defs/TickSize"
               },
               "type": "array"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Option-Tick-Sizes"
      }
   },
   "$defs": {
      "InstrumentType": {
         "description": "This is an :class:`~enum.Enum` that contains the valid types of instruments\nand their representation in the API.",
         "enum": [
            "Bond",
            "Cryptocurrency",
            "Currency Pair",
            "Equity",
            "Equity Offering",
            "Equity Option",
            "Fixed Income Security",
            "Future",
            "Future Option",
            "Index",
            "Liquidity Pool",
            "Unknown",
            "Warrant"
         ],
         "title": "InstrumentType",
         "type": "string"
      },
      "TickSize": {
         "description": "Dataclass representing the tick size for an instrument.",
         "properties": {
            "value": {
               "anyOf": [
                  {
                     "type": "number"
                  },
                  {
                     "type": "string"
                  }
               ],
               "title": "Value"
            },
            "threshold": {
               "anyOf": [
                  {
                     "type": "number"
                  },
                  {
                     "type": "string"
                  },
                  {
                     "type": "null"
                  }
               ],
               "default": null,
               "title": "Threshold"
            },
            "symbol": {
               "anyOf": [
                  {
                     "type": "string"
                  },
                  {
                     "type": "null"
                  }
               ],
               "default": null,
               "title": "Symbol"
            }
         },
         "required": [
            "value"
         ],
         "title": "TickSize",
         "type": "object"
      }
   },
   "required": [
      "instrument-type",
      "symbol",
      "id",
      "is-index",
      "description",
      "lendability",
      "market-time-instrument-collection",
      "is-closing-only",
      "is-options-closing-only",
      "active",
      "is-illiquid",
      "is-etf",
      "streamer-symbol"
   ]
}
```

---

## Sessions - tastytrade 11.1.0 documentation

**URL:** https://tastyworks-api.readthedocs.io/en/latest/sessions.html

**Contents:**
- Sessions¶
- Creating an OAuth application¶
- Generating an initial refresh token¶
- Creating a session¶

A session object is required to authenticate your requests to the Tastytrade API. Tastytrade uses OAuth logins, which allow you to connect applications (third-party or private) to your trading account to use the API.

To get started, create a new OAuth application here. Check all the scopes you plan to use, add http://localhost:8000 as a valid callback, and create the application. Save the client secret, you’ll need it later!

In order to generate an initial refresh token, you have two options. The easiest way is to simply generate one from Tastytrade’s website: go to OAuth Applications > Manage > Create Grant to get a new refresh token, which you should also save.

At this point, OAuth is now setup correctly! Doing these steps once is sufficient for indefinite usage of Session for authentication to the API, since refresh tokens never expire. From now on you can simply authenticate with your client secret and refresh token.

These session objects can be used to make API requests:

Note that OAuth sessions make API requests using a special session token, which has a duration of only 15 minutes. However, since the refresh tokens last forever, you can call Session.refresh() to refresh the session token whenever needed. The session object will keep track of session expiration time for you to make it easier to know when to refresh:

A sandbox account for testing can be created here, then used to create a session in the same way:

**Examples:**

Example 1 (python):
```python
from tastytrade import Session

session = Session('client_secret', 'refresh_token')
```

Example 2 (python):
```python
from tastytrade import Account

accounts = Account.get(session)
```

Example 3 (python):
```python
from tastytrade.utils import now_in_new_york

if now_in_new_york() > session.session_expiration:
    session.refresh()
    print(Account.get(session))
```

Example 4 (python):
```python
from tastytrade import Session
session = Session('client_secret', 'refresh_token', is_test=True)
```

---

## sync/async - tastytrade 11.1.0 documentation

**URL:** https://tastyworks-api.readthedocs.io/en/latest/sync-async.html

**Contents:**
- sync/async¶

After creating a session (which is always initialized synchronously), the rest of the API endpoints implemented in the SDK have both sync and async implementations as of version 9.0.

Let’s see how this looks:

The async implementation is similar:

That’s it! All sync methods have a parallel async method that starts with a_.

Please note that two modules, tastytrade.backtest and tastytrade.streamer, only have async implementations. But for everything else, you can use what you’d like!

**Examples:**

Example 1 (julia):
```julia
from tastytrade Account, Session
session = Session(username, password)
# using sync implementation
accounts = Account.get(session)
```

Example 2 (julia):
```julia
from tastytrade Account, Session
session = Session(username, password)
# using async implementation
accounts = await Account.a_get(session)
```

---

## Installation - tastytrade 11.1.0 documentation

**URL:** https://tastyworks-api.readthedocs.io/en/latest/installation.html

**Contents:**
- Installation¶
- Via pypi¶
- From source¶
- Windows¶

The easiest way to install the SDK is using pip:

You can also install from source. Make sure you have uv installed beforehand.

If you’re contributing, you’ll want to run tests on your changes locally:

If you want to build the documentation (usually not necessary):

If you want to install from source on Windows, you can’t use the Makefile, so just run the commands individually. For example:

**Examples:**

Example 1 (unknown):
```unknown
$ pip install tastytrade
```

Example 2 (unknown):
```unknown
$ git clone https://github.com/tastyware/tastytrade.git
$ cd tastytrade
$ make install
```

Example 3 (unknown):
```unknown
$ make lint
$ make test
```

Example 4 (unknown):
```unknown
$ make docs
```

---

## Market Data - tastytrade 11.1.0 documentation

**URL:** https://tastyworks-api.readthedocs.io/en/latest/market-data.html

**Contents:**
- Market Data¶

We’ve seen how the streamer can be used to get quotes continually throughout the day, which is very helpful. However, sometimes we just need to get data once, which makes setting up a streamer, subscribing to events, and listening for them more complex than need be.

Fortunately, Tastytrade has endpoints that make fetching data for one-time use a breeze:

You can also fetch data for multiple symbols at once:

**Examples:**

Example 1 (swift):
```swift
from tastytrade.market_data import get_market_data
from tastytrade.order import InstrumentType

data = get_market_data(session, "SPY", InstrumentType.EQUITY)
print(data)
```

Example 2 (unknown):
```unknown
>>> symbol='SPY' instrument_type=<InstrumentType.EQUITY: 'Equity'> updated_at=datetime.datetime(2025, 4, 28, 21, 46, 48, 84000, tzinfo=TzInfo(UTC)) bid_size=Decimal('2.0') ask_size=Decimal('4.0') mark=Decimal('549.96') close_price_type=<ClosePriceType.FINAL: 'Final'> prev_close=Decimal('550.64') prev_close_price_type=<ClosePriceType.FINAL: 'Final'> summary_date=datetime.date(2025, 4, 28) prev_close_date=datetime.date(2025, 4, 25) halt_start_time=-1 halt_end_time=-1 ask=Decimal('550.0') beta=Decimal('1.009463163') bid=Decimal('549.9') close=Decimal('550.85') day_high_price=Decimal('553.55') day_low_price=Decimal('545.02') dividend_amount=Decimal('1.695528') dividend_frequency=Decimal('4.0') high_limit_price=Decimal('606.41') last=Decimal('549.96') last_mkt=Decimal('550.85') low_limit_price=Decimal('496.16') mid=Decimal('549.95') open=Decimal('551.39') volume=Decimal('47417792.0') year_low_price=Decimal('481.8') year_high_price=Decimal('613.23')
```

Example 3 (swift):
```swift
from tastytrade.market_data import get_market_data_by_type

data = get_market_data_by_type(
     session,
     indices=["SPX", "VIX"],
     cryptocurrencies=["ETH/USD", "BTC/USD"],
     equities=["SPLG", "SPY"],
     futures=["/MCLG6", "/MCLF6"],
     future_options=["./MCLM5MW2K5 250509C62.5", "./MCLM5MW2K5 250509P65.75"],
     options=["SPLG  250516C00048000", "SPLG  250516P00054000"],
)
print(data)
```

Example 4 (unknown):
```unknown
>>> [MarketData(symbol='SPLG  250516C00048000' instrument_type=<InstrumentType.EQUITY_OPTION: 'Equity Option'> updated_at=datetime.datetime(2025, 4, 28, 21, 30, 5, 358000, tzinfo=TzInfo(UTC)) bid_size=Decimal('28.0') ask_size=Decimal('62.0') mark=Decimal('16.8') close_price_type=<ClosePriceType.REGULAR: 'Regular'> prev_close=Decimal('12.3') prev_close_price_type=<ClosePriceType.REGULAR: 'Regular'> summary_date=datetime.date(2025, 4, 28) prev_close_date=datetime.date(2025, 4, 21) halt_start_time=-1 halt_end_time=-1 ask=Decimal('17.4') bid=Decimal('16.2') day_high_price=Decimal('12.99') day_low_price=Decimal('12.3') last=Decimal('12.3') last_mkt=Decimal('12.3') mid=Decimal('16.8') open=Decimal('12.99') volume=Decimal('4.0')), MarketData(symbol='BTC/USD' instrument_type=<InstrumentType.CRYPTOCURRENCY: 'Cryptocurrency'> updated_at=datetime.datetime(2025, 4, 28, 21, 46, 15, 630000, tzinfo=TzInfo(UTC)) bid_size=Decimal('0.222') mark=Decimal('94370.795') close_price_type=<ClosePriceType.REGULAR: 'Regular'> prev_close=Decimal('93797.555') prev_close_price_type=<ClosePriceType.REGULAR: 'Regular'> summary_date=datetime.date(2025, 4, 28) prev_close_date=datetime.date(2025, 4, 27) halt_start_time=-1 halt_end_time=-1 ask=Decimal('94848.23') bid=Decimal('93893.36') day_high_price=Decimal('95581.855') day_low_price=Decimal('93476.925') last=Decimal('94388.57') last_mkt=Decimal('94370.8') mid=Decimal('94370.795') open=Decimal('93795.825') year_low_price=Decimal('49149.415') year_high_price=Decimal('109558.42')), MarketData(symbol='ETH/USD' instrument_type=<InstrumentType.CRYPTOCURRENCY: 'Cryptocurrency'> updated_at=datetime.datetime(2025, 4, 28, 21, 46, 40, 633000, tzinfo=TzInfo(UTC)) bid_size=Decimal('11.09900497') ask_size=Decimal('11.0') mark=Decimal('1786.455') close_price_type=<ClosePriceType.REGULAR: 'Regular'> prev_close=Decimal('1788.33') prev_close_price_type=<ClosePriceType.REGULAR: 'Regular'> summary_date=datetime.date(2025, 4, 28) prev_close_date=datetime.date(2025, 4, 27) halt_start_time=-1 halt_end_time=-1 ask=Decimal('1795.59') bid=Decimal('1777.32') day_high_price=Decimal('1828.26') day_low_price=Decimal('1745.165') last=Decimal('1786.46') last_mkt=Decimal('1786.46') mid=Decimal('1786.455') open=Decimal('1788.345') year_low_price=Decimal('1384.31') year_high_price=Decimal('4109.98')), MarketData(symbol='VIX' instrument_type=<InstrumentType.EQUITY: 'Equity'> updated_at=datetime.datetime(2025, 4, 28, 20, 15, 1, 568000, tzinfo=TzInfo(UTC)) mark=Decimal('25.15') close_price_type=<ClosePriceType.REGULAR: 'Regular'> prev_close=Decimal('24.84') prev_close_price_type=<ClosePriceType.REGULAR: 'Regular'> summary_date=datetime.date(2025, 4, 28) prev_close_date=datetime.date(2025, 4, 25) halt_start_time=-1 halt_end_time=-1 beta=Decimal('-6.538134414') day_high_price=Decimal('26.93') day_low_price=Decimal('24.7') last=Decimal('25.15') last_mkt=Decimal('25.15') open=Decimal('25.75') year_low_price=Decimal('10.62') year_high_price=Decimal('65.73')), MarketData(symbol='/MCLG6' instrument_type=<InstrumentType.FUTURE: 'Future'> updated_at=datetime.datetime(2025, 4, 28, 21, 40, 0, 903000, tzinfo=TzInfo(UTC)) mark=Decimal('59.44') close_price_type=<ClosePriceType.REGULAR: 'Regular'> prev_close=Decimal('59.87') prev_close_price_type=<ClosePriceType.PRELIMINARY: 'Preliminary'> summary_date=datetime.date(2025, 4, 29) prev_close_date=datetime.date(2025, 4, 28) halt_start_time=-1 halt_end_time=-1 ask=Decimal('60.08') bid=Decimal('59.3') day_high_price=Decimal('60.3') day_low_price=Decimal('59.44') last=Decimal('59.44') last_mkt=Decimal('59.44') mid=Decimal('59.69') open=Decimal('60.3') volume=Decimal('5.0')), MarketData(symbol='/MCLF6' instrument_type=<InstrumentType.FUTURE: 'Future'> updated_at=datetime.datetime(2025, 4, 28, 21, 40, 0, 905000, tzinfo=TzInfo(UTC)) bid_size=Decimal('1.0') ask_size=Decimal('1.0') mark=Decimal('60.5') close_price_type=<ClosePriceType.REGULAR: 'Regular'> prev_close=Decimal('59.87') prev_close_price_type=<ClosePriceType.PRELIMINARY: 'Preliminary'> summary_date=datetime.date(2025, 4, 29) prev_close_date=datetime.date(2025, 4, 28) halt_start_time=-1 halt_end_time=-1 ask=Decimal('62.18') bid=Decimal('57.0') day_high_price=Decimal('60.5') day_low_price=Decimal('59.9') last=Decimal('60.5') last_mkt=Decimal('60.5') mid=Decimal('59.59') open=Decimal('59.9') volume=Decimal('2.0')), MarketData(symbol='./MCLM5MW2K5 250509C62.5' instrument_type=<InstrumentType.FUTURE_OPTION: 'Future Option'> updated_at=datetime.datetime(2025, 4, 28, 21, 30, 2, 211000, tzinfo=TzInfo(UTC)) mark=Decimal('1.479701886') close_price_type=<ClosePriceType.REGULAR: 'Regular'> prev_close_price_type=<ClosePriceType.INDICATIVE: 'Indicative'> summary_date=datetime.date(2025, 4, 29) prev_close_date=datetime.date(2025, 4, 25) halt_start_time=-1 halt_end_time=-1 ask=Decimal('2.19') bid=Decimal('0.91') mid=Decimal('1.55')), MarketData(symbol='SPX' instrument_type=<InstrumentType.INDEX: 'Index'> updated_at=datetime.datetime(2025, 4, 28, 20, 53, 27, 551000, tzinfo=TzInfo(UTC)) mark=Decimal('5509.565') close_price_type=<ClosePriceType.REGULAR: 'Regular'> prev_close=Decimal('5525.21') prev_close_price_type=<ClosePriceType.REGULAR: 'Regular'> summary_date=datetime.date(2025, 4, 28) prev_close_date=datetime.date(2025, 4, 25) halt_start_time=-1 halt_end_time=-1 ask=Decimal('5576.76') beta=Decimal('1.0') bid=Decimal('5442.37') day_high_price=Decimal('5553.66') day_low_price=Decimal('5468.64') last=Decimal('5528.75') last_mkt=Decimal('5528.75') mid=Decimal('5509.565') open=Decimal('5529.22') year_low_price=Decimal('4835.04') year_high_price=Decimal('6147.43')), MarketData(symbol='SPLG  250516P00054000' instrument_type=<InstrumentType.EQUITY_OPTION: 'Equity Option'> updated_at=datetime.datetime(2025, 4, 28, 21, 31, 33, 779000, tzinfo=TzInfo(UTC)) bid_size=Decimal('1.0') ask_size=Decimal('11.0') mark=Decimal('0.075') close_price_type=<ClosePriceType.REGULAR: 'Regular'> prev_close=Decimal('0.1') prev_close_price_type=<ClosePriceType.REGULAR: 'Regular'> summary_date=datetime.date(2025, 4, 28) prev_close_date=datetime.date(2025, 4, 25) halt_start_time=-1 halt_end_time=-1 ask=Decimal('0.1') bid=Decimal('0.05') close=Decimal('0.05') day_high_price=Decimal('0.1') day_low_price=Decimal('0.05') last=Decimal('0.05') last_mkt=Decimal('0.05') mid=Decimal('0.075') open=Decimal('0.1') volume=Decimal('2.0')), MarketData(symbol='SPY' instrument_type=<InstrumentType.EQUITY: 'Equity'> updated_at=datetime.datetime(2025, 4, 28, 21, 46, 48, 84000, tzinfo=TzInfo(UTC)) bid_size=Decimal('2.0') ask_size=Decimal('4.0') mark=Decimal('549.96') close_price_type=<ClosePriceType.FINAL: 'Final'> prev_close=Decimal('550.64') prev_close_price_type=<ClosePriceType.FINAL: 'Final'> summary_date=datetime.date(2025, 4, 28) prev_close_date=datetime.date(2025, 4, 25) halt_start_time=-1 halt_end_time=-1 ask=Decimal('550.0') beta=Decimal('1.009463163') bid=Decimal('549.9') close=Decimal('550.85') day_high_price=Decimal('553.55') day_low_price=Decimal('545.02') dividend_amount=Decimal('1.695528') dividend_frequency=Decimal('4.0') high_limit_price=Decimal('606.41') last=Decimal('549.96') last_mkt=Decimal('550.85') low_limit_price=Decimal('496.16') mid=Decimal('549.95') open=Decimal('551.39') volume=Decimal('47417792.0') year_low_price=Decimal('481.8') year_high_price=Decimal('613.23')), MarketData(symbol='SPLG' instrument_type=<InstrumentType.EQUITY: 'Equity'> updated_at=datetime.datetime(2025, 4, 28, 21, 46, 25, 333000, tzinfo=TzInfo(UTC)) bid_size=Decimal('1.0') ask_size=Decimal('1.0') mark=Decimal('64.73') close_price_type=<ClosePriceType.FINAL: 'Final'> prev_close=Decimal('64.74') prev_close_price_type=<ClosePriceType.FINAL: 'Final'> summary_date=datetime.date(2025, 4, 28) prev_close_date=datetime.date(2025, 4, 25) halt_start_time=-1 halt_end_time=-1 ask=Decimal('64.75') beta=Decimal('1.008512722') bid=Decimal('64.68') close=Decimal('64.8') day_high_price=Decimal('65.1') day_low_price=Decimal('64.11') dividend_amount=Decimal('0.217412') dividend_frequency=Decimal('4.0') high_limit_price=Decimal('71.34') last=Decimal('64.73') last_mkt=Decimal('64.8') low_limit_price=Decimal('58.37') mid=Decimal('64.715') open=Decimal('64.86') volume=Decimal('7159762.0') year_low_price=Decimal('56.6699') year_high_price=Decimal('72.14')), MarketData(symbol='./MCLM5MW2K5 250509P65.75' instrument_type=<InstrumentType.FUTURE_OPTION: 'Future Option'> updated_at=datetime.datetime(2025, 4, 28, 21, 30, 2, 58000, tzinfo=TzInfo(UTC)) mark=Decimal('4.26456101') close_price_type=<ClosePriceType.REGULAR: 'Regular'> prev_close_price_type=<ClosePriceType.INDICATIVE: 'Indicative'> summary_date=datetime.date(2025, 4, 29) prev_close_date=datetime.date(2025, 4, 25) halt_start_time=-1 halt_end_time=-1 ask=Decimal('4.62') bid=Decimal('3.7') mid=Decimal('4.16'))]
```

---

## tastytrade.watchlists - tastytrade 11.1.0 documentation

**URL:** https://tastyworks-api.readthedocs.io/en/latest/api/watchlists.html

**Contents:**
- tastytrade.watchlists¶

Bases: TastytradeData

Dataclass that represents a specific pair in a pairs watchlist.

Show JSON schema{ "title": "Pair", "description": "Dataclass that represents a specific pair in a pairs watchlist.", "type": "object", "properties": { "left-action": { "title": "Left-Action", "type": "string" }, "left-symbol": { "title": "Left-Symbol", "type": "string" }, "left-quantity": { "title": "Left-Quantity", "type": "integer" }, "right-action": { "title": "Right-Action", "type": "string" }, "right-symbol": { "title": "Right-Symbol", "type": "string" }, "right-quantity": { "title": "Right-Quantity", "type": "integer" } }, "required": [ "left-action", "left-symbol", "left-quantity", "right-action", "right-symbol", "right-quantity" ] }

Bases: TastytradeData

Dataclass that represents a pairs watchlist object.

Show JSON schema{ "title": "PairsWatchlist", "description": "Dataclass that represents a pairs watchlist object.", "type": "object", "properties": { "name": { "title": "Name", "type": "string" }, "order-index": { "title": "Order-Index", "type": "integer" }, "pairs-equations": { "items": { "$ref": "#/$defs/Pair" }, "title": "Pairs-Equations", "type": "array" } }, "$defs": { "Pair": { "description": "Dataclass that represents a specific pair in a pairs watchlist.", "properties": { "left-action": { "title": "Left-Action", "type": "string" }, "left-symbol": { "title": "Left-Symbol", "type": "string" }, "left-quantity": { "title": "Left-Quantity", "type": "integer" }, "right-action": { "title": "Right-Action", "type": "string" }, "right-symbol": { "title": "Right-Symbol", "type": "string" }, "right-quantity": { "title": "Right-Quantity", "type": "integer" } }, "required": [ "left-action", "left-symbol", "left-quantity", "right-action", "right-symbol", "right-quantity" ], "title": "Pair", "type": "object" } }, "required": [ "name", "order-index", "pairs-equations" ] }

pairs_equations (list[tastytrade.watchlists.Pair])

Fetches a list of all Tastytrade public pairs watchlists, or a specific one if a name is provided.

the session to use for the request.

the name of the pairs watchlist to fetch.

Fetches a list of all Tastytrade public pairs watchlists, or a specific one if a name is provided.

the session to use for the request.

the name of the pairs watchlist to fetch.

Dataclass that contains a private watchlist object, with functions to update, publish, modify and remove watchlists.

Show JSON schema{ "title": "PrivateWatchlist", "description": "Dataclass that contains a private watchlist object, with functions to\nupdate, publish, modify and remove watchlists.", "type": "object", "properties": { "name": { "title": "Name", "type": "string" }, "watchlist-entries": { "anyOf": [ { "items": { "additionalProperties": true, "type": "object" }, "type": "array" }, { "type": "null" } ], "default": null, "title": "Watchlist-Entries" }, "group-name": { "default": "default", "title": "Group-Name", "type": "string" }, "order-index": { "default": 9999, "title": "Order-Index", "type": "integer" } }, "required": [ "name" ] }

Fetches the user’s private watchlists, or a specific one if a name is provided.

the session to use for the request.

the name of the watchlist to fetch.

Deletes the named private watchlist.

the session to use for the request.

the name of the watchlist to delete.

Updates the existing private remote watchlist.

the session to use for the request.

Creates a private remote watchlist identical to this local one.

the session to use for the request.

Adds a symbol to the watchlist.

Fetches the user’s private watchlists, or a specific one if a name is provided.

the session to use for the request.

the name of the watchlist to fetch.

Deletes the named private watchlist.

the session to use for the request.

the name of the watchlist to delete.

Removes a symbol from the watchlist.

Updates the existing private remote watchlist.

the session to use for the request.

Creates a private remote watchlist identical to this local one.

the session to use for the request.

Dataclass that contains symbols from a public watchlist.

Show JSON schema{ "title": "PublicWatchlist", "description": "Dataclass that contains symbols from a public watchlist.", "type": "object", "properties": { "name": { "title": "Name", "type": "string" }, "watchlist-entries": { "anyOf": [ { "items": { "additionalProperties": true, "type": "object" }, "type": "array" }, { "type": "null" } ], "default": null, "title": "Watchlist-Entries" }, "group-name": { "default": "default", "title": "Group-Name", "type": "string" }, "order-index": { "default": 9999, "title": "Order-Index", "type": "integer" } }, "required": [ "name" ] }

Fetches a list of all Tastytrade public watchlists, or a specific one if a name is provided.

the session to use for the request.

the name of the watchlist to fetch.

whether to only fetch the counts of the watchlists.

Fetches a list of all Tastytrade public watchlists, or a specific one if a name is provided.

the session to use for the request.

the name of the watchlist to fetch.

whether to only fetch the counts of the watchlists.

Bases: TastytradeData

Show JSON schema{ "title": "Watchlist", "type": "object", "properties": { "name": { "title": "Name", "type": "string" }, "watchlist-entries": { "anyOf": [ { "items": { "additionalProperties": true, "type": "object" }, "type": "array" }, { "type": "null" } ], "default": null, "title": "Watchlist-Entries" }, "group-name": { "default": "default", "title": "Group-Name", "type": "string" }, "order-index": { "default": 9999, "title": "Order-Index", "type": "integer" } }, "required": [ "name" ] }

watchlist_entries (list[dict[str, Any]] | None)

**Examples:**

Example 1 (json):
```json
{
   "title": "Pair",
   "description": "Dataclass that represents a specific pair in a pairs watchlist.",
   "type": "object",
   "properties": {
      "left-action": {
         "title": "Left-Action",
         "type": "string"
      },
      "left-symbol": {
         "title": "Left-Symbol",
         "type": "string"
      },
      "left-quantity": {
         "title": "Left-Quantity",
         "type": "integer"
      },
      "right-action": {
         "title": "Right-Action",
         "type": "string"
      },
      "right-symbol": {
         "title": "Right-Symbol",
         "type": "string"
      },
      "right-quantity": {
         "title": "Right-Quantity",
         "type": "integer"
      }
   },
   "required": [
      "left-action",
      "left-symbol",
      "left-quantity",
      "right-action",
      "right-symbol",
      "right-quantity"
   ]
}
```

Example 2 (json):
```json
{
   "title": "PairsWatchlist",
   "description": "Dataclass that represents a pairs watchlist object.",
   "type": "object",
   "properties": {
      "name": {
         "title": "Name",
         "type": "string"
      },
      "order-index": {
         "title": "Order-Index",
         "type": "integer"
      },
      "pairs-equations": {
         "items": {
            "$ref": "#/$defs/Pair"
         },
         "title": "Pairs-Equations",
         "type": "array"
      }
   },
   "$defs": {
      "Pair": {
         "description": "Dataclass that represents a specific pair in a pairs watchlist.",
         "properties": {
            "left-action": {
               "title": "Left-Action",
               "type": "string"
            },
            "left-symbol": {
               "title": "Left-Symbol",
               "type": "string"
            },
            "left-quantity": {
               "title": "Left-Quantity",
               "type": "integer"
            },
            "right-action": {
               "title": "Right-Action",
               "type": "string"
            },
            "right-symbol": {
               "title": "Right-Symbol",
               "type": "string"
            },
            "right-quantity": {
               "title": "Right-Quantity",
               "type": "integer"
            }
         },
         "required": [
            "left-action",
            "left-symbol",
            "left-quantity",
            "right-action",
            "right-symbol",
            "right-quantity"
         ],
         "title": "Pair",
         "type": "object"
      }
   },
   "required": [
      "name",
      "order-index",
      "pairs-equations"
   ]
}
```

Example 3 (json):
```json
{
   "title": "PrivateWatchlist",
   "description": "Dataclass that contains a private watchlist object, with functions to\nupdate, publish, modify and remove watchlists.",
   "type": "object",
   "properties": {
      "name": {
         "title": "Name",
         "type": "string"
      },
      "watchlist-entries": {
         "anyOf": [
            {
               "items": {
                  "additionalProperties": true,
                  "type": "object"
               },
               "type": "array"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Watchlist-Entries"
      },
      "group-name": {
         "default": "default",
         "title": "Group-Name",
         "type": "string"
      },
      "order-index": {
         "default": 9999,
         "title": "Order-Index",
         "type": "integer"
      }
   },
   "required": [
      "name"
   ]
}
```

Example 4 (json):
```json
{
   "title": "PublicWatchlist",
   "description": "Dataclass that contains symbols from a public watchlist.",
   "type": "object",
   "properties": {
      "name": {
         "title": "Name",
         "type": "string"
      },
      "watchlist-entries": {
         "anyOf": [
            {
               "items": {
                  "additionalProperties": true,
                  "type": "object"
               },
               "type": "array"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Watchlist-Entries"
      },
      "group-name": {
         "default": "default",
         "title": "Group-Name",
         "type": "string"
      },
      "order-index": {
         "default": 9999,
         "title": "Order-Index",
         "type": "integer"
      }
   },
   "required": [
      "name"
   ]
}
```

---

## Instruments - tastytrade 11.1.0 documentation

**URL:** https://tastyworks-api.readthedocs.io/en/latest/instruments.html

**Contents:**
- Instruments¶
- Initialization¶
- Options chains¶
- Placing trades¶

In the Tastytrade API, an instrument is a tradeable object, such as a cryptocurrency, an option, an equity/ETF, futures, futures options, and warrants. The SDK makes it easy to fetch, trade, and perform various other operations for these instruments.

Instruments follow a basic schema for initialization. To create an instrument(s), use the classmethods for the desired type of instrument:

These functions take the session object as the first parameter, and the symbol (or list of symbols) as the second. Note that ETFs and indices are treated as equities for the purposes of the API.

The different instruments have a host of properties that will be automatically populated with their associated values upon initialization. You can explore these properties in depth in the “SDK Reference” section.

The symbol structure for options and futures options is somewhat complex, so you can use get_option_chain() and get_future_option_chain() to get the instruments for a specific underlying as explained below.

Alternatively, NestedOptionChain and NestedFutureOptionChain provide a structured way to fetch chain expirations and available strikes.

Each expiration contains a list of these strikes, which have the associated put and call symbols that can then be used to fetch option objects via Option.get_options() or converted to dxfeed symbols for use with the streamer via Option.occ_to_streamer_symbol().

Probably the most powerful tool available for instruments is the build_leg() function. This allows an instrument to be quickly converted into a tradeable ‘leg’, which by itself or together with other legs forms the basis for a trade. This makes placing new trades across a wide variety of instruments surprisingly simple:

That’s it! We just sold a micro crude oil futures strangle in a few lines of code. Note that price is per quantity, not the price for the entire order! So if the legs looked like this:

the price would still be Decimal('1.25'), and the total credit collected would be $2.50. This holds true for ratio spreads, so a 4:2 ratio spread should be priced as a 2:1 ratio spread.

**Examples:**

Example 1 (swift):
```swift
from tastytrade.instruments import Equity, FutureOption

equities = Equity.get(session, ['SPY', 'AAPL'])
print(equities[0].is_etf, equities[0].description)
future_option = FutureOption.get(session, './GCJ4 OG4G4 240223P1915')
print(future_option.exchange)
```

Example 2 (unknown):
```unknown
>>> (False, 'APPLE INC')
>>> 'CME'
```

Example 3 (swift):
```swift
from tastytrade.instruments import get_option_chain, get_future_option_chain
from tastytrade.utils import get_tasty_monthly

chain = get_option_chain(session, 'SPLG')
exp = get_tasty_monthly()  # 45 DTE expiration!
print(chain[exp][0])
future_chain = get_future_option_chain(session, '/MCL')
print(future_chain.keys())  # print all expirations
```

Example 4 (rust):
```rust
>>> instrument_type=<InstrumentType.EQUITY_OPTION: 'Equity Option'> symbol='SPLG  240315C00024000' active=True strike_price=Decimal('24.0') root_symbol='SPLG' underlying_symbol='SPLG' expiration_date=datetime.date(2024, 3, 15) exercise_style='American' shares_per_contract=100 option_type=<OptionType.CALL: 'C'> option_chain_type='Standard' expiration_type='Regular' settlement_type='PM' stops_trading_at=datetime.datetime(2024, 3, 15, 20, 0, tzinfo=datetime.timezone.utc) market_time_instrument_collection='Equity Option' days_to_expiration=38 expires_at=datetime.datetime(2024, 3, 15, 20, 0, tzinfo=datetime.timezone.utc) is_closing_only=False listed_market=None halted_at=None old_security_number=None streamer_symbol='.SPLG240315C24'
>>> dict_keys([datetime.date(2024, 7, 17), datetime.date(2024, 6, 14), datetime.date(2024, 9, 17), datetime.date(2024, 11, 15), datetime.date(2024, 12, 16), datetime.date(2024, 2, 9), datetime.date(2024, 5, 16), datetime.date(2025, 1, 15), datetime.date(2024, 8, 15), datetime.date(2024, 2, 16), datetime.date(2024, 2, 14), datetime.date(2024, 10, 17), datetime.date(2024, 4, 17), datetime.date(2024, 3, 15)])
```

---

## tastytrade.session - tastytrade 11.1.0 documentation

**URL:** https://tastyworks-api.readthedocs.io/en/latest/api/session.html

**Contents:**
- tastytrade.session¶

Bases: TastytradeData

Dataclass containing customer address information.

Show JSON schema{ "title": "Address", "description": "Dataclass containing customer address information.", "type": "object", "properties": { "city": { "title": "City", "type": "string" }, "country": { "title": "Country", "type": "string" }, "is-domestic": { "title": "Is-Domestic", "type": "boolean" }, "is-foreign": { "title": "Is-Foreign", "type": "boolean" }, "postal-code": { "title": "Postal-Code", "type": "string" }, "state-region": { "title": "State-Region", "type": "string" }, "street-one": { "title": "Street-One", "type": "string" }, "street-two": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Street-Two" }, "street-three": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Street-Three" } }, "required": [ "city", "country", "is-domestic", "is-foreign", "postal-code", "state-region", "street-one" ] }

street_three (str | None)

street_two (str | None)

Bases: TastytradeData

Dataclass containing customer information.

Show JSON schema{ "title": "Customer", "description": "Dataclass containing customer information.", "type": "object", "properties": { "id": { "title": "Id", "type": "string" }, "first-name": { "title": "First-Name", "type": "string" }, "first-surname": { "title": "First-Surname", "type": "string" }, "last-name": { "title": "Last-Name", "type": "string" }, "address": { "$ref": "#/$defs/Address" }, "customer-suitability": { "$ref": "#/$defs/CustomerSuitability" }, "mailing-address": { "$ref": "#/$defs/Address" }, "is-foreign": { "title": "Is-Foreign", "type": "boolean" }, "regulatory-domain": { "title": "Regulatory-Domain", "type": "string" }, "usa-citizenship-type": { "title": "Usa-Citizenship-Type", "type": "string" }, "home-phone-number": { "title": "Home-Phone-Number", "type": "string" }, "mobile-phone-number": { "title": "Mobile-Phone-Number", "type": "string" }, "work-phone-number": { "title": "Work-Phone-Number", "type": "string" }, "birth-date": { "format": "date", "title": "Birth-Date", "type": "string" }, "email": { "title": "Email", "type": "string" }, "external-id": { "title": "External-Id", "type": "string" }, "tax-number": { "title": "Tax-Number", "type": "string" }, "tax-number-type": { "title": "Tax-Number-Type", "type": "string" }, "citizenship-country": { "title": "Citizenship-Country", "type": "string" }, "agreed-to-margining": { "title": "Agreed-To-Margining", "type": "boolean" }, "subject-to-tax-withholding": { "title": "Subject-To-Tax-Withholding", "type": "boolean" }, "agreed-to-terms": { "title": "Agreed-To-Terms", "type": "boolean" }, "ext-crm-id": { "title": "Ext-Crm-Id", "type": "string" }, "has-industry-affiliation": { "title": "Has-Industry-Affiliation", "type": "boolean" }, "has-listed-affiliation": { "title": "Has-Listed-Affiliation", "type": "boolean" }, "has-political-affiliation": { "title": "Has-Political-Affiliation", "type": "boolean" }, "has-delayed-quotes": { "title": "Has-Delayed-Quotes", "type": "boolean" }, "has-pending-or-approved-application": { "title": "Has-Pending-Or-Approved-Application", "type": "boolean" }, "is-professional": { "title": "Is-Professional", "type": "boolean" }, "permitted-account-types": { "items": { "$ref": "#/$defs/CustomerAccountType" }, "title": "Permitted-Account-Types", "type": "array" }, "created-at": { "format": "date-time", "title": "Created-At", "type": "string" }, "identifiable-type": { "title": "Identifiable-Type", "type": "string" }, "person": { "$ref": "#/$defs/CustomerPerson" }, "gender": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Gender" }, "middle-name": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Middle-Name" }, "prefix-name": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Prefix-Name" }, "second-surname": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Second-Surname" }, "suffix-name": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Suffix-Name" }, "foreign-tax-number": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Foreign-Tax-Number" }, "birth-country": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Birth-Country" }, "visa-expiration-date": { "anyOf": [ { "format": "date", "type": "string" }, { "type": "null" } ], "default": null, "title": "Visa-Expiration-Date" }, "visa-type": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Visa-Type" }, "signature-of-agreement": { "anyOf": [ { "type": "boolean" }, { "type": "null" } ], "default": null, "title": "Signature-Of-Agreement" }, "desk-customer-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Desk-Customer-Id" }, "entity": { "anyOf": [ { "$ref": "#/$defs/CustomerEntity" }, { "type": "null" } ], "default": null }, "family-member-names": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Family-Member-Names" }, "has-institutional-assets": { "anyOf": [ { "type": "string" }, { "type": "boolean" }, { "type": "null" } ], "default": null, "title": "Has-Institutional-Assets" }, "industry-affiliation-firm": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Industry-Affiliation-Firm" }, "is-investment-adviser": { "anyOf": [ { "type": "boolean" }, { "type": "null" } ], "default": null, "title": "Is-Investment-Adviser" }, "listed-affiliation-symbol": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Listed-Affiliation-Symbol" }, "political-organization": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Political-Organization" }, "user-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "User-Id" } }, "$defs": { "Address": { "description": "Dataclass containing customer address information.", "properties": { "city": { "title": "City", "type": "string" }, "country": { "title": "Country", "type": "string" }, "is-domestic": { "title": "Is-Domestic", "type": "boolean" }, "is-foreign": { "title": "Is-Foreign", "type": "boolean" }, "postal-code": { "title": "Postal-Code", "type": "string" }, "state-region": { "title": "State-Region", "type": "string" }, "street-one": { "title": "Street-One", "type": "string" }, "street-two": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Street-Two" }, "street-three": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Street-Three" } }, "required": [ "city", "country", "is-domestic", "is-foreign", "postal-code", "state-region", "street-one" ], "title": "Address", "type": "object" }, "CustomerAccountMarginType": { "description": "Dataclass containing margin information for a customer account type.", "properties": { "name": { "title": "Name", "type": "string" }, "is-margin": { "title": "Is-Margin", "type": "boolean" } }, "required": [ "name", "is-margin" ], "title": "CustomerAccountMarginType", "type": "object" }, "CustomerAccountType": { "description": "Dataclass containing information for a type of customer account.", "properties": { "name": { "title": "Name", "type": "string" }, "description": { "title": "Description", "type": "string" }, "is-tax-advantaged": { "title": "Is-Tax-Advantaged", "type": "boolean" }, "is-publicly-available": { "title": "Is-Publicly-Available", "type": "boolean" }, "has-multiple-owners": { "title": "Has-Multiple-Owners", "type": "boolean" }, "margin-types": { "items": { "$ref": "#/$defs/CustomerAccountMarginType" }, "title": "Margin-Types", "type": "array" } }, "required": [ "name", "description", "is-tax-advantaged", "is-publicly-available", "has-multiple-owners", "margin-types" ], "title": "CustomerAccountType", "type": "object" }, "CustomerEntity": { "description": "Dataclass containing customer entity information.", "properties": { "id": { "title": "Id", "type": "string" }, "address": { "$ref": "#/$defs/Address" }, "business-nature": { "title": "Business-Nature", "type": "string" }, "email": { "title": "Email", "type": "string" }, "entity-officers": { "items": { "$ref": "#/$defs/EntityOfficer" }, "title": "Entity-Officers", "type": "array" }, "entity-suitability": { "$ref": "#/$defs/EntitySuitability" }, "entity-type": { "title": "Entity-Type", "type": "string" }, "foreign-institution": { "title": "Foreign-Institution", "type": "string" }, "grantor-birth-date": { "title": "Grantor-Birth-Date", "type": "string" }, "grantor-email": { "title": "Grantor-Email", "type": "string" }, "grantor-first-name": { "title": "Grantor-First-Name", "type": "string" }, "grantor-last-name": { "title": "Grantor-Last-Name", "type": "string" }, "grantor-middle-name": { "title": "Grantor-Middle-Name", "type": "string" }, "grantor-tax-number": { "title": "Grantor-Tax-Number", "type": "string" }, "has-foreign-bank-affiliation": { "title": "Has-Foreign-Bank-Affiliation", "type": "string" }, "has-foreign-institution-affiliation": { "title": "Has-Foreign-Institution-Affiliation", "type": "string" }, "is-domestic": { "title": "Is-Domestic", "type": "boolean" }, "legal-name": { "title": "Legal-Name", "type": "string" }, "phone-number": { "title": "Phone-Number", "type": "string" }, "tax-number": { "title": "Tax-Number", "type": "string" } }, "required": [ "id", "address", "business-nature", "email", "entity-officers", "entity-suitability", "entity-type", "foreign-institution", "grantor-birth-date", "grantor-email", "grantor-first-name", "grantor-last-name", "grantor-middle-name", "grantor-tax-number", "has-foreign-bank-affiliation", "has-foreign-institution-affiliation", "is-domestic", "legal-name", "phone-number", "tax-number" ], "title": "CustomerEntity", "type": "object" }, "CustomerPerson": { "description": "Dataclass containing customer person information.", "properties": { "external-id": { "title": "External-Id", "type": "string" }, "first-name": { "title": "First-Name", "type": "string" }, "last-name": { "title": "Last-Name", "type": "string" }, "citizenship-country": { "title": "Citizenship-Country", "type": "string" }, "usa-citizenship-type": { "title": "Usa-Citizenship-Type", "type": "string" }, "employment-status": { "title": "Employment-Status", "type": "string" }, "marital-status": { "title": "Marital-Status", "type": "string" }, "number-of-dependents": { "title": "Number-Of-Dependents", "type": "integer" }, "occupation": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Occupation" }, "middle-name": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Middle-Name" }, "prefix-name": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Prefix-Name" }, "suffix-name": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Suffix-Name" }, "birth-country": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Birth-Country" }, "birth-date": { "anyOf": [ { "format": "date", "type": "string" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Birth-Date" }, "visa-expiration-date": { "anyOf": [ { "format": "date", "type": "string" }, { "type": "null" } ], "default": null, "title": "Visa-Expiration-Date" }, "visa-type": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Visa-Type" }, "employer-name": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Employer-Name" }, "job-title": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Job-Title" } }, "required": [ "external-id", "first-name", "last-name", "citizenship-country", "usa-citizenship-type", "employment-status", "marital-status", "number-of-dependents" ], "title": "CustomerPerson", "type": "object" }, "CustomerSuitability": { "description": "Dataclass containing customer suitability information.", "properties": { "id": { "title": "Id", "type": "integer" }, "annual-net-income": { "title": "Annual-Net-Income", "type": "integer" }, "covered-options-trading-experience": { "title": "Covered-Options-Trading-Experience", "type": "string" }, "employment-status": { "title": "Employment-Status", "type": "string" }, "futures-trading-experience": { "title": "Futures-Trading-Experience", "type": "string" }, "liquid-net-worth": { "title": "Liquid-Net-Worth", "type": "integer" }, "marital-status": { "title": "Marital-Status", "type": "string" }, "net-worth": { "title": "Net-Worth", "type": "integer" }, "number-of-dependents": { "title": "Number-Of-Dependents", "type": "integer" }, "stock-trading-experience": { "title": "Stock-Trading-Experience", "type": "string" }, "uncovered-options-trading-experience": { "title": "Uncovered-Options-Trading-Experience", "type": "string" }, "customer-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Customer-Id" }, "employer-name": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Employer-Name" }, "job-title": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Job-Title" }, "occupation": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Occupation" }, "tax-bracket": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Tax-Bracket" } }, "required": [ "id", "annual-net-income", "covered-options-trading-experience", "employment-status", "futures-trading-experience", "liquid-net-worth", "marital-status", "net-worth", "number-of-dependents", "stock-trading-experience", "uncovered-options-trading-experience" ], "title": "CustomerSuitability", "type": "object" }, "EntityOfficer": { "description": "Dataclass containing entity officer information.", "properties": { "id": { "title": "Id", "type": "string" }, "external-id": { "title": "External-Id", "type": "string" }, "first-name": { "title": "First-Name", "type": "string" }, "last-name": { "title": "Last-Name", "type": "string" }, "middle-name": { "title": "Middle-Name", "type": "string" }, "prefix-name": { "title": "Prefix-Name", "type": "string" }, "suffix-name": { "title": "Suffix-Name", "type": "string" }, "address": { "$ref": "#/$defs/Address" }, "birth-country": { "title": "Birth-Country", "type": "string" }, "birth-date": { "format": "date", "title": "Birth-Date", "type": "string" }, "citizenship-country": { "title": "Citizenship-Country", "type": "string" }, "email": { "title": "Email", "type": "string" }, "employer-name": { "title": "Employer-Name", "type": "string" }, "employment-status": { "title": "Employment-Status", "type": "string" }, "home-phone-number": { "title": "Home-Phone-Number", "type": "string" }, "is-foreign": { "title": "Is-Foreign", "type": "boolean" }, "job-title": { "title": "Job-Title", "type": "string" }, "marital-status": { "title": "Marital-Status", "type": "string" }, "mobile-phone-number": { "title": "Mobile-Phone-Number", "type": "string" }, "number-of-dependents": { "title": "Number-Of-Dependents", "type": "integer" }, "occupation": { "title": "Occupation", "type": "string" }, "owner-of-record": { "title": "Owner-Of-Record", "type": "boolean" }, "relationship-to-entity": { "title": "Relationship-To-Entity", "type": "string" }, "tax-number": { "title": "Tax-Number", "type": "string" }, "tax-number-type": { "title": "Tax-Number-Type", "type": "string" }, "usa-citizenship-type": { "title": "Usa-Citizenship-Type", "type": "string" }, "visa-expiration-date": { "format": "date", "title": "Visa-Expiration-Date", "type": "string" }, "visa-type": { "title": "Visa-Type", "type": "string" }, "work-phone-number": { "title": "Work-Phone-Number", "type": "string" } }, "required": [ "id", "external-id", "first-name", "last-name", "middle-name", "prefix-name", "suffix-name", "address", "birth-country", "birth-date", "citizenship-country", "email", "employer-name", "employment-status", "home-phone-number", "is-foreign", "job-title", "marital-status", "mobile-phone-number", "number-of-dependents", "occupation", "owner-of-record", "relationship-to-entity", "tax-number", "tax-number-type", "usa-citizenship-type", "visa-expiration-date", "visa-type", "work-phone-number" ], "title": "EntityOfficer", "type": "object" }, "EntitySuitability": { "description": "Dataclass containing entity suitability information.", "properties": { "id": { "title": "Id", "type": "string" }, "annual-net-income": { "title": "Annual-Net-Income", "type": "integer" }, "covered-options-trading-experience": { "title": "Covered-Options-Trading-Experience", "type": "string" }, "entity-id": { "title": "Entity-Id", "type": "integer" }, "futures-trading-experience": { "title": "Futures-Trading-Experience", "type": "string" }, "liquid-net-worth": { "title": "Liquid-Net-Worth", "type": "integer" }, "net-worth": { "title": "Net-Worth", "type": "integer" }, "stock-trading-experience": { "title": "Stock-Trading-Experience", "type": "string" }, "tax-bracket": { "title": "Tax-Bracket", "type": "string" }, "uncovered-options-trading-experience": { "title": "Uncovered-Options-Trading-Experience", "type": "string" } }, "required": [ "id", "annual-net-income", "covered-options-trading-experience", "entity-id", "futures-trading-experience", "liquid-net-worth", "net-worth", "stock-trading-experience", "tax-bracket", "uncovered-options-trading-experience" ], "title": "EntitySuitability", "type": "object" } }, "required": [ "id", "first-name", "first-surname", "last-name", "address", "customer-suitability", "mailing-address", "is-foreign", "regulatory-domain", "usa-citizenship-type", "home-phone-number", "mobile-phone-number", "work-phone-number", "birth-date", "email", "external-id", "tax-number", "tax-number-type", "citizenship-country", "agreed-to-margining", "subject-to-tax-withholding", "agreed-to-terms", "ext-crm-id", "has-industry-affiliation", "has-listed-affiliation", "has-political-affiliation", "has-delayed-quotes", "has-pending-or-approved-application", "is-professional", "permitted-account-types", "created-at", "identifiable-type", "person" ] }

address (tastytrade.session.Address)

agreed_to_margining (bool)

agreed_to_terms (bool)

birth_country (str | None)

birth_date (datetime.date)

citizenship_country (str)

created_at (datetime.datetime)

customer_suitability (tastytrade.session.CustomerSuitability)

desk_customer_id (str | None)

entity (tastytrade.session.CustomerEntity | None)

family_member_names (str | None)

foreign_tax_number (str | None)

has_delayed_quotes (bool)

has_industry_affiliation (bool)

has_institutional_assets (str | bool | None)

has_listed_affiliation (bool)

has_pending_or_approved_application (bool)

has_political_affiliation (bool)

home_phone_number (str)

identifiable_type (str)

industry_affiliation_firm (str | None)

is_investment_adviser (bool | None)

is_professional (bool)

listed_affiliation_symbol (str | None)

mailing_address (tastytrade.session.Address)

middle_name (str | None)

mobile_phone_number (str)

permitted_account_types (list[tastytrade.session.CustomerAccountType])

person (tastytrade.session.CustomerPerson)

political_organization (str | None)

prefix_name (str | None)

regulatory_domain (str)

second_surname (str | None)

signature_of_agreement (bool | None)

subject_to_tax_withholding (bool)

suffix_name (str | None)

tax_number_type (str)

usa_citizenship_type (str)

visa_expiration_date (datetime.date | None)

visa_type (str | None)

work_phone_number (str)

Bases: TastytradeData

Dataclass containing margin information for a customer account type.

Show JSON schema{ "title": "CustomerAccountMarginType", "description": "Dataclass containing margin information for a customer account type.", "type": "object", "properties": { "name": { "title": "Name", "type": "string" }, "is-margin": { "title": "Is-Margin", "type": "boolean" } }, "required": [ "name", "is-margin" ] }

Bases: TastytradeData

Dataclass containing information for a type of customer account.

Show JSON schema{ "title": "CustomerAccountType", "description": "Dataclass containing information for a type of customer account.", "type": "object", "properties": { "name": { "title": "Name", "type": "string" }, "description": { "title": "Description", "type": "string" }, "is-tax-advantaged": { "title": "Is-Tax-Advantaged", "type": "boolean" }, "is-publicly-available": { "title": "Is-Publicly-Available", "type": "boolean" }, "has-multiple-owners": { "title": "Has-Multiple-Owners", "type": "boolean" }, "margin-types": { "items": { "$ref": "#/$defs/CustomerAccountMarginType" }, "title": "Margin-Types", "type": "array" } }, "$defs": { "CustomerAccountMarginType": { "description": "Dataclass containing margin information for a customer account type.", "properties": { "name": { "title": "Name", "type": "string" }, "is-margin": { "title": "Is-Margin", "type": "boolean" } }, "required": [ "name", "is-margin" ], "title": "CustomerAccountMarginType", "type": "object" } }, "required": [ "name", "description", "is-tax-advantaged", "is-publicly-available", "has-multiple-owners", "margin-types" ] }

has_multiple_owners (bool)

is_publicly_available (bool)

is_tax_advantaged (bool)

margin_types (list[tastytrade.session.CustomerAccountMarginType])

Bases: TastytradeData

Dataclass containing customer entity information.

Show JSON schema{ "title": "CustomerEntity", "description": "Dataclass containing customer entity information.", "type": "object", "properties": { "id": { "title": "Id", "type": "string" }, "address": { "$ref": "#/$defs/Address" }, "business-nature": { "title": "Business-Nature", "type": "string" }, "email": { "title": "Email", "type": "string" }, "entity-officers": { "items": { "$ref": "#/$defs/EntityOfficer" }, "title": "Entity-Officers", "type": "array" }, "entity-suitability": { "$ref": "#/$defs/EntitySuitability" }, "entity-type": { "title": "Entity-Type", "type": "string" }, "foreign-institution": { "title": "Foreign-Institution", "type": "string" }, "grantor-birth-date": { "title": "Grantor-Birth-Date", "type": "string" }, "grantor-email": { "title": "Grantor-Email", "type": "string" }, "grantor-first-name": { "title": "Grantor-First-Name", "type": "string" }, "grantor-last-name": { "title": "Grantor-Last-Name", "type": "string" }, "grantor-middle-name": { "title": "Grantor-Middle-Name", "type": "string" }, "grantor-tax-number": { "title": "Grantor-Tax-Number", "type": "string" }, "has-foreign-bank-affiliation": { "title": "Has-Foreign-Bank-Affiliation", "type": "string" }, "has-foreign-institution-affiliation": { "title": "Has-Foreign-Institution-Affiliation", "type": "string" }, "is-domestic": { "title": "Is-Domestic", "type": "boolean" }, "legal-name": { "title": "Legal-Name", "type": "string" }, "phone-number": { "title": "Phone-Number", "type": "string" }, "tax-number": { "title": "Tax-Number", "type": "string" } }, "$defs": { "Address": { "description": "Dataclass containing customer address information.", "properties": { "city": { "title": "City", "type": "string" }, "country": { "title": "Country", "type": "string" }, "is-domestic": { "title": "Is-Domestic", "type": "boolean" }, "is-foreign": { "title": "Is-Foreign", "type": "boolean" }, "postal-code": { "title": "Postal-Code", "type": "string" }, "state-region": { "title": "State-Region", "type": "string" }, "street-one": { "title": "Street-One", "type": "string" }, "street-two": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Street-Two" }, "street-three": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Street-Three" } }, "required": [ "city", "country", "is-domestic", "is-foreign", "postal-code", "state-region", "street-one" ], "title": "Address", "type": "object" }, "EntityOfficer": { "description": "Dataclass containing entity officer information.", "properties": { "id": { "title": "Id", "type": "string" }, "external-id": { "title": "External-Id", "type": "string" }, "first-name": { "title": "First-Name", "type": "string" }, "last-name": { "title": "Last-Name", "type": "string" }, "middle-name": { "title": "Middle-Name", "type": "string" }, "prefix-name": { "title": "Prefix-Name", "type": "string" }, "suffix-name": { "title": "Suffix-Name", "type": "string" }, "address": { "$ref": "#/$defs/Address" }, "birth-country": { "title": "Birth-Country", "type": "string" }, "birth-date": { "format": "date", "title": "Birth-Date", "type": "string" }, "citizenship-country": { "title": "Citizenship-Country", "type": "string" }, "email": { "title": "Email", "type": "string" }, "employer-name": { "title": "Employer-Name", "type": "string" }, "employment-status": { "title": "Employment-Status", "type": "string" }, "home-phone-number": { "title": "Home-Phone-Number", "type": "string" }, "is-foreign": { "title": "Is-Foreign", "type": "boolean" }, "job-title": { "title": "Job-Title", "type": "string" }, "marital-status": { "title": "Marital-Status", "type": "string" }, "mobile-phone-number": { "title": "Mobile-Phone-Number", "type": "string" }, "number-of-dependents": { "title": "Number-Of-Dependents", "type": "integer" }, "occupation": { "title": "Occupation", "type": "string" }, "owner-of-record": { "title": "Owner-Of-Record", "type": "boolean" }, "relationship-to-entity": { "title": "Relationship-To-Entity", "type": "string" }, "tax-number": { "title": "Tax-Number", "type": "string" }, "tax-number-type": { "title": "Tax-Number-Type", "type": "string" }, "usa-citizenship-type": { "title": "Usa-Citizenship-Type", "type": "string" }, "visa-expiration-date": { "format": "date", "title": "Visa-Expiration-Date", "type": "string" }, "visa-type": { "title": "Visa-Type", "type": "string" }, "work-phone-number": { "title": "Work-Phone-Number", "type": "string" } }, "required": [ "id", "external-id", "first-name", "last-name", "middle-name", "prefix-name", "suffix-name", "address", "birth-country", "birth-date", "citizenship-country", "email", "employer-name", "employment-status", "home-phone-number", "is-foreign", "job-title", "marital-status", "mobile-phone-number", "number-of-dependents", "occupation", "owner-of-record", "relationship-to-entity", "tax-number", "tax-number-type", "usa-citizenship-type", "visa-expiration-date", "visa-type", "work-phone-number" ], "title": "EntityOfficer", "type": "object" }, "EntitySuitability": { "description": "Dataclass containing entity suitability information.", "properties": { "id": { "title": "Id", "type": "string" }, "annual-net-income": { "title": "Annual-Net-Income", "type": "integer" }, "covered-options-trading-experience": { "title": "Covered-Options-Trading-Experience", "type": "string" }, "entity-id": { "title": "Entity-Id", "type": "integer" }, "futures-trading-experience": { "title": "Futures-Trading-Experience", "type": "string" }, "liquid-net-worth": { "title": "Liquid-Net-Worth", "type": "integer" }, "net-worth": { "title": "Net-Worth", "type": "integer" }, "stock-trading-experience": { "title": "Stock-Trading-Experience", "type": "string" }, "tax-bracket": { "title": "Tax-Bracket", "type": "string" }, "uncovered-options-trading-experience": { "title": "Uncovered-Options-Trading-Experience", "type": "string" } }, "required": [ "id", "annual-net-income", "covered-options-trading-experience", "entity-id", "futures-trading-experience", "liquid-net-worth", "net-worth", "stock-trading-experience", "tax-bracket", "uncovered-options-trading-experience" ], "title": "EntitySuitability", "type": "object" } }, "required": [ "id", "address", "business-nature", "email", "entity-officers", "entity-suitability", "entity-type", "foreign-institution", "grantor-birth-date", "grantor-email", "grantor-first-name", "grantor-last-name", "grantor-middle-name", "grantor-tax-number", "has-foreign-bank-affiliation", "has-foreign-institution-affiliation", "is-domestic", "legal-name", "phone-number", "tax-number" ] }

address (tastytrade.session.Address)

business_nature (str)

entity_officers (list[tastytrade.session.EntityOfficer])

entity_suitability (tastytrade.session.EntitySuitability)

foreign_institution (str)

grantor_birth_date (str)

grantor_first_name (str)

grantor_last_name (str)

grantor_middle_name (str)

grantor_tax_number (str)

has_foreign_bank_affiliation (str)

has_foreign_institution_affiliation (str)

Bases: TastytradeData

Dataclass containing customer person information.

Show JSON schema{ "title": "CustomerPerson", "description": "Dataclass containing customer person information.", "type": "object", "properties": { "external-id": { "title": "External-Id", "type": "string" }, "first-name": { "title": "First-Name", "type": "string" }, "last-name": { "title": "Last-Name", "type": "string" }, "citizenship-country": { "title": "Citizenship-Country", "type": "string" }, "usa-citizenship-type": { "title": "Usa-Citizenship-Type", "type": "string" }, "employment-status": { "title": "Employment-Status", "type": "string" }, "marital-status": { "title": "Marital-Status", "type": "string" }, "number-of-dependents": { "title": "Number-Of-Dependents", "type": "integer" }, "occupation": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Occupation" }, "middle-name": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Middle-Name" }, "prefix-name": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Prefix-Name" }, "suffix-name": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Suffix-Name" }, "birth-country": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Birth-Country" }, "birth-date": { "anyOf": [ { "format": "date", "type": "string" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Birth-Date" }, "visa-expiration-date": { "anyOf": [ { "format": "date", "type": "string" }, { "type": "null" } ], "default": null, "title": "Visa-Expiration-Date" }, "visa-type": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Visa-Type" }, "employer-name": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Employer-Name" }, "job-title": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Job-Title" } }, "required": [ "external-id", "first-name", "last-name", "citizenship-country", "usa-citizenship-type", "employment-status", "marital-status", "number-of-dependents" ] }

birth_country (str | None)

birth_date (datetime.date | str | None)

citizenship_country (str)

employer_name (str | None)

employment_status (str)

job_title (str | None)

middle_name (str | None)

number_of_dependents (int)

occupation (str | None)

prefix_name (str | None)

suffix_name (str | None)

usa_citizenship_type (str)

visa_expiration_date (datetime.date | None)

visa_type (str | None)

Bases: TastytradeData

Dataclass containing customer suitability information.

Show JSON schema{ "title": "CustomerSuitability", "description": "Dataclass containing customer suitability information.", "type": "object", "properties": { "id": { "title": "Id", "type": "integer" }, "annual-net-income": { "title": "Annual-Net-Income", "type": "integer" }, "covered-options-trading-experience": { "title": "Covered-Options-Trading-Experience", "type": "string" }, "employment-status": { "title": "Employment-Status", "type": "string" }, "futures-trading-experience": { "title": "Futures-Trading-Experience", "type": "string" }, "liquid-net-worth": { "title": "Liquid-Net-Worth", "type": "integer" }, "marital-status": { "title": "Marital-Status", "type": "string" }, "net-worth": { "title": "Net-Worth", "type": "integer" }, "number-of-dependents": { "title": "Number-Of-Dependents", "type": "integer" }, "stock-trading-experience": { "title": "Stock-Trading-Experience", "type": "string" }, "uncovered-options-trading-experience": { "title": "Uncovered-Options-Trading-Experience", "type": "string" }, "customer-id": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Customer-Id" }, "employer-name": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Employer-Name" }, "job-title": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Job-Title" }, "occupation": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Occupation" }, "tax-bracket": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Tax-Bracket" } }, "required": [ "id", "annual-net-income", "covered-options-trading-experience", "employment-status", "futures-trading-experience", "liquid-net-worth", "marital-status", "net-worth", "number-of-dependents", "stock-trading-experience", "uncovered-options-trading-experience" ] }

annual_net_income (int)

covered_options_trading_experience (str)

customer_id (str | None)

employer_name (str | None)

employment_status (str)

futures_trading_experience (str)

job_title (str | None)

liquid_net_worth (int)

number_of_dependents (int)

occupation (str | None)

stock_trading_experience (str)

tax_bracket (str | None)

uncovered_options_trading_experience (str)

Bases: TastytradeData

Dataclass containing entity officer information.

Show JSON schema{ "title": "EntityOfficer", "description": "Dataclass containing entity officer information.", "type": "object", "properties": { "id": { "title": "Id", "type": "string" }, "external-id": { "title": "External-Id", "type": "string" }, "first-name": { "title": "First-Name", "type": "string" }, "last-name": { "title": "Last-Name", "type": "string" }, "middle-name": { "title": "Middle-Name", "type": "string" }, "prefix-name": { "title": "Prefix-Name", "type": "string" }, "suffix-name": { "title": "Suffix-Name", "type": "string" }, "address": { "$ref": "#/$defs/Address" }, "birth-country": { "title": "Birth-Country", "type": "string" }, "birth-date": { "format": "date", "title": "Birth-Date", "type": "string" }, "citizenship-country": { "title": "Citizenship-Country", "type": "string" }, "email": { "title": "Email", "type": "string" }, "employer-name": { "title": "Employer-Name", "type": "string" }, "employment-status": { "title": "Employment-Status", "type": "string" }, "home-phone-number": { "title": "Home-Phone-Number", "type": "string" }, "is-foreign": { "title": "Is-Foreign", "type": "boolean" }, "job-title": { "title": "Job-Title", "type": "string" }, "marital-status": { "title": "Marital-Status", "type": "string" }, "mobile-phone-number": { "title": "Mobile-Phone-Number", "type": "string" }, "number-of-dependents": { "title": "Number-Of-Dependents", "type": "integer" }, "occupation": { "title": "Occupation", "type": "string" }, "owner-of-record": { "title": "Owner-Of-Record", "type": "boolean" }, "relationship-to-entity": { "title": "Relationship-To-Entity", "type": "string" }, "tax-number": { "title": "Tax-Number", "type": "string" }, "tax-number-type": { "title": "Tax-Number-Type", "type": "string" }, "usa-citizenship-type": { "title": "Usa-Citizenship-Type", "type": "string" }, "visa-expiration-date": { "format": "date", "title": "Visa-Expiration-Date", "type": "string" }, "visa-type": { "title": "Visa-Type", "type": "string" }, "work-phone-number": { "title": "Work-Phone-Number", "type": "string" } }, "$defs": { "Address": { "description": "Dataclass containing customer address information.", "properties": { "city": { "title": "City", "type": "string" }, "country": { "title": "Country", "type": "string" }, "is-domestic": { "title": "Is-Domestic", "type": "boolean" }, "is-foreign": { "title": "Is-Foreign", "type": "boolean" }, "postal-code": { "title": "Postal-Code", "type": "string" }, "state-region": { "title": "State-Region", "type": "string" }, "street-one": { "title": "Street-One", "type": "string" }, "street-two": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Street-Two" }, "street-three": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Street-Three" } }, "required": [ "city", "country", "is-domestic", "is-foreign", "postal-code", "state-region", "street-one" ], "title": "Address", "type": "object" } }, "required": [ "id", "external-id", "first-name", "last-name", "middle-name", "prefix-name", "suffix-name", "address", "birth-country", "birth-date", "citizenship-country", "email", "employer-name", "employment-status", "home-phone-number", "is-foreign", "job-title", "marital-status", "mobile-phone-number", "number-of-dependents", "occupation", "owner-of-record", "relationship-to-entity", "tax-number", "tax-number-type", "usa-citizenship-type", "visa-expiration-date", "visa-type", "work-phone-number" ] }

address (tastytrade.session.Address)

birth_date (datetime.date)

citizenship_country (str)

employment_status (str)

home_phone_number (str)

mobile_phone_number (str)

number_of_dependents (int)

owner_of_record (bool)

relationship_to_entity (str)

tax_number_type (str)

usa_citizenship_type (str)

visa_expiration_date (datetime.date)

work_phone_number (str)

Bases: TastytradeData

Dataclass containing entity suitability information.

Show JSON schema{ "title": "EntitySuitability", "description": "Dataclass containing entity suitability information.", "type": "object", "properties": { "id": { "title": "Id", "type": "string" }, "annual-net-income": { "title": "Annual-Net-Income", "type": "integer" }, "covered-options-trading-experience": { "title": "Covered-Options-Trading-Experience", "type": "string" }, "entity-id": { "title": "Entity-Id", "type": "integer" }, "futures-trading-experience": { "title": "Futures-Trading-Experience", "type": "string" }, "liquid-net-worth": { "title": "Liquid-Net-Worth", "type": "integer" }, "net-worth": { "title": "Net-Worth", "type": "integer" }, "stock-trading-experience": { "title": "Stock-Trading-Experience", "type": "string" }, "tax-bracket": { "title": "Tax-Bracket", "type": "string" }, "uncovered-options-trading-experience": { "title": "Uncovered-Options-Trading-Experience", "type": "string" } }, "required": [ "id", "annual-net-income", "covered-options-trading-experience", "entity-id", "futures-trading-experience", "liquid-net-worth", "net-worth", "stock-trading-experience", "tax-bracket", "uncovered-options-trading-experience" ] }

annual_net_income (int)

covered_options_trading_experience (str)

futures_trading_experience (str)

liquid_net_worth (int)

stock_trading_experience (str)

uncovered_options_trading_experience (str)

Contains a managed user login which can then be used to interact with the remote API.

OAuth secret for your provider

refresh token for the user

whether to use the test API endpoints, default False

if provided, all requests will be made through this proxy, as well as web socket connections for streamers.

Gets the customer dict from the API.

Refreshes the acccess token using the stored refresh token. Also refreshes the streamer token if necessary.

Validates the current session by sending a request to the API.

httpx client for async requests

Create a new Session object from a serialized string.

Gets the customer dict from the API.

Whether this is a cert or real session

OAuth secret for your provider

Proxy URL to use for requests and web sockets

Refreshes the acccess token using the stored refresh token. Also refreshes the streamer token if necessary.

Refresh token for the user

Serializes the session to a string, useful for storing a session for later use. Could be used with pickle, Redis, etc.

expiration for streamer token

httpx client for sync requests

Validates the current session by sending a request to the API.

**Examples:**

Example 1 (json):
```json
{
   "title": "Address",
   "description": "Dataclass containing customer address information.",
   "type": "object",
   "properties": {
      "city": {
         "title": "City",
         "type": "string"
      },
      "country": {
         "title": "Country",
         "type": "string"
      },
      "is-domestic": {
         "title": "Is-Domestic",
         "type": "boolean"
      },
      "is-foreign": {
         "title": "Is-Foreign",
         "type": "boolean"
      },
      "postal-code": {
         "title": "Postal-Code",
         "type": "string"
      },
      "state-region": {
         "title": "State-Region",
         "type": "string"
      },
      "street-one": {
         "title": "Street-One",
         "type": "string"
      },
      "street-two": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Street-Two"
      },
      "street-three": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Street-Three"
      }
   },
   "required": [
      "city",
      "country",
      "is-domestic",
      "is-foreign",
      "postal-code",
      "state-region",
      "street-one"
   ]
}
```

Example 2 (json):
```json
{
   "title": "Customer",
   "description": "Dataclass containing customer information.",
   "type": "object",
   "properties": {
      "id": {
         "title": "Id",
         "type": "string"
      },
      "first-name": {
         "title": "First-Name",
         "type": "string"
      },
      "first-surname": {
         "title": "First-Surname",
         "type": "string"
      },
      "last-name": {
         "title": "Last-Name",
         "type": "string"
      },
      "address": {
         "$ref": "#/$defs/Address"
      },
      "customer-suitability": {
         "$ref": "#/$defs/CustomerSuitability"
      },
      "mailing-address": {
         "$ref": "#/$defs/Address"
      },
      "is-foreign": {
         "title": "Is-Foreign",
         "type": "boolean"
      },
      "regulatory-domain": {
         "title": "Regulatory-Domain",
         "type": "string"
      },
      "usa-citizenship-type": {
         "title": "Usa-Citizenship-Type",
         "type": "string"
      },
      "home-phone-number": {
         "title": "Home-Phone-Number",
         "type": "string"
      },
      "mobile-phone-number": {
         "title": "Mobile-Phone-Number",
         "type": "string"
      },
      "work-phone-number": {
         "title": "Work-Phone-Number",
         "type": "string"
      },
      "birth-date": {
         "format": "date",
         "title": "Birth-Date",
         "type": "string"
      },
      "email": {
         "title": "Email",
         "type": "string"
      },
      "external-id": {
         "title": "External-Id",
         "type": "string"
      },
      "tax-number": {
         "title": "Tax-Number",
         "type": "string"
      },
      "tax-number-type": {
         "title": "Tax-Number-Type",
         "type": "string"
      },
      "citizenship-country": {
         "title": "Citizenship-Country",
         "type": "string"
      },
      "agreed-to-margining": {
         "title": "Agreed-To-Margining",
         "type": "boolean"
      },
      "subject-to-tax-withholding": {
         "title": "Subject-To-Tax-Withholding",
         "type": "boolean"
      },
      "agreed-to-terms": {
         "title": "Agreed-To-Terms",
         "type": "boolean"
      },
      "ext-crm-id": {
         "title": "Ext-Crm-Id",
         "type": "string"
      },
      "has-industry-affiliation": {
         "title": "Has-Industry-Affiliation",
         "type": "boolean"
      },
      "has-listed-affiliation": {
         "title": "Has-Listed-Affiliation",
         "type": "boolean"
      },
      "has-political-affiliation": {
         "title": "Has-Political-Affiliation",
         "type": "boolean"
      },
      "has-delayed-quotes": {
         "title": "Has-Delayed-Quotes",
         "type": "boolean"
      },
      "has-pending-or-approved-application": {
         "title": "Has-Pending-Or-Approved-Application",
         "type": "boolean"
      },
      "is-professional": {
         "title": "Is-Professional",
         "type": "boolean"
      },
      "permitted-account-types": {
         "items": {
            "$ref": "#/$defs/CustomerAccountType"
         },
         "title": "Permitted-Account-Types",
         "type": "array"
      },
      "created-at": {
         "format": "date-time",
         "title": "Created-At",
         "type": "string"
      },
      "identifiable-type": {
         "title": "Identifiable-Type",
         "type": "string"
      },
      "person": {
         "$ref": "#/$defs/CustomerPerson"
      },
      "gender": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Gender"
      },
      "middle-name": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Middle-Name"
      },
      "prefix-name": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Prefix-Name"
      },
      "second-surname": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Second-Surname"
      },
      "suffix-name": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Suffix-Name"
      },
      "foreign-tax-number": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Foreign-Tax-Number"
      },
      "birth-country": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Birth-Country"
      },
      "visa-expiration-date": {
         "anyOf": [
            {
               "format": "date",
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Visa-Expiration-Date"
      },
      "visa-type": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Visa-Type"
      },
      "signature-of-agreement": {
         "anyOf": [
            {
               "type": "boolean"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Signature-Of-Agreement"
      },
      "desk-customer-id": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Desk-Customer-Id"
      },
      "entity": {
         "anyOf": [
            {
               "$ref": "#/$defs/CustomerEntity"
            },
            {
               "type": "null"
            }
         ],
         "default": null
      },
      "family-member-names": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Family-Member-Names"
      },
      "has-institutional-assets": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "boolean"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Has-Institutional-Assets"
      },
      "industry-affiliation-firm": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Industry-Affiliation-Firm"
      },
      "is-investment-adviser": {
         "anyOf": [
            {
               "type": "boolean"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Is-Investment-Adviser"
      },
      "listed-affiliation-symbol": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Listed-Affiliation-Symbol"
      },
      "political-organization": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Political-Organization"
      },
      "user-id": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "User-Id"
      }
   },
   "$defs": {
      "Address": {
         "description": "Dataclass containing customer address information.",
         "properties": {
            "city": {
               "title": "City",
               "type": "string"
            },
            "country": {
               "title": "Country",
               "type": "string"
            },
            "is-domestic": {
               "title": "Is-Domestic",
               "type": "boolean"
            },
            "is-foreign": {
               "title": "Is-Foreign",
               "type": "boolean"
            },
            "postal-code": {
               "title": "Postal-Code",
               "type": "string"
            },
            "state-region": {
               "title": "State-Region",
               "type": "string"
            },
            "street-one": {
               "title": "Street-One",
               "type": "string"
            },
            "street-two": {
               "anyOf": [
                  {
                     "type": "string"
                  },
                  {
                     "type": "null"
                  }
               ],
               "default": null,
               "title": "Street-Two"
            },
            "street-three": {
               "anyOf": [
                  {
                     "type": "string"
                  },
                  {
                     "type": "null"
                  }
               ],
               "default": null,
               "title": "Street-Three"
            }
         },
         "required": [
            "city",
            "country",
            "is-domestic",
            "is-foreign",
            "postal-code",
            "state-region",
            "street-one"
         ],
         "title": "Address",
         "type": "object"
      },
      "CustomerAccountMarginType": {
         "description": "Dataclass containing margin information for a customer account type.",
         "properties": {
            "name": {
               "title": "Name",
               "type": "string"
            },
            "is-margin": {
               "title": "Is-Margin",
               "type": "boolean"
            }
         },
         "required": [
            "name",
            "is-margin"
         ],
         "title": "CustomerAccountMarginType",
         "type": "object"
      },
      "CustomerAccountType": {
         "description": "Dataclass containing information for a type of customer account.",
         "properties": {
            "name": {
               "title": "Name",
               "type": "string"
            },
            "description": {
               "title": "Description",
               "type": "string"
            },
            "is-tax-advantaged": {
               "title": "Is-Tax-Advantaged",
               "type": "boolean"
            },
            "is-publicly-available": {
               "title": "Is-Publicly-Available",
               "type": "boolean"
            },
            "has-multiple-owners": {
               "title": "Has-Multiple-Owners",
               "type": "boolean"
            },
            "margin-types": {
               "items": {
                  "$ref": "#/$defs/CustomerAccountMarginType"
               },
               "title": "Margin-Types",
               "type": "array"
            }
         },
         "required": [
            "name",
            "description",
            "is-tax-advantaged",
            "is-publicly-available",
            "has-multiple-owners",
            "margin-types"
         ],
         "title": "CustomerAccountType",
         "type": "object"
      },
      "CustomerEntity": {
         "description": "Dataclass containing customer entity information.",
         "properties": {
            "id": {
               "title": "Id",
               "type": "string"
            },
            "address": {
               "$ref": "#/$defs/Address"
            },
            "business-nature": {
               "title": "Business-Nature",
               "type": "string"
            },
            "email": {
               "title": "Email",
               "type": "string"
            },
            "entity-officers": {
               "items": {
                  "$ref": "#/$defs/EntityOfficer"
               },
               "title": "Entity-Officers",
               "type": "array"
            },
            "entity-suitability": {
               "$ref": "#/$defs/EntitySuitability"
            },
            "entity-type": {
               "title": "Entity-Type",
               "type": "string"
            },
            "foreign-institution": {
               "title": "Foreign-Institution",
               "type": "string"
            },
            "grantor-birth-date": {
               "title": "Grantor-Birth-Date",
               "type": "string"
            },
            "grantor-email": {
               "title": "Grantor-Email",
               "type": "string"
            },
            "grantor-first-name": {
               "title": "Grantor-First-Name",
               "type": "string"
            },
            "grantor-last-name": {
               "title": "Grantor-Last-Name",
               "type": "string"
            },
            "grantor-middle-name": {
               "title": "Grantor-Middle-Name",
               "type": "string"
            },
            "grantor-tax-number": {
               "title": "Grantor-Tax-Number",
               "type": "string"
            },
            "has-foreign-bank-affiliation": {
               "title": "Has-Foreign-Bank-Affiliation",
               "type": "string"
            },
            "has-foreign-institution-affiliation": {
               "title": "Has-Foreign-Institution-Affiliation",
               "type": "string"
            },
            "is-domestic": {
               "title": "Is-Domestic",
               "type": "boolean"
            },
            "legal-name": {
               "title": "Legal-Name",
               "type": "string"
            },
            "phone-number": {
               "title": "Phone-Number",
               "type": "string"
            },
            "tax-number": {
               "title": "Tax-Number",
               "type": "string"
            }
         },
         "required": [
            "id",
            "address",
            "business-nature",
            "email",
            "entity-officers",
            "entity-suitability",
            "entity-type",
            "foreign-institution",
            "grantor-birth-date",
            "grantor-email",
            "grantor-first-name",
            "grantor-last-name",
            "grantor-middle-name",
            "grantor-tax-number",
            "has-foreign-bank-affiliation",
            "has-foreign-institution-affiliation",
            "is-domestic",
            "legal-name",
            "phone-number",
            "tax-number"
         ],
         "title": "CustomerEntity",
         "type": "object"
      },
      "CustomerPerson": {
         "description": "Dataclass containing customer person information.",
         "properties": {
            "external-id": {
               "title": "External-Id",
               "type": "string"
            },
            "first-name": {
               "title": "First-Name",
               "type": "string"
            },
            "last-name": {
               "title": "Last-Name",
               "type": "string"
            },
            "citizenship-country": {
               "title": "Citizenship-Country",
               "type": "string"
            },
            "usa-citizenship-type": {
               "title": "Usa-Citizenship-Type",
               "type": "string"
            },
            "employment-status": {
               "title": "Employment-Status",
               "type": "string"
            },
            "marital-status": {
               "title": "Marital-Status",
               "type": "string"
            },
            "number-of-dependents": {
               "title": "Number-Of-Dependents",
               "type": "integer"
            },
            "occupation": {
               "anyOf": [
                  {
                     "type": "string"
                  },
                  {
                     "type": "null"
                  }
               ],
               "default": null,
               "title": "Occupation"
            },
            "middle-name": {
               "anyOf": [
                  {
                     "type": "string"
                  },
                  {
                     "type": "null"
                  }
               ],
               "default": null,
               "title": "Middle-Name"
            },
            "prefix-name": {
               "anyOf": [
                  {
                     "type": "string"
                  },
                  {
                     "type": "null"
                  }
               ],
               "default": null,
               "title": "Prefix-Name"
            },
            "suffix-name": {
               "anyOf": [
                  {
                     "type": "string"
                  },
                  {
                     "type": "null"
                  }
               ],
               "default": null,
               "title": "Suffix-Name"
            },
            "birth-country": {
               "anyOf": [
                  {
                     "type": "string"
                  },
                  {
                     "type": "null"
                  }
               ],
               "default": null,
               "title": "Birth-Country"
            },
            "birth-date": {
               "anyOf": [
                  {
                     "format": "date",
                     "type": "string"
                  },
                  {
                     "type": "string"
                  },
                  {
                     "type": "null"
                  }
               ],
               "default": null,
               "title": "Birth-Date"
            },
            "visa-expiration-date": {
               "anyOf": [
                  {
                     "format": "date",
                     "type": "string"
                  },
                  {
                     "type": "null"
                  }
               ],
               "default": null,
               "title": "Visa-Expiration-Date"
            },
            "visa-type": {
               "anyOf": [
                  {
                     "type": "string"
                  },
                  {
                     "type": "null"
                  }
               ],
               "default": null,
               "title": "Visa-Type"
            },
            "employer-name": {
               "anyOf": [
                  {
                     "type": "string"
                  },
                  {
                     "type": "null"
                  }
               ],
               "default": null,
               "title": "Employer-Name"
            },
            "job-title": {
               "anyOf": [
                  {
                     "type": "string"
                  },
                  {
                     "type": "null"
                  }
               ],
               "default": null,
               "title": "Job-Title"
            }
         },
         "required": [
            "external-id",
            "first-name",
            "last-name",
            "citizenship-country",
            "usa-citizenship-type",
            "employment-status",
            "marital-status",
            "number-of-dependents"
         ],
         "title": "CustomerPerson",
         "type": "object"
      },
      "CustomerSuitability": {
         "description": "Dataclass containing customer suitability information.",
         "properties": {
            "id": {
               "title": "Id",
               "type": "integer"
            },
            "annual-net-income": {
               "title": "Annual-Net-Income",
               "type": "integer"
            },
            "covered-options-trading-experience": {
               "title": "Covered-Options-Trading-Experience",
               "type": "string"
            },
            "employment-status": {
               "title": "Employment-Status",
               "type": "string"
            },
            "futures-trading-experience": {
               "title": "Futures-Trading-Experience",
               "type": "string"
            },
            "liquid-net-worth": {
               "title": "Liquid-Net-Worth",
               "type": "integer"
            },
            "marital-status": {
               "title": "Marital-Status",
               "type": "string"
            },
            "net-worth": {
               "title": "Net-Worth",
               "type": "integer"
            },
            "number-of-dependents": {
               "title": "Number-Of-Dependents",
               "type": "integer"
            },
            "stock-trading-experience": {
               "title": "Stock-Trading-Experience",
               "type": "string"
            },
            "uncovered-options-trading-experience": {
               "title": "Uncovered-Options-Trading-Experience",
               "type": "string"
            },
            "customer-id": {
               "anyOf": [
                  {
                     "type": "string"
                  },
                  {
                     "type": "null"
                  }
               ],
               "default": null,
               "title": "Customer-Id"
            },
            "employer-name": {
               "anyOf": [
                  {
                     "type": "string"
                  },
                  {
                     "type": "null"
                  }
               ],
               "default": null,
               "title": "Employer-Name"
            },
            "job-title": {
               "anyOf": [
                  {
                     "type": "string"
                  },
                  {
                     "type": "null"
                  }
               ],
               "default": null,
               "title": "Job-Title"
            },
            "occupation": {
               "anyOf": [
                  {
                     "type": "string"
                  },
                  {
                     "type": "null"
                  }
               ],
               "default": null,
               "title": "Occupation"
            },
            "tax-bracket": {
               "anyOf": [
                  {
                     "type": "string"
                  },
                  {
                     "type": "null"
                  }
               ],
               "default": null,
               "title": "Tax-Bracket"
            }
         },
         "required": [
            "id",
            "annual-net-income",
            "covered-options-trading-experience",
            "employment-status",
            "futures-trading-experience",
            "liquid-net-worth",
            "marital-status",
            "net-worth",
            "number-of-dependents",
            "stock-trading-experience",
            "uncovered-options-trading-experience"
         ],
         "title": "CustomerSuitability",
         "type": "object"
      },
      "EntityOfficer": {
         "description": "Dataclass containing entity officer information.",
         "properties": {
            "id": {
               "title": "Id",
               "type": "string"
            },
            "external-id": {
               "title": "External-Id",
               "type": "string"
            },
            "first-name": {
               "title": "First-Name",
               "type": "string"
            },
            "last-name": {
               "title": "Last-Name",
               "type": "string"
            },
            "middle-name": {
               "title": "Middle-Name",
               "type": "string"
            },
            "prefix-name": {
               "title": "Prefix-Name",
               "type": "string"
            },
            "suffix-name": {
               "title": "Suffix-Name",
               "type": "string"
            },
            "address": {
               "$ref": "#/$defs/Address"
            },
            "birth-country": {
               "title": "Birth-Country",
               "type": "string"
            },
            "birth-date": {
               "format": "date",
               "title": "Birth-Date",
               "type": "string"
            },
            "citizenship-country": {
               "title": "Citizenship-Country",
               "type": "string"
            },
            "email": {
               "title": "Email",
               "type": "string"
            },
            "employer-name": {
               "title": "Employer-Name",
               "type": "string"
            },
            "employment-status": {
               "title": "Employment-Status",
               "type": "string"
            },
            "home-phone-number": {
               "title": "Home-Phone-Number",
               "type": "string"
            },
            "is-foreign": {
               "title": "Is-Foreign",
               "type": "boolean"
            },
            "job-title": {
               "title": "Job-Title",
               "type": "string"
            },
            "marital-status": {
               "title": "Marital-Status",
               "type": "string"
            },
            "mobile-phone-number": {
               "title": "Mobile-Phone-Number",
               "type": "string"
            },
            "number-of-dependents": {
               "title": "Number-Of-Dependents",
               "type": "integer"
            },
            "occupation": {
               "title": "Occupation",
               "type": "string"
            },
            "owner-of-record": {
               "title": "Owner-Of-Record",
               "type": "boolean"
            },
            "relationship-to-entity": {
               "title": "Relationship-To-Entity",
               "type": "string"
            },
            "tax-number": {
               "title": "Tax-Number",
               "type": "string"
            },
            "tax-number-type": {
               "title": "Tax-Number-Type",
               "type": "string"
            },
            "usa-citizenship-type": {
               "title": "Usa-Citizenship-Type",
               "type": "string"
            },
            "visa-expiration-date": {
               "format": "date",
               "title": "Visa-Expiration-Date",
               "type": "string"
            },
            "visa-type": {
               "title": "Visa-Type",
               "type": "string"
            },
            "work-phone-number": {
               "title": "Work-Phone-Number",
               "type": "string"
            }
         },
         "required": [
            "id",
            "external-id",
            "first-name",
            "last-name",
            "middle-name",
            "prefix-name",
            "suffix-name",
            "address",
            "birth-country",
            "birth-date",
            "citizenship-country",
            "email",
            "employer-name",
            "employment-status",
            "home-phone-number",
            "is-foreign",
            "job-title",
            "marital-status",
            "mobile-phone-number",
            "number-of-dependents",
            "occupation",
            "owner-of-record",
            "relationship-to-entity",
            "tax-number",
            "tax-number-type",
            "usa-citizenship-type",
            "visa-expiration-date",
            "visa-type",
            "work-phone-number"
         ],
         "title": "EntityOfficer",
         "type": "object"
      },
      "EntitySuitability": {
         "description": "Dataclass containing entity suitability information.",
         "properties": {
            "id": {
               "title": "Id",
               "type": "string"
            },
            "annual-net-income": {
               "title": "Annual-Net-Income",
               "type": "integer"
            },
            "covered-options-trading-experience": {
               "title": "Covered-Options-Trading-Experience",
               "type": "string"
            },
            "entity-id": {
               "title": "Entity-Id",
               "type": "integer"
            },
            "futures-trading-experience": {
               "title": "Futures-Trading-Experience",
               "type": "string"
            },
            "liquid-net-worth": {
               "title": "Liquid-Net-Worth",
               "type": "integer"
            },
            "net-worth": {
               "title": "Net-Worth",
               "type": "integer"
            },
            "stock-trading-experience": {
               "title": "Stock-Trading-Experience",
               "type": "string"
            },
            "tax-bracket": {
               "title": "Tax-Bracket",
               "type": "string"
            },
            "uncovered-options-trading-experience": {
               "title": "Uncovered-Options-Trading-Experience",
               "type": "string"
            }
         },
         "required": [
            "id",
            "annual-net-income",
            "covered-options-trading-experience",
            "entity-id",
            "futures-trading-experience",
            "liquid-net-worth",
            "net-worth",
            "stock-trading-experience",
            "tax-bracket",
            "uncovered-options-trading-experience"
         ],
         "title": "EntitySuitability",
         "type": "object"
      }
   },
   "required": [
      "id",
      "first-name",
      "first-surname",
      "last-name",
      "address",
      "customer-suitability",
      "mailing-address",
      "is-foreign",
      "regulatory-domain",
      "usa-citizenship-type",
      "home-phone-number",
      "mobile-phone-number",
      "work-phone-number",
      "birth-date",
      "email",
      "external-id",
      "tax-number",
      "tax-number-type",
      "citizenship-country",
      "agreed-to-margining",
      "subject-to-tax-withholding",
      "agreed-to-terms",
      "ext-crm-id",
      "has-industry-affiliation",
      "has-listed-affiliation",
      "has-political-affiliation",
      "has-delayed-quotes",
      "has-pending-or-approved-application",
      "is-professional",
      "permitted-account-types",
      "created-at",
      "identifiable-type",
      "person"
   ]
}
```

Example 3 (json):
```json
{
   "title": "CustomerAccountMarginType",
   "description": "Dataclass containing margin information for a customer account type.",
   "type": "object",
   "properties": {
      "name": {
         "title": "Name",
         "type": "string"
      },
      "is-margin": {
         "title": "Is-Margin",
         "type": "boolean"
      }
   },
   "required": [
      "name",
      "is-margin"
   ]
}
```

Example 4 (json):
```json
{
   "title": "CustomerAccountType",
   "description": "Dataclass containing information for a type of customer account.",
   "type": "object",
   "properties": {
      "name": {
         "title": "Name",
         "type": "string"
      },
      "description": {
         "title": "Description",
         "type": "string"
      },
      "is-tax-advantaged": {
         "title": "Is-Tax-Advantaged",
         "type": "boolean"
      },
      "is-publicly-available": {
         "title": "Is-Publicly-Available",
         "type": "boolean"
      },
      "has-multiple-owners": {
         "title": "Has-Multiple-Owners",
         "type": "boolean"
      },
      "margin-types": {
         "items": {
            "$ref": "#/$defs/CustomerAccountMarginType"
         },
         "title": "Margin-Types",
         "type": "array"
      }
   },
   "$defs": {
      "CustomerAccountMarginType": {
         "description": "Dataclass containing margin information for a customer account type.",
         "properties": {
            "name": {
               "title": "Name",
               "type": "string"
            },
            "is-margin": {
               "title": "Is-Margin",
               "type": "boolean"
            }
         },
         "required": [
            "name",
            "is-margin"
         ],
         "title": "CustomerAccountMarginType",
         "type": "object"
      }
   },
   "required": [
      "name",
      "description",
      "is-tax-advantaged",
      "is-publicly-available",
      "has-multiple-owners",
      "margin-types"
   ]
}
```

---

## Accounts - tastytrade 11.1.0 documentation

**URL:** https://tastyworks-api.readthedocs.io/en/latest/accounts.html

**Contents:**
- Accounts¶

An account object contains information about a specific Tastytrade account. It can be used to place trades, monitor profit/loss, and analyze positions.

The easiest way to get an account is to grab all accounts associated with a specific session:

You can also get a specific account by its unique ID:

The get_balances function can be used to obtain information about the current buying power and cash balance:

To obtain information about current positions:

To fetch a list of past transactions:

We can also view portfolio P/L over time (and even plot it!):

Accounts are needed to place, replace, and delete orders. See more in Orders.

There are many more things you can do with an Account object–check out the SDK Reference section!

**Examples:**

Example 1 (python):
```python
from tastytrade import Account
accounts = Account.get(session)
```

Example 2 (unknown):
```unknown
account = Account.get(session, '5WX01234')
```

Example 3 (swift):
```swift
balance = account.get_balances(session)
print(balance)
```

Example 4 (rust):
```rust
>>> AccountBalance(account_number='5WX01234', cash_balance=Decimal('87.055'), long_equity_value=Decimal('4046.05'), short_equity_value=Decimal('0.0'), long_derivative_value=Decimal('0.0'), short_derivative_value=Decimal('0.0'), long_futures_value=Decimal('0.0'), short_futures_value=Decimal('0.0'), long_futures_derivative_value=Decimal('0.0'), short_futures_derivative_value=Decimal('0.0'), long_margineable_value=Decimal('0.0'), short_margineable_value=Decimal('0.0'), margin_equity=Decimal('4133.105'), equity_buying_power=Decimal('87.055'), derivative_buying_power=Decimal('87.055'), day_trading_buying_power=Decimal('0.0'), futures_margin_requirement=Decimal('0.0'), available_trading_funds=Decimal('0.0'), maintenance_requirement=Decimal('4048.85'), maintenance_call_value=Decimal('0.0'), reg_t_call_value=Decimal('0.0'), day_trading_call_value=Decimal('0.0'), day_equity_call_value=Decimal('0.0'), net_liquidating_value=Decimal('4133.105'), cash_available_to_withdraw=Decimal('87.06'), day_trade_excess=Decimal('87.06'), pending_cash=Decimal('0.0'), pending_cash_effect=<PriceEffect.NONE: 'None'>, long_cryptocurrency_value=Decimal('0.0'), short_cryptocurrency_value=Decimal('0.0'), cryptocurrency_margin_requirement=Decimal('0.0'), unsettled_cryptocurrency_fiat_amount=Decimal('0.0'), unsettled_cryptocurrency_fiat_effect=<PriceEffect.NONE: 'None'>, closed_loop_available_balance=Decimal('87.06'), equity_offering_margin_requirement=Decimal('0.0'), long_bond_value=Decimal('0.0'), bond_margin_requirement=Decimal('0.0'), snapshot_date=datetime.date(2023, 11, 28), reg_t_margin_requirement=Decimal('4048.85'), futures_overnight_margin_requirement=Decimal('0.0'), futures_intraday_margin_requirement=Decimal('0.0'), maintenance_excess=Decimal('87.055'), pending_margin_interest=Decimal('0.0'), effective_cryptocurrency_buying_power=Decimal('87.055'), updated_at=datetime.datetime(2023, 11, 28, 20, 54, 33, 556000, tzinfo=datetime.timezone.utc), apex_starting_day_margin_equity=None, buying_power_adjustment=None, buying_power_adjustment_effect=None, time_of_day=None)
```

---

## Data Streamer - tastytrade 11.1.0 documentation

**URL:** https://tastyworks-api.readthedocs.io/en/latest/data-streamer.html

**Contents:**
- Data Streamer¶
- Basic usage¶
- Advanced usage¶
- Disconnect callback¶
- Retry callback¶

The streamer is a websocket connection to dxfeed (the Tastytrade data provider) that allows you to subscribe to real-time data for quotes, greeks, and more. You can create a streamer using an active production session:

Or, you can create a streamer using an asynchronous context manager:

Once you’ve created the streamer, you can subscribe/unsubscribe to events, like Quote:

Note that these are asyncio calls, so you’ll need to run this code asynchronously. Here’s an example:

Alternatively, you can do testing in a Jupyter notebook, which allows you to make async calls directly, or run a python shell like this: python -m asyncio.

We can also use the streamer to stream greeks for options symbols:

Since the streamer makes use of Python’s asyncio library, it’s not always straightforward to use; however, it’s very powerful. For example, we can use the streamer to create an option chain that will continuously update prices as new data arrives:

Now, we can access the quotes and greeks at any time, and they’ll be up-to-date with the live prices from the streamer:

The disconnect callback can be used to run arbitrary code when the websocket connection has been disconnected. This is useful for notification purposes in your application when you need high availability. The callback function should look something like this:

The requirements are that the first parameter be the DXLinkStreamer instance, and the function should be asynchronous. This callback can then be used when creating the streamer:

The data streamer has a special “callback” function which can be used to execute arbitrary code whenever the websocket reconnects. This is useful for re-subscribing to whatever events you wanted to subscribe to initially (in fact, you can probably use the same function/code you use when initializing the connection). The callback function should look something like this:

The requirements are that the first parameter be the DXLinkStreamer instance, and the function should be asynchronous. Other than that, you have the flexibility to decide what arguments you want to use. This callback can then be used when creating the streamer:

The reconnection uses websockets’ exponential backoff algorithm, which can be configured through environment variables here.

**Examples:**

Example 1 (python):
```python
from tastytrade import DXLinkStreamer
streamer = await DXLinkStreamer(session)
```

Example 2 (python):
```python
from tastytrade import DXLinkStreamer
async with DXLinkStreamer(session) as streamer:
    pass
```

Example 3 (swift):
```swift
from tastytrade.dxfeed import Quote
subs_list = ['SPY']  # you can add more symbols here!

async with DXLinkStreamer(session) as streamer:
    await streamer.subscribe(Quote, subs_list)
    quotes = {}
    async for quote in streamer.listen(Quote):
        quotes[quote.event_symbol] = quote
        if len(quotes) >= len(subs_list):
            break
    print(quotes)
```

Example 4 (unknown):
```unknown
>>> [{'SPY': Quote(event_symbol='SPY', event_time=0, sequence=0, time_nano_part=0, bid_time=0, bid_exchange_code='Q', bid_price=411.58, bid_size=400.0, ask_time=0, ask_exchange_code='Q', ask_price=411.6, ask_size=1313.0), 'SPX': Quote(event_symbol='SPX', event_time=0, sequence=0, time_nano_part=0, bid_time=0, bid_exchange_code='\x00', bid_price=4122.49, bid_size='NaN', ask_time=0, ask_exchange_code='\x00', ask_price=4123.65, ask_size='NaN')}]
```

---

## tastytrade 11.1.0 documentation

**URL:** https://tastyworks-api.readthedocs.io/en/latest/index.html

**Contents:**
- Tastytrade Python SDK¶
- Indices and tables¶

A simple, reverse-engineered, sync/async SDK for Tastytrade built on their (now mostly public) API. This will allow you to create trading algorithms for whatever strategies you may have quickly and painlessly in Python.

Want to see the SDK in action? Check out tastytrade-cli, a CLI for Tastytrade that showcases many of the SDK’s features.

Want to build an advanced trading system? Check out streaQ, an async job queuing library for Python that’s perfect for complex applications!

---

## tastytrade.market_data - tastytrade 11.1.0 documentation

**URL:** https://tastyworks-api.readthedocs.io/en/latest/api/market-data.html

**Contents:**
- tastytrade.market_data¶

Contains possible statuses for close prices.

Valid values are as follows:

Contains the valid exchanges to fetch data for.

Valid values are as follows:

Bases: TastytradeData

Dataclass containing information about an instrument.

Show JSON schema{ "title": "Instrument", "description": "Dataclass containing information about an instrument.", "type": "object", "properties": { "symbol": { "title": "Symbol", "type": "string" }, "instrument-type": { "$ref": "#/$defs/InstrumentType" }, "instrument-key": { "$ref": "#/$defs/InstrumentKey" }, "underlying-instrument": { "title": "Underlying-Instrument", "type": "string" }, "root-symbol": { "title": "Root-Symbol", "type": "string" }, "exchange": { "$ref": "#/$defs/ExchangeType" } }, "$defs": { "ExchangeType": { "description": "Contains the valid exchanges to fetch data for.", "enum": [ "CME", "CFE", "Equity", "Smalls", "CBOED", "Bond", "Cryptocurrency", "Equity Offering", "Unknown" ], "title": "ExchangeType", "type": "string" }, "InstrumentKey": { "description": "Dataclass containing an instrument key.", "properties": { "symbol": { "title": "Symbol", "type": "string" }, "instrument-type": { "$ref": "#/$defs/InstrumentType" } }, "required": [ "symbol", "instrument-type" ], "title": "InstrumentKey", "type": "object" }, "InstrumentType": { "description": "This is an :class:`~enum.Enum` that contains the valid types of instruments\nand their representation in the API.", "enum": [ "Bond", "Cryptocurrency", "Currency Pair", "Equity", "Equity Offering", "Equity Option", "Fixed Income Security", "Future", "Future Option", "Index", "Liquidity Pool", "Unknown", "Warrant" ], "title": "InstrumentType", "type": "string" } }, "required": [ "symbol", "instrument-type", "instrument-key", "underlying-instrument", "root-symbol", "exchange" ] }

exchange (tastytrade.market_data.ExchangeType)

instrument_key (tastytrade.market_data.InstrumentKey)

instrument_type (tastytrade.order.InstrumentType)

underlying_instrument (str)

Bases: TastytradeData

Dataclass containing an instrument key.

Show JSON schema{ "title": "InstrumentKey", "description": "Dataclass containing an instrument key.", "type": "object", "properties": { "symbol": { "title": "Symbol", "type": "string" }, "instrument-type": { "$ref": "#/$defs/InstrumentType" } }, "$defs": { "InstrumentType": { "description": "This is an :class:`~enum.Enum` that contains the valid types of instruments\nand their representation in the API.", "enum": [ "Bond", "Cryptocurrency", "Currency Pair", "Equity", "Equity Offering", "Equity Option", "Fixed Income Security", "Future", "Future Option", "Index", "Liquidity Pool", "Unknown", "Warrant" ], "title": "InstrumentType", "type": "string" } }, "required": [ "symbol", "instrument-type" ] }

instrument_type (tastytrade.order.InstrumentType)

Bases: TastytradeData

Dataclass containing life market data for a symbol.

Show JSON schema{ "title": "MarketData", "description": "Dataclass containing life market data for a symbol.", "type": "object", "properties": { "symbol": { "title": "Symbol", "type": "string" }, "instrument-type": { "$ref": "#/$defs/InstrumentType" }, "updated-at": { "format": "date-time", "title": "Updated-At", "type": "string" }, "bid-size": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Bid-Size" }, "ask-size": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Ask-Size" }, "mark": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Mark" }, "close-price-type": { "$ref": "#/$defs/ClosePriceType" }, "summary-date": { "format": "date", "title": "Summary-Date", "type": "string" }, "prev-close-date": { "format": "date", "title": "Prev-Close-Date", "type": "string" }, "prev-close-price-type": { "$ref": "#/$defs/ClosePriceType" }, "halt-start-time": { "title": "Halt-Start-Time", "type": "integer" }, "halt-end-time": { "title": "Halt-End-Time", "type": "integer" }, "ask": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Ask" }, "beta": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Beta" }, "bid": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Bid" }, "close": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Close" }, "day-open": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Day-Open" }, "day-high": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Day-High" }, "day-low": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Day-Low" }, "day-close": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Day-Close" }, "day-high-price": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Day-High-Price" }, "day-low-price": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Day-Low-Price" }, "dividend-amount": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Dividend-Amount" }, "dividend-frequency": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Dividend-Frequency" }, "high-limit-price": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "High-Limit-Price" }, "instrument": { "anyOf": [ { "$ref": "#/$defs/Instrument" }, { "type": "null" } ], "default": null }, "last": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Last" }, "last-mkt": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Last-Mkt" }, "last-ext": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Last-Ext" }, "last-trade-time": { "anyOf": [ { "type": "integer" }, { "type": "null" } ], "default": null, "title": "Last-Trade-Time" }, "low-limit-price": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Low-Limit-Price" }, "mid": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Mid" }, "open": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Open" }, "prev-close": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Prev-Close" }, "prev-day-close": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Prev-Day-Close" }, "trading-halted": { "anyOf": [ { "type": "boolean" }, { "type": "null" } ], "default": null, "title": "Trading-Halted" }, "trading-halted-reason": { "anyOf": [ { "type": "string" }, { "type": "null" } ], "default": null, "title": "Trading-Halted-Reason" }, "volume": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Volume" }, "year-low-price": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Year-Low-Price" }, "year-high-price": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Year-High-Price" }, "open-interest": { "anyOf": [ { "type": "number" }, { "type": "string" }, { "type": "null" } ], "default": null, "title": "Open-Interest" } }, "$defs": { "ClosePriceType": { "description": "Contains possible statuses for close prices.", "enum": [ "Final", "Indicative", "Preliminary", "Regular", "Unknown" ], "title": "ClosePriceType", "type": "string" }, "ExchangeType": { "description": "Contains the valid exchanges to fetch data for.", "enum": [ "CME", "CFE", "Equity", "Smalls", "CBOED", "Bond", "Cryptocurrency", "Equity Offering", "Unknown" ], "title": "ExchangeType", "type": "string" }, "Instrument": { "description": "Dataclass containing information about an instrument.", "properties": { "symbol": { "title": "Symbol", "type": "string" }, "instrument-type": { "$ref": "#/$defs/InstrumentType" }, "instrument-key": { "$ref": "#/$defs/InstrumentKey" }, "underlying-instrument": { "title": "Underlying-Instrument", "type": "string" }, "root-symbol": { "title": "Root-Symbol", "type": "string" }, "exchange": { "$ref": "#/$defs/ExchangeType" } }, "required": [ "symbol", "instrument-type", "instrument-key", "underlying-instrument", "root-symbol", "exchange" ], "title": "Instrument", "type": "object" }, "InstrumentKey": { "description": "Dataclass containing an instrument key.", "properties": { "symbol": { "title": "Symbol", "type": "string" }, "instrument-type": { "$ref": "#/$defs/InstrumentType" } }, "required": [ "symbol", "instrument-type" ], "title": "InstrumentKey", "type": "object" }, "InstrumentType": { "description": "This is an :class:`~enum.Enum` that contains the valid types of instruments\nand their representation in the API.", "enum": [ "Bond", "Cryptocurrency", "Currency Pair", "Equity", "Equity Offering", "Equity Option", "Fixed Income Security", "Future", "Future Option", "Index", "Liquidity Pool", "Unknown", "Warrant" ], "title": "InstrumentType", "type": "string" } }, "required": [ "symbol", "instrument-type", "updated-at", "bid-size", "ask-size", "mark", "close-price-type", "summary-date", "prev-close-date", "prev-close-price-type", "halt-start-time", "halt-end-time" ] }

ask (decimal.Decimal | None)

ask_size (decimal.Decimal)

beta (decimal.Decimal | None)

bid (decimal.Decimal | None)

bid_size (decimal.Decimal)

close (decimal.Decimal | None)

close_price_type (tastytrade.market_data.ClosePriceType)

day_close (decimal.Decimal | None)

day_high (decimal.Decimal | None)

day_high_price (decimal.Decimal | None)

day_low (decimal.Decimal | None)

day_low_price (decimal.Decimal | None)

day_open (decimal.Decimal | None)

dividend_amount (decimal.Decimal | None)

dividend_frequency (decimal.Decimal | None)

halt_start_time (int)

high_limit_price (decimal.Decimal | None)

instrument (tastytrade.market_data.Instrument | None)

instrument_type (tastytrade.order.InstrumentType)

last (decimal.Decimal | None)

last_ext (decimal.Decimal | None)

last_mkt (decimal.Decimal | None)

last_trade_time (int | None)

low_limit_price (decimal.Decimal | None)

mark (decimal.Decimal)

mid (decimal.Decimal | None)

open (decimal.Decimal | None)

open_interest (decimal.Decimal | None)

prev_close (decimal.Decimal | None)

prev_close_date (datetime.date)

prev_close_price_type (tastytrade.market_data.ClosePriceType)

prev_day_close (decimal.Decimal | None)

summary_date (datetime.date)

trading_halted (bool | None)

trading_halted_reason (str | None)

updated_at (datetime.datetime)

volume (decimal.Decimal | None)

year_high_price (decimal.Decimal | None)

year_low_price (decimal.Decimal | None)

Get market data for the given symbol.

active session to use

symbol to get data for

type of instrument for the symbol

Get market data for the given symbols grouped by instrument type. Combined limit across all types is 100.

active session to use

list of cryptocurrencies to fetch

list of equities to fetch

list of futures to fetch

list of future options to fetch

list of indices to fetch

list of options to fetch

Get market data for the given symbol.

active session to use

symbol to get data for

type of instrument for the symbol

Get market data for the given symbols grouped by instrument type. Combined limit across all types is 100.

active session to use

list of cryptocurrencies to fetch

list of equities to fetch

list of futures to fetch

list of future options to fetch

list of indices to fetch

list of options to fetch

**Examples:**

Example 1 (json):
```json
{
   "title": "Instrument",
   "description": "Dataclass containing information about an instrument.",
   "type": "object",
   "properties": {
      "symbol": {
         "title": "Symbol",
         "type": "string"
      },
      "instrument-type": {
         "$ref": "#/$defs/InstrumentType"
      },
      "instrument-key": {
         "$ref": "#/$defs/InstrumentKey"
      },
      "underlying-instrument": {
         "title": "Underlying-Instrument",
         "type": "string"
      },
      "root-symbol": {
         "title": "Root-Symbol",
         "type": "string"
      },
      "exchange": {
         "$ref": "#/$defs/ExchangeType"
      }
   },
   "$defs": {
      "ExchangeType": {
         "description": "Contains the valid exchanges to fetch data for.",
         "enum": [
            "CME",
            "CFE",
            "Equity",
            "Smalls",
            "CBOED",
            "Bond",
            "Cryptocurrency",
            "Equity Offering",
            "Unknown"
         ],
         "title": "ExchangeType",
         "type": "string"
      },
      "InstrumentKey": {
         "description": "Dataclass containing an instrument key.",
         "properties": {
            "symbol": {
               "title": "Symbol",
               "type": "string"
            },
            "instrument-type": {
               "$ref": "#/$defs/InstrumentType"
            }
         },
         "required": [
            "symbol",
            "instrument-type"
         ],
         "title": "InstrumentKey",
         "type": "object"
      },
      "InstrumentType": {
         "description": "This is an :class:`~enum.Enum` that contains the valid types of instruments\nand their representation in the API.",
         "enum": [
            "Bond",
            "Cryptocurrency",
            "Currency Pair",
            "Equity",
            "Equity Offering",
            "Equity Option",
            "Fixed Income Security",
            "Future",
            "Future Option",
            "Index",
            "Liquidity Pool",
            "Unknown",
            "Warrant"
         ],
         "title": "InstrumentType",
         "type": "string"
      }
   },
   "required": [
      "symbol",
      "instrument-type",
      "instrument-key",
      "underlying-instrument",
      "root-symbol",
      "exchange"
   ]
}
```

Example 2 (json):
```json
{
   "title": "InstrumentKey",
   "description": "Dataclass containing an instrument key.",
   "type": "object",
   "properties": {
      "symbol": {
         "title": "Symbol",
         "type": "string"
      },
      "instrument-type": {
         "$ref": "#/$defs/InstrumentType"
      }
   },
   "$defs": {
      "InstrumentType": {
         "description": "This is an :class:`~enum.Enum` that contains the valid types of instruments\nand their representation in the API.",
         "enum": [
            "Bond",
            "Cryptocurrency",
            "Currency Pair",
            "Equity",
            "Equity Offering",
            "Equity Option",
            "Fixed Income Security",
            "Future",
            "Future Option",
            "Index",
            "Liquidity Pool",
            "Unknown",
            "Warrant"
         ],
         "title": "InstrumentType",
         "type": "string"
      }
   },
   "required": [
      "symbol",
      "instrument-type"
   ]
}
```

Example 3 (json):
```json
{
   "title": "MarketData",
   "description": "Dataclass containing life market data for a symbol.",
   "type": "object",
   "properties": {
      "symbol": {
         "title": "Symbol",
         "type": "string"
      },
      "instrument-type": {
         "$ref": "#/$defs/InstrumentType"
      },
      "updated-at": {
         "format": "date-time",
         "title": "Updated-At",
         "type": "string"
      },
      "bid-size": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Bid-Size"
      },
      "ask-size": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Ask-Size"
      },
      "mark": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            }
         ],
         "title": "Mark"
      },
      "close-price-type": {
         "$ref": "#/$defs/ClosePriceType"
      },
      "summary-date": {
         "format": "date",
         "title": "Summary-Date",
         "type": "string"
      },
      "prev-close-date": {
         "format": "date",
         "title": "Prev-Close-Date",
         "type": "string"
      },
      "prev-close-price-type": {
         "$ref": "#/$defs/ClosePriceType"
      },
      "halt-start-time": {
         "title": "Halt-Start-Time",
         "type": "integer"
      },
      "halt-end-time": {
         "title": "Halt-End-Time",
         "type": "integer"
      },
      "ask": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Ask"
      },
      "beta": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Beta"
      },
      "bid": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Bid"
      },
      "close": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Close"
      },
      "day-open": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Day-Open"
      },
      "day-high": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Day-High"
      },
      "day-low": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Day-Low"
      },
      "day-close": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Day-Close"
      },
      "day-high-price": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Day-High-Price"
      },
      "day-low-price": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Day-Low-Price"
      },
      "dividend-amount": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Dividend-Amount"
      },
      "dividend-frequency": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Dividend-Frequency"
      },
      "high-limit-price": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "High-Limit-Price"
      },
      "instrument": {
         "anyOf": [
            {
               "$ref": "#/$defs/Instrument"
            },
            {
               "type": "null"
            }
         ],
         "default": null
      },
      "last": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Last"
      },
      "last-mkt": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Last-Mkt"
      },
      "last-ext": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Last-Ext"
      },
      "last-trade-time": {
         "anyOf": [
            {
               "type": "integer"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Last-Trade-Time"
      },
      "low-limit-price": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Low-Limit-Price"
      },
      "mid": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Mid"
      },
      "open": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Open"
      },
      "prev-close": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Prev-Close"
      },
      "prev-day-close": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Prev-Day-Close"
      },
      "trading-halted": {
         "anyOf": [
            {
               "type": "boolean"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Trading-Halted"
      },
      "trading-halted-reason": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Trading-Halted-Reason"
      },
      "volume": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Volume"
      },
      "year-low-price": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Year-Low-Price"
      },
      "year-high-price": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Year-High-Price"
      },
      "open-interest": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "title": "Open-Interest"
      }
   },
   "$defs": {
      "ClosePriceType": {
         "description": "Contains possible statuses for close prices.",
         "enum": [
            "Final",
            "Indicative",
            "Preliminary",
            "Regular",
            "Unknown"
         ],
         "title": "ClosePriceType",
         "type": "string"
      },
      "ExchangeType": {
         "description": "Contains the valid exchanges to fetch data for.",
         "enum": [
            "CME",
            "CFE",
            "Equity",
            "Smalls",
            "CBOED",
            "Bond",
            "Cryptocurrency",
            "Equity Offering",
            "Unknown"
         ],
         "title": "ExchangeType",
         "type": "string"
      },
      "Instrument": {
         "description": "Dataclass containing information about an instrument.",
         "properties": {
            "symbol": {
               "title": "Symbol",
               "type": "string"
            },
            "instrument-type": {
               "$ref": "#/$defs/InstrumentType"
            },
            "instrument-key": {
               "$ref": "#/$defs/InstrumentKey"
            },
            "underlying-instrument": {
               "title": "Underlying-Instrument",
               "type": "string"
            },
            "root-symbol": {
               "title": "Root-Symbol",
               "type": "string"
            },
            "exchange": {
               "$ref": "#/$defs/ExchangeType"
            }
         },
         "required": [
            "symbol",
            "instrument-type",
            "instrument-key",
            "underlying-instrument",
            "root-symbol",
            "exchange"
         ],
         "title": "Instrument",
         "type": "object"
      },
      "InstrumentKey": {
         "description": "Dataclass containing an instrument key.",
         "properties": {
            "symbol": {
               "title": "Symbol",
               "type": "string"
            },
            "instrument-type": {
               "$ref": "#/$defs/InstrumentType"
            }
         },
         "required": [
            "symbol",
            "instrument-type"
         ],
         "title": "InstrumentKey",
         "type": "object"
      },
      "InstrumentType": {
         "description": "This is an :class:`~enum.Enum` that contains the valid types of instruments\nand their representation in the API.",
         "enum": [
            "Bond",
            "Cryptocurrency",
            "Currency Pair",
            "Equity",
            "Equity Offering",
            "Equity Option",
            "Fixed Income Security",
            "Future",
            "Future Option",
            "Index",
            "Liquidity Pool",
            "Unknown",
            "Warrant"
         ],
         "title": "InstrumentType",
         "type": "string"
      }
   },
   "required": [
      "symbol",
      "instrument-type",
      "updated-at",
      "bid-size",
      "ask-size",
      "mark",
      "close-price-type",
      "summary-date",
      "prev-close-date",
      "prev-close-price-type",
      "halt-start-time",
      "halt-end-time"
   ]
}
```

---

## tastytrade.streamer - tastytrade 11.1.0 documentation

**URL:** https://tastyworks-api.readthedocs.io/en/latest/api/streamer.html

**Contents:**
- tastytrade.streamer¶

Used to subscribe to account-level updates (balances, orders, positions), public watchlist updates, quote alerts, and user-level messages. It should always be initialized as an async context manager, or by awaiting it, since the object cannot be fully instantiated without async.

The base url for the streamer websocket

Closes the websocket connection and cancels the pending tasks.

Variable number of arguments to pass to the reconnect function

An async function to be called upon disconnection. The first argument must be of type AlertStreamer and will be a reference to the streamer object.

Iterate over non-heartbeat messages received from the streamer, mapping them to their appropriate data class and yielding them.

This is designed to be friendly for type checking; the return type will be the same class you pass in.

the type of alert to listen for, should be of AlertType

The proxy URL, if any, associated with the session

Variable number of arguments to pass to the reconnect function

An async function to be called upon reconnection. The first argument must be of type AlertStreamer and will be a reference to the streamer object.

Counter used to track the request ID for the streamer

Subscribes to account-level updates (balances, orders, positions).

list of Account to subscribe to updates for

Subscribes to public watchlist updates.

Subscribes to quote alerts (which are configured at a user level).

The active session used to initiate the streamer or make requests

List of all possible types to stream with the alert streamer

A DXLinkStreamer object is used to fetch quotes or greeks for a given symbol or list of symbols. It should always be initialized as an async context manager, or by awaiting it, since the object cannot be fully instantiated without async.

Closes the websocket connection and cancels the heartbeat task.

Variable number of arguments to pass to the disconnect function

An async function to be called upon disconnection. The first argument must be of type DXLinkStreamer and will be a reference to the streamer object.

Using the existing subscription, pulls an event of the given type and returns it.

This is designed to be friendly for type checking; the return type will be the same class you pass in.

the type of alert to listen for, should be of EventType

Using the existing subscriptions, pulls an event of the given type and returns it. If the queue is empty None is returned.

This is designed to be friendly for type checking; the return type will be the same class you pass in.

the type of alert to listen for, should be of EventType

Using the existing subscriptions, pulls events of the given type and yield returns them. Never exits unless there’s an error or the channel is closed.

This is designed to be friendly for type checking; the return type will be the same class you pass in.

the type of alert to listen for, should be of EventType

The proxy URL, if any, associated with the session

Variable number of arguments to pass to the reconnect function

An async function to be called upon reconnection. The first argument must be of type DXLinkStreamer and will be a reference to the streamer object.

Subscribes to quotes for given list of symbols. Used for recurring data feeds. For candles, use subscribe_candle() instead.

type of subscription to add, should be of EventType

list of symbols to subscribe for

Time in seconds between fetching new events from dxfeed for this event type. You can try a higher value if processing quote updates quickly is not a high priority. Once refresh_interval is set for this event type and channel is opened, it cannot be changed later.

Subscribes to candle data for the given list of symbols.

list of symbols to get data for

the width of each candle in time, e.g. ’15s’, ‘5m’, ‘1h’, ‘3d’, ‘1w’, ‘1mo’

starting time for the data range

whether to include extended trading

Time in seconds between fetching new events from dxfeed for this event type. You can try a higher value if processing quote updates quickly is not a high priority. Once refresh_interval is set for this event type and channel is opened, it cannot be changed later.

Removes existing subscription for given list of symbols. For candles, use unsubscribe_candle() instead.

type of subscription to remove

list of symbols to unsubscribe from

Unsubscribes to all events of the given event type.

type of event to unsubscribe from.

Removes existing subscription for a candle.

symbol to unsubscribe from

candle width to unsubscribe from

whether candle to unsubscribe from contains extended trading hours

List of all possible types to stream with the data streamer

Bases: TastytradeData

Dataclass containing information on an external transaction (eg money movement).

Show JSON schema{ "title": "ExternalTransaction", "description": "Dataclass containing information on an external transaction (eg money movement).", "type": "object", "properties": { "id": { "title": "Id", "type": "integer" }, "account-number": { "title": "Account-Number", "type": "string" }, "amount": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Amount" }, "bank-account-type": { "title": "Bank-Account-Type", "type": "string" }, "banking-date": { "format": "date", "title": "Banking-Date", "type": "string" }, "created-at": { "format": "date-time", "title": "Created-At", "type": "string" }, "direction": { "title": "Direction", "type": "string" }, "disbursement-type": { "title": "Disbursement-Type", "type": "string" }, "ext-transfer-id": { "title": "Ext-Transfer-Id", "type": "string" }, "funds-available-date": { "format": "date", "title": "Funds-Available-Date", "type": "string" }, "is-cancelable": { "title": "Is-Cancelable", "type": "boolean" }, "is-clearing-accepted": { "title": "Is-Clearing-Accepted", "type": "boolean" }, "state": { "title": "State", "type": "string" }, "transfer-method": { "title": "Transfer-Method", "type": "string" }, "updated-at": { "format": "date-time", "title": "Updated-At", "type": "string" } }, "required": [ "id", "account-number", "amount", "bank-account-type", "banking-date", "created-at", "direction", "disbursement-type", "ext-transfer-id", "funds-available-date", "is-cancelable", "is-clearing-accepted", "state", "transfer-method", "updated-at" ] }

amount (decimal.Decimal)

bank_account_type (str)

banking_date (datetime.date)

created_at (datetime.datetime)

disbursement_type (str)

ext_transfer_id (str)

funds_available_date (datetime.date)

is_clearing_accepted (bool)

transfer_method (str)

updated_at (datetime.datetime)

Bases: TastytradeData

Dataclass that contains information about a quote alert

Show JSON schema{ "title": "QuoteAlert", "description": "Dataclass that contains information about a quote alert", "type": "object", "properties": { "user-external-id": { "title": "User-External-Id", "type": "string" }, "symbol": { "title": "Symbol", "type": "string" }, "alert-external-id": { "title": "Alert-External-Id", "type": "string" }, "expires-at": { "title": "Expires-At", "type": "integer" }, "completed-at": { "format": "date-time", "title": "Completed-At", "type": "string" }, "created-at": { "format": "date-time", "title": "Created-At", "type": "string" }, "triggered-at": { "format": "date-time", "title": "Triggered-At", "type": "string" }, "field": { "title": "Field", "type": "string" }, "operator": { "title": "Operator", "type": "string" }, "threshold": { "title": "Threshold", "type": "string" }, "threshold-numeric": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Threshold-Numeric" }, "dx-symbol": { "title": "Dx-Symbol", "type": "string" } }, "required": [ "user-external-id", "symbol", "alert-external-id", "expires-at", "completed-at", "created-at", "triggered-at", "field", "operator", "threshold", "threshold-numeric", "dx-symbol" ] }

alert_external_id (str)

completed_at (datetime.datetime)

created_at (datetime.datetime)

threshold_numeric (decimal.Decimal)

triggered_at (datetime.datetime)

user_external_id (str)

This is an Enum that contains the subscription types for the alert streamer.

Valid values are as follows:

Bases: TastytradeData

Dataclass that contains information about the yearly gain or loss for an underlying

Show JSON schema{ "title": "UnderlyingYearGainSummary", "description": "Dataclass that contains information about the yearly gain\nor loss for an underlying", "type": "object", "properties": { "year": { "title": "Year", "type": "integer" }, "account-number": { "title": "Account-Number", "type": "string" }, "symbol": { "title": "Symbol", "type": "string" }, "instrument-type": { "$ref": "#/$defs/InstrumentType" }, "fees": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Fees" }, "commissions": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Commissions" }, "yearly-realized-gain": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Yearly-Realized-Gain" }, "realized-lot-gain": { "anyOf": [ { "type": "number" }, { "type": "string" } ], "title": "Realized-Lot-Gain" } }, "$defs": { "InstrumentType": { "description": "This is an :class:`~enum.Enum` that contains the valid types of instruments\nand their representation in the API.", "enum": [ "Bond", "Cryptocurrency", "Currency Pair", "Equity", "Equity Offering", "Equity Option", "Fixed Income Security", "Future", "Future Option", "Index", "Liquidity Pool", "Unknown", "Warrant" ], "title": "InstrumentType", "type": "string" } }, "required": [ "year", "account-number", "symbol", "instrument-type", "fees", "commissions", "yearly-realized-gain", "realized-lot-gain" ] }

commissions (decimal.Decimal)

fees (decimal.Decimal)

instrument_type (tastytrade.order.InstrumentType)

realized_lot_gain (decimal.Decimal)

yearly_realized_gain (decimal.Decimal)

validate_price_effects » all fields

**Examples:**

Example 1 (python):
```python
from tastytrade import Account, AlertStreamer
from tastytrade.order import PlacedOrder

async with AlertStreamer(session) as streamer:
    accounts = Account.get_accounts(session)

    # updates to balances, orders, and positions
    await streamer.subscribe_accounts(accounts)
    # changes in public watchlists
    await streamer.subscribe_public_watchlists()
    # quote alerts configured by the user
    await streamer.subscribe_quote_alerts()

    async for order in streamer.listen(PlacedOrder):
        print(order)
```

Example 2 (swift):
```swift
streamer = await AlertStreamer(session)
```

Example 3 (python):
```python
from tastytrade import DXLinkStreamer
from tastytrade.dxfeed import Quote

# must be a production session
async with DXLinkStreamer(session) as streamer:
    subs = ['SPY']  # list of quotes to subscribe to
    await streamer.subscribe(Quote, subs)
    quote = await streamer.get_event(Quote)
    print(quote)
```

Example 4 (swift):
```swift
streamer = await DXLinkStreamer(session)
```

---

## tastytrade.utils - tastytrade 11.1.0 documentation

**URL:** https://tastyworks-api.readthedocs.io/en/latest/api/utils.html

**Contents:**
- tastytrade.utils¶

This is an Enum that shows the sign of a price effect, since Tastytrade is apparently against negative numbers.

Valid values are as follows:

The Enum and its members also have the following methods:

Encode the string using the codec registered for encoding.

The encoding in which to encode the string.

The error handling scheme to use for encoding errors. The default is ‘strict’ meaning that encoding errors raise a UnicodeEncodeError. Other possible values are ‘ignore’, ‘replace’ and ‘xmlcharrefreplace’ as well as any other name registered with codecs.register_error that can handle UnicodeEncodeErrors.

Return a copy with all occurrences of substring old replaced by new.

Maximum number of occurrences to replace. -1 (the default value) means replace all occurrences.

If the optional argument count is given, only the first count occurrences are replaced.

Return a list of the substrings in the string, using sep as the separator string.

The separator used to split the string.

When set to None (the default value), will split on any whitespace character (including \n \r \t \f and spaces) and will discard empty strings from the result.

Maximum number of splits (starting from the left). -1 (the default value) means no limit.

Note, str.split() is mainly useful for data that has been intentionally delimited. With natural text that includes punctuation, consider using the regular expression module.

Return a list of the substrings in the string, using sep as the separator string.

The separator used to split the string.

When set to None (the default value), will split on any whitespace character (including \n \r \t \f and spaces) and will discard empty strings from the result.

Maximum number of splits (starting from the left). -1 (the default value) means no limit.

Splitting starts at the end of the string and works to the front.

Concatenate any number of strings.

The string whose method is called is inserted in between each given string. The result is returned as a new string.

Example: ‘.’.join([‘ab’, ‘pq’, ‘rs’]) -> ‘ab.pq.rs’

Return a capitalized version of the string.

More specifically, make the first character have upper case and the rest lower case.

Return a version of the string suitable for caseless comparisons.

Return a version of the string where each word is titlecased.

More specifically, words start with uppercased characters and all remaining cased characters have lower case.

Return a centered string of length width.

Padding is done using the specified fill character (default is a space).

Return the number of non-overlapping occurrences of substring sub in string S[start:end]. Optional arguments start and end are interpreted as in slice notation.

Return a copy where all tab characters are expanded using spaces.

If tabsize is not given, a tab size of 8 characters is assumed.

Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation.

Return -1 on failure.

Partition the string into three parts using the given separator.

This will search for the separator in the string. If the separator is found, returns a 3-tuple containing the part before the separator, the separator itself, and the part after it.

If the separator is not found, returns a 3-tuple containing the original string and two empty strings.

Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation.

Raises ValueError when the substring is not found.

Return a left-justified string of length width.

Padding is done using the specified fill character (default is a space).

Return a copy of the string converted to lowercase.

Return a copy of the string with leading whitespace removed.

If chars is given and not None, remove characters in chars instead.

Return the highest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation.

Return -1 on failure.

Return the highest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation.

Raises ValueError when the substring is not found.

Return a right-justified string of length width.

Padding is done using the specified fill character (default is a space).

Return a copy of the string with trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.

Partition the string into three parts using the given separator.

This will search for the separator in the string, starting at the end. If the separator is found, returns a 3-tuple containing the part before the separator, the separator itself, and the part after it.

If the separator is not found, returns a 3-tuple containing two empty strings and the original string.

Return a list of the lines in the string, breaking at line boundaries.

Line breaks are not included in the resulting list unless keepends is given and true.

Return a copy of the string with leading and trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.

Convert uppercase characters to lowercase and lowercase characters to uppercase.

Replace each character in the string using the given translation table.

Translation table, which must be a mapping of Unicode ordinals to Unicode ordinals, strings, or None.

The table must implement lookup/indexing via __getitem__, for instance a dictionary or list. If this operation raises LookupError, the character is left untouched. Characters mapped to None are deleted.

Return a copy of the string converted to uppercase.

Return True if S starts with the specified prefix, False otherwise. With optional start, test S beginning at that position. With optional end, stop comparing S at that position. prefix can also be a tuple of strings to try.

Return True if S ends with the specified suffix, False otherwise. With optional start, test S beginning at that position. With optional end, stop comparing S at that position. suffix can also be a tuple of strings to try.

Return a str with the given prefix string removed if present.

If the string starts with the prefix string, return string[len(prefix):]. Otherwise, return a copy of the original string.

Return a str with the given suffix string removed if present.

If the string ends with the suffix string and that suffix is not empty, return string[:-len(suffix)]. Otherwise, return a copy of the original string.

Return True if all characters in the string are ASCII, False otherwise.

ASCII characters have code points in the range U+0000-U+007F. Empty string is ASCII too.

Return True if the string is a lowercase string, False otherwise.

A string is lowercase if all cased characters in the string are lowercase and there is at least one cased character in the string.

Return True if the string is an uppercase string, False otherwise.

A string is uppercase if all cased characters in the string are uppercase and there is at least one cased character in the string.

Return True if the string is a title-cased string, False otherwise.

In a title-cased string, upper- and title-case characters may only follow uncased characters and lowercase characters only cased ones.

Return True if the string is a whitespace string, False otherwise.

A string is whitespace if all characters in the string are whitespace and there is at least one character in the string.

Return True if the string is a decimal string, False otherwise.

A string is a decimal string if all characters in the string are decimal and there is at least one character in the string.

Return True if the string is a digit string, False otherwise.

A string is a digit string if all characters in the string are digits and there is at least one character in the string.

Return True if the string is a numeric string, False otherwise.

A string is numeric if all characters in the string are numeric and there is at least one character in the string.

Return True if the string is an alphabetic string, False otherwise.

A string is alphabetic if all characters in the string are alphabetic and there is at least one character in the string.

Return True if the string is an alpha-numeric string, False otherwise.

A string is alpha-numeric if all characters in the string are alpha-numeric and there is at least one character in the string.

Return True if the string is a valid Python identifier, False otherwise.

Call keyword.iskeyword(s) to test whether string s is a reserved identifier, such as “def” or “class”.

Return True if the string is printable, False otherwise.

A string is printable if all of its characters are considered printable in repr() or if it is empty.

Pad a numeric string with zeros on the left, to fill a field of the given width.

The string is never truncated.

Return a formatted version of S, using substitutions from args and kwargs. The substitutions are identified by braces (‘{’ and ‘}’).

Return a formatted version of S, using substitutions from mapping. The substitutions are identified by braces (‘{’ and ‘}’).

Return a translation table usable for str.translate().

If there is only one argument, it must be a dictionary mapping Unicode ordinals (integers) or characters to Unicode ordinals, strings or None. Character keys will be then converted to ordinals. If there are two arguments, they must be strings of equal length, and in the resulting dictionary, each character in x will be mapped to the character at the same position in y. If there is a third argument, it must be a string, whose characters will be mapped to None in the result.

A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.

Show JSON schema{ "title": "TastytradeData", "description": "A pydantic dataclass that converts keys from snake case to dasherized\nand performs type validation and coercion.", "type": "object", "properties": {} }

Returns a copy of the model.

This method is now deprecated; use model_copy instead.

If you need include or exclude, use:

`python {test="skip" lint="skip"} data = self.model_dump(include=include, exclude=exclude, round_trip=True) data = {**data, **(update or {})} copied = self.model_validate(data) `

include: Optional set or mapping specifying which fields to include in the copied model. exclude: Optional set or mapping specifying which fields to exclude in the copied model. update: Optional dictionary of field-value pairs to override field values in the copied model. deep: If True, the values of fields that are Pydantic models will be deep-copied.

A copy of the model with included, excluded and updated fields as specified.

Creates a new instance of the Model class with validated data.

Creates a new model setting __dict__ and __pydantic_fields_set__ from trusted or pre-validated data. Default values are respected, but no other validation is performed.

model_construct() generally respects the model_config.extra setting on the provided model. That is, if model_config.extra == ‘allow’, then all extra passed values are added to the model instance’s __dict__ and __pydantic_extra__ fields. If model_config.extra == ‘ignore’ (the default), then all extra passed values are ignored. Because no validation is performed with a call to model_construct(), having model_config.extra == ‘forbid’ does not result in an error if extra values are passed, but they will be ignored.

this is directly used for the [model_fields_set][pydantic.BaseModel.model_fields_set] attribute. Otherwise, the field names from the values argument will be used.

values: Trusted or pre-validated data dictionary.

A new instance of the Model class with validated data.

[model_copy](../concepts/serialization.md#model_copy)

Returns a copy of the model.

The underlying instance’s [__dict__][object.__dict__] attribute is copied. This might have unexpected side effects if you store anything in it, on top of the model fields (e.g. the value of [cached properties][functools.cached_property]).

before creating the new model. You should trust this data.

deep: Set to True to make a deep copy of the model.

[model_dump](../concepts/serialization.md#modelmodel_dump)

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

If mode is ‘json’, the output will only contain JSON serializable types. If mode is ‘python’, the output may contain non-JSON-serializable Python objects.

include: A set of fields to include in the output. exclude: A set of fields to exclude from the output. context: Additional context to pass to the serializer. by_alias: Whether to use the field’s alias in the dictionary key if defined. exclude_unset: Whether to exclude fields that have not been explicitly set. exclude_defaults: Whether to exclude fields that are set to their default value. exclude_none: Whether to exclude fields that have a value of None. round_trip: If True, dumped values should be valid as input for non-idempotent types such as Json[T]. warnings: How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,

“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any: Whether to serialize fields with duck-typing serialization behavior.

A dictionary representation of the model.

[model_dump_json](../concepts/serialization.md#modelmodel_dump_json)

Generates a JSON representation of the model using Pydantic’s to_json method.

indent: Indentation to use in the JSON output. If None is passed, the output will be compact. include: Field(s) to include in the JSON output. exclude: Field(s) to exclude from the JSON output. context: Additional context to pass to the serializer. by_alias: Whether to serialize using field aliases. exclude_unset: Whether to exclude fields that have not been explicitly set. exclude_defaults: Whether to exclude fields that are set to their default value. exclude_none: Whether to exclude fields that have a value of None. round_trip: If True, dumped values should be valid as input for non-idempotent types such as Json[T]. warnings: How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,

“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any: Whether to serialize fields with duck-typing serialization behavior.

A JSON string representation of the model.

Generates a JSON schema for a model class.

by_alias: Whether to use attribute aliases or not. ref_template: The reference template. schema_generator: To override the logic used to generate the JSON schema, as a subclass of

GenerateJsonSchema with your desired modifications

mode: The mode in which to generate the schema.

The JSON schema for the given model class.

Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

Model with 2 type variables and a concrete model Model[str, int], the value (str, int) would be passed to params.

String representing the new class where params are passed to cls as type variables.

TypeError: Raised when trying to generate concrete names for non-generic models.

Override this method to perform additional initialization after __init__ and model_construct. This is useful if you want to do some validation that requires the entire model to be initialized.

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during the initial attempt to build the schema, and automatic rebuilding fails.

force: Whether to force the rebuilding of the model schema, defaults to False. raise_errors: Whether to raise errors, defaults to True. _parent_namespace_depth: The depth level of the parent namespace, defaults to 2. _types_namespace: The types namespace, defaults to None.

Returns None if the schema is already “complete” and rebuilding was not required. If rebuilding _was_ required, returns True if rebuilding was successful, otherwise False.

Validate a pydantic model instance.

obj: The object to validate. strict: Whether to enforce types strictly. from_attributes: Whether to extract data from object attributes. context: Additional context to pass to the validator. by_alias: Whether to use the field’s alias when validating against the provided input data. by_name: Whether to use the field’s name when validating against the provided input data.

ValidationError: If the object could not be validated.

The validated model instance.

[JSON Parsing](../concepts/json.md#json-parsing)

Validate the given JSON data against the Pydantic model.

json_data: The JSON data to validate. strict: Whether to enforce types strictly. context: Extra variables to pass to the validator. by_alias: Whether to use the field’s alias when validating against the provided input data. by_name: Whether to use the field’s name when validating against the provided input data.

The validated Pydantic model.

ValidationError: If json_data is not a JSON string or the object could not be validated.

Validate the given object with string data against the Pydantic model.

obj: The object containing string data to validate. strict: Whether to enforce types strictly. context: Extra variables to pass to the validator. by_alias: Whether to use the field’s alias when validating against the provided input data. by_name: Whether to use the field’s name when validating against the provided input data.

The validated Pydantic model.

Get extra fields set during validation.

A dictionary of extra fields, or None if config.extra is not set to “allow”.

Returns the set of fields that have been explicitly set on this model instance.

i.e. that were not filled from defaults.

An internal error raised by the Tastytrade SDK.

Exception.with_traceback(tb) – set self.__traceback__ to tb and return self.

Helper for paginated endpoints. Excepts params to have at least page-offset and per-page parameters. If params[“page-offset”] is None, iterates over all results; otherwise, gets a specific page.

the httpx client for making request

the TastytradeData model for results

parameters for request

Gets the monthly expiration associated with the FX futures: /6E, /6A, etc. As far as I can tell, these expire on the first Friday prior to the second Wednesday.

date to check. If not provided defaults to current NY date.

Gets the monthly expiration associated with the grain futures: /ZC, /ZW, etc. According to CME, these expire on the Friday which precedes, by at least 2 business days, the last business day of the month.

date to check. If not provided defaults to current NY date.

Gets the monthly expiration associated with the index futures: /ES, /RTY, /NQ, etc. According to CME, these expire on the last business day of the month.

date to check. If not provided defaults to current NY date.

Gets the monthly expiration associated with the metals futures: /GC, /SI, etc. According to CME, these expire on the 4th last business day of the month, unless that day occurs on a Friday or the day before a holiday, in which case they expire on the prior business day.

date to check. If not provided defaults to current NY date.

Gets the monthly expiration associated with the WTI oil futures: /CL and /MCL. According to CME, these expire 6 business days before the 25th day of the month, unless the 25th day is not a business day, in which case they expire 7 business days prior to the 25th day of the month.

date to check. If not provided defaults to current NY date.

Gets the monthly expiration associated with the treasury futures: /ZN, /ZB, etc. According to CME, these expire the Friday before the 2nd last business day of the month. If this is not a business day, they expire 1 business day prior.

date to check. If not provided defaults to current NY date.

Get a PriceEffect for a signed value.

Gets the monthly expiration closest to 45 days from the current date.

Gets the monthly expiration associated with the month of the given date, or the monthly expiration associated with today’s month.

date to check. If not provided defaults to current NY date.

Check if the market is currently open.

Returns whether the market was/is/will be open at ANY point during the given day.

date to check. If not provided defaults to current NY date.

Gets the current time in the New York timezone.

Helper for paginated endpoints. Excepts params to have at least page-offset and per-page parameters. If params[“page-offset”] is None, iterates over all results; otherwise, gets a specific page.

the httpx client for making request

the TastytradeData model for results

parameters for request

Handles setting the sign of a number using the associated “-effect” field.

the raw, unprocessed model object

the name of the number fields to set

Gets the current date in the New York timezone.

Checks if the given code is an error; if so, raises an exception. Then, returns the JSON payload.

response to check for errors

Checks if the given code is an error; if so, raises an exception.

response to check for errors

**Examples:**

Example 1 (json):
```json
{
   "title": "TastytradeData",
   "description": "A pydantic dataclass that converts keys from snake case to dasherized\nand performs type validation and coercion.",
   "type": "object",
   "properties": {}
}
```

---
