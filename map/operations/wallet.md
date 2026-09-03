<!-- Generated file — do not edit; regenerated with the SDK. -->

# Wallet — operations

Accessor: `client.wallet` · Source: `binance_public_spot_api/apis/wallet.py` · 34 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.wallet.account_api_trading_status_user_data

- **Route**: `GET /sapi/v1/account/apiTradingStatus`
- **Auth**: `api_key_auth`
- **Signature**: `def account_api_trading_status_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1AccountApiTradingStatusResponse`
- **Returns (raw)**: `ApiResult[SapiV1AccountApiTradingStatusResponse, AccountApiTradingStatusUserDataErrorBody]`
- **Error**: `AccountApiTradingStatusUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1AccountApiTradingStatusResponse` | `binance_public_spot_api/models/sapi_v1_account_api_trading_status_response.py` |
| `AccountApiTradingStatusUserDataErrorBody` | `binance_public_spot_api/errors/account_api_trading_status_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.wallet.account_status_user_data

- **Route**: `GET /sapi/v1/account/status`
- **Auth**: `api_key_auth`
- **Signature**: `def account_status_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1AccountStatusResponse`
- **Returns (raw)**: `ApiResult[SapiV1AccountStatusResponse, AccountStatusUserDataErrorBody]`
- **Error**: `AccountStatusUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1AccountStatusResponse` | `binance_public_spot_api/models/sapi_v1_account_status_response.py` |
| `AccountStatusUserDataErrorBody` | `binance_public_spot_api/errors/account_status_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.wallet.account_info_user_data

- **Route**: `GET /sapi/v1/account/info`
- **Auth**: `api_key_auth`
- **Signature**: `def account_info_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1AccountInfoResponse`
- **Returns (raw)**: `ApiResult[SapiV1AccountInfoResponse, AccountInfoUserDataErrorBody]`
- **Error**: `AccountInfoUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1AccountInfoResponse` | `binance_public_spot_api/models/sapi_v1_account_info_response.py` |
| `AccountInfoUserDataErrorBody` | `binance_public_spot_api/errors/account_info_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.wallet.all_coins_information_user_data

- **Route**: `GET /sapi/v1/capital/config/getall`
- **Auth**: `api_key_auth`
- **Signature**: `def all_coins_information_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1CapitalConfigGetallResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1CapitalConfigGetallResponse], AllCoinsInformationUserDataErrorBody]`
- **Error**: `AllCoinsInformationUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1CapitalConfigGetallResponse` | `binance_public_spot_api/models/sapi_v1_capital_config_getall_response.py` |
| `AllCoinsInformationUserDataErrorBody` | `binance_public_spot_api/errors/all_coins_information_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.wallet.asset_detail_user_data

- **Route**: `GET /sapi/v1/asset/assetDetail`
- **Auth**: `api_key_auth`
- **Signature**: `def asset_detail_user_data(timestamp: int, signature: str, *, asset: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `asset` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1AssetAssetDetailResponse`
- **Returns (raw)**: `ApiResult[SapiV1AssetAssetDetailResponse, AssetDetailUserDataErrorBody]`
- **Error**: `AssetDetailUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1AssetAssetDetailResponse` | `binance_public_spot_api/models/sapi_v1_asset_asset_detail_response.py` |
| `AssetDetailUserDataErrorBody` | `binance_public_spot_api/errors/asset_detail_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.wallet.asset_dividend_record_user_data

- **Route**: `GET /sapi/v1/asset/assetDividend`
- **Auth**: `api_key_auth`
- **Signature**: `def asset_dividend_record_user_data(timestamp: int, signature: str, *, asset: str | None = None, start_time: int | None = None, end_time: int | None = None, limit: int | None = 20, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `asset` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `limit` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1AssetAssetDividendResponse`
- **Returns (raw)**: `ApiResult[SapiV1AssetAssetDividendResponse, AssetDividendRecordUserDataErrorBody]`
- **Error**: `AssetDividendRecordUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1AssetAssetDividendResponse` | `binance_public_spot_api/models/sapi_v1_asset_asset_dividend_response.py` |
| `AssetDividendRecordUserDataErrorBody` | `binance_public_spot_api/errors/asset_dividend_record_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.wallet.convert_transfer_user_data

- **Route**: `POST /sapi/v1/asset/convert-transfer`
- **Auth**: `api_key_auth`
- **Signature**: `def convert_transfer_user_data(client_tran_id: str, asset: str, amount: float, target_asset: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `client_tran_id`, `asset`, `amount`, `target_asset`, `timestamp`, `signature`
- **Params**: `client_tran_id` — query `clientTranId` · `asset` — query · `amount` — query · `target_asset` — query `targetAsset` · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1AssetConvertTransferResponse`
- **Returns (raw)**: `ApiResult[SapiV1AssetConvertTransferResponse, ConvertTransferUserDataErrorBody]`
- **Error**: `ConvertTransferUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1AssetConvertTransferResponse` | `binance_public_spot_api/models/sapi_v1_asset_convert_transfer_response.py` |
| `ConvertTransferUserDataErrorBody` | `binance_public_spot_api/errors/convert_transfer_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.wallet.daily_account_snapshot_user_data

- **Route**: `GET /sapi/v1/accountSnapshot`
- **Auth**: `api_key_auth`
- **Signature**: `def daily_account_snapshot_user_data(type_: Type6OrStr, timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, limit: int | None = 7, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `type_`, `timestamp`, `signature`
- **Params**: `type_` — query `type` · `timestamp` — query · `signature` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `limit` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1AccountSnapshotResponse`
- **Returns (raw)**: `ApiResult[SapiV1AccountSnapshotResponse, DailyAccountSnapshotUserDataErrorBody]`
- **Error**: `DailyAccountSnapshotUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Type6OrStr` | `binance_public_spot_api/models/enums/type6.py` |
| `SapiV1AccountSnapshotResponse` | `binance_public_spot_api/models/unions/sapi_v1_account_snapshot_response.py` |
| `DailyAccountSnapshotUserDataErrorBody` | `binance_public_spot_api/errors/daily_account_snapshot_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.wallet.deposit_address_supporting_network_user_data

- **Route**: `GET /sapi/v1/capital/deposit/address`
- **Auth**: `api_key_auth`
- **Signature**: `def deposit_address_supporting_network_user_data(coin: str, timestamp: int, signature: str, *, network: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `coin`, `timestamp`, `signature`
- **Params**: `coin` — query · `timestamp` — query · `signature` — query · `network` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1CapitalDepositAddressResponse`
- **Returns (raw)**: `ApiResult[SapiV1CapitalDepositAddressResponse, DepositAddressSupportingNetworkUserDataErrorBody]`
- **Error**: `DepositAddressSupportingNetworkUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1CapitalDepositAddressResponse` | `binance_public_spot_api/models/sapi_v1_capital_deposit_address_response.py` |
| `DepositAddressSupportingNetworkUserDataErrorBody` | `binance_public_spot_api/errors/deposit_address_supporting_network_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.wallet.deposit_history_supporting_network_user_data

- **Route**: `GET /sapi/v1/capital/deposit/hisrec`
- **Auth**: `api_key_auth`
- **Signature**: `def deposit_history_supporting_network_user_data(timestamp: int, signature: str, *, coin: str | None = None, status: int | None = None, start_time: int | None = None, end_time: int | None = None, offset: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `coin` — query · `status` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `offset` — query · `limit` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1CapitalDepositHisrecResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1CapitalDepositHisrecResponse], DepositHistorySupportingNetworkUserDataErrorBody]`
- **Error**: `DepositHistorySupportingNetworkUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1CapitalDepositHisrecResponse` | `binance_public_spot_api/models/sapi_v1_capital_deposit_hisrec_response.py` |
| `DepositHistorySupportingNetworkUserDataErrorBody` | `binance_public_spot_api/errors/deposit_history_supporting_network_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.wallet.disable_fast_withdraw_switch_user_data

- **Route**: `POST /sapi/v1/account/disableFastWithdrawSwitch`
- **Auth**: `api_key_auth`
- **Signature**: `def disable_fast_withdraw_switch_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, DisableFastWithdrawSwitchUserDataErrorBody]`
- **Error**: `DisableFastWithdrawSwitchUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DisableFastWithdrawSwitchUserDataErrorBody` | `binance_public_spot_api/errors/disable_fast_withdraw_switch_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.wallet.dust_transfer_user_data

- **Route**: `POST /sapi/v1/asset/dust`
- **Auth**: `api_key_auth`
- **Signature**: `def dust_transfer_user_data(asset: list[str], timestamp: int, signature: str, *, account_type: AccountTypeOrStr | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `asset`, `timestamp`, `signature`
- **Params**: `asset` — query · `timestamp` — query · `signature` — query · `account_type` — query `accountType` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1AssetDustResponse`
- **Returns (raw)**: `ApiResult[SapiV1AssetDustResponse, DustTransferUserDataErrorBody]`
- **Error**: `DustTransferUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AccountTypeOrStr` | `binance_public_spot_api/models/enums/account_type.py` |
| `SapiV1AssetDustResponse` | `binance_public_spot_api/models/sapi_v1_asset_dust_response.py` |
| `DustTransferUserDataErrorBody` | `binance_public_spot_api/errors/dust_transfer_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.wallet.dust_log_user_data

- **Route**: `GET /sapi/v1/asset/dribblet`
- **Auth**: `api_key_auth`
- **Signature**: `def dust_log_user_data(timestamp: int, signature: str, *, account_type: AccountTypeOrStr | None = None, start_time: int | None = None, end_time: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `account_type` — query `accountType` · `start_time` — query `startTime` · `end_time` — query `endTime` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1AssetDribbletResponse`
- **Returns (raw)**: `ApiResult[SapiV1AssetDribbletResponse, DustLogUserDataErrorBody]`
- **Error**: `DustLogUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AccountTypeOrStr` | `binance_public_spot_api/models/enums/account_type.py` |
| `SapiV1AssetDribbletResponse` | `binance_public_spot_api/models/sapi_v1_asset_dribblet_response.py` |
| `DustLogUserDataErrorBody` | `binance_public_spot_api/errors/dust_log_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.wallet.enable_fast_withdraw_switch_user_data

- **Route**: `POST /sapi/v1/account/enableFastWithdrawSwitch`
- **Auth**: `api_key_auth`
- **Signature**: `def enable_fast_withdraw_switch_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, EnableFastWithdrawSwitchUserDataErrorBody]`
- **Error**: `EnableFastWithdrawSwitchUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `EnableFastWithdrawSwitchUserDataErrorBody` | `binance_public_spot_api/errors/enable_fast_withdraw_switch_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.wallet.fetch_deposit_address_list_with_network_user_data

- **Route**: `GET /sapi/v1/capital/deposit/address/list`
- **Auth**: `api_key_auth`
- **Signature**: `def fetch_deposit_address_list_with_network_user_data(coin: str, timestamp: int, signature: str, *, network: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `coin`, `timestamp`, `signature`
- **Params**: `coin` — query · `timestamp` — query · `signature` — query · `network` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1CapitalDepositAddressListResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1CapitalDepositAddressListResponse], FetchDepositAddressListWithNetworkUserDataErrorBody]`
- **Error**: `FetchDepositAddressListWithNetworkUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1CapitalDepositAddressListResponse` | `binance_public_spot_api/models/sapi_v1_capital_deposit_address_list_response.py` |
| `FetchDepositAddressListWithNetworkUserDataErrorBody` | `binance_public_spot_api/errors/fetch_deposit_address_list_with_network_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.wallet.fetch_withdraw_address_list_user_data

- **Route**: `GET /sapi/v1/capital/withdraw/address/list`
- **Auth**: `api_key_auth`
- **Signature**: `def fetch_withdraw_address_list_user_data(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `list[SapiV1CapitalWithdrawAddressListResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1CapitalWithdrawAddressListResponse], FetchWithdrawAddressListUserDataErrorBody]`
- **Error**: `FetchWithdrawAddressListUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1CapitalWithdrawAddressListResponse` | `binance_public_spot_api/models/sapi_v1_capital_withdraw_address_list_response.py` |
| `FetchWithdrawAddressListUserDataErrorBody` | `binance_public_spot_api/errors/fetch_withdraw_address_list_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.wallet.funding_wallet_user_data

- **Route**: `POST /sapi/v1/asset/get-funding-asset`
- **Auth**: `api_key_auth`
- **Signature**: `def funding_wallet_user_data(timestamp: int, signature: str, *, asset: str | None = None, need_btc_valuation: NeedBtcValuationOrStr | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `asset` — query · `need_btc_valuation` — query `needBtcValuation` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1AssetGetFundingAssetResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1AssetGetFundingAssetResponse], FundingWalletUserDataErrorBody]`
- **Error**: `FundingWalletUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `NeedBtcValuationOrStr` | `binance_public_spot_api/models/enums/need_btc_valuation.py` |
| `SapiV1AssetGetFundingAssetResponse` | `binance_public_spot_api/models/sapi_v1_asset_get_funding_asset_response.py` |
| `FundingWalletUserDataErrorBody` | `binance_public_spot_api/errors/funding_wallet_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.wallet.get_api_key_permission_user_data

- **Route**: `GET /sapi/v1/account/apiRestrictions`
- **Auth**: `api_key_auth`
- **Signature**: `def get_api_key_permission_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1AccountApiRestrictionsResponse`
- **Returns (raw)**: `ApiResult[SapiV1AccountApiRestrictionsResponse, GetApiKeyPermissionUserDataErrorBody]`
- **Error**: `GetApiKeyPermissionUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1AccountApiRestrictionsResponse` | `binance_public_spot_api/models/sapi_v1_account_api_restrictions_response.py` |
| `GetApiKeyPermissionUserDataErrorBody` | `binance_public_spot_api/errors/get_api_key_permission_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.wallet.get_assets_that_can_be_converted_into_bnb_user_data

- **Route**: `POST /sapi/v1/asset/dust-btc`
- **Auth**: `api_key_auth`
- **Signature**: `def get_assets_that_can_be_converted_into_bnb_user_data(timestamp: int, signature: str, *, account_type: AccountTypeOrStr | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `account_type` — query `accountType` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1AssetDustBtcResponse`
- **Returns (raw)**: `ApiResult[SapiV1AssetDustBtcResponse, GetAssetsThatCanBeConvertedIntoBnbUserDataErrorBody]`
- **Error**: `GetAssetsThatCanBeConvertedIntoBnbUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AccountTypeOrStr` | `binance_public_spot_api/models/enums/account_type.py` |
| `SapiV1AssetDustBtcResponse` | `binance_public_spot_api/models/sapi_v1_asset_dust_btc_response.py` |
| `GetAssetsThatCanBeConvertedIntoBnbUserDataErrorBody` | `binance_public_spot_api/errors/get_assets_that_can_be_converted_into_bnb_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.wallet.get_cloud_mining_payment_and_refund_history_user_data

- **Route**: `GET /sapi/v1/asset/ledger-transfer/cloud-mining/queryByPage`
- **Auth**: `api_key_auth`
- **Signature**: `def get_cloud_mining_payment_and_refund_history_user_data(start_time: int, end_time: int, timestamp: int, signature: str, *, tran_id: int | None = None, client_tran_id: str | None = None, asset: str | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `start_time`, `end_time`, `timestamp`, `signature`
- **Params**: `start_time` — query `startTime` · `end_time` — query `endTime` · `timestamp` — query · `signature` — query · `tran_id` — query `tranId` · `client_tran_id` — query `clientTranId` · `asset` — query · `current` — query · `size` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1AssetLedgerTransferCloudMiningQueryByPageResponse`
- **Returns (raw)**: `ApiResult[SapiV1AssetLedgerTransferCloudMiningQueryByPageResponse, GetCloudMiningPaymentAndRefundHistoryUserDataErrorBody]`
- **Error**: `GetCloudMiningPaymentAndRefundHistoryUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1AssetLedgerTransferCloudMiningQueryByPageResponse` | `binance_public_spot_api/models/sapi_v1_asset_ledger_transfer_cloud_mining_query_by_page_response.py` |
| `GetCloudMiningPaymentAndRefundHistoryUserDataErrorBody` | `binance_public_spot_api/errors/get_cloud_mining_payment_and_refund_history_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.wallet.get_symbols_delist_schedule_for_spot_market_data

- **Route**: `GET /sapi/v1/spot/delist-schedule`
- **Auth**: `api_key_auth`
- **Signature**: `def get_symbols_delist_schedule_for_spot_market_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1SpotDelistScheduleResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1SpotDelistScheduleResponse], GetSymbolsDelistScheduleForSpotMarketDataErrorBody]`
- **Error**: `GetSymbolsDelistScheduleForSpotMarketDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1SpotDelistScheduleResponse` | `binance_public_spot_api/models/sapi_v1_spot_delist_schedule_response.py` |
| `GetSymbolsDelistScheduleForSpotMarketDataErrorBody` | `binance_public_spot_api/errors/get_symbols_delist_schedule_for_spot_market_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.wallet.one_click_arrival_deposit_apply_user_data

- **Route**: `POST /sapi/v1/capital/deposit/credit-apply`
- **Auth**: `api_key_auth`
- **Signature**: `def one_click_arrival_deposit_apply_user_data(timestamp: int, signature: str, *, deposit_id: int | None = None, tx_id: str | None = None, sub_account_id: int | None = None, sub_user_id: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `deposit_id` — query `depositId` · `tx_id` — query `txId` · `sub_account_id` — query `subAccountId` · `sub_user_id` — query `subUserId` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1CapitalDepositCreditApplyResponse`
- **Returns (raw)**: `ApiResult[SapiV1CapitalDepositCreditApplyResponse, OneClickArrivalDepositApplyUserDataErrorBody]`
- **Error**: `OneClickArrivalDepositApplyUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1CapitalDepositCreditApplyResponse` | `binance_public_spot_api/models/sapi_v1_capital_deposit_credit_apply_response.py` |
| `OneClickArrivalDepositApplyUserDataErrorBody` | `binance_public_spot_api/errors/one_click_arrival_deposit_apply_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.wallet.query_convert_transfer_user_data

- **Route**: `GET /sapi/v1/asset/convert-transfer/queryByPage`
- **Auth**: `api_key_auth`
- **Signature**: `def query_convert_transfer_user_data(start_time: int, end_time: int, timestamp: int, signature: str, *, tran_id: int | None = None, asset: str | None = None, account_type: AccountType3OrStr | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `start_time`, `end_time`, `timestamp`, `signature`
- **Params**: `start_time` — query `startTime` · `end_time` — query `endTime` · `timestamp` — query · `signature` — query · `tran_id` — query `tranId` · `asset` — query · `account_type` — query `accountType` · `current` — query · `size` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1AssetConvertTransferQueryByPageResponse`
- **Returns (raw)**: `ApiResult[SapiV1AssetConvertTransferQueryByPageResponse, QueryConvertTransferUserDataErrorBody]`
- **Error**: `QueryConvertTransferUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AccountType3OrStr` | `binance_public_spot_api/models/enums/account_type3.py` |
| `SapiV1AssetConvertTransferQueryByPageResponse` | `binance_public_spot_api/models/sapi_v1_asset_convert_transfer_query_by_page_response.py` |
| `QueryConvertTransferUserDataErrorBody` | `binance_public_spot_api/errors/query_convert_transfer_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.wallet.query_user_delegation_history_for_master_account_user_data

- **Route**: `GET /sapi/v1/asset/custody/transfer-history`
- **Auth**: `api_key_auth`
- **Signature**: `def query_user_delegation_history_for_master_account_user_data(email: str, start_time: int, end_time: int, asset: str, timestamp: int, signature: str, *, type_: str | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `email`, `start_time`, `end_time`, `asset`, `timestamp`, `signature`
- **Params**: `email` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `asset` — query · `timestamp` — query · `signature` — query · `type_` — query `type` · `current` — query · `size` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1AssetCustodyTransferHistoryResponse`
- **Returns (raw)**: `ApiResult[SapiV1AssetCustodyTransferHistoryResponse, QueryUserDelegationHistoryForMasterAccountUserDataErrorBody]`
- **Error**: `QueryUserDelegationHistoryForMasterAccountUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1AssetCustodyTransferHistoryResponse` | `binance_public_spot_api/models/sapi_v1_asset_custody_transfer_history_response.py` |
| `QueryUserDelegationHistoryForMasterAccountUserDataErrorBody` | `binance_public_spot_api/errors/query_user_delegation_history_for_master_account_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.wallet.query_user_universal_transfer_history_user_data

- **Route**: `GET /sapi/v1/asset/transfer`
- **Auth**: `api_key_auth`
- **Signature**: `def query_user_universal_transfer_history_user_data(type_: Type7OrStr, timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, current: int | None = None, size: int | None = None, from_symbol: str | None = None, to_symbol: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `type_`, `timestamp`, `signature`
- **Params**: `type_` — query `type` · `timestamp` — query · `signature` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `current` — query · `size` — query · `from_symbol` — query `fromSymbol` · `to_symbol` — query `toSymbol` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1AssetTransferResponse`
- **Returns (raw)**: `ApiResult[SapiV1AssetTransferResponse, QueryUserUniversalTransferHistoryUserDataErrorBody]`
- **Error**: `QueryUserUniversalTransferHistoryUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Type7OrStr` | `binance_public_spot_api/models/enums/type7.py` |
| `SapiV1AssetTransferResponse` | `binance_public_spot_api/models/sapi_v1_asset_transfer_response.py` |
| `QueryUserUniversalTransferHistoryUserDataErrorBody` | `binance_public_spot_api/errors/query_user_universal_transfer_history_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.wallet.query_user_wallet_balance_user_data

- **Route**: `GET /sapi/v1/asset/wallet/balance`
- **Auth**: `api_key_auth`
- **Signature**: `def query_user_wallet_balance_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1AssetWalletBalanceResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1AssetWalletBalanceResponse], QueryUserWalletBalanceUserDataErrorBody]`
- **Error**: `QueryUserWalletBalanceUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1AssetWalletBalanceResponse` | `binance_public_spot_api/models/sapi_v1_asset_wallet_balance_response.py` |
| `QueryUserWalletBalanceUserDataErrorBody` | `binance_public_spot_api/errors/query_user_wallet_balance_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.wallet.query_auto_converting_stable_coins_user_data

- **Route**: `GET /sapi/v1/capital/contract/convertible-coins`
- **Auth**: `api_key_auth`
- **Signature**: `def query_auto_converting_stable_coins_user_data(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `SapiV1CapitalContractConvertibleCoinsResponse`
- **Returns (raw)**: `ApiResult[SapiV1CapitalContractConvertibleCoinsResponse, QueryAutoConvertingStableCoinsUserDataErrorBody]`
- **Error**: `QueryAutoConvertingStableCoinsUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1CapitalContractConvertibleCoinsResponse` | `binance_public_spot_api/models/sapi_v1_capital_contract_convertible_coins_response.py` |
| `QueryAutoConvertingStableCoinsUserDataErrorBody` | `binance_public_spot_api/errors/query_auto_converting_stable_coins_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.wallet.switch_on_off_busd_and_stable_coins_conversion_user_data_user_data

- **Route**: `POST /sapi/v1/capital/contract/convertible-coins`
- **Auth**: `api_key_auth`
- **Signature**: `def switch_on_off_busd_and_stable_coins_conversion_user_data_user_data(coin: str, enable: bool, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `coin`, `enable`
- **Params**: `coin` — query · `enable` — query
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, SwitchOnOffBusdAndStableCoinsConversionUserDataUserDataErrorBody]`
- **Error**: `SwitchOnOffBusdAndStableCoinsConversionUserDataUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SwitchOnOffBusdAndStableCoinsConversionUserDataUserDataErrorBody` | `binance_public_spot_api/errors/switch_on_off_busd_and_stable_coins_conversion_user_data_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.wallet.system_status_system

- **Route**: `GET /sapi/v1/system/status`
- **Signature**: `def system_status_system(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `SapiV1SystemStatusResponse`
- **Returns (raw)**: `ApiResult[SapiV1SystemStatusResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SapiV1SystemStatusResponse` | `binance_public_spot_api/models/sapi_v1_system_status_response.py` |

### client.wallet.trade_fee_user_data

- **Route**: `GET /sapi/v1/asset/tradeFee`
- **Auth**: `api_key_auth`
- **Signature**: `def trade_fee_user_data(timestamp: int, signature: str, *, symbol: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `symbol` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1AssetTradeFeeResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1AssetTradeFeeResponse], TradeFeeUserDataErrorBody]`
- **Error**: `TradeFeeUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1AssetTradeFeeResponse` | `binance_public_spot_api/models/sapi_v1_asset_trade_fee_response.py` |
| `TradeFeeUserDataErrorBody` | `binance_public_spot_api/errors/trade_fee_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.wallet.user_asset_user_data

- **Route**: `POST /sapi/v3/asset/getUserAsset`
- **Auth**: `api_key_auth`
- **Signature**: `def user_asset_user_data(timestamp: int, signature: str, *, asset: str | None = None, need_btc_valuation: NeedBtcValuationOrStr | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `asset` — query · `need_btc_valuation` — query `needBtcValuation` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV3AssetGetUserAssetResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV3AssetGetUserAssetResponse], UserAssetUserDataErrorBody]`
- **Error**: `UserAssetUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `NeedBtcValuationOrStr` | `binance_public_spot_api/models/enums/need_btc_valuation.py` |
| `SapiV3AssetGetUserAssetResponse` | `binance_public_spot_api/models/sapi_v3_asset_get_user_asset_response.py` |
| `UserAssetUserDataErrorBody` | `binance_public_spot_api/errors/user_asset_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.wallet.user_universal_transfer_user_data

- **Route**: `POST /sapi/v1/asset/transfer`
- **Auth**: `api_key_auth`
- **Signature**: `def user_universal_transfer_user_data(type_: Type7OrStr, asset: str, amount: float, timestamp: int, signature: str, *, from_symbol: str | None = None, to_symbol: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `type_`, `asset`, `amount`, `timestamp`, `signature`
- **Params**: `type_` — query `type` · `asset` — query · `amount` — query · `timestamp` — query · `signature` — query · `from_symbol` — query `fromSymbol` · `to_symbol` — query `toSymbol` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1AssetTransferResponse1`
- **Returns (raw)**: `ApiResult[SapiV1AssetTransferResponse1, UserUniversalTransferUserDataErrorBody]`
- **Error**: `UserUniversalTransferUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Type7OrStr` | `binance_public_spot_api/models/enums/type7.py` |
| `SapiV1AssetTransferResponse1` | `binance_public_spot_api/models/sapi_v1_asset_transfer_response1.py` |
| `UserUniversalTransferUserDataErrorBody` | `binance_public_spot_api/errors/user_universal_transfer_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.wallet.withdraw_user_data

- **Route**: `POST /sapi/v1/capital/withdraw/apply`
- **Auth**: `api_key_auth`
- **Signature**: `def withdraw_user_data(coin: str, address: str, amount: float, timestamp: int, signature: str, *, withdraw_order_id: str | None = None, network: str | None = None, address_tag: str | None = None, transaction_fee_flag: bool | None = False, name: str | None = None, wallet_type: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `coin`, `address`, `amount`, `timestamp`, `signature`
- **Params**: `coin` — query · `address` — query · `amount` — query · `timestamp` — query · `signature` — query · `withdraw_order_id` — query `withdrawOrderId` · `network` — query · `address_tag` — query `addressTag` · `transaction_fee_flag` — query `transactionFeeFlag` · `name` — query · `wallet_type` — query `walletType` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1CapitalWithdrawApplyResponse`
- **Returns (raw)**: `ApiResult[SapiV1CapitalWithdrawApplyResponse, WithdrawUserDataErrorBody]`
- **Error**: `WithdrawUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1CapitalWithdrawApplyResponse` | `binance_public_spot_api/models/sapi_v1_capital_withdraw_apply_response.py` |
| `WithdrawUserDataErrorBody` | `binance_public_spot_api/errors/withdraw_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.wallet.withdraw_history_supporting_network_user_data

- **Route**: `GET /sapi/v1/capital/withdraw/history`
- **Auth**: `api_key_auth`
- **Signature**: `def withdraw_history_supporting_network_user_data(timestamp: int, signature: str, *, coin: str | None = None, withdraw_order_id: str | None = None, status: int | None = None, start_time: int | None = None, end_time: int | None = None, offset: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `coin` — query · `withdraw_order_id` — query `withdrawOrderId` · `status` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `offset` — query · `limit` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1CapitalWithdrawHistoryResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1CapitalWithdrawHistoryResponse], WithdrawHistorySupportingNetworkUserDataErrorBody]`
- **Error**: `WithdrawHistorySupportingNetworkUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1CapitalWithdrawHistoryResponse` | `binance_public_spot_api/models/sapi_v1_capital_withdraw_history_response.py` |
| `WithdrawHistorySupportingNetworkUserDataErrorBody` | `binance_public_spot_api/errors/withdraw_history_supporting_network_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

