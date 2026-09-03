<!-- Generated file — do not edit; regenerated with the SDK. -->

# SimpleEarn — operations

Accessor: `client.simple_earn` · Source: `binance_public_spot_api/apis/simple_earn.py` · 24 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.simple_earn.get_collateral_record_user_data

- **Route**: `GET /sapi/v1/simple-earn/flexible/history/collateralRecord`
- **Auth**: `api_key_auth`
- **Signature**: `def get_collateral_record_user_data(timestamp: int, signature: str, *, product_id: str | None = None, start_time: int | None = None, end_time: int | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `product_id` — query `productId` · `start_time` — query `startTime` · `end_time` — query `endTime` · `current` — query · `size` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SimpleEarnFlexibleHistoryCollateralRecordResponse`
- **Returns (raw)**: `ApiResult[SapiV1SimpleEarnFlexibleHistoryCollateralRecordResponse, GetCollateralRecordUserDataErrorBody]`
- **Error**: `GetCollateralRecordUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SimpleEarnFlexibleHistoryCollateralRecordResponse` | `binance_public_spot_api/models/sapi_v1_simple_earn_flexible_history_collateral_record_response.py` |
| `GetCollateralRecordUserDataErrorBody` | `binance_public_spot_api/errors/get_collateral_record_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.simple_earn.get_flexible_personal_left_quota_user_data

- **Route**: `GET /sapi/v1/simple-earn/flexible/personalLeftQuota`
- **Auth**: `api_key_auth`
- **Signature**: `def get_flexible_personal_left_quota_user_data(product_id: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `product_id`, `timestamp`, `signature`
- **Params**: `product_id` — query `productId` · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SimpleEarnFlexiblePersonalLeftQuotaResponse`
- **Returns (raw)**: `ApiResult[SapiV1SimpleEarnFlexiblePersonalLeftQuotaResponse, GetFlexiblePersonalLeftQuotaUserDataErrorBody]`
- **Error**: `GetFlexiblePersonalLeftQuotaUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SimpleEarnFlexiblePersonalLeftQuotaResponse` | `binance_public_spot_api/models/sapi_v1_simple_earn_flexible_personal_left_quota_response.py` |
| `GetFlexiblePersonalLeftQuotaUserDataErrorBody` | `binance_public_spot_api/errors/get_flexible_personal_left_quota_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.simple_earn.get_flexible_product_position_user_data

- **Route**: `GET /sapi/v1/simple-earn/flexible/position`
- **Auth**: `api_key_auth`
- **Signature**: `def get_flexible_product_position_user_data(timestamp: int, signature: str, *, asset: str | None = None, product_id: str | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `asset` — query · `product_id` — query `productId` · `current` — query · `size` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SimpleEarnFlexiblePositionResponse`
- **Returns (raw)**: `ApiResult[SapiV1SimpleEarnFlexiblePositionResponse, GetFlexibleProductPositionUserDataErrorBody]`
- **Error**: `GetFlexibleProductPositionUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SimpleEarnFlexiblePositionResponse` | `binance_public_spot_api/models/sapi_v1_simple_earn_flexible_position_response.py` |
| `GetFlexibleProductPositionUserDataErrorBody` | `binance_public_spot_api/errors/get_flexible_product_position_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.simple_earn.get_flexible_redemption_record_user_data

- **Route**: `GET /sapi/v1/simple-earn/flexible/history/redemptionRecord`
- **Auth**: `api_key_auth`
- **Signature**: `def get_flexible_redemption_record_user_data(*, product_id: str | None = None, redeem_id: str | None = None, asset: str | None = None, start_time: int | None = None, end_time: int | None = None, current: int | None = None, size: int | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `product_id` — query `productId` · `redeem_id` — query `redeemId` · `asset` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `current` — query · `size` — query
- **Returns (parsed)**: `SapiV1SimpleEarnFlexibleHistoryRedemptionRecordResponse`
- **Returns (raw)**: `ApiResult[SapiV1SimpleEarnFlexibleHistoryRedemptionRecordResponse, GetFlexibleRedemptionRecordUserDataErrorBody]`
- **Error**: `GetFlexibleRedemptionRecordUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SimpleEarnFlexibleHistoryRedemptionRecordResponse` | `binance_public_spot_api/models/sapi_v1_simple_earn_flexible_history_redemption_record_response.py` |
| `GetFlexibleRedemptionRecordUserDataErrorBody` | `binance_public_spot_api/errors/get_flexible_redemption_record_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.simple_earn.get_flexible_rewards_history_user_data

- **Route**: `GET /sapi/v1/simple-earn/flexible/history/rewardsRecord`
- **Auth**: `api_key_auth`
- **Signature**: `def get_flexible_rewards_history_user_data(type_: str, *, product_id: str | None = None, asset: str | None = None, start_time: int | None = None, end_time: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `type_`
- **Params**: `type_` — query `type` · `product_id` — query `productId` · `asset` — query · `start_time` — query `startTime` · `end_time` — query `endTime`
- **Returns (parsed)**: `SapiV1SimpleEarnFlexibleHistoryRewardsRecordResponse`
- **Returns (raw)**: `ApiResult[SapiV1SimpleEarnFlexibleHistoryRewardsRecordResponse, GetFlexibleRewardsHistoryUserDataErrorBody]`
- **Error**: `GetFlexibleRewardsHistoryUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SimpleEarnFlexibleHistoryRewardsRecordResponse` | `binance_public_spot_api/models/sapi_v1_simple_earn_flexible_history_rewards_record_response.py` |
| `GetFlexibleRewardsHistoryUserDataErrorBody` | `binance_public_spot_api/errors/get_flexible_rewards_history_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.simple_earn.get_flexible_subscription_preview_user_data

- **Route**: `GET /sapi/v1/simple-earn/flexible/subscriptionPreview`
- **Auth**: `api_key_auth`
- **Signature**: `def get_flexible_subscription_preview_user_data(product_id: str, amount: float, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `product_id`, `amount`, `timestamp`, `signature`
- **Params**: `product_id` — query `productId` · `amount` — query · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SimpleEarnFlexibleSubscriptionPreviewResponse`
- **Returns (raw)**: `ApiResult[SapiV1SimpleEarnFlexibleSubscriptionPreviewResponse, GetFlexibleSubscriptionPreviewUserDataErrorBody]`
- **Error**: `GetFlexibleSubscriptionPreviewUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SimpleEarnFlexibleSubscriptionPreviewResponse` | `binance_public_spot_api/models/sapi_v1_simple_earn_flexible_subscription_preview_response.py` |
| `GetFlexibleSubscriptionPreviewUserDataErrorBody` | `binance_public_spot_api/errors/get_flexible_subscription_preview_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.simple_earn.get_flexible_subscription_record_user_data

- **Route**: `GET /sapi/v1/simple-earn/flexible/history/subscriptionRecord`
- **Auth**: `api_key_auth`
- **Signature**: `def get_flexible_subscription_record_user_data(timestamp: int, signature: str, *, product_id: str | None = None, purchase_id: str | None = None, asset: str | None = None, start_time: int | None = None, end_time: int | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `product_id` — query `productId` · `purchase_id` — query `purchaseId` · `asset` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `current` — query · `size` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SimpleEarnFlexibleHistorySubscriptionRecordResponse`
- **Returns (raw)**: `ApiResult[SapiV1SimpleEarnFlexibleHistorySubscriptionRecordResponse, GetFlexibleSubscriptionRecordUserDataErrorBody]`
- **Error**: `GetFlexibleSubscriptionRecordUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SimpleEarnFlexibleHistorySubscriptionRecordResponse` | `binance_public_spot_api/models/sapi_v1_simple_earn_flexible_history_subscription_record_response.py` |
| `GetFlexibleSubscriptionRecordUserDataErrorBody` | `binance_public_spot_api/errors/get_flexible_subscription_record_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.simple_earn.get_locked_personal_left_quota_user_data

- **Route**: `GET /sapi/v1/simple-earn/locked/personalLeftQuota`
- **Auth**: `api_key_auth`
- **Signature**: `def get_locked_personal_left_quota_user_data(project_id: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`, `timestamp`, `signature`
- **Params**: `project_id` — query `projectId` · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SimpleEarnLockedPersonalLeftQuotaResponse`
- **Returns (raw)**: `ApiResult[SapiV1SimpleEarnLockedPersonalLeftQuotaResponse, GetLockedPersonalLeftQuotaUserDataErrorBody]`
- **Error**: `GetLockedPersonalLeftQuotaUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SimpleEarnLockedPersonalLeftQuotaResponse` | `binance_public_spot_api/models/sapi_v1_simple_earn_locked_personal_left_quota_response.py` |
| `GetLockedPersonalLeftQuotaUserDataErrorBody` | `binance_public_spot_api/errors/get_locked_personal_left_quota_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.simple_earn.get_locked_product_position_user_data

- **Route**: `GET /sapi/v1/simple-earn/locked/position`
- **Auth**: `api_key_auth`
- **Signature**: `def get_locked_product_position_user_data(timestamp: int, signature: str, *, asset: str | None = None, position_id: str | None = None, project_id: str | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `asset` — query · `position_id` — query `positionId` · `project_id` — query `projectId` · `current` — query · `size` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SimpleEarnLockedPositionResponse`
- **Returns (raw)**: `ApiResult[SapiV1SimpleEarnLockedPositionResponse, GetLockedProductPositionUserDataErrorBody]`
- **Error**: `GetLockedProductPositionUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SimpleEarnLockedPositionResponse` | `binance_public_spot_api/models/sapi_v1_simple_earn_locked_position_response.py` |
| `GetLockedProductPositionUserDataErrorBody` | `binance_public_spot_api/errors/get_locked_product_position_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.simple_earn.get_locked_redemption_record_user_data

- **Route**: `GET /sapi/v1/simple-earn/locked/history/redemptionRecord`
- **Auth**: `api_key_auth`
- **Signature**: `def get_locked_redemption_record_user_data(timestamp: int, signature: str, *, position_id: str | None = None, redeem_id: str | None = None, asset: str | None = None, start_time: int | None = None, end_time: int | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `position_id` — query `positionId` · `redeem_id` — query `redeemId` · `asset` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `current` — query · `size` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SimpleEarnLockedHistoryRedemptionRecordResponse`
- **Returns (raw)**: `ApiResult[SapiV1SimpleEarnLockedHistoryRedemptionRecordResponse, GetLockedRedemptionRecordUserDataErrorBody]`
- **Error**: `GetLockedRedemptionRecordUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SimpleEarnLockedHistoryRedemptionRecordResponse` | `binance_public_spot_api/models/sapi_v1_simple_earn_locked_history_redemption_record_response.py` |
| `GetLockedRedemptionRecordUserDataErrorBody` | `binance_public_spot_api/errors/get_locked_redemption_record_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.simple_earn.get_locked_rewards_history_user_data

- **Route**: `GET /sapi/v1/simple-earn/locked/history/rewardsRecord`
- **Auth**: `api_key_auth`
- **Signature**: `def get_locked_rewards_history_user_data(timestamp: int, signature: str, *, position_id: str | None = None, asset: str | None = None, start_time: int | None = None, end_time: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `position_id` — query `positionId` · `asset` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `size` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SimpleEarnLockedHistoryRewardsRecordResponse`
- **Returns (raw)**: `ApiResult[SapiV1SimpleEarnLockedHistoryRewardsRecordResponse, GetLockedRewardsHistoryUserDataErrorBody]`
- **Error**: `GetLockedRewardsHistoryUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SimpleEarnLockedHistoryRewardsRecordResponse` | `binance_public_spot_api/models/sapi_v1_simple_earn_locked_history_rewards_record_response.py` |
| `GetLockedRewardsHistoryUserDataErrorBody` | `binance_public_spot_api/errors/get_locked_rewards_history_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.simple_earn.get_locked_subscription_preview_user_data

- **Route**: `GET /sapi/v1/simple-earn/locked/subscriptionPreview`
- **Auth**: `api_key_auth`
- **Signature**: `def get_locked_subscription_preview_user_data(project_id: str, amount: float, timestamp: int, signature: str, *, auto_subscribe: bool | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`, `amount`, `timestamp`, `signature`
- **Params**: `project_id` — query `projectId` · `amount` — query · `timestamp` — query · `signature` — query · `auto_subscribe` — query `autoSubscribe` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1SimpleEarnLockedSubscriptionPreviewResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1SimpleEarnLockedSubscriptionPreviewResponse], GetLockedSubscriptionPreviewUserDataErrorBody]`
- **Error**: `GetLockedSubscriptionPreviewUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SimpleEarnLockedSubscriptionPreviewResponse` | `binance_public_spot_api/models/sapi_v1_simple_earn_locked_subscription_preview_response.py` |
| `GetLockedSubscriptionPreviewUserDataErrorBody` | `binance_public_spot_api/errors/get_locked_subscription_preview_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.simple_earn.get_locked_subscription_record_user_data

- **Route**: `GET /sapi/v1/simple-earn/locked/history/subscriptionRecord`
- **Auth**: `api_key_auth`
- **Signature**: `def get_locked_subscription_record_user_data(timestamp: int, signature: str, *, purchase_id: str | None = None, asset: str | None = None, start_time: int | None = None, end_time: int | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `purchase_id` — query `purchaseId` · `asset` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `current` — query · `size` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SimpleEarnLockedHistorySubscriptionRecordResponse`
- **Returns (raw)**: `ApiResult[SapiV1SimpleEarnLockedHistorySubscriptionRecordResponse, GetLockedSubscriptionRecordUserDataErrorBody]`
- **Error**: `GetLockedSubscriptionRecordUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SimpleEarnLockedHistorySubscriptionRecordResponse` | `binance_public_spot_api/models/sapi_v1_simple_earn_locked_history_subscription_record_response.py` |
| `GetLockedSubscriptionRecordUserDataErrorBody` | `binance_public_spot_api/errors/get_locked_subscription_record_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.simple_earn.get_rate_history_user_data

- **Route**: `GET /sapi/v1/simple-earn/flexible/history/rateHistory`
- **Auth**: `api_key_auth`
- **Signature**: `def get_rate_history_user_data(product_id: str, timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `product_id`, `timestamp`, `signature`
- **Params**: `product_id` — query `productId` · `timestamp` — query · `signature` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `current` — query · `size` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SimpleEarnFlexibleHistoryRateHistoryResponse`
- **Returns (raw)**: `ApiResult[SapiV1SimpleEarnFlexibleHistoryRateHistoryResponse, GetRateHistoryUserDataErrorBody]`
- **Error**: `GetRateHistoryUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SimpleEarnFlexibleHistoryRateHistoryResponse` | `binance_public_spot_api/models/sapi_v1_simple_earn_flexible_history_rate_history_response.py` |
| `GetRateHistoryUserDataErrorBody` | `binance_public_spot_api/errors/get_rate_history_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.simple_earn.get_simple_earn_flexible_product_list_user_data

- **Route**: `GET /sapi/v1/simple-earn/flexible/list`
- **Auth**: `api_key_auth`
- **Signature**: `def get_simple_earn_flexible_product_list_user_data(timestamp: int, signature: str, *, asset: str | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `asset` — query · `current` — query · `size` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SimpleEarnFlexibleListResponse`
- **Returns (raw)**: `ApiResult[SapiV1SimpleEarnFlexibleListResponse, GetSimpleEarnFlexibleProductListUserDataErrorBody]`
- **Error**: `GetSimpleEarnFlexibleProductListUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SimpleEarnFlexibleListResponse` | `binance_public_spot_api/models/sapi_v1_simple_earn_flexible_list_response.py` |
| `GetSimpleEarnFlexibleProductListUserDataErrorBody` | `binance_public_spot_api/errors/get_simple_earn_flexible_product_list_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.simple_earn.get_simple_earn_locked_product_list_user_data

- **Route**: `GET /sapi/v1/simple-earn/locked/list`
- **Auth**: `api_key_auth`
- **Signature**: `def get_simple_earn_locked_product_list_user_data(timestamp: int, signature: str, *, asset: str | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `asset` — query · `current` — query · `size` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SimpleEarnLockedListResponse`
- **Returns (raw)**: `ApiResult[SapiV1SimpleEarnLockedListResponse, GetSimpleEarnLockedProductListUserDataErrorBody]`
- **Error**: `GetSimpleEarnLockedProductListUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SimpleEarnLockedListResponse` | `binance_public_spot_api/models/sapi_v1_simple_earn_locked_list_response.py` |
| `GetSimpleEarnLockedProductListUserDataErrorBody` | `binance_public_spot_api/errors/get_simple_earn_locked_product_list_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.simple_earn.redeem_flexible_product_trade

- **Route**: `POST /sapi/v1/simple-earn/flexible/redeem`
- **Auth**: `api_key_auth`
- **Signature**: `def redeem_flexible_product_trade(product_id: str, timestamp: int, signature: str, *, redeem_all: bool | None = None, amount: float | None = None, dest_account: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `product_id`, `timestamp`, `signature`
- **Params**: `product_id` — query `productId` · `timestamp` — query · `signature` — query · `redeem_all` — query `redeemAll` · `amount` — query · `dest_account` — query `destAccount` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SimpleEarnFlexibleRedeemResponse`
- **Returns (raw)**: `ApiResult[SapiV1SimpleEarnFlexibleRedeemResponse, RedeemFlexibleProductTradeErrorBody]`
- **Error**: `RedeemFlexibleProductTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SimpleEarnFlexibleRedeemResponse` | `binance_public_spot_api/models/sapi_v1_simple_earn_flexible_redeem_response.py` |
| `RedeemFlexibleProductTradeErrorBody` | `binance_public_spot_api/errors/redeem_flexible_product_trade_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.simple_earn.redeem_locked_product_trade

- **Route**: `POST /sapi/v1/simple-earn/locked/redeem`
- **Auth**: `api_key_auth`
- **Signature**: `def redeem_locked_product_trade(position_id: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `position_id`, `timestamp`, `signature`
- **Params**: `position_id` — query `positionId` · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SimpleEarnLockedRedeemResponse`
- **Returns (raw)**: `ApiResult[SapiV1SimpleEarnLockedRedeemResponse, RedeemLockedProductTradeErrorBody]`
- **Error**: `RedeemLockedProductTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SimpleEarnLockedRedeemResponse` | `binance_public_spot_api/models/sapi_v1_simple_earn_locked_redeem_response.py` |
| `RedeemLockedProductTradeErrorBody` | `binance_public_spot_api/errors/redeem_locked_product_trade_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.simple_earn.set_flexible_auto_subscribe_user_data

- **Route**: `POST /sapi/v1/simple-earn/flexible/setAutoSubscribe`
- **Auth**: `api_key_auth`
- **Signature**: `def set_flexible_auto_subscribe_user_data(product_id: str, auto_subscribe: bool, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `product_id`, `auto_subscribe`, `timestamp`, `signature`
- **Params**: `product_id` — query `productId` · `auto_subscribe` — query `autoSubscribe` · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SimpleEarnFlexibleSetAutoSubscribeResponse`
- **Returns (raw)**: `ApiResult[SapiV1SimpleEarnFlexibleSetAutoSubscribeResponse, SetFlexibleAutoSubscribeUserDataErrorBody]`
- **Error**: `SetFlexibleAutoSubscribeUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SimpleEarnFlexibleSetAutoSubscribeResponse` | `binance_public_spot_api/models/sapi_v1_simple_earn_flexible_set_auto_subscribe_response.py` |
| `SetFlexibleAutoSubscribeUserDataErrorBody` | `binance_public_spot_api/errors/set_flexible_auto_subscribe_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.simple_earn.set_locked_auto_subscribe_user_data

- **Route**: `POST /sapi/v1/simple-earn/locked/setAutoSubscribe`
- **Auth**: `api_key_auth`
- **Signature**: `def set_locked_auto_subscribe_user_data(position_id: str, auto_subscribe: bool, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `position_id`, `auto_subscribe`, `timestamp`, `signature`
- **Params**: `position_id` — query `positionId` · `auto_subscribe` — query `autoSubscribe` · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SimpleEarnLockedSetAutoSubscribeResponse`
- **Returns (raw)**: `ApiResult[SapiV1SimpleEarnLockedSetAutoSubscribeResponse, SetLockedAutoSubscribeUserDataErrorBody]`
- **Error**: `SetLockedAutoSubscribeUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SimpleEarnLockedSetAutoSubscribeResponse` | `binance_public_spot_api/models/sapi_v1_simple_earn_locked_set_auto_subscribe_response.py` |
| `SetLockedAutoSubscribeUserDataErrorBody` | `binance_public_spot_api/errors/set_locked_auto_subscribe_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.simple_earn.set_locked_product_redeem_option_user_data

- **Route**: `GET /sapi/v1/simple-earn/locked/setRedeemOption`
- **Auth**: `api_key_auth`
- **Signature**: `def set_locked_product_redeem_option_user_data(position_id: str, timestamp: int, signature: str, *, redeem_to: RedeemToOrStr | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `position_id`, `timestamp`, `signature`
- **Params**: `position_id` — query `positionId` · `timestamp` — query · `signature` — query · `redeem_to` — query `redeemTo` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SimpleEarnLockedSetRedeemOptionResponse`
- **Returns (raw)**: `ApiResult[SapiV1SimpleEarnLockedSetRedeemOptionResponse, SetLockedProductRedeemOptionUserDataErrorBody]`
- **Error**: `SetLockedProductRedeemOptionUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RedeemToOrStr` | `binance_public_spot_api/models/enums/redeem_to.py` |
| `SapiV1SimpleEarnLockedSetRedeemOptionResponse` | `binance_public_spot_api/models/sapi_v1_simple_earn_locked_set_redeem_option_response.py` |
| `SetLockedProductRedeemOptionUserDataErrorBody` | `binance_public_spot_api/errors/set_locked_product_redeem_option_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.simple_earn.simple_account_user_data

- **Route**: `GET /sapi/v1/simple-earn/account`
- **Auth**: `api_key_auth`
- **Signature**: `def simple_account_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SimpleEarnAccountResponse`
- **Returns (raw)**: `ApiResult[SapiV1SimpleEarnAccountResponse, SimpleAccountUserDataErrorBody]`
- **Error**: `SimpleAccountUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SimpleEarnAccountResponse` | `binance_public_spot_api/models/sapi_v1_simple_earn_account_response.py` |
| `SimpleAccountUserDataErrorBody` | `binance_public_spot_api/errors/simple_account_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.simple_earn.subscribe_flexible_product_trade

- **Route**: `POST /sapi/v1/simple-earn/flexible/subscribe`
- **Auth**: `api_key_auth`
- **Signature**: `def subscribe_flexible_product_trade(product_id: str, amount: float, timestamp: int, signature: str, *, auto_subscribe: bool | None = None, source_account: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `product_id`, `amount`, `timestamp`, `signature`
- **Params**: `product_id` — query `productId` · `amount` — query · `timestamp` — query · `signature` — query · `auto_subscribe` — query `autoSubscribe` · `source_account` — query `sourceAccount` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SimpleEarnFlexibleSubscribeResponse`
- **Returns (raw)**: `ApiResult[SapiV1SimpleEarnFlexibleSubscribeResponse, SubscribeFlexibleProductTradeErrorBody]`
- **Error**: `SubscribeFlexibleProductTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SimpleEarnFlexibleSubscribeResponse` | `binance_public_spot_api/models/sapi_v1_simple_earn_flexible_subscribe_response.py` |
| `SubscribeFlexibleProductTradeErrorBody` | `binance_public_spot_api/errors/subscribe_flexible_product_trade_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.simple_earn.subscribe_locked_product_trade

- **Route**: `POST /sapi/v1/simple-earn/locked/subscribe`
- **Auth**: `api_key_auth`
- **Signature**: `def subscribe_locked_product_trade(project_id: str, amount: float, timestamp: int, signature: str, *, auto_subscribe: bool | None = None, source_account: str | None = None, redeem_to: RedeemToOrStr | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`, `amount`, `timestamp`, `signature`
- **Params**: `project_id` — query `projectId` · `amount` — query · `timestamp` — query · `signature` — query · `auto_subscribe` — query `autoSubscribe` · `source_account` — query `sourceAccount` · `redeem_to` — query `redeemTo` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SimpleEarnLockedSubscribeResponse`
- **Returns (raw)**: `ApiResult[SapiV1SimpleEarnLockedSubscribeResponse, SubscribeLockedProductTradeErrorBody]`
- **Error**: `SubscribeLockedProductTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RedeemToOrStr` | `binance_public_spot_api/models/enums/redeem_to.py` |
| `SapiV1SimpleEarnLockedSubscribeResponse` | `binance_public_spot_api/models/sapi_v1_simple_earn_locked_subscribe_response.py` |
| `SubscribeLockedProductTradeErrorBody` | `binance_public_spot_api/errors/subscribe_locked_product_trade_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

