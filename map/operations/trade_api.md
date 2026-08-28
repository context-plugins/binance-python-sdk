<!-- Generated file — do not edit; regenerated with the SDK. -->

# TradeApi — operations

Accessor: `client.trade_api` · Source: `binance/apis/trade_api.py` · 23 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.trade_api.account_information_user_data

- **Route**: `GET /api/v3/account`
- **Signature**: `def account_information_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `Account`
- **Returns (raw)**: `ApiResult[Account, AccountInformationUserDataErrorBody]`
- **Error**: `AccountInformationUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Account` | `binance/models/account.py` |
| `AccountInformationUserDataErrorBody` | `binance/errors/account_information_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.trade_api.account_trade_list_user_data

- **Route**: `GET /api/v3/myTrades`
- **Signature**: `def account_trade_list_user_data(symbol: str, timestamp: int, signature: str, *, order_id: int | None = None, start_time: int | None = None, end_time: int | None = None, from_id: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `timestamp`, `signature`
- **Params**: `symbol` — query · `timestamp` — query · `signature` — query · `order_id` — query `orderId` · `start_time` — query `startTime` · `end_time` — query `endTime` · `from_id` — query `fromId` · `limit` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[MyTrade]`
- **Returns (raw)**: `ApiResult[list[MyTrade], AccountTradeListUserDataErrorBody]`
- **Error**: `AccountTradeListUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MyTrade` | `binance/models/my_trade.py` |
| `AccountTradeListUserDataErrorBody` | `binance/errors/account_trade_list_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.trade_api.all_orders_user_data

- **Route**: `GET /api/v3/allOrders`
- **Signature**: `def all_orders_user_data(symbol: str, timestamp: int, signature: str, *, order_id: int | None = None, start_time: int | None = None, end_time: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `timestamp`, `signature`
- **Params**: `symbol` — query · `timestamp` — query · `signature` — query · `order_id` — query `orderId` · `start_time` — query `startTime` · `end_time` — query `endTime` · `limit` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[OrderDetails]`
- **Returns (raw)**: `ApiResult[list[OrderDetails], AllOrdersUserDataErrorBody]`
- **Error**: `AllOrdersUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OrderDetails` | `binance/models/order_details.py` |
| `AllOrdersUserDataErrorBody` | `binance/errors/all_orders_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.trade_api.cancel_oco_trade

- **Route**: `DELETE /api/v3/orderList`
- **Signature**: `def cancel_oco_trade(symbol: str, timestamp: int, signature: str, *, order_list_id: int | None = None, list_client_order_id: str | None = None, new_client_order_id: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `timestamp`, `signature`
- **Params**: `symbol` — query · `timestamp` — query · `signature` — query · `order_list_id` — query `orderListId` · `list_client_order_id` — query `listClientOrderId` · `new_client_order_id` — query `newClientOrderId` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `OcoOrder`
- **Returns (raw)**: `ApiResult[OcoOrder, CancelOcoTradeErrorBody]`
- **Error**: `CancelOcoTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OcoOrder` | `binance/models/oco_order.py` |
| `CancelOcoTradeErrorBody` | `binance/errors/cancel_oco_trade_error.py` |
| `Error` | `binance/models/error.py` |

### client.trade_api.cancel_order_trade

- **Route**: `DELETE /api/v3/order`
- **Signature**: `def cancel_order_trade(symbol: str, timestamp: int, signature: str, *, order_id: int | None = None, orig_client_order_id: str | None = None, new_client_order_id: str | None = None, cancel_restrictions: CancelRestrictionsOrStr | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `timestamp`, `signature`
- **Params**: `symbol` — query · `timestamp` — query · `signature` — query · `order_id` — query `orderId` · `orig_client_order_id` — query `origClientOrderId` · `new_client_order_id` — query `newClientOrderId` · `cancel_restrictions` — query `cancelRestrictions` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `Order`
- **Returns (raw)**: `ApiResult[Order, CancelOrderTradeErrorBody]`
- **Error**: `CancelOrderTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CancelRestrictionsOrStr` | `binance/models/enums/cancel_restrictions.py` |
| `Order` | `binance/models/order.py` |
| `CancelOrderTradeErrorBody` | `binance/errors/cancel_order_trade_error.py` |
| `Error` | `binance/models/error.py` |

### client.trade_api.cancel_all_open_orders_on_a_symbol_trade

- **Route**: `DELETE /api/v3/openOrders`
- **Signature**: `def cancel_all_open_orders_on_a_symbol_trade(symbol: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `timestamp`, `signature`
- **Params**: `symbol` — query · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[ApiV3OpenOrdersResponse]`
- **Returns (raw)**: `ApiResult[list[ApiV3OpenOrdersResponse], CancelAllOpenOrdersOnASymbolTradeErrorBody]`
- **Error**: `CancelAllOpenOrdersOnASymbolTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ApiV3OpenOrdersResponse` | `binance/models/unions/api_v3_open_orders_response.py` |
| `CancelAllOpenOrdersOnASymbolTradeErrorBody` | `binance/errors/cancel_all_open_orders_on_a_symbol_trade_error.py` |
| `Error` | `binance/models/error.py` |

### client.trade_api.cancel_an_existing_order_and_send_a_new_order_trade

- **Route**: `POST /api/v3/order/cancelReplace`
- **Signature**: `def cancel_an_existing_order_and_send_a_new_order_trade(symbol: str, side: SideOrStr, type_: Type1OrStr, cancel_replace_mode: str, timestamp: int, signature: str, *, cancel_restrictions: CancelRestrictionsOrStr | None = None, time_in_force: TimeInForceOrStr | None = None, quantity: float | None = None, quote_order_qty: float | None = None, price: float | None = None, cancel_new_client_order_id: str | None = None, cancel_orig_client_order_id: str | None = None, cancel_order_id: int | None = None, new_client_order_id: str | None = None, strategy_id: int | None = None, strategy_type: int | None = None, stop_price: float | None = None, trailing_delta: float | None = None, iceberg_qty: float | None = None, new_order_resp_type: NewOrderRespTypeOrStr | None = None, self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `side`, `type_`, `cancel_replace_mode`, `timestamp`, `signature`
- **Params**: `symbol` — query · `side` — query · `type_` — query `type` · `cancel_replace_mode` — query `cancelReplaceMode` · `timestamp` — query · `signature` — query · `cancel_restrictions` — query `cancelRestrictions` · `time_in_force` — query `timeInForce` · `quantity` — query · `quote_order_qty` — query `quoteOrderQty` · `price` — query · `cancel_new_client_order_id` — query `cancelNewClientOrderId` · `cancel_orig_client_order_id` — query `cancelOrigClientOrderId` · `cancel_order_id` — query `cancelOrderId` · `new_client_order_id` — query `newClientOrderId` · `strategy_id` — query `strategyId` · `strategy_type` — query `strategyType` · `stop_price` — query `stopPrice` · `trailing_delta` — query `trailingDelta` · `iceberg_qty` — query `icebergQty` · `new_order_resp_type` — query `newOrderRespType` · `self_trade_prevention_mode` — query `selfTradePreventionMode` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `ApiV3OrderCancelReplaceResponse`
- **Returns (raw)**: `ApiResult[ApiV3OrderCancelReplaceResponse, CancelAnExistingOrderAndSendANewOrderTradeErrorBody]`
- **Error**: `CancelAnExistingOrderAndSendANewOrderTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SideOrStr` | `binance/models/enums/side.py` |
| `Type1OrStr` | `binance/models/enums/type1.py` |
| `CancelRestrictionsOrStr` | `binance/models/enums/cancel_restrictions.py` |
| `TimeInForceOrStr` | `binance/models/enums/time_in_force.py` |
| `NewOrderRespTypeOrStr` | `binance/models/enums/new_order_resp_type.py` |
| `SelfTradePreventionModeOrStr` | `binance/models/enums/self_trade_prevention_mode.py` |
| `ApiV3OrderCancelReplaceResponse` | `binance/models/api_v3_order_cancel_replace_response.py` |
| `CancelAnExistingOrderAndSendANewOrderTradeErrorBody` | `binance/errors/cancel_an_existing_order_and_send_a_new_order_trade_error.py` |
| `Error` | `binance/models/error.py` |

### client.trade_api.current_open_orders_user_data

- **Route**: `GET /api/v3/openOrders`
- **Signature**: `def current_open_orders_user_data(timestamp: int, signature: str, *, symbol: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `symbol` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[OrderDetails]`
- **Returns (raw)**: `ApiResult[list[OrderDetails], CurrentOpenOrdersUserDataErrorBody]`
- **Error**: `CurrentOpenOrdersUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OrderDetails` | `binance/models/order_details.py` |
| `CurrentOpenOrdersUserDataErrorBody` | `binance/errors/current_open_orders_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.trade_api.new_order_trade

- **Route**: `POST /api/v3/order`
- **Signature**: `def new_order_trade(symbol: str, side: SideOrStr, type_: Type1OrStr, timestamp: int, signature: str, *, time_in_force: TimeInForceOrStr | None = None, quantity: float | None = None, quote_order_qty: float | None = None, price: float | None = None, new_client_order_id: str | None = None, strategy_id: int | None = None, strategy_type: int | None = None, stop_price: float | None = None, trailing_delta: float | None = None, iceberg_qty: float | None = None, new_order_resp_type: NewOrderRespTypeOrStr | None = None, self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `side`, `type_`, `timestamp`, `signature`
- **Params**: `symbol` — query · `side` — query · `type_` — query `type` · `timestamp` — query · `signature` — query · `time_in_force` — query `timeInForce` · `quantity` — query · `quote_order_qty` — query `quoteOrderQty` · `price` — query · `new_client_order_id` — query `newClientOrderId` · `strategy_id` — query `strategyId` · `strategy_type` — query `strategyType` · `stop_price` — query `stopPrice` · `trailing_delta` — query `trailingDelta` · `iceberg_qty` — query `icebergQty` · `new_order_resp_type` — query `newOrderRespType` · `self_trade_prevention_mode` — query `selfTradePreventionMode` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `ApiV3OrderResponse`
- **Returns (raw)**: `ApiResult[ApiV3OrderResponse, NewOrderTradeErrorBody]`
- **Error**: `NewOrderTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SideOrStr` | `binance/models/enums/side.py` |
| `Type1OrStr` | `binance/models/enums/type1.py` |
| `TimeInForceOrStr` | `binance/models/enums/time_in_force.py` |
| `NewOrderRespTypeOrStr` | `binance/models/enums/new_order_resp_type.py` |
| `SelfTradePreventionModeOrStr` | `binance/models/enums/self_trade_prevention_mode.py` |
| `ApiV3OrderResponse` | `binance/models/unions/api_v3_order_response.py` |
| `NewOrderTradeErrorBody` | `binance/errors/new_order_trade_error.py` |
| `Error` | `binance/models/error.py` |

### client.trade_api.new_order_list_oto_trade

- **Route**: `POST /api/v3/orderList/oto`
- **Signature**: `def new_order_list_oto_trade(symbol: str, working_type: WorkingTypeOrStr, working_side: WorkingSideOrStr, working_price: float, working_quantity: float, working_iceberg_qty: float, pending_type: PendingTypeOrStr, pending_side: PendingSideOrStr, pending_quantity: float, timestamp: int, signature: str, *, list_client_order_id: str | None = None, new_order_resp_type: NewOrderRespTypeOrStr | None = None, self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None, working_client_order_id: str | None = None, working_time_in_force: WorkingTimeInForceOrStr | None = None, working_strategy_id: float | None = None, working_strategy_type: int | None = None, pending_client_order_id: str | None = None, pending_price: float | None = None, pending_stop_price: float | None = None, pending_trailing_delta: float | None = None, pending_iceberg_qty: float | None = None, pending_time_in_force: PendingTimeInForceOrStr | None = None, pending_strategy_id: float | None = None, pending_strategy_type: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `working_type`, `working_side`, `working_price`, `working_quantity`, `working_iceberg_qty`, `pending_type`, `pending_side`, `pending_quantity`, `timestamp`, `signature`
- **Params**: `symbol` — query · `working_type` — query `workingType` · `working_side` — query `workingSide` · `working_price` — query `workingPrice` · `working_quantity` — query `workingQuantity` · `working_iceberg_qty` — query `workingIcebergQty` · `pending_type` — query `pendingType` · `pending_side` — query `pendingSide` · `pending_quantity` — query `pendingQuantity` · `timestamp` — query · `signature` — query · `list_client_order_id` — query `listClientOrderId` · `new_order_resp_type` — query `newOrderRespType` · `self_trade_prevention_mode` — query `selfTradePreventionMode` · `working_client_order_id` — query `workingClientOrderId` · `working_time_in_force` — query `workingTimeInForce` · `working_strategy_id` — query `workingStrategyId` · `working_strategy_type` — query `workingStrategyType` · `pending_client_order_id` — query `pendingClientOrderId` · `pending_price` — query `pendingPrice` · `pending_stop_price` — query `pendingStopPrice` · `pending_trailing_delta` — query `pendingTrailingDelta` · `pending_iceberg_qty` — query `pendingIcebergQty` · `pending_time_in_force` — query `pendingTimeInForce` · `pending_strategy_id` — query `pendingStrategyId` · `pending_strategy_type` — query `pendingStrategyType`
- **Returns (parsed)**: `ApiV3OrderListOtoResponse`
- **Returns (raw)**: `ApiResult[ApiV3OrderListOtoResponse, NewOrderListOtoTradeErrorBody]`
- **Error**: `NewOrderListOtoTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WorkingTypeOrStr` | `binance/models/enums/working_type.py` |
| `WorkingSideOrStr` | `binance/models/enums/working_side.py` |
| `PendingTypeOrStr` | `binance/models/enums/pending_type.py` |
| `PendingSideOrStr` | `binance/models/enums/pending_side.py` |
| `NewOrderRespTypeOrStr` | `binance/models/enums/new_order_resp_type.py` |
| `SelfTradePreventionModeOrStr` | `binance/models/enums/self_trade_prevention_mode.py` |
| `WorkingTimeInForceOrStr` | `binance/models/enums/working_time_in_force.py` |
| `PendingTimeInForceOrStr` | `binance/models/enums/pending_time_in_force.py` |
| `ApiV3OrderListOtoResponse` | `binance/models/api_v3_order_list_oto_response.py` |
| `NewOrderListOtoTradeErrorBody` | `binance/errors/new_order_list_oto_trade_error.py` |
| `Error` | `binance/models/error.py` |

### client.trade_api.new_order_list_otoco_trade

- **Route**: `POST /api/v3/orderList/otoco`
- **Signature**: `def new_order_list_otoco_trade(symbol: str, working_type: WorkingTypeOrStr, working_side: WorkingSideOrStr, working_price: float, working_quantity: float, working_iceberg_qty: float, pending_side: PendingSideOrStr, pending_quantity: float, pending_above_type: PendingAboveTypeOrStr, timestamp: int, signature: str, *, list_client_order_id: str | None = None, new_order_resp_type: NewOrderRespTypeOrStr | None = None, self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None, working_client_order_id: str | None = None, working_time_in_force: WorkingTimeInForceOrStr | None = None, working_strategy_id: float | None = None, working_strategy_type: int | None = None, pending_above_client_order_id: str | None = None, pending_above_price: float | None = None, pending_above_stop_price: float | None = None, pending_above_trailing_delta: float | None = None, pending_above_iceberg_qty: float | None = None, pending_above_time_in_force: PendingAboveTimeInForceOrStr | None = None, pending_above_strategy_id: float | None = None, pending_above_strategy_type: int | None = None, pending_below_type: PendingBelowTypeOrStr | None = None, pending_below_client_order_id: str | None = None, pending_below_price: float | None = None, pending_below_stop_price: float | None = None, pending_below_trailing_delta: float | None = None, pending_below_iceberg_qty: float | None = None, pending_below_time_in_force: PendingBelowTimeInForceOrStr | None = None, pending_below_strategy_id: float | None = None, pending_below_strategy_type: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `working_type`, `working_side`, `working_price`, `working_quantity`, `working_iceberg_qty`, `pending_side`, `pending_quantity`, `pending_above_type`, `timestamp`, `signature`
- **Params**: `symbol` — query · `working_type` — query `workingType` · `working_side` — query `workingSide` · `working_price` — query `workingPrice` · `working_quantity` — query `workingQuantity` · `working_iceberg_qty` — query `workingIcebergQty` · `pending_side` — query `pendingSide` · `pending_quantity` — query `pendingQuantity` · `pending_above_type` — query `pendingAboveType` · `timestamp` — query · `signature` — query · `list_client_order_id` — query `listClientOrderId` · `new_order_resp_type` — query `newOrderRespType` · `self_trade_prevention_mode` — query `selfTradePreventionMode` · `working_client_order_id` — query `workingClientOrderId` · `working_time_in_force` — query `workingTimeInForce` · `working_strategy_id` — query `workingStrategyId` · `working_strategy_type` — query `workingStrategyType` · `pending_above_client_order_id` — query `pendingAboveClientOrderId` · `pending_above_price` — query `pendingAbovePrice` · `pending_above_stop_price` — query `pendingAboveStopPrice` · `pending_above_trailing_delta` — query `pendingAboveTrailingDelta` · `pending_above_iceberg_qty` — query `pendingAboveIcebergQty` · `pending_above_time_in_force` — query `pendingAboveTimeInForce` · `pending_above_strategy_id` — query `pendingAboveStrategyId` · `pending_above_strategy_type` — query `pendingAboveStrategyType` · `pending_below_type` — query `pendingBelowType` · `pending_below_client_order_id` — query `pendingBelowClientOrderId` · `pending_below_price` — query `pendingBelowPrice` · `pending_below_stop_price` — query `pendingBelowStopPrice` · `pending_below_trailing_delta` — query `pendingBelowTrailingDelta` · `pending_below_iceberg_qty` — query `pendingBelowIcebergQty` · `pending_below_time_in_force` — query `pendingBelowTimeInForce` · `pending_below_strategy_id` — query `pendingBelowStrategyId` · `pending_below_strategy_type` — query `pendingBelowStrategyType` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `ApiV3OrderListOtocoResponse`
- **Returns (raw)**: `ApiResult[ApiV3OrderListOtocoResponse, NewOrderListOtocoTradeErrorBody]`
- **Error**: `NewOrderListOtocoTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WorkingTypeOrStr` | `binance/models/enums/working_type.py` |
| `WorkingSideOrStr` | `binance/models/enums/working_side.py` |
| `PendingSideOrStr` | `binance/models/enums/pending_side.py` |
| `PendingAboveTypeOrStr` | `binance/models/enums/pending_above_type.py` |
| `NewOrderRespTypeOrStr` | `binance/models/enums/new_order_resp_type.py` |
| `SelfTradePreventionModeOrStr` | `binance/models/enums/self_trade_prevention_mode.py` |
| `WorkingTimeInForceOrStr` | `binance/models/enums/working_time_in_force.py` |
| `PendingAboveTimeInForceOrStr` | `binance/models/enums/pending_above_time_in_force.py` |
| `PendingBelowTypeOrStr` | `binance/models/enums/pending_below_type.py` |
| `PendingBelowTimeInForceOrStr` | `binance/models/enums/pending_below_time_in_force.py` |
| `ApiV3OrderListOtocoResponse` | `binance/models/api_v3_order_list_otoco_response.py` |
| `NewOrderListOtocoTradeErrorBody` | `binance/errors/new_order_list_otoco_trade_error.py` |
| `Error` | `binance/models/error.py` |

### client.trade_api.new_order_list_oco_trade

- **Route**: `POST /api/v3/orderList/oco`
- **Signature**: `def new_order_list_oco_trade(symbol: str, side: SideOrStr, quantity: float, above_type: str, below_type: str, timestamp: int, signature: str, *, list_client_order_id: str | None = None, above_client_order_id: str | None = None, above_iceberg_qty: float | None = None, above_price: float | None = None, above_stop_price: float | None = None, above_trailing_delta: float | None = None, above_time_in_force: AboveTimeInForceOrStr | None = None, above_strategy_id: float | None = None, above_strategy_type: int | None = None, below_client_order_id: str | None = None, below_iceberg_qty: float | None = None, below_price: float | None = None, below_stop_price: float | None = None, below_trailing_delta: float | None = None, below_time_in_force: BelowTimeInForceOrStr | None = None, below_strategy_id: float | None = None, below_strategy_type: int | None = None, new_order_resp_type: NewOrderRespTypeOrStr | None = None, self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `side`, `quantity`, `above_type`, `below_type`, `timestamp`, `signature`
- **Params**: `symbol` — query · `side` — query · `quantity` — query · `above_type` — query `aboveType` · `below_type` — query `belowType` · `timestamp` — query · `signature` — query · `list_client_order_id` — query `listClientOrderId` · `above_client_order_id` — query `aboveClientOrderId` · `above_iceberg_qty` — query `aboveIcebergQty` · `above_price` — query `abovePrice` · `above_stop_price` — query `aboveStopPrice` · `above_trailing_delta` — query `aboveTrailingDelta` · `above_time_in_force` — query `aboveTimeInForce` · `above_strategy_id` — query `aboveStrategyId` · `above_strategy_type` — query `aboveStrategyType` · `below_client_order_id` — query `belowClientOrderId` · `below_iceberg_qty` — query `belowIcebergQty` · `below_price` — query `belowPrice` · `below_stop_price` — query `belowStopPrice` · `below_trailing_delta` — query `belowTrailingDelta` · `below_time_in_force` — query `belowTimeInForce` · `below_strategy_id` — query `belowStrategyId` · `below_strategy_type` — query `belowStrategyType` · `new_order_resp_type` — query `newOrderRespType` · `self_trade_prevention_mode` — query `selfTradePreventionMode` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `ApiV3OrderListOcoResponse`
- **Returns (raw)**: `ApiResult[ApiV3OrderListOcoResponse, NewOrderListOcoTradeErrorBody]`
- **Error**: `NewOrderListOcoTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SideOrStr` | `binance/models/enums/side.py` |
| `AboveTimeInForceOrStr` | `binance/models/enums/above_time_in_force.py` |
| `BelowTimeInForceOrStr` | `binance/models/enums/below_time_in_force.py` |
| `NewOrderRespTypeOrStr` | `binance/models/enums/new_order_resp_type.py` |
| `SelfTradePreventionModeOrStr` | `binance/models/enums/self_trade_prevention_mode.py` |
| `ApiV3OrderListOcoResponse` | `binance/models/api_v3_order_list_oco_response.py` |
| `NewOrderListOcoTradeErrorBody` | `binance/errors/new_order_list_oco_trade_error.py` |
| `Error` | `binance/models/error.py` |

### client.trade_api.new_order_using_sor_trade

- **Route**: `POST /api/v3/sor/order`
- **Signature**: `def new_order_using_sor_trade(symbol: str, side: SideOrStr, type_: Type1OrStr, quantity: float, timestamp: int, signature: str, *, time_in_force: TimeInForceOrStr | None = None, price: float | None = None, new_client_order_id: str | None = None, strategy_id: int | None = None, strategy_type: int | None = None, iceberg_qty: float | None = None, new_order_resp_type: NewOrderRespTypeOrStr | None = None, self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `side`, `type_`, `quantity`, `timestamp`, `signature`
- **Params**: `symbol` — query · `side` — query · `type_` — query `type` · `quantity` — query · `timestamp` — query · `signature` — query · `time_in_force` — query `timeInForce` · `price` — query · `new_client_order_id` — query `newClientOrderId` · `strategy_id` — query `strategyId` · `strategy_type` — query `strategyType` · `iceberg_qty` — query `icebergQty` · `new_order_resp_type` — query `newOrderRespType` · `self_trade_prevention_mode` — query `selfTradePreventionMode` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `ApiV3SorOrderResponse`
- **Returns (raw)**: `ApiResult[ApiV3SorOrderResponse, NewOrderUsingSorTradeErrorBody]`
- **Error**: `NewOrderUsingSorTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SideOrStr` | `binance/models/enums/side.py` |
| `Type1OrStr` | `binance/models/enums/type1.py` |
| `TimeInForceOrStr` | `binance/models/enums/time_in_force.py` |
| `NewOrderRespTypeOrStr` | `binance/models/enums/new_order_resp_type.py` |
| `SelfTradePreventionModeOrStr` | `binance/models/enums/self_trade_prevention_mode.py` |
| `ApiV3SorOrderResponse` | `binance/models/api_v3_sor_order_response.py` |
| `NewOrderUsingSorTradeErrorBody` | `binance/errors/new_order_using_sor_trade_error.py` |
| `Error` | `binance/models/error.py` |

### client.trade_api.query_allocations_user_data

- **Route**: `GET /api/v3/myAllocations`
- **Signature**: `def query_allocations_user_data(symbol: str, timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, from_allocation_id: int | None = None, limit: int | None = None, order_id: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `timestamp`, `signature`
- **Params**: `symbol` — query · `timestamp` — query · `signature` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `from_allocation_id` — query `fromAllocationId` · `limit` — query · `order_id` — query `orderId` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[ApiV3MyAllocationsResponse]`
- **Returns (raw)**: `ApiResult[list[ApiV3MyAllocationsResponse], QueryAllocationsUserDataErrorBody]`
- **Error**: `QueryAllocationsUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ApiV3MyAllocationsResponse` | `binance/models/api_v3_my_allocations_response.py` |
| `QueryAllocationsUserDataErrorBody` | `binance/errors/query_allocations_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.trade_api.query_commission_rates_user_data

- **Route**: `GET /api/v3/account/commission`
- **Signature**: `def query_commission_rates_user_data(symbol: str, timestamp: int, signature: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `timestamp`, `signature`
- **Params**: `symbol` — query · `timestamp` — query · `signature` — query
- **Returns (parsed)**: `ApiV3AccountCommissionResponse`
- **Returns (raw)**: `ApiResult[ApiV3AccountCommissionResponse, QueryCommissionRatesUserDataErrorBody]`
- **Error**: `QueryCommissionRatesUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ApiV3AccountCommissionResponse` | `binance/models/api_v3_account_commission_response.py` |
| `QueryCommissionRatesUserDataErrorBody` | `binance/errors/query_commission_rates_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.trade_api.query_current_order_count_usage_trade

- **Route**: `GET /api/v3/rateLimit/order`
- **Signature**: `def query_current_order_count_usage_trade(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[ApiV3RateLimitOrderResponse]`
- **Returns (raw)**: `ApiResult[list[ApiV3RateLimitOrderResponse], QueryCurrentOrderCountUsageTradeErrorBody]`
- **Error**: `QueryCurrentOrderCountUsageTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ApiV3RateLimitOrderResponse` | `binance/models/api_v3_rate_limit_order_response.py` |
| `QueryCurrentOrderCountUsageTradeErrorBody` | `binance/errors/query_current_order_count_usage_trade_error.py` |
| `Error` | `binance/models/error.py` |

### client.trade_api.query_oco_user_data

- **Route**: `GET /api/v3/orderList`
- **Signature**: `def query_oco_user_data(timestamp: int, signature: str, *, order_list_id: int | None = None, orig_client_order_id: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `order_list_id` — query `orderListId` · `orig_client_order_id` — query `origClientOrderId` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `ApiV3OrderListResponse`
- **Returns (raw)**: `ApiResult[ApiV3OrderListResponse, QueryOcoUserDataErrorBody]`
- **Error**: `QueryOcoUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ApiV3OrderListResponse` | `binance/models/api_v3_order_list_response.py` |
| `QueryOcoUserDataErrorBody` | `binance/errors/query_oco_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.trade_api.query_open_oco_user_data

- **Route**: `GET /api/v3/openOrderList`
- **Signature**: `def query_open_oco_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[ApiV3OpenOrderListResponse]`
- **Returns (raw)**: `ApiResult[list[ApiV3OpenOrderListResponse], QueryOpenOcoUserDataErrorBody]`
- **Error**: `QueryOpenOcoUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ApiV3OpenOrderListResponse` | `binance/models/api_v3_open_order_list_response.py` |
| `QueryOpenOcoUserDataErrorBody` | `binance/errors/query_open_oco_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.trade_api.query_order_user_data

- **Route**: `GET /api/v3/order`
- **Signature**: `def query_order_user_data(symbol: str, timestamp: int, signature: str, *, order_id: int | None = None, orig_client_order_id: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `timestamp`, `signature`
- **Params**: `symbol` — query · `timestamp` — query · `signature` — query · `order_id` — query `orderId` · `orig_client_order_id` — query `origClientOrderId` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `OrderDetails`
- **Returns (raw)**: `ApiResult[OrderDetails, QueryOrderUserDataErrorBody]`
- **Error**: `QueryOrderUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OrderDetails` | `binance/models/order_details.py` |
| `QueryOrderUserDataErrorBody` | `binance/errors/query_order_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.trade_api.query_prevented_matches

- **Route**: `GET /api/v3/myPreventedMatches`
- **Signature**: `def query_prevented_matches(symbol: str, timestamp: int, signature: str, *, prevented_match_id: int | None = None, order_id: int | None = None, from_prevented_match_id: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `timestamp`, `signature`
- **Params**: `symbol` — query · `timestamp` — query · `signature` — query · `prevented_match_id` — query `preventedMatchId` · `order_id` — query `orderId` · `from_prevented_match_id` — query `fromPreventedMatchId` · `limit` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[ApiV3MyPreventedMatchesResponse]`
- **Returns (raw)**: `ApiResult[list[ApiV3MyPreventedMatchesResponse], QueryPreventedMatchesErrorBody]`
- **Error**: `QueryPreventedMatchesErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ApiV3MyPreventedMatchesResponse` | `binance/models/api_v3_my_prevented_matches_response.py` |
| `QueryPreventedMatchesErrorBody` | `binance/errors/query_prevented_matches_error.py` |
| `Error` | `binance/models/error.py` |

### client.trade_api.query_all_oco_user_data

- **Route**: `GET /api/v3/allOrderList`
- **Signature**: `def query_all_oco_user_data(timestamp: int, signature: str, *, from_id: int | None = None, start_time: int | None = None, end_time: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `from_id` — query `fromId` · `start_time` — query `startTime` · `end_time` — query `endTime` · `limit` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[ApiV3AllOrderListResponse]`
- **Returns (raw)**: `ApiResult[list[ApiV3AllOrderListResponse], QueryAllOcoUserDataErrorBody]`
- **Error**: `QueryAllOcoUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ApiV3AllOrderListResponse` | `binance/models/api_v3_all_order_list_response.py` |
| `QueryAllOcoUserDataErrorBody` | `binance/errors/query_all_oco_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.trade_api.test_new_order_trade

- **Route**: `POST /api/v3/order/test`
- **Signature**: `def test_new_order_trade(symbol: str, side: SideOrStr, type_: Type1OrStr, timestamp: int, signature: str, *, time_in_force: TimeInForceOrStr | None = None, quantity: float | None = None, quote_order_qty: float | None = None, price: float | None = None, new_client_order_id: str | None = None, strategy_id: int | None = None, strategy_type: int | None = None, stop_price: float | None = None, trailing_delta: float | None = None, iceberg_qty: float | None = None, new_order_resp_type: NewOrderRespTypeOrStr | None = None, recv_window: int | None = None, compute_commission_rates: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `side`, `type_`, `timestamp`, `signature`
- **Params**: `symbol` — query · `side` — query · `type_` — query `type` · `timestamp` — query · `signature` — query · `time_in_force` — query `timeInForce` · `quantity` — query · `quote_order_qty` — query `quoteOrderQty` · `price` — query · `new_client_order_id` — query `newClientOrderId` · `strategy_id` — query `strategyId` · `strategy_type` — query `strategyType` · `stop_price` — query `stopPrice` · `trailing_delta` — query `trailingDelta` · `iceberg_qty` — query `icebergQty` · `new_order_resp_type` — query `newOrderRespType` · `recv_window` — query `recvWindow` · `compute_commission_rates` — query `computeCommissionRates`
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, TestNewOrderTradeErrorBody]`
- **Error**: `TestNewOrderTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SideOrStr` | `binance/models/enums/side.py` |
| `Type1OrStr` | `binance/models/enums/type1.py` |
| `TimeInForceOrStr` | `binance/models/enums/time_in_force.py` |
| `NewOrderRespTypeOrStr` | `binance/models/enums/new_order_resp_type.py` |
| `TestNewOrderTradeErrorBody` | `binance/errors/test_new_order_trade_error.py` |
| `Error` | `binance/models/error.py` |

### client.trade_api.test_new_order_using_sor_trade

- **Route**: `POST /api/v3/sor/order/test`
- **Signature**: `def test_new_order_using_sor_trade(symbol: str, side: SideOrStr, type_: Type1OrStr, quantity: float, timestamp: int, signature: str, *, time_in_force: TimeInForceOrStr | None = None, price: float | None = None, new_client_order_id: str | None = None, strategy_id: int | None = None, strategy_type: int | None = None, iceberg_qty: float | None = None, new_order_resp_type: NewOrderRespTypeOrStr | None = None, self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None, compute_commission_rates: bool | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `side`, `type_`, `quantity`, `timestamp`, `signature`
- **Params**: `symbol` — query · `side` — query · `type_` — query `type` · `quantity` — query · `timestamp` — query · `signature` — query · `time_in_force` — query `timeInForce` · `price` — query · `new_client_order_id` — query `newClientOrderId` · `strategy_id` — query `strategyId` · `strategy_type` — query `strategyType` · `iceberg_qty` — query `icebergQty` · `new_order_resp_type` — query `newOrderRespType` · `self_trade_prevention_mode` — query `selfTradePreventionMode` · `compute_commission_rates` — query `computeCommissionRates` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, TestNewOrderUsingSorTradeErrorBody]`
- **Error**: `TestNewOrderUsingSorTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SideOrStr` | `binance/models/enums/side.py` |
| `Type1OrStr` | `binance/models/enums/type1.py` |
| `TimeInForceOrStr` | `binance/models/enums/time_in_force.py` |
| `NewOrderRespTypeOrStr` | `binance/models/enums/new_order_resp_type.py` |
| `SelfTradePreventionModeOrStr` | `binance/models/enums/self_trade_prevention_mode.py` |
| `TestNewOrderUsingSorTradeErrorBody` | `binance/errors/test_new_order_using_sor_trade_error.py` |
| `Error` | `binance/models/error.py` |

