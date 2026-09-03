<!-- Generated file — do not edit; regenerated with the SDK. -->

# Convert — operations

Accessor: `client.convert` · Source: `binance_public_spot_api/apis/convert.py` · 9 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.convert.accept_quote_trade

- **Route**: `POST /sapi/v1/convert/acceptQuote`
- **Auth**: `api_key_auth`
- **Signature**: `def accept_quote_trade(quote_id: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `quote_id`, `timestamp`, `signature`
- **Params**: `quote_id` — query `quoteId` · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1ConvertAcceptQuoteResponse`
- **Returns (raw)**: `ApiResult[SapiV1ConvertAcceptQuoteResponse, AcceptQuoteTradeErrorBody]`
- **Error**: `AcceptQuoteTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1ConvertAcceptQuoteResponse` | `binance_public_spot_api/models/sapi_v1_convert_accept_quote_response.py` |
| `AcceptQuoteTradeErrorBody` | `binance_public_spot_api/errors/accept_quote_trade_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.convert.cancel_limit_order_user_data

- **Route**: `POST /sapi/v1/convert/limit/cancelOrder`
- **Auth**: `api_key_auth`
- **Signature**: `def cancel_limit_order_user_data(order_id: int, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `order_id`, `timestamp`, `signature`
- **Params**: `order_id` — query `orderId` · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1ConvertLimitCancelOrderResponse`
- **Returns (raw)**: `ApiResult[SapiV1ConvertLimitCancelOrderResponse, CancelLimitOrderUserDataErrorBody]`
- **Error**: `CancelLimitOrderUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1ConvertLimitCancelOrderResponse` | `binance_public_spot_api/models/sapi_v1_convert_limit_cancel_order_response.py` |
| `CancelLimitOrderUserDataErrorBody` | `binance_public_spot_api/errors/cancel_limit_order_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.convert.get_convert_trade_history_user_data

- **Route**: `GET /sapi/v1/convert/tradeFlow`
- **Auth**: `api_key_auth`
- **Signature**: `def get_convert_trade_history_user_data(start_time: int, end_time: int, timestamp: int, signature: str, *, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `start_time`, `end_time`, `timestamp`, `signature`
- **Params**: `start_time` — query `startTime` · `end_time` — query `endTime` · `timestamp` — query · `signature` — query · `limit` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1ConvertTradeFlowResponse`
- **Returns (raw)**: `ApiResult[SapiV1ConvertTradeFlowResponse, GetConvertTradeHistoryUserDataErrorBody]`
- **Error**: `GetConvertTradeHistoryUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1ConvertTradeFlowResponse` | `binance_public_spot_api/models/sapi_v1_convert_trade_flow_response.py` |
| `GetConvertTradeHistoryUserDataErrorBody` | `binance_public_spot_api/errors/get_convert_trade_history_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.convert.list_all_convert_pairs

- **Route**: `GET /sapi/v1/convert/exchangeInfo`
- **Signature**: `def list_all_convert_pairs(*, from_asset: str | None = None, to_asset: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `from_asset` — query `fromAsset` · `to_asset` — query `toAsset`
- **Returns (parsed)**: `list[SapiV1ConvertExchangeInfoResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1ConvertExchangeInfoResponse], ListAllConvertPairsErrorBody]`
- **Error**: `ListAllConvertPairsErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1ConvertExchangeInfoResponse` | `binance_public_spot_api/models/sapi_v1_convert_exchange_info_response.py` |
| `ListAllConvertPairsErrorBody` | `binance_public_spot_api/errors/list_all_convert_pairs_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.convert.order_status_user_data

- **Route**: `GET /sapi/v1/convert/orderStatus`
- **Auth**: `api_key_auth`
- **Signature**: `def order_status_user_data(timestamp: int, signature: str, *, order_id: str | None = None, quote_id: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `order_id` — query `orderId` · `quote_id` — query `quoteId` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1ConvertOrderStatusResponse`
- **Returns (raw)**: `ApiResult[SapiV1ConvertOrderStatusResponse, OrderStatusUserDataErrorBody]`
- **Error**: `OrderStatusUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1ConvertOrderStatusResponse` | `binance_public_spot_api/models/sapi_v1_convert_order_status_response.py` |
| `OrderStatusUserDataErrorBody` | `binance_public_spot_api/errors/order_status_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.convert.place_limit_order_user_data

- **Route**: `POST /sapi/v1/convert/limit/placeOrder`
- **Auth**: `api_key_auth`
- **Signature**: `def place_limit_order_user_data(base_asset: str, quote_asset: str, limit_price: float, side: SideOrStr, timestamp: int, signature: str, *, base_amount: float | None = None, quote_amount: float | None = None, wallet_type: WalletTypeOrStr | None = None, expired_type: ExpiredTypeOrStr | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `base_asset`, `quote_asset`, `limit_price`, `side`, `timestamp`, `signature`
- **Params**: `base_asset` — query `baseAsset` · `quote_asset` — query `quoteAsset` · `limit_price` — query `limitPrice` · `side` — query · `timestamp` — query · `signature` — query · `base_amount` — query `baseAmount` · `quote_amount` — query `quoteAmount` · `wallet_type` — query `walletType` · `expired_type` — query `expiredType` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1ConvertLimitPlaceOrderResponse`
- **Returns (raw)**: `ApiResult[SapiV1ConvertLimitPlaceOrderResponse, PlaceLimitOrderUserDataErrorBody]`
- **Error**: `PlaceLimitOrderUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SideOrStr` | `binance_public_spot_api/models/enums/side.py` |
| `WalletTypeOrStr` | `binance_public_spot_api/models/enums/wallet_type.py` |
| `ExpiredTypeOrStr` | `binance_public_spot_api/models/enums/expired_type.py` |
| `SapiV1ConvertLimitPlaceOrderResponse` | `binance_public_spot_api/models/sapi_v1_convert_limit_place_order_response.py` |
| `PlaceLimitOrderUserDataErrorBody` | `binance_public_spot_api/errors/place_limit_order_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.convert.query_limit_open_orders_user_data

- **Route**: `GET /sapi/v1/convert/limit/queryOpenOrders`
- **Auth**: `api_key_auth`
- **Signature**: `def query_limit_open_orders_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1ConvertLimitQueryOpenOrdersResponse`
- **Returns (raw)**: `ApiResult[SapiV1ConvertLimitQueryOpenOrdersResponse, QueryLimitOpenOrdersUserDataErrorBody]`
- **Error**: `QueryLimitOpenOrdersUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1ConvertLimitQueryOpenOrdersResponse` | `binance_public_spot_api/models/sapi_v1_convert_limit_query_open_orders_response.py` |
| `QueryLimitOpenOrdersUserDataErrorBody` | `binance_public_spot_api/errors/query_limit_open_orders_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.convert.query_order_quantity_precision_per_asset_user_data

- **Route**: `GET /sapi/v1/convert/assetInfo`
- **Auth**: `api_key_auth`
- **Signature**: `def query_order_quantity_precision_per_asset_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1ConvertAssetInfoResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1ConvertAssetInfoResponse], QueryOrderQuantityPrecisionPerAssetUserDataErrorBody]`
- **Error**: `QueryOrderQuantityPrecisionPerAssetUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1ConvertAssetInfoResponse` | `binance_public_spot_api/models/sapi_v1_convert_asset_info_response.py` |
| `QueryOrderQuantityPrecisionPerAssetUserDataErrorBody` | `binance_public_spot_api/errors/query_order_quantity_precision_per_asset_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.convert.send_quote_request_user_data

- **Route**: `POST /sapi/v1/convert/getQuote`
- **Auth**: `api_key_auth`
- **Signature**: `def send_quote_request_user_data(from_asset: str, to_asset: str, timestamp: int, signature: str, *, from_amount: float | None = None, to_amount: float | None = None, valid_time: str | None = None, wallet_type: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `from_asset`, `to_asset`, `timestamp`, `signature`
- **Params**: `from_asset` — query `fromAsset` · `to_asset` — query `toAsset` · `timestamp` — query · `signature` — query · `from_amount` — query `fromAmount` · `to_amount` — query `toAmount` · `valid_time` — query `validTime` · `wallet_type` — query `walletType` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1ConvertGetQuoteResponse`
- **Returns (raw)**: `ApiResult[SapiV1ConvertGetQuoteResponse, SendQuoteRequestUserDataErrorBody]`
- **Error**: `SendQuoteRequestUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1ConvertGetQuoteResponse` | `binance_public_spot_api/models/sapi_v1_convert_get_quote_response.py` |
| `SendQuoteRequestUserDataErrorBody` | `binance_public_spot_api/errors/send_quote_request_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

