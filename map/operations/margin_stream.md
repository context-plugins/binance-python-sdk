<!-- Generated file — do not edit; regenerated with the SDK. -->

# MarginStream — operations

Accessor: `client.margin_stream` · Source: `binance/apis/margin_stream.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.margin_stream.close_a_listen_key_user_stream_2

- **Route**: `DELETE /sapi/v1/userDataStream`
- **Signature**: `def close_a_listen_key_user_stream_2(*, listen_key: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `listen_key` — query `listenKey`
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, CloseAListenKeyUserStream2ErrorBody]`
- **Error**: `CloseAListenKeyUserStream2ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CloseAListenKeyUserStream2ErrorBody` | `binance/errors/close_a_listen_key_user_stream2_error.py` |
| `Error` | `binance/models/error.py` |

### client.margin_stream.create_a_listen_key_user_stream_2

- **Route**: `POST /sapi/v1/userDataStream`
- **Signature**: `def create_a_listen_key_user_stream_2(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `SapiV1UserDataStreamResponse`
- **Returns (raw)**: `ApiResult[SapiV1UserDataStreamResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SapiV1UserDataStreamResponse` | `binance/models/sapi_v1_user_data_stream_response.py` |

### client.margin_stream.ping_keep_alive_a_listen_key_user_stream_2

- **Route**: `PUT /sapi/v1/userDataStream`
- **Signature**: `def ping_keep_alive_a_listen_key_user_stream_2(*, listen_key: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `listen_key` — query `listenKey`
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, PingKeepAliveAListenKeyUserStream2ErrorBody]`
- **Error**: `PingKeepAliveAListenKeyUserStream2ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PingKeepAliveAListenKeyUserStream2ErrorBody` | `binance/errors/ping_keep_alive_a_listen_key_user_stream2_error.py` |
| `Error` | `binance/models/error.py` |

