<!-- Generated file — do not edit; regenerated with the SDK. -->

# SpotAlgo — operations

Accessor: `client.spot_algo` · Source: `binance_public_spot_api/apis/spot_algo.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.spot_algo.cancel_algo_order

- **Route**: `DELETE /sapi/v1/algo/spot/order`
- **Auth**: `api_key_auth`
- **Signature**: `def cancel_algo_order(algo_id: int, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `algo_id`, `timestamp`, `signature`
- **Params**: `algo_id` — query `algoId` · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1AlgoSpotOrderResponse`
- **Returns (raw)**: `ApiResult[SapiV1AlgoSpotOrderResponse, CancelAlgoOrderErrorBody]`
- **Error**: `CancelAlgoOrderErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1AlgoSpotOrderResponse` | `binance_public_spot_api/models/sapi_v1_algo_spot_order_response.py` |
| `CancelAlgoOrderErrorBody` | `binance_public_spot_api/errors/cancel_algo_order_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.spot_algo.query_current_algo_open_orders

- **Route**: `GET /sapi/v1/algo/spot/openOrders`
- **Auth**: `api_key_auth`
- **Signature**: `def query_current_algo_open_orders(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1AlgoSpotOpenOrdersResponse`
- **Returns (raw)**: `ApiResult[SapiV1AlgoSpotOpenOrdersResponse, QueryCurrentAlgoOpenOrdersErrorBody]`
- **Error**: `QueryCurrentAlgoOpenOrdersErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1AlgoSpotOpenOrdersResponse` | `binance_public_spot_api/models/sapi_v1_algo_spot_open_orders_response.py` |
| `QueryCurrentAlgoOpenOrdersErrorBody` | `binance_public_spot_api/errors/query_current_algo_open_orders_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.spot_algo.query_historical_algo_orders

- **Route**: `GET /sapi/v1/algo/spot/historicalOrders`
- **Auth**: `api_key_auth`
- **Signature**: `def query_historical_algo_orders(symbol: str, side: SideOrStr, timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, page: int | None = None, page_size: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `side`, `timestamp`, `signature`
- **Params**: `symbol` — query · `side` — query · `timestamp` — query · `signature` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `page` — query · `page_size` — query `pageSize` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1AlgoSpotHistoricalOrdersResponse`
- **Returns (raw)**: `ApiResult[SapiV1AlgoSpotHistoricalOrdersResponse, QueryHistoricalAlgoOrdersErrorBody]`
- **Error**: `QueryHistoricalAlgoOrdersErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SideOrStr` | `binance_public_spot_api/models/enums/side.py` |
| `SapiV1AlgoSpotHistoricalOrdersResponse` | `binance_public_spot_api/models/sapi_v1_algo_spot_historical_orders_response.py` |
| `QueryHistoricalAlgoOrdersErrorBody` | `binance_public_spot_api/errors/query_historical_algo_orders_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.spot_algo.query_sub_orders

- **Route**: `GET /sapi/v1/algo/spot/subOrders`
- **Auth**: `api_key_auth`
- **Signature**: `def query_sub_orders(algo_id: int, timestamp: int, signature: str, *, page: int | None = None, page_size: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `algo_id`, `timestamp`, `signature`
- **Params**: `algo_id` — query `algoId` · `timestamp` — query · `signature` — query · `page` — query · `page_size` — query `pageSize` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1AlgoSpotSubOrdersResponse`
- **Returns (raw)**: `ApiResult[SapiV1AlgoSpotSubOrdersResponse, QuerySubOrdersErrorBody]`
- **Error**: `QuerySubOrdersErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1AlgoSpotSubOrdersResponse` | `binance_public_spot_api/models/sapi_v1_algo_spot_sub_orders_response.py` |
| `QuerySubOrdersErrorBody` | `binance_public_spot_api/errors/query_sub_orders_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.spot_algo.time_weighted_average_price_twap_new_order

- **Route**: `POST /sapi/v1/algo/spot/newOrderTwap`
- **Auth**: `api_key_auth`
- **Signature**: `def time_weighted_average_price_twap_new_order(symbol: str, side: SideOrStr, quantity: float, duration: int, timestamp: int, signature: str, *, client_algo_id: str | None = None, limit_price: float | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `side`, `quantity`, `duration`, `timestamp`, `signature`
- **Params**: `symbol` — query · `side` — query · `quantity` — query · `duration` — query · `timestamp` — query · `signature` — query · `client_algo_id` — query `clientAlgoId` · `limit_price` — query `limitPrice` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1AlgoSpotNewOrderTwapResponse`
- **Returns (raw)**: `ApiResult[SapiV1AlgoSpotNewOrderTwapResponse, TimeWeightedAveragePriceTwapNewOrderErrorBody]`
- **Error**: `TimeWeightedAveragePriceTwapNewOrderErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SideOrStr` | `binance_public_spot_api/models/enums/side.py` |
| `SapiV1AlgoSpotNewOrderTwapResponse` | `binance_public_spot_api/models/sapi_v1_algo_spot_new_order_twap_response.py` |
| `TimeWeightedAveragePriceTwapNewOrderErrorBody` | `binance_public_spot_api/errors/time_weighted_average_price_twap_new_order_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

