from __future__ import annotations

from typing import Any
from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder, param
from ..errors.account_information_user_data_error import (
    AccountInformationUserDataErrorBody,
    account_information_user_data_error_mapper,
)
from ..errors.account_trade_list_user_data_error import (
    AccountTradeListUserDataErrorBody,
    account_trade_list_user_data_error_mapper,
)
from ..errors.all_orders_user_data_error import AllOrdersUserDataErrorBody, all_orders_user_data_error_mapper
from ..errors.cancel_all_open_orders_on_a_symbol_trade_error import (
    CancelAllOpenOrdersOnASymbolTradeErrorBody,
    cancel_all_open_orders_on_a_symbol_trade_error_mapper,
)
from ..errors.cancel_an_existing_order_and_send_a_new_order_trade_error import (
    CancelAnExistingOrderAndSendANewOrderTradeErrorBody,
    cancel_an_existing_order_and_send_a_new_order_trade_error_mapper,
)
from ..errors.cancel_oco_trade_error import CancelOcoTradeErrorBody, cancel_oco_trade_error_mapper
from ..errors.cancel_order_trade_error import CancelOrderTradeErrorBody, cancel_order_trade_error_mapper
from ..errors.current_open_orders_user_data_error import (
    CurrentOpenOrdersUserDataErrorBody,
    current_open_orders_user_data_error_mapper,
)
from ..errors.new_order_list_oco_trade_error import NewOrderListOcoTradeErrorBody, new_order_list_oco_trade_error_mapper
from ..errors.new_order_list_oto_trade_error import NewOrderListOtoTradeErrorBody, new_order_list_oto_trade_error_mapper
from ..errors.new_order_list_otoco_trade_error import (
    NewOrderListOtocoTradeErrorBody,
    new_order_list_otoco_trade_error_mapper,
)
from ..errors.new_order_trade_error import NewOrderTradeErrorBody, new_order_trade_error_mapper
from ..errors.new_order_using_sor_trade_error import (
    NewOrderUsingSorTradeErrorBody,
    new_order_using_sor_trade_error_mapper,
)
from ..errors.query_all_oco_user_data_error import QueryAllOcoUserDataErrorBody, query_all_oco_user_data_error_mapper
from ..errors.query_allocations_user_data_error import (
    QueryAllocationsUserDataErrorBody,
    query_allocations_user_data_error_mapper,
)
from ..errors.query_commission_rates_user_data_error import (
    QueryCommissionRatesUserDataErrorBody,
    query_commission_rates_user_data_error_mapper,
)
from ..errors.query_current_order_count_usage_trade_error import (
    QueryCurrentOrderCountUsageTradeErrorBody,
    query_current_order_count_usage_trade_error_mapper,
)
from ..errors.query_oco_user_data_error import QueryOcoUserDataErrorBody, query_oco_user_data_error_mapper
from ..errors.query_open_oco_user_data_error import QueryOpenOcoUserDataErrorBody, query_open_oco_user_data_error_mapper
from ..errors.query_order_user_data_error import QueryOrderUserDataErrorBody, query_order_user_data_error_mapper
from ..errors.query_prevented_matches_error import QueryPreventedMatchesErrorBody, query_prevented_matches_error_mapper
from ..errors.test_new_order_trade_error import TestNewOrderTradeErrorBody, test_new_order_trade_error_mapper
from ..errors.test_new_order_using_sor_trade_error import (
    TestNewOrderUsingSorTradeErrorBody,
    test_new_order_using_sor_trade_error_mapper,
)
from ..models.account import Account
from ..models.api_v3_account_commission_response import ApiV3AccountCommissionResponse
from ..models.api_v3_all_order_list_response import ApiV3AllOrderListResponse
from ..models.api_v3_my_allocations_response import ApiV3MyAllocationsResponse
from ..models.api_v3_my_prevented_matches_response import ApiV3MyPreventedMatchesResponse
from ..models.api_v3_open_order_list_response import ApiV3OpenOrderListResponse
from ..models.api_v3_order_cancel_replace_response import ApiV3OrderCancelReplaceResponse
from ..models.api_v3_order_list_oco_response import ApiV3OrderListOcoResponse
from ..models.api_v3_order_list_oto_response import ApiV3OrderListOtoResponse
from ..models.api_v3_order_list_otoco_response import ApiV3OrderListOtocoResponse
from ..models.api_v3_order_list_response import ApiV3OrderListResponse
from ..models.api_v3_rate_limit_order_response import ApiV3RateLimitOrderResponse
from ..models.api_v3_sor_order_response import ApiV3SorOrderResponse
from ..models.enums.above_time_in_force import AboveTimeInForceOrStr
from ..models.enums.below_time_in_force import BelowTimeInForceOrStr
from ..models.enums.cancel_restrictions import CancelRestrictionsOrStr
from ..models.enums.new_order_resp_type import NewOrderRespTypeOrStr
from ..models.enums.pending_above_time_in_force import PendingAboveTimeInForceOrStr
from ..models.enums.pending_above_type import PendingAboveTypeOrStr
from ..models.enums.pending_below_time_in_force import PendingBelowTimeInForceOrStr
from ..models.enums.pending_below_type import PendingBelowTypeOrStr
from ..models.enums.pending_side import PendingSideOrStr
from ..models.enums.pending_time_in_force import PendingTimeInForceOrStr
from ..models.enums.pending_type import PendingTypeOrStr
from ..models.enums.self_trade_prevention_mode import SelfTradePreventionModeOrStr
from ..models.enums.side import SideOrStr
from ..models.enums.time_in_force import TimeInForceOrStr
from ..models.enums.type1 import Type1OrStr
from ..models.enums.working_side import WorkingSideOrStr
from ..models.enums.working_time_in_force import WorkingTimeInForceOrStr
from ..models.enums.working_type import WorkingTypeOrStr
from ..models.my_trade import MyTrade
from ..models.oco_order import OcoOrder
from ..models.order import Order
from ..models.order_details import OrderDetails
from ..models.unions.api_v3_open_orders_response import ApiV3OpenOrdersResponse
from ..models.unions.api_v3_order_response import ApiV3OrderResponse
from ..server.server import Server


class TradeApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TradeApiWithRawResponse(client, server, auth)

    def account_information_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Account:
        """Get current account information.

        Weight(IP): 20

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Account details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.account_information_user_data(
            timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def account_trade_list_user_data(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        from_id: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[MyTrade]:
        """Get trades for a specific account and symbol.

        If ``fromId`` is set, it will get id >= that ``fromId``. Otherwise most recent orders are returned.

        The time between startTime and endTime can't be longer than 24 hours. These are the supported combinations of
        all parameters:

          symbol

          symbol + orderId

          symbol + startTime

          symbol + endTime

          symbol + fromId

          symbol + startTime + endTime

          symbol+ orderId + fromId

        Weight(IP): 20

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: This can only be used in combination with symbol.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            from_id: Trade id to fetch from. Default gets most recent trades.
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of trades

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.account_trade_list_user_data(
            symbol,
            timestamp,
            signature,
            order_id=order_id,
            start_time=start_time,
            end_time=end_time,
            from_id=from_id,
            limit=limit,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def all_orders_user_data(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[OrderDetails]:
        """Get all account orders; active, canceled, or filled..

        - If ``orderId`` is set, it will get orders >= that ``orderId``. Otherwise most recent orders are returned.
        - For some historical orders ``cummulativeQuoteQty`` will be < 0, meaning the data is not available at this
            time.
        - If ``startTime`` and/or ``endTime`` provided, ``orderId`` is not required

        Weight(IP): 20

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order id
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Current open orders

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.all_orders_user_data(
            symbol,
            timestamp,
            signature,
            order_id=order_id,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def cancel_oco_trade(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        order_list_id: int | None = None,
        list_client_order_id: str | None = None,
        new_client_order_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OcoOrder:
        """Cancel an entire Order List

        Canceling an individual leg will cancel the entire OCO

        Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            order_list_id: Order list id
            list_client_order_id: A unique Id for the entire orderList
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Report on deleted OCO

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.cancel_oco_trade(
            symbol,
            timestamp,
            signature,
            order_list_id=order_list_id,
            list_client_order_id=list_client_order_id,
            new_client_order_id=new_client_order_id,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def cancel_order_trade(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        orig_client_order_id: str | None = None,
        new_client_order_id: str | None = None,
        cancel_restrictions: CancelRestrictionsOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Order:
        """Cancel an active order.

        Either ``orderId`` or ``origClientOrderId`` must be sent.

        Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order id
            orig_client_order_id: Order id from client
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            cancel_restrictions: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Cancelled order

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.cancel_order_trade(
            symbol,
            timestamp,
            signature,
            order_id=order_id,
            orig_client_order_id=orig_client_order_id,
            new_client_order_id=new_client_order_id,
            cancel_restrictions=cancel_restrictions,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def cancel_all_open_orders_on_a_symbol_trade(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ApiV3OpenOrdersResponse]:
        """Cancels all active orders on a symbol. This includes OCO orders.

        Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Cancelled orders

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.cancel_all_open_orders_on_a_symbol_trade(
            symbol, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def cancel_an_existing_order_and_send_a_new_order_trade(
        self,
        symbol: str,
        side: SideOrStr,
        type_: Type1OrStr,
        cancel_replace_mode: str,
        timestamp: int,
        signature: str,
        *,
        cancel_restrictions: CancelRestrictionsOrStr | None = None,
        time_in_force: TimeInForceOrStr | None = None,
        quantity: float | None = None,
        quote_order_qty: float | None = None,
        price: float | None = None,
        cancel_new_client_order_id: str | None = None,
        cancel_orig_client_order_id: str | None = None,
        cancel_order_id: int | None = None,
        new_client_order_id: str | None = None,
        strategy_id: int | None = None,
        strategy_type: int | None = None,
        stop_price: float | None = None,
        trailing_delta: float | None = None,
        iceberg_qty: float | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV3OrderCancelReplaceResponse:
        """Cancels an existing order and places a new order on the same symbol.

        Filters and Order Count are evaluated before the processing of the cancellation and order placement occurs.

        A new order that was not attempted (i.e. when newOrderResult: NOT_ATTEMPTED), will still increase the order
        count by 1.

        Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            type_: Order type
            cancel_replace_mode: - ``STOP_ON_FAILURE`` If the cancel request fails, the new order placement will not be
                attempted. - ``ALLOW_FAILURES`` If new order placement will be attempted even if cancel request fails.
            timestamp: UTC timestamp in ms
            signature: Signature
            cancel_restrictions: Value sent with the request.
            time_in_force: Order time in force
            quantity: Order quantity
            quote_order_qty: Quote quantity
            price: Order price
            cancel_new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            cancel_orig_client_order_id: Either the cancelOrigClientOrderId or cancelOrderId must be provided. If both
                are provided, cancelOrderId takes precedence.
            cancel_order_id: Either the cancelOrigClientOrderId or cancelOrderId must be provided. If both are provided,
                cancelOrderId takes precedence.
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            strategy_id: Value sent with the request.
            strategy_type: The value cannot be less than 1000000.
            stop_price: Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
            trailing_delta: Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
            iceberg_qty: Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.
            new_order_resp_type: Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders
                default to ACK.
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Operation details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.cancel_an_existing_order_and_send_a_new_order_trade(
            symbol,
            side,
            type_,
            cancel_replace_mode,
            timestamp,
            signature,
            cancel_restrictions=cancel_restrictions,
            time_in_force=time_in_force,
            quantity=quantity,
            quote_order_qty=quote_order_qty,
            price=price,
            cancel_new_client_order_id=cancel_new_client_order_id,
            cancel_orig_client_order_id=cancel_orig_client_order_id,
            cancel_order_id=cancel_order_id,
            new_client_order_id=new_client_order_id,
            strategy_id=strategy_id,
            strategy_type=strategy_type,
            stop_price=stop_price,
            trailing_delta=trailing_delta,
            iceberg_qty=iceberg_qty,
            new_order_resp_type=new_order_resp_type,
            self_trade_prevention_mode=self_trade_prevention_mode,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def current_open_orders_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[OrderDetails]:
        """Get all open orders on a symbol. Careful when accessing this with no symbol.

        Weight(IP):
        - ``6`` for a single symbol;
        - ``80`` when the symbol parameter is omitted;

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            symbol: Trading symbol, e.g. BNBUSDT
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Current open orders

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.current_open_orders_user_data(
            timestamp, signature, symbol=symbol, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def new_order_trade(
        self,
        symbol: str,
        side: SideOrStr,
        type_: Type1OrStr,
        timestamp: int,
        signature: str,
        *,
        time_in_force: TimeInForceOrStr | None = None,
        quantity: float | None = None,
        quote_order_qty: float | None = None,
        price: float | None = None,
        new_client_order_id: str | None = None,
        strategy_id: int | None = None,
        strategy_type: int | None = None,
        stop_price: float | None = None,
        trailing_delta: float | None = None,
        iceberg_qty: float | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV3OrderResponse:
        """Send in a new order.

        - ``LIMIT_MAKER`` are ``LIMIT`` orders that will be rejected if they would immediately match and trade as a
            taker.
        - ``STOP_LOSS`` and ``TAKE_PROFIT`` will execute a ``MARKET`` order when the ``stopPrice`` is reached.
        - Any ``LIMIT`` or ``LIMIT_MAKER`` type order can be made an iceberg order by sending an ``icebergQty``.
        - Any order with an ``icebergQty`` MUST have ``timeInForce`` set to ``GTC``.
        - ``MARKET`` orders using ``quantity`` specifies how much a user wants to buy or sell based on the market price.
        - ``MARKET`` orders using ``quoteOrderQty`` specifies the amount the user wants to spend (when buying) or
            receive (when selling) of the quote asset; the correct quantity will be determined based on the market
            liquidity and ``quoteOrderQty``.
        - ``MARKET`` orders using ``quoteOrderQty`` will not break ``LOT_SIZE`` filter rules; the order will execute a
            quantity that will have the notional value as close as possible to ``quoteOrderQty``.
        - same ``newClientOrderId`` can be accepted only when the previous one is filled, otherwise the order will be
            rejected.

        Trigger order price rules against market price for both ``MARKET`` and ``LIMIT`` versions:

        - Price above market price: ``STOP_LOSS`` ``BUY``, ``TAKE_PROFIT`` ``SELL``
        - Price below market price: ``STOP_LOSS`` ``SELL``, ``TAKE_PROFIT`` ``BUY``


        Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            type_: Order type
            timestamp: UTC timestamp in ms
            signature: Signature
            time_in_force: Order time in force
            quantity: Order quantity
            quote_order_qty: Quote quantity
            price: Order price
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            strategy_id: Value sent with the request.
            strategy_type: The value cannot be less than 1000000.
            stop_price: Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
            trailing_delta: Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
            iceberg_qty: Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.
            new_order_resp_type: Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders
                default to ACK.
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Order result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.new_order_trade(
            symbol,
            side,
            type_,
            timestamp,
            signature,
            time_in_force=time_in_force,
            quantity=quantity,
            quote_order_qty=quote_order_qty,
            price=price,
            new_client_order_id=new_client_order_id,
            strategy_id=strategy_id,
            strategy_type=strategy_type,
            stop_price=stop_price,
            trailing_delta=trailing_delta,
            iceberg_qty=iceberg_qty,
            new_order_resp_type=new_order_resp_type,
            self_trade_prevention_mode=self_trade_prevention_mode,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def new_order_list_oto_trade(
        self,
        symbol: str,
        working_type: WorkingTypeOrStr,
        working_side: WorkingSideOrStr,
        working_price: float,
        working_quantity: float,
        working_iceberg_qty: float,
        pending_type: PendingTypeOrStr,
        pending_side: PendingSideOrStr,
        pending_quantity: float,
        timestamp: int,
        signature: str,
        *,
        list_client_order_id: str | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        working_client_order_id: str | None = None,
        working_time_in_force: WorkingTimeInForceOrStr | None = None,
        working_strategy_id: float | None = None,
        working_strategy_type: int | None = None,
        pending_client_order_id: str | None = None,
        pending_price: float | None = None,
        pending_stop_price: float | None = None,
        pending_trailing_delta: float | None = None,
        pending_iceberg_qty: float | None = None,
        pending_time_in_force: PendingTimeInForceOrStr | None = None,
        pending_strategy_id: float | None = None,
        pending_strategy_type: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV3OrderListOtoResponse:
        """Places an ``OTO``.
        - An ``OTO`` (One-Triggers-the-Other) is an order list comprised of 2 orders.
        - The first order is called the working order and must be ``LIMIT`` or ``LIMIT_MAKER``. Initially, only the
            working order goes on the order book.
        - The second order is called the pending order. It can be any order type except for ``MARKET`` orders using
            parameter ``quoteOrderQty``. The pending order is only placed on the order book when the working order gets
            fully filled.
        - If either the working order or the pending order is cancelled individually, the other order in the order list
            will also be canceled or expired.
        - When the order list is placed, if the working order gets immediately fully filled, the placement response will
            show the working order as ``FILLED`` but the pending order will still appear as ``PENDING_NEW``. You need to
            query the status of the pending order again to see its updated status.
        - OTOs add 2 orders to the unfilled order count, ``EXCHANGE_MAX_NUM_ORDERS`` filter and ``MAX_NUM_ORDERS``
            filter.

        Weight: 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            working_type: Supported values: LIMIT,LIMIT_MAKER
            working_side: BUY,SELL
            working_price: Value sent with the request.
            working_quantity: Sets the quantity for the working order.
            working_iceberg_qty: This can only be used if workingTimeInForce is GTC.
            pending_type: Supported values: Order Types Note that MARKET orders using quoteOrderQty are not supported.
            pending_side: BUY,SELL
            pending_quantity: Sets the quantity for the pending order.
            timestamp: UTC timestamp in ms
            signature: Signature
            list_client_order_id: Arbitrary unique ID among open order lists. Automatically generated if not sent. A new
                order list with the same ``listClientOrderId`` is accepted only when the previous one is filled or
                completely expired. ``listClientOrderId`` is distinct from the ``workingClientOrderId`` and the
                ``pendingClientOrderId``.
            new_order_resp_type: Set the response JSON.
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            working_client_order_id: Arbitrary unique ID among open orders for the working order. Automatically
                generated if not sent.
            working_time_in_force: GTC, IOC, FOK
            working_strategy_id: Arbitrary numeric value identifying the working order within an order strategy.
            working_strategy_type: Arbitrary numeric value identifying the working order strategy. Values smaller than
                1000000 are reserved and cannot be used.
            pending_client_order_id: Arbitrary unique ID among open orders for the pending order. Automatically
                generated if not sent.
            pending_price: Value sent with the request.
            pending_stop_price: Value sent with the request.
            pending_trailing_delta: Value sent with the request.
            pending_iceberg_qty: This can only be used if pendingTimeInForce is GTC.
            pending_time_in_force: GTC, IOC, FOK
            pending_strategy_id: Arbitrary numeric value identifying the pending order within an order strategy.
            pending_strategy_type: Arbitrary numeric value identifying the pending order strategy. Values smaller than
                1000000 are reserved and cannot be used.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            New OTO details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.new_order_list_oto_trade(
            symbol,
            working_type,
            working_side,
            working_price,
            working_quantity,
            working_iceberg_qty,
            pending_type,
            pending_side,
            pending_quantity,
            timestamp,
            signature,
            list_client_order_id=list_client_order_id,
            new_order_resp_type=new_order_resp_type,
            self_trade_prevention_mode=self_trade_prevention_mode,
            working_client_order_id=working_client_order_id,
            working_time_in_force=working_time_in_force,
            working_strategy_id=working_strategy_id,
            working_strategy_type=working_strategy_type,
            pending_client_order_id=pending_client_order_id,
            pending_price=pending_price,
            pending_stop_price=pending_stop_price,
            pending_trailing_delta=pending_trailing_delta,
            pending_iceberg_qty=pending_iceberg_qty,
            pending_time_in_force=pending_time_in_force,
            pending_strategy_id=pending_strategy_id,
            pending_strategy_type=pending_strategy_type,
            request_options=request_options,
        ).unwrap()

    def new_order_list_otoco_trade(
        self,
        symbol: str,
        working_type: WorkingTypeOrStr,
        working_side: WorkingSideOrStr,
        working_price: float,
        working_quantity: float,
        working_iceberg_qty: float,
        pending_side: PendingSideOrStr,
        pending_quantity: float,
        pending_above_type: PendingAboveTypeOrStr,
        timestamp: int,
        signature: str,
        *,
        list_client_order_id: str | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        working_client_order_id: str | None = None,
        working_time_in_force: WorkingTimeInForceOrStr | None = None,
        working_strategy_id: float | None = None,
        working_strategy_type: int | None = None,
        pending_above_client_order_id: str | None = None,
        pending_above_price: float | None = None,
        pending_above_stop_price: float | None = None,
        pending_above_trailing_delta: float | None = None,
        pending_above_iceberg_qty: float | None = None,
        pending_above_time_in_force: PendingAboveTimeInForceOrStr | None = None,
        pending_above_strategy_id: float | None = None,
        pending_above_strategy_type: int | None = None,
        pending_below_type: PendingBelowTypeOrStr | None = None,
        pending_below_client_order_id: str | None = None,
        pending_below_price: float | None = None,
        pending_below_stop_price: float | None = None,
        pending_below_trailing_delta: float | None = None,
        pending_below_iceberg_qty: float | None = None,
        pending_below_time_in_force: PendingBelowTimeInForceOrStr | None = None,
        pending_below_strategy_id: float | None = None,
        pending_below_strategy_type: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV3OrderListOtocoResponse:
        """Place an ``OTOCO``.
        - An ``OTOCO`` (One-Triggers-One-Cancels-the-Other) is an order list comprised of 3 orders.
        - The first order is called the working order and must be ``LIMIT`` or ``LIMIT_MAKER``. Initially, only the
            working order goes on the order book.
          - The behavior of the working order is the same as the ``OTO``.
        - ``OTOCO`` has 2 pending orders (pending above and pending below), forming an ``OCO`` pair. The pending orders
            are only placed on the order book when the working order gets fully filled.
          - The rules of the pending above and pending below follow the same rules as the Order List ``OCO``.
        - OTOCOs add 3 orders against the unfilled order count, ``EXCHANGE_MAX_NUM_ORDERS`` filter, and
            ``MAX_NUM_ORDERS`` filter.

        Weight: 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            working_type: Supported values: LIMIT,LIMIT_MAKER
            working_side: BUY,SELL
            working_price: Value sent with the request.
            working_quantity: Sets the quantity for the working order.
            working_iceberg_qty: This can only be used if workingTimeInForce is GTC.
            pending_side: BUY,SELL
            pending_quantity: Sets the quantity for the pending order.
            pending_above_type: Supported values: LIMIT_MAKER, STOP_LOSS, and STOP_LOSS_LIMIT
            timestamp: UTC timestamp in ms
            signature: Signature
            list_client_order_id: Arbitrary unique ID among open order lists. Automatically generated if not sent. A new
                order list with the same ``listClientOrderId`` is accepted only when the previous one is filled or
                completely expired. ``listClientOrderId`` is distinct from the ``workingClientOrderId`` and the
                ``pendingClientOrderId``.
            new_order_resp_type: Set the response JSON.
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            working_client_order_id: Arbitrary unique ID among open orders for the working order. Automatically
                generated if not sent.
            working_time_in_force: GTC, IOC, FOK
            working_strategy_id: Arbitrary numeric value identifying the working order within an order strategy.
            working_strategy_type: Arbitrary numeric value identifying the working order strategy. Values smaller than
                1000000 are reserved and cannot be used.
            pending_above_client_order_id: Arbitrary unique ID among open orders for the pending above order.
                Automatically generated if not sent.
            pending_above_price: Value sent with the request.
            pending_above_stop_price: Value sent with the request.
            pending_above_trailing_delta: Value sent with the request.
            pending_above_iceberg_qty: This can only be used if pendingAboveTimeInForce is GTC.
            pending_above_time_in_force: Value sent with the request.
            pending_above_strategy_id: Arbitrary numeric value identifying the pending above order within an order
                strategy.
            pending_above_strategy_type: Arbitrary numeric value identifying the pending above order strategy. Values
                smaller than 1000000 are reserved and cannot be used.
            pending_below_type: Supported values: LIMIT_MAKER, STOP_LOSS, and STOP_LOSS_LIMIT
            pending_below_client_order_id: Arbitrary unique ID among open orders for the pending below order.
                Automatically generated if not sent.
            pending_below_price: Value sent with the request.
            pending_below_stop_price: Value sent with the request.
            pending_below_trailing_delta: Value sent with the request.
            pending_below_iceberg_qty: This can only be used if pendingBelowTimeInForce is GTC.
            pending_below_time_in_force: Value sent with the request.
            pending_below_strategy_id: Arbitrary numeric value identifying the pending below order within an order
                strategy.
            pending_below_strategy_type: Arbitrary numeric value identifying the pending below order strategy. Values
                smaller than 1000000 are reserved and cannot be used.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            New OTOCO details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.new_order_list_otoco_trade(
            symbol,
            working_type,
            working_side,
            working_price,
            working_quantity,
            working_iceberg_qty,
            pending_side,
            pending_quantity,
            pending_above_type,
            timestamp,
            signature,
            list_client_order_id=list_client_order_id,
            new_order_resp_type=new_order_resp_type,
            self_trade_prevention_mode=self_trade_prevention_mode,
            working_client_order_id=working_client_order_id,
            working_time_in_force=working_time_in_force,
            working_strategy_id=working_strategy_id,
            working_strategy_type=working_strategy_type,
            pending_above_client_order_id=pending_above_client_order_id,
            pending_above_price=pending_above_price,
            pending_above_stop_price=pending_above_stop_price,
            pending_above_trailing_delta=pending_above_trailing_delta,
            pending_above_iceberg_qty=pending_above_iceberg_qty,
            pending_above_time_in_force=pending_above_time_in_force,
            pending_above_strategy_id=pending_above_strategy_id,
            pending_above_strategy_type=pending_above_strategy_type,
            pending_below_type=pending_below_type,
            pending_below_client_order_id=pending_below_client_order_id,
            pending_below_price=pending_below_price,
            pending_below_stop_price=pending_below_stop_price,
            pending_below_trailing_delta=pending_below_trailing_delta,
            pending_below_iceberg_qty=pending_below_iceberg_qty,
            pending_below_time_in_force=pending_below_time_in_force,
            pending_below_strategy_id=pending_below_strategy_id,
            pending_below_strategy_type=pending_below_strategy_type,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def new_order_list_oco_trade(
        self,
        symbol: str,
        side: SideOrStr,
        quantity: float,
        above_type: str,
        below_type: str,
        timestamp: int,
        signature: str,
        *,
        list_client_order_id: str | None = None,
        above_client_order_id: str | None = None,
        above_iceberg_qty: float | None = None,
        above_price: float | None = None,
        above_stop_price: float | None = None,
        above_trailing_delta: float | None = None,
        above_time_in_force: AboveTimeInForceOrStr | None = None,
        above_strategy_id: float | None = None,
        above_strategy_type: int | None = None,
        below_client_order_id: str | None = None,
        below_iceberg_qty: float | None = None,
        below_price: float | None = None,
        below_stop_price: float | None = None,
        below_trailing_delta: float | None = None,
        below_time_in_force: BelowTimeInForceOrStr | None = None,
        below_strategy_id: float | None = None,
        below_strategy_type: int | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV3OrderListOcoResponse:
        """Send in an one-cancels-the-other (OCO) pair, where activation of one order immediately cancels the other.

        - An ``OCO`` has 2 orders called the above order and below order.
        - One of the orders must be a ``LIMIT_MAKER`` order and the other must be ``STOP_LOSS`` or``STOP_LOSS_LIMIT``
            order.
        - Price restrictions:
            - If the ``OCO`` is on the ``SELL`` side: ``LIMIT_MAKER`` price > Last Traded Price > stopPrice
            - If the ``OCO`` is on the ``BUY`` side: ``LIMIT_MAKER`` price < Last Traded Price < stopPrice
        - OCOs add 2 orders to the unfilled order count, ``EXCHANGE_MAX_ORDERS`` filter, and the ``MAX_NUM_ORDERS``
            filter.

        Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            quantity: Value sent with the request.
            above_type: Supported values : ``STOP_LOSS_LIMIT``, ``STOP_LOSS``, ``LIMIT_MAKER``
            below_type: Supported values : ``STOP_LOSS_LIMIT``, ``STOP_LOSS``, ``LIMIT_MAKER``
            timestamp: UTC timestamp in ms
            signature: Signature
            list_client_order_id: Arbitrary unique ID among open order lists. Automatically generated if not sent. A new
                order list with the same ``listClientOrderId`` is accepted only when the previous one is filled or
                completely expired. ``listClientOrderId`` is distinct from the ``aboveClientOrderId`` and the
                ``belowCLientOrderId``.
            above_client_order_id: Arbitrary unique ID among open orders for the above order. Automatically generated if
                not sent
            above_iceberg_qty: Note that this can only be used if ``aboveTimeInForce`` is ``GTC``.
            above_price: Value sent with the request.
            above_stop_price: Can be used if ``aboveType`` is ``STOP_LOSS`` or ``STOP_LOSS_LIMIT``. Either
                ``aboveStopPrice`` or ``aboveTrailingDelta`` or both, must be specified.
            above_trailing_delta: Value sent with the request.
            above_time_in_force: Required if the ``aboveType`` is ``STOP_LOSS_LIMIT``.
            above_strategy_id: Arbitrary numeric value identifying the above order within an order strategy.
            above_strategy_type: Arbitrary numeric value identifying the above order strategy. Values smaller than
                1000000 are reserved and cannot be used.
            below_client_order_id: Arbitrary unique ID among open orders for the below order. Automatically generated if
                not sent
            below_iceberg_qty: Note that this can only be used if ``belowTimeInForce`` is ``GTC``.
            below_price: Can be used if ``belowType`` is ``STOP_LOSS_LIMIT`` or ``LIMIT_MAKER`` to specify the limit
                price.
            below_stop_price: Can be used if ``belowType`` is ``STOP_LOSS`` or ``STOP_LOSS_LIMIT``. Either
                ``belowStopPrice`` or ``belowTrailingDelta`` or both, must be specified.
            below_trailing_delta: Value sent with the request.
            below_time_in_force: Required if the ``belowType`` is ``STOP_LOSS_LIMIT``.
            below_strategy_id: Arbitrary numeric value identifying the below order within an order strategy.
            below_strategy_type: Arbitrary numeric value identifying the below order strategy. Values smaller than
                1000000 are reserved and cannot be used.
            new_order_resp_type: Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders
                default to ACK.
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            New OCO details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.new_order_list_oco_trade(
            symbol,
            side,
            quantity,
            above_type,
            below_type,
            timestamp,
            signature,
            list_client_order_id=list_client_order_id,
            above_client_order_id=above_client_order_id,
            above_iceberg_qty=above_iceberg_qty,
            above_price=above_price,
            above_stop_price=above_stop_price,
            above_trailing_delta=above_trailing_delta,
            above_time_in_force=above_time_in_force,
            above_strategy_id=above_strategy_id,
            above_strategy_type=above_strategy_type,
            below_client_order_id=below_client_order_id,
            below_iceberg_qty=below_iceberg_qty,
            below_price=below_price,
            below_stop_price=below_stop_price,
            below_trailing_delta=below_trailing_delta,
            below_time_in_force=below_time_in_force,
            below_strategy_id=below_strategy_id,
            below_strategy_type=below_strategy_type,
            new_order_resp_type=new_order_resp_type,
            self_trade_prevention_mode=self_trade_prevention_mode,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def new_order_using_sor_trade(
        self,
        symbol: str,
        side: SideOrStr,
        type_: Type1OrStr,
        quantity: float,
        timestamp: int,
        signature: str,
        *,
        time_in_force: TimeInForceOrStr | None = None,
        price: float | None = None,
        new_client_order_id: str | None = None,
        strategy_id: int | None = None,
        strategy_type: int | None = None,
        iceberg_qty: float | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV3SorOrderResponse:
        """Weight(IP): 6

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            type_: Order type
            quantity: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            time_in_force: Order time in force
            price: Value sent with the request.
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            strategy_id: Value sent with the request.
            strategy_type: The value cannot be less than 1000000.
            iceberg_qty: Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.
            new_order_resp_type: Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders
                default to ACK.
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            New order details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.new_order_using_sor_trade(
            symbol,
            side,
            type_,
            quantity,
            timestamp,
            signature,
            time_in_force=time_in_force,
            price=price,
            new_client_order_id=new_client_order_id,
            strategy_id=strategy_id,
            strategy_type=strategy_type,
            iceberg_qty=iceberg_qty,
            new_order_resp_type=new_order_resp_type,
            self_trade_prevention_mode=self_trade_prevention_mode,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def query_allocations_user_data(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        from_allocation_id: int | None = None,
        limit: int | None = None,
        order_id: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ApiV3MyAllocationsResponse]:
        """Retrieves allocations resulting from SOR order placement.

        Weight: 20

        Supported parameter combinations: Parameters Response symbol allocations from oldest to newest symbol +
        startTime oldest allocations since startTime symbol + endTime newest allocations until endTime symbol +
        startTime + endTime allocations within the time range symbol + fromAllocationId allocations by allocation ID
        symbol + orderId allocations related to an order starting with oldest symbol + orderId + fromAllocationId
        allocations related to an order by allocation ID

        Note: The time between startTime and endTime can't be longer than 24 hours.

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            from_allocation_id: Value sent with the request.
            limit: Default 500; max 1000.
            order_id: Order id
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Allocations resulting from SOR order placement

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_allocations_user_data(
            symbol,
            timestamp,
            signature,
            start_time=start_time,
            end_time=end_time,
            from_allocation_id=from_allocation_id,
            limit=limit,
            order_id=order_id,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def query_commission_rates_user_data(
        self, symbol: str, timestamp: int, signature: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV3AccountCommissionResponse:
        """Get current account commission rates.

        Weight: 20

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Current account commission rates.

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_commission_rates_user_data(
            symbol, timestamp, signature, request_options=request_options
        ).unwrap()

    def query_current_order_count_usage_trade(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ApiV3RateLimitOrderResponse]:
        """Displays the user's current order count usage for all intervals.

        Weight(IP): 40

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Order rate limits

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_current_order_count_usage_trade(
            timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def query_oco_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        order_list_id: int | None = None,
        orig_client_order_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV3OrderListResponse:
        """Retrieves a specific OCO based on provided optional parameters

        Weight(IP): 4

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_list_id: Order list id
            orig_client_order_id: Order id from client
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OCO details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_oco_user_data(
            timestamp,
            signature,
            order_list_id=order_list_id,
            orig_client_order_id=orig_client_order_id,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def query_open_oco_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ApiV3OpenOrderListResponse]:
        """Weight(IP): 6

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of OCO orders

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_open_oco_user_data(
            timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def query_order_user_data(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        orig_client_order_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OrderDetails:
        """Check an order's status.

        - Either ``orderId`` or ``origClientOrderId`` must be sent.
        - For some historical orders ``cummulativeQuoteQty`` will be < 0, meaning the data is not available at this
            time.

        Weight(IP): 4

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order id
            orig_client_order_id: Order id from client
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Order details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_order_user_data(
            symbol,
            timestamp,
            signature,
            order_id=order_id,
            orig_client_order_id=orig_client_order_id,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def query_prevented_matches(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        prevented_match_id: int | None = None,
        order_id: int | None = None,
        from_prevented_match_id: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ApiV3MyPreventedMatchesResponse]:
        """Displays the list of orders that were expired because of STP.

        For additional information on what a Prevented match is, as well as Self Trade Prevention (STP), please refer to
        our STP FAQ page.

        These are the combinations supported:

        * symbol + preventedMatchId
        * symbol + orderId
        * symbol + orderId + fromPreventedMatchId (limit will default to 500)
        * symbol + orderId + fromPreventedMatchId + limit

        Weight(IP):

        Case Weight If symbol is invalid: 2 Querying by preventedMatchId: 2 Querying by orderId: 20

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            prevented_match_id: Value sent with the request.
            order_id: Order id
            from_prevented_match_id: Value sent with the request.
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Order list that were expired due to STP

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_prevented_matches(
            symbol,
            timestamp,
            signature,
            prevented_match_id=prevented_match_id,
            order_id=order_id,
            from_prevented_match_id=from_prevented_match_id,
            limit=limit,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def query_all_oco_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        from_id: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ApiV3AllOrderListResponse]:
        """Retrieves all OCO based on provided optional parameters

        Weight(IP): 20

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            from_id: Trade id to fetch from. Default gets most recent trades.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of OCO orders

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_all_oco_user_data(
            timestamp,
            signature,
            from_id=from_id,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def test_new_order_trade(
        self,
        symbol: str,
        side: SideOrStr,
        type_: Type1OrStr,
        timestamp: int,
        signature: str,
        *,
        time_in_force: TimeInForceOrStr | None = None,
        quantity: float | None = None,
        quote_order_qty: float | None = None,
        price: float | None = None,
        new_client_order_id: str | None = None,
        strategy_id: int | None = None,
        strategy_type: int | None = None,
        stop_price: float | None = None,
        trailing_delta: float | None = None,
        iceberg_qty: float | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        recv_window: int | None = None,
        compute_commission_rates: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Test new order creation and signature/recvWindow long. Creates and validates a new order but does not send it
        into the matching engine.

        Weight(IP):
          - Without computeCommissionRates: ``1``
          - With computeCommissionRates: ``20``

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            type_: Order type
            timestamp: UTC timestamp in ms
            signature: Signature
            time_in_force: Order time in force
            quantity: Order quantity
            quote_order_qty: Quote quantity
            price: Order price
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            strategy_id: Value sent with the request.
            strategy_type: The value cannot be less than 1000000.
            stop_price: Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
            trailing_delta: Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
            iceberg_qty: Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.
            new_order_resp_type: Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders
                default to ACK.
            recv_window: The value cannot be greater than 60000
            compute_commission_rates: Default: false
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.test_new_order_trade(
            symbol,
            side,
            type_,
            timestamp,
            signature,
            time_in_force=time_in_force,
            quantity=quantity,
            quote_order_qty=quote_order_qty,
            price=price,
            new_client_order_id=new_client_order_id,
            strategy_id=strategy_id,
            strategy_type=strategy_type,
            stop_price=stop_price,
            trailing_delta=trailing_delta,
            iceberg_qty=iceberg_qty,
            new_order_resp_type=new_order_resp_type,
            recv_window=recv_window,
            compute_commission_rates=compute_commission_rates,
            request_options=request_options,
        ).unwrap()

    def test_new_order_using_sor_trade(
        self,
        symbol: str,
        side: SideOrStr,
        type_: Type1OrStr,
        quantity: float,
        timestamp: int,
        signature: str,
        *,
        time_in_force: TimeInForceOrStr | None = None,
        price: float | None = None,
        new_client_order_id: str | None = None,
        strategy_id: int | None = None,
        strategy_type: int | None = None,
        iceberg_qty: float | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        compute_commission_rates: bool | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Test new order creation and signature/recvWindow using smart order routing (SOR). Creates and validates a new
        order but does not send it into the matching engine.

        Weight(IP):
          - Without computeCommissionRates: ``1``
          - With computeCommissionRates: ``20``

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            type_: Order type
            quantity: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            time_in_force: Order time in force
            price: Value sent with the request.
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            strategy_id: Value sent with the request.
            strategy_type: The value cannot be less than 1000000.
            iceberg_qty: Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.
            new_order_resp_type: Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders
                default to ACK.
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            compute_commission_rates: Default: false
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Test new order

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.test_new_order_using_sor_trade(
            symbol,
            side,
            type_,
            quantity,
            timestamp,
            signature,
            time_in_force=time_in_force,
            price=price,
            new_client_order_id=new_client_order_id,
            strategy_id=strategy_id,
            strategy_type=strategy_type,
            iceberg_qty=iceberg_qty,
            new_order_resp_type=new_order_resp_type,
            self_trade_prevention_mode=self_trade_prevention_mode,
            compute_commission_rates=compute_commission_rates,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> TradeApiWithRawResponse:
        return self._with_raw_response


class AsyncTradeApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTradeApiWithRawResponse(client, server, auth)

    async def account_information_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Account:
        """Get current account information.

        Weight(IP): 20

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Account details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.account_information_user_data(
                timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def account_trade_list_user_data(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        from_id: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[MyTrade]:
        """Get trades for a specific account and symbol.

        If ``fromId`` is set, it will get id >= that ``fromId``. Otherwise most recent orders are returned.

        The time between startTime and endTime can't be longer than 24 hours. These are the supported combinations of
        all parameters:

          symbol

          symbol + orderId

          symbol + startTime

          symbol + endTime

          symbol + fromId

          symbol + startTime + endTime

          symbol+ orderId + fromId

        Weight(IP): 20

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: This can only be used in combination with symbol.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            from_id: Trade id to fetch from. Default gets most recent trades.
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of trades

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.account_trade_list_user_data(
                symbol,
                timestamp,
                signature,
                order_id=order_id,
                start_time=start_time,
                end_time=end_time,
                from_id=from_id,
                limit=limit,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def all_orders_user_data(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[OrderDetails]:
        """Get all account orders; active, canceled, or filled..

        - If ``orderId`` is set, it will get orders >= that ``orderId``. Otherwise most recent orders are returned.
        - For some historical orders ``cummulativeQuoteQty`` will be < 0, meaning the data is not available at this
            time.
        - If ``startTime`` and/or ``endTime`` provided, ``orderId`` is not required

        Weight(IP): 20

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order id
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Current open orders

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.all_orders_user_data(
                symbol,
                timestamp,
                signature,
                order_id=order_id,
                start_time=start_time,
                end_time=end_time,
                limit=limit,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def cancel_oco_trade(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        order_list_id: int | None = None,
        list_client_order_id: str | None = None,
        new_client_order_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OcoOrder:
        """Cancel an entire Order List

        Canceling an individual leg will cancel the entire OCO

        Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            order_list_id: Order list id
            list_client_order_id: A unique Id for the entire orderList
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Report on deleted OCO

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.cancel_oco_trade(
                symbol,
                timestamp,
                signature,
                order_list_id=order_list_id,
                list_client_order_id=list_client_order_id,
                new_client_order_id=new_client_order_id,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def cancel_order_trade(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        orig_client_order_id: str | None = None,
        new_client_order_id: str | None = None,
        cancel_restrictions: CancelRestrictionsOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Order:
        """Cancel an active order.

        Either ``orderId`` or ``origClientOrderId`` must be sent.

        Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order id
            orig_client_order_id: Order id from client
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            cancel_restrictions: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Cancelled order

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.cancel_order_trade(
                symbol,
                timestamp,
                signature,
                order_id=order_id,
                orig_client_order_id=orig_client_order_id,
                new_client_order_id=new_client_order_id,
                cancel_restrictions=cancel_restrictions,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def cancel_all_open_orders_on_a_symbol_trade(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ApiV3OpenOrdersResponse]:
        """Cancels all active orders on a symbol. This includes OCO orders.

        Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Cancelled orders

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.cancel_all_open_orders_on_a_symbol_trade(
                symbol, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def cancel_an_existing_order_and_send_a_new_order_trade(
        self,
        symbol: str,
        side: SideOrStr,
        type_: Type1OrStr,
        cancel_replace_mode: str,
        timestamp: int,
        signature: str,
        *,
        cancel_restrictions: CancelRestrictionsOrStr | None = None,
        time_in_force: TimeInForceOrStr | None = None,
        quantity: float | None = None,
        quote_order_qty: float | None = None,
        price: float | None = None,
        cancel_new_client_order_id: str | None = None,
        cancel_orig_client_order_id: str | None = None,
        cancel_order_id: int | None = None,
        new_client_order_id: str | None = None,
        strategy_id: int | None = None,
        strategy_type: int | None = None,
        stop_price: float | None = None,
        trailing_delta: float | None = None,
        iceberg_qty: float | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV3OrderCancelReplaceResponse:
        """Cancels an existing order and places a new order on the same symbol.

        Filters and Order Count are evaluated before the processing of the cancellation and order placement occurs.

        A new order that was not attempted (i.e. when newOrderResult: NOT_ATTEMPTED), will still increase the order
        count by 1.

        Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            type_: Order type
            cancel_replace_mode: - ``STOP_ON_FAILURE`` If the cancel request fails, the new order placement will not be
                attempted. - ``ALLOW_FAILURES`` If new order placement will be attempted even if cancel request fails.
            timestamp: UTC timestamp in ms
            signature: Signature
            cancel_restrictions: Value sent with the request.
            time_in_force: Order time in force
            quantity: Order quantity
            quote_order_qty: Quote quantity
            price: Order price
            cancel_new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            cancel_orig_client_order_id: Either the cancelOrigClientOrderId or cancelOrderId must be provided. If both
                are provided, cancelOrderId takes precedence.
            cancel_order_id: Either the cancelOrigClientOrderId or cancelOrderId must be provided. If both are provided,
                cancelOrderId takes precedence.
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            strategy_id: Value sent with the request.
            strategy_type: The value cannot be less than 1000000.
            stop_price: Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
            trailing_delta: Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
            iceberg_qty: Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.
            new_order_resp_type: Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders
                default to ACK.
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Operation details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.cancel_an_existing_order_and_send_a_new_order_trade(
                symbol,
                side,
                type_,
                cancel_replace_mode,
                timestamp,
                signature,
                cancel_restrictions=cancel_restrictions,
                time_in_force=time_in_force,
                quantity=quantity,
                quote_order_qty=quote_order_qty,
                price=price,
                cancel_new_client_order_id=cancel_new_client_order_id,
                cancel_orig_client_order_id=cancel_orig_client_order_id,
                cancel_order_id=cancel_order_id,
                new_client_order_id=new_client_order_id,
                strategy_id=strategy_id,
                strategy_type=strategy_type,
                stop_price=stop_price,
                trailing_delta=trailing_delta,
                iceberg_qty=iceberg_qty,
                new_order_resp_type=new_order_resp_type,
                self_trade_prevention_mode=self_trade_prevention_mode,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def current_open_orders_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[OrderDetails]:
        """Get all open orders on a symbol. Careful when accessing this with no symbol.

        Weight(IP):
        - ``6`` for a single symbol;
        - ``80`` when the symbol parameter is omitted;

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            symbol: Trading symbol, e.g. BNBUSDT
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Current open orders

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.current_open_orders_user_data(
                timestamp, signature, symbol=symbol, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def new_order_trade(
        self,
        symbol: str,
        side: SideOrStr,
        type_: Type1OrStr,
        timestamp: int,
        signature: str,
        *,
        time_in_force: TimeInForceOrStr | None = None,
        quantity: float | None = None,
        quote_order_qty: float | None = None,
        price: float | None = None,
        new_client_order_id: str | None = None,
        strategy_id: int | None = None,
        strategy_type: int | None = None,
        stop_price: float | None = None,
        trailing_delta: float | None = None,
        iceberg_qty: float | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV3OrderResponse:
        """Send in a new order.

        - ``LIMIT_MAKER`` are ``LIMIT`` orders that will be rejected if they would immediately match and trade as a
            taker.
        - ``STOP_LOSS`` and ``TAKE_PROFIT`` will execute a ``MARKET`` order when the ``stopPrice`` is reached.
        - Any ``LIMIT`` or ``LIMIT_MAKER`` type order can be made an iceberg order by sending an ``icebergQty``.
        - Any order with an ``icebergQty`` MUST have ``timeInForce`` set to ``GTC``.
        - ``MARKET`` orders using ``quantity`` specifies how much a user wants to buy or sell based on the market price.
        - ``MARKET`` orders using ``quoteOrderQty`` specifies the amount the user wants to spend (when buying) or
            receive (when selling) of the quote asset; the correct quantity will be determined based on the market
            liquidity and ``quoteOrderQty``.
        - ``MARKET`` orders using ``quoteOrderQty`` will not break ``LOT_SIZE`` filter rules; the order will execute a
            quantity that will have the notional value as close as possible to ``quoteOrderQty``.
        - same ``newClientOrderId`` can be accepted only when the previous one is filled, otherwise the order will be
            rejected.

        Trigger order price rules against market price for both ``MARKET`` and ``LIMIT`` versions:

        - Price above market price: ``STOP_LOSS`` ``BUY``, ``TAKE_PROFIT`` ``SELL``
        - Price below market price: ``STOP_LOSS`` ``SELL``, ``TAKE_PROFIT`` ``BUY``


        Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            type_: Order type
            timestamp: UTC timestamp in ms
            signature: Signature
            time_in_force: Order time in force
            quantity: Order quantity
            quote_order_qty: Quote quantity
            price: Order price
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            strategy_id: Value sent with the request.
            strategy_type: The value cannot be less than 1000000.
            stop_price: Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
            trailing_delta: Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
            iceberg_qty: Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.
            new_order_resp_type: Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders
                default to ACK.
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Order result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.new_order_trade(
                symbol,
                side,
                type_,
                timestamp,
                signature,
                time_in_force=time_in_force,
                quantity=quantity,
                quote_order_qty=quote_order_qty,
                price=price,
                new_client_order_id=new_client_order_id,
                strategy_id=strategy_id,
                strategy_type=strategy_type,
                stop_price=stop_price,
                trailing_delta=trailing_delta,
                iceberg_qty=iceberg_qty,
                new_order_resp_type=new_order_resp_type,
                self_trade_prevention_mode=self_trade_prevention_mode,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def new_order_list_oto_trade(
        self,
        symbol: str,
        working_type: WorkingTypeOrStr,
        working_side: WorkingSideOrStr,
        working_price: float,
        working_quantity: float,
        working_iceberg_qty: float,
        pending_type: PendingTypeOrStr,
        pending_side: PendingSideOrStr,
        pending_quantity: float,
        timestamp: int,
        signature: str,
        *,
        list_client_order_id: str | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        working_client_order_id: str | None = None,
        working_time_in_force: WorkingTimeInForceOrStr | None = None,
        working_strategy_id: float | None = None,
        working_strategy_type: int | None = None,
        pending_client_order_id: str | None = None,
        pending_price: float | None = None,
        pending_stop_price: float | None = None,
        pending_trailing_delta: float | None = None,
        pending_iceberg_qty: float | None = None,
        pending_time_in_force: PendingTimeInForceOrStr | None = None,
        pending_strategy_id: float | None = None,
        pending_strategy_type: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV3OrderListOtoResponse:
        """Places an ``OTO``.
        - An ``OTO`` (One-Triggers-the-Other) is an order list comprised of 2 orders.
        - The first order is called the working order and must be ``LIMIT`` or ``LIMIT_MAKER``. Initially, only the
            working order goes on the order book.
        - The second order is called the pending order. It can be any order type except for ``MARKET`` orders using
            parameter ``quoteOrderQty``. The pending order is only placed on the order book when the working order gets
            fully filled.
        - If either the working order or the pending order is cancelled individually, the other order in the order list
            will also be canceled or expired.
        - When the order list is placed, if the working order gets immediately fully filled, the placement response will
            show the working order as ``FILLED`` but the pending order will still appear as ``PENDING_NEW``. You need to
            query the status of the pending order again to see its updated status.
        - OTOs add 2 orders to the unfilled order count, ``EXCHANGE_MAX_NUM_ORDERS`` filter and ``MAX_NUM_ORDERS``
            filter.

        Weight: 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            working_type: Supported values: LIMIT,LIMIT_MAKER
            working_side: BUY,SELL
            working_price: Value sent with the request.
            working_quantity: Sets the quantity for the working order.
            working_iceberg_qty: This can only be used if workingTimeInForce is GTC.
            pending_type: Supported values: Order Types Note that MARKET orders using quoteOrderQty are not supported.
            pending_side: BUY,SELL
            pending_quantity: Sets the quantity for the pending order.
            timestamp: UTC timestamp in ms
            signature: Signature
            list_client_order_id: Arbitrary unique ID among open order lists. Automatically generated if not sent. A new
                order list with the same ``listClientOrderId`` is accepted only when the previous one is filled or
                completely expired. ``listClientOrderId`` is distinct from the ``workingClientOrderId`` and the
                ``pendingClientOrderId``.
            new_order_resp_type: Set the response JSON.
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            working_client_order_id: Arbitrary unique ID among open orders for the working order. Automatically
                generated if not sent.
            working_time_in_force: GTC, IOC, FOK
            working_strategy_id: Arbitrary numeric value identifying the working order within an order strategy.
            working_strategy_type: Arbitrary numeric value identifying the working order strategy. Values smaller than
                1000000 are reserved and cannot be used.
            pending_client_order_id: Arbitrary unique ID among open orders for the pending order. Automatically
                generated if not sent.
            pending_price: Value sent with the request.
            pending_stop_price: Value sent with the request.
            pending_trailing_delta: Value sent with the request.
            pending_iceberg_qty: This can only be used if pendingTimeInForce is GTC.
            pending_time_in_force: GTC, IOC, FOK
            pending_strategy_id: Arbitrary numeric value identifying the pending order within an order strategy.
            pending_strategy_type: Arbitrary numeric value identifying the pending order strategy. Values smaller than
                1000000 are reserved and cannot be used.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            New OTO details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.new_order_list_oto_trade(
                symbol,
                working_type,
                working_side,
                working_price,
                working_quantity,
                working_iceberg_qty,
                pending_type,
                pending_side,
                pending_quantity,
                timestamp,
                signature,
                list_client_order_id=list_client_order_id,
                new_order_resp_type=new_order_resp_type,
                self_trade_prevention_mode=self_trade_prevention_mode,
                working_client_order_id=working_client_order_id,
                working_time_in_force=working_time_in_force,
                working_strategy_id=working_strategy_id,
                working_strategy_type=working_strategy_type,
                pending_client_order_id=pending_client_order_id,
                pending_price=pending_price,
                pending_stop_price=pending_stop_price,
                pending_trailing_delta=pending_trailing_delta,
                pending_iceberg_qty=pending_iceberg_qty,
                pending_time_in_force=pending_time_in_force,
                pending_strategy_id=pending_strategy_id,
                pending_strategy_type=pending_strategy_type,
                request_options=request_options,
            )
        ).unwrap()

    async def new_order_list_otoco_trade(
        self,
        symbol: str,
        working_type: WorkingTypeOrStr,
        working_side: WorkingSideOrStr,
        working_price: float,
        working_quantity: float,
        working_iceberg_qty: float,
        pending_side: PendingSideOrStr,
        pending_quantity: float,
        pending_above_type: PendingAboveTypeOrStr,
        timestamp: int,
        signature: str,
        *,
        list_client_order_id: str | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        working_client_order_id: str | None = None,
        working_time_in_force: WorkingTimeInForceOrStr | None = None,
        working_strategy_id: float | None = None,
        working_strategy_type: int | None = None,
        pending_above_client_order_id: str | None = None,
        pending_above_price: float | None = None,
        pending_above_stop_price: float | None = None,
        pending_above_trailing_delta: float | None = None,
        pending_above_iceberg_qty: float | None = None,
        pending_above_time_in_force: PendingAboveTimeInForceOrStr | None = None,
        pending_above_strategy_id: float | None = None,
        pending_above_strategy_type: int | None = None,
        pending_below_type: PendingBelowTypeOrStr | None = None,
        pending_below_client_order_id: str | None = None,
        pending_below_price: float | None = None,
        pending_below_stop_price: float | None = None,
        pending_below_trailing_delta: float | None = None,
        pending_below_iceberg_qty: float | None = None,
        pending_below_time_in_force: PendingBelowTimeInForceOrStr | None = None,
        pending_below_strategy_id: float | None = None,
        pending_below_strategy_type: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV3OrderListOtocoResponse:
        """Place an ``OTOCO``.
        - An ``OTOCO`` (One-Triggers-One-Cancels-the-Other) is an order list comprised of 3 orders.
        - The first order is called the working order and must be ``LIMIT`` or ``LIMIT_MAKER``. Initially, only the
            working order goes on the order book.
          - The behavior of the working order is the same as the ``OTO``.
        - ``OTOCO`` has 2 pending orders (pending above and pending below), forming an ``OCO`` pair. The pending orders
            are only placed on the order book when the working order gets fully filled.
          - The rules of the pending above and pending below follow the same rules as the Order List ``OCO``.
        - OTOCOs add 3 orders against the unfilled order count, ``EXCHANGE_MAX_NUM_ORDERS`` filter, and
            ``MAX_NUM_ORDERS`` filter.

        Weight: 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            working_type: Supported values: LIMIT,LIMIT_MAKER
            working_side: BUY,SELL
            working_price: Value sent with the request.
            working_quantity: Sets the quantity for the working order.
            working_iceberg_qty: This can only be used if workingTimeInForce is GTC.
            pending_side: BUY,SELL
            pending_quantity: Sets the quantity for the pending order.
            pending_above_type: Supported values: LIMIT_MAKER, STOP_LOSS, and STOP_LOSS_LIMIT
            timestamp: UTC timestamp in ms
            signature: Signature
            list_client_order_id: Arbitrary unique ID among open order lists. Automatically generated if not sent. A new
                order list with the same ``listClientOrderId`` is accepted only when the previous one is filled or
                completely expired. ``listClientOrderId`` is distinct from the ``workingClientOrderId`` and the
                ``pendingClientOrderId``.
            new_order_resp_type: Set the response JSON.
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            working_client_order_id: Arbitrary unique ID among open orders for the working order. Automatically
                generated if not sent.
            working_time_in_force: GTC, IOC, FOK
            working_strategy_id: Arbitrary numeric value identifying the working order within an order strategy.
            working_strategy_type: Arbitrary numeric value identifying the working order strategy. Values smaller than
                1000000 are reserved and cannot be used.
            pending_above_client_order_id: Arbitrary unique ID among open orders for the pending above order.
                Automatically generated if not sent.
            pending_above_price: Value sent with the request.
            pending_above_stop_price: Value sent with the request.
            pending_above_trailing_delta: Value sent with the request.
            pending_above_iceberg_qty: This can only be used if pendingAboveTimeInForce is GTC.
            pending_above_time_in_force: Value sent with the request.
            pending_above_strategy_id: Arbitrary numeric value identifying the pending above order within an order
                strategy.
            pending_above_strategy_type: Arbitrary numeric value identifying the pending above order strategy. Values
                smaller than 1000000 are reserved and cannot be used.
            pending_below_type: Supported values: LIMIT_MAKER, STOP_LOSS, and STOP_LOSS_LIMIT
            pending_below_client_order_id: Arbitrary unique ID among open orders for the pending below order.
                Automatically generated if not sent.
            pending_below_price: Value sent with the request.
            pending_below_stop_price: Value sent with the request.
            pending_below_trailing_delta: Value sent with the request.
            pending_below_iceberg_qty: This can only be used if pendingBelowTimeInForce is GTC.
            pending_below_time_in_force: Value sent with the request.
            pending_below_strategy_id: Arbitrary numeric value identifying the pending below order within an order
                strategy.
            pending_below_strategy_type: Arbitrary numeric value identifying the pending below order strategy. Values
                smaller than 1000000 are reserved and cannot be used.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            New OTOCO details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.new_order_list_otoco_trade(
                symbol,
                working_type,
                working_side,
                working_price,
                working_quantity,
                working_iceberg_qty,
                pending_side,
                pending_quantity,
                pending_above_type,
                timestamp,
                signature,
                list_client_order_id=list_client_order_id,
                new_order_resp_type=new_order_resp_type,
                self_trade_prevention_mode=self_trade_prevention_mode,
                working_client_order_id=working_client_order_id,
                working_time_in_force=working_time_in_force,
                working_strategy_id=working_strategy_id,
                working_strategy_type=working_strategy_type,
                pending_above_client_order_id=pending_above_client_order_id,
                pending_above_price=pending_above_price,
                pending_above_stop_price=pending_above_stop_price,
                pending_above_trailing_delta=pending_above_trailing_delta,
                pending_above_iceberg_qty=pending_above_iceberg_qty,
                pending_above_time_in_force=pending_above_time_in_force,
                pending_above_strategy_id=pending_above_strategy_id,
                pending_above_strategy_type=pending_above_strategy_type,
                pending_below_type=pending_below_type,
                pending_below_client_order_id=pending_below_client_order_id,
                pending_below_price=pending_below_price,
                pending_below_stop_price=pending_below_stop_price,
                pending_below_trailing_delta=pending_below_trailing_delta,
                pending_below_iceberg_qty=pending_below_iceberg_qty,
                pending_below_time_in_force=pending_below_time_in_force,
                pending_below_strategy_id=pending_below_strategy_id,
                pending_below_strategy_type=pending_below_strategy_type,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def new_order_list_oco_trade(
        self,
        symbol: str,
        side: SideOrStr,
        quantity: float,
        above_type: str,
        below_type: str,
        timestamp: int,
        signature: str,
        *,
        list_client_order_id: str | None = None,
        above_client_order_id: str | None = None,
        above_iceberg_qty: float | None = None,
        above_price: float | None = None,
        above_stop_price: float | None = None,
        above_trailing_delta: float | None = None,
        above_time_in_force: AboveTimeInForceOrStr | None = None,
        above_strategy_id: float | None = None,
        above_strategy_type: int | None = None,
        below_client_order_id: str | None = None,
        below_iceberg_qty: float | None = None,
        below_price: float | None = None,
        below_stop_price: float | None = None,
        below_trailing_delta: float | None = None,
        below_time_in_force: BelowTimeInForceOrStr | None = None,
        below_strategy_id: float | None = None,
        below_strategy_type: int | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV3OrderListOcoResponse:
        """Send in an one-cancels-the-other (OCO) pair, where activation of one order immediately cancels the other.

        - An ``OCO`` has 2 orders called the above order and below order.
        - One of the orders must be a ``LIMIT_MAKER`` order and the other must be ``STOP_LOSS`` or``STOP_LOSS_LIMIT``
            order.
        - Price restrictions:
            - If the ``OCO`` is on the ``SELL`` side: ``LIMIT_MAKER`` price > Last Traded Price > stopPrice
            - If the ``OCO`` is on the ``BUY`` side: ``LIMIT_MAKER`` price < Last Traded Price < stopPrice
        - OCOs add 2 orders to the unfilled order count, ``EXCHANGE_MAX_ORDERS`` filter, and the ``MAX_NUM_ORDERS``
            filter.

        Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            quantity: Value sent with the request.
            above_type: Supported values : ``STOP_LOSS_LIMIT``, ``STOP_LOSS``, ``LIMIT_MAKER``
            below_type: Supported values : ``STOP_LOSS_LIMIT``, ``STOP_LOSS``, ``LIMIT_MAKER``
            timestamp: UTC timestamp in ms
            signature: Signature
            list_client_order_id: Arbitrary unique ID among open order lists. Automatically generated if not sent. A new
                order list with the same ``listClientOrderId`` is accepted only when the previous one is filled or
                completely expired. ``listClientOrderId`` is distinct from the ``aboveClientOrderId`` and the
                ``belowCLientOrderId``.
            above_client_order_id: Arbitrary unique ID among open orders for the above order. Automatically generated if
                not sent
            above_iceberg_qty: Note that this can only be used if ``aboveTimeInForce`` is ``GTC``.
            above_price: Value sent with the request.
            above_stop_price: Can be used if ``aboveType`` is ``STOP_LOSS`` or ``STOP_LOSS_LIMIT``. Either
                ``aboveStopPrice`` or ``aboveTrailingDelta`` or both, must be specified.
            above_trailing_delta: Value sent with the request.
            above_time_in_force: Required if the ``aboveType`` is ``STOP_LOSS_LIMIT``.
            above_strategy_id: Arbitrary numeric value identifying the above order within an order strategy.
            above_strategy_type: Arbitrary numeric value identifying the above order strategy. Values smaller than
                1000000 are reserved and cannot be used.
            below_client_order_id: Arbitrary unique ID among open orders for the below order. Automatically generated if
                not sent
            below_iceberg_qty: Note that this can only be used if ``belowTimeInForce`` is ``GTC``.
            below_price: Can be used if ``belowType`` is ``STOP_LOSS_LIMIT`` or ``LIMIT_MAKER`` to specify the limit
                price.
            below_stop_price: Can be used if ``belowType`` is ``STOP_LOSS`` or ``STOP_LOSS_LIMIT``. Either
                ``belowStopPrice`` or ``belowTrailingDelta`` or both, must be specified.
            below_trailing_delta: Value sent with the request.
            below_time_in_force: Required if the ``belowType`` is ``STOP_LOSS_LIMIT``.
            below_strategy_id: Arbitrary numeric value identifying the below order within an order strategy.
            below_strategy_type: Arbitrary numeric value identifying the below order strategy. Values smaller than
                1000000 are reserved and cannot be used.
            new_order_resp_type: Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders
                default to ACK.
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            New OCO details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.new_order_list_oco_trade(
                symbol,
                side,
                quantity,
                above_type,
                below_type,
                timestamp,
                signature,
                list_client_order_id=list_client_order_id,
                above_client_order_id=above_client_order_id,
                above_iceberg_qty=above_iceberg_qty,
                above_price=above_price,
                above_stop_price=above_stop_price,
                above_trailing_delta=above_trailing_delta,
                above_time_in_force=above_time_in_force,
                above_strategy_id=above_strategy_id,
                above_strategy_type=above_strategy_type,
                below_client_order_id=below_client_order_id,
                below_iceberg_qty=below_iceberg_qty,
                below_price=below_price,
                below_stop_price=below_stop_price,
                below_trailing_delta=below_trailing_delta,
                below_time_in_force=below_time_in_force,
                below_strategy_id=below_strategy_id,
                below_strategy_type=below_strategy_type,
                new_order_resp_type=new_order_resp_type,
                self_trade_prevention_mode=self_trade_prevention_mode,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def new_order_using_sor_trade(
        self,
        symbol: str,
        side: SideOrStr,
        type_: Type1OrStr,
        quantity: float,
        timestamp: int,
        signature: str,
        *,
        time_in_force: TimeInForceOrStr | None = None,
        price: float | None = None,
        new_client_order_id: str | None = None,
        strategy_id: int | None = None,
        strategy_type: int | None = None,
        iceberg_qty: float | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV3SorOrderResponse:
        """Weight(IP): 6

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            type_: Order type
            quantity: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            time_in_force: Order time in force
            price: Value sent with the request.
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            strategy_id: Value sent with the request.
            strategy_type: The value cannot be less than 1000000.
            iceberg_qty: Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.
            new_order_resp_type: Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders
                default to ACK.
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            New order details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.new_order_using_sor_trade(
                symbol,
                side,
                type_,
                quantity,
                timestamp,
                signature,
                time_in_force=time_in_force,
                price=price,
                new_client_order_id=new_client_order_id,
                strategy_id=strategy_id,
                strategy_type=strategy_type,
                iceberg_qty=iceberg_qty,
                new_order_resp_type=new_order_resp_type,
                self_trade_prevention_mode=self_trade_prevention_mode,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def query_allocations_user_data(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        from_allocation_id: int | None = None,
        limit: int | None = None,
        order_id: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ApiV3MyAllocationsResponse]:
        """Retrieves allocations resulting from SOR order placement.

        Weight: 20

        Supported parameter combinations: Parameters Response symbol allocations from oldest to newest symbol +
        startTime oldest allocations since startTime symbol + endTime newest allocations until endTime symbol +
        startTime + endTime allocations within the time range symbol + fromAllocationId allocations by allocation ID
        symbol + orderId allocations related to an order starting with oldest symbol + orderId + fromAllocationId
        allocations related to an order by allocation ID

        Note: The time between startTime and endTime can't be longer than 24 hours.

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            from_allocation_id: Value sent with the request.
            limit: Default 500; max 1000.
            order_id: Order id
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Allocations resulting from SOR order placement

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_allocations_user_data(
                symbol,
                timestamp,
                signature,
                start_time=start_time,
                end_time=end_time,
                from_allocation_id=from_allocation_id,
                limit=limit,
                order_id=order_id,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def query_commission_rates_user_data(
        self, symbol: str, timestamp: int, signature: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV3AccountCommissionResponse:
        """Get current account commission rates.

        Weight: 20

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Current account commission rates.

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_commission_rates_user_data(
                symbol, timestamp, signature, request_options=request_options
            )
        ).unwrap()

    async def query_current_order_count_usage_trade(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ApiV3RateLimitOrderResponse]:
        """Displays the user's current order count usage for all intervals.

        Weight(IP): 40

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Order rate limits

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_current_order_count_usage_trade(
                timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def query_oco_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        order_list_id: int | None = None,
        orig_client_order_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV3OrderListResponse:
        """Retrieves a specific OCO based on provided optional parameters

        Weight(IP): 4

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_list_id: Order list id
            orig_client_order_id: Order id from client
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OCO details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_oco_user_data(
                timestamp,
                signature,
                order_list_id=order_list_id,
                orig_client_order_id=orig_client_order_id,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def query_open_oco_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ApiV3OpenOrderListResponse]:
        """Weight(IP): 6

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of OCO orders

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_open_oco_user_data(
                timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def query_order_user_data(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        orig_client_order_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OrderDetails:
        """Check an order's status.

        - Either ``orderId`` or ``origClientOrderId`` must be sent.
        - For some historical orders ``cummulativeQuoteQty`` will be < 0, meaning the data is not available at this
            time.

        Weight(IP): 4

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order id
            orig_client_order_id: Order id from client
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Order details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_order_user_data(
                symbol,
                timestamp,
                signature,
                order_id=order_id,
                orig_client_order_id=orig_client_order_id,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def query_prevented_matches(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        prevented_match_id: int | None = None,
        order_id: int | None = None,
        from_prevented_match_id: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ApiV3MyPreventedMatchesResponse]:
        """Displays the list of orders that were expired because of STP.

        For additional information on what a Prevented match is, as well as Self Trade Prevention (STP), please refer to
        our STP FAQ page.

        These are the combinations supported:

        * symbol + preventedMatchId
        * symbol + orderId
        * symbol + orderId + fromPreventedMatchId (limit will default to 500)
        * symbol + orderId + fromPreventedMatchId + limit

        Weight(IP):

        Case Weight If symbol is invalid: 2 Querying by preventedMatchId: 2 Querying by orderId: 20

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            prevented_match_id: Value sent with the request.
            order_id: Order id
            from_prevented_match_id: Value sent with the request.
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Order list that were expired due to STP

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_prevented_matches(
                symbol,
                timestamp,
                signature,
                prevented_match_id=prevented_match_id,
                order_id=order_id,
                from_prevented_match_id=from_prevented_match_id,
                limit=limit,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def query_all_oco_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        from_id: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ApiV3AllOrderListResponse]:
        """Retrieves all OCO based on provided optional parameters

        Weight(IP): 20

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            from_id: Trade id to fetch from. Default gets most recent trades.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of OCO orders

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_all_oco_user_data(
                timestamp,
                signature,
                from_id=from_id,
                start_time=start_time,
                end_time=end_time,
                limit=limit,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def test_new_order_trade(
        self,
        symbol: str,
        side: SideOrStr,
        type_: Type1OrStr,
        timestamp: int,
        signature: str,
        *,
        time_in_force: TimeInForceOrStr | None = None,
        quantity: float | None = None,
        quote_order_qty: float | None = None,
        price: float | None = None,
        new_client_order_id: str | None = None,
        strategy_id: int | None = None,
        strategy_type: int | None = None,
        stop_price: float | None = None,
        trailing_delta: float | None = None,
        iceberg_qty: float | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        recv_window: int | None = None,
        compute_commission_rates: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Test new order creation and signature/recvWindow long. Creates and validates a new order but does not send it
        into the matching engine.

        Weight(IP):
          - Without computeCommissionRates: ``1``
          - With computeCommissionRates: ``20``

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            type_: Order type
            timestamp: UTC timestamp in ms
            signature: Signature
            time_in_force: Order time in force
            quantity: Order quantity
            quote_order_qty: Quote quantity
            price: Order price
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            strategy_id: Value sent with the request.
            strategy_type: The value cannot be less than 1000000.
            stop_price: Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
            trailing_delta: Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
            iceberg_qty: Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.
            new_order_resp_type: Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders
                default to ACK.
            recv_window: The value cannot be greater than 60000
            compute_commission_rates: Default: false
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.test_new_order_trade(
                symbol,
                side,
                type_,
                timestamp,
                signature,
                time_in_force=time_in_force,
                quantity=quantity,
                quote_order_qty=quote_order_qty,
                price=price,
                new_client_order_id=new_client_order_id,
                strategy_id=strategy_id,
                strategy_type=strategy_type,
                stop_price=stop_price,
                trailing_delta=trailing_delta,
                iceberg_qty=iceberg_qty,
                new_order_resp_type=new_order_resp_type,
                recv_window=recv_window,
                compute_commission_rates=compute_commission_rates,
                request_options=request_options,
            )
        ).unwrap()

    async def test_new_order_using_sor_trade(
        self,
        symbol: str,
        side: SideOrStr,
        type_: Type1OrStr,
        quantity: float,
        timestamp: int,
        signature: str,
        *,
        time_in_force: TimeInForceOrStr | None = None,
        price: float | None = None,
        new_client_order_id: str | None = None,
        strategy_id: int | None = None,
        strategy_type: int | None = None,
        iceberg_qty: float | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        compute_commission_rates: bool | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Test new order creation and signature/recvWindow using smart order routing (SOR). Creates and validates a new
        order but does not send it into the matching engine.

        Weight(IP):
          - Without computeCommissionRates: ``1``
          - With computeCommissionRates: ``20``

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            type_: Order type
            quantity: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            time_in_force: Order time in force
            price: Value sent with the request.
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            strategy_id: Value sent with the request.
            strategy_type: The value cannot be less than 1000000.
            iceberg_qty: Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.
            new_order_resp_type: Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders
                default to ACK.
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            compute_commission_rates: Default: false
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Test new order

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.test_new_order_using_sor_trade(
                symbol,
                side,
                type_,
                quantity,
                timestamp,
                signature,
                time_in_force=time_in_force,
                price=price,
                new_client_order_id=new_client_order_id,
                strategy_id=strategy_id,
                strategy_type=strategy_type,
                iceberg_qty=iceberg_qty,
                new_order_resp_type=new_order_resp_type,
                self_trade_prevention_mode=self_trade_prevention_mode,
                compute_commission_rates=compute_commission_rates,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTradeApiWithRawResponse:
        return self._with_raw_response


class TradeApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def account_information_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Account, AccountInformationUserDataErrorBody]:
        """Get current account information.

        Weight(IP): 20

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/account"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[Account],
            error_mapper=account_information_user_data_error_mapper,
            request_options=request_options,
        )

    def account_trade_list_user_data(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        from_id: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[MyTrade], AccountTradeListUserDataErrorBody]:
        """Get trades for a specific account and symbol.

        If ``fromId`` is set, it will get id >= that ``fromId``. Otherwise most recent orders are returned.

        The time between startTime and endTime can't be longer than 24 hours. These are the supported combinations of
        all parameters:

          symbol

          symbol + orderId

          symbol + startTime

          symbol + endTime

          symbol + fromId

          symbol + startTime + endTime

          symbol+ orderId + fromId

        Weight(IP): 20

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: This can only be used in combination with symbol.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            from_id: Trade id to fetch from. Default gets most recent trades.
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/myTrades"),
            query_params=[
                param[str]("symbol", symbol),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("orderId", order_id),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("fromId", from_id),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[MyTrade]],
            error_mapper=account_trade_list_user_data_error_mapper,
            request_options=request_options,
        )

    def all_orders_user_data(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[OrderDetails], AllOrdersUserDataErrorBody]:
        """Get all account orders; active, canceled, or filled..

        - If ``orderId`` is set, it will get orders >= that ``orderId``. Otherwise most recent orders are returned.
        - For some historical orders ``cummulativeQuoteQty`` will be < 0, meaning the data is not available at this
            time.
        - If ``startTime`` and/or ``endTime`` provided, ``orderId`` is not required

        Weight(IP): 20

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order id
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/allOrders"),
            query_params=[
                param[str]("symbol", symbol),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("orderId", order_id),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[OrderDetails]],
            error_mapper=all_orders_user_data_error_mapper,
            request_options=request_options,
        )

    def cancel_oco_trade(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        order_list_id: int | None = None,
        list_client_order_id: str | None = None,
        new_client_order_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OcoOrder, CancelOcoTradeErrorBody]:
        """Cancel an entire Order List

        Canceling an individual leg will cancel the entire OCO

        Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            order_list_id: Order list id
            list_client_order_id: A unique Id for the entire orderList
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/api/v3/orderList"),
            query_params=[
                param[str]("symbol", symbol),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("orderListId", order_list_id),
                param[str | None]("listClientOrderId", list_client_order_id),
                param[str | None]("newClientOrderId", new_client_order_id),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[OcoOrder],
            error_mapper=cancel_oco_trade_error_mapper,
            request_options=request_options,
        )

    def cancel_order_trade(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        orig_client_order_id: str | None = None,
        new_client_order_id: str | None = None,
        cancel_restrictions: CancelRestrictionsOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Order, CancelOrderTradeErrorBody]:
        """Cancel an active order.

        Either ``orderId`` or ``origClientOrderId`` must be sent.

        Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order id
            orig_client_order_id: Order id from client
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            cancel_restrictions: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/api/v3/order"),
            query_params=[
                param[str]("symbol", symbol),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("orderId", order_id),
                param[str | None]("origClientOrderId", orig_client_order_id),
                param[str | None]("newClientOrderId", new_client_order_id),
                param[CancelRestrictionsOrStr | None]("cancelRestrictions", cancel_restrictions),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[Order],
            error_mapper=cancel_order_trade_error_mapper,
            request_options=request_options,
        )

    def cancel_all_open_orders_on_a_symbol_trade(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ApiV3OpenOrdersResponse], CancelAllOpenOrdersOnASymbolTradeErrorBody]:
        """Cancels all active orders on a symbol. This includes OCO orders.

        Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/api/v3/openOrders"),
            query_params=[
                param[str]("symbol", symbol),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[ApiV3OpenOrdersResponse]],
            error_mapper=cancel_all_open_orders_on_a_symbol_trade_error_mapper,
            request_options=request_options,
        )

    def cancel_an_existing_order_and_send_a_new_order_trade(
        self,
        symbol: str,
        side: SideOrStr,
        type_: Type1OrStr,
        cancel_replace_mode: str,
        timestamp: int,
        signature: str,
        *,
        cancel_restrictions: CancelRestrictionsOrStr | None = None,
        time_in_force: TimeInForceOrStr | None = None,
        quantity: float | None = None,
        quote_order_qty: float | None = None,
        price: float | None = None,
        cancel_new_client_order_id: str | None = None,
        cancel_orig_client_order_id: str | None = None,
        cancel_order_id: int | None = None,
        new_client_order_id: str | None = None,
        strategy_id: int | None = None,
        strategy_type: int | None = None,
        stop_price: float | None = None,
        trailing_delta: float | None = None,
        iceberg_qty: float | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV3OrderCancelReplaceResponse, CancelAnExistingOrderAndSendANewOrderTradeErrorBody]:
        """Cancels an existing order and places a new order on the same symbol.

        Filters and Order Count are evaluated before the processing of the cancellation and order placement occurs.

        A new order that was not attempted (i.e. when newOrderResult: NOT_ATTEMPTED), will still increase the order
        count by 1.

        Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            type_: Order type
            cancel_replace_mode: - ``STOP_ON_FAILURE`` If the cancel request fails, the new order placement will not be
                attempted. - ``ALLOW_FAILURES`` If new order placement will be attempted even if cancel request fails.
            timestamp: UTC timestamp in ms
            signature: Signature
            cancel_restrictions: Value sent with the request.
            time_in_force: Order time in force
            quantity: Order quantity
            quote_order_qty: Quote quantity
            price: Order price
            cancel_new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            cancel_orig_client_order_id: Either the cancelOrigClientOrderId or cancelOrderId must be provided. If both
                are provided, cancelOrderId takes precedence.
            cancel_order_id: Either the cancelOrigClientOrderId or cancelOrderId must be provided. If both are provided,
                cancelOrderId takes precedence.
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            strategy_id: Value sent with the request.
            strategy_type: The value cannot be less than 1000000.
            stop_price: Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
            trailing_delta: Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
            iceberg_qty: Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.
            new_order_resp_type: Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders
                default to ACK.
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/v3/order/cancelReplace"),
            query_params=[
                param[str]("symbol", symbol),
                param[SideOrStr]("side", side),
                param[Type1OrStr]("type", type_),
                param[str]("cancelReplaceMode", cancel_replace_mode),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[CancelRestrictionsOrStr | None]("cancelRestrictions", cancel_restrictions),
                param[TimeInForceOrStr | None]("timeInForce", time_in_force),
                param[float | None]("quantity", quantity),
                param[float | None]("quoteOrderQty", quote_order_qty),
                param[float | None]("price", price),
                param[str | None]("cancelNewClientOrderId", cancel_new_client_order_id),
                param[str | None]("cancelOrigClientOrderId", cancel_orig_client_order_id),
                param[int | None]("cancelOrderId", cancel_order_id),
                param[str | None]("newClientOrderId", new_client_order_id),
                param[int | None]("strategyId", strategy_id),
                param[int | None]("strategyType", strategy_type),
                param[float | None]("stopPrice", stop_price),
                param[float | None]("trailingDelta", trailing_delta),
                param[float | None]("icebergQty", iceberg_qty),
                param[NewOrderRespTypeOrStr | None]("newOrderRespType", new_order_resp_type),
                param[SelfTradePreventionModeOrStr | None]("selfTradePreventionMode", self_trade_prevention_mode),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ApiV3OrderCancelReplaceResponse],
            error_mapper=cancel_an_existing_order_and_send_a_new_order_trade_error_mapper,
            request_options=request_options,
        )

    def current_open_orders_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[OrderDetails], CurrentOpenOrdersUserDataErrorBody]:
        """Get all open orders on a symbol. Careful when accessing this with no symbol.

        Weight(IP):
        - ``6`` for a single symbol;
        - ``80`` when the symbol parameter is omitted;

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            symbol: Trading symbol, e.g. BNBUSDT
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/openOrders"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("symbol", symbol),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[OrderDetails]],
            error_mapper=current_open_orders_user_data_error_mapper,
            request_options=request_options,
        )

    def new_order_trade(
        self,
        symbol: str,
        side: SideOrStr,
        type_: Type1OrStr,
        timestamp: int,
        signature: str,
        *,
        time_in_force: TimeInForceOrStr | None = None,
        quantity: float | None = None,
        quote_order_qty: float | None = None,
        price: float | None = None,
        new_client_order_id: str | None = None,
        strategy_id: int | None = None,
        strategy_type: int | None = None,
        stop_price: float | None = None,
        trailing_delta: float | None = None,
        iceberg_qty: float | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV3OrderResponse, NewOrderTradeErrorBody]:
        """Send in a new order.

        - ``LIMIT_MAKER`` are ``LIMIT`` orders that will be rejected if they would immediately match and trade as a
            taker.
        - ``STOP_LOSS`` and ``TAKE_PROFIT`` will execute a ``MARKET`` order when the ``stopPrice`` is reached.
        - Any ``LIMIT`` or ``LIMIT_MAKER`` type order can be made an iceberg order by sending an ``icebergQty``.
        - Any order with an ``icebergQty`` MUST have ``timeInForce`` set to ``GTC``.
        - ``MARKET`` orders using ``quantity`` specifies how much a user wants to buy or sell based on the market price.
        - ``MARKET`` orders using ``quoteOrderQty`` specifies the amount the user wants to spend (when buying) or
            receive (when selling) of the quote asset; the correct quantity will be determined based on the market
            liquidity and ``quoteOrderQty``.
        - ``MARKET`` orders using ``quoteOrderQty`` will not break ``LOT_SIZE`` filter rules; the order will execute a
            quantity that will have the notional value as close as possible to ``quoteOrderQty``.
        - same ``newClientOrderId`` can be accepted only when the previous one is filled, otherwise the order will be
            rejected.

        Trigger order price rules against market price for both ``MARKET`` and ``LIMIT`` versions:

        - Price above market price: ``STOP_LOSS`` ``BUY``, ``TAKE_PROFIT`` ``SELL``
        - Price below market price: ``STOP_LOSS`` ``SELL``, ``TAKE_PROFIT`` ``BUY``


        Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            type_: Order type
            timestamp: UTC timestamp in ms
            signature: Signature
            time_in_force: Order time in force
            quantity: Order quantity
            quote_order_qty: Quote quantity
            price: Order price
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            strategy_id: Value sent with the request.
            strategy_type: The value cannot be less than 1000000.
            stop_price: Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
            trailing_delta: Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
            iceberg_qty: Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.
            new_order_resp_type: Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders
                default to ACK.
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/v3/order"),
            query_params=[
                param[str]("symbol", symbol),
                param[SideOrStr]("side", side),
                param[Type1OrStr]("type", type_),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[TimeInForceOrStr | None]("timeInForce", time_in_force),
                param[float | None]("quantity", quantity),
                param[float | None]("quoteOrderQty", quote_order_qty),
                param[float | None]("price", price),
                param[str | None]("newClientOrderId", new_client_order_id),
                param[int | None]("strategyId", strategy_id),
                param[int | None]("strategyType", strategy_type),
                param[float | None]("stopPrice", stop_price),
                param[float | None]("trailingDelta", trailing_delta),
                param[float | None]("icebergQty", iceberg_qty),
                param[NewOrderRespTypeOrStr | None]("newOrderRespType", new_order_resp_type),
                param[SelfTradePreventionModeOrStr | None]("selfTradePreventionMode", self_trade_prevention_mode),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ApiV3OrderResponse],
            error_mapper=new_order_trade_error_mapper,
            request_options=request_options,
        )

    def new_order_list_oto_trade(
        self,
        symbol: str,
        working_type: WorkingTypeOrStr,
        working_side: WorkingSideOrStr,
        working_price: float,
        working_quantity: float,
        working_iceberg_qty: float,
        pending_type: PendingTypeOrStr,
        pending_side: PendingSideOrStr,
        pending_quantity: float,
        timestamp: int,
        signature: str,
        *,
        list_client_order_id: str | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        working_client_order_id: str | None = None,
        working_time_in_force: WorkingTimeInForceOrStr | None = None,
        working_strategy_id: float | None = None,
        working_strategy_type: int | None = None,
        pending_client_order_id: str | None = None,
        pending_price: float | None = None,
        pending_stop_price: float | None = None,
        pending_trailing_delta: float | None = None,
        pending_iceberg_qty: float | None = None,
        pending_time_in_force: PendingTimeInForceOrStr | None = None,
        pending_strategy_id: float | None = None,
        pending_strategy_type: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV3OrderListOtoResponse, NewOrderListOtoTradeErrorBody]:
        """Places an ``OTO``.
        - An ``OTO`` (One-Triggers-the-Other) is an order list comprised of 2 orders.
        - The first order is called the working order and must be ``LIMIT`` or ``LIMIT_MAKER``. Initially, only the
            working order goes on the order book.
        - The second order is called the pending order. It can be any order type except for ``MARKET`` orders using
            parameter ``quoteOrderQty``. The pending order is only placed on the order book when the working order gets
            fully filled.
        - If either the working order or the pending order is cancelled individually, the other order in the order list
            will also be canceled or expired.
        - When the order list is placed, if the working order gets immediately fully filled, the placement response will
            show the working order as ``FILLED`` but the pending order will still appear as ``PENDING_NEW``. You need to
            query the status of the pending order again to see its updated status.
        - OTOs add 2 orders to the unfilled order count, ``EXCHANGE_MAX_NUM_ORDERS`` filter and ``MAX_NUM_ORDERS``
            filter.

        Weight: 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            working_type: Supported values: LIMIT,LIMIT_MAKER
            working_side: BUY,SELL
            working_price: Value sent with the request.
            working_quantity: Sets the quantity for the working order.
            working_iceberg_qty: This can only be used if workingTimeInForce is GTC.
            pending_type: Supported values: Order Types Note that MARKET orders using quoteOrderQty are not supported.
            pending_side: BUY,SELL
            pending_quantity: Sets the quantity for the pending order.
            timestamp: UTC timestamp in ms
            signature: Signature
            list_client_order_id: Arbitrary unique ID among open order lists. Automatically generated if not sent. A new
                order list with the same ``listClientOrderId`` is accepted only when the previous one is filled or
                completely expired. ``listClientOrderId`` is distinct from the ``workingClientOrderId`` and the
                ``pendingClientOrderId``.
            new_order_resp_type: Set the response JSON.
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            working_client_order_id: Arbitrary unique ID among open orders for the working order. Automatically
                generated if not sent.
            working_time_in_force: GTC, IOC, FOK
            working_strategy_id: Arbitrary numeric value identifying the working order within an order strategy.
            working_strategy_type: Arbitrary numeric value identifying the working order strategy. Values smaller than
                1000000 are reserved and cannot be used.
            pending_client_order_id: Arbitrary unique ID among open orders for the pending order. Automatically
                generated if not sent.
            pending_price: Value sent with the request.
            pending_stop_price: Value sent with the request.
            pending_trailing_delta: Value sent with the request.
            pending_iceberg_qty: This can only be used if pendingTimeInForce is GTC.
            pending_time_in_force: GTC, IOC, FOK
            pending_strategy_id: Arbitrary numeric value identifying the pending order within an order strategy.
            pending_strategy_type: Arbitrary numeric value identifying the pending order strategy. Values smaller than
                1000000 are reserved and cannot be used.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/v3/orderList/oto"),
            query_params=[
                param[str]("symbol", symbol),
                param[WorkingTypeOrStr]("workingType", working_type),
                param[WorkingSideOrStr]("workingSide", working_side),
                param[float]("workingPrice", working_price),
                param[float]("workingQuantity", working_quantity),
                param[float]("workingIcebergQty", working_iceberg_qty),
                param[PendingTypeOrStr]("pendingType", pending_type),
                param[PendingSideOrStr]("pendingSide", pending_side),
                param[float]("pendingQuantity", pending_quantity),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("listClientOrderId", list_client_order_id),
                param[NewOrderRespTypeOrStr | None]("newOrderRespType", new_order_resp_type),
                param[SelfTradePreventionModeOrStr | None]("selfTradePreventionMode", self_trade_prevention_mode),
                param[str | None]("workingClientOrderId", working_client_order_id),
                param[WorkingTimeInForceOrStr | None]("workingTimeInForce", working_time_in_force),
                param[float | None]("workingStrategyId", working_strategy_id),
                param[int | None]("workingStrategyType", working_strategy_type),
                param[str | None]("pendingClientOrderId", pending_client_order_id),
                param[float | None]("pendingPrice", pending_price),
                param[float | None]("pendingStopPrice", pending_stop_price),
                param[float | None]("pendingTrailingDelta", pending_trailing_delta),
                param[float | None]("pendingIcebergQty", pending_iceberg_qty),
                param[PendingTimeInForceOrStr | None]("pendingTimeInForce", pending_time_in_force),
                param[float | None]("pendingStrategyId", pending_strategy_id),
                param[int | None]("pendingStrategyType", pending_strategy_type),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ApiV3OrderListOtoResponse],
            error_mapper=new_order_list_oto_trade_error_mapper,
            request_options=request_options,
        )

    def new_order_list_otoco_trade(
        self,
        symbol: str,
        working_type: WorkingTypeOrStr,
        working_side: WorkingSideOrStr,
        working_price: float,
        working_quantity: float,
        working_iceberg_qty: float,
        pending_side: PendingSideOrStr,
        pending_quantity: float,
        pending_above_type: PendingAboveTypeOrStr,
        timestamp: int,
        signature: str,
        *,
        list_client_order_id: str | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        working_client_order_id: str | None = None,
        working_time_in_force: WorkingTimeInForceOrStr | None = None,
        working_strategy_id: float | None = None,
        working_strategy_type: int | None = None,
        pending_above_client_order_id: str | None = None,
        pending_above_price: float | None = None,
        pending_above_stop_price: float | None = None,
        pending_above_trailing_delta: float | None = None,
        pending_above_iceberg_qty: float | None = None,
        pending_above_time_in_force: PendingAboveTimeInForceOrStr | None = None,
        pending_above_strategy_id: float | None = None,
        pending_above_strategy_type: int | None = None,
        pending_below_type: PendingBelowTypeOrStr | None = None,
        pending_below_client_order_id: str | None = None,
        pending_below_price: float | None = None,
        pending_below_stop_price: float | None = None,
        pending_below_trailing_delta: float | None = None,
        pending_below_iceberg_qty: float | None = None,
        pending_below_time_in_force: PendingBelowTimeInForceOrStr | None = None,
        pending_below_strategy_id: float | None = None,
        pending_below_strategy_type: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV3OrderListOtocoResponse, NewOrderListOtocoTradeErrorBody]:
        """Place an ``OTOCO``.
        - An ``OTOCO`` (One-Triggers-One-Cancels-the-Other) is an order list comprised of 3 orders.
        - The first order is called the working order and must be ``LIMIT`` or ``LIMIT_MAKER``. Initially, only the
            working order goes on the order book.
          - The behavior of the working order is the same as the ``OTO``.
        - ``OTOCO`` has 2 pending orders (pending above and pending below), forming an ``OCO`` pair. The pending orders
            are only placed on the order book when the working order gets fully filled.
          - The rules of the pending above and pending below follow the same rules as the Order List ``OCO``.
        - OTOCOs add 3 orders against the unfilled order count, ``EXCHANGE_MAX_NUM_ORDERS`` filter, and
            ``MAX_NUM_ORDERS`` filter.

        Weight: 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            working_type: Supported values: LIMIT,LIMIT_MAKER
            working_side: BUY,SELL
            working_price: Value sent with the request.
            working_quantity: Sets the quantity for the working order.
            working_iceberg_qty: This can only be used if workingTimeInForce is GTC.
            pending_side: BUY,SELL
            pending_quantity: Sets the quantity for the pending order.
            pending_above_type: Supported values: LIMIT_MAKER, STOP_LOSS, and STOP_LOSS_LIMIT
            timestamp: UTC timestamp in ms
            signature: Signature
            list_client_order_id: Arbitrary unique ID among open order lists. Automatically generated if not sent. A new
                order list with the same ``listClientOrderId`` is accepted only when the previous one is filled or
                completely expired. ``listClientOrderId`` is distinct from the ``workingClientOrderId`` and the
                ``pendingClientOrderId``.
            new_order_resp_type: Set the response JSON.
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            working_client_order_id: Arbitrary unique ID among open orders for the working order. Automatically
                generated if not sent.
            working_time_in_force: GTC, IOC, FOK
            working_strategy_id: Arbitrary numeric value identifying the working order within an order strategy.
            working_strategy_type: Arbitrary numeric value identifying the working order strategy. Values smaller than
                1000000 are reserved and cannot be used.
            pending_above_client_order_id: Arbitrary unique ID among open orders for the pending above order.
                Automatically generated if not sent.
            pending_above_price: Value sent with the request.
            pending_above_stop_price: Value sent with the request.
            pending_above_trailing_delta: Value sent with the request.
            pending_above_iceberg_qty: This can only be used if pendingAboveTimeInForce is GTC.
            pending_above_time_in_force: Value sent with the request.
            pending_above_strategy_id: Arbitrary numeric value identifying the pending above order within an order
                strategy.
            pending_above_strategy_type: Arbitrary numeric value identifying the pending above order strategy. Values
                smaller than 1000000 are reserved and cannot be used.
            pending_below_type: Supported values: LIMIT_MAKER, STOP_LOSS, and STOP_LOSS_LIMIT
            pending_below_client_order_id: Arbitrary unique ID among open orders for the pending below order.
                Automatically generated if not sent.
            pending_below_price: Value sent with the request.
            pending_below_stop_price: Value sent with the request.
            pending_below_trailing_delta: Value sent with the request.
            pending_below_iceberg_qty: This can only be used if pendingBelowTimeInForce is GTC.
            pending_below_time_in_force: Value sent with the request.
            pending_below_strategy_id: Arbitrary numeric value identifying the pending below order within an order
                strategy.
            pending_below_strategy_type: Arbitrary numeric value identifying the pending below order strategy. Values
                smaller than 1000000 are reserved and cannot be used.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/v3/orderList/otoco"),
            query_params=[
                param[str]("symbol", symbol),
                param[WorkingTypeOrStr]("workingType", working_type),
                param[WorkingSideOrStr]("workingSide", working_side),
                param[float]("workingPrice", working_price),
                param[float]("workingQuantity", working_quantity),
                param[float]("workingIcebergQty", working_iceberg_qty),
                param[PendingSideOrStr]("pendingSide", pending_side),
                param[float]("pendingQuantity", pending_quantity),
                param[PendingAboveTypeOrStr]("pendingAboveType", pending_above_type),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("listClientOrderId", list_client_order_id),
                param[NewOrderRespTypeOrStr | None]("newOrderRespType", new_order_resp_type),
                param[SelfTradePreventionModeOrStr | None]("selfTradePreventionMode", self_trade_prevention_mode),
                param[str | None]("workingClientOrderId", working_client_order_id),
                param[WorkingTimeInForceOrStr | None]("workingTimeInForce", working_time_in_force),
                param[float | None]("workingStrategyId", working_strategy_id),
                param[int | None]("workingStrategyType", working_strategy_type),
                param[str | None]("pendingAboveClientOrderId", pending_above_client_order_id),
                param[float | None]("pendingAbovePrice", pending_above_price),
                param[float | None]("pendingAboveStopPrice", pending_above_stop_price),
                param[float | None]("pendingAboveTrailingDelta", pending_above_trailing_delta),
                param[float | None]("pendingAboveIcebergQty", pending_above_iceberg_qty),
                param[PendingAboveTimeInForceOrStr | None]("pendingAboveTimeInForce", pending_above_time_in_force),
                param[float | None]("pendingAboveStrategyId", pending_above_strategy_id),
                param[int | None]("pendingAboveStrategyType", pending_above_strategy_type),
                param[PendingBelowTypeOrStr | None]("pendingBelowType", pending_below_type),
                param[str | None]("pendingBelowClientOrderId", pending_below_client_order_id),
                param[float | None]("pendingBelowPrice", pending_below_price),
                param[float | None]("pendingBelowStopPrice", pending_below_stop_price),
                param[float | None]("pendingBelowTrailingDelta", pending_below_trailing_delta),
                param[float | None]("pendingBelowIcebergQty", pending_below_iceberg_qty),
                param[PendingBelowTimeInForceOrStr | None]("pendingBelowTimeInForce", pending_below_time_in_force),
                param[float | None]("pendingBelowStrategyId", pending_below_strategy_id),
                param[int | None]("pendingBelowStrategyType", pending_below_strategy_type),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ApiV3OrderListOtocoResponse],
            error_mapper=new_order_list_otoco_trade_error_mapper,
            request_options=request_options,
        )

    def new_order_list_oco_trade(
        self,
        symbol: str,
        side: SideOrStr,
        quantity: float,
        above_type: str,
        below_type: str,
        timestamp: int,
        signature: str,
        *,
        list_client_order_id: str | None = None,
        above_client_order_id: str | None = None,
        above_iceberg_qty: float | None = None,
        above_price: float | None = None,
        above_stop_price: float | None = None,
        above_trailing_delta: float | None = None,
        above_time_in_force: AboveTimeInForceOrStr | None = None,
        above_strategy_id: float | None = None,
        above_strategy_type: int | None = None,
        below_client_order_id: str | None = None,
        below_iceberg_qty: float | None = None,
        below_price: float | None = None,
        below_stop_price: float | None = None,
        below_trailing_delta: float | None = None,
        below_time_in_force: BelowTimeInForceOrStr | None = None,
        below_strategy_id: float | None = None,
        below_strategy_type: int | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV3OrderListOcoResponse, NewOrderListOcoTradeErrorBody]:
        """Send in an one-cancels-the-other (OCO) pair, where activation of one order immediately cancels the other.

        - An ``OCO`` has 2 orders called the above order and below order.
        - One of the orders must be a ``LIMIT_MAKER`` order and the other must be ``STOP_LOSS`` or``STOP_LOSS_LIMIT``
            order.
        - Price restrictions:
            - If the ``OCO`` is on the ``SELL`` side: ``LIMIT_MAKER`` price > Last Traded Price > stopPrice
            - If the ``OCO`` is on the ``BUY`` side: ``LIMIT_MAKER`` price < Last Traded Price < stopPrice
        - OCOs add 2 orders to the unfilled order count, ``EXCHANGE_MAX_ORDERS`` filter, and the ``MAX_NUM_ORDERS``
            filter.

        Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            quantity: Value sent with the request.
            above_type: Supported values : ``STOP_LOSS_LIMIT``, ``STOP_LOSS``, ``LIMIT_MAKER``
            below_type: Supported values : ``STOP_LOSS_LIMIT``, ``STOP_LOSS``, ``LIMIT_MAKER``
            timestamp: UTC timestamp in ms
            signature: Signature
            list_client_order_id: Arbitrary unique ID among open order lists. Automatically generated if not sent. A new
                order list with the same ``listClientOrderId`` is accepted only when the previous one is filled or
                completely expired. ``listClientOrderId`` is distinct from the ``aboveClientOrderId`` and the
                ``belowCLientOrderId``.
            above_client_order_id: Arbitrary unique ID among open orders for the above order. Automatically generated if
                not sent
            above_iceberg_qty: Note that this can only be used if ``aboveTimeInForce`` is ``GTC``.
            above_price: Value sent with the request.
            above_stop_price: Can be used if ``aboveType`` is ``STOP_LOSS`` or ``STOP_LOSS_LIMIT``. Either
                ``aboveStopPrice`` or ``aboveTrailingDelta`` or both, must be specified.
            above_trailing_delta: Value sent with the request.
            above_time_in_force: Required if the ``aboveType`` is ``STOP_LOSS_LIMIT``.
            above_strategy_id: Arbitrary numeric value identifying the above order within an order strategy.
            above_strategy_type: Arbitrary numeric value identifying the above order strategy. Values smaller than
                1000000 are reserved and cannot be used.
            below_client_order_id: Arbitrary unique ID among open orders for the below order. Automatically generated if
                not sent
            below_iceberg_qty: Note that this can only be used if ``belowTimeInForce`` is ``GTC``.
            below_price: Can be used if ``belowType`` is ``STOP_LOSS_LIMIT`` or ``LIMIT_MAKER`` to specify the limit
                price.
            below_stop_price: Can be used if ``belowType`` is ``STOP_LOSS`` or ``STOP_LOSS_LIMIT``. Either
                ``belowStopPrice`` or ``belowTrailingDelta`` or both, must be specified.
            below_trailing_delta: Value sent with the request.
            below_time_in_force: Required if the ``belowType`` is ``STOP_LOSS_LIMIT``.
            below_strategy_id: Arbitrary numeric value identifying the below order within an order strategy.
            below_strategy_type: Arbitrary numeric value identifying the below order strategy. Values smaller than
                1000000 are reserved and cannot be used.
            new_order_resp_type: Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders
                default to ACK.
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/v3/orderList/oco"),
            query_params=[
                param[str]("symbol", symbol),
                param[SideOrStr]("side", side),
                param[float]("quantity", quantity),
                param[str]("aboveType", above_type),
                param[str]("belowType", below_type),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("listClientOrderId", list_client_order_id),
                param[str | None]("aboveClientOrderId", above_client_order_id),
                param[float | None]("aboveIcebergQty", above_iceberg_qty),
                param[float | None]("abovePrice", above_price),
                param[float | None]("aboveStopPrice", above_stop_price),
                param[float | None]("aboveTrailingDelta", above_trailing_delta),
                param[AboveTimeInForceOrStr | None]("aboveTimeInForce", above_time_in_force),
                param[float | None]("aboveStrategyId", above_strategy_id),
                param[int | None]("aboveStrategyType", above_strategy_type),
                param[str | None]("belowClientOrderId", below_client_order_id),
                param[float | None]("belowIcebergQty", below_iceberg_qty),
                param[float | None]("belowPrice", below_price),
                param[float | None]("belowStopPrice", below_stop_price),
                param[float | None]("belowTrailingDelta", below_trailing_delta),
                param[BelowTimeInForceOrStr | None]("belowTimeInForce", below_time_in_force),
                param[float | None]("belowStrategyId", below_strategy_id),
                param[int | None]("belowStrategyType", below_strategy_type),
                param[NewOrderRespTypeOrStr | None]("newOrderRespType", new_order_resp_type),
                param[SelfTradePreventionModeOrStr | None]("selfTradePreventionMode", self_trade_prevention_mode),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ApiV3OrderListOcoResponse],
            error_mapper=new_order_list_oco_trade_error_mapper,
            request_options=request_options,
        )

    def new_order_using_sor_trade(
        self,
        symbol: str,
        side: SideOrStr,
        type_: Type1OrStr,
        quantity: float,
        timestamp: int,
        signature: str,
        *,
        time_in_force: TimeInForceOrStr | None = None,
        price: float | None = None,
        new_client_order_id: str | None = None,
        strategy_id: int | None = None,
        strategy_type: int | None = None,
        iceberg_qty: float | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV3SorOrderResponse, NewOrderUsingSorTradeErrorBody]:
        """Weight(IP): 6

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            type_: Order type
            quantity: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            time_in_force: Order time in force
            price: Value sent with the request.
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            strategy_id: Value sent with the request.
            strategy_type: The value cannot be less than 1000000.
            iceberg_qty: Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.
            new_order_resp_type: Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders
                default to ACK.
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/v3/sor/order"),
            query_params=[
                param[str]("symbol", symbol),
                param[SideOrStr]("side", side),
                param[Type1OrStr]("type", type_),
                param[float]("quantity", quantity),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[TimeInForceOrStr | None]("timeInForce", time_in_force),
                param[float | None]("price", price),
                param[str | None]("newClientOrderId", new_client_order_id),
                param[int | None]("strategyId", strategy_id),
                param[int | None]("strategyType", strategy_type),
                param[float | None]("icebergQty", iceberg_qty),
                param[NewOrderRespTypeOrStr | None]("newOrderRespType", new_order_resp_type),
                param[SelfTradePreventionModeOrStr | None]("selfTradePreventionMode", self_trade_prevention_mode),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ApiV3SorOrderResponse],
            error_mapper=new_order_using_sor_trade_error_mapper,
            request_options=request_options,
        )

    def query_allocations_user_data(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        from_allocation_id: int | None = None,
        limit: int | None = None,
        order_id: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ApiV3MyAllocationsResponse], QueryAllocationsUserDataErrorBody]:
        """Retrieves allocations resulting from SOR order placement.

        Weight: 20

        Supported parameter combinations: Parameters Response symbol allocations from oldest to newest symbol +
        startTime oldest allocations since startTime symbol + endTime newest allocations until endTime symbol +
        startTime + endTime allocations within the time range symbol + fromAllocationId allocations by allocation ID
        symbol + orderId allocations related to an order starting with oldest symbol + orderId + fromAllocationId
        allocations related to an order by allocation ID

        Note: The time between startTime and endTime can't be longer than 24 hours.

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            from_allocation_id: Value sent with the request.
            limit: Default 500; max 1000.
            order_id: Order id
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/myAllocations"),
            query_params=[
                param[str]("symbol", symbol),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("fromAllocationId", from_allocation_id),
                param[int | None]("limit", limit),
                param[int | None]("orderId", order_id),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[ApiV3MyAllocationsResponse]],
            error_mapper=query_allocations_user_data_error_mapper,
            request_options=request_options,
        )

    def query_commission_rates_user_data(
        self, symbol: str, timestamp: int, signature: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV3AccountCommissionResponse, QueryCommissionRatesUserDataErrorBody]:
        """Get current account commission rates.

        Weight: 20

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/account/commission"),
            query_params=[
                param[str]("symbol", symbol), param[int]("timestamp", timestamp), param[str]("signature", signature)
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ApiV3AccountCommissionResponse],
            error_mapper=query_commission_rates_user_data_error_mapper,
            request_options=request_options,
        )

    def query_current_order_count_usage_trade(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ApiV3RateLimitOrderResponse], QueryCurrentOrderCountUsageTradeErrorBody]:
        """Displays the user's current order count usage for all intervals.

        Weight(IP): 40

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/rateLimit/order"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[ApiV3RateLimitOrderResponse]],
            error_mapper=query_current_order_count_usage_trade_error_mapper,
            request_options=request_options,
        )

    def query_oco_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        order_list_id: int | None = None,
        orig_client_order_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV3OrderListResponse, QueryOcoUserDataErrorBody]:
        """Retrieves a specific OCO based on provided optional parameters

        Weight(IP): 4

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_list_id: Order list id
            orig_client_order_id: Order id from client
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/orderList"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("orderListId", order_list_id),
                param[str | None]("origClientOrderId", orig_client_order_id),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ApiV3OrderListResponse],
            error_mapper=query_oco_user_data_error_mapper,
            request_options=request_options,
        )

    def query_open_oco_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ApiV3OpenOrderListResponse], QueryOpenOcoUserDataErrorBody]:
        """Weight(IP): 6

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/openOrderList"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[ApiV3OpenOrderListResponse]],
            error_mapper=query_open_oco_user_data_error_mapper,
            request_options=request_options,
        )

    def query_order_user_data(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        orig_client_order_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OrderDetails, QueryOrderUserDataErrorBody]:
        """Check an order's status.

        - Either ``orderId`` or ``origClientOrderId`` must be sent.
        - For some historical orders ``cummulativeQuoteQty`` will be < 0, meaning the data is not available at this
            time.

        Weight(IP): 4

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order id
            orig_client_order_id: Order id from client
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/order"),
            query_params=[
                param[str]("symbol", symbol),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("orderId", order_id),
                param[str | None]("origClientOrderId", orig_client_order_id),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[OrderDetails],
            error_mapper=query_order_user_data_error_mapper,
            request_options=request_options,
        )

    def query_prevented_matches(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        prevented_match_id: int | None = None,
        order_id: int | None = None,
        from_prevented_match_id: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ApiV3MyPreventedMatchesResponse], QueryPreventedMatchesErrorBody]:
        """Displays the list of orders that were expired because of STP.

        For additional information on what a Prevented match is, as well as Self Trade Prevention (STP), please refer to
        our STP FAQ page.

        These are the combinations supported:

        * symbol + preventedMatchId
        * symbol + orderId
        * symbol + orderId + fromPreventedMatchId (limit will default to 500)
        * symbol + orderId + fromPreventedMatchId + limit

        Weight(IP):

        Case Weight If symbol is invalid: 2 Querying by preventedMatchId: 2 Querying by orderId: 20

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            prevented_match_id: Value sent with the request.
            order_id: Order id
            from_prevented_match_id: Value sent with the request.
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/myPreventedMatches"),
            query_params=[
                param[str]("symbol", symbol),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("preventedMatchId", prevented_match_id),
                param[int | None]("orderId", order_id),
                param[int | None]("fromPreventedMatchId", from_prevented_match_id),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[ApiV3MyPreventedMatchesResponse]],
            error_mapper=query_prevented_matches_error_mapper,
            request_options=request_options,
        )

    def query_all_oco_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        from_id: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ApiV3AllOrderListResponse], QueryAllOcoUserDataErrorBody]:
        """Retrieves all OCO based on provided optional parameters

        Weight(IP): 20

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            from_id: Trade id to fetch from. Default gets most recent trades.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/allOrderList"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("fromId", from_id),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[ApiV3AllOrderListResponse]],
            error_mapper=query_all_oco_user_data_error_mapper,
            request_options=request_options,
        )

    def test_new_order_trade(
        self,
        symbol: str,
        side: SideOrStr,
        type_: Type1OrStr,
        timestamp: int,
        signature: str,
        *,
        time_in_force: TimeInForceOrStr | None = None,
        quantity: float | None = None,
        quote_order_qty: float | None = None,
        price: float | None = None,
        new_client_order_id: str | None = None,
        strategy_id: int | None = None,
        strategy_type: int | None = None,
        stop_price: float | None = None,
        trailing_delta: float | None = None,
        iceberg_qty: float | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        recv_window: int | None = None,
        compute_commission_rates: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, TestNewOrderTradeErrorBody]:
        """Test new order creation and signature/recvWindow long. Creates and validates a new order but does not send it
        into the matching engine.

        Weight(IP):
          - Without computeCommissionRates: ``1``
          - With computeCommissionRates: ``20``

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            type_: Order type
            timestamp: UTC timestamp in ms
            signature: Signature
            time_in_force: Order time in force
            quantity: Order quantity
            quote_order_qty: Quote quantity
            price: Order price
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            strategy_id: Value sent with the request.
            strategy_type: The value cannot be less than 1000000.
            stop_price: Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
            trailing_delta: Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
            iceberg_qty: Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.
            new_order_resp_type: Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders
                default to ACK.
            recv_window: The value cannot be greater than 60000
            compute_commission_rates: Default: false
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/v3/order/test"),
            query_params=[
                param[str]("symbol", symbol),
                param[SideOrStr]("side", side),
                param[Type1OrStr]("type", type_),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[TimeInForceOrStr | None]("timeInForce", time_in_force),
                param[float | None]("quantity", quantity),
                param[float | None]("quoteOrderQty", quote_order_qty),
                param[float | None]("price", price),
                param[str | None]("newClientOrderId", new_client_order_id),
                param[int | None]("strategyId", strategy_id),
                param[int | None]("strategyType", strategy_type),
                param[float | None]("stopPrice", stop_price),
                param[float | None]("trailingDelta", trailing_delta),
                param[float | None]("icebergQty", iceberg_qty),
                param[NewOrderRespTypeOrStr | None]("newOrderRespType", new_order_resp_type),
                param[int | None]("recvWindow", recv_window),
                param[bool | None]("computeCommissionRates", compute_commission_rates),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[Any],
            error_mapper=test_new_order_trade_error_mapper,
            request_options=request_options,
        )

    def test_new_order_using_sor_trade(
        self,
        symbol: str,
        side: SideOrStr,
        type_: Type1OrStr,
        quantity: float,
        timestamp: int,
        signature: str,
        *,
        time_in_force: TimeInForceOrStr | None = None,
        price: float | None = None,
        new_client_order_id: str | None = None,
        strategy_id: int | None = None,
        strategy_type: int | None = None,
        iceberg_qty: float | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        compute_commission_rates: bool | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, TestNewOrderUsingSorTradeErrorBody]:
        """Test new order creation and signature/recvWindow using smart order routing (SOR). Creates and validates a new
        order but does not send it into the matching engine.

        Weight(IP):
          - Without computeCommissionRates: ``1``
          - With computeCommissionRates: ``20``

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            type_: Order type
            quantity: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            time_in_force: Order time in force
            price: Value sent with the request.
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            strategy_id: Value sent with the request.
            strategy_type: The value cannot be less than 1000000.
            iceberg_qty: Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.
            new_order_resp_type: Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders
                default to ACK.
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            compute_commission_rates: Default: false
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/v3/sor/order/test"),
            query_params=[
                param[str]("symbol", symbol),
                param[SideOrStr]("side", side),
                param[Type1OrStr]("type", type_),
                param[float]("quantity", quantity),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[TimeInForceOrStr | None]("timeInForce", time_in_force),
                param[float | None]("price", price),
                param[str | None]("newClientOrderId", new_client_order_id),
                param[int | None]("strategyId", strategy_id),
                param[int | None]("strategyType", strategy_type),
                param[float | None]("icebergQty", iceberg_qty),
                param[NewOrderRespTypeOrStr | None]("newOrderRespType", new_order_resp_type),
                param[SelfTradePreventionModeOrStr | None]("selfTradePreventionMode", self_trade_prevention_mode),
                param[bool | None]("computeCommissionRates", compute_commission_rates),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[Any],
            error_mapper=test_new_order_using_sor_trade_error_mapper,
            request_options=request_options,
        )


class AsyncTradeApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def account_information_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Account, AccountInformationUserDataErrorBody]:
        """Get current account information.

        Weight(IP): 20

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/account"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[Account],
            error_mapper=account_information_user_data_error_mapper,
            request_options=request_options,
        )

    async def account_trade_list_user_data(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        from_id: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[MyTrade], AccountTradeListUserDataErrorBody]:
        """Get trades for a specific account and symbol.

        If ``fromId`` is set, it will get id >= that ``fromId``. Otherwise most recent orders are returned.

        The time between startTime and endTime can't be longer than 24 hours. These are the supported combinations of
        all parameters:

          symbol

          symbol + orderId

          symbol + startTime

          symbol + endTime

          symbol + fromId

          symbol + startTime + endTime

          symbol+ orderId + fromId

        Weight(IP): 20

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: This can only be used in combination with symbol.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            from_id: Trade id to fetch from. Default gets most recent trades.
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/myTrades"),
            query_params=[
                param[str]("symbol", symbol),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("orderId", order_id),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("fromId", from_id),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[MyTrade]],
            error_mapper=account_trade_list_user_data_error_mapper,
            request_options=request_options,
        )

    async def all_orders_user_data(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[OrderDetails], AllOrdersUserDataErrorBody]:
        """Get all account orders; active, canceled, or filled..

        - If ``orderId`` is set, it will get orders >= that ``orderId``. Otherwise most recent orders are returned.
        - For some historical orders ``cummulativeQuoteQty`` will be < 0, meaning the data is not available at this
            time.
        - If ``startTime`` and/or ``endTime`` provided, ``orderId`` is not required

        Weight(IP): 20

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order id
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/allOrders"),
            query_params=[
                param[str]("symbol", symbol),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("orderId", order_id),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[OrderDetails]],
            error_mapper=all_orders_user_data_error_mapper,
            request_options=request_options,
        )

    async def cancel_oco_trade(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        order_list_id: int | None = None,
        list_client_order_id: str | None = None,
        new_client_order_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OcoOrder, CancelOcoTradeErrorBody]:
        """Cancel an entire Order List

        Canceling an individual leg will cancel the entire OCO

        Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            order_list_id: Order list id
            list_client_order_id: A unique Id for the entire orderList
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/api/v3/orderList"),
            query_params=[
                param[str]("symbol", symbol),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("orderListId", order_list_id),
                param[str | None]("listClientOrderId", list_client_order_id),
                param[str | None]("newClientOrderId", new_client_order_id),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[OcoOrder],
            error_mapper=cancel_oco_trade_error_mapper,
            request_options=request_options,
        )

    async def cancel_order_trade(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        orig_client_order_id: str | None = None,
        new_client_order_id: str | None = None,
        cancel_restrictions: CancelRestrictionsOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Order, CancelOrderTradeErrorBody]:
        """Cancel an active order.

        Either ``orderId`` or ``origClientOrderId`` must be sent.

        Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order id
            orig_client_order_id: Order id from client
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            cancel_restrictions: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/api/v3/order"),
            query_params=[
                param[str]("symbol", symbol),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("orderId", order_id),
                param[str | None]("origClientOrderId", orig_client_order_id),
                param[str | None]("newClientOrderId", new_client_order_id),
                param[CancelRestrictionsOrStr | None]("cancelRestrictions", cancel_restrictions),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[Order],
            error_mapper=cancel_order_trade_error_mapper,
            request_options=request_options,
        )

    async def cancel_all_open_orders_on_a_symbol_trade(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ApiV3OpenOrdersResponse], CancelAllOpenOrdersOnASymbolTradeErrorBody]:
        """Cancels all active orders on a symbol. This includes OCO orders.

        Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/api/v3/openOrders"),
            query_params=[
                param[str]("symbol", symbol),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[ApiV3OpenOrdersResponse]],
            error_mapper=cancel_all_open_orders_on_a_symbol_trade_error_mapper,
            request_options=request_options,
        )

    async def cancel_an_existing_order_and_send_a_new_order_trade(
        self,
        symbol: str,
        side: SideOrStr,
        type_: Type1OrStr,
        cancel_replace_mode: str,
        timestamp: int,
        signature: str,
        *,
        cancel_restrictions: CancelRestrictionsOrStr | None = None,
        time_in_force: TimeInForceOrStr | None = None,
        quantity: float | None = None,
        quote_order_qty: float | None = None,
        price: float | None = None,
        cancel_new_client_order_id: str | None = None,
        cancel_orig_client_order_id: str | None = None,
        cancel_order_id: int | None = None,
        new_client_order_id: str | None = None,
        strategy_id: int | None = None,
        strategy_type: int | None = None,
        stop_price: float | None = None,
        trailing_delta: float | None = None,
        iceberg_qty: float | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV3OrderCancelReplaceResponse, CancelAnExistingOrderAndSendANewOrderTradeErrorBody]:
        """Cancels an existing order and places a new order on the same symbol.

        Filters and Order Count are evaluated before the processing of the cancellation and order placement occurs.

        A new order that was not attempted (i.e. when newOrderResult: NOT_ATTEMPTED), will still increase the order
        count by 1.

        Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            type_: Order type
            cancel_replace_mode: - ``STOP_ON_FAILURE`` If the cancel request fails, the new order placement will not be
                attempted. - ``ALLOW_FAILURES`` If new order placement will be attempted even if cancel request fails.
            timestamp: UTC timestamp in ms
            signature: Signature
            cancel_restrictions: Value sent with the request.
            time_in_force: Order time in force
            quantity: Order quantity
            quote_order_qty: Quote quantity
            price: Order price
            cancel_new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            cancel_orig_client_order_id: Either the cancelOrigClientOrderId or cancelOrderId must be provided. If both
                are provided, cancelOrderId takes precedence.
            cancel_order_id: Either the cancelOrigClientOrderId or cancelOrderId must be provided. If both are provided,
                cancelOrderId takes precedence.
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            strategy_id: Value sent with the request.
            strategy_type: The value cannot be less than 1000000.
            stop_price: Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
            trailing_delta: Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
            iceberg_qty: Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.
            new_order_resp_type: Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders
                default to ACK.
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/v3/order/cancelReplace"),
            query_params=[
                param[str]("symbol", symbol),
                param[SideOrStr]("side", side),
                param[Type1OrStr]("type", type_),
                param[str]("cancelReplaceMode", cancel_replace_mode),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[CancelRestrictionsOrStr | None]("cancelRestrictions", cancel_restrictions),
                param[TimeInForceOrStr | None]("timeInForce", time_in_force),
                param[float | None]("quantity", quantity),
                param[float | None]("quoteOrderQty", quote_order_qty),
                param[float | None]("price", price),
                param[str | None]("cancelNewClientOrderId", cancel_new_client_order_id),
                param[str | None]("cancelOrigClientOrderId", cancel_orig_client_order_id),
                param[int | None]("cancelOrderId", cancel_order_id),
                param[str | None]("newClientOrderId", new_client_order_id),
                param[int | None]("strategyId", strategy_id),
                param[int | None]("strategyType", strategy_type),
                param[float | None]("stopPrice", stop_price),
                param[float | None]("trailingDelta", trailing_delta),
                param[float | None]("icebergQty", iceberg_qty),
                param[NewOrderRespTypeOrStr | None]("newOrderRespType", new_order_resp_type),
                param[SelfTradePreventionModeOrStr | None]("selfTradePreventionMode", self_trade_prevention_mode),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ApiV3OrderCancelReplaceResponse],
            error_mapper=cancel_an_existing_order_and_send_a_new_order_trade_error_mapper,
            request_options=request_options,
        )

    async def current_open_orders_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[OrderDetails], CurrentOpenOrdersUserDataErrorBody]:
        """Get all open orders on a symbol. Careful when accessing this with no symbol.

        Weight(IP):
        - ``6`` for a single symbol;
        - ``80`` when the symbol parameter is omitted;

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            symbol: Trading symbol, e.g. BNBUSDT
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/openOrders"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("symbol", symbol),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[OrderDetails]],
            error_mapper=current_open_orders_user_data_error_mapper,
            request_options=request_options,
        )

    async def new_order_trade(
        self,
        symbol: str,
        side: SideOrStr,
        type_: Type1OrStr,
        timestamp: int,
        signature: str,
        *,
        time_in_force: TimeInForceOrStr | None = None,
        quantity: float | None = None,
        quote_order_qty: float | None = None,
        price: float | None = None,
        new_client_order_id: str | None = None,
        strategy_id: int | None = None,
        strategy_type: int | None = None,
        stop_price: float | None = None,
        trailing_delta: float | None = None,
        iceberg_qty: float | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV3OrderResponse, NewOrderTradeErrorBody]:
        """Send in a new order.

        - ``LIMIT_MAKER`` are ``LIMIT`` orders that will be rejected if they would immediately match and trade as a
            taker.
        - ``STOP_LOSS`` and ``TAKE_PROFIT`` will execute a ``MARKET`` order when the ``stopPrice`` is reached.
        - Any ``LIMIT`` or ``LIMIT_MAKER`` type order can be made an iceberg order by sending an ``icebergQty``.
        - Any order with an ``icebergQty`` MUST have ``timeInForce`` set to ``GTC``.
        - ``MARKET`` orders using ``quantity`` specifies how much a user wants to buy or sell based on the market price.
        - ``MARKET`` orders using ``quoteOrderQty`` specifies the amount the user wants to spend (when buying) or
            receive (when selling) of the quote asset; the correct quantity will be determined based on the market
            liquidity and ``quoteOrderQty``.
        - ``MARKET`` orders using ``quoteOrderQty`` will not break ``LOT_SIZE`` filter rules; the order will execute a
            quantity that will have the notional value as close as possible to ``quoteOrderQty``.
        - same ``newClientOrderId`` can be accepted only when the previous one is filled, otherwise the order will be
            rejected.

        Trigger order price rules against market price for both ``MARKET`` and ``LIMIT`` versions:

        - Price above market price: ``STOP_LOSS`` ``BUY``, ``TAKE_PROFIT`` ``SELL``
        - Price below market price: ``STOP_LOSS`` ``SELL``, ``TAKE_PROFIT`` ``BUY``


        Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            type_: Order type
            timestamp: UTC timestamp in ms
            signature: Signature
            time_in_force: Order time in force
            quantity: Order quantity
            quote_order_qty: Quote quantity
            price: Order price
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            strategy_id: Value sent with the request.
            strategy_type: The value cannot be less than 1000000.
            stop_price: Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
            trailing_delta: Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
            iceberg_qty: Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.
            new_order_resp_type: Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders
                default to ACK.
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/v3/order"),
            query_params=[
                param[str]("symbol", symbol),
                param[SideOrStr]("side", side),
                param[Type1OrStr]("type", type_),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[TimeInForceOrStr | None]("timeInForce", time_in_force),
                param[float | None]("quantity", quantity),
                param[float | None]("quoteOrderQty", quote_order_qty),
                param[float | None]("price", price),
                param[str | None]("newClientOrderId", new_client_order_id),
                param[int | None]("strategyId", strategy_id),
                param[int | None]("strategyType", strategy_type),
                param[float | None]("stopPrice", stop_price),
                param[float | None]("trailingDelta", trailing_delta),
                param[float | None]("icebergQty", iceberg_qty),
                param[NewOrderRespTypeOrStr | None]("newOrderRespType", new_order_resp_type),
                param[SelfTradePreventionModeOrStr | None]("selfTradePreventionMode", self_trade_prevention_mode),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ApiV3OrderResponse],
            error_mapper=new_order_trade_error_mapper,
            request_options=request_options,
        )

    async def new_order_list_oto_trade(
        self,
        symbol: str,
        working_type: WorkingTypeOrStr,
        working_side: WorkingSideOrStr,
        working_price: float,
        working_quantity: float,
        working_iceberg_qty: float,
        pending_type: PendingTypeOrStr,
        pending_side: PendingSideOrStr,
        pending_quantity: float,
        timestamp: int,
        signature: str,
        *,
        list_client_order_id: str | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        working_client_order_id: str | None = None,
        working_time_in_force: WorkingTimeInForceOrStr | None = None,
        working_strategy_id: float | None = None,
        working_strategy_type: int | None = None,
        pending_client_order_id: str | None = None,
        pending_price: float | None = None,
        pending_stop_price: float | None = None,
        pending_trailing_delta: float | None = None,
        pending_iceberg_qty: float | None = None,
        pending_time_in_force: PendingTimeInForceOrStr | None = None,
        pending_strategy_id: float | None = None,
        pending_strategy_type: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV3OrderListOtoResponse, NewOrderListOtoTradeErrorBody]:
        """Places an ``OTO``.
        - An ``OTO`` (One-Triggers-the-Other) is an order list comprised of 2 orders.
        - The first order is called the working order and must be ``LIMIT`` or ``LIMIT_MAKER``. Initially, only the
            working order goes on the order book.
        - The second order is called the pending order. It can be any order type except for ``MARKET`` orders using
            parameter ``quoteOrderQty``. The pending order is only placed on the order book when the working order gets
            fully filled.
        - If either the working order or the pending order is cancelled individually, the other order in the order list
            will also be canceled or expired.
        - When the order list is placed, if the working order gets immediately fully filled, the placement response will
            show the working order as ``FILLED`` but the pending order will still appear as ``PENDING_NEW``. You need to
            query the status of the pending order again to see its updated status.
        - OTOs add 2 orders to the unfilled order count, ``EXCHANGE_MAX_NUM_ORDERS`` filter and ``MAX_NUM_ORDERS``
            filter.

        Weight: 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            working_type: Supported values: LIMIT,LIMIT_MAKER
            working_side: BUY,SELL
            working_price: Value sent with the request.
            working_quantity: Sets the quantity for the working order.
            working_iceberg_qty: This can only be used if workingTimeInForce is GTC.
            pending_type: Supported values: Order Types Note that MARKET orders using quoteOrderQty are not supported.
            pending_side: BUY,SELL
            pending_quantity: Sets the quantity for the pending order.
            timestamp: UTC timestamp in ms
            signature: Signature
            list_client_order_id: Arbitrary unique ID among open order lists. Automatically generated if not sent. A new
                order list with the same ``listClientOrderId`` is accepted only when the previous one is filled or
                completely expired. ``listClientOrderId`` is distinct from the ``workingClientOrderId`` and the
                ``pendingClientOrderId``.
            new_order_resp_type: Set the response JSON.
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            working_client_order_id: Arbitrary unique ID among open orders for the working order. Automatically
                generated if not sent.
            working_time_in_force: GTC, IOC, FOK
            working_strategy_id: Arbitrary numeric value identifying the working order within an order strategy.
            working_strategy_type: Arbitrary numeric value identifying the working order strategy. Values smaller than
                1000000 are reserved and cannot be used.
            pending_client_order_id: Arbitrary unique ID among open orders for the pending order. Automatically
                generated if not sent.
            pending_price: Value sent with the request.
            pending_stop_price: Value sent with the request.
            pending_trailing_delta: Value sent with the request.
            pending_iceberg_qty: This can only be used if pendingTimeInForce is GTC.
            pending_time_in_force: GTC, IOC, FOK
            pending_strategy_id: Arbitrary numeric value identifying the pending order within an order strategy.
            pending_strategy_type: Arbitrary numeric value identifying the pending order strategy. Values smaller than
                1000000 are reserved and cannot be used.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/v3/orderList/oto"),
            query_params=[
                param[str]("symbol", symbol),
                param[WorkingTypeOrStr]("workingType", working_type),
                param[WorkingSideOrStr]("workingSide", working_side),
                param[float]("workingPrice", working_price),
                param[float]("workingQuantity", working_quantity),
                param[float]("workingIcebergQty", working_iceberg_qty),
                param[PendingTypeOrStr]("pendingType", pending_type),
                param[PendingSideOrStr]("pendingSide", pending_side),
                param[float]("pendingQuantity", pending_quantity),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("listClientOrderId", list_client_order_id),
                param[NewOrderRespTypeOrStr | None]("newOrderRespType", new_order_resp_type),
                param[SelfTradePreventionModeOrStr | None]("selfTradePreventionMode", self_trade_prevention_mode),
                param[str | None]("workingClientOrderId", working_client_order_id),
                param[WorkingTimeInForceOrStr | None]("workingTimeInForce", working_time_in_force),
                param[float | None]("workingStrategyId", working_strategy_id),
                param[int | None]("workingStrategyType", working_strategy_type),
                param[str | None]("pendingClientOrderId", pending_client_order_id),
                param[float | None]("pendingPrice", pending_price),
                param[float | None]("pendingStopPrice", pending_stop_price),
                param[float | None]("pendingTrailingDelta", pending_trailing_delta),
                param[float | None]("pendingIcebergQty", pending_iceberg_qty),
                param[PendingTimeInForceOrStr | None]("pendingTimeInForce", pending_time_in_force),
                param[float | None]("pendingStrategyId", pending_strategy_id),
                param[int | None]("pendingStrategyType", pending_strategy_type),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ApiV3OrderListOtoResponse],
            error_mapper=new_order_list_oto_trade_error_mapper,
            request_options=request_options,
        )

    async def new_order_list_otoco_trade(
        self,
        symbol: str,
        working_type: WorkingTypeOrStr,
        working_side: WorkingSideOrStr,
        working_price: float,
        working_quantity: float,
        working_iceberg_qty: float,
        pending_side: PendingSideOrStr,
        pending_quantity: float,
        pending_above_type: PendingAboveTypeOrStr,
        timestamp: int,
        signature: str,
        *,
        list_client_order_id: str | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        working_client_order_id: str | None = None,
        working_time_in_force: WorkingTimeInForceOrStr | None = None,
        working_strategy_id: float | None = None,
        working_strategy_type: int | None = None,
        pending_above_client_order_id: str | None = None,
        pending_above_price: float | None = None,
        pending_above_stop_price: float | None = None,
        pending_above_trailing_delta: float | None = None,
        pending_above_iceberg_qty: float | None = None,
        pending_above_time_in_force: PendingAboveTimeInForceOrStr | None = None,
        pending_above_strategy_id: float | None = None,
        pending_above_strategy_type: int | None = None,
        pending_below_type: PendingBelowTypeOrStr | None = None,
        pending_below_client_order_id: str | None = None,
        pending_below_price: float | None = None,
        pending_below_stop_price: float | None = None,
        pending_below_trailing_delta: float | None = None,
        pending_below_iceberg_qty: float | None = None,
        pending_below_time_in_force: PendingBelowTimeInForceOrStr | None = None,
        pending_below_strategy_id: float | None = None,
        pending_below_strategy_type: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV3OrderListOtocoResponse, NewOrderListOtocoTradeErrorBody]:
        """Place an ``OTOCO``.
        - An ``OTOCO`` (One-Triggers-One-Cancels-the-Other) is an order list comprised of 3 orders.
        - The first order is called the working order and must be ``LIMIT`` or ``LIMIT_MAKER``. Initially, only the
            working order goes on the order book.
          - The behavior of the working order is the same as the ``OTO``.
        - ``OTOCO`` has 2 pending orders (pending above and pending below), forming an ``OCO`` pair. The pending orders
            are only placed on the order book when the working order gets fully filled.
          - The rules of the pending above and pending below follow the same rules as the Order List ``OCO``.
        - OTOCOs add 3 orders against the unfilled order count, ``EXCHANGE_MAX_NUM_ORDERS`` filter, and
            ``MAX_NUM_ORDERS`` filter.

        Weight: 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            working_type: Supported values: LIMIT,LIMIT_MAKER
            working_side: BUY,SELL
            working_price: Value sent with the request.
            working_quantity: Sets the quantity for the working order.
            working_iceberg_qty: This can only be used if workingTimeInForce is GTC.
            pending_side: BUY,SELL
            pending_quantity: Sets the quantity for the pending order.
            pending_above_type: Supported values: LIMIT_MAKER, STOP_LOSS, and STOP_LOSS_LIMIT
            timestamp: UTC timestamp in ms
            signature: Signature
            list_client_order_id: Arbitrary unique ID among open order lists. Automatically generated if not sent. A new
                order list with the same ``listClientOrderId`` is accepted only when the previous one is filled or
                completely expired. ``listClientOrderId`` is distinct from the ``workingClientOrderId`` and the
                ``pendingClientOrderId``.
            new_order_resp_type: Set the response JSON.
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            working_client_order_id: Arbitrary unique ID among open orders for the working order. Automatically
                generated if not sent.
            working_time_in_force: GTC, IOC, FOK
            working_strategy_id: Arbitrary numeric value identifying the working order within an order strategy.
            working_strategy_type: Arbitrary numeric value identifying the working order strategy. Values smaller than
                1000000 are reserved and cannot be used.
            pending_above_client_order_id: Arbitrary unique ID among open orders for the pending above order.
                Automatically generated if not sent.
            pending_above_price: Value sent with the request.
            pending_above_stop_price: Value sent with the request.
            pending_above_trailing_delta: Value sent with the request.
            pending_above_iceberg_qty: This can only be used if pendingAboveTimeInForce is GTC.
            pending_above_time_in_force: Value sent with the request.
            pending_above_strategy_id: Arbitrary numeric value identifying the pending above order within an order
                strategy.
            pending_above_strategy_type: Arbitrary numeric value identifying the pending above order strategy. Values
                smaller than 1000000 are reserved and cannot be used.
            pending_below_type: Supported values: LIMIT_MAKER, STOP_LOSS, and STOP_LOSS_LIMIT
            pending_below_client_order_id: Arbitrary unique ID among open orders for the pending below order.
                Automatically generated if not sent.
            pending_below_price: Value sent with the request.
            pending_below_stop_price: Value sent with the request.
            pending_below_trailing_delta: Value sent with the request.
            pending_below_iceberg_qty: This can only be used if pendingBelowTimeInForce is GTC.
            pending_below_time_in_force: Value sent with the request.
            pending_below_strategy_id: Arbitrary numeric value identifying the pending below order within an order
                strategy.
            pending_below_strategy_type: Arbitrary numeric value identifying the pending below order strategy. Values
                smaller than 1000000 are reserved and cannot be used.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/v3/orderList/otoco"),
            query_params=[
                param[str]("symbol", symbol),
                param[WorkingTypeOrStr]("workingType", working_type),
                param[WorkingSideOrStr]("workingSide", working_side),
                param[float]("workingPrice", working_price),
                param[float]("workingQuantity", working_quantity),
                param[float]("workingIcebergQty", working_iceberg_qty),
                param[PendingSideOrStr]("pendingSide", pending_side),
                param[float]("pendingQuantity", pending_quantity),
                param[PendingAboveTypeOrStr]("pendingAboveType", pending_above_type),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("listClientOrderId", list_client_order_id),
                param[NewOrderRespTypeOrStr | None]("newOrderRespType", new_order_resp_type),
                param[SelfTradePreventionModeOrStr | None]("selfTradePreventionMode", self_trade_prevention_mode),
                param[str | None]("workingClientOrderId", working_client_order_id),
                param[WorkingTimeInForceOrStr | None]("workingTimeInForce", working_time_in_force),
                param[float | None]("workingStrategyId", working_strategy_id),
                param[int | None]("workingStrategyType", working_strategy_type),
                param[str | None]("pendingAboveClientOrderId", pending_above_client_order_id),
                param[float | None]("pendingAbovePrice", pending_above_price),
                param[float | None]("pendingAboveStopPrice", pending_above_stop_price),
                param[float | None]("pendingAboveTrailingDelta", pending_above_trailing_delta),
                param[float | None]("pendingAboveIcebergQty", pending_above_iceberg_qty),
                param[PendingAboveTimeInForceOrStr | None]("pendingAboveTimeInForce", pending_above_time_in_force),
                param[float | None]("pendingAboveStrategyId", pending_above_strategy_id),
                param[int | None]("pendingAboveStrategyType", pending_above_strategy_type),
                param[PendingBelowTypeOrStr | None]("pendingBelowType", pending_below_type),
                param[str | None]("pendingBelowClientOrderId", pending_below_client_order_id),
                param[float | None]("pendingBelowPrice", pending_below_price),
                param[float | None]("pendingBelowStopPrice", pending_below_stop_price),
                param[float | None]("pendingBelowTrailingDelta", pending_below_trailing_delta),
                param[float | None]("pendingBelowIcebergQty", pending_below_iceberg_qty),
                param[PendingBelowTimeInForceOrStr | None]("pendingBelowTimeInForce", pending_below_time_in_force),
                param[float | None]("pendingBelowStrategyId", pending_below_strategy_id),
                param[int | None]("pendingBelowStrategyType", pending_below_strategy_type),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ApiV3OrderListOtocoResponse],
            error_mapper=new_order_list_otoco_trade_error_mapper,
            request_options=request_options,
        )

    async def new_order_list_oco_trade(
        self,
        symbol: str,
        side: SideOrStr,
        quantity: float,
        above_type: str,
        below_type: str,
        timestamp: int,
        signature: str,
        *,
        list_client_order_id: str | None = None,
        above_client_order_id: str | None = None,
        above_iceberg_qty: float | None = None,
        above_price: float | None = None,
        above_stop_price: float | None = None,
        above_trailing_delta: float | None = None,
        above_time_in_force: AboveTimeInForceOrStr | None = None,
        above_strategy_id: float | None = None,
        above_strategy_type: int | None = None,
        below_client_order_id: str | None = None,
        below_iceberg_qty: float | None = None,
        below_price: float | None = None,
        below_stop_price: float | None = None,
        below_trailing_delta: float | None = None,
        below_time_in_force: BelowTimeInForceOrStr | None = None,
        below_strategy_id: float | None = None,
        below_strategy_type: int | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV3OrderListOcoResponse, NewOrderListOcoTradeErrorBody]:
        """Send in an one-cancels-the-other (OCO) pair, where activation of one order immediately cancels the other.

        - An ``OCO`` has 2 orders called the above order and below order.
        - One of the orders must be a ``LIMIT_MAKER`` order and the other must be ``STOP_LOSS`` or``STOP_LOSS_LIMIT``
            order.
        - Price restrictions:
            - If the ``OCO`` is on the ``SELL`` side: ``LIMIT_MAKER`` price > Last Traded Price > stopPrice
            - If the ``OCO`` is on the ``BUY`` side: ``LIMIT_MAKER`` price < Last Traded Price < stopPrice
        - OCOs add 2 orders to the unfilled order count, ``EXCHANGE_MAX_ORDERS`` filter, and the ``MAX_NUM_ORDERS``
            filter.

        Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            quantity: Value sent with the request.
            above_type: Supported values : ``STOP_LOSS_LIMIT``, ``STOP_LOSS``, ``LIMIT_MAKER``
            below_type: Supported values : ``STOP_LOSS_LIMIT``, ``STOP_LOSS``, ``LIMIT_MAKER``
            timestamp: UTC timestamp in ms
            signature: Signature
            list_client_order_id: Arbitrary unique ID among open order lists. Automatically generated if not sent. A new
                order list with the same ``listClientOrderId`` is accepted only when the previous one is filled or
                completely expired. ``listClientOrderId`` is distinct from the ``aboveClientOrderId`` and the
                ``belowCLientOrderId``.
            above_client_order_id: Arbitrary unique ID among open orders for the above order. Automatically generated if
                not sent
            above_iceberg_qty: Note that this can only be used if ``aboveTimeInForce`` is ``GTC``.
            above_price: Value sent with the request.
            above_stop_price: Can be used if ``aboveType`` is ``STOP_LOSS`` or ``STOP_LOSS_LIMIT``. Either
                ``aboveStopPrice`` or ``aboveTrailingDelta`` or both, must be specified.
            above_trailing_delta: Value sent with the request.
            above_time_in_force: Required if the ``aboveType`` is ``STOP_LOSS_LIMIT``.
            above_strategy_id: Arbitrary numeric value identifying the above order within an order strategy.
            above_strategy_type: Arbitrary numeric value identifying the above order strategy. Values smaller than
                1000000 are reserved and cannot be used.
            below_client_order_id: Arbitrary unique ID among open orders for the below order. Automatically generated if
                not sent
            below_iceberg_qty: Note that this can only be used if ``belowTimeInForce`` is ``GTC``.
            below_price: Can be used if ``belowType`` is ``STOP_LOSS_LIMIT`` or ``LIMIT_MAKER`` to specify the limit
                price.
            below_stop_price: Can be used if ``belowType`` is ``STOP_LOSS`` or ``STOP_LOSS_LIMIT``. Either
                ``belowStopPrice`` or ``belowTrailingDelta`` or both, must be specified.
            below_trailing_delta: Value sent with the request.
            below_time_in_force: Required if the ``belowType`` is ``STOP_LOSS_LIMIT``.
            below_strategy_id: Arbitrary numeric value identifying the below order within an order strategy.
            below_strategy_type: Arbitrary numeric value identifying the below order strategy. Values smaller than
                1000000 are reserved and cannot be used.
            new_order_resp_type: Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders
                default to ACK.
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/v3/orderList/oco"),
            query_params=[
                param[str]("symbol", symbol),
                param[SideOrStr]("side", side),
                param[float]("quantity", quantity),
                param[str]("aboveType", above_type),
                param[str]("belowType", below_type),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("listClientOrderId", list_client_order_id),
                param[str | None]("aboveClientOrderId", above_client_order_id),
                param[float | None]("aboveIcebergQty", above_iceberg_qty),
                param[float | None]("abovePrice", above_price),
                param[float | None]("aboveStopPrice", above_stop_price),
                param[float | None]("aboveTrailingDelta", above_trailing_delta),
                param[AboveTimeInForceOrStr | None]("aboveTimeInForce", above_time_in_force),
                param[float | None]("aboveStrategyId", above_strategy_id),
                param[int | None]("aboveStrategyType", above_strategy_type),
                param[str | None]("belowClientOrderId", below_client_order_id),
                param[float | None]("belowIcebergQty", below_iceberg_qty),
                param[float | None]("belowPrice", below_price),
                param[float | None]("belowStopPrice", below_stop_price),
                param[float | None]("belowTrailingDelta", below_trailing_delta),
                param[BelowTimeInForceOrStr | None]("belowTimeInForce", below_time_in_force),
                param[float | None]("belowStrategyId", below_strategy_id),
                param[int | None]("belowStrategyType", below_strategy_type),
                param[NewOrderRespTypeOrStr | None]("newOrderRespType", new_order_resp_type),
                param[SelfTradePreventionModeOrStr | None]("selfTradePreventionMode", self_trade_prevention_mode),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ApiV3OrderListOcoResponse],
            error_mapper=new_order_list_oco_trade_error_mapper,
            request_options=request_options,
        )

    async def new_order_using_sor_trade(
        self,
        symbol: str,
        side: SideOrStr,
        type_: Type1OrStr,
        quantity: float,
        timestamp: int,
        signature: str,
        *,
        time_in_force: TimeInForceOrStr | None = None,
        price: float | None = None,
        new_client_order_id: str | None = None,
        strategy_id: int | None = None,
        strategy_type: int | None = None,
        iceberg_qty: float | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV3SorOrderResponse, NewOrderUsingSorTradeErrorBody]:
        """Weight(IP): 6

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            type_: Order type
            quantity: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            time_in_force: Order time in force
            price: Value sent with the request.
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            strategy_id: Value sent with the request.
            strategy_type: The value cannot be less than 1000000.
            iceberg_qty: Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.
            new_order_resp_type: Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders
                default to ACK.
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/v3/sor/order"),
            query_params=[
                param[str]("symbol", symbol),
                param[SideOrStr]("side", side),
                param[Type1OrStr]("type", type_),
                param[float]("quantity", quantity),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[TimeInForceOrStr | None]("timeInForce", time_in_force),
                param[float | None]("price", price),
                param[str | None]("newClientOrderId", new_client_order_id),
                param[int | None]("strategyId", strategy_id),
                param[int | None]("strategyType", strategy_type),
                param[float | None]("icebergQty", iceberg_qty),
                param[NewOrderRespTypeOrStr | None]("newOrderRespType", new_order_resp_type),
                param[SelfTradePreventionModeOrStr | None]("selfTradePreventionMode", self_trade_prevention_mode),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ApiV3SorOrderResponse],
            error_mapper=new_order_using_sor_trade_error_mapper,
            request_options=request_options,
        )

    async def query_allocations_user_data(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        from_allocation_id: int | None = None,
        limit: int | None = None,
        order_id: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ApiV3MyAllocationsResponse], QueryAllocationsUserDataErrorBody]:
        """Retrieves allocations resulting from SOR order placement.

        Weight: 20

        Supported parameter combinations: Parameters Response symbol allocations from oldest to newest symbol +
        startTime oldest allocations since startTime symbol + endTime newest allocations until endTime symbol +
        startTime + endTime allocations within the time range symbol + fromAllocationId allocations by allocation ID
        symbol + orderId allocations related to an order starting with oldest symbol + orderId + fromAllocationId
        allocations related to an order by allocation ID

        Note: The time between startTime and endTime can't be longer than 24 hours.

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            from_allocation_id: Value sent with the request.
            limit: Default 500; max 1000.
            order_id: Order id
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/myAllocations"),
            query_params=[
                param[str]("symbol", symbol),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("fromAllocationId", from_allocation_id),
                param[int | None]("limit", limit),
                param[int | None]("orderId", order_id),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[ApiV3MyAllocationsResponse]],
            error_mapper=query_allocations_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_commission_rates_user_data(
        self, symbol: str, timestamp: int, signature: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV3AccountCommissionResponse, QueryCommissionRatesUserDataErrorBody]:
        """Get current account commission rates.

        Weight: 20

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/account/commission"),
            query_params=[
                param[str]("symbol", symbol), param[int]("timestamp", timestamp), param[str]("signature", signature)
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ApiV3AccountCommissionResponse],
            error_mapper=query_commission_rates_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_current_order_count_usage_trade(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ApiV3RateLimitOrderResponse], QueryCurrentOrderCountUsageTradeErrorBody]:
        """Displays the user's current order count usage for all intervals.

        Weight(IP): 40

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/rateLimit/order"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[ApiV3RateLimitOrderResponse]],
            error_mapper=query_current_order_count_usage_trade_error_mapper,
            request_options=request_options,
        )

    async def query_oco_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        order_list_id: int | None = None,
        orig_client_order_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV3OrderListResponse, QueryOcoUserDataErrorBody]:
        """Retrieves a specific OCO based on provided optional parameters

        Weight(IP): 4

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_list_id: Order list id
            orig_client_order_id: Order id from client
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/orderList"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("orderListId", order_list_id),
                param[str | None]("origClientOrderId", orig_client_order_id),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ApiV3OrderListResponse],
            error_mapper=query_oco_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_open_oco_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ApiV3OpenOrderListResponse], QueryOpenOcoUserDataErrorBody]:
        """Weight(IP): 6

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/openOrderList"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[ApiV3OpenOrderListResponse]],
            error_mapper=query_open_oco_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_order_user_data(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        orig_client_order_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OrderDetails, QueryOrderUserDataErrorBody]:
        """Check an order's status.

        - Either ``orderId`` or ``origClientOrderId`` must be sent.
        - For some historical orders ``cummulativeQuoteQty`` will be < 0, meaning the data is not available at this
            time.

        Weight(IP): 4

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order id
            orig_client_order_id: Order id from client
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/order"),
            query_params=[
                param[str]("symbol", symbol),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("orderId", order_id),
                param[str | None]("origClientOrderId", orig_client_order_id),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[OrderDetails],
            error_mapper=query_order_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_prevented_matches(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        prevented_match_id: int | None = None,
        order_id: int | None = None,
        from_prevented_match_id: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ApiV3MyPreventedMatchesResponse], QueryPreventedMatchesErrorBody]:
        """Displays the list of orders that were expired because of STP.

        For additional information on what a Prevented match is, as well as Self Trade Prevention (STP), please refer to
        our STP FAQ page.

        These are the combinations supported:

        * symbol + preventedMatchId
        * symbol + orderId
        * symbol + orderId + fromPreventedMatchId (limit will default to 500)
        * symbol + orderId + fromPreventedMatchId + limit

        Weight(IP):

        Case Weight If symbol is invalid: 2 Querying by preventedMatchId: 2 Querying by orderId: 20

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            prevented_match_id: Value sent with the request.
            order_id: Order id
            from_prevented_match_id: Value sent with the request.
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/myPreventedMatches"),
            query_params=[
                param[str]("symbol", symbol),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("preventedMatchId", prevented_match_id),
                param[int | None]("orderId", order_id),
                param[int | None]("fromPreventedMatchId", from_prevented_match_id),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[ApiV3MyPreventedMatchesResponse]],
            error_mapper=query_prevented_matches_error_mapper,
            request_options=request_options,
        )

    async def query_all_oco_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        from_id: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ApiV3AllOrderListResponse], QueryAllOcoUserDataErrorBody]:
        """Retrieves all OCO based on provided optional parameters

        Weight(IP): 20

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            from_id: Trade id to fetch from. Default gets most recent trades.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/allOrderList"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("fromId", from_id),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[ApiV3AllOrderListResponse]],
            error_mapper=query_all_oco_user_data_error_mapper,
            request_options=request_options,
        )

    async def test_new_order_trade(
        self,
        symbol: str,
        side: SideOrStr,
        type_: Type1OrStr,
        timestamp: int,
        signature: str,
        *,
        time_in_force: TimeInForceOrStr | None = None,
        quantity: float | None = None,
        quote_order_qty: float | None = None,
        price: float | None = None,
        new_client_order_id: str | None = None,
        strategy_id: int | None = None,
        strategy_type: int | None = None,
        stop_price: float | None = None,
        trailing_delta: float | None = None,
        iceberg_qty: float | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        recv_window: int | None = None,
        compute_commission_rates: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, TestNewOrderTradeErrorBody]:
        """Test new order creation and signature/recvWindow long. Creates and validates a new order but does not send it
        into the matching engine.

        Weight(IP):
          - Without computeCommissionRates: ``1``
          - With computeCommissionRates: ``20``

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            type_: Order type
            timestamp: UTC timestamp in ms
            signature: Signature
            time_in_force: Order time in force
            quantity: Order quantity
            quote_order_qty: Quote quantity
            price: Order price
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            strategy_id: Value sent with the request.
            strategy_type: The value cannot be less than 1000000.
            stop_price: Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
            trailing_delta: Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
            iceberg_qty: Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.
            new_order_resp_type: Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders
                default to ACK.
            recv_window: The value cannot be greater than 60000
            compute_commission_rates: Default: false
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/v3/order/test"),
            query_params=[
                param[str]("symbol", symbol),
                param[SideOrStr]("side", side),
                param[Type1OrStr]("type", type_),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[TimeInForceOrStr | None]("timeInForce", time_in_force),
                param[float | None]("quantity", quantity),
                param[float | None]("quoteOrderQty", quote_order_qty),
                param[float | None]("price", price),
                param[str | None]("newClientOrderId", new_client_order_id),
                param[int | None]("strategyId", strategy_id),
                param[int | None]("strategyType", strategy_type),
                param[float | None]("stopPrice", stop_price),
                param[float | None]("trailingDelta", trailing_delta),
                param[float | None]("icebergQty", iceberg_qty),
                param[NewOrderRespTypeOrStr | None]("newOrderRespType", new_order_resp_type),
                param[int | None]("recvWindow", recv_window),
                param[bool | None]("computeCommissionRates", compute_commission_rates),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[Any],
            error_mapper=test_new_order_trade_error_mapper,
            request_options=request_options,
        )

    async def test_new_order_using_sor_trade(
        self,
        symbol: str,
        side: SideOrStr,
        type_: Type1OrStr,
        quantity: float,
        timestamp: int,
        signature: str,
        *,
        time_in_force: TimeInForceOrStr | None = None,
        price: float | None = None,
        new_client_order_id: str | None = None,
        strategy_id: int | None = None,
        strategy_type: int | None = None,
        iceberg_qty: float | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        compute_commission_rates: bool | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, TestNewOrderUsingSorTradeErrorBody]:
        """Test new order creation and signature/recvWindow using smart order routing (SOR). Creates and validates a new
        order but does not send it into the matching engine.

        Weight(IP):
          - Without computeCommissionRates: ``1``
          - With computeCommissionRates: ``20``

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            type_: Order type
            quantity: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            time_in_force: Order time in force
            price: Value sent with the request.
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            strategy_id: Value sent with the request.
            strategy_type: The value cannot be less than 1000000.
            iceberg_qty: Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.
            new_order_resp_type: Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders
                default to ACK.
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            compute_commission_rates: Default: false
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/v3/sor/order/test"),
            query_params=[
                param[str]("symbol", symbol),
                param[SideOrStr]("side", side),
                param[Type1OrStr]("type", type_),
                param[float]("quantity", quantity),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[TimeInForceOrStr | None]("timeInForce", time_in_force),
                param[float | None]("price", price),
                param[str | None]("newClientOrderId", new_client_order_id),
                param[int | None]("strategyId", strategy_id),
                param[int | None]("strategyType", strategy_type),
                param[float | None]("icebergQty", iceberg_qty),
                param[NewOrderRespTypeOrStr | None]("newOrderRespType", new_order_resp_type),
                param[SelfTradePreventionModeOrStr | None]("selfTradePreventionMode", self_trade_prevention_mode),
                param[bool | None]("computeCommissionRates", compute_commission_rates),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[Any],
            error_mapper=test_new_order_using_sor_trade_error_mapper,
            request_options=request_options,
        )
