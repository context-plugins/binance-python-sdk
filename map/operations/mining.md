<!-- Generated file — do not edit; regenerated with the SDK. -->

# Mining — operations

Accessor: `client.mining` · Source: `binance_public_spot_api/apis/mining.py` · 13 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.mining.account_list_user_data

- **Route**: `GET /sapi/v1/mining/statistics/user/list`
- **Auth**: `api_key_auth`
- **Signature**: `def account_list_user_data(algo: str, user_name: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `algo`, `user_name`, `timestamp`, `signature`
- **Params**: `algo` — query · `user_name` — query `userName` · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1MiningStatisticsUserListResponse`
- **Returns (raw)**: `ApiResult[SapiV1MiningStatisticsUserListResponse, AccountListUserDataErrorBody]`
- **Error**: `AccountListUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MiningStatisticsUserListResponse` | `binance_public_spot_api/models/sapi_v1_mining_statistics_user_list_response.py` |
| `AccountListUserDataErrorBody` | `binance_public_spot_api/errors/account_list_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.mining.acquiring_algorithm_market_data

- **Route**: `GET /sapi/v1/mining/pub/algoList`
- **Auth**: `api_key_auth`
- **Signature**: `def acquiring_algorithm_market_data(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `SapiV1MiningPubAlgoListResponse`
- **Returns (raw)**: `ApiResult[SapiV1MiningPubAlgoListResponse, AcquiringAlgorithmMarketDataErrorBody]`
- **Error**: `AcquiringAlgorithmMarketDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MiningPubAlgoListResponse` | `binance_public_spot_api/models/sapi_v1_mining_pub_algo_list_response.py` |
| `AcquiringAlgorithmMarketDataErrorBody` | `binance_public_spot_api/errors/acquiring_algorithm_market_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.mining.acquiring_coin_name_market_data

- **Route**: `GET /sapi/v1/mining/pub/coinList`
- **Auth**: `api_key_auth`
- **Signature**: `def acquiring_coin_name_market_data(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `SapiV1MiningPubCoinListResponse`
- **Returns (raw)**: `ApiResult[SapiV1MiningPubCoinListResponse, AcquiringCoinNameMarketDataErrorBody]`
- **Error**: `AcquiringCoinNameMarketDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MiningPubCoinListResponse` | `binance_public_spot_api/models/sapi_v1_mining_pub_coin_list_response.py` |
| `AcquiringCoinNameMarketDataErrorBody` | `binance_public_spot_api/errors/acquiring_coin_name_market_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.mining.cancel_hashrate_resale_configuration_user_data

- **Route**: `POST /sapi/v1/mining/hash-transfer/config/cancel`
- **Auth**: `api_key_auth`
- **Signature**: `def cancel_hashrate_resale_configuration_user_data(config_id: str, user_name: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `config_id`, `user_name`, `timestamp`, `signature`
- **Params**: `config_id` — query `configId` · `user_name` — query `userName` · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1MiningHashTransferConfigCancelResponse`
- **Returns (raw)**: `ApiResult[SapiV1MiningHashTransferConfigCancelResponse, CancelHashrateResaleConfigurationUserDataErrorBody]`
- **Error**: `CancelHashrateResaleConfigurationUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MiningHashTransferConfigCancelResponse` | `binance_public_spot_api/models/sapi_v1_mining_hash_transfer_config_cancel_response.py` |
| `CancelHashrateResaleConfigurationUserDataErrorBody` | `binance_public_spot_api/errors/cancel_hashrate_resale_configuration_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.mining.earnings_list_user_data

- **Route**: `GET /sapi/v1/mining/payment/list`
- **Auth**: `api_key_auth`
- **Signature**: `def earnings_list_user_data(algo: str, user_name: str, timestamp: int, signature: str, *, coin: str | None = None, start_date: str | None = None, end_date: str | None = None, page_index: int | None = None, page_size: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `algo`, `user_name`, `timestamp`, `signature`
- **Params**: `algo` — query · `user_name` — query `userName` · `timestamp` — query · `signature` — query · `coin` — query · `start_date` — query `startDate` · `end_date` — query `endDate` · `page_index` — query `pageIndex` · `page_size` — query `pageSize` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1MiningPaymentListResponse`
- **Returns (raw)**: `ApiResult[SapiV1MiningPaymentListResponse, EarningsListUserDataErrorBody]`
- **Error**: `EarningsListUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MiningPaymentListResponse` | `binance_public_spot_api/models/sapi_v1_mining_payment_list_response.py` |
| `EarningsListUserDataErrorBody` | `binance_public_spot_api/errors/earnings_list_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.mining.extra_bonus_list_user_data

- **Route**: `GET /sapi/v1/mining/payment/other`
- **Auth**: `api_key_auth`
- **Signature**: `def extra_bonus_list_user_data(algo: str, user_name: str, timestamp: int, signature: str, *, coin: str | None = None, start_date: str | None = None, end_date: str | None = None, page_index: int | None = None, page_size: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `algo`, `user_name`, `timestamp`, `signature`
- **Params**: `algo` — query · `user_name` — query `userName` · `timestamp` — query · `signature` — query · `coin` — query · `start_date` — query `startDate` · `end_date` — query `endDate` · `page_index` — query `pageIndex` · `page_size` — query `pageSize` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1MiningPaymentOtherResponse`
- **Returns (raw)**: `ApiResult[SapiV1MiningPaymentOtherResponse, ExtraBonusListUserDataErrorBody]`
- **Error**: `ExtraBonusListUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MiningPaymentOtherResponse` | `binance_public_spot_api/models/sapi_v1_mining_payment_other_response.py` |
| `ExtraBonusListUserDataErrorBody` | `binance_public_spot_api/errors/extra_bonus_list_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.mining.hashrate_resale_details_user_data

- **Route**: `GET /sapi/v1/mining/hash-transfer/profit/details`
- **Auth**: `api_key_auth`
- **Signature**: `def hashrate_resale_details_user_data(config_id: str, user_name: str, timestamp: int, signature: str, *, page_index: int | None = None, page_size: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `config_id`, `user_name`, `timestamp`, `signature`
- **Params**: `config_id` — query `configId` · `user_name` — query `userName` · `timestamp` — query · `signature` — query · `page_index` — query `pageIndex` · `page_size` — query `pageSize` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1MiningHashTransferProfitDetailsResponse`
- **Returns (raw)**: `ApiResult[SapiV1MiningHashTransferProfitDetailsResponse, HashrateResaleDetailsUserDataErrorBody]`
- **Error**: `HashrateResaleDetailsUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MiningHashTransferProfitDetailsResponse` | `binance_public_spot_api/models/sapi_v1_mining_hash_transfer_profit_details_response.py` |
| `HashrateResaleDetailsUserDataErrorBody` | `binance_public_spot_api/errors/hashrate_resale_details_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.mining.hashrate_resale_list_user_data

- **Route**: `GET /sapi/v1/mining/hash-transfer/config/details/list`
- **Auth**: `api_key_auth`
- **Signature**: `def hashrate_resale_list_user_data(timestamp: int, signature: str, *, page_index: int | None = None, page_size: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `page_index` — query `pageIndex` · `page_size` — query `pageSize` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1MiningHashTransferConfigDetailsListResponse`
- **Returns (raw)**: `ApiResult[SapiV1MiningHashTransferConfigDetailsListResponse, HashrateResaleListUserDataErrorBody]`
- **Error**: `HashrateResaleListUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MiningHashTransferConfigDetailsListResponse` | `binance_public_spot_api/models/sapi_v1_mining_hash_transfer_config_details_list_response.py` |
| `HashrateResaleListUserDataErrorBody` | `binance_public_spot_api/errors/hashrate_resale_list_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.mining.hashrate_resale_request_user_data

- **Route**: `POST /sapi/v1/mining/hash-transfer/config`
- **Auth**: `api_key_auth`
- **Signature**: `def hashrate_resale_request_user_data(user_name: str, algo: str, to_pool_user: str, hash_rate: str, timestamp: int, signature: str, *, start_date: str | None = None, end_date: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_name`, `algo`, `to_pool_user`, `hash_rate`, `timestamp`, `signature`
- **Params**: `user_name` — query `userName` · `algo` — query · `to_pool_user` — query `toPoolUser` · `hash_rate` — query `hashRate` · `timestamp` — query · `signature` — query · `start_date` — query `startDate` · `end_date` — query `endDate` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1MiningHashTransferConfigResponse`
- **Returns (raw)**: `ApiResult[SapiV1MiningHashTransferConfigResponse, HashrateResaleRequestUserDataErrorBody]`
- **Error**: `HashrateResaleRequestUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MiningHashTransferConfigResponse` | `binance_public_spot_api/models/sapi_v1_mining_hash_transfer_config_response.py` |
| `HashrateResaleRequestUserDataErrorBody` | `binance_public_spot_api/errors/hashrate_resale_request_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.mining.mining_account_earning_user_data

- **Route**: `GET /sapi/v1/mining/payment/uid`
- **Auth**: `api_key_auth`
- **Signature**: `def mining_account_earning_user_data(algo: str, timestamp: int, signature: str, *, start_date: str | None = None, end_date: str | None = None, page_index: int | None = None, page_size: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `algo`, `timestamp`, `signature`
- **Params**: `algo` — query · `timestamp` — query · `signature` — query · `start_date` — query `startDate` · `end_date` — query `endDate` · `page_index` — query `pageIndex` · `page_size` — query `pageSize` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1MiningPaymentUidResponse`
- **Returns (raw)**: `ApiResult[SapiV1MiningPaymentUidResponse, MiningAccountEarningUserDataErrorBody]`
- **Error**: `MiningAccountEarningUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MiningPaymentUidResponse` | `binance_public_spot_api/models/sapi_v1_mining_payment_uid_response.py` |
| `MiningAccountEarningUserDataErrorBody` | `binance_public_spot_api/errors/mining_account_earning_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.mining.request_for_detail_miner_list_user_data

- **Route**: `GET /sapi/v1/mining/worker/detail`
- **Auth**: `api_key_auth`
- **Signature**: `def request_for_detail_miner_list_user_data(algo: str, user_name: str, worker_name: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `algo`, `user_name`, `worker_name`, `timestamp`, `signature`
- **Params**: `algo` — query · `user_name` — query `userName` · `worker_name` — query `workerName` · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1MiningWorkerDetailResponse`
- **Returns (raw)**: `ApiResult[SapiV1MiningWorkerDetailResponse, RequestForDetailMinerListUserDataErrorBody]`
- **Error**: `RequestForDetailMinerListUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MiningWorkerDetailResponse` | `binance_public_spot_api/models/sapi_v1_mining_worker_detail_response.py` |
| `RequestForDetailMinerListUserDataErrorBody` | `binance_public_spot_api/errors/request_for_detail_miner_list_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.mining.request_for_miner_list_user_data

- **Route**: `GET /sapi/v1/mining/worker/list`
- **Auth**: `api_key_auth`
- **Signature**: `def request_for_miner_list_user_data(algo: str, user_name: str, timestamp: int, signature: str, *, page_index: int | None = None, sort: int | None = None, sort_column: int | None = None, worker_status: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `algo`, `user_name`, `timestamp`, `signature`
- **Params**: `algo` — query · `user_name` — query `userName` · `timestamp` — query · `signature` — query · `page_index` — query `pageIndex` · `sort` — query · `sort_column` — query `sortColumn` · `worker_status` — query `workerStatus` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1MiningWorkerListResponse`
- **Returns (raw)**: `ApiResult[SapiV1MiningWorkerListResponse, RequestForMinerListUserDataErrorBody]`
- **Error**: `RequestForMinerListUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MiningWorkerListResponse` | `binance_public_spot_api/models/sapi_v1_mining_worker_list_response.py` |
| `RequestForMinerListUserDataErrorBody` | `binance_public_spot_api/errors/request_for_miner_list_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.mining.statistic_list_user_data

- **Route**: `GET /sapi/v1/mining/statistics/user/status`
- **Auth**: `api_key_auth`
- **Signature**: `def statistic_list_user_data(algo: str, user_name: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `algo`, `user_name`, `timestamp`, `signature`
- **Params**: `algo` — query · `user_name` — query `userName` · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1MiningStatisticsUserStatusResponse`
- **Returns (raw)**: `ApiResult[SapiV1MiningStatisticsUserStatusResponse, StatisticListUserDataErrorBody]`
- **Error**: `StatisticListUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MiningStatisticsUserStatusResponse` | `binance_public_spot_api/models/sapi_v1_mining_statistics_user_status_response.py` |
| `StatisticListUserDataErrorBody` | `binance_public_spot_api/errors/statistic_list_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

