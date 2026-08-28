from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder, param
from ..errors.cancel_algo_order_trade_error import CancelAlgoOrderTradeErrorBody, cancel_algo_order_trade_error_mapper
from ..errors.query_current_algo_open_orders_user_data_error import (
    QueryCurrentAlgoOpenOrdersUserDataErrorBody,
    query_current_algo_open_orders_user_data_error_mapper,
)
from ..errors.query_historical_algo_orders_user_data_error import (
    QueryHistoricalAlgoOrdersUserDataErrorBody,
    query_historical_algo_orders_user_data_error_mapper,
)
from ..errors.query_sub_orders_user_data_error import (
    QuerySubOrdersUserDataErrorBody,
    query_sub_orders_user_data_error_mapper,
)
from ..errors.time_weighted_average_price_twap_new_order_trade_error import (
    TimeWeightedAveragePriceTwapNewOrderTradeErrorBody,
    time_weighted_average_price_twap_new_order_trade_error_mapper,
)
from ..errors.volume_participation_vp_new_order_trade_error import (
    VolumeParticipationVpNewOrderTradeErrorBody,
    volume_participation_vp_new_order_trade_error_mapper,
)
from ..models.enums.position_side import PositionSideOrStr
from ..models.enums.side import SideOrStr
from ..models.enums.urgency import UrgencyOrStr
from ..models.sapi_v1_algo_futures_historical_orders_response import SapiV1AlgoFuturesHistoricalOrdersResponse
from ..models.sapi_v1_algo_futures_new_order_twap_response import SapiV1AlgoFuturesNewOrderTwapResponse
from ..models.sapi_v1_algo_futures_new_order_vp_response import SapiV1AlgoFuturesNewOrderVpResponse
from ..models.sapi_v1_algo_futures_open_orders_response import SapiV1AlgoFuturesOpenOrdersResponse
from ..models.sapi_v1_algo_futures_order_response import SapiV1AlgoFuturesOrderResponse
from ..models.sapi_v1_algo_futures_sub_orders_response import SapiV1AlgoFuturesSubOrdersResponse
from ..server.server import Server


class FuturesAlgo:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FuturesAlgoWithRawResponse(client, server, auth)

    def cancel_algo_order_trade(
        self,
        algo_id: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AlgoFuturesOrderResponse:
        """Cancel an active order.
        - You need to enable Futures Trading Permission for the api key which requests this endpoint.
        - Base URL: https://api.binance.com

        Weight(IP): 1

        Args:
            algo_id: Eg. 14511
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Cancelled order

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.cancel_algo_order_trade(
            algo_id, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def query_current_algo_open_orders_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AlgoFuturesOpenOrdersResponse:
        """- You need to enable Futures Trading Permission for the api key which requests this endpoint.
        - Base URL: https://api.binance.com

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Open Algo Orders

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_current_algo_open_orders_user_data(
            timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def query_historical_algo_orders_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        symbol: str | None = None,
        side: SideOrStr | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        page_size: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AlgoFuturesHistoricalOrdersResponse:
        """- You need to enable Futures Trading Permission for the api key which requests this endpoint.
        - Base URL: https://api.binance.com

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            page: Default 1
            page_size: MIN 1, MAX 100; Default 100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Historical Algo Orders

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_historical_algo_orders_user_data(
            timestamp,
            signature,
            symbol=symbol,
            side=side,
            start_time=start_time,
            end_time=end_time,
            page=page,
            page_size=page_size,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def query_sub_orders_user_data(
        self,
        algo_id: int,
        timestamp: int,
        signature: str,
        *,
        page: int | None = None,
        page_size: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AlgoFuturesSubOrdersResponse:
        """- You need to enable Futures Trading Permission for the api key which requests this endpoint.
        - Base URL: https://api.binance.com

        Weight(IP): 1

        Args:
            algo_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            page: Default 1
            page_size: MIN 1, MAX 100; Default 100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Sub orders

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_sub_orders_user_data(
            algo_id,
            timestamp,
            signature,
            page=page,
            page_size=page_size,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def time_weighted_average_price_twap_new_order_trade(
        self,
        symbol: str,
        side: SideOrStr,
        quantity: float,
        duration: int,
        timestamp: int,
        signature: str,
        *,
        position_side: PositionSideOrStr | None = None,
        client_algo_id: str | None = None,
        reduce_only: bool | None = None,
        limit_price: float | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AlgoFuturesNewOrderTwapResponse:
        """Send in a Twap new order. Only support on USDⓈ-M Contracts.

        You need to enable Futures Trading Permission for the api key which requests this endpoint. Base URL:
        https://api.binance.com

        - Total Algo open orders max allowed: 10 orders.
        - Leverage of symbols and position mode will be the same as your futures account settings. You can set up
            through the trading page or fapi.
        - Receiving "success": true does not mean that your order will be executed. Please use the query order
            endpoints(GET sapi/v1/algo/futures/openOrders or GET sapi/v1/algo/futures/historicalOrders) to check the
            order status. For example: Your futures balance is insufficient, or open position with reduce only or
            position side is inconsistent with your own setting. In these cases you will receive "success": true, but
            the order status will be expired after we check it.
        - quantity * 60 / duration should be larger than minQty
        - duration cannot be less than 5 mins or more than 24 hours.
        - For delivery contracts, TWAP end time should be one hour earlier than the delivery time of the symbol.

        Weight(UID): 3000

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            quantity: Quantity of base asset; The notional (quantity * mark price(base asset)) must be more than the
                equivalent of 10,000 USDT and less than the equivalent of 1,000,000 USDT
            duration: Duration for TWAP orders in seconds. [300, 86400];Less than 5min => defaults to 5 min; Greater
                than 24h => defaults to 24h
            timestamp: UTC timestamp in ms
            signature: Signature
            position_side: Default BOTH for One-way Mode ; LONG or SHORT for Hedge Mode. It must be sent in Hedge Mode.
            client_algo_id: A unique id among Algo orders (length should be 32 characters)， If it is not sent, we will
                give default value
            reduce_only: 'true' or 'false'. Default 'false'; Cannot be sent in Hedge Mode; Cannot be sent when you open
                a position
            limit_price: Limit price of the order; If it is not sent, will place order by market price by default
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Time-Weighted Average Price(Twap) New Order

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.time_weighted_average_price_twap_new_order_trade(
            symbol,
            side,
            quantity,
            duration,
            timestamp,
            signature,
            position_side=position_side,
            client_algo_id=client_algo_id,
            reduce_only=reduce_only,
            limit_price=limit_price,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def volume_participation_vp_new_order_trade(
        self,
        symbol: str,
        side: SideOrStr,
        quantity: float,
        urgency: UrgencyOrStr,
        timestamp: int,
        signature: str,
        *,
        position_side: PositionSideOrStr | None = None,
        client_algo_id: str | None = None,
        reduce_only: bool | None = None,
        limit_price: float | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AlgoFuturesNewOrderVpResponse:
        """Send in a VP new order. Only support on USDⓈ-M Contracts.

        - You need to enable ``Futures Trading Permission`` for the api key which requests this endpoint.
        - Base URL: https://api.binance.com

        - Total Algo open orders max allowed: 10 orders.
        - Leverage of symbols and position mode will be the same as your futures account settings. You can set up
            through the trading page or fapi.
        - Receiving "success": true does not mean that your order will be executed. Please use the query order
            endpoints(GET sapi/v1/algo/futures/openOrders or GET sapi/v1/algo/futures/historicalOrders) to check the
            order status. For example: Your futures balance is insufficient, or open position with reduce only or
            position side is inconsistent with your own setting. In these cases you will receive "success": true, but
            the order status will be expired after we check it.

        Weight(UID): 3000

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            quantity: Quantity of base asset; The notional (quantity * mark price(base asset)) must be more than the
                equivalent of 10,000 USDT and less than the equivalent of 1,000,000 USDT
            urgency: Represent the relative speed of the current execution; ENUM: LOW, MEDIUM, HIGH
            timestamp: UTC timestamp in ms
            signature: Signature
            position_side: Default BOTH for One-way Mode ; LONG or SHORT for Hedge Mode. It must be sent in Hedge Mode.
            client_algo_id: A unique id among Algo orders (length should be 32 characters)， If it is not sent, we will
                give default value
            reduce_only: 'true' or 'false'. Default 'false'; Cannot be sent in Hedge Mode; Cannot be sent when you open
                a position
            limit_price: Limit price of the order; If it is not sent, will place order by market price by default
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Volume Participation(VP) Order

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.volume_participation_vp_new_order_trade(
            symbol,
            side,
            quantity,
            urgency,
            timestamp,
            signature,
            position_side=position_side,
            client_algo_id=client_algo_id,
            reduce_only=reduce_only,
            limit_price=limit_price,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> FuturesAlgoWithRawResponse:
        return self._with_raw_response


class AsyncFuturesAlgo:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFuturesAlgoWithRawResponse(client, server, auth)

    async def cancel_algo_order_trade(
        self,
        algo_id: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AlgoFuturesOrderResponse:
        """Cancel an active order.
        - You need to enable Futures Trading Permission for the api key which requests this endpoint.
        - Base URL: https://api.binance.com

        Weight(IP): 1

        Args:
            algo_id: Eg. 14511
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Cancelled order

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.cancel_algo_order_trade(
                algo_id, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def query_current_algo_open_orders_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AlgoFuturesOpenOrdersResponse:
        """- You need to enable Futures Trading Permission for the api key which requests this endpoint.
        - Base URL: https://api.binance.com

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Open Algo Orders

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_current_algo_open_orders_user_data(
                timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def query_historical_algo_orders_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        symbol: str | None = None,
        side: SideOrStr | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        page_size: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AlgoFuturesHistoricalOrdersResponse:
        """- You need to enable Futures Trading Permission for the api key which requests this endpoint.
        - Base URL: https://api.binance.com

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            page: Default 1
            page_size: MIN 1, MAX 100; Default 100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Historical Algo Orders

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_historical_algo_orders_user_data(
                timestamp,
                signature,
                symbol=symbol,
                side=side,
                start_time=start_time,
                end_time=end_time,
                page=page,
                page_size=page_size,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def query_sub_orders_user_data(
        self,
        algo_id: int,
        timestamp: int,
        signature: str,
        *,
        page: int | None = None,
        page_size: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AlgoFuturesSubOrdersResponse:
        """- You need to enable Futures Trading Permission for the api key which requests this endpoint.
        - Base URL: https://api.binance.com

        Weight(IP): 1

        Args:
            algo_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            page: Default 1
            page_size: MIN 1, MAX 100; Default 100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Sub orders

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_sub_orders_user_data(
                algo_id,
                timestamp,
                signature,
                page=page,
                page_size=page_size,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def time_weighted_average_price_twap_new_order_trade(
        self,
        symbol: str,
        side: SideOrStr,
        quantity: float,
        duration: int,
        timestamp: int,
        signature: str,
        *,
        position_side: PositionSideOrStr | None = None,
        client_algo_id: str | None = None,
        reduce_only: bool | None = None,
        limit_price: float | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AlgoFuturesNewOrderTwapResponse:
        """Send in a Twap new order. Only support on USDⓈ-M Contracts.

        You need to enable Futures Trading Permission for the api key which requests this endpoint. Base URL:
        https://api.binance.com

        - Total Algo open orders max allowed: 10 orders.
        - Leverage of symbols and position mode will be the same as your futures account settings. You can set up
            through the trading page or fapi.
        - Receiving "success": true does not mean that your order will be executed. Please use the query order
            endpoints(GET sapi/v1/algo/futures/openOrders or GET sapi/v1/algo/futures/historicalOrders) to check the
            order status. For example: Your futures balance is insufficient, or open position with reduce only or
            position side is inconsistent with your own setting. In these cases you will receive "success": true, but
            the order status will be expired after we check it.
        - quantity * 60 / duration should be larger than minQty
        - duration cannot be less than 5 mins or more than 24 hours.
        - For delivery contracts, TWAP end time should be one hour earlier than the delivery time of the symbol.

        Weight(UID): 3000

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            quantity: Quantity of base asset; The notional (quantity * mark price(base asset)) must be more than the
                equivalent of 10,000 USDT and less than the equivalent of 1,000,000 USDT
            duration: Duration for TWAP orders in seconds. [300, 86400];Less than 5min => defaults to 5 min; Greater
                than 24h => defaults to 24h
            timestamp: UTC timestamp in ms
            signature: Signature
            position_side: Default BOTH for One-way Mode ; LONG or SHORT for Hedge Mode. It must be sent in Hedge Mode.
            client_algo_id: A unique id among Algo orders (length should be 32 characters)， If it is not sent, we will
                give default value
            reduce_only: 'true' or 'false'. Default 'false'; Cannot be sent in Hedge Mode; Cannot be sent when you open
                a position
            limit_price: Limit price of the order; If it is not sent, will place order by market price by default
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Time-Weighted Average Price(Twap) New Order

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.time_weighted_average_price_twap_new_order_trade(
                symbol,
                side,
                quantity,
                duration,
                timestamp,
                signature,
                position_side=position_side,
                client_algo_id=client_algo_id,
                reduce_only=reduce_only,
                limit_price=limit_price,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def volume_participation_vp_new_order_trade(
        self,
        symbol: str,
        side: SideOrStr,
        quantity: float,
        urgency: UrgencyOrStr,
        timestamp: int,
        signature: str,
        *,
        position_side: PositionSideOrStr | None = None,
        client_algo_id: str | None = None,
        reduce_only: bool | None = None,
        limit_price: float | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AlgoFuturesNewOrderVpResponse:
        """Send in a VP new order. Only support on USDⓈ-M Contracts.

        - You need to enable ``Futures Trading Permission`` for the api key which requests this endpoint.
        - Base URL: https://api.binance.com

        - Total Algo open orders max allowed: 10 orders.
        - Leverage of symbols and position mode will be the same as your futures account settings. You can set up
            through the trading page or fapi.
        - Receiving "success": true does not mean that your order will be executed. Please use the query order
            endpoints(GET sapi/v1/algo/futures/openOrders or GET sapi/v1/algo/futures/historicalOrders) to check the
            order status. For example: Your futures balance is insufficient, or open position with reduce only or
            position side is inconsistent with your own setting. In these cases you will receive "success": true, but
            the order status will be expired after we check it.

        Weight(UID): 3000

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            quantity: Quantity of base asset; The notional (quantity * mark price(base asset)) must be more than the
                equivalent of 10,000 USDT and less than the equivalent of 1,000,000 USDT
            urgency: Represent the relative speed of the current execution; ENUM: LOW, MEDIUM, HIGH
            timestamp: UTC timestamp in ms
            signature: Signature
            position_side: Default BOTH for One-way Mode ; LONG or SHORT for Hedge Mode. It must be sent in Hedge Mode.
            client_algo_id: A unique id among Algo orders (length should be 32 characters)， If it is not sent, we will
                give default value
            reduce_only: 'true' or 'false'. Default 'false'; Cannot be sent in Hedge Mode; Cannot be sent when you open
                a position
            limit_price: Limit price of the order; If it is not sent, will place order by market price by default
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Volume Participation(VP) Order

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.volume_participation_vp_new_order_trade(
                symbol,
                side,
                quantity,
                urgency,
                timestamp,
                signature,
                position_side=position_side,
                client_algo_id=client_algo_id,
                reduce_only=reduce_only,
                limit_price=limit_price,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncFuturesAlgoWithRawResponse:
        return self._with_raw_response


class FuturesAlgoWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def cancel_algo_order_trade(
        self,
        algo_id: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AlgoFuturesOrderResponse, CancelAlgoOrderTradeErrorBody]:
        """Cancel an active order.
        - You need to enable Futures Trading Permission for the api key which requests this endpoint.
        - Base URL: https://api.binance.com

        Weight(IP): 1

        Args:
            algo_id: Eg. 14511
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/sapi/v1/algo/futures/order"),
            query_params=[
                param[int]("algoId", algo_id),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AlgoFuturesOrderResponse],
            error_mapper=cancel_algo_order_trade_error_mapper,
            request_options=request_options,
        )

    def query_current_algo_open_orders_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AlgoFuturesOpenOrdersResponse, QueryCurrentAlgoOpenOrdersUserDataErrorBody]:
        """- You need to enable Futures Trading Permission for the api key which requests this endpoint.
        - Base URL: https://api.binance.com

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/algo/futures/openOrders"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AlgoFuturesOpenOrdersResponse],
            error_mapper=query_current_algo_open_orders_user_data_error_mapper,
            request_options=request_options,
        )

    def query_historical_algo_orders_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        symbol: str | None = None,
        side: SideOrStr | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        page_size: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AlgoFuturesHistoricalOrdersResponse, QueryHistoricalAlgoOrdersUserDataErrorBody]:
        """- You need to enable Futures Trading Permission for the api key which requests this endpoint.
        - Base URL: https://api.binance.com

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            page: Default 1
            page_size: MIN 1, MAX 100; Default 100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/algo/futures/historicalOrders"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("symbol", symbol),
                param[SideOrStr | None]("side", side),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("page", page),
                param[str | None]("pageSize", page_size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AlgoFuturesHistoricalOrdersResponse],
            error_mapper=query_historical_algo_orders_user_data_error_mapper,
            request_options=request_options,
        )

    def query_sub_orders_user_data(
        self,
        algo_id: int,
        timestamp: int,
        signature: str,
        *,
        page: int | None = None,
        page_size: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AlgoFuturesSubOrdersResponse, QuerySubOrdersUserDataErrorBody]:
        """- You need to enable Futures Trading Permission for the api key which requests this endpoint.
        - Base URL: https://api.binance.com

        Weight(IP): 1

        Args:
            algo_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            page: Default 1
            page_size: MIN 1, MAX 100; Default 100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/algo/futures/subOrders"),
            query_params=[
                param[int]("algoId", algo_id),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("page", page),
                param[str | None]("pageSize", page_size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AlgoFuturesSubOrdersResponse],
            error_mapper=query_sub_orders_user_data_error_mapper,
            request_options=request_options,
        )

    def time_weighted_average_price_twap_new_order_trade(
        self,
        symbol: str,
        side: SideOrStr,
        quantity: float,
        duration: int,
        timestamp: int,
        signature: str,
        *,
        position_side: PositionSideOrStr | None = None,
        client_algo_id: str | None = None,
        reduce_only: bool | None = None,
        limit_price: float | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AlgoFuturesNewOrderTwapResponse, TimeWeightedAveragePriceTwapNewOrderTradeErrorBody]:
        """Send in a Twap new order. Only support on USDⓈ-M Contracts.

        You need to enable Futures Trading Permission for the api key which requests this endpoint. Base URL:
        https://api.binance.com

        - Total Algo open orders max allowed: 10 orders.
        - Leverage of symbols and position mode will be the same as your futures account settings. You can set up
            through the trading page or fapi.
        - Receiving "success": true does not mean that your order will be executed. Please use the query order
            endpoints(GET sapi/v1/algo/futures/openOrders or GET sapi/v1/algo/futures/historicalOrders) to check the
            order status. For example: Your futures balance is insufficient, or open position with reduce only or
            position side is inconsistent with your own setting. In these cases you will receive "success": true, but
            the order status will be expired after we check it.
        - quantity * 60 / duration should be larger than minQty
        - duration cannot be less than 5 mins or more than 24 hours.
        - For delivery contracts, TWAP end time should be one hour earlier than the delivery time of the symbol.

        Weight(UID): 3000

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            quantity: Quantity of base asset; The notional (quantity * mark price(base asset)) must be more than the
                equivalent of 10,000 USDT and less than the equivalent of 1,000,000 USDT
            duration: Duration for TWAP orders in seconds. [300, 86400];Less than 5min => defaults to 5 min; Greater
                than 24h => defaults to 24h
            timestamp: UTC timestamp in ms
            signature: Signature
            position_side: Default BOTH for One-way Mode ; LONG or SHORT for Hedge Mode. It must be sent in Hedge Mode.
            client_algo_id: A unique id among Algo orders (length should be 32 characters)， If it is not sent, we will
                give default value
            reduce_only: 'true' or 'false'. Default 'false'; Cannot be sent in Hedge Mode; Cannot be sent when you open
                a position
            limit_price: Limit price of the order; If it is not sent, will place order by market price by default
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/algo/futures/newOrderTwap"),
            query_params=[
                param[str]("symbol", symbol),
                param[SideOrStr]("side", side),
                param[float]("quantity", quantity),
                param[int]("duration", duration),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[PositionSideOrStr | None]("positionSide", position_side),
                param[str | None]("clientAlgoId", client_algo_id),
                param[bool | None]("reduceOnly", reduce_only),
                param[float | None]("limitPrice", limit_price),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AlgoFuturesNewOrderTwapResponse],
            error_mapper=time_weighted_average_price_twap_new_order_trade_error_mapper,
            request_options=request_options,
        )

    def volume_participation_vp_new_order_trade(
        self,
        symbol: str,
        side: SideOrStr,
        quantity: float,
        urgency: UrgencyOrStr,
        timestamp: int,
        signature: str,
        *,
        position_side: PositionSideOrStr | None = None,
        client_algo_id: str | None = None,
        reduce_only: bool | None = None,
        limit_price: float | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AlgoFuturesNewOrderVpResponse, VolumeParticipationVpNewOrderTradeErrorBody]:
        """Send in a VP new order. Only support on USDⓈ-M Contracts.

        - You need to enable ``Futures Trading Permission`` for the api key which requests this endpoint.
        - Base URL: https://api.binance.com

        - Total Algo open orders max allowed: 10 orders.
        - Leverage of symbols and position mode will be the same as your futures account settings. You can set up
            through the trading page or fapi.
        - Receiving "success": true does not mean that your order will be executed. Please use the query order
            endpoints(GET sapi/v1/algo/futures/openOrders or GET sapi/v1/algo/futures/historicalOrders) to check the
            order status. For example: Your futures balance is insufficient, or open position with reduce only or
            position side is inconsistent with your own setting. In these cases you will receive "success": true, but
            the order status will be expired after we check it.

        Weight(UID): 3000

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            quantity: Quantity of base asset; The notional (quantity * mark price(base asset)) must be more than the
                equivalent of 10,000 USDT and less than the equivalent of 1,000,000 USDT
            urgency: Represent the relative speed of the current execution; ENUM: LOW, MEDIUM, HIGH
            timestamp: UTC timestamp in ms
            signature: Signature
            position_side: Default BOTH for One-way Mode ; LONG or SHORT for Hedge Mode. It must be sent in Hedge Mode.
            client_algo_id: A unique id among Algo orders (length should be 32 characters)， If it is not sent, we will
                give default value
            reduce_only: 'true' or 'false'. Default 'false'; Cannot be sent in Hedge Mode; Cannot be sent when you open
                a position
            limit_price: Limit price of the order; If it is not sent, will place order by market price by default
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/algo/futures/newOrderVp"),
            query_params=[
                param[str]("symbol", symbol),
                param[SideOrStr]("side", side),
                param[float]("quantity", quantity),
                param[UrgencyOrStr]("urgency", urgency),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[PositionSideOrStr | None]("positionSide", position_side),
                param[str | None]("clientAlgoId", client_algo_id),
                param[bool | None]("reduceOnly", reduce_only),
                param[float | None]("limitPrice", limit_price),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AlgoFuturesNewOrderVpResponse],
            error_mapper=volume_participation_vp_new_order_trade_error_mapper,
            request_options=request_options,
        )


class AsyncFuturesAlgoWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def cancel_algo_order_trade(
        self,
        algo_id: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AlgoFuturesOrderResponse, CancelAlgoOrderTradeErrorBody]:
        """Cancel an active order.
        - You need to enable Futures Trading Permission for the api key which requests this endpoint.
        - Base URL: https://api.binance.com

        Weight(IP): 1

        Args:
            algo_id: Eg. 14511
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/sapi/v1/algo/futures/order"),
            query_params=[
                param[int]("algoId", algo_id),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AlgoFuturesOrderResponse],
            error_mapper=cancel_algo_order_trade_error_mapper,
            request_options=request_options,
        )

    async def query_current_algo_open_orders_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AlgoFuturesOpenOrdersResponse, QueryCurrentAlgoOpenOrdersUserDataErrorBody]:
        """- You need to enable Futures Trading Permission for the api key which requests this endpoint.
        - Base URL: https://api.binance.com

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/algo/futures/openOrders"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AlgoFuturesOpenOrdersResponse],
            error_mapper=query_current_algo_open_orders_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_historical_algo_orders_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        symbol: str | None = None,
        side: SideOrStr | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        page_size: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AlgoFuturesHistoricalOrdersResponse, QueryHistoricalAlgoOrdersUserDataErrorBody]:
        """- You need to enable Futures Trading Permission for the api key which requests this endpoint.
        - Base URL: https://api.binance.com

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            page: Default 1
            page_size: MIN 1, MAX 100; Default 100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/algo/futures/historicalOrders"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("symbol", symbol),
                param[SideOrStr | None]("side", side),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("page", page),
                param[str | None]("pageSize", page_size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AlgoFuturesHistoricalOrdersResponse],
            error_mapper=query_historical_algo_orders_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_sub_orders_user_data(
        self,
        algo_id: int,
        timestamp: int,
        signature: str,
        *,
        page: int | None = None,
        page_size: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AlgoFuturesSubOrdersResponse, QuerySubOrdersUserDataErrorBody]:
        """- You need to enable Futures Trading Permission for the api key which requests this endpoint.
        - Base URL: https://api.binance.com

        Weight(IP): 1

        Args:
            algo_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            page: Default 1
            page_size: MIN 1, MAX 100; Default 100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/algo/futures/subOrders"),
            query_params=[
                param[int]("algoId", algo_id),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("page", page),
                param[str | None]("pageSize", page_size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AlgoFuturesSubOrdersResponse],
            error_mapper=query_sub_orders_user_data_error_mapper,
            request_options=request_options,
        )

    async def time_weighted_average_price_twap_new_order_trade(
        self,
        symbol: str,
        side: SideOrStr,
        quantity: float,
        duration: int,
        timestamp: int,
        signature: str,
        *,
        position_side: PositionSideOrStr | None = None,
        client_algo_id: str | None = None,
        reduce_only: bool | None = None,
        limit_price: float | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AlgoFuturesNewOrderTwapResponse, TimeWeightedAveragePriceTwapNewOrderTradeErrorBody]:
        """Send in a Twap new order. Only support on USDⓈ-M Contracts.

        You need to enable Futures Trading Permission for the api key which requests this endpoint. Base URL:
        https://api.binance.com

        - Total Algo open orders max allowed: 10 orders.
        - Leverage of symbols and position mode will be the same as your futures account settings. You can set up
            through the trading page or fapi.
        - Receiving "success": true does not mean that your order will be executed. Please use the query order
            endpoints(GET sapi/v1/algo/futures/openOrders or GET sapi/v1/algo/futures/historicalOrders) to check the
            order status. For example: Your futures balance is insufficient, or open position with reduce only or
            position side is inconsistent with your own setting. In these cases you will receive "success": true, but
            the order status will be expired after we check it.
        - quantity * 60 / duration should be larger than minQty
        - duration cannot be less than 5 mins or more than 24 hours.
        - For delivery contracts, TWAP end time should be one hour earlier than the delivery time of the symbol.

        Weight(UID): 3000

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            quantity: Quantity of base asset; The notional (quantity * mark price(base asset)) must be more than the
                equivalent of 10,000 USDT and less than the equivalent of 1,000,000 USDT
            duration: Duration for TWAP orders in seconds. [300, 86400];Less than 5min => defaults to 5 min; Greater
                than 24h => defaults to 24h
            timestamp: UTC timestamp in ms
            signature: Signature
            position_side: Default BOTH for One-way Mode ; LONG or SHORT for Hedge Mode. It must be sent in Hedge Mode.
            client_algo_id: A unique id among Algo orders (length should be 32 characters)， If it is not sent, we will
                give default value
            reduce_only: 'true' or 'false'. Default 'false'; Cannot be sent in Hedge Mode; Cannot be sent when you open
                a position
            limit_price: Limit price of the order; If it is not sent, will place order by market price by default
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/algo/futures/newOrderTwap"),
            query_params=[
                param[str]("symbol", symbol),
                param[SideOrStr]("side", side),
                param[float]("quantity", quantity),
                param[int]("duration", duration),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[PositionSideOrStr | None]("positionSide", position_side),
                param[str | None]("clientAlgoId", client_algo_id),
                param[bool | None]("reduceOnly", reduce_only),
                param[float | None]("limitPrice", limit_price),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AlgoFuturesNewOrderTwapResponse],
            error_mapper=time_weighted_average_price_twap_new_order_trade_error_mapper,
            request_options=request_options,
        )

    async def volume_participation_vp_new_order_trade(
        self,
        symbol: str,
        side: SideOrStr,
        quantity: float,
        urgency: UrgencyOrStr,
        timestamp: int,
        signature: str,
        *,
        position_side: PositionSideOrStr | None = None,
        client_algo_id: str | None = None,
        reduce_only: bool | None = None,
        limit_price: float | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AlgoFuturesNewOrderVpResponse, VolumeParticipationVpNewOrderTradeErrorBody]:
        """Send in a VP new order. Only support on USDⓈ-M Contracts.

        - You need to enable ``Futures Trading Permission`` for the api key which requests this endpoint.
        - Base URL: https://api.binance.com

        - Total Algo open orders max allowed: 10 orders.
        - Leverage of symbols and position mode will be the same as your futures account settings. You can set up
            through the trading page or fapi.
        - Receiving "success": true does not mean that your order will be executed. Please use the query order
            endpoints(GET sapi/v1/algo/futures/openOrders or GET sapi/v1/algo/futures/historicalOrders) to check the
            order status. For example: Your futures balance is insufficient, or open position with reduce only or
            position side is inconsistent with your own setting. In these cases you will receive "success": true, but
            the order status will be expired after we check it.

        Weight(UID): 3000

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            quantity: Quantity of base asset; The notional (quantity * mark price(base asset)) must be more than the
                equivalent of 10,000 USDT and less than the equivalent of 1,000,000 USDT
            urgency: Represent the relative speed of the current execution; ENUM: LOW, MEDIUM, HIGH
            timestamp: UTC timestamp in ms
            signature: Signature
            position_side: Default BOTH for One-way Mode ; LONG or SHORT for Hedge Mode. It must be sent in Hedge Mode.
            client_algo_id: A unique id among Algo orders (length should be 32 characters)， If it is not sent, we will
                give default value
            reduce_only: 'true' or 'false'. Default 'false'; Cannot be sent in Hedge Mode; Cannot be sent when you open
                a position
            limit_price: Limit price of the order; If it is not sent, will place order by market price by default
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/algo/futures/newOrderVp"),
            query_params=[
                param[str]("symbol", symbol),
                param[SideOrStr]("side", side),
                param[float]("quantity", quantity),
                param[UrgencyOrStr]("urgency", urgency),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[PositionSideOrStr | None]("positionSide", position_side),
                param[str | None]("clientAlgoId", client_algo_id),
                param[bool | None]("reduceOnly", reduce_only),
                param[float | None]("limitPrice", limit_price),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AlgoFuturesNewOrderVpResponse],
            error_mapper=volume_participation_vp_new_order_trade_error_mapper,
            request_options=request_options,
        )
