<!-- Generated file — do not edit; regenerated with the SDK. -->

# SubAccountApi — operations

Accessor: `client.sub_account_api` · Source: `binance/apis/sub_account_api.py` · 45 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.sub_account_api.create_a_virtual_sub_account_for_master_account

- **Route**: `POST /sapi/v1/sub-account/virtualSubAccount`
- **Signature**: `def create_a_virtual_sub_account_for_master_account(sub_account_string: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sub_account_string`, `timestamp`, `signature`
- **Params**: `sub_account_string` — query `subAccountString` · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SubAccountVirtualSubAccountResponse`
- **Returns (raw)**: `ApiResult[SapiV1SubAccountVirtualSubAccountResponse, CreateAVirtualSubAccountForMasterAccountErrorBody]`
- **Error**: `CreateAVirtualSubAccountForMasterAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SubAccountVirtualSubAccountResponse` | `binance/models/sapi_v1_sub_account_virtual_sub_account_response.py` |
| `CreateAVirtualSubAccountForMasterAccountErrorBody` | `binance/errors/create_a_virtual_sub_account_for_master_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.delete_ip_list_for_a_sub_account_api_key_for_master_account

- **Route**: `DELETE /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList`
- **Signature**: `def delete_ip_list_for_a_sub_account_api_key_for_master_account(email: str, sub_account_api_key: str, timestamp: int, signature: str, *, ip_address: str | None = None, third_party_name: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `email`, `sub_account_api_key`, `timestamp`, `signature`
- **Params**: `email` — query · `sub_account_api_key` — query `subAccountApiKey` · `timestamp` — query · `signature` — query · `ip_address` — query `ipAddress` · `third_party_name` — query `thirdPartyName` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SubAccountSubAccountApiIpRestrictionIpListResponse`
- **Returns (raw)**: `ApiResult[SapiV1SubAccountSubAccountApiIpRestrictionIpListResponse, DeleteIpListForASubAccountApiKeyForMasterAccountErrorBody]`
- **Error**: `DeleteIpListForASubAccountApiKeyForMasterAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SubAccountSubAccountApiIpRestrictionIpListResponse` | `binance/models/sapi_v1_sub_account_sub_account_api_ip_restriction_ip_list_response.py` |
| `DeleteIpListForASubAccountApiKeyForMasterAccountErrorBody` | `binance/errors/delete_ip_list_for_a_sub_account_api_key_for_master_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.deposit_assets_into_the_managed_sub_account_for_investor_master_account

- **Route**: `POST /sapi/v1/managed-subaccount/deposit`
- **Signature**: `def deposit_assets_into_the_managed_sub_account_for_investor_master_account(to_email: str, asset: str, amount: float, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `to_email`, `asset`, `amount`, `timestamp`, `signature`
- **Params**: `to_email` — query `toEmail` · `asset` — query · `amount` — query · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1ManagedSubaccountDepositResponse`
- **Returns (raw)**: `ApiResult[SapiV1ManagedSubaccountDepositResponse, DepositAssetsIntoTheManagedSubAccountForInvestorMasterAccountErrorBody]`
- **Error**: `DepositAssetsIntoTheManagedSubAccountForInvestorMasterAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1ManagedSubaccountDepositResponse` | `binance/models/sapi_v1_managed_subaccount_deposit_response.py` |
| `DepositAssetsIntoTheManagedSubAccountForInvestorMasterAccountErrorBody` | `binance/errors/deposit_assets_into_the_managed_sub_account_for_investor_master_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.detail_on_sub_account_s_futures_account_for_master_account

- **Route**: `GET /sapi/v1/sub-account/futures/account`
- **Signature**: `def detail_on_sub_account_s_futures_account_for_master_account(email: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `email`, `timestamp`, `signature`
- **Params**: `email` — query · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SubAccountFuturesAccountResponse`
- **Returns (raw)**: `ApiResult[SapiV1SubAccountFuturesAccountResponse, DetailOnSubAccountSFuturesAccountForMasterAccountErrorBody]`
- **Error**: `DetailOnSubAccountSFuturesAccountForMasterAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SubAccountFuturesAccountResponse` | `binance/models/sapi_v1_sub_account_futures_account_response.py` |
| `DetailOnSubAccountSFuturesAccountForMasterAccountErrorBody` | `binance/errors/detail_on_sub_account_s_futures_account_for_master_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.detail_on_sub_account_s_futures_account_v2_for_master_account

- **Route**: `GET /sapi/v2/sub-account/futures/account`
- **Signature**: `def detail_on_sub_account_s_futures_account_v2_for_master_account(email: str, futures_type: int, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `email`, `futures_type`, `timestamp`, `signature`
- **Params**: `email` — query · `futures_type` — query `futuresType` · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV2SubAccountFuturesAccountResponse`
- **Returns (raw)**: `ApiResult[SapiV2SubAccountFuturesAccountResponse, DetailOnSubAccountSFuturesAccountV2ForMasterAccountErrorBody]`
- **Error**: `DetailOnSubAccountSFuturesAccountV2ForMasterAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV2SubAccountFuturesAccountResponse` | `binance/models/unions/sapi_v2_sub_account_futures_account_response.py` |
| `DetailOnSubAccountSFuturesAccountV2ForMasterAccountErrorBody` | `binance/errors/detail_on_sub_account_s_futures_account_v2_for_master_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.detail_on_sub_account_s_margin_account_for_master_account

- **Route**: `GET /sapi/v1/sub-account/margin/account`
- **Signature**: `def detail_on_sub_account_s_margin_account_for_master_account(email: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `email`, `timestamp`, `signature`
- **Params**: `email` — query · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SubAccountMarginAccountResponse`
- **Returns (raw)**: `ApiResult[SapiV1SubAccountMarginAccountResponse, DetailOnSubAccountSMarginAccountForMasterAccountErrorBody]`
- **Error**: `DetailOnSubAccountSMarginAccountForMasterAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SubAccountMarginAccountResponse` | `binance/models/sapi_v1_sub_account_margin_account_response.py` |
| `DetailOnSubAccountSMarginAccountForMasterAccountErrorBody` | `binance/errors/detail_on_sub_account_s_margin_account_for_master_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.enable_futures_for_sub_account_for_master_account

- **Route**: `POST /sapi/v1/sub-account/futures/enable`
- **Signature**: `def enable_futures_for_sub_account_for_master_account(email: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `email`, `timestamp`, `signature`
- **Params**: `email` — query · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SubAccountFuturesEnableResponse`
- **Returns (raw)**: `ApiResult[SapiV1SubAccountFuturesEnableResponse, EnableFuturesForSubAccountForMasterAccountErrorBody]`
- **Error**: `EnableFuturesForSubAccountForMasterAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SubAccountFuturesEnableResponse` | `binance/models/sapi_v1_sub_account_futures_enable_response.py` |
| `EnableFuturesForSubAccountForMasterAccountErrorBody` | `binance/errors/enable_futures_for_sub_account_for_master_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.enable_leverage_token_for_sub_account_for_master_account

- **Route**: `POST /sapi/v1/sub-account/blvt/enable`
- **Signature**: `def enable_leverage_token_for_sub_account_for_master_account(email: str, enable_blvt: bool, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `email`, `enable_blvt`, `timestamp`, `signature`
- **Params**: `email` — query · `enable_blvt` — query `enableBlvt` · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SubAccountBlvtEnableResponse`
- **Returns (raw)**: `ApiResult[SapiV1SubAccountBlvtEnableResponse, EnableLeverageTokenForSubAccountForMasterAccountErrorBody]`
- **Error**: `EnableLeverageTokenForSubAccountForMasterAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SubAccountBlvtEnableResponse` | `binance/models/sapi_v1_sub_account_blvt_enable_response.py` |
| `EnableLeverageTokenForSubAccountForMasterAccountErrorBody` | `binance/errors/enable_leverage_token_for_sub_account_for_master_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.enable_margin_for_sub_account_for_master_account

- **Route**: `POST /sapi/v1/sub-account/margin/enable`
- **Signature**: `def enable_margin_for_sub_account_for_master_account(email: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `email`, `timestamp`, `signature`
- **Params**: `email` — query · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SubAccountMarginEnableResponse`
- **Returns (raw)**: `ApiResult[SapiV1SubAccountMarginEnableResponse, EnableMarginForSubAccountForMasterAccountErrorBody]`
- **Error**: `EnableMarginForSubAccountForMasterAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SubAccountMarginEnableResponse` | `binance/models/sapi_v1_sub_account_margin_enable_response.py` |
| `EnableMarginForSubAccountForMasterAccountErrorBody` | `binance/errors/enable_margin_for_sub_account_for_master_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.enable_options_for_sub_account_for_master_account_user_data

- **Route**: `POST /sapi/v1/sub-account/eoptions/enable`
- **Signature**: `def enable_options_for_sub_account_for_master_account_user_data(email: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `email`, `timestamp`, `signature`
- **Params**: `email` — query · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SubAccountEoptionsEnableResponse`
- **Returns (raw)**: `ApiResult[SapiV1SubAccountEoptionsEnableResponse, EnableOptionsForSubAccountForMasterAccountUserDataErrorBody]`
- **Error**: `EnableOptionsForSubAccountForMasterAccountUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SubAccountEoptionsEnableResponse` | `binance/models/sapi_v1_sub_account_eoptions_enable_response.py` |
| `EnableOptionsForSubAccountForMasterAccountUserDataErrorBody` | `binance/errors/enable_options_for_sub_account_for_master_account_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.futures_position_risk_of_sub_account_for_master_account

- **Route**: `GET /sapi/v1/sub-account/futures/positionRisk`
- **Signature**: `def futures_position_risk_of_sub_account_for_master_account(email: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `email`, `timestamp`, `signature`
- **Params**: `email` — query · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1SubAccountFuturesPositionRiskResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1SubAccountFuturesPositionRiskResponse], FuturesPositionRiskOfSubAccountForMasterAccountErrorBody]`
- **Error**: `FuturesPositionRiskOfSubAccountForMasterAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SubAccountFuturesPositionRiskResponse` | `binance/models/sapi_v1_sub_account_futures_position_risk_response.py` |
| `FuturesPositionRiskOfSubAccountForMasterAccountErrorBody` | `binance/errors/futures_position_risk_of_sub_account_for_master_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.futures_position_risk_of_sub_account_v2_for_master_account

- **Route**: `GET /sapi/v2/sub-account/futures/positionRisk`
- **Signature**: `def futures_position_risk_of_sub_account_v2_for_master_account(email: str, futures_type: int, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `email`, `futures_type`, `timestamp`, `signature`
- **Params**: `email` — query · `futures_type` — query `futuresType` · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV2SubAccountFuturesPositionRiskResponse`
- **Returns (raw)**: `ApiResult[SapiV2SubAccountFuturesPositionRiskResponse, FuturesPositionRiskOfSubAccountV2ForMasterAccountErrorBody]`
- **Error**: `FuturesPositionRiskOfSubAccountV2ForMasterAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV2SubAccountFuturesPositionRiskResponse` | `binance/models/unions/sapi_v2_sub_account_futures_position_risk_response.py` |
| `FuturesPositionRiskOfSubAccountV2ForMasterAccountErrorBody` | `binance/errors/futures_position_risk_of_sub_account_v2_for_master_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.get_ip_restriction_for_a_sub_account_api_key_for_master_account

- **Route**: `GET /sapi/v1/sub-account/subAccountApi/ipRestriction`
- **Signature**: `def get_ip_restriction_for_a_sub_account_api_key_for_master_account(email: str, sub_account_api_key: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `email`, `sub_account_api_key`, `timestamp`, `signature`
- **Params**: `email` — query · `sub_account_api_key` — query `subAccountApiKey` · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SubAccountSubAccountApiIpRestrictionResponse`
- **Returns (raw)**: `ApiResult[SapiV1SubAccountSubAccountApiIpRestrictionResponse, GetIpRestrictionForASubAccountApiKeyForMasterAccountErrorBody]`
- **Error**: `GetIpRestrictionForASubAccountApiKeyForMasterAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SubAccountSubAccountApiIpRestrictionResponse` | `binance/models/sapi_v1_sub_account_sub_account_api_ip_restriction_response.py` |
| `GetIpRestrictionForASubAccountApiKeyForMasterAccountErrorBody` | `binance/errors/get_ip_restriction_for_a_sub_account_api_key_for_master_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.get_managed_sub_account_deposit_address_for_investor_master_account

- **Route**: `GET /sapi/v1/managed-subaccount/deposit/address`
- **Signature**: `def get_managed_sub_account_deposit_address_for_investor_master_account(email: str, coin: str, timestamp: int, signature: str, *, network: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `email`, `coin`, `timestamp`, `signature`
- **Params**: `email` — query · `coin` — query · `timestamp` — query · `signature` — query · `network` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1ManagedSubaccountDepositAddressResponse`
- **Returns (raw)**: `ApiResult[SapiV1ManagedSubaccountDepositAddressResponse, GetManagedSubAccountDepositAddressForInvestorMasterAccountErrorBody]`
- **Error**: `GetManagedSubAccountDepositAddressForInvestorMasterAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1ManagedSubaccountDepositAddressResponse` | `binance/models/sapi_v1_managed_subaccount_deposit_address_response.py` |
| `GetManagedSubAccountDepositAddressForInvestorMasterAccountErrorBody` | `binance/errors/get_managed_sub_account_deposit_address_for_investor_master_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.managed_sub_account_asset_details_for_investor_master_account

- **Route**: `GET /sapi/v1/managed-subaccount/asset`
- **Signature**: `def managed_sub_account_asset_details_for_investor_master_account(email: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `email`, `timestamp`, `signature`
- **Params**: `email` — query · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1ManagedSubaccountAssetResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1ManagedSubaccountAssetResponse], ManagedSubAccountAssetDetailsForInvestorMasterAccountErrorBody]`
- **Error**: `ManagedSubAccountAssetDetailsForInvestorMasterAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1ManagedSubaccountAssetResponse` | `binance/models/sapi_v1_managed_subaccount_asset_response.py` |
| `ManagedSubAccountAssetDetailsForInvestorMasterAccountErrorBody` | `binance/errors/managed_sub_account_asset_details_for_investor_master_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.managed_sub_account_snapshot_for_investor_master_account

- **Route**: `GET /sapi/v1/managed-subaccount/accountSnapshot`
- **Signature**: `def managed_sub_account_snapshot_for_investor_master_account(email: str, type_: str, timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `email`, `type_`, `timestamp`, `signature`
- **Params**: `email` — query · `type_` — query `type` · `timestamp` — query · `signature` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `limit` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1ManagedSubaccountAccountSnapshotResponse`
- **Returns (raw)**: `ApiResult[SapiV1ManagedSubaccountAccountSnapshotResponse, ManagedSubAccountSnapshotForInvestorMasterAccountErrorBody]`
- **Error**: `ManagedSubAccountSnapshotForInvestorMasterAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1ManagedSubaccountAccountSnapshotResponse` | `binance/models/sapi_v1_managed_subaccount_account_snapshot_response.py` |
| `ManagedSubAccountSnapshotForInvestorMasterAccountErrorBody` | `binance/errors/managed_sub_account_snapshot_for_investor_master_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.margin_transfer_for_sub_account_for_master_account

- **Route**: `POST /sapi/v1/sub-account/margin/transfer`
- **Signature**: `def margin_transfer_for_sub_account_for_master_account(email: str, asset: str, amount: float, type_: int, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `email`, `asset`, `amount`, `type_`, `timestamp`, `signature`
- **Params**: `email` — query · `asset` — query · `amount` — query · `type_` — query `type` · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SubAccountMarginTransferResponse`
- **Returns (raw)**: `ApiResult[SapiV1SubAccountMarginTransferResponse, MarginTransferForSubAccountForMasterAccountErrorBody]`
- **Error**: `MarginTransferForSubAccountForMasterAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SubAccountMarginTransferResponse` | `binance/models/sapi_v1_sub_account_margin_transfer_response.py` |
| `MarginTransferForSubAccountForMasterAccountErrorBody` | `binance/errors/margin_transfer_for_sub_account_for_master_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.query_managed_sub_account_transfer_log_for_investor_master_account

- **Route**: `GET /sapi/v1/managed-subaccount/queryTransLogForInvestor`
- **Signature**: `def query_managed_sub_account_transfer_log_for_investor_master_account(email: str, timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, page: int | None = None, limit: int | None = None, transfers: str | None = None, transfer_function_account_type: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `email`, `timestamp`, `signature`
- **Params**: `email` — query · `timestamp` — query · `signature` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `page` — query · `limit` — query · `transfers` — query · `transfer_function_account_type` — query `transferFunctionAccountType` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1ManagedSubaccountQueryTransLogForInvestorResponse`
- **Returns (raw)**: `ApiResult[SapiV1ManagedSubaccountQueryTransLogForInvestorResponse, QueryManagedSubAccountTransferLogForInvestorMasterAccountErrorBody]`
- **Error**: `QueryManagedSubAccountTransferLogForInvestorMasterAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1ManagedSubaccountQueryTransLogForInvestorResponse` | `binance/models/sapi_v1_managed_subaccount_query_trans_log_for_investor_response.py` |
| `QueryManagedSubAccountTransferLogForInvestorMasterAccountErrorBody` | `binance/errors/query_managed_sub_account_transfer_log_for_investor_master_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.query_managed_sub_account_transfer_log_for_trading_team_master_account

- **Route**: `GET /sapi/v1/managed-subaccount/queryTransLogForTradeParent`
- **Signature**: `def query_managed_sub_account_transfer_log_for_trading_team_master_account(email: str, timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, page: int | None = None, limit: int | None = None, transfers: str | None = None, transfer_function_account_type: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `email`, `timestamp`, `signature`
- **Params**: `email` — query · `timestamp` — query · `signature` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `page` — query · `limit` — query · `transfers` — query · `transfer_function_account_type` — query `transferFunctionAccountType` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1ManagedSubaccountQueryTransLogForTradeParentResponse`
- **Returns (raw)**: `ApiResult[SapiV1ManagedSubaccountQueryTransLogForTradeParentResponse, QueryManagedSubAccountTransferLogForTradingTeamMasterAccountErrorBody]`
- **Error**: `QueryManagedSubAccountTransferLogForTradingTeamMasterAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1ManagedSubaccountQueryTransLogForTradeParentResponse` | `binance/models/sapi_v1_managed_subaccount_query_trans_log_for_trade_parent_response.py` |
| `QueryManagedSubAccountTransferLogForTradingTeamMasterAccountErrorBody` | `binance/errors/query_managed_sub_account_transfer_log_for_trading_team_master_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.query_managed_sub_account_transfer_log_for_trading_team_sub_account_user_data

- **Route**: `GET /sapi/v1/managed-subaccount/query-trans-log`
- **Signature**: `def query_managed_sub_account_transfer_log_for_trading_team_sub_account_user_data(transfers: TransfersOrStr, transfer_function_account_type: TransferFunctionAccountTypeOrStr, timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, page: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `transfers`, `transfer_function_account_type`, `timestamp`, `signature`
- **Params**: `transfers` — query · `transfer_function_account_type` — query `transferFunctionAccountType` · `timestamp` — query · `signature` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `page` — query · `limit` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1ManagedSubaccountQueryTransLogResponse`
- **Returns (raw)**: `ApiResult[SapiV1ManagedSubaccountQueryTransLogResponse, QueryManagedSubAccountTransferLogForTradingTeamSubAccountUserDataErrorBody]`
- **Error**: `QueryManagedSubAccountTransferLogForTradingTeamSubAccountUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TransfersOrStr` | `binance/models/enums/transfers.py` |
| `TransferFunctionAccountTypeOrStr` | `binance/models/enums/transfer_function_account_type.py` |
| `SapiV1ManagedSubaccountQueryTransLogResponse` | `binance/models/sapi_v1_managed_subaccount_query_trans_log_response.py` |
| `QueryManagedSubAccountTransferLogForTradingTeamSubAccountUserDataErrorBody` | `binance/errors/query_managed_sub_account_transfer_log_for_trading_team_sub_account_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.query_managed_sub_account_futures_asset_details_for_investor_master_account

- **Route**: `GET /sapi/v1/managed-subaccount/fetch-future-asset`
- **Signature**: `def query_managed_sub_account_futures_asset_details_for_investor_master_account(email: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `email`, `timestamp`, `signature`
- **Params**: `email` — query · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1ManagedSubaccountFetchFutureAssetResponse`
- **Returns (raw)**: `ApiResult[SapiV1ManagedSubaccountFetchFutureAssetResponse, QueryManagedSubAccountFuturesAssetDetailsForInvestorMasterAccountErrorBody]`
- **Error**: `QueryManagedSubAccountFuturesAssetDetailsForInvestorMasterAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1ManagedSubaccountFetchFutureAssetResponse` | `binance/models/sapi_v1_managed_subaccount_fetch_future_asset_response.py` |
| `QueryManagedSubAccountFuturesAssetDetailsForInvestorMasterAccountErrorBody` | `binance/errors/query_managed_sub_account_futures_asset_details_for_investor_master_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.query_managed_sub_account_list_for_investor

- **Route**: `GET /sapi/v1/managed-subaccount/info`
- **Signature**: `def query_managed_sub_account_list_for_investor(email: str, timestamp: int, signature: str, *, page: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `email`, `timestamp`, `signature`
- **Params**: `email` — query · `timestamp` — query · `signature` — query · `page` — query · `limit` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1ManagedSubaccountInfoResponse`
- **Returns (raw)**: `ApiResult[SapiV1ManagedSubaccountInfoResponse, QueryManagedSubAccountListForInvestorErrorBody]`
- **Error**: `QueryManagedSubAccountListForInvestorErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1ManagedSubaccountInfoResponse` | `binance/models/sapi_v1_managed_subaccount_info_response.py` |
| `QueryManagedSubAccountListForInvestorErrorBody` | `binance/errors/query_managed_sub_account_list_for_investor_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.query_managed_sub_account_margin_asset_details_for_investor_master_account

- **Route**: `GET /sapi/v1/managed-subaccount/marginAsset`
- **Signature**: `def query_managed_sub_account_margin_asset_details_for_investor_master_account(email: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `email`, `timestamp`, `signature`
- **Params**: `email` — query · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1ManagedSubaccountMarginAssetResponse`
- **Returns (raw)**: `ApiResult[SapiV1ManagedSubaccountMarginAssetResponse, QueryManagedSubAccountMarginAssetDetailsForInvestorMasterAccountErrorBody]`
- **Error**: `QueryManagedSubAccountMarginAssetDetailsForInvestorMasterAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1ManagedSubaccountMarginAssetResponse` | `binance/models/sapi_v1_managed_subaccount_margin_asset_response.py` |
| `QueryManagedSubAccountMarginAssetDetailsForInvestorMasterAccountErrorBody` | `binance/errors/query_managed_sub_account_margin_asset_details_for_investor_master_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.query_sub_account_assets_for_master_account

- **Route**: `GET /sapi/v4/sub-account/assets`
- **Signature**: `def query_sub_account_assets_for_master_account(email: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `email`, `timestamp`, `signature`
- **Params**: `email` — query · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV4SubAccountAssetsResponse`
- **Returns (raw)**: `ApiResult[SapiV4SubAccountAssetsResponse, QuerySubAccountAssetsForMasterAccountErrorBody]`
- **Error**: `QuerySubAccountAssetsForMasterAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV4SubAccountAssetsResponse` | `binance/models/sapi_v4_sub_account_assets_response.py` |
| `QuerySubAccountAssetsForMasterAccountErrorBody` | `binance/errors/query_sub_account_assets_for_master_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.query_sub_account_list_for_master_account

- **Route**: `GET /sapi/v1/sub-account/list`
- **Signature**: `def query_sub_account_list_for_master_account(timestamp: int, signature: str, *, email: str | None = None, is_freeze: IsFreezeOrStr | None = None, page: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `email` — query · `is_freeze` — query `isFreeze` · `page` — query · `limit` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SubAccountListResponse`
- **Returns (raw)**: `ApiResult[SapiV1SubAccountListResponse, QuerySubAccountListForMasterAccountErrorBody]`
- **Error**: `QuerySubAccountListForMasterAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `IsFreezeOrStr` | `binance/models/enums/is_freeze.py` |
| `SapiV1SubAccountListResponse` | `binance/models/sapi_v1_sub_account_list_response.py` |
| `QuerySubAccountListForMasterAccountErrorBody` | `binance/errors/query_sub_account_list_for_master_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.query_sub_account_transaction_statistics_for_master_account

- **Route**: `GET /sapi/v1/sub-account/transaction-statistics`
- **Signature**: `def query_sub_account_transaction_statistics_for_master_account(email: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `email`, `timestamp`, `signature`
- **Params**: `email` — query · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SubAccountTransactionStatisticsResponse`
- **Returns (raw)**: `ApiResult[SapiV1SubAccountTransactionStatisticsResponse, QuerySubAccountTransactionStatisticsForMasterAccountErrorBody]`
- **Error**: `QuerySubAccountTransactionStatisticsForMasterAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SubAccountTransactionStatisticsResponse` | `binance/models/sapi_v1_sub_account_transaction_statistics_response.py` |
| `QuerySubAccountTransactionStatisticsForMasterAccountErrorBody` | `binance/errors/query_sub_account_transaction_statistics_for_master_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.sub_account_assets_for_master_account

- **Route**: `GET /sapi/v3/sub-account/assets`
- **Signature**: `def sub_account_assets_for_master_account(email: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `email`, `timestamp`, `signature`
- **Params**: `email` — query · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV3SubAccountAssetsResponse`
- **Returns (raw)**: `ApiResult[SapiV3SubAccountAssetsResponse, SubAccountAssetsForMasterAccountErrorBody]`
- **Error**: `SubAccountAssetsForMasterAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV3SubAccountAssetsResponse` | `binance/models/sapi_v3_sub_account_assets_response.py` |
| `SubAccountAssetsForMasterAccountErrorBody` | `binance/errors/sub_account_assets_for_master_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.sub_account_deposit_history_for_master_account

- **Route**: `GET /sapi/v1/capital/deposit/subHisrec`
- **Signature**: `def sub_account_deposit_history_for_master_account(email: str, timestamp: int, signature: str, *, coin: str | None = None, status: int | None = None, start_time: int | None = None, end_time: int | None = None, limit: int | None = None, offset: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `email`, `timestamp`, `signature`
- **Params**: `email` — query · `timestamp` — query · `signature` — query · `coin` — query · `status` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `limit` — query · `offset` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1CapitalDepositSubHisrecResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1CapitalDepositSubHisrecResponse], SubAccountDepositHistoryForMasterAccountErrorBody]`
- **Error**: `SubAccountDepositHistoryForMasterAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1CapitalDepositSubHisrecResponse` | `binance/models/sapi_v1_capital_deposit_sub_hisrec_response.py` |
| `SubAccountDepositHistoryForMasterAccountErrorBody` | `binance/errors/sub_account_deposit_history_for_master_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.sub_account_futures_asset_transfer_for_master_account

- **Route**: `POST /sapi/v1/sub-account/futures/internalTransfer`
- **Signature**: `def sub_account_futures_asset_transfer_for_master_account(from_email: str, to_email: str, futures_type: int, asset: str, amount: float, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `from_email`, `to_email`, `futures_type`, `asset`, `amount`, `timestamp`, `signature`
- **Params**: `from_email` — query `fromEmail` · `to_email` — query `toEmail` · `futures_type` — query `futuresType` · `asset` — query · `amount` — query · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SubAccountFuturesInternalTransferResponse1`
- **Returns (raw)**: `ApiResult[SapiV1SubAccountFuturesInternalTransferResponse1, SubAccountFuturesAssetTransferForMasterAccountErrorBody]`
- **Error**: `SubAccountFuturesAssetTransferForMasterAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SubAccountFuturesInternalTransferResponse1` | `binance/models/sapi_v1_sub_account_futures_internal_transfer_response1.py` |
| `SubAccountFuturesAssetTransferForMasterAccountErrorBody` | `binance/errors/sub_account_futures_asset_transfer_for_master_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.sub_account_futures_asset_transfer_history_for_master_account

- **Route**: `GET /sapi/v1/sub-account/futures/internalTransfer`
- **Signature**: `def sub_account_futures_asset_transfer_history_for_master_account(email: str, futures_type: int, timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, page: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `email`, `futures_type`, `timestamp`, `signature`
- **Params**: `email` — query · `futures_type` — query `futuresType` · `timestamp` — query · `signature` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `page` — query · `limit` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SubAccountFuturesInternalTransferResponse`
- **Returns (raw)**: `ApiResult[SapiV1SubAccountFuturesInternalTransferResponse, SubAccountFuturesAssetTransferHistoryForMasterAccountErrorBody]`
- **Error**: `SubAccountFuturesAssetTransferHistoryForMasterAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SubAccountFuturesInternalTransferResponse` | `binance/models/sapi_v1_sub_account_futures_internal_transfer_response.py` |
| `SubAccountFuturesAssetTransferHistoryForMasterAccountErrorBody` | `binance/errors/sub_account_futures_asset_transfer_history_for_master_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.sub_account_spot_asset_transfer_history_for_master_account

- **Route**: `GET /sapi/v1/sub-account/sub/transfer/history`
- **Signature**: `def sub_account_spot_asset_transfer_history_for_master_account(timestamp: int, signature: str, *, from_email: str | None = None, to_email: str | None = None, start_time: int | None = None, end_time: int | None = None, page: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `from_email` — query `fromEmail` · `to_email` — query `toEmail` · `start_time` — query `startTime` · `end_time` — query `endTime` · `page` — query · `limit` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1SubAccountSubTransferHistoryResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1SubAccountSubTransferHistoryResponse], SubAccountSpotAssetTransferHistoryForMasterAccountErrorBody]`
- **Error**: `SubAccountSpotAssetTransferHistoryForMasterAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SubAccountSubTransferHistoryResponse` | `binance/models/sapi_v1_sub_account_sub_transfer_history_response.py` |
| `SubAccountSpotAssetTransferHistoryForMasterAccountErrorBody` | `binance/errors/sub_account_spot_asset_transfer_history_for_master_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.sub_account_spot_assets_summary_for_master_account

- **Route**: `GET /sapi/v1/sub-account/spotSummary`
- **Signature**: `def sub_account_spot_assets_summary_for_master_account(timestamp: int, signature: str, *, email: str | None = None, page: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `email` — query · `page` — query · `size` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SubAccountSpotSummaryResponse`
- **Returns (raw)**: `ApiResult[SapiV1SubAccountSpotSummaryResponse, SubAccountSpotAssetsSummaryForMasterAccountErrorBody]`
- **Error**: `SubAccountSpotAssetsSummaryForMasterAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SubAccountSpotSummaryResponse` | `binance/models/sapi_v1_sub_account_spot_summary_response.py` |
| `SubAccountSpotAssetsSummaryForMasterAccountErrorBody` | `binance/errors/sub_account_spot_assets_summary_for_master_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.sub_account_spot_assets_summary_for_master_account_2

- **Route**: `GET /sapi/v1/capital/deposit/subAddress`
- **Signature**: `def sub_account_spot_assets_summary_for_master_account_2(email: str, coin: str, timestamp: int, signature: str, *, network: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `email`, `coin`, `timestamp`, `signature`
- **Params**: `email` — query · `coin` — query · `timestamp` — query · `signature` — query · `network` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1CapitalDepositSubAddressResponse`
- **Returns (raw)**: `ApiResult[SapiV1CapitalDepositSubAddressResponse, SubAccountSpotAssetsSummaryForMasterAccount2ErrorBody]`
- **Error**: `SubAccountSpotAssetsSummaryForMasterAccount2ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1CapitalDepositSubAddressResponse` | `binance/models/sapi_v1_capital_deposit_sub_address_response.py` |
| `SubAccountSpotAssetsSummaryForMasterAccount2ErrorBody` | `binance/errors/sub_account_spot_assets_summary_for_master_account2_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.sub_account_transfer_history_for_sub_account

- **Route**: `GET /sapi/v1/sub-account/transfer/subUserHistory`
- **Signature**: `def sub_account_transfer_history_for_sub_account(timestamp: int, signature: str, *, asset: str | None = None, type_: int | None = None, start_time: int | None = None, end_time: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `asset` — query · `type_` — query `type` · `start_time` — query `startTime` · `end_time` — query `endTime` · `limit` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1SubAccountTransferSubUserHistoryResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1SubAccountTransferSubUserHistoryResponse], SubAccountTransferHistoryForSubAccountErrorBody]`
- **Error**: `SubAccountTransferHistoryForSubAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SubAccountTransferSubUserHistoryResponse` | `binance/models/sapi_v1_sub_account_transfer_sub_user_history_response.py` |
| `SubAccountTransferHistoryForSubAccountErrorBody` | `binance/errors/sub_account_transfer_history_for_sub_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.sub_account_s_status_on_margin_futures_for_master_account

- **Route**: `GET /sapi/v1/sub-account/status`
- **Signature**: `def sub_account_s_status_on_margin_futures_for_master_account(timestamp: int, signature: str, *, email: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `email` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1SubAccountStatusResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1SubAccountStatusResponse], SubAccountSStatusOnMarginFuturesForMasterAccountErrorBody]`
- **Error**: `SubAccountSStatusOnMarginFuturesForMasterAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SubAccountStatusResponse` | `binance/models/sapi_v1_sub_account_status_response.py` |
| `SubAccountSStatusOnMarginFuturesForMasterAccountErrorBody` | `binance/errors/sub_account_s_status_on_margin_futures_for_master_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.summary_of_sub_account_s_futures_account_for_master_account

- **Route**: `GET /sapi/v1/sub-account/futures/accountSummary`
- **Signature**: `def summary_of_sub_account_s_futures_account_for_master_account(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SubAccountFuturesAccountSummaryResponse`
- **Returns (raw)**: `ApiResult[SapiV1SubAccountFuturesAccountSummaryResponse, SummaryOfSubAccountSFuturesAccountForMasterAccountErrorBody]`
- **Error**: `SummaryOfSubAccountSFuturesAccountForMasterAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SubAccountFuturesAccountSummaryResponse` | `binance/models/sapi_v1_sub_account_futures_account_summary_response.py` |
| `SummaryOfSubAccountSFuturesAccountForMasterAccountErrorBody` | `binance/errors/summary_of_sub_account_s_futures_account_for_master_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.summary_of_sub_account_s_futures_account_v2_for_master_account

- **Route**: `GET /sapi/v2/sub-account/futures/accountSummary`
- **Signature**: `def summary_of_sub_account_s_futures_account_v2_for_master_account(futures_type: int, timestamp: int, signature: str, *, page: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `futures_type`, `timestamp`, `signature`
- **Params**: `futures_type` — query `futuresType` · `timestamp` — query · `signature` — query · `page` — query · `limit` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV2SubAccountFuturesAccountSummaryResponse`
- **Returns (raw)**: `ApiResult[SapiV2SubAccountFuturesAccountSummaryResponse, SummaryOfSubAccountSFuturesAccountV2ForMasterAccountErrorBody]`
- **Error**: `SummaryOfSubAccountSFuturesAccountV2ForMasterAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV2SubAccountFuturesAccountSummaryResponse` | `binance/models/unions/sapi_v2_sub_account_futures_account_summary_response.py` |
| `SummaryOfSubAccountSFuturesAccountV2ForMasterAccountErrorBody` | `binance/errors/summary_of_sub_account_s_futures_account_v2_for_master_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.summary_of_sub_account_s_margin_account_for_master_account

- **Route**: `GET /sapi/v1/sub-account/margin/accountSummary`
- **Signature**: `def summary_of_sub_account_s_margin_account_for_master_account(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SubAccountMarginAccountSummaryResponse`
- **Returns (raw)**: `ApiResult[SapiV1SubAccountMarginAccountSummaryResponse, SummaryOfSubAccountSMarginAccountForMasterAccountErrorBody]`
- **Error**: `SummaryOfSubAccountSMarginAccountForMasterAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SubAccountMarginAccountSummaryResponse` | `binance/models/sapi_v1_sub_account_margin_account_summary_response.py` |
| `SummaryOfSubAccountSMarginAccountForMasterAccountErrorBody` | `binance/errors/summary_of_sub_account_s_margin_account_for_master_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.transfer_for_sub_account_for_master_account

- **Route**: `POST /sapi/v1/sub-account/futures/transfer`
- **Signature**: `def transfer_for_sub_account_for_master_account(email: str, asset: str, amount: float, type_: int, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `email`, `asset`, `amount`, `type_`, `timestamp`, `signature`
- **Params**: `email` — query · `asset` — query · `amount` — query · `type_` — query `type` · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SubAccountFuturesTransferResponse`
- **Returns (raw)**: `ApiResult[SapiV1SubAccountFuturesTransferResponse, TransferForSubAccountForMasterAccountErrorBody]`
- **Error**: `TransferForSubAccountForMasterAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SubAccountFuturesTransferResponse` | `binance/models/sapi_v1_sub_account_futures_transfer_response.py` |
| `TransferForSubAccountForMasterAccountErrorBody` | `binance/errors/transfer_for_sub_account_for_master_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.transfer_to_master_for_sub_account

- **Route**: `POST /sapi/v1/sub-account/transfer/subToMaster`
- **Signature**: `def transfer_to_master_for_sub_account(asset: str, amount: float, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `asset`, `amount`, `timestamp`, `signature`
- **Params**: `asset` — query · `amount` — query · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SubAccountTransferSubToMasterResponse`
- **Returns (raw)**: `ApiResult[SapiV1SubAccountTransferSubToMasterResponse, TransferToMasterForSubAccountErrorBody]`
- **Error**: `TransferToMasterForSubAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SubAccountTransferSubToMasterResponse` | `binance/models/sapi_v1_sub_account_transfer_sub_to_master_response.py` |
| `TransferToMasterForSubAccountErrorBody` | `binance/errors/transfer_to_master_for_sub_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.transfer_to_sub_account_of_same_master_for_sub_account

- **Route**: `POST /sapi/v1/sub-account/transfer/subToSub`
- **Signature**: `def transfer_to_sub_account_of_same_master_for_sub_account(to_email: str, asset: str, amount: float, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `to_email`, `asset`, `amount`, `timestamp`, `signature`
- **Params**: `to_email` — query `toEmail` · `asset` — query · `amount` — query · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SubAccountTransferSubToSubResponse`
- **Returns (raw)**: `ApiResult[SapiV1SubAccountTransferSubToSubResponse, TransferToSubAccountOfSameMasterForSubAccountErrorBody]`
- **Error**: `TransferToSubAccountOfSameMasterForSubAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SubAccountTransferSubToSubResponse` | `binance/models/sapi_v1_sub_account_transfer_sub_to_sub_response.py` |
| `TransferToSubAccountOfSameMasterForSubAccountErrorBody` | `binance/errors/transfer_to_sub_account_of_same_master_for_sub_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.universal_transfer_for_master_account

- **Route**: `POST /sapi/v1/sub-account/universalTransfer`
- **Signature**: `def universal_transfer_for_master_account(from_account_type: FromAccountTypeOrStr, to_account_type: ToAccountTypeOrStr, asset: str, amount: float, timestamp: int, signature: str, *, from_email: str | None = None, to_email: str | None = None, client_tran_id: str | None = None, symbol: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `from_account_type`, `to_account_type`, `asset`, `amount`, `timestamp`, `signature`
- **Params**: `from_account_type` — query `fromAccountType` · `to_account_type` — query `toAccountType` · `asset` — query · `amount` — query · `timestamp` — query · `signature` — query · `from_email` — query `fromEmail` · `to_email` — query `toEmail` · `client_tran_id` — query `clientTranId` · `symbol` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1SubAccountUniversalTransferResponse1`
- **Returns (raw)**: `ApiResult[SapiV1SubAccountUniversalTransferResponse1, UniversalTransferForMasterAccountErrorBody]`
- **Error**: `UniversalTransferForMasterAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FromAccountTypeOrStr` | `binance/models/enums/from_account_type.py` |
| `ToAccountTypeOrStr` | `binance/models/enums/to_account_type.py` |
| `SapiV1SubAccountUniversalTransferResponse1` | `binance/models/sapi_v1_sub_account_universal_transfer_response1.py` |
| `UniversalTransferForMasterAccountErrorBody` | `binance/errors/universal_transfer_for_master_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.universal_transfer_history_for_master_account

- **Route**: `GET /sapi/v1/sub-account/universalTransfer`
- **Signature**: `def universal_transfer_history_for_master_account(timestamp: int, signature: str, *, from_email: str | None = None, to_email: str | None = None, client_tran_id: str | None = None, start_time: int | None = None, end_time: int | None = None, page: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `from_email` — query `fromEmail` · `to_email` — query `toEmail` · `client_tran_id` — query `clientTranId` · `start_time` — query `startTime` · `end_time` — query `endTime` · `page` — query · `limit` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1SubAccountUniversalTransferResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1SubAccountUniversalTransferResponse], UniversalTransferHistoryForMasterAccountErrorBody]`
- **Error**: `UniversalTransferHistoryForMasterAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SubAccountUniversalTransferResponse` | `binance/models/sapi_v1_sub_account_universal_transfer_response.py` |
| `UniversalTransferHistoryForMasterAccountErrorBody` | `binance/errors/universal_transfer_history_for_master_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.update_ip_restriction_for_sub_account_api_key_for_master_account

- **Route**: `POST /sapi/v2/sub-account/subAccountApi/ipRestriction`
- **Signature**: `def update_ip_restriction_for_sub_account_api_key_for_master_account(email: str, sub_account_api_key: str, status: str, timestamp: int, signature: str, *, third_party_name: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `email`, `sub_account_api_key`, `status`, `timestamp`, `signature`
- **Params**: `email` — query · `sub_account_api_key` — query `subAccountApiKey` · `status` — query · `timestamp` — query · `signature` — query · `third_party_name` — query `thirdPartyName` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV2SubAccountSubAccountApiIpRestrictionResponse`
- **Returns (raw)**: `ApiResult[SapiV2SubAccountSubAccountApiIpRestrictionResponse, UpdateIpRestrictionForSubAccountApiKeyForMasterAccountErrorBody]`
- **Error**: `UpdateIpRestrictionForSubAccountApiKeyForMasterAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV2SubAccountSubAccountApiIpRestrictionResponse` | `binance/models/sapi_v2_sub_account_sub_account_api_ip_restriction_response.py` |
| `UpdateIpRestrictionForSubAccountApiKeyForMasterAccountErrorBody` | `binance/errors/update_ip_restriction_for_sub_account_api_key_for_master_account_error.py` |
| `Error` | `binance/models/error.py` |

### client.sub_account_api.withdrawl_assets_from_the_managed_sub_account_for_investor_master_account

- **Route**: `POST /sapi/v1/managed-subaccount/withdraw`
- **Signature**: `def withdrawl_assets_from_the_managed_sub_account_for_investor_master_account(from_email: str, asset: str, amount: float, timestamp: int, signature: str, *, transfer_date: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `from_email`, `asset`, `amount`, `timestamp`, `signature`
- **Params**: `from_email` — query `fromEmail` · `asset` — query · `amount` — query · `timestamp` — query · `signature` — query · `transfer_date` — query `transferDate` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1ManagedSubaccountWithdrawResponse`
- **Returns (raw)**: `ApiResult[SapiV1ManagedSubaccountWithdrawResponse, WithdrawlAssetsFromTheManagedSubAccountForInvestorMasterAccountErrorBody]`
- **Error**: `WithdrawlAssetsFromTheManagedSubAccountForInvestorMasterAccountErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1ManagedSubaccountWithdrawResponse` | `binance/models/sapi_v1_managed_subaccount_withdraw_response.py` |
| `WithdrawlAssetsFromTheManagedSubAccountForInvestorMasterAccountErrorBody` | `binance/errors/withdrawl_assets_from_the_managed_sub_account_for_investor_master_account_error.py` |
| `Error` | `binance/models/error.py` |

