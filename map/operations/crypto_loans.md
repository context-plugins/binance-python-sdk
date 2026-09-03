<!-- Generated file — do not edit; regenerated with the SDK. -->

# CryptoLoans — operations

Accessor: `client.crypto_loans` · Source: `binance_public_spot_api/apis/crypto_loans.py` · 21 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.crypto_loans.adjust_ltv_flexible_loan_adjust_ltv_trade

- **Route**: `POST /sapi/v2/loan/flexible/adjust/ltv`
- **Auth**: `api_key_auth`
- **Signature**: `def adjust_ltv_flexible_loan_adjust_ltv_trade(adjustment_amount: float, direction: DirectionOrStr, timestamp: int, signature: str, *, loan_coin: str | None = None, collateral_coin: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `adjustment_amount`, `direction`, `timestamp`, `signature`
- **Params**: `adjustment_amount` — query `adjustmentAmount` · `direction` — query · `timestamp` — query · `signature` — query · `loan_coin` — query `loanCoin` · `collateral_coin` — query `collateralCoin` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV2LoanFlexibleAdjustLtvResponse`
- **Returns (raw)**: `ApiResult[SapiV2LoanFlexibleAdjustLtvResponse, AdjustLtvFlexibleLoanAdjustLtvTradeErrorBody]`
- **Error**: `AdjustLtvFlexibleLoanAdjustLtvTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `binance_public_spot_api/models/enums/direction.py` |
| `SapiV2LoanFlexibleAdjustLtvResponse` | `binance_public_spot_api/models/sapi_v2_loan_flexible_adjust_ltv_response.py` |
| `AdjustLtvFlexibleLoanAdjustLtvTradeErrorBody` | `binance_public_spot_api/errors/adjust_ltv_flexible_loan_adjust_ltv_trade_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.crypto_loans.adjust_ltv_get_flexible_loan_ltv_adjustment_history_user_data

- **Route**: `GET /sapi/v2/loan/flexible/ltv/adjustment/history`
- **Auth**: `api_key_auth`
- **Signature**: `def adjust_ltv_get_flexible_loan_ltv_adjustment_history_user_data(timestamp: int, signature: str, *, loan_coin: str | None = None, collateral_coin: str | None = None, start_time: int | None = None, end_time: int | None = None, current: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `loan_coin` — query `loanCoin` · `collateral_coin` — query `collateralCoin` · `start_time` — query `startTime` · `end_time` — query `endTime` · `current` — query · `limit` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV2LoanFlexibleLtvAdjustmentHistoryResponse`
- **Returns (raw)**: `ApiResult[SapiV2LoanFlexibleLtvAdjustmentHistoryResponse, AdjustLtvGetFlexibleLoanLtvAdjustmentHistoryUserDataErrorBody]`
- **Error**: `AdjustLtvGetFlexibleLoanLtvAdjustmentHistoryUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV2LoanFlexibleLtvAdjustmentHistoryResponse` | `binance_public_spot_api/models/sapi_v2_loan_flexible_ltv_adjustment_history_response.py` |
| `AdjustLtvGetFlexibleLoanLtvAdjustmentHistoryUserDataErrorBody` | `binance_public_spot_api/errors/adjust_ltv_get_flexible_loan_ltv_adjustment_history_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.crypto_loans.borrow_flexible_loan_borrow_trade

- **Route**: `POST /sapi/v2/loan/flexible/borrow`
- **Auth**: `api_key_auth`
- **Signature**: `def borrow_flexible_loan_borrow_trade(timestamp: int, signature: str, *, loan_coin: str | None = None, loan_amount: float | None = None, collateral_coin: str | None = None, collateral_amount: float | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `loan_coin` — query `loanCoin` · `loan_amount` — query `loanAmount` · `collateral_coin` — query `collateralCoin` · `collateral_amount` — query `collateralAmount` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV2LoanFlexibleBorrowResponse`
- **Returns (raw)**: `ApiResult[SapiV2LoanFlexibleBorrowResponse, BorrowFlexibleLoanBorrowTradeErrorBody]`
- **Error**: `BorrowFlexibleLoanBorrowTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV2LoanFlexibleBorrowResponse` | `binance_public_spot_api/models/sapi_v2_loan_flexible_borrow_response.py` |
| `BorrowFlexibleLoanBorrowTradeErrorBody` | `binance_public_spot_api/errors/borrow_flexible_loan_borrow_trade_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.crypto_loans.borrow_get_flexible_loan_borrow_history_user_data

- **Route**: `GET /sapi/v2/loan/flexible/borrow/history`
- **Auth**: `api_key_auth`
- **Signature**: `def borrow_get_flexible_loan_borrow_history_user_data(timestamp: int, signature: str, *, loan_coin: str | None = None, collateral_coin: str | None = None, start_time: int | None = None, end_time: int | None = None, current: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `loan_coin` — query `loanCoin` · `collateral_coin` — query `collateralCoin` · `start_time` — query `startTime` · `end_time` — query `endTime` · `current` — query · `limit` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV2LoanFlexibleBorrowHistoryResponse`
- **Returns (raw)**: `ApiResult[SapiV2LoanFlexibleBorrowHistoryResponse, BorrowGetFlexibleLoanBorrowHistoryUserDataErrorBody]`
- **Error**: `BorrowGetFlexibleLoanBorrowHistoryUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV2LoanFlexibleBorrowHistoryResponse` | `binance_public_spot_api/models/sapi_v2_loan_flexible_borrow_history_response.py` |
| `BorrowGetFlexibleLoanBorrowHistoryUserDataErrorBody` | `binance_public_spot_api/errors/borrow_get_flexible_loan_borrow_history_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.crypto_loans.borrow_get_flexible_loan_ongoing_orders_user_data

- **Route**: `GET /sapi/v2/loan/flexible/ongoing/orders`
- **Auth**: `api_key_auth`
- **Signature**: `def borrow_get_flexible_loan_ongoing_orders_user_data(timestamp: int, signature: str, *, loan_coin: str | None = None, collateral_coin: str | None = None, current: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `loan_coin` — query `loanCoin` · `collateral_coin` — query `collateralCoin` · `current` — query · `limit` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV2LoanFlexibleOngoingOrdersResponse`
- **Returns (raw)**: `ApiResult[SapiV2LoanFlexibleOngoingOrdersResponse, BorrowGetFlexibleLoanOngoingOrdersUserDataErrorBody]`
- **Error**: `BorrowGetFlexibleLoanOngoingOrdersUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV2LoanFlexibleOngoingOrdersResponse` | `binance_public_spot_api/models/sapi_v2_loan_flexible_ongoing_orders_response.py` |
| `BorrowGetFlexibleLoanOngoingOrdersUserDataErrorBody` | `binance_public_spot_api/errors/borrow_get_flexible_loan_ongoing_orders_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.crypto_loans.check_collateral_repay_rate_user_data

- **Route**: `GET /sapi/v1/loan/repay/collateral/rate`
- **Auth**: `api_key_auth`
- **Signature**: `def check_collateral_repay_rate_user_data(loan_coin: str, collateral_coin: str, repay_amount: float, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `loan_coin`, `collateral_coin`, `repay_amount`, `timestamp`, `signature`
- **Params**: `loan_coin` — query `loanCoin` · `collateral_coin` — query `collateralCoin` · `repay_amount` — query `repayAmount` · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1LoanRepayCollateralRateResponse`
- **Returns (raw)**: `ApiResult[SapiV1LoanRepayCollateralRateResponse, CheckCollateralRepayRateUserDataErrorBody]`
- **Error**: `CheckCollateralRepayRateUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1LoanRepayCollateralRateResponse` | `binance_public_spot_api/models/sapi_v1_loan_repay_collateral_rate_response.py` |
| `CheckCollateralRepayRateUserDataErrorBody` | `binance_public_spot_api/errors/check_collateral_repay_rate_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.crypto_loans.crypto_loan_adjust_ltv_trade

- **Route**: `POST /sapi/v1/loan/adjust/ltv`
- **Auth**: `api_key_auth`
- **Signature**: `def crypto_loan_adjust_ltv_trade(order_id: int, amount: float, direction: DirectionOrStr, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `order_id`, `amount`, `direction`, `timestamp`, `signature`
- **Params**: `order_id` — query `orderId` · `amount` — query · `direction` — query · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1LoanAdjustLtvResponse`
- **Returns (raw)**: `ApiResult[SapiV1LoanAdjustLtvResponse, CryptoLoanAdjustLtvTradeErrorBody]`
- **Error**: `CryptoLoanAdjustLtvTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `binance_public_spot_api/models/enums/direction.py` |
| `SapiV1LoanAdjustLtvResponse` | `binance_public_spot_api/models/sapi_v1_loan_adjust_ltv_response.py` |
| `CryptoLoanAdjustLtvTradeErrorBody` | `binance_public_spot_api/errors/crypto_loan_adjust_ltv_trade_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.crypto_loans.crypto_loan_borrow_trade

- **Route**: `POST /sapi/v1/loan/borrow`
- **Auth**: `api_key_auth`
- **Signature**: `def crypto_loan_borrow_trade(loan_coin: str, collateral_coin: str, loan_term: int, timestamp: int, signature: str, *, loan_amount: float | None = None, collateral_amount: float | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `loan_coin`, `collateral_coin`, `loan_term`, `timestamp`, `signature`
- **Params**: `loan_coin` — query `loanCoin` · `collateral_coin` — query `collateralCoin` · `loan_term` — query `loanTerm` · `timestamp` — query · `signature` — query · `loan_amount` — query `loanAmount` · `collateral_amount` — query `collateralAmount` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1LoanBorrowResponse`
- **Returns (raw)**: `ApiResult[SapiV1LoanBorrowResponse, CryptoLoanBorrowTradeErrorBody]`
- **Error**: `CryptoLoanBorrowTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1LoanBorrowResponse` | `binance_public_spot_api/models/sapi_v1_loan_borrow_response.py` |
| `CryptoLoanBorrowTradeErrorBody` | `binance_public_spot_api/errors/crypto_loan_borrow_trade_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.crypto_loans.crypto_loan_customize_margin_call_trade

- **Route**: `POST /sapi/v1/loan/customize/margin_call`
- **Auth**: `api_key_auth`
- **Signature**: `def crypto_loan_customize_margin_call_trade(margin_call: float, timestamp: int, signature: str, *, order_id: int | None = None, collateral_coin: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `margin_call`, `timestamp`, `signature`
- **Params**: `margin_call` — query `marginCall` · `timestamp` — query · `signature` — query · `order_id` — query `orderId` · `collateral_coin` — query `collateralCoin` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1LoanCustomizeMarginCallResponse`
- **Returns (raw)**: `ApiResult[SapiV1LoanCustomizeMarginCallResponse, CryptoLoanCustomizeMarginCallTradeErrorBody]`
- **Error**: `CryptoLoanCustomizeMarginCallTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1LoanCustomizeMarginCallResponse` | `binance_public_spot_api/models/sapi_v1_loan_customize_margin_call_response.py` |
| `CryptoLoanCustomizeMarginCallTradeErrorBody` | `binance_public_spot_api/errors/crypto_loan_customize_margin_call_trade_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.crypto_loans.crypto_loan_repay_trade

- **Route**: `POST /sapi/v1/loan/repay`
- **Auth**: `api_key_auth`
- **Signature**: `def crypto_loan_repay_trade(order_id: int, amount: float, timestamp: int, signature: str, *, type_: int | None = None, collateral_return: bool | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `order_id`, `amount`, `timestamp`, `signature`
- **Params**: `order_id` — query `orderId` · `amount` — query · `timestamp` — query · `signature` — query · `type_` — query `type` · `collateral_return` — query `collateralReturn` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1LoanRepayResponse`
- **Returns (raw)**: `ApiResult[SapiV1LoanRepayResponse, CryptoLoanRepayTradeErrorBody]`
- **Error**: `CryptoLoanRepayTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1LoanRepayResponse` | `binance_public_spot_api/models/unions/sapi_v1_loan_repay_response.py` |
| `CryptoLoanRepayTradeErrorBody` | `binance_public_spot_api/errors/crypto_loan_repay_trade_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.crypto_loans.get_collateral_assets_data_user_data

- **Route**: `GET /sapi/v1/loan/collateral/data`
- **Auth**: `api_key_auth`
- **Signature**: `def get_collateral_assets_data_user_data(timestamp: int, signature: str, *, collateral_coin: str | None = None, vip_level: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `collateral_coin` — query `collateralCoin` · `vip_level` — query `vipLevel` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1LoanCollateralDataResponse`
- **Returns (raw)**: `ApiResult[SapiV1LoanCollateralDataResponse, GetCollateralAssetsDataUserDataErrorBody]`
- **Error**: `GetCollateralAssetsDataUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1LoanCollateralDataResponse` | `binance_public_spot_api/models/sapi_v1_loan_collateral_data_response.py` |
| `GetCollateralAssetsDataUserDataErrorBody` | `binance_public_spot_api/errors/get_collateral_assets_data_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.crypto_loans.get_crypto_loans_borrow_history_user_data

- **Route**: `GET /sapi/v1/loan/borrow/history`
- **Auth**: `api_key_auth`
- **Signature**: `def get_crypto_loans_borrow_history_user_data(timestamp: int, signature: str, *, order_id: int | None = None, loan_coin: str | None = None, collateral_coin: str | None = None, start_time: int | None = None, end_time: int | None = None, current: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `order_id` — query `orderId` · `loan_coin` — query `loanCoin` · `collateral_coin` — query `collateralCoin` · `start_time` — query `startTime` · `end_time` — query `endTime` · `current` — query · `limit` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1LoanBorrowHistoryResponse`
- **Returns (raw)**: `ApiResult[SapiV1LoanBorrowHistoryResponse, GetCryptoLoansBorrowHistoryUserDataErrorBody]`
- **Error**: `GetCryptoLoansBorrowHistoryUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1LoanBorrowHistoryResponse` | `binance_public_spot_api/models/sapi_v1_loan_borrow_history_response.py` |
| `GetCryptoLoansBorrowHistoryUserDataErrorBody` | `binance_public_spot_api/errors/get_crypto_loans_borrow_history_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.crypto_loans.get_crypto_loans_income_history_user_data

- **Route**: `GET /sapi/v1/loan/income`
- **Auth**: `api_key_auth`
- **Signature**: `def get_crypto_loans_income_history_user_data(timestamp: int, signature: str, *, asset: str | None = None, type_: Type9OrStr | None = None, start_time: int | None = None, end_time: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `asset` — query · `type_` — query `type` · `start_time` — query `startTime` · `end_time` — query `endTime` · `limit` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1LoanIncomeResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1LoanIncomeResponse], GetCryptoLoansIncomeHistoryUserDataErrorBody]`
- **Error**: `GetCryptoLoansIncomeHistoryUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Type9OrStr` | `binance_public_spot_api/models/enums/type9.py` |
| `SapiV1LoanIncomeResponse` | `binance_public_spot_api/models/sapi_v1_loan_income_response.py` |
| `GetCryptoLoansIncomeHistoryUserDataErrorBody` | `binance_public_spot_api/errors/get_crypto_loans_income_history_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.crypto_loans.get_flexible_loan_assets_data_user_data

- **Route**: `GET /sapi/v2/loan/flexible/loanable/data`
- **Auth**: `api_key_auth`
- **Signature**: `def get_flexible_loan_assets_data_user_data(timestamp: int, signature: str, *, loan_coin: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `loan_coin` — query `loanCoin` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV2LoanFlexibleLoanableDataResponse`
- **Returns (raw)**: `ApiResult[SapiV2LoanFlexibleLoanableDataResponse, GetFlexibleLoanAssetsDataUserDataErrorBody]`
- **Error**: `GetFlexibleLoanAssetsDataUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV2LoanFlexibleLoanableDataResponse` | `binance_public_spot_api/models/sapi_v2_loan_flexible_loanable_data_response.py` |
| `GetFlexibleLoanAssetsDataUserDataErrorBody` | `binance_public_spot_api/errors/get_flexible_loan_assets_data_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.crypto_loans.get_flexible_loan_collateral_assets_data_user_data

- **Route**: `GET /sapi/v2/loan/flexible/collateral/data`
- **Auth**: `api_key_auth`
- **Signature**: `def get_flexible_loan_collateral_assets_data_user_data(timestamp: int, signature: str, *, collateral_coin: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `collateral_coin` — query `collateralCoin` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV2LoanFlexibleCollateralDataResponse`
- **Returns (raw)**: `ApiResult[SapiV2LoanFlexibleCollateralDataResponse, GetFlexibleLoanCollateralAssetsDataUserDataErrorBody]`
- **Error**: `GetFlexibleLoanCollateralAssetsDataUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV2LoanFlexibleCollateralDataResponse` | `binance_public_spot_api/models/sapi_v2_loan_flexible_collateral_data_response.py` |
| `GetFlexibleLoanCollateralAssetsDataUserDataErrorBody` | `binance_public_spot_api/errors/get_flexible_loan_collateral_assets_data_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.crypto_loans.get_loan_ltv_adjustment_history_user_data

- **Route**: `GET /sapi/v1/loan/ltv/adjustment/history`
- **Auth**: `api_key_auth`
- **Signature**: `def get_loan_ltv_adjustment_history_user_data(timestamp: int, signature: str, *, order_id: int | None = None, loan_coin: str | None = None, collateral_coin: str | None = None, start_time: int | None = None, end_time: int | None = None, current: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `order_id` — query `orderId` · `loan_coin` — query `loanCoin` · `collateral_coin` — query `collateralCoin` · `start_time` — query `startTime` · `end_time` — query `endTime` · `current` — query · `limit` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1LoanLtvAdjustmentHistoryResponse`
- **Returns (raw)**: `ApiResult[SapiV1LoanLtvAdjustmentHistoryResponse, GetLoanLtvAdjustmentHistoryUserDataErrorBody]`
- **Error**: `GetLoanLtvAdjustmentHistoryUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1LoanLtvAdjustmentHistoryResponse` | `binance_public_spot_api/models/sapi_v1_loan_ltv_adjustment_history_response.py` |
| `GetLoanLtvAdjustmentHistoryUserDataErrorBody` | `binance_public_spot_api/errors/get_loan_ltv_adjustment_history_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.crypto_loans.get_loan_ongoing_orders_user_data

- **Route**: `GET /sapi/v1/loan/ongoing/orders`
- **Auth**: `api_key_auth`
- **Signature**: `def get_loan_ongoing_orders_user_data(timestamp: int, signature: str, *, order_id: int | None = None, loan_coin: str | None = None, collateral_coin: str | None = None, current: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `order_id` — query `orderId` · `loan_coin` — query `loanCoin` · `collateral_coin` — query `collateralCoin` · `current` — query · `limit` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1LoanOngoingOrdersResponse`
- **Returns (raw)**: `ApiResult[SapiV1LoanOngoingOrdersResponse, GetLoanOngoingOrdersUserDataErrorBody]`
- **Error**: `GetLoanOngoingOrdersUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1LoanOngoingOrdersResponse` | `binance_public_spot_api/models/sapi_v1_loan_ongoing_orders_response.py` |
| `GetLoanOngoingOrdersUserDataErrorBody` | `binance_public_spot_api/errors/get_loan_ongoing_orders_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.crypto_loans.get_loan_repayment_history_user_data

- **Route**: `GET /sapi/v1/loan/repay/history`
- **Auth**: `api_key_auth`
- **Signature**: `def get_loan_repayment_history_user_data(timestamp: int, signature: str, *, order_id: int | None = None, loan_coin: str | None = None, collateral_coin: str | None = None, start_time: int | None = None, end_time: int | None = None, current: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `order_id` — query `orderId` · `loan_coin` — query `loanCoin` · `collateral_coin` — query `collateralCoin` · `start_time` — query `startTime` · `end_time` — query `endTime` · `current` — query · `limit` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1LoanRepayHistoryResponse`
- **Returns (raw)**: `ApiResult[SapiV1LoanRepayHistoryResponse, GetLoanRepaymentHistoryUserDataErrorBody]`
- **Error**: `GetLoanRepaymentHistoryUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1LoanRepayHistoryResponse` | `binance_public_spot_api/models/sapi_v1_loan_repay_history_response.py` |
| `GetLoanRepaymentHistoryUserDataErrorBody` | `binance_public_spot_api/errors/get_loan_repayment_history_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.crypto_loans.get_loanable_assets_data_user_data

- **Route**: `GET /sapi/v1/loan/loanable/data`
- **Auth**: `api_key_auth`
- **Signature**: `def get_loanable_assets_data_user_data(timestamp: int, signature: str, *, loan_coin: str | None = None, vip_level: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `loan_coin` — query `loanCoin` · `vip_level` — query `vipLevel` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1LoanLoanableDataResponse`
- **Returns (raw)**: `ApiResult[SapiV1LoanLoanableDataResponse, GetLoanableAssetsDataUserDataErrorBody]`
- **Error**: `GetLoanableAssetsDataUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1LoanLoanableDataResponse` | `binance_public_spot_api/models/sapi_v1_loan_loanable_data_response.py` |
| `GetLoanableAssetsDataUserDataErrorBody` | `binance_public_spot_api/errors/get_loanable_assets_data_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.crypto_loans.repay_flexible_loan_repay_trade

- **Route**: `POST /sapi/v2/loan/flexible/repay`
- **Auth**: `api_key_auth`
- **Signature**: `def repay_flexible_loan_repay_trade(repay_amount: float, timestamp: int, signature: str, *, loan_coin: str | None = None, collateral_coin: str | None = None, collateral_return: bool | None = None, full_repayment: bool | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `repay_amount`, `timestamp`, `signature`
- **Params**: `repay_amount` — query `repayAmount` · `timestamp` — query · `signature` — query · `loan_coin` — query `loanCoin` · `collateral_coin` — query `collateralCoin` · `collateral_return` — query `collateralReturn` · `full_repayment` — query `fullRepayment` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV2LoanFlexibleRepayResponse`
- **Returns (raw)**: `ApiResult[SapiV2LoanFlexibleRepayResponse, RepayFlexibleLoanRepayTradeErrorBody]`
- **Error**: `RepayFlexibleLoanRepayTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV2LoanFlexibleRepayResponse` | `binance_public_spot_api/models/sapi_v2_loan_flexible_repay_response.py` |
| `RepayFlexibleLoanRepayTradeErrorBody` | `binance_public_spot_api/errors/repay_flexible_loan_repay_trade_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.crypto_loans.repay_get_flexible_loan_repayment_history_user_data

- **Route**: `GET /sapi/v2/loan/flexible/repay/history`
- **Auth**: `api_key_auth`
- **Signature**: `def repay_get_flexible_loan_repayment_history_user_data(timestamp: int, signature: str, *, loan_coin: str | None = None, collateral_coin: str | None = None, start_time: int | None = None, end_time: int | None = None, current: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `loan_coin` — query `loanCoin` · `collateral_coin` — query `collateralCoin` · `start_time` — query `startTime` · `end_time` — query `endTime` · `current` — query · `limit` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV2LoanFlexibleRepayHistoryResponse`
- **Returns (raw)**: `ApiResult[SapiV2LoanFlexibleRepayHistoryResponse, RepayGetFlexibleLoanRepaymentHistoryUserDataErrorBody]`
- **Error**: `RepayGetFlexibleLoanRepaymentHistoryUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV2LoanFlexibleRepayHistoryResponse` | `binance_public_spot_api/models/sapi_v2_loan_flexible_repay_history_response.py` |
| `RepayGetFlexibleLoanRepaymentHistoryUserDataErrorBody` | `binance_public_spot_api/errors/repay_get_flexible_loan_repayment_history_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

