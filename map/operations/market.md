<!-- Generated file — do not edit; regenerated with the SDK. -->

# Market — operations

Accessor: `client.market` · Source: `binance/apis/market.py` · 15 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.market.hr_ticker_price_change_statistics24

- **Route**: `GET /api/v3/ticker/24hr`
- **Signature**: `def hr_ticker_price_change_statistics24(*, symbol: str | None = None, symbols: str | None = None, type_: TypeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `symbols` — query · `type_` — query `type`
- **Returns (parsed)**: `ApiV3Ticker24HrResponse`
- **Returns (raw)**: `ApiResult[ApiV3Ticker24HrResponse, HrTickerPriceChangeStatistics24ErrorBody]`
- **Error**: `HrTickerPriceChangeStatistics24ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TypeOrStr` | `binance/models/enums/type.py` |
| `ApiV3Ticker24HrResponse` | `binance/models/unions/api_v3_ticker24_hr_response.py` |
| `HrTickerPriceChangeStatistics24ErrorBody` | `binance/errors/hr_ticker_price_change_statistics24_error.py` |
| `Error` | `binance/models/error.py` |

### client.market.check_server_time

- **Route**: `GET /api/v3/time`
- **Signature**: `def check_server_time(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `ApiV3TimeResponse`
- **Returns (raw)**: `ApiResult[ApiV3TimeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV3TimeResponse` | `binance/models/api_v3_time_response.py` |

### client.market.compressed_aggregate_trades_list

- **Route**: `GET /api/v3/aggTrades`
- **Signature**: `def compressed_aggregate_trades_list(symbol: str, *, from_id: int | None = None, start_time: int | None = None, end_time: int | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `from_id` — query `fromId` · `start_time` — query `startTime` · `end_time` — query `endTime` · `limit` — query
- **Returns (parsed)**: `list[AggTrade]`
- **Returns (raw)**: `ApiResult[list[AggTrade], CompressedAggregateTradesListErrorBody]`
- **Error**: `CompressedAggregateTradesListErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AggTrade` | `binance/models/agg_trade.py` |
| `CompressedAggregateTradesListErrorBody` | `binance/errors/compressed_aggregate_trades_list_error.py` |
| `Error` | `binance/models/error.py` |

### client.market.current_average_price

- **Route**: `GET /api/v3/avgPrice`
- **Signature**: `def current_average_price(symbol: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query
- **Returns (parsed)**: `ApiV3AvgPriceResponse`
- **Returns (raw)**: `ApiResult[ApiV3AvgPriceResponse, CurrentAveragePriceErrorBody]`
- **Error**: `CurrentAveragePriceErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ApiV3AvgPriceResponse` | `binance/models/api_v3_avg_price_response.py` |
| `CurrentAveragePriceErrorBody` | `binance/errors/current_average_price_error.py` |
| `Error` | `binance/models/error.py` |

### client.market.exchange_information

- **Route**: `GET /api/v3/exchangeInfo`
- **Signature**: `def exchange_information(*, symbol: str | None = None, symbols: str | None = None, permissions: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `symbols` — query · `permissions` — query
- **Returns (parsed)**: `ApiV3ExchangeInfoResponse`
- **Returns (raw)**: `ApiResult[ApiV3ExchangeInfoResponse, ExchangeInformationErrorBody]`
- **Error**: `ExchangeInformationErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ApiV3ExchangeInfoResponse` | `binance/models/api_v3_exchange_info_response.py` |
| `ExchangeInformationErrorBody` | `binance/errors/exchange_information_error.py` |
| `Error` | `binance/models/error.py` |

### client.market.kline_candlestick_data

- **Route**: `GET /api/v3/klines`
- **Signature**: `def kline_candlestick_data(symbol: str, interval: IntervalOrStr, *, start_time: int | None = None, end_time: int | None = None, time_zone: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `interval`
- **Params**: `symbol` — query · `interval` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `time_zone` — query `timeZone` · `limit` — query
- **Returns (parsed)**: `list[list[ApiV3KlinesResponse]]`
- **Returns (raw)**: `ApiResult[list[list[ApiV3KlinesResponse]], KlineCandlestickDataErrorBody]`
- **Error**: `KlineCandlestickDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `IntervalOrStr` | `binance/models/enums/interval.py` |
| `ApiV3KlinesResponse` | `binance/models/unions/api_v3_klines_response.py` |
| `KlineCandlestickDataErrorBody` | `binance/errors/kline_candlestick_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.market.old_trade_lookup

- **Route**: `GET /api/v3/historicalTrades`
- **Signature**: `def old_trade_lookup(symbol: str, *, limit: int | None = None, from_id: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `limit` — query · `from_id` — query `fromId`
- **Returns (parsed)**: `list[Trade]`
- **Returns (raw)**: `ApiResult[list[Trade], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Trade` | `binance/models/trade.py` |

### client.market.order_book

- **Route**: `GET /api/v3/depth`
- **Signature**: `def order_book(symbol: str, *, limit: int | None = 100, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `limit` — query
- **Returns (parsed)**: `ApiV3DepthResponse`
- **Returns (raw)**: `ApiResult[ApiV3DepthResponse, OrderBookErrorBody]`
- **Error**: `OrderBookErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ApiV3DepthResponse` | `binance/models/api_v3_depth_response.py` |
| `OrderBookErrorBody` | `binance/errors/order_book_error.py` |
| `Error` | `binance/models/error.py` |

### client.market.recent_trades_list

- **Route**: `GET /api/v3/trades`
- **Signature**: `def recent_trades_list(symbol: str, *, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `limit` — query
- **Returns (parsed)**: `list[Trade]`
- **Returns (raw)**: `ApiResult[list[Trade], RecentTradesListErrorBody]`
- **Error**: `RecentTradesListErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Trade` | `binance/models/trade.py` |
| `RecentTradesListErrorBody` | `binance/errors/recent_trades_list_error.py` |
| `Error` | `binance/models/error.py` |

### client.market.rolling_window_price_change_statistics

- **Route**: `GET /api/v3/ticker`
- **Signature**: `def rolling_window_price_change_statistics(*, symbol: str | None = None, symbols: str | None = None, window_size: str | None = None, type_: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `symbols` — query · `window_size` — query `windowSize` · `type_` — query `type`
- **Returns (parsed)**: `ApiV3TickerResponse`
- **Returns (raw)**: `ApiResult[ApiV3TickerResponse, RollingWindowPriceChangeStatisticsErrorBody]`
- **Error**: `RollingWindowPriceChangeStatisticsErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ApiV3TickerResponse` | `binance/models/api_v3_ticker_response.py` |
| `RollingWindowPriceChangeStatisticsErrorBody` | `binance/errors/rolling_window_price_change_statistics_error.py` |
| `Error` | `binance/models/error.py` |

### client.market.symbol_order_book_ticker

- **Route**: `GET /api/v3/ticker/bookTicker`
- **Signature**: `def symbol_order_book_ticker(*, symbol: str | None = None, symbols: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `symbols` — query
- **Returns (parsed)**: `ApiV3TickerBookTickerResponse`
- **Returns (raw)**: `ApiResult[ApiV3TickerBookTickerResponse, SymbolOrderBookTickerErrorBody]`
- **Error**: `SymbolOrderBookTickerErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ApiV3TickerBookTickerResponse` | `binance/models/unions/api_v3_ticker_book_ticker_response.py` |
| `SymbolOrderBookTickerErrorBody` | `binance/errors/symbol_order_book_ticker_error.py` |
| `Error` | `binance/models/error.py` |

### client.market.symbol_price_ticker

- **Route**: `GET /api/v3/ticker/price`
- **Signature**: `def symbol_price_ticker(*, symbol: str | None = None, symbols: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `symbols` — query
- **Returns (parsed)**: `ApiV3TickerPriceResponse`
- **Returns (raw)**: `ApiResult[ApiV3TickerPriceResponse, SymbolPriceTickerErrorBody]`
- **Error**: `SymbolPriceTickerErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ApiV3TickerPriceResponse` | `binance/models/unions/api_v3_ticker_price_response.py` |
| `SymbolPriceTickerErrorBody` | `binance/errors/symbol_price_ticker_error.py` |
| `Error` | `binance/models/error.py` |

### client.market.test_connectivity

- **Route**: `GET /api/v3/ping`
- **Signature**: `def test_connectivity(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, RawError]`
- **Error**: `RawError` — **Case B**

### client.market.trading_day_ticker

- **Route**: `GET /api/v3/ticker/tradingDay`
- **Signature**: `def trading_day_ticker(*, symbol: str | None = None, symbols: str | None = None, time_zone: str | None = None, type_: TypeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `symbols` — query · `time_zone` — query `timeZone` · `type_` — query `type`
- **Returns (parsed)**: `ApiV3TickerTradingDayResponse`
- **Returns (raw)**: `ApiResult[ApiV3TickerTradingDayResponse, TradingDayTickerErrorBody]`
- **Error**: `TradingDayTickerErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TypeOrStr` | `binance/models/enums/type.py` |
| `ApiV3TickerTradingDayResponse` | `binance/models/unions/api_v3_ticker_trading_day_response.py` |
| `TradingDayTickerErrorBody` | `binance/errors/trading_day_ticker_error.py` |
| `Error` | `binance/models/error.py` |

### client.market.ui_klines

- **Route**: `GET /api/v3/uiKlines`
- **Signature**: `def ui_klines(symbol: str, interval: IntervalOrStr, *, start_time: int | None = None, end_time: int | None = None, time_zone: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `interval`
- **Params**: `symbol` — query · `interval` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `time_zone` — query `timeZone` · `limit` — query
- **Returns (parsed)**: `list[list[ApiV3UiKlinesResponse]]`
- **Returns (raw)**: `ApiResult[list[list[ApiV3UiKlinesResponse]], UiklinesErrorBody]`
- **Error**: `UiklinesErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `IntervalOrStr` | `binance/models/enums/interval.py` |
| `ApiV3UiKlinesResponse` | `binance/models/unions/api_v3_ui_klines_response.py` |
| `UiklinesErrorBody` | `binance/errors/uiklines_error.py` |
| `Error` | `binance/models/error.py` |

