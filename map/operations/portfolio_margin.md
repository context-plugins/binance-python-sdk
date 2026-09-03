<!-- Generated file — do not edit; regenerated with the SDK. -->

# PortfolioMargin — operations

Accessor: `client.portfolio_margin` · Source: `binance_public_spot_api/apis/portfolio_margin.py` · 14 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.portfolio_margin.bnb_transfer_user_data

- **Route**: `POST /sapi/v1/portfolio/bnb-transfer`
- **Auth**: `api_key_auth`
- **Signature**: `def bnb_transfer_user_data(transfer_side: TransferSideOrStr, amount: float, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `transfer_side`, `amount`, `timestamp`, `signature`
- **Params**: `transfer_side` — query `transferSide` · `amount` — query · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1PortfolioBnbTransferResponse`
- **Returns (raw)**: `ApiResult[SapiV1PortfolioBnbTransferResponse, BnbTransferUserDataErrorBody]`
- **Error**: `BnbTransferUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TransferSideOrStr` | `binance_public_spot_api/models/enums/transfer_side.py` |
| `SapiV1PortfolioBnbTransferResponse` | `binance_public_spot_api/models/sapi_v1_portfolio_bnb_transfer_response.py` |
| `BnbTransferUserDataErrorBody` | `binance_public_spot_api/errors/bnb_transfer_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.portfolio_margin.change_auto_repay_futures_status_user_data

- **Route**: `POST /sapi/v1/portfolio/repay-futures-switch`
- **Auth**: `api_key_auth`
- **Signature**: `def change_auto_repay_futures_status_user_data(auto_repay: bool, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `auto_repay`, `timestamp`, `signature`
- **Params**: `auto_repay` — query `autoRepay` · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1PortfolioRepayFuturesSwitchResponse`
- **Returns (raw)**: `ApiResult[SapiV1PortfolioRepayFuturesSwitchResponse, ChangeAutoRepayFuturesStatusUserDataErrorBody]`
- **Error**: `ChangeAutoRepayFuturesStatusUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1PortfolioRepayFuturesSwitchResponse` | `binance_public_spot_api/models/sapi_v1_portfolio_repay_futures_switch_response.py` |
| `ChangeAutoRepayFuturesStatusUserDataErrorBody` | `binance_public_spot_api/errors/change_auto_repay_futures_status_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.portfolio_margin.fund_auto_collection_user_data

- **Route**: `POST /sapi/v1/portfolio/auto-collection`
- **Auth**: `api_key_auth`
- **Signature**: `def fund_auto_collection_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1PortfolioAutoCollectionResponse`
- **Returns (raw)**: `ApiResult[SapiV1PortfolioAutoCollectionResponse, FundAutoCollectionUserDataErrorBody]`
- **Error**: `FundAutoCollectionUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1PortfolioAutoCollectionResponse` | `binance_public_spot_api/models/sapi_v1_portfolio_auto_collection_response.py` |
| `FundAutoCollectionUserDataErrorBody` | `binance_public_spot_api/errors/fund_auto_collection_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.portfolio_margin.fund_collection_by_asset_user_data

- **Route**: `POST /sapi/v1/portfolio/asset-collection`
- **Auth**: `api_key_auth`
- **Signature**: `def fund_collection_by_asset_user_data(asset: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `asset`, `timestamp`, `signature`
- **Params**: `asset` — query · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1PortfolioAssetCollectionResponse`
- **Returns (raw)**: `ApiResult[SapiV1PortfolioAssetCollectionResponse, FundCollectionByAssetUserDataErrorBody]`
- **Error**: `FundCollectionByAssetUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1PortfolioAssetCollectionResponse` | `binance_public_spot_api/models/sapi_v1_portfolio_asset_collection_response.py` |
| `FundCollectionByAssetUserDataErrorBody` | `binance_public_spot_api/errors/fund_collection_by_asset_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.portfolio_margin.get_auto_repay_futures_status_user_data

- **Route**: `GET /sapi/v1/portfolio/repay-futures-switch`
- **Auth**: `api_key_auth`
- **Signature**: `def get_auto_repay_futures_status_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1PortfolioRepayFuturesSwitchResponse1`
- **Returns (raw)**: `ApiResult[SapiV1PortfolioRepayFuturesSwitchResponse1, GetAutoRepayFuturesStatusUserDataErrorBody]`
- **Error**: `GetAutoRepayFuturesStatusUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1PortfolioRepayFuturesSwitchResponse1` | `binance_public_spot_api/models/sapi_v1_portfolio_repay_futures_switch_response1.py` |
| `GetAutoRepayFuturesStatusUserDataErrorBody` | `binance_public_spot_api/errors/get_auto_repay_futures_status_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.portfolio_margin.get_portfolio_margin_asset_leverage_user_data

- **Route**: `GET /sapi/v1/portfolio/margin-asset-leverage`
- **Signature**: `def get_portfolio_margin_asset_leverage_user_data(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `list[SapiV1PortfolioMarginAssetLeverageResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1PortfolioMarginAssetLeverageResponse], GetPortfolioMarginAssetLeverageUserDataErrorBody]`
- **Error**: `GetPortfolioMarginAssetLeverageUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1PortfolioMarginAssetLeverageResponse` | `binance_public_spot_api/models/sapi_v1_portfolio_margin_asset_leverage_response.py` |
| `GetPortfolioMarginAssetLeverageUserDataErrorBody` | `binance_public_spot_api/errors/get_portfolio_margin_asset_leverage_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.portfolio_margin.portfolio_margin_account_user_data

- **Route**: `GET /sapi/v1/portfolio/account`
- **Auth**: `api_key_auth`
- **Signature**: `def portfolio_margin_account_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1PortfolioAccountResponse`
- **Returns (raw)**: `ApiResult[SapiV1PortfolioAccountResponse, PortfolioMarginAccountUserDataErrorBody]`
- **Error**: `PortfolioMarginAccountUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1PortfolioAccountResponse` | `binance_public_spot_api/models/sapi_v1_portfolio_account_response.py` |
| `PortfolioMarginAccountUserDataErrorBody` | `binance_public_spot_api/errors/portfolio_margin_account_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.portfolio_margin.portfolio_margin_bankruptcy_loan_amount_user_data

- **Route**: `GET /sapi/v1/portfolio/pmLoan`
- **Auth**: `api_key_auth`
- **Signature**: `def portfolio_margin_bankruptcy_loan_amount_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1PortfolioPmLoanResponse`
- **Returns (raw)**: `ApiResult[SapiV1PortfolioPmLoanResponse, PortfolioMarginBankruptcyLoanAmountUserDataErrorBody]`
- **Error**: `PortfolioMarginBankruptcyLoanAmountUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1PortfolioPmLoanResponse` | `binance_public_spot_api/models/sapi_v1_portfolio_pm_loan_response.py` |
| `PortfolioMarginBankruptcyLoanAmountUserDataErrorBody` | `binance_public_spot_api/errors/portfolio_margin_bankruptcy_loan_amount_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.portfolio_margin.portfolio_margin_bankruptcy_loan_repay_user_data

- **Route**: `POST /sapi/v1/portfolio/repay`
- **Auth**: `api_key_auth`
- **Signature**: `def portfolio_margin_bankruptcy_loan_repay_user_data(timestamp: int, signature: str, *, from_: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `from_` — query `from` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1PortfolioRepayResponse`
- **Returns (raw)**: `ApiResult[SapiV1PortfolioRepayResponse, PortfolioMarginBankruptcyLoanRepayUserDataErrorBody]`
- **Error**: `PortfolioMarginBankruptcyLoanRepayUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1PortfolioRepayResponse` | `binance_public_spot_api/models/sapi_v1_portfolio_repay_response.py` |
| `PortfolioMarginBankruptcyLoanRepayUserDataErrorBody` | `binance_public_spot_api/errors/portfolio_margin_bankruptcy_loan_repay_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.portfolio_margin.portfolio_margin_collateral_rate_market_data

- **Route**: `GET /sapi/v1/portfolio/collateralRate`
- **Auth**: `api_key_auth`
- **Signature**: `def portfolio_margin_collateral_rate_market_data(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `list[SapiV1PortfolioCollateralRateResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1PortfolioCollateralRateResponse], PortfolioMarginCollateralRateMarketDataErrorBody]`
- **Error**: `PortfolioMarginCollateralRateMarketDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1PortfolioCollateralRateResponse` | `binance_public_spot_api/models/sapi_v1_portfolio_collateral_rate_response.py` |
| `PortfolioMarginCollateralRateMarketDataErrorBody` | `binance_public_spot_api/errors/portfolio_margin_collateral_rate_market_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.portfolio_margin.portfolio_margin_pro_tiered_collateral_rate_user_data

- **Route**: `GET /sapi/v2/portfolio/collateralRate`
- **Auth**: `api_key_auth`
- **Signature**: `def portfolio_margin_pro_tiered_collateral_rate_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV2PortfolioCollateralRateResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV2PortfolioCollateralRateResponse], PortfolioMarginProTieredCollateralRateUserDataErrorBody]`
- **Error**: `PortfolioMarginProTieredCollateralRateUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV2PortfolioCollateralRateResponse` | `binance_public_spot_api/models/sapi_v2_portfolio_collateral_rate_response.py` |
| `PortfolioMarginProTieredCollateralRateUserDataErrorBody` | `binance_public_spot_api/errors/portfolio_margin_pro_tiered_collateral_rate_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.portfolio_margin.query_classic_portfolio_margin_negative_balance_interest_history_user_data

- **Route**: `GET /sapi/v1/portfolio/interest-history`
- **Auth**: `api_key_auth`
- **Signature**: `def query_classic_portfolio_margin_negative_balance_interest_history_user_data(asset: str, timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `asset`, `timestamp`, `signature`
- **Params**: `asset` — query · `timestamp` — query · `signature` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `size` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1PortfolioInterestHistoryResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1PortfolioInterestHistoryResponse], QueryClassicPortfolioMarginNegativeBalanceInterestHistoryUserDataErrorBody]`
- **Error**: `QueryClassicPortfolioMarginNegativeBalanceInterestHistoryUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1PortfolioInterestHistoryResponse` | `binance_public_spot_api/models/sapi_v1_portfolio_interest_history_response.py` |
| `QueryClassicPortfolioMarginNegativeBalanceInterestHistoryUserDataErrorBody` | `binance_public_spot_api/errors/query_classic_portfolio_margin_negative_balance_interest_history_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.portfolio_margin.query_portfolio_margin_asset_index_price_market_data

- **Route**: `GET /sapi/v1/portfolio/asset-index-price`
- **Auth**: `api_key_auth`
- **Signature**: `def query_portfolio_margin_asset_index_price_market_data(*, asset: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `asset` — query
- **Returns (parsed)**: `list[SapiV1PortfolioAssetIndexPriceResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1PortfolioAssetIndexPriceResponse], QueryPortfolioMarginAssetIndexPriceMarketDataErrorBody]`
- **Error**: `QueryPortfolioMarginAssetIndexPriceMarketDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1PortfolioAssetIndexPriceResponse` | `binance_public_spot_api/models/sapi_v1_portfolio_asset_index_price_response.py` |
| `QueryPortfolioMarginAssetIndexPriceMarketDataErrorBody` | `binance_public_spot_api/errors/query_portfolio_margin_asset_index_price_market_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.portfolio_margin.repay_futures_negative_balance_user_data

- **Route**: `POST /sapi/v1/portfolio/repay-futures-negative-balance`
- **Auth**: `api_key_auth`
- **Signature**: `def repay_futures_negative_balance_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1PortfolioRepayFuturesNegativeBalanceResponse`
- **Returns (raw)**: `ApiResult[SapiV1PortfolioRepayFuturesNegativeBalanceResponse, RepayFuturesNegativeBalanceUserDataErrorBody]`
- **Error**: `RepayFuturesNegativeBalanceUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1PortfolioRepayFuturesNegativeBalanceResponse` | `binance_public_spot_api/models/sapi_v1_portfolio_repay_futures_negative_balance_response.py` |
| `RepayFuturesNegativeBalanceUserDataErrorBody` | `binance_public_spot_api/errors/repay_futures_negative_balance_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

