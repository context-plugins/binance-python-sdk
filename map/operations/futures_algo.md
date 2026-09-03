<!-- Generated file — do not edit; regenerated with the SDK. -->

# FuturesAlgo — operations

Accessor: `client.futures_algo` · Source: `binance_public_spot_api/apis/futures_algo.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.futures_algo.cancel_algo_order_trade

- **Route**: `DELETE /sapi/v1/algo/futures/order`
- **Auth**: `api_key_auth`
- **Signature**: `def cancel_algo_order_trade(algo_id: int, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `algo_id`, `timestamp`, `signature`
- **Params**: `algo_id` — query `algoId` · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1AlgoFuturesOrderResponse`
- **Returns (raw)**: `ApiResult[SapiV1AlgoFuturesOrderResponse, CancelAlgoOrderTradeErrorBody]`
- **Error**: `CancelAlgoOrderTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1AlgoFuturesOrderResponse` | `binance_public_spot_api/models/sapi_v1_algo_futures_order_response.py` |
| `CancelAlgoOrderTradeErrorBody` | `binance_public_spot_api/errors/cancel_algo_order_trade_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.futures_algo.query_current_algo_open_orders_user_data

- **Route**: `GET /sapi/v1/algo/futures/openOrders`
- **Auth**: `api_key_auth`
- **Signature**: `def query_current_algo_open_orders_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1AlgoFuturesOpenOrdersResponse`
- **Returns (raw)**: `ApiResult[SapiV1AlgoFuturesOpenOrdersResponse, QueryCurrentAlgoOpenOrdersUserDataErrorBody]`
- **Error**: `QueryCurrentAlgoOpenOrdersUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1AlgoFuturesOpenOrdersResponse` | `binance_public_spot_api/models/sapi_v1_algo_futures_open_orders_response.py` |
| `QueryCurrentAlgoOpenOrdersUserDataErrorBody` | `binance_public_spot_api/errors/query_current_algo_open_orders_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.futures_algo.query_historical_algo_orders_user_data

- **Route**: `GET /sapi/v1/algo/futures/historicalOrders`
- **Auth**: `api_key_auth`
- **Signature**: `def query_historical_algo_orders_user_data(timestamp: int, signature: str, *, symbol: str | None = None, side: SideOrStr | None = None, start_time: int | None = None, end_time: int | None = None, page: int | None = None, page_size: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `symbol` — query · `side` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `page` — query · `page_size` — query `pageSize` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1AlgoFuturesHistoricalOrdersResponse`
- **Returns (raw)**: `ApiResult[SapiV1AlgoFuturesHistoricalOrdersResponse, QueryHistoricalAlgoOrdersUserDataErrorBody]`
- **Error**: `QueryHistoricalAlgoOrdersUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SideOrStr` | `binance_public_spot_api/models/enums/side.py` |
| `SapiV1AlgoFuturesHistoricalOrdersResponse` | `binance_public_spot_api/models/sapi_v1_algo_futures_historical_orders_response.py` |
| `QueryHistoricalAlgoOrdersUserDataErrorBody` | `binance_public_spot_api/errors/query_historical_algo_orders_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.futures_algo.query_sub_orders_user_data

- **Route**: `GET /sapi/v1/algo/futures/subOrders`
- **Auth**: `api_key_auth`
- **Signature**: `def query_sub_orders_user_data(algo_id: int, timestamp: int, signature: str, *, page: int | None = None, page_size: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `algo_id`, `timestamp`, `signature`
- **Params**: `algo_id` — query `algoId` · `timestamp` — query · `signature` — query · `page` — query · `page_size` — query `pageSize` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1AlgoFuturesSubOrdersResponse`
- **Returns (raw)**: `ApiResult[SapiV1AlgoFuturesSubOrdersResponse, QuerySubOrdersUserDataErrorBody]`
- **Error**: `QuerySubOrdersUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1AlgoFuturesSubOrdersResponse` | `binance_public_spot_api/models/sapi_v1_algo_futures_sub_orders_response.py` |
| `QuerySubOrdersUserDataErrorBody` | `binance_public_spot_api/errors/query_sub_orders_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.futures_algo.time_weighted_average_price_twap_new_order_trade

- **Route**: `POST /sapi/v1/algo/futures/newOrderTwap`
- **Auth**: `api_key_auth`
- **Signature**: `def time_weighted_average_price_twap_new_order_trade(symbol: str, side: SideOrStr, quantity: float, duration: int, timestamp: int, signature: str, *, position_side: PositionSideOrStr | None = None, client_algo_id: str | None = None, reduce_only: bool | None = None, limit_price: float | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `side`, `quantity`, `duration`, `timestamp`, `signature`
- **Params**: `symbol` — query · `side` — query · `quantity` — query · `duration` — query · `timestamp` — query · `signature` — query · `position_side` — query `positionSide` · `client_algo_id` — query `clientAlgoId` · `reduce_only` — query `reduceOnly` · `limit_price` — query `limitPrice` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1AlgoFuturesNewOrderTwapResponse`
- **Returns (raw)**: `ApiResult[SapiV1AlgoFuturesNewOrderTwapResponse, TimeWeightedAveragePriceTwapNewOrderTradeErrorBody]`
- **Error**: `TimeWeightedAveragePriceTwapNewOrderTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SideOrStr` | `binance_public_spot_api/models/enums/side.py` |
| `PositionSideOrStr` | `binance_public_spot_api/models/enums/position_side.py` |
| `SapiV1AlgoFuturesNewOrderTwapResponse` | `binance_public_spot_api/models/sapi_v1_algo_futures_new_order_twap_response.py` |
| `TimeWeightedAveragePriceTwapNewOrderTradeErrorBody` | `binance_public_spot_api/errors/time_weighted_average_price_twap_new_order_trade_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.futures_algo.volume_participation_vp_new_order_trade

- **Route**: `POST /sapi/v1/algo/futures/newOrderVp`
- **Auth**: `api_key_auth`
- **Signature**: `def volume_participation_vp_new_order_trade(symbol: str, side: SideOrStr, quantity: float, urgency: UrgencyOrStr, timestamp: int, signature: str, *, position_side: PositionSideOrStr | None = None, client_algo_id: str | None = None, reduce_only: bool | None = None, limit_price: float | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `side`, `quantity`, `urgency`, `timestamp`, `signature`
- **Params**: `symbol` — query · `side` — query · `quantity` — query · `urgency` — query · `timestamp` — query · `signature` — query · `position_side` — query `positionSide` · `client_algo_id` — query `clientAlgoId` · `reduce_only` — query `reduceOnly` · `limit_price` — query `limitPrice` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1AlgoFuturesNewOrderVpResponse`
- **Returns (raw)**: `ApiResult[SapiV1AlgoFuturesNewOrderVpResponse, VolumeParticipationVpNewOrderTradeErrorBody]`
- **Error**: `VolumeParticipationVpNewOrderTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SideOrStr` | `binance_public_spot_api/models/enums/side.py` |
| `UrgencyOrStr` | `binance_public_spot_api/models/enums/urgency.py` |
| `PositionSideOrStr` | `binance_public_spot_api/models/enums/position_side.py` |
| `SapiV1AlgoFuturesNewOrderVpResponse` | `binance_public_spot_api/models/sapi_v1_algo_futures_new_order_vp_response.py` |
| `VolumeParticipationVpNewOrderTradeErrorBody` | `binance_public_spot_api/errors/volume_participation_vp_new_order_trade_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

