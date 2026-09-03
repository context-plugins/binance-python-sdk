<!-- Generated file — do not edit; regenerated with the SDK. -->

# Rebate — operations

Accessor: `client.rebate` · Source: `binance_public_spot_api/apis/rebate.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.rebate.get_spot_rebate_history_records_user_data

- **Route**: `GET /sapi/v1/rebate/taxQuery`
- **Auth**: `api_key_auth`
- **Signature**: `def get_spot_rebate_history_records_user_data(timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, page: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `page` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1RebateTaxQueryResponse`
- **Returns (raw)**: `ApiResult[SapiV1RebateTaxQueryResponse, GetSpotRebateHistoryRecordsUserDataErrorBody]`
- **Error**: `GetSpotRebateHistoryRecordsUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1RebateTaxQueryResponse` | `binance_public_spot_api/models/sapi_v1_rebate_tax_query_response.py` |
| `GetSpotRebateHistoryRecordsUserDataErrorBody` | `binance_public_spot_api/errors/get_spot_rebate_history_records_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

