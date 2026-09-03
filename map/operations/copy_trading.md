<!-- Generated file — do not edit; regenerated with the SDK. -->

# CopyTrading — operations

Accessor: `client.copy_trading` · Source: `binance_public_spot_api/apis/copy_trading.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.copy_trading.get_futures_lead_trader_status_trade

- **Route**: `GET /sapi/v1/copyTrading/futures/userStatus`
- **Auth**: `api_key_auth`
- **Signature**: `def get_futures_lead_trader_status_trade(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1CopyTradingFuturesUserStatusResponse`
- **Returns (raw)**: `ApiResult[SapiV1CopyTradingFuturesUserStatusResponse, GetFuturesLeadTraderStatusTradeErrorBody]`
- **Error**: `GetFuturesLeadTraderStatusTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1CopyTradingFuturesUserStatusResponse` | `binance_public_spot_api/models/sapi_v1_copy_trading_futures_user_status_response.py` |
| `GetFuturesLeadTraderStatusTradeErrorBody` | `binance_public_spot_api/errors/get_futures_lead_trader_status_trade_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.copy_trading.get_futures_lead_trading_symbol_whitelist_user_data

- **Route**: `GET /sapi/v1/copyTrading/futures/leadSymbol`
- **Auth**: `api_key_auth`
- **Signature**: `def get_futures_lead_trading_symbol_whitelist_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1CopyTradingFuturesLeadSymbolResponse`
- **Returns (raw)**: `ApiResult[SapiV1CopyTradingFuturesLeadSymbolResponse, GetFuturesLeadTradingSymbolWhitelistUserDataErrorBody]`
- **Error**: `GetFuturesLeadTradingSymbolWhitelistUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1CopyTradingFuturesLeadSymbolResponse` | `binance_public_spot_api/models/sapi_v1_copy_trading_futures_lead_symbol_response.py` |
| `GetFuturesLeadTradingSymbolWhitelistUserDataErrorBody` | `binance_public_spot_api/errors/get_futures_lead_trading_symbol_whitelist_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

