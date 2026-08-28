<!-- Generated file — do not edit; regenerated with the SDK. -->

# Savings — operations

Accessor: `client.savings` · Source: `binance/apis/savings.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.savings.change_fixed_activity_position_to_daily_position_user_data

- **Route**: `POST /sapi/v1/lending/positionChanged`
- **Signature**: `def change_fixed_activity_position_to_daily_position_user_data(project_id: str, lot: str, timestamp: int, signature: str, *, position_id: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`, `lot`, `timestamp`, `signature`
- **Params**: `project_id` — query `projectId` · `lot` — query · `timestamp` — query · `signature` — query · `position_id` — query `positionId` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1LendingPositionChangedResponse`
- **Returns (raw)**: `ApiResult[SapiV1LendingPositionChangedResponse, ChangeFixedActivityPositionToDailyPositionUserDataErrorBody]`
- **Error**: `ChangeFixedActivityPositionToDailyPositionUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1LendingPositionChangedResponse` | `binance/models/sapi_v1_lending_position_changed_response.py` |
| `ChangeFixedActivityPositionToDailyPositionUserDataErrorBody` | `binance/errors/change_fixed_activity_position_to_daily_position_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.savings.get_fixed_activity_project_list_user_data

- **Route**: `GET /sapi/v1/lending/project/list`
- **Signature**: `def get_fixed_activity_project_list_user_data(type_: Type8OrStr, timestamp: int, signature: str, *, asset: str | None = None, status: StatusOrStr | None = None, is_sort_asc: bool | None = None, sort_by: SortByOrStr | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `type_`, `timestamp`, `signature`
- **Params**: `type_` — query `type` · `timestamp` — query · `signature` — query · `asset` — query · `status` — query · `is_sort_asc` — query `isSortAsc` · `sort_by` — query `sortBy` · `current` — query · `size` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1LendingProjectListResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1LendingProjectListResponse], GetFixedActivityProjectListUserDataErrorBody]`
- **Error**: `GetFixedActivityProjectListUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Type8OrStr` | `binance/models/enums/type8.py` |
| `StatusOrStr` | `binance/models/enums/status.py` |
| `SortByOrStr` | `binance/models/enums/sort_by.py` |
| `SapiV1LendingProjectListResponse` | `binance/models/sapi_v1_lending_project_list_response.py` |
| `GetFixedActivityProjectListUserDataErrorBody` | `binance/errors/get_fixed_activity_project_list_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.savings.get_fixed_activity_project_position_user_data

- **Route**: `GET /sapi/v1/lending/project/position/list`
- **Signature**: `def get_fixed_activity_project_position_user_data(asset: str, timestamp: int, signature: str, *, project_id: str | None = None, status: StatusOrStr | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `asset`, `timestamp`, `signature`
- **Params**: `asset` — query · `timestamp` — query · `signature` — query · `project_id` — query `projectId` · `status` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1LendingProjectPositionListResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1LendingProjectPositionListResponse], GetFixedActivityProjectPositionUserDataErrorBody]`
- **Error**: `GetFixedActivityProjectPositionUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `StatusOrStr` | `binance/models/enums/status.py` |
| `SapiV1LendingProjectPositionListResponse` | `binance/models/sapi_v1_lending_project_position_list_response.py` |
| `GetFixedActivityProjectPositionUserDataErrorBody` | `binance/errors/get_fixed_activity_project_position_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.savings.purchase_fixed_activity_project_user_data

- **Route**: `POST /sapi/v1/lending/customizedFixed/purchase`
- **Signature**: `def purchase_fixed_activity_project_user_data(project_id: str, lot: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`, `lot`, `timestamp`, `signature`
- **Params**: `project_id` — query `projectId` · `lot` — query · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1LendingCustomizedFixedPurchaseResponse`
- **Returns (raw)**: `ApiResult[SapiV1LendingCustomizedFixedPurchaseResponse, PurchaseFixedActivityProjectUserDataErrorBody]`
- **Error**: `PurchaseFixedActivityProjectUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1LendingCustomizedFixedPurchaseResponse` | `binance/models/sapi_v1_lending_customized_fixed_purchase_response.py` |
| `PurchaseFixedActivityProjectUserDataErrorBody` | `binance/errors/purchase_fixed_activity_project_user_data_error.py` |
| `Error` | `binance/models/error.py` |

