<!-- Generated file — do not edit; regenerated with the SDK. -->

# C2C — operations

Accessor: `client.c2_c` · Source: `binance_public_spot_api/apis/c2_c.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.c2_c.get_c2_c_trade_history_user_data

- **Route**: `GET /sapi/v1/c2c/orderMatch/listUserOrderHistory`
- **Auth**: `api_key_auth`
- **Signature**: `def get_c2_c_trade_history_user_data(trade_type: TradeTypeOrStr, timestamp: int, signature: str, *, start_timestamp: int | None = None, end_timestamp: int | None = None, page: int | None = None, rows: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `trade_type`, `timestamp`, `signature`
- **Params**: `trade_type` — query `tradeType` · `timestamp` — query · `signature` — query · `start_timestamp` — query `startTimestamp` · `end_timestamp` — query `endTimestamp` · `page` — query · `rows` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1C2COrderMatchListUserOrderHistoryResponse`
- **Returns (raw)**: `ApiResult[SapiV1C2COrderMatchListUserOrderHistoryResponse, GetC2CTradeHistoryUserDataErrorBody]`
- **Error**: `GetC2CTradeHistoryUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TradeTypeOrStr` | `binance_public_spot_api/models/enums/trade_type.py` |
| `SapiV1C2COrderMatchListUserOrderHistoryResponse` | `binance_public_spot_api/models/sapi_v1_c2_c_order_match_list_user_order_history_response.py` |
| `GetC2CTradeHistoryUserDataErrorBody` | `binance_public_spot_api/errors/get_c2_c_trade_history_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

