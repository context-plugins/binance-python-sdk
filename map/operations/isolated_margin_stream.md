<!-- Generated file — do not edit; regenerated with the SDK. -->

# IsolatedMarginStream — operations

Accessor: `client.isolated_margin_stream` · Source: `binance/apis/isolated_margin_stream.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.isolated_margin_stream.close_a_listen_key_user_stream_3

- **Route**: `DELETE /sapi/v1/userDataStream/isolated`
- **Signature**: `def close_a_listen_key_user_stream_3(*, listen_key: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `listen_key` — query `listenKey`
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, CloseAListenKeyUserStream3ErrorBody]`
- **Error**: `CloseAListenKeyUserStream3ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CloseAListenKeyUserStream3ErrorBody` | `binance/errors/close_a_listen_key_user_stream3_error.py` |
| `Error` | `binance/models/error.py` |

### client.isolated_margin_stream.generate_a_listen_key_user_stream

- **Route**: `POST /sapi/v1/userDataStream/isolated`
- **Signature**: `def generate_a_listen_key_user_stream(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `SapiV1UserDataStreamIsolatedResponse`
- **Returns (raw)**: `ApiResult[SapiV1UserDataStreamIsolatedResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SapiV1UserDataStreamIsolatedResponse` | `binance/models/sapi_v1_user_data_stream_isolated_response.py` |

### client.isolated_margin_stream.ping_keep_alive_a_listen_key_user_stream

- **Route**: `PUT /sapi/v1/userDataStream/isolated`
- **Signature**: `def ping_keep_alive_a_listen_key_user_stream(*, listen_key: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `listen_key` — query `listenKey`
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, PingKeepAliveAListenKeyUserStreamErrorBody]`
- **Error**: `PingKeepAliveAListenKeyUserStreamErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PingKeepAliveAListenKeyUserStreamErrorBody` | `binance/errors/ping_keep_alive_a_listen_key_user_stream_error.py` |
| `Error` | `binance/models/error.py` |

