<!-- Generated file — do not edit; regenerated with the SDK. -->

# Stream — operations

Accessor: `client.stream` · Source: `binance/apis/stream.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.stream.close_a_listen_key_user_stream

- **Route**: `DELETE /api/v3/userDataStream`
- **Signature**: `def close_a_listen_key_user_stream(*, listen_key: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `listen_key` — query `listenKey`
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, CloseAListenKeyUserStreamErrorBody]`
- **Error**: `CloseAListenKeyUserStreamErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CloseAListenKeyUserStreamErrorBody` | `binance/errors/close_a_listen_key_user_stream_error.py` |
| `Error` | `binance/models/error.py` |

### client.stream.create_a_listen_key_user_stream

- **Route**: `POST /api/v3/userDataStream`
- **Signature**: `def create_a_listen_key_user_stream(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `ApiV3UserDataStreamResponse`
- **Returns (raw)**: `ApiResult[ApiV3UserDataStreamResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApiV3UserDataStreamResponse` | `binance/models/api_v3_user_data_stream_response.py` |

### client.stream.ping_keep_alive_a_listen_key_user_stream

- **Route**: `PUT /api/v3/userDataStream`
- **Signature**: `def ping_keep_alive_a_listen_key_user_stream(*, listen_key: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `listen_key` — query `listenKey`
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, PingKeepAliveAListenKeyUserStreamApiErrorBody]`
- **Error**: `PingKeepAliveAListenKeyUserStreamApiErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PingKeepAliveAListenKeyUserStreamApiErrorBody` | `binance/errors/ping_keep_alive_a_listen_key_user_stream_api_error.py` |
| `Error` | `binance/models/error.py` |

