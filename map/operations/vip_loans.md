<!-- Generated file — do not edit; regenerated with the SDK. -->

# VipLoans — operations

Accessor: `client.vip_loans` · Source: `binance_public_spot_api/apis/vip_loans.py` · 10 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.vip_loans.check_locked_value_of_vip_collateral_account_user_data

- **Route**: `GET /sapi/v1/loan/vip/collateral/account`
- **Auth**: `api_key_auth`
- **Signature**: `def check_locked_value_of_vip_collateral_account_user_data(timestamp: int, signature: str, *, order_id: int | None = None, collateral_account_id: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `order_id` — query `orderId` · `collateral_account_id` — query `collateralAccountId` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1LoanVipCollateralAccountResponse`
- **Returns (raw)**: `ApiResult[SapiV1LoanVipCollateralAccountResponse, CheckLockedValueOfVipCollateralAccountUserDataErrorBody]`
- **Error**: `CheckLockedValueOfVipCollateralAccountUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1LoanVipCollateralAccountResponse` | `binance_public_spot_api/models/sapi_v1_loan_vip_collateral_account_response.py` |
| `CheckLockedValueOfVipCollateralAccountUserDataErrorBody` | `binance_public_spot_api/errors/check_locked_value_of_vip_collateral_account_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.vip_loans.get_borrow_interest_rate_user_data

- **Route**: `GET /sapi/v1/loan/vip/request/interestRate`
- **Auth**: `api_key_auth`
- **Signature**: `def get_borrow_interest_rate_user_data(timestamp: int, signature: str, *, loan_coin: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `loan_coin` — query `loanCoin` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1LoanVipRequestInterestRateResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1LoanVipRequestInterestRateResponse], GetBorrowInterestRateUserDataErrorBody]`
- **Error**: `GetBorrowInterestRateUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1LoanVipRequestInterestRateResponse` | `binance_public_spot_api/models/sapi_v1_loan_vip_request_interest_rate_response.py` |
| `GetBorrowInterestRateUserDataErrorBody` | `binance_public_spot_api/errors/get_borrow_interest_rate_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.vip_loans.get_collateral_asset_data_user_data

- **Route**: `GET /sapi/v1/loan/vip/collateral/data`
- **Auth**: `api_key_auth`
- **Signature**: `def get_collateral_asset_data_user_data(timestamp: int, signature: str, *, collateral_coin: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `collateral_coin` — query `collateralCoin` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1LoanVipCollateralDataResponse`
- **Returns (raw)**: `ApiResult[SapiV1LoanVipCollateralDataResponse, GetCollateralAssetDataUserDataErrorBody]`
- **Error**: `GetCollateralAssetDataUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1LoanVipCollateralDataResponse` | `binance_public_spot_api/models/sapi_v1_loan_vip_collateral_data_response.py` |
| `GetCollateralAssetDataUserDataErrorBody` | `binance_public_spot_api/errors/get_collateral_asset_data_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.vip_loans.get_loanable_assets_data

- **Route**: `GET /sapi/v1/loan/vip/loanable/data`
- **Auth**: `api_key_auth`
- **Signature**: `def get_loanable_assets_data(timestamp: int, signature: str, *, loan_coin: str | None = None, vip_level: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `loan_coin` — query `loanCoin` · `vip_level` — query `vipLevel` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1LoanVipLoanableDataResponse`
- **Returns (raw)**: `ApiResult[SapiV1LoanVipLoanableDataResponse, GetLoanableAssetsDataErrorBody]`
- **Error**: `GetLoanableAssetsDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1LoanVipLoanableDataResponse` | `binance_public_spot_api/models/sapi_v1_loan_vip_loanable_data_response.py` |
| `GetLoanableAssetsDataErrorBody` | `binance_public_spot_api/errors/get_loanable_assets_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.vip_loans.get_vip_loan_ongoing_orders_user_data

- **Route**: `GET /sapi/v1/loan/vip/ongoing/orders`
- **Auth**: `api_key_auth`
- **Signature**: `def get_vip_loan_ongoing_orders_user_data(timestamp: int, signature: str, *, order_id: int | None = None, collateral_account_id: int | None = None, loan_coin: str | None = None, collateral_coin: str | None = None, current: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `order_id` — query `orderId` · `collateral_account_id` — query `collateralAccountId` · `loan_coin` — query `loanCoin` · `collateral_coin` — query `collateralCoin` · `current` — query · `limit` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1LoanVipOngoingOrdersResponse`
- **Returns (raw)**: `ApiResult[SapiV1LoanVipOngoingOrdersResponse, GetVipLoanOngoingOrdersUserDataErrorBody]`
- **Error**: `GetVipLoanOngoingOrdersUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1LoanVipOngoingOrdersResponse` | `binance_public_spot_api/models/sapi_v1_loan_vip_ongoing_orders_response.py` |
| `GetVipLoanOngoingOrdersUserDataErrorBody` | `binance_public_spot_api/errors/get_vip_loan_ongoing_orders_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.vip_loans.get_vip_loan_repayment_history_user_data

- **Route**: `GET /sapi/v1/loan/vip/repay/history`
- **Auth**: `api_key_auth`
- **Signature**: `def get_vip_loan_repayment_history_user_data(timestamp: int, signature: str, *, order_id: int | None = None, loan_coin: str | None = None, start_time: int | None = None, end_time: int | None = None, current: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `order_id` — query `orderId` · `loan_coin` — query `loanCoin` · `start_time` — query `startTime` · `end_time` — query `endTime` · `current` — query · `limit` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1LoanVipRepayHistoryResponse`
- **Returns (raw)**: `ApiResult[SapiV1LoanVipRepayHistoryResponse, GetVipLoanRepaymentHistoryUserDataErrorBody]`
- **Error**: `GetVipLoanRepaymentHistoryUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1LoanVipRepayHistoryResponse` | `binance_public_spot_api/models/sapi_v1_loan_vip_repay_history_response.py` |
| `GetVipLoanRepaymentHistoryUserDataErrorBody` | `binance_public_spot_api/errors/get_vip_loan_repayment_history_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.vip_loans.query_application_status_user_data

- **Route**: `GET /sapi/v1/loan/vip/request/data`
- **Auth**: `api_key_auth`
- **Signature**: `def query_application_status_user_data(timestamp: int, signature: str, *, current: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `current` — query · `limit` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1LoanVipRequestDataResponse`
- **Returns (raw)**: `ApiResult[SapiV1LoanVipRequestDataResponse, QueryApplicationStatusUserDataErrorBody]`
- **Error**: `QueryApplicationStatusUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1LoanVipRequestDataResponse` | `binance_public_spot_api/models/sapi_v1_loan_vip_request_data_response.py` |
| `QueryApplicationStatusUserDataErrorBody` | `binance_public_spot_api/errors/query_application_status_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.vip_loans.vip_loan_borrow

- **Route**: `POST /sapi/v1/loan/vip/borrow`
- **Auth**: `api_key_auth`
- **Signature**: `def vip_loan_borrow(loan_account_id: int, loan_amount: float, collateral_account_id: str, collateral_coin: str, is_flexible_rate: IsFlexibleRateOrStr, timestamp: int, signature: str, *, loan_coin: str | None = None, loan_term: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `loan_account_id`, `loan_amount`, `collateral_account_id`, `collateral_coin`, `is_flexible_rate`, `timestamp`, `signature`
- **Params**: `loan_account_id` — query `loanAccountId` · `loan_amount` — query `loanAmount` · `collateral_account_id` — query `collateralAccountId` · `collateral_coin` — query `collateralCoin` · `is_flexible_rate` — query `isFlexibleRate` · `timestamp` — query · `signature` — query · `loan_coin` — query `loanCoin` · `loan_term` — query `loanTerm` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1LoanVipBorrowResponse`
- **Returns (raw)**: `ApiResult[SapiV1LoanVipBorrowResponse, VipLoanBorrowErrorBody]`
- **Error**: `VipLoanBorrowErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `IsFlexibleRateOrStr` | `binance_public_spot_api/models/enums/is_flexible_rate.py` |
| `SapiV1LoanVipBorrowResponse` | `binance_public_spot_api/models/sapi_v1_loan_vip_borrow_response.py` |
| `VipLoanBorrowErrorBody` | `binance_public_spot_api/errors/vip_loan_borrow_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.vip_loans.vip_loan_renew

- **Route**: `POST /sapi/v1/loan/vip/renew`
- **Auth**: `api_key_auth`
- **Signature**: `def vip_loan_renew(timestamp: int, signature: str, *, order_id: int | None = None, loan_term: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `order_id` — query `orderId` · `loan_term` — query `loanTerm` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1LoanVipRenewResponse`
- **Returns (raw)**: `ApiResult[SapiV1LoanVipRenewResponse, VipLoanRenewErrorBody]`
- **Error**: `VipLoanRenewErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1LoanVipRenewResponse` | `binance_public_spot_api/models/sapi_v1_loan_vip_renew_response.py` |
| `VipLoanRenewErrorBody` | `binance_public_spot_api/errors/vip_loan_renew_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.vip_loans.vip_loan_repay_trade

- **Route**: `POST /sapi/v1/loan/vip/repay`
- **Auth**: `api_key_auth`
- **Signature**: `def vip_loan_repay_trade(amount: float, timestamp: int, signature: str, *, order_id: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `amount`, `timestamp`, `signature`
- **Params**: `amount` — query · `timestamp` — query · `signature` — query · `order_id` — query `orderId` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1LoanVipRepayResponse`
- **Returns (raw)**: `ApiResult[SapiV1LoanVipRepayResponse, VipLoanRepayTradeErrorBody]`
- **Error**: `VipLoanRepayTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1LoanVipRepayResponse` | `binance_public_spot_api/models/sapi_v1_loan_vip_repay_response.py` |
| `VipLoanRepayTradeErrorBody` | `binance_public_spot_api/errors/vip_loan_repay_trade_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

