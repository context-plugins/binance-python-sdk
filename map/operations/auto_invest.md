<!-- Generated file — do not edit; regenerated with the SDK. -->

# AutoInvest — operations

Accessor: `client.auto_invest` · Source: `binance_public_spot_api/apis/auto_invest.py` · 17 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.auto_invest.change_plan_status

- **Route**: `POST /sapi/v1/lending/auto-invest/plan/edit-status`
- **Auth**: `api_key_auth`
- **Signature**: `def change_plan_status(plan_id: int, status: Status1OrStr, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`, `status`, `timestamp`, `signature`
- **Params**: `plan_id` — query `planId` · `status` — query · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1LendingAutoInvestPlanEditStatusResponse`
- **Returns (raw)**: `ApiResult[SapiV1LendingAutoInvestPlanEditStatusResponse, ChangePlanStatusErrorBody]`
- **Error**: `ChangePlanStatusErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Status1OrStr` | `binance_public_spot_api/models/enums/status1.py` |
| `SapiV1LendingAutoInvestPlanEditStatusResponse` | `binance_public_spot_api/models/sapi_v1_lending_auto_invest_plan_edit_status_response.py` |
| `ChangePlanStatusErrorBody` | `binance_public_spot_api/errors/change_plan_status_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.auto_invest.get_list_of_plans

- **Route**: `GET /sapi/v1/lending/auto-invest/plan/list`
- **Auth**: `api_key_auth`
- **Signature**: `def get_list_of_plans(plan_type: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_type`, `timestamp`, `signature`
- **Params**: `plan_type` — query `planType` · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1LendingAutoInvestPlanListResponse`
- **Returns (raw)**: `ApiResult[SapiV1LendingAutoInvestPlanListResponse, GetListOfPlansErrorBody]`
- **Error**: `GetListOfPlansErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1LendingAutoInvestPlanListResponse` | `binance_public_spot_api/models/sapi_v1_lending_auto_invest_plan_list_response.py` |
| `GetListOfPlansErrorBody` | `binance_public_spot_api/errors/get_list_of_plans_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.auto_invest.get_target_asset_roi_data_user_data

- **Route**: `GET /sapi/v1/lending/auto-invest/target-asset/roi/list`
- **Auth**: `api_key_auth`
- **Signature**: `def get_target_asset_roi_data_user_data(target_asset: str, his_roi_type: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `target_asset`, `his_roi_type`, `timestamp`, `signature`
- **Params**: `target_asset` — query `targetAsset` · `his_roi_type` — query `hisRoiType` · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1LendingAutoInvestTargetAssetRoiListResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1LendingAutoInvestTargetAssetRoiListResponse], GetTargetAssetRoiDataUserDataErrorBody]`
- **Error**: `GetTargetAssetRoiDataUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1LendingAutoInvestTargetAssetRoiListResponse` | `binance_public_spot_api/models/sapi_v1_lending_auto_invest_target_asset_roi_list_response.py` |
| `GetTargetAssetRoiDataUserDataErrorBody` | `binance_public_spot_api/errors/get_target_asset_roi_data_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.auto_invest.get_target_asset_list_user_data

- **Route**: `GET /sapi/v1/lending/auto-invest/target-asset/list`
- **Auth**: `api_key_auth`
- **Signature**: `def get_target_asset_list_user_data(timestamp: int, signature: str, *, target_asset: str | None = None, size: int | None = None, current: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `target_asset` — query `targetAsset` · `size` — query · `current` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1LendingAutoInvestTargetAssetListResponse`
- **Returns (raw)**: `ApiResult[SapiV1LendingAutoInvestTargetAssetListResponse, GetTargetAssetListUserDataErrorBody]`
- **Error**: `GetTargetAssetListUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1LendingAutoInvestTargetAssetListResponse` | `binance_public_spot_api/models/sapi_v1_lending_auto_invest_target_asset_list_response.py` |
| `GetTargetAssetListUserDataErrorBody` | `binance_public_spot_api/errors/get_target_asset_list_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.auto_invest.index_linked_plan_rebalance_details_user_data

- **Route**: `GET /sapi/v1/lending/auto-invest/rebalance/history`
- **Auth**: `api_key_auth`
- **Signature**: `def index_linked_plan_rebalance_details_user_data(timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `current` — query · `size` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1LendingAutoInvestRebalanceHistoryResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1LendingAutoInvestRebalanceHistoryResponse], IndexLinkedPlanRebalanceDetailsUserDataErrorBody]`
- **Error**: `IndexLinkedPlanRebalanceDetailsUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1LendingAutoInvestRebalanceHistoryResponse` | `binance_public_spot_api/models/sapi_v1_lending_auto_invest_rebalance_history_response.py` |
| `IndexLinkedPlanRebalanceDetailsUserDataErrorBody` | `binance_public_spot_api/errors/index_linked_plan_rebalance_details_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.auto_invest.index_linked_plan_redemption_trade

- **Route**: `POST /sapi/v1/lending/auto-invest/redeem`
- **Auth**: `api_key_auth`
- **Signature**: `def index_linked_plan_redemption_trade(index_id: int, redemption_percentage: int, timestamp: int, signature: str, *, request_id: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `index_id`, `redemption_percentage`, `timestamp`, `signature`
- **Params**: `index_id` — query `indexId` · `redemption_percentage` — query `redemptionPercentage` · `timestamp` — query · `signature` — query · `request_id` — query `requestId` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1LendingAutoInvestRedeemResponse`
- **Returns (raw)**: `ApiResult[SapiV1LendingAutoInvestRedeemResponse, IndexLinkedPlanRedemptionTradeErrorBody]`
- **Error**: `IndexLinkedPlanRedemptionTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1LendingAutoInvestRedeemResponse` | `binance_public_spot_api/models/sapi_v1_lending_auto_invest_redeem_response.py` |
| `IndexLinkedPlanRedemptionTradeErrorBody` | `binance_public_spot_api/errors/index_linked_plan_redemption_trade_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.auto_invest.index_linked_plan_redemption_history_user_data

- **Route**: `GET /sapi/v1/lending/auto-invest/redeem/history`
- **Auth**: `api_key_auth`
- **Signature**: `def index_linked_plan_redemption_history_user_data(request_id: int, timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, current: int | None = None, asset: str | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `request_id`, `timestamp`, `signature`
- **Params**: `request_id` — query `requestId` · `timestamp` — query · `signature` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `current` — query · `asset` — query · `size` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1LendingAutoInvestRedeemHistoryResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1LendingAutoInvestRedeemHistoryResponse], IndexLinkedPlanRedemptionHistoryUserDataErrorBody]`
- **Error**: `IndexLinkedPlanRedemptionHistoryUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1LendingAutoInvestRedeemHistoryResponse` | `binance_public_spot_api/models/sapi_v1_lending_auto_invest_redeem_history_response.py` |
| `IndexLinkedPlanRedemptionHistoryUserDataErrorBody` | `binance_public_spot_api/errors/index_linked_plan_redemption_history_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.auto_invest.investment_plan_adjustment

- **Route**: `POST /sapi/v1/lending/auto-invest/plan/edit`
- **Auth**: `api_key_auth`
- **Signature**: `def investment_plan_adjustment(plan_id: int, subscription_amount: float, subscription_cycle: SubscriptionCycleOrStr, subscription_start_time: int, source_asset: str, timestamp: int, signature: str, *, subscription_start_day: int | None = None, subscription_start_weekday: SubscriptionStartWeekdayOrStr | None = None, flexible_allowed_to_use: bool | None = None, details: list[Detail1 | Detail1Dict] | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`, `subscription_amount`, `subscription_cycle`, `subscription_start_time`, `source_asset`, `timestamp`, `signature`
- **Params**: `plan_id` — query `planId` · `subscription_amount` — query `subscriptionAmount` · `subscription_cycle` — query `subscriptionCycle` · `subscription_start_time` — query `subscriptionStartTime` · `source_asset` — query `sourceAsset` · `timestamp` — query · `signature` — query · `subscription_start_day` — query `subscriptionStartDay` · `subscription_start_weekday` — query `subscriptionStartWeekday` · `flexible_allowed_to_use` — query `flexibleAllowedToUse` · `details` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1LendingAutoInvestPlanEditResponse`
- **Returns (raw)**: `ApiResult[SapiV1LendingAutoInvestPlanEditResponse, InvestmentPlanAdjustmentErrorBody]`
- **Error**: `InvestmentPlanAdjustmentErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SubscriptionCycleOrStr` | `binance_public_spot_api/models/enums/subscription_cycle.py` |
| `SubscriptionStartWeekdayOrStr` | `binance_public_spot_api/models/enums/subscription_start_weekday.py` |
| `Detail1` | `binance_public_spot_api/models/detail1.py` |
| `Detail1Dict` | `binance_public_spot_api/models/detail1.py` |
| `SapiV1LendingAutoInvestPlanEditResponse` | `binance_public_spot_api/models/sapi_v1_lending_auto_invest_plan_edit_response.py` |
| `InvestmentPlanAdjustmentErrorBody` | `binance_public_spot_api/errors/investment_plan_adjustment_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.auto_invest.investment_plan_creation_user_data

- **Route**: `POST /sapi/v1/lending/auto-invest/plan/add`
- **Auth**: `api_key_auth`
- **Signature**: `def investment_plan_creation_user_data(source_type: SourceTypeOrStr, plan_type: PlanTypeOrStr, subscription_amount: float, subscription_cycle: SubscriptionCycleOrStr, subscription_start_time: int, source_asset: str, details: list[Detail1 | Detail1Dict], timestamp: int, signature: str, *, request_id: str | None = None, index_id: int | None = None, subscription_start_day: int | None = None, subscription_start_weekday: SubscriptionStartWeekdayOrStr | None = None, flexible_allowed_to_use: bool | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `source_type`, `plan_type`, `subscription_amount`, `subscription_cycle`, `subscription_start_time`, `source_asset`, `details`, `timestamp`, `signature`
- **Params**: `source_type` — query `sourceType` · `plan_type` — query `planType` · `subscription_amount` — query `subscriptionAmount` · `subscription_cycle` — query `subscriptionCycle` · `subscription_start_time` — query `subscriptionStartTime` · `source_asset` — query `sourceAsset` · `details` — query · `timestamp` — query · `signature` — query · `request_id` — query `requestId` · `index_id` — query `IndexId` · `subscription_start_day` — query `subscriptionStartDay` · `subscription_start_weekday` — query `subscriptionStartWeekday` · `flexible_allowed_to_use` — query `flexibleAllowedToUse` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1LendingAutoInvestPlanAddResponse`
- **Returns (raw)**: `ApiResult[SapiV1LendingAutoInvestPlanAddResponse, InvestmentPlanCreationUserDataErrorBody]`
- **Error**: `InvestmentPlanCreationUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SourceTypeOrStr` | `binance_public_spot_api/models/enums/source_type.py` |
| `PlanTypeOrStr` | `binance_public_spot_api/models/enums/plan_type.py` |
| `SubscriptionCycleOrStr` | `binance_public_spot_api/models/enums/subscription_cycle.py` |
| `Detail1` | `binance_public_spot_api/models/detail1.py` |
| `Detail1Dict` | `binance_public_spot_api/models/detail1.py` |
| `SubscriptionStartWeekdayOrStr` | `binance_public_spot_api/models/enums/subscription_start_weekday.py` |
| `SapiV1LendingAutoInvestPlanAddResponse` | `binance_public_spot_api/models/sapi_v1_lending_auto_invest_plan_add_response.py` |
| `InvestmentPlanCreationUserDataErrorBody` | `binance_public_spot_api/errors/investment_plan_creation_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.auto_invest.one_time_transaction_trade

- **Route**: `POST /sapi/v1/lending/auto-invest/one-off`
- **Auth**: `api_key_auth`
- **Signature**: `def one_time_transaction_trade(source_type: str, subscription_amount: float, source_asset: str, timestamp: int, signature: str, *, request_id: str | None = None, flexible_allowed_to_use: bool | None = None, plan_id: int | None = None, index_id: int | None = None, details: list[Detail5 | Detail5Dict] | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `source_type`, `subscription_amount`, `source_asset`, `timestamp`, `signature`
- **Params**: `source_type` — query `sourceType` · `subscription_amount` — query `subscriptionAmount` · `source_asset` — query `sourceAsset` · `timestamp` — query · `signature` — query · `request_id` — query `requestId` · `flexible_allowed_to_use` — query `flexibleAllowedToUse` · `plan_id` — query `planId` · `index_id` — query `indexId` · `details` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1LendingAutoInvestOneOffResponse`
- **Returns (raw)**: `ApiResult[SapiV1LendingAutoInvestOneOffResponse, OneTimeTransactionTradeErrorBody]`
- **Error**: `OneTimeTransactionTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Detail5` | `binance_public_spot_api/models/detail5.py` |
| `Detail5Dict` | `binance_public_spot_api/models/detail5.py` |
| `SapiV1LendingAutoInvestOneOffResponse` | `binance_public_spot_api/models/sapi_v1_lending_auto_invest_one_off_response.py` |
| `OneTimeTransactionTradeErrorBody` | `binance_public_spot_api/errors/one_time_transaction_trade_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.auto_invest.query_index_details_user_data

- **Route**: `GET /sapi/v1/lending/auto-invest/index/info`
- **Auth**: `api_key_auth`
- **Signature**: `def query_index_details_user_data(index_id: int, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `index_id`, `timestamp`, `signature`
- **Params**: `index_id` — query `indexId` · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1LendingAutoInvestIndexInfoResponse`
- **Returns (raw)**: `ApiResult[SapiV1LendingAutoInvestIndexInfoResponse, QueryIndexDetailsUserDataErrorBody]`
- **Error**: `QueryIndexDetailsUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1LendingAutoInvestIndexInfoResponse` | `binance_public_spot_api/models/sapi_v1_lending_auto_invest_index_info_response.py` |
| `QueryIndexDetailsUserDataErrorBody` | `binance_public_spot_api/errors/query_index_details_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.auto_invest.query_index_linked_plan_position_details_user_data

- **Route**: `GET /sapi/v1/lending/auto-invest/index/user-summary`
- **Auth**: `api_key_auth`
- **Signature**: `def query_index_linked_plan_position_details_user_data(index_id: int, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `index_id`, `timestamp`, `signature`
- **Params**: `index_id` — query `indexId` · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1LendingAutoInvestIndexUserSummaryResponse`
- **Returns (raw)**: `ApiResult[SapiV1LendingAutoInvestIndexUserSummaryResponse, QueryIndexLinkedPlanPositionDetailsUserDataErrorBody]`
- **Error**: `QueryIndexLinkedPlanPositionDetailsUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1LendingAutoInvestIndexUserSummaryResponse` | `binance_public_spot_api/models/sapi_v1_lending_auto_invest_index_user_summary_response.py` |
| `QueryIndexLinkedPlanPositionDetailsUserDataErrorBody` | `binance_public_spot_api/errors/query_index_linked_plan_position_details_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.auto_invest.query_one_time_transaction_status_user_data

- **Route**: `GET /sapi/v1/lending/auto-invest/one-off/status`
- **Auth**: `api_key_auth`
- **Signature**: `def query_one_time_transaction_status_user_data(transaction_id: int, timestamp: int, signature: str, *, request_id: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `transaction_id`, `timestamp`, `signature`
- **Params**: `transaction_id` — query `transactionId` · `timestamp` — query · `signature` — query · `request_id` — query `requestId` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1LendingAutoInvestOneOffStatusResponse`
- **Returns (raw)**: `ApiResult[SapiV1LendingAutoInvestOneOffStatusResponse, QueryOneTimeTransactionStatusUserDataErrorBody]`
- **Error**: `QueryOneTimeTransactionStatusUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1LendingAutoInvestOneOffStatusResponse` | `binance_public_spot_api/models/sapi_v1_lending_auto_invest_one_off_status_response.py` |
| `QueryOneTimeTransactionStatusUserDataErrorBody` | `binance_public_spot_api/errors/query_one_time_transaction_status_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.auto_invest.query_all_source_asset_and_target_asset_user_data

- **Route**: `GET /sapi/v1/lending/auto-invest/all/asset`
- **Auth**: `api_key_auth`
- **Signature**: `def query_all_source_asset_and_target_asset_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1LendingAutoInvestAllAssetResponse`
- **Returns (raw)**: `ApiResult[SapiV1LendingAutoInvestAllAssetResponse, QueryAllSourceAssetAndTargetAssetUserDataErrorBody]`
- **Error**: `QueryAllSourceAssetAndTargetAssetUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1LendingAutoInvestAllAssetResponse` | `binance_public_spot_api/models/sapi_v1_lending_auto_invest_all_asset_response.py` |
| `QueryAllSourceAssetAndTargetAssetUserDataErrorBody` | `binance_public_spot_api/errors/query_all_source_asset_and_target_asset_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.auto_invest.query_holding_details_of_the_plan

- **Route**: `GET /sapi/v1/lending/auto-invest/plan/id`
- **Auth**: `api_key_auth`
- **Signature**: `def query_holding_details_of_the_plan(timestamp: int, signature: str, *, plan_id: int | None = None, request_id: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `plan_id` — query `planId` · `request_id` — query `requestId` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1LendingAutoInvestPlanIdResponse`
- **Returns (raw)**: `ApiResult[SapiV1LendingAutoInvestPlanIdResponse, QueryHoldingDetailsOfThePlanErrorBody]`
- **Error**: `QueryHoldingDetailsOfThePlanErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1LendingAutoInvestPlanIdResponse` | `binance_public_spot_api/models/sapi_v1_lending_auto_invest_plan_id_response.py` |
| `QueryHoldingDetailsOfThePlanErrorBody` | `binance_public_spot_api/errors/query_holding_details_of_the_plan_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.auto_invest.query_source_asset_list_user_data

- **Route**: `GET /sapi/v1/lending/auto-invest/source-asset/list`
- **Auth**: `api_key_auth`
- **Signature**: `def query_source_asset_list_user_data(usage_type: str, timestamp: int, signature: str, *, target_asset: str | None = None, index_id: int | None = None, flexible_allowed_to_use: bool | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `usage_type`, `timestamp`, `signature`
- **Params**: `usage_type` — query `usageType` · `timestamp` — query · `signature` — query · `target_asset` — query `targetAsset` · `index_id` — query `indexId` · `flexible_allowed_to_use` — query `flexibleAllowedToUse` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1LendingAutoInvestSourceAssetListResponse`
- **Returns (raw)**: `ApiResult[SapiV1LendingAutoInvestSourceAssetListResponse, QuerySourceAssetListUserDataErrorBody]`
- **Error**: `QuerySourceAssetListUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1LendingAutoInvestSourceAssetListResponse` | `binance_public_spot_api/models/sapi_v1_lending_auto_invest_source_asset_list_response.py` |
| `QuerySourceAssetListUserDataErrorBody` | `binance_public_spot_api/errors/query_source_asset_list_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.auto_invest.query_subscription_transaction_history

- **Route**: `GET /sapi/v1/lending/auto-invest/history/list`
- **Auth**: `api_key_auth`
- **Signature**: `def query_subscription_transaction_history(timestamp: int, signature: str, *, plan_id: int | None = None, start_time: int | None = None, end_time: int | None = None, target_asset: int | None = None, plan_type: PlanType1OrStr | None = None, size: int | None = None, current: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `plan_id` — query `planId` · `start_time` — query `startTime` · `end_time` — query `endTime` · `target_asset` — query `targetAsset` · `plan_type` — query `planType` · `size` — query · `current` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1LendingAutoInvestHistoryListResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1LendingAutoInvestHistoryListResponse], QuerySubscriptionTransactionHistoryErrorBody]`
- **Error**: `QuerySubscriptionTransactionHistoryErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PlanType1OrStr` | `binance_public_spot_api/models/enums/plan_type1.py` |
| `SapiV1LendingAutoInvestHistoryListResponse` | `binance_public_spot_api/models/sapi_v1_lending_auto_invest_history_list_response.py` |
| `QuerySubscriptionTransactionHistoryErrorBody` | `binance_public_spot_api/errors/query_subscription_transaction_history_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

