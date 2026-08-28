<!-- Generated file — do not edit; regenerated with the SDK. -->

# Fiat — operations

Accessor: `client.fiat` · Source: `binance/apis/fiat.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.fiat.fiat_deposit_withdraw_history_user_data

- **Route**: `GET /sapi/v1/fiat/orders`
- **Signature**: `def fiat_deposit_withdraw_history_user_data(transaction_type: int, timestamp: int, signature: str, *, begin_time: int | None = None, end_time: int | None = None, page: int | None = None, rows: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `transaction_type`, `timestamp`, `signature`
- **Params**: `transaction_type` — query `transactionType` · `timestamp` — query · `signature` — query · `begin_time` — query `beginTime` · `end_time` — query `endTime` · `page` — query · `rows` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1FiatOrdersResponse`
- **Returns (raw)**: `ApiResult[SapiV1FiatOrdersResponse, FiatDepositWithdrawHistoryUserDataErrorBody]`
- **Error**: `FiatDepositWithdrawHistoryUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1FiatOrdersResponse` | `binance/models/sapi_v1_fiat_orders_response.py` |
| `FiatDepositWithdrawHistoryUserDataErrorBody` | `binance/errors/fiat_deposit_withdraw_history_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.fiat.fiat_payments_history_user_data

- **Route**: `GET /sapi/v1/fiat/payments`
- **Signature**: `def fiat_payments_history_user_data(transaction_type: int, timestamp: int, signature: str, *, begin_time: int | None = None, end_time: int | None = None, page: int | None = None, rows: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `transaction_type`, `timestamp`, `signature`
- **Params**: `transaction_type` — query `transactionType` · `timestamp` — query · `signature` — query · `begin_time` — query `beginTime` · `end_time` — query `endTime` · `page` — query · `rows` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1FiatPaymentsResponse`
- **Returns (raw)**: `ApiResult[SapiV1FiatPaymentsResponse, FiatPaymentsHistoryUserDataErrorBody]`
- **Error**: `FiatPaymentsHistoryUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1FiatPaymentsResponse` | `binance/models/sapi_v1_fiat_payments_response.py` |
| `FiatPaymentsHistoryUserDataErrorBody` | `binance/errors/fiat_payments_history_user_data_error.py` |
| `Error` | `binance/models/error.py` |

