from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder, param
from ..errors.cancel_algo_order_error import CancelAlgoOrderErrorBody, cancel_algo_order_error_mapper
from ..errors.query_current_algo_open_orders_error import (
    QueryCurrentAlgoOpenOrdersErrorBody,
    query_current_algo_open_orders_error_mapper,
)
from ..errors.query_historical_algo_orders_error import (
    QueryHistoricalAlgoOrdersErrorBody,
    query_historical_algo_orders_error_mapper,
)
from ..errors.query_sub_orders_error import QuerySubOrdersErrorBody, query_sub_orders_error_mapper
from ..errors.time_weighted_average_price_twap_new_order_error import (
    TimeWeightedAveragePriceTwapNewOrderErrorBody,
    time_weighted_average_price_twap_new_order_error_mapper,
)
from ..models.enums.side import SideOrStr
from ..models.sapi_v1_algo_spot_historical_orders_response import SapiV1AlgoSpotHistoricalOrdersResponse
from ..models.sapi_v1_algo_spot_new_order_twap_response import SapiV1AlgoSpotNewOrderTwapResponse
from ..models.sapi_v1_algo_spot_open_orders_response import SapiV1AlgoSpotOpenOrdersResponse
from ..models.sapi_v1_algo_spot_order_response import SapiV1AlgoSpotOrderResponse
from ..models.sapi_v1_algo_spot_sub_orders_response import SapiV1AlgoSpotSubOrdersResponse
from ..server.server import Server


class SpotAlgo:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SpotAlgoWithRawResponse(client, server, auth)

    def cancel_algo_order(
        self,
        algo_id: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AlgoSpotOrderResponse:
        """Cancel an open TWAP order

        Weight(IP): 1

        Args:
            algo_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Cancelled twap order response

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.cancel_algo_order(
            algo_id, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def query_current_algo_open_orders(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AlgoSpotOpenOrdersResponse:
        """Get all open SPOT TWAP orders

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            twap open orders

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_current_algo_open_orders(
            timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def query_historical_algo_orders(
        self,
        symbol: str,
        side: SideOrStr,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        page_size: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AlgoSpotHistoricalOrdersResponse:
        """Get all historical SPOT TWAP orders

        Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            page: Default 1
            page_size: MIN 1, MAX 100; Default 100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            twap historical orders

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_historical_algo_orders(
            symbol,
            side,
            timestamp,
            signature,
            start_time=start_time,
            end_time=end_time,
            page=page,
            page_size=page_size,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def query_sub_orders(
        self,
        algo_id: int,
        timestamp: int,
        signature: str,
        *,
        page: int | None = None,
        page_size: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AlgoSpotSubOrdersResponse:
        """Get respective sub orders for a specified algoId

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
            twap sub orders

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_sub_orders(
            algo_id,
            timestamp,
            signature,
            page=page,
            page_size=page_size,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def time_weighted_average_price_twap_new_order(
        self,
        symbol: str,
        side: SideOrStr,
        quantity: float,
        duration: int,
        timestamp: int,
        signature: str,
        *,
        client_algo_id: str | None = None,
        limit_price: float | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AlgoSpotNewOrderTwapResponse:
        """Place a new spot TWAP order with Algo service.

        Weight(UID): 3000

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            quantity: Value sent with the request.
            duration: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            client_algo_id: Value sent with the request.
            limit_price: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            twap order response

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.time_weighted_average_price_twap_new_order(
            symbol,
            side,
            quantity,
            duration,
            timestamp,
            signature,
            client_algo_id=client_algo_id,
            limit_price=limit_price,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> SpotAlgoWithRawResponse:
        return self._with_raw_response


class AsyncSpotAlgo:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSpotAlgoWithRawResponse(client, server, auth)

    async def cancel_algo_order(
        self,
        algo_id: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AlgoSpotOrderResponse:
        """Cancel an open TWAP order

        Weight(IP): 1

        Args:
            algo_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Cancelled twap order response

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.cancel_algo_order(
                algo_id, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def query_current_algo_open_orders(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AlgoSpotOpenOrdersResponse:
        """Get all open SPOT TWAP orders

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            twap open orders

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_current_algo_open_orders(
                timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def query_historical_algo_orders(
        self,
        symbol: str,
        side: SideOrStr,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        page_size: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AlgoSpotHistoricalOrdersResponse:
        """Get all historical SPOT TWAP orders

        Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            page: Default 1
            page_size: MIN 1, MAX 100; Default 100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            twap historical orders

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_historical_algo_orders(
                symbol,
                side,
                timestamp,
                signature,
                start_time=start_time,
                end_time=end_time,
                page=page,
                page_size=page_size,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def query_sub_orders(
        self,
        algo_id: int,
        timestamp: int,
        signature: str,
        *,
        page: int | None = None,
        page_size: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AlgoSpotSubOrdersResponse:
        """Get respective sub orders for a specified algoId

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
            twap sub orders

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_sub_orders(
                algo_id,
                timestamp,
                signature,
                page=page,
                page_size=page_size,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def time_weighted_average_price_twap_new_order(
        self,
        symbol: str,
        side: SideOrStr,
        quantity: float,
        duration: int,
        timestamp: int,
        signature: str,
        *,
        client_algo_id: str | None = None,
        limit_price: float | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AlgoSpotNewOrderTwapResponse:
        """Place a new spot TWAP order with Algo service.

        Weight(UID): 3000

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            quantity: Value sent with the request.
            duration: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            client_algo_id: Value sent with the request.
            limit_price: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            twap order response

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.time_weighted_average_price_twap_new_order(
                symbol,
                side,
                quantity,
                duration,
                timestamp,
                signature,
                client_algo_id=client_algo_id,
                limit_price=limit_price,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSpotAlgoWithRawResponse:
        return self._with_raw_response


class SpotAlgoWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def cancel_algo_order(
        self,
        algo_id: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AlgoSpotOrderResponse, CancelAlgoOrderErrorBody]:
        """Cancel an open TWAP order

        Weight(IP): 1

        Args:
            algo_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/sapi/v1/algo/spot/order"),
            query_params=[
                param[int]("algoId", algo_id),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AlgoSpotOrderResponse],
            error_mapper=cancel_algo_order_error_mapper,
            request_options=request_options,
        )

    def query_current_algo_open_orders(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AlgoSpotOpenOrdersResponse, QueryCurrentAlgoOpenOrdersErrorBody]:
        """Get all open SPOT TWAP orders

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
            url_template=self._server.default("/sapi/v1/algo/spot/openOrders"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AlgoSpotOpenOrdersResponse],
            error_mapper=query_current_algo_open_orders_error_mapper,
            request_options=request_options,
        )

    def query_historical_algo_orders(
        self,
        symbol: str,
        side: SideOrStr,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        page_size: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AlgoSpotHistoricalOrdersResponse, QueryHistoricalAlgoOrdersErrorBody]:
        """Get all historical SPOT TWAP orders

        Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
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
            url_template=self._server.default("/sapi/v1/algo/spot/historicalOrders"),
            query_params=[
                param[str]("symbol", symbol),
                param[SideOrStr]("side", side),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("page", page),
                param[str | None]("pageSize", page_size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AlgoSpotHistoricalOrdersResponse],
            error_mapper=query_historical_algo_orders_error_mapper,
            request_options=request_options,
        )

    def query_sub_orders(
        self,
        algo_id: int,
        timestamp: int,
        signature: str,
        *,
        page: int | None = None,
        page_size: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AlgoSpotSubOrdersResponse, QuerySubOrdersErrorBody]:
        """Get respective sub orders for a specified algoId

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
            url_template=self._server.default("/sapi/v1/algo/spot/subOrders"),
            query_params=[
                param[int]("algoId", algo_id),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("page", page),
                param[str | None]("pageSize", page_size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AlgoSpotSubOrdersResponse],
            error_mapper=query_sub_orders_error_mapper,
            request_options=request_options,
        )

    def time_weighted_average_price_twap_new_order(
        self,
        symbol: str,
        side: SideOrStr,
        quantity: float,
        duration: int,
        timestamp: int,
        signature: str,
        *,
        client_algo_id: str | None = None,
        limit_price: float | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AlgoSpotNewOrderTwapResponse, TimeWeightedAveragePriceTwapNewOrderErrorBody]:
        """Place a new spot TWAP order with Algo service.

        Weight(UID): 3000

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            quantity: Value sent with the request.
            duration: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            client_algo_id: Value sent with the request.
            limit_price: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/algo/spot/newOrderTwap"),
            query_params=[
                param[str]("symbol", symbol),
                param[SideOrStr]("side", side),
                param[float]("quantity", quantity),
                param[int]("duration", duration),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("clientAlgoId", client_algo_id),
                param[float | None]("limitPrice", limit_price),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AlgoSpotNewOrderTwapResponse],
            error_mapper=time_weighted_average_price_twap_new_order_error_mapper,
            request_options=request_options,
        )


class AsyncSpotAlgoWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def cancel_algo_order(
        self,
        algo_id: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AlgoSpotOrderResponse, CancelAlgoOrderErrorBody]:
        """Cancel an open TWAP order

        Weight(IP): 1

        Args:
            algo_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/sapi/v1/algo/spot/order"),
            query_params=[
                param[int]("algoId", algo_id),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AlgoSpotOrderResponse],
            error_mapper=cancel_algo_order_error_mapper,
            request_options=request_options,
        )

    async def query_current_algo_open_orders(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AlgoSpotOpenOrdersResponse, QueryCurrentAlgoOpenOrdersErrorBody]:
        """Get all open SPOT TWAP orders

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
            url_template=self._server.default("/sapi/v1/algo/spot/openOrders"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AlgoSpotOpenOrdersResponse],
            error_mapper=query_current_algo_open_orders_error_mapper,
            request_options=request_options,
        )

    async def query_historical_algo_orders(
        self,
        symbol: str,
        side: SideOrStr,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        page_size: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AlgoSpotHistoricalOrdersResponse, QueryHistoricalAlgoOrdersErrorBody]:
        """Get all historical SPOT TWAP orders

        Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
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
            url_template=self._server.default("/sapi/v1/algo/spot/historicalOrders"),
            query_params=[
                param[str]("symbol", symbol),
                param[SideOrStr]("side", side),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("page", page),
                param[str | None]("pageSize", page_size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AlgoSpotHistoricalOrdersResponse],
            error_mapper=query_historical_algo_orders_error_mapper,
            request_options=request_options,
        )

    async def query_sub_orders(
        self,
        algo_id: int,
        timestamp: int,
        signature: str,
        *,
        page: int | None = None,
        page_size: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AlgoSpotSubOrdersResponse, QuerySubOrdersErrorBody]:
        """Get respective sub orders for a specified algoId

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
            url_template=self._server.default("/sapi/v1/algo/spot/subOrders"),
            query_params=[
                param[int]("algoId", algo_id),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("page", page),
                param[str | None]("pageSize", page_size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AlgoSpotSubOrdersResponse],
            error_mapper=query_sub_orders_error_mapper,
            request_options=request_options,
        )

    async def time_weighted_average_price_twap_new_order(
        self,
        symbol: str,
        side: SideOrStr,
        quantity: float,
        duration: int,
        timestamp: int,
        signature: str,
        *,
        client_algo_id: str | None = None,
        limit_price: float | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AlgoSpotNewOrderTwapResponse, TimeWeightedAveragePriceTwapNewOrderErrorBody]:
        """Place a new spot TWAP order with Algo service.

        Weight(UID): 3000

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            quantity: Value sent with the request.
            duration: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            client_algo_id: Value sent with the request.
            limit_price: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/algo/spot/newOrderTwap"),
            query_params=[
                param[str]("symbol", symbol),
                param[SideOrStr]("side", side),
                param[float]("quantity", quantity),
                param[int]("duration", duration),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("clientAlgoId", client_algo_id),
                param[float | None]("limitPrice", limit_price),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AlgoSpotNewOrderTwapResponse],
            error_mapper=time_weighted_average_price_twap_new_order_error_mapper,
            request_options=request_options,
        )
