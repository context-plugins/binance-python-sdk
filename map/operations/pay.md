<!-- Generated file — do not edit; regenerated with the SDK. -->

# Pay — operations

Accessor: `client.pay` · Source: `binance_public_spot_api/apis/pay.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.pay.get_pay_trade_history_user_data

- **Route**: `GET /sapi/v1/pay/transactions`
- **Auth**: `api_key_auth`
- **Signature**: `def get_pay_trade_history_user_data(timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `limit` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1PayTransactionsResponse`
- **Returns (raw)**: `ApiResult[SapiV1PayTransactionsResponse, GetPayTradeHistoryUserDataErrorBody]`
- **Error**: `GetPayTradeHistoryUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1PayTransactionsResponse` | `binance_public_spot_api/models/sapi_v1_pay_transactions_response.py` |
| `GetPayTradeHistoryUserDataErrorBody` | `binance_public_spot_api/errors/get_pay_trade_history_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

