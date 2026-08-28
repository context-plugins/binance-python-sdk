<!-- Generated file — do not edit; regenerated with the SDK. -->

# Blvt — operations

Accessor: `client.blvt` · Source: `binance/apis/blvt.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.blvt.blvt_info_market_data

- **Route**: `GET /sapi/v1/blvt/tokenInfo`
- **Signature**: `def blvt_info_market_data(*, token_name: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `token_name` — query `tokenName`
- **Returns (parsed)**: `list[SapiV1BlvtTokenInfoResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1BlvtTokenInfoResponse], BlvtInfoMarketDataErrorBody]`
- **Error**: `BlvtInfoMarketDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1BlvtTokenInfoResponse` | `binance/models/sapi_v1_blvt_token_info_response.py` |
| `BlvtInfoMarketDataErrorBody` | `binance/errors/blvt_info_market_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.blvt.blvt_user_limit_info_user_data

- **Route**: `GET /sapi/v1/blvt/userLimit`
- **Signature**: `def blvt_user_limit_info_user_data(timestamp: int, signature: str, *, token_name: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `token_name` — query `tokenName` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1BlvtUserLimitResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1BlvtUserLimitResponse], BlvtUserLimitInfoUserDataErrorBody]`
- **Error**: `BlvtUserLimitInfoUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1BlvtUserLimitResponse` | `binance/models/sapi_v1_blvt_user_limit_response.py` |
| `BlvtUserLimitInfoUserDataErrorBody` | `binance/errors/blvt_user_limit_info_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.blvt.query_subscription_record_user_data

- **Route**: `GET /sapi/v1/blvt/subscribe/record`
- **Signature**: `def query_subscription_record_user_data(timestamp: int, signature: str, *, token_name: str | None = None, id: int | None = None, start_time: int | None = None, end_time: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `token_name` — query `tokenName` · `id` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `limit` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1BlvtSubscribeRecordResponse`
- **Returns (raw)**: `ApiResult[SapiV1BlvtSubscribeRecordResponse, QuerySubscriptionRecordUserDataErrorBody]`
- **Error**: `QuerySubscriptionRecordUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1BlvtSubscribeRecordResponse` | `binance/models/sapi_v1_blvt_subscribe_record_response.py` |
| `QuerySubscriptionRecordUserDataErrorBody` | `binance/errors/query_subscription_record_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.blvt.redeem_blvt_user_data

- **Route**: `POST /sapi/v1/blvt/redeem`
- **Signature**: `def redeem_blvt_user_data(token_name: str, amount: float, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token_name`, `amount`, `timestamp`, `signature`
- **Params**: `token_name` — query `tokenName` · `amount` — query · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1BlvtRedeemResponse`
- **Returns (raw)**: `ApiResult[SapiV1BlvtRedeemResponse, RedeemBlvtUserDataErrorBody]`
- **Error**: `RedeemBlvtUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1BlvtRedeemResponse` | `binance/models/sapi_v1_blvt_redeem_response.py` |
| `RedeemBlvtUserDataErrorBody` | `binance/errors/redeem_blvt_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.blvt.redemption_record_user_data

- **Route**: `GET /sapi/v1/blvt/redeem/record`
- **Signature**: `def redemption_record_user_data(timestamp: int, signature: str, *, token_name: str | None = None, id: int | None = None, start_time: int | None = None, end_time: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `token_name` — query `tokenName` · `id` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `limit` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1BlvtRedeemRecordResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1BlvtRedeemRecordResponse], RedemptionRecordUserDataErrorBody]`
- **Error**: `RedemptionRecordUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1BlvtRedeemRecordResponse` | `binance/models/sapi_v1_blvt_redeem_record_response.py` |
| `RedemptionRecordUserDataErrorBody` | `binance/errors/redemption_record_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.blvt.subscribe_blvt_user_data

- **Route**: `POST /sapi/v1/blvt/subscribe`
- **Signature**: `def subscribe_blvt_user_data(token_name: str, cost: float, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token_name`, `cost`, `timestamp`, `signature`
- **Params**: `token_name` — query `tokenName` · `cost` — query · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1BlvtSubscribeResponse`
- **Returns (raw)**: `ApiResult[SapiV1BlvtSubscribeResponse, SubscribeBlvtUserDataErrorBody]`
- **Error**: `SubscribeBlvtUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1BlvtSubscribeResponse` | `binance/models/sapi_v1_blvt_subscribe_response.py` |
| `SubscribeBlvtUserDataErrorBody` | `binance/errors/subscribe_blvt_user_data_error.py` |
| `Error` | `binance/models/error.py` |

