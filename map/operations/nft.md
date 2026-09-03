<!-- Generated file — do not edit; regenerated with the SDK. -->

# Nft — operations

Accessor: `client.nft` · Source: `binance_public_spot_api/apis/nft.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.nft.get_nft_asset_user_data

- **Route**: `GET /sapi/v1/nft/user/getAsset`
- **Auth**: `api_key_auth`
- **Signature**: `def get_nft_asset_user_data(timestamp: int, signature: str, *, limit: int | None = None, page: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `limit` — query · `page` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1NftUserGetAssetResponse`
- **Returns (raw)**: `ApiResult[SapiV1NftUserGetAssetResponse, GetNftAssetUserDataErrorBody]`
- **Error**: `GetNftAssetUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1NftUserGetAssetResponse` | `binance_public_spot_api/models/sapi_v1_nft_user_get_asset_response.py` |
| `GetNftAssetUserDataErrorBody` | `binance_public_spot_api/errors/get_nft_asset_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.nft.get_nft_deposit_history_user_data

- **Route**: `GET /sapi/v1/nft/history/deposit`
- **Auth**: `api_key_auth`
- **Signature**: `def get_nft_deposit_history_user_data(timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, limit: int | None = None, page: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `limit` — query · `page` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1NftHistoryDepositResponse`
- **Returns (raw)**: `ApiResult[SapiV1NftHistoryDepositResponse, GetNftDepositHistoryUserDataErrorBody]`
- **Error**: `GetNftDepositHistoryUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1NftHistoryDepositResponse` | `binance_public_spot_api/models/sapi_v1_nft_history_deposit_response.py` |
| `GetNftDepositHistoryUserDataErrorBody` | `binance_public_spot_api/errors/get_nft_deposit_history_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.nft.get_nft_transaction_history_user_data

- **Route**: `GET /sapi/v1/nft/history/transactions`
- **Auth**: `api_key_auth`
- **Signature**: `def get_nft_transaction_history_user_data(order_type: int, timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, limit: int | None = None, page: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `order_type`, `timestamp`, `signature`
- **Params**: `order_type` — query `orderType` · `timestamp` — query · `signature` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `limit` — query · `page` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1NftHistoryTransactionsResponse`
- **Returns (raw)**: `ApiResult[SapiV1NftHistoryTransactionsResponse, GetNftTransactionHistoryUserDataErrorBody]`
- **Error**: `GetNftTransactionHistoryUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1NftHistoryTransactionsResponse` | `binance_public_spot_api/models/sapi_v1_nft_history_transactions_response.py` |
| `GetNftTransactionHistoryUserDataErrorBody` | `binance_public_spot_api/errors/get_nft_transaction_history_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.nft.get_nft_withdraw_history_user_data

- **Route**: `GET /sapi/v1/nft/history/withdraw`
- **Auth**: `api_key_auth`
- **Signature**: `def get_nft_withdraw_history_user_data(timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, limit: int | None = None, page: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `limit` — query · `page` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1NftHistoryWithdrawResponse`
- **Returns (raw)**: `ApiResult[SapiV1NftHistoryWithdrawResponse, GetNftWithdrawHistoryUserDataErrorBody]`
- **Error**: `GetNftWithdrawHistoryUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1NftHistoryWithdrawResponse` | `binance_public_spot_api/models/sapi_v1_nft_history_withdraw_response.py` |
| `GetNftWithdrawHistoryUserDataErrorBody` | `binance_public_spot_api/errors/get_nft_withdraw_history_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

