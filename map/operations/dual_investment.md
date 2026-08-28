<!-- Generated file — do not edit; regenerated with the SDK. -->

# DualInvestment — operations

Accessor: `client.dual_investment` · Source: `binance/apis/dual_investment.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.dual_investment.change_auto_compound_status_user_data

- **Route**: `POST /sapi/v1/dci/product/auto_compound/edit-status`
- **Signature**: `def change_auto_compound_status_user_data(position_id: int, auto_compound_plan: AutoCompoundPlanOrStr, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `position_id`, `auto_compound_plan`, `timestamp`, `signature`
- **Params**: `position_id` — query `positionId` · `auto_compound_plan` — query `autoCompoundPlan` · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1DciProductAutoCompoundEditStatusResponse`
- **Returns (raw)**: `ApiResult[SapiV1DciProductAutoCompoundEditStatusResponse, ChangeAutoCompoundStatusUserDataErrorBody]`
- **Error**: `ChangeAutoCompoundStatusUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AutoCompoundPlanOrStr` | `binance/models/enums/auto_compound_plan.py` |
| `SapiV1DciProductAutoCompoundEditStatusResponse` | `binance/models/sapi_v1_dci_product_auto_compound_edit_status_response.py` |
| `ChangeAutoCompoundStatusUserDataErrorBody` | `binance/errors/change_auto_compound_status_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.dual_investment.check_dual_investment_accounts_user_data

- **Route**: `GET /sapi/v1/dci/product/accounts`
- **Signature**: `def check_dual_investment_accounts_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1DciProductAccountsResponse`
- **Returns (raw)**: `ApiResult[SapiV1DciProductAccountsResponse, CheckDualInvestmentAccountsUserDataErrorBody]`
- **Error**: `CheckDualInvestmentAccountsUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1DciProductAccountsResponse` | `binance/models/sapi_v1_dci_product_accounts_response.py` |
| `CheckDualInvestmentAccountsUserDataErrorBody` | `binance/errors/check_dual_investment_accounts_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.dual_investment.get_dual_investment_positions_user_data

- **Route**: `GET /sapi/v1/dci/product/positions`
- **Signature**: `def get_dual_investment_positions_user_data(timestamp: int, signature: str, *, status: Status2OrStr | None = None, page_size: str | None = None, page_index: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `status` — query · `page_size` — query `pageSize` · `page_index` — query `pageIndex` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1DciProductPositionsResponse`
- **Returns (raw)**: `ApiResult[SapiV1DciProductPositionsResponse, GetDualInvestmentPositionsUserDataErrorBody]`
- **Error**: `GetDualInvestmentPositionsUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Status2OrStr` | `binance/models/enums/status2.py` |
| `SapiV1DciProductPositionsResponse` | `binance/models/sapi_v1_dci_product_positions_response.py` |
| `GetDualInvestmentPositionsUserDataErrorBody` | `binance/errors/get_dual_investment_positions_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.dual_investment.get_dual_investment_product_list_user_data

- **Route**: `GET /sapi/v1/dci/product/list`
- **Signature**: `def get_dual_investment_product_list_user_data(option_type: OptionTypeOrStr, exercised_coin: str, invest_coin: str, timestamp: int, signature: str, *, page_size: str | None = None, page_index: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `option_type`, `exercised_coin`, `invest_coin`, `timestamp`, `signature`
- **Params**: `option_type` — query `optionType` · `exercised_coin` — query `exercisedCoin` · `invest_coin` — query `investCoin` · `timestamp` — query · `signature` — query · `page_size` — query `pageSize` · `page_index` — query `pageIndex` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1DciProductListResponse`
- **Returns (raw)**: `ApiResult[SapiV1DciProductListResponse, GetDualInvestmentProductListUserDataErrorBody]`
- **Error**: `GetDualInvestmentProductListUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OptionTypeOrStr` | `binance/models/enums/option_type.py` |
| `SapiV1DciProductListResponse` | `binance/models/sapi_v1_dci_product_list_response.py` |
| `GetDualInvestmentProductListUserDataErrorBody` | `binance/errors/get_dual_investment_product_list_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.dual_investment.subscribe_dual_investment_products_user_data

- **Route**: `POST /sapi/v1/dci/product/subscribe`
- **Signature**: `def subscribe_dual_investment_products_user_data(id: str, order_id: str, deposit_amount: float, auto_compound_plan: AutoCompoundPlanOrStr, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `order_id`, `deposit_amount`, `auto_compound_plan`, `timestamp`, `signature`
- **Params**: `id` — query · `order_id` — query `orderId` · `deposit_amount` — query `depositAmount` · `auto_compound_plan` — query `autoCompoundPlan` · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1DciProductSubscribeResponse`
- **Returns (raw)**: `ApiResult[SapiV1DciProductSubscribeResponse, SubscribeDualInvestmentProductsUserDataErrorBody]`
- **Error**: `SubscribeDualInvestmentProductsUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AutoCompoundPlanOrStr` | `binance/models/enums/auto_compound_plan.py` |
| `SapiV1DciProductSubscribeResponse` | `binance/models/sapi_v1_dci_product_subscribe_response.py` |
| `SubscribeDualInvestmentProductsUserDataErrorBody` | `binance/errors/subscribe_dual_investment_products_user_data_error.py` |
| `Error` | `binance/models/error.py` |

