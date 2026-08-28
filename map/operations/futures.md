<!-- Generated file — do not edit; regenerated with the SDK. -->

# Futures — operations

Accessor: `client.futures` · Source: `binance/apis/futures.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.futures.get_future_account_transaction_history_list_user_data

- **Route**: `GET /sapi/v1/futures/transfer`
- **Signature**: `def get_future_account_transaction_history_list_user_data(asset: str, start_time: int, timestamp: int, signature: str, *, end_time: int | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `asset`, `start_time`, `timestamp`, `signature`
- **Params**: `asset` — query · `start_time` — query `startTime` · `timestamp` — query · `signature` — query · `end_time` — query `endTime` · `current` — query · `size` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1FuturesTransferResponse1`
- **Returns (raw)**: `ApiResult[SapiV1FuturesTransferResponse1, GetFutureAccountTransactionHistoryListUserDataErrorBody]`
- **Error**: `GetFutureAccountTransactionHistoryListUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1FuturesTransferResponse1` | `binance/models/sapi_v1_futures_transfer_response1.py` |
| `GetFutureAccountTransactionHistoryListUserDataErrorBody` | `binance/errors/get_future_account_transaction_history_list_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.futures.get_future_tick_level_orderbook_historical_data_download_link_user_data

- **Route**: `GET /sapi/v1/futures/histDataLink`
- **Signature**: `def get_future_tick_level_orderbook_historical_data_download_link_user_data(symbol: str, data_type: DataTypeOrStr, timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `data_type`, `timestamp`, `signature`
- **Params**: `symbol` — query · `data_type` — query `dataType` · `timestamp` — query · `signature` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1FuturesHistDataLinkResponse`
- **Returns (raw)**: `ApiResult[SapiV1FuturesHistDataLinkResponse, GetFutureTickLevelOrderbookHistoricalDataDownloadLinkUserDataErrorBody]`
- **Error**: `GetFutureTickLevelOrderbookHistoricalDataDownloadLinkUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DataTypeOrStr` | `binance/models/enums/data_type.py` |
| `SapiV1FuturesHistDataLinkResponse` | `binance/models/sapi_v1_futures_hist_data_link_response.py` |
| `GetFutureTickLevelOrderbookHistoricalDataDownloadLinkUserDataErrorBody` | `binance/errors/get_future_tick_level_orderbook_historical_data_download_link_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.futures.new_future_account_transfer_user_data

- **Route**: `POST /sapi/v1/futures/transfer`
- **Signature**: `def new_future_account_transfer_user_data(asset: str, amount: float, type_: int, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `asset`, `amount`, `type_`, `timestamp`, `signature`
- **Params**: `asset` — query · `amount` — query · `type_` — query `type` · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1FuturesTransferResponse`
- **Returns (raw)**: `ApiResult[SapiV1FuturesTransferResponse, NewFutureAccountTransferUserDataErrorBody]`
- **Error**: `NewFutureAccountTransferUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1FuturesTransferResponse` | `binance/models/sapi_v1_futures_transfer_response.py` |
| `NewFutureAccountTransferUserDataErrorBody` | `binance/errors/new_future_account_transfer_user_data_error.py` |
| `Error` | `binance/models/error.py` |

