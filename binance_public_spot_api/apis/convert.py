from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder, param
from ..errors.accept_quote_trade_error import AcceptQuoteTradeErrorBody, accept_quote_trade_error_mapper
from ..errors.cancel_limit_order_user_data_error import (
    CancelLimitOrderUserDataErrorBody,
    cancel_limit_order_user_data_error_mapper,
)
from ..errors.get_convert_trade_history_user_data_error import (
    GetConvertTradeHistoryUserDataErrorBody,
    get_convert_trade_history_user_data_error_mapper,
)
from ..errors.list_all_convert_pairs_error import ListAllConvertPairsErrorBody, list_all_convert_pairs_error_mapper
from ..errors.order_status_user_data_error import OrderStatusUserDataErrorBody, order_status_user_data_error_mapper
from ..errors.place_limit_order_user_data_error import (
    PlaceLimitOrderUserDataErrorBody,
    place_limit_order_user_data_error_mapper,
)
from ..errors.query_limit_open_orders_user_data_error import (
    QueryLimitOpenOrdersUserDataErrorBody,
    query_limit_open_orders_user_data_error_mapper,
)
from ..errors.query_order_quantity_precision_per_asset_user_data_error import (
    QueryOrderQuantityPrecisionPerAssetUserDataErrorBody,
    query_order_quantity_precision_per_asset_user_data_error_mapper,
)
from ..errors.send_quote_request_user_data_error import (
    SendQuoteRequestUserDataErrorBody,
    send_quote_request_user_data_error_mapper,
)
from ..models.enums.expired_type import ExpiredTypeOrStr
from ..models.enums.side import SideOrStr
from ..models.enums.wallet_type import WalletTypeOrStr
from ..models.sapi_v1_convert_accept_quote_response import SapiV1ConvertAcceptQuoteResponse
from ..models.sapi_v1_convert_asset_info_response import SapiV1ConvertAssetInfoResponse
from ..models.sapi_v1_convert_exchange_info_response import SapiV1ConvertExchangeInfoResponse
from ..models.sapi_v1_convert_get_quote_response import SapiV1ConvertGetQuoteResponse
from ..models.sapi_v1_convert_limit_cancel_order_response import SapiV1ConvertLimitCancelOrderResponse
from ..models.sapi_v1_convert_limit_place_order_response import SapiV1ConvertLimitPlaceOrderResponse
from ..models.sapi_v1_convert_limit_query_open_orders_response import SapiV1ConvertLimitQueryOpenOrdersResponse
from ..models.sapi_v1_convert_order_status_response import SapiV1ConvertOrderStatusResponse
from ..models.sapi_v1_convert_trade_flow_response import SapiV1ConvertTradeFlowResponse
from ..server.server import Server


class Convert:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ConvertWithRawResponse(client, server, auth)

    def accept_quote_trade(
        self,
        quote_id: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1ConvertAcceptQuoteResponse:
        """Accept the offered quote by quote ID.

        Weight(UID): 500

        Args:
            quote_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Accept Quote

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.accept_quote_trade(
            quote_id, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def cancel_limit_order_user_data(
        self,
        order_id: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1ConvertLimitCancelOrderResponse:
        """Enable users to cancel a limit order

        Weight(UID): 200

        Args:
            order_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Cancel Order

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.cancel_limit_order_user_data(
            order_id, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def get_convert_trade_history_user_data(
        self,
        start_time: int,
        end_time: int,
        timestamp: int,
        signature: str,
        *,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1ConvertTradeFlowResponse:
        """- The max interval between startTime and endTime is 30 days.

        Weight(UID): 3000

        Args:
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            timestamp: UTC timestamp in ms
            signature: Signature
            limit: default 100, max 1000
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Convert Trade History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_convert_trade_history_user_data(
            start_time,
            end_time,
            timestamp,
            signature,
            limit=limit,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def list_all_convert_pairs(
        self,
        *,
        from_asset: str | None = None,
        to_asset: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1ConvertExchangeInfoResponse]:
        """Query for all convertible token pairs and the tokens’ respective upper/lower limits

        Weight(IP): 3000

        Args:
            from_asset: User spends coin
            to_asset: User receives coin
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List Convert Pairs

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.list_all_convert_pairs(
            from_asset=from_asset, to_asset=to_asset, request_options=request_options
        ).unwrap()

    def order_status_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        order_id: str | None = None,
        quote_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1ConvertOrderStatusResponse:
        """Query order status by order ID.

        Weight(UID): 100

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Value sent with the request.
            quote_id: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Order Status

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.order_status_user_data(
            timestamp,
            signature,
            order_id=order_id,
            quote_id=quote_id,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def place_limit_order_user_data(
        self,
        base_asset: str,
        quote_asset: str,
        limit_price: float,
        side: SideOrStr,
        timestamp: int,
        signature: str,
        *,
        base_amount: float | None = None,
        quote_amount: float | None = None,
        wallet_type: WalletTypeOrStr | None = None,
        expired_type: ExpiredTypeOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1ConvertLimitPlaceOrderResponse:
        """Enable users to place a limit order

        - baseAsset or quoteAsset can be determined via exchangeInfo endpoint.
        - Limit price is defined from baseAsset to quoteAsset.
        - Either baseAmount or quoteAmount is used.

        Weight(UID): 500

        Args:
            base_asset: Value sent with the request.
            quote_asset: Value sent with the request.
            limit_price: Symbol limit price (from baseAsset to quoteAsset)
            side: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            base_amount: Base asset amount. (One of baseAmount or quoteAmount is required)
            quote_amount: Quote asset amount. (One of baseAmount or quoteAmount is required)
            wallet_type: SPOT or FUNDING or SPOT_FUNDING. It is to use which type of assets. Default is SPOT.
            expired_type: 1_D, 3_D, 7_D, 30_D (D means day)
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The deserialized ``SapiV1ConvertLimitPlaceOrderResponse`` response.

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.place_limit_order_user_data(
            base_asset,
            quote_asset,
            limit_price,
            side,
            timestamp,
            signature,
            base_amount=base_amount,
            quote_amount=quote_amount,
            wallet_type=wallet_type,
            expired_type=expired_type,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def query_limit_open_orders_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1ConvertLimitQueryOpenOrdersResponse:
        """Enable users to query for all existing limit orders

        Weight(UID): 3000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            All existing limit orders

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_limit_open_orders_user_data(
            timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def query_order_quantity_precision_per_asset_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1ConvertAssetInfoResponse]:
        """Query for supported asset precision information

        Weight(IP): 100

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Asset Precision Information

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_order_quantity_precision_per_asset_user_data(
            timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def send_quote_request_user_data(
        self,
        from_asset: str,
        to_asset: str,
        timestamp: int,
        signature: str,
        *,
        from_amount: float | None = None,
        to_amount: float | None = None,
        valid_time: str | None = None,
        wallet_type: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1ConvertGetQuoteResponse:
        """Request a quote for the requested token pairs

        Weight(UID): 200

        Args:
            from_asset: Value sent with the request.
            to_asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            from_amount: When specified, it is the amount you will be debited after the conversion
            to_amount: When specified, it is the amount you will be debited after the conversion
            valid_time: 10s, 30s, 1m, 2m, default 10s
            wallet_type: SPOT or FUNDING. Default is SPOT
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Quote Request

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.send_quote_request_user_data(
            from_asset,
            to_asset,
            timestamp,
            signature,
            from_amount=from_amount,
            to_amount=to_amount,
            valid_time=valid_time,
            wallet_type=wallet_type,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> ConvertWithRawResponse:
        return self._with_raw_response


class AsyncConvert:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncConvertWithRawResponse(client, server, auth)

    async def accept_quote_trade(
        self,
        quote_id: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1ConvertAcceptQuoteResponse:
        """Accept the offered quote by quote ID.

        Weight(UID): 500

        Args:
            quote_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Accept Quote

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.accept_quote_trade(
                quote_id, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def cancel_limit_order_user_data(
        self,
        order_id: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1ConvertLimitCancelOrderResponse:
        """Enable users to cancel a limit order

        Weight(UID): 200

        Args:
            order_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Cancel Order

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.cancel_limit_order_user_data(
                order_id, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def get_convert_trade_history_user_data(
        self,
        start_time: int,
        end_time: int,
        timestamp: int,
        signature: str,
        *,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1ConvertTradeFlowResponse:
        """- The max interval between startTime and endTime is 30 days.

        Weight(UID): 3000

        Args:
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            timestamp: UTC timestamp in ms
            signature: Signature
            limit: default 100, max 1000
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Convert Trade History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_convert_trade_history_user_data(
                start_time,
                end_time,
                timestamp,
                signature,
                limit=limit,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def list_all_convert_pairs(
        self,
        *,
        from_asset: str | None = None,
        to_asset: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1ConvertExchangeInfoResponse]:
        """Query for all convertible token pairs and the tokens’ respective upper/lower limits

        Weight(IP): 3000

        Args:
            from_asset: User spends coin
            to_asset: User receives coin
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List Convert Pairs

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.list_all_convert_pairs(
                from_asset=from_asset, to_asset=to_asset, request_options=request_options
            )
        ).unwrap()

    async def order_status_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        order_id: str | None = None,
        quote_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1ConvertOrderStatusResponse:
        """Query order status by order ID.

        Weight(UID): 100

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Value sent with the request.
            quote_id: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Order Status

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.order_status_user_data(
                timestamp,
                signature,
                order_id=order_id,
                quote_id=quote_id,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def place_limit_order_user_data(
        self,
        base_asset: str,
        quote_asset: str,
        limit_price: float,
        side: SideOrStr,
        timestamp: int,
        signature: str,
        *,
        base_amount: float | None = None,
        quote_amount: float | None = None,
        wallet_type: WalletTypeOrStr | None = None,
        expired_type: ExpiredTypeOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1ConvertLimitPlaceOrderResponse:
        """Enable users to place a limit order

        - baseAsset or quoteAsset can be determined via exchangeInfo endpoint.
        - Limit price is defined from baseAsset to quoteAsset.
        - Either baseAmount or quoteAmount is used.

        Weight(UID): 500

        Args:
            base_asset: Value sent with the request.
            quote_asset: Value sent with the request.
            limit_price: Symbol limit price (from baseAsset to quoteAsset)
            side: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            base_amount: Base asset amount. (One of baseAmount or quoteAmount is required)
            quote_amount: Quote asset amount. (One of baseAmount or quoteAmount is required)
            wallet_type: SPOT or FUNDING or SPOT_FUNDING. It is to use which type of assets. Default is SPOT.
            expired_type: 1_D, 3_D, 7_D, 30_D (D means day)
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The deserialized ``SapiV1ConvertLimitPlaceOrderResponse`` response.

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.place_limit_order_user_data(
                base_asset,
                quote_asset,
                limit_price,
                side,
                timestamp,
                signature,
                base_amount=base_amount,
                quote_amount=quote_amount,
                wallet_type=wallet_type,
                expired_type=expired_type,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def query_limit_open_orders_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1ConvertLimitQueryOpenOrdersResponse:
        """Enable users to query for all existing limit orders

        Weight(UID): 3000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            All existing limit orders

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_limit_open_orders_user_data(
                timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def query_order_quantity_precision_per_asset_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1ConvertAssetInfoResponse]:
        """Query for supported asset precision information

        Weight(IP): 100

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Asset Precision Information

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_order_quantity_precision_per_asset_user_data(
                timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def send_quote_request_user_data(
        self,
        from_asset: str,
        to_asset: str,
        timestamp: int,
        signature: str,
        *,
        from_amount: float | None = None,
        to_amount: float | None = None,
        valid_time: str | None = None,
        wallet_type: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1ConvertGetQuoteResponse:
        """Request a quote for the requested token pairs

        Weight(UID): 200

        Args:
            from_asset: Value sent with the request.
            to_asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            from_amount: When specified, it is the amount you will be debited after the conversion
            to_amount: When specified, it is the amount you will be debited after the conversion
            valid_time: 10s, 30s, 1m, 2m, default 10s
            wallet_type: SPOT or FUNDING. Default is SPOT
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Quote Request

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.send_quote_request_user_data(
                from_asset,
                to_asset,
                timestamp,
                signature,
                from_amount=from_amount,
                to_amount=to_amount,
                valid_time=valid_time,
                wallet_type=wallet_type,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncConvertWithRawResponse:
        return self._with_raw_response


class ConvertWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def accept_quote_trade(
        self,
        quote_id: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1ConvertAcceptQuoteResponse, AcceptQuoteTradeErrorBody]:
        """Accept the offered quote by quote ID.

        Weight(UID): 500

        Args:
            quote_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/convert/acceptQuote"),
            query_params=[
                param[str]("quoteId", quote_id),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1ConvertAcceptQuoteResponse],
            error_mapper=accept_quote_trade_error_mapper,
            request_options=request_options,
        )

    def cancel_limit_order_user_data(
        self,
        order_id: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1ConvertLimitCancelOrderResponse, CancelLimitOrderUserDataErrorBody]:
        """Enable users to cancel a limit order

        Weight(UID): 200

        Args:
            order_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/convert/limit/cancelOrder"),
            query_params=[
                param[int]("orderId", order_id),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1ConvertLimitCancelOrderResponse],
            error_mapper=cancel_limit_order_user_data_error_mapper,
            request_options=request_options,
        )

    def get_convert_trade_history_user_data(
        self,
        start_time: int,
        end_time: int,
        timestamp: int,
        signature: str,
        *,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1ConvertTradeFlowResponse, GetConvertTradeHistoryUserDataErrorBody]:
        """- The max interval between startTime and endTime is 30 days.

        Weight(UID): 3000

        Args:
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            timestamp: UTC timestamp in ms
            signature: Signature
            limit: default 100, max 1000
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/convert/tradeFlow"),
            query_params=[
                param[int]("startTime", start_time),
                param[int]("endTime", end_time),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1ConvertTradeFlowResponse],
            error_mapper=get_convert_trade_history_user_data_error_mapper,
            request_options=request_options,
        )

    def list_all_convert_pairs(
        self,
        *,
        from_asset: str | None = None,
        to_asset: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1ConvertExchangeInfoResponse], ListAllConvertPairsErrorBody]:
        """Query for all convertible token pairs and the tokens’ respective upper/lower limits

        Weight(IP): 3000

        Args:
            from_asset: User spends coin
            to_asset: User receives coin
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/convert/exchangeInfo"),
            query_params=[param[str | None]("fromAsset", from_asset), param[str | None]("toAsset", to_asset)],
            decoder=json_decoder[list[SapiV1ConvertExchangeInfoResponse]],
            error_mapper=list_all_convert_pairs_error_mapper,
            request_options=request_options,
        )

    def order_status_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        order_id: str | None = None,
        quote_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1ConvertOrderStatusResponse, OrderStatusUserDataErrorBody]:
        """Query order status by order ID.

        Weight(UID): 100

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Value sent with the request.
            quote_id: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/convert/orderStatus"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("orderId", order_id),
                param[str | None]("quoteId", quote_id),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1ConvertOrderStatusResponse],
            error_mapper=order_status_user_data_error_mapper,
            request_options=request_options,
        )

    def place_limit_order_user_data(
        self,
        base_asset: str,
        quote_asset: str,
        limit_price: float,
        side: SideOrStr,
        timestamp: int,
        signature: str,
        *,
        base_amount: float | None = None,
        quote_amount: float | None = None,
        wallet_type: WalletTypeOrStr | None = None,
        expired_type: ExpiredTypeOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1ConvertLimitPlaceOrderResponse, PlaceLimitOrderUserDataErrorBody]:
        """Enable users to place a limit order

        - baseAsset or quoteAsset can be determined via exchangeInfo endpoint.
        - Limit price is defined from baseAsset to quoteAsset.
        - Either baseAmount or quoteAmount is used.

        Weight(UID): 500

        Args:
            base_asset: Value sent with the request.
            quote_asset: Value sent with the request.
            limit_price: Symbol limit price (from baseAsset to quoteAsset)
            side: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            base_amount: Base asset amount. (One of baseAmount or quoteAmount is required)
            quote_amount: Quote asset amount. (One of baseAmount or quoteAmount is required)
            wallet_type: SPOT or FUNDING or SPOT_FUNDING. It is to use which type of assets. Default is SPOT.
            expired_type: 1_D, 3_D, 7_D, 30_D (D means day)
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/convert/limit/placeOrder"),
            query_params=[
                param[str]("baseAsset", base_asset),
                param[str]("quoteAsset", quote_asset),
                param[float]("limitPrice", limit_price),
                param[SideOrStr]("side", side),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[float | None]("baseAmount", base_amount),
                param[float | None]("quoteAmount", quote_amount),
                param[WalletTypeOrStr | None]("walletType", wallet_type),
                param[ExpiredTypeOrStr | None]("expiredType", expired_type),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1ConvertLimitPlaceOrderResponse],
            error_mapper=place_limit_order_user_data_error_mapper,
            request_options=request_options,
        )

    def query_limit_open_orders_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1ConvertLimitQueryOpenOrdersResponse, QueryLimitOpenOrdersUserDataErrorBody]:
        """Enable users to query for all existing limit orders

        Weight(UID): 3000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/convert/limit/queryOpenOrders"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1ConvertLimitQueryOpenOrdersResponse],
            error_mapper=query_limit_open_orders_user_data_error_mapper,
            request_options=request_options,
        )

    def query_order_quantity_precision_per_asset_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1ConvertAssetInfoResponse], QueryOrderQuantityPrecisionPerAssetUserDataErrorBody]:
        """Query for supported asset precision information

        Weight(IP): 100

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/convert/assetInfo"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1ConvertAssetInfoResponse]],
            error_mapper=query_order_quantity_precision_per_asset_user_data_error_mapper,
            request_options=request_options,
        )

    def send_quote_request_user_data(
        self,
        from_asset: str,
        to_asset: str,
        timestamp: int,
        signature: str,
        *,
        from_amount: float | None = None,
        to_amount: float | None = None,
        valid_time: str | None = None,
        wallet_type: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1ConvertGetQuoteResponse, SendQuoteRequestUserDataErrorBody]:
        """Request a quote for the requested token pairs

        Weight(UID): 200

        Args:
            from_asset: Value sent with the request.
            to_asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            from_amount: When specified, it is the amount you will be debited after the conversion
            to_amount: When specified, it is the amount you will be debited after the conversion
            valid_time: 10s, 30s, 1m, 2m, default 10s
            wallet_type: SPOT or FUNDING. Default is SPOT
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/convert/getQuote"),
            query_params=[
                param[str]("fromAsset", from_asset),
                param[str]("toAsset", to_asset),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[float | None]("fromAmount", from_amount),
                param[float | None]("toAmount", to_amount),
                param[str | None]("validTime", valid_time),
                param[str | None]("walletType", wallet_type),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1ConvertGetQuoteResponse],
            error_mapper=send_quote_request_user_data_error_mapper,
            request_options=request_options,
        )


class AsyncConvertWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def accept_quote_trade(
        self,
        quote_id: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1ConvertAcceptQuoteResponse, AcceptQuoteTradeErrorBody]:
        """Accept the offered quote by quote ID.

        Weight(UID): 500

        Args:
            quote_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/convert/acceptQuote"),
            query_params=[
                param[str]("quoteId", quote_id),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1ConvertAcceptQuoteResponse],
            error_mapper=accept_quote_trade_error_mapper,
            request_options=request_options,
        )

    async def cancel_limit_order_user_data(
        self,
        order_id: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1ConvertLimitCancelOrderResponse, CancelLimitOrderUserDataErrorBody]:
        """Enable users to cancel a limit order

        Weight(UID): 200

        Args:
            order_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/convert/limit/cancelOrder"),
            query_params=[
                param[int]("orderId", order_id),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1ConvertLimitCancelOrderResponse],
            error_mapper=cancel_limit_order_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_convert_trade_history_user_data(
        self,
        start_time: int,
        end_time: int,
        timestamp: int,
        signature: str,
        *,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1ConvertTradeFlowResponse, GetConvertTradeHistoryUserDataErrorBody]:
        """- The max interval between startTime and endTime is 30 days.

        Weight(UID): 3000

        Args:
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            timestamp: UTC timestamp in ms
            signature: Signature
            limit: default 100, max 1000
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/convert/tradeFlow"),
            query_params=[
                param[int]("startTime", start_time),
                param[int]("endTime", end_time),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1ConvertTradeFlowResponse],
            error_mapper=get_convert_trade_history_user_data_error_mapper,
            request_options=request_options,
        )

    async def list_all_convert_pairs(
        self,
        *,
        from_asset: str | None = None,
        to_asset: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1ConvertExchangeInfoResponse], ListAllConvertPairsErrorBody]:
        """Query for all convertible token pairs and the tokens’ respective upper/lower limits

        Weight(IP): 3000

        Args:
            from_asset: User spends coin
            to_asset: User receives coin
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/convert/exchangeInfo"),
            query_params=[param[str | None]("fromAsset", from_asset), param[str | None]("toAsset", to_asset)],
            decoder=json_decoder[list[SapiV1ConvertExchangeInfoResponse]],
            error_mapper=list_all_convert_pairs_error_mapper,
            request_options=request_options,
        )

    async def order_status_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        order_id: str | None = None,
        quote_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1ConvertOrderStatusResponse, OrderStatusUserDataErrorBody]:
        """Query order status by order ID.

        Weight(UID): 100

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Value sent with the request.
            quote_id: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/convert/orderStatus"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("orderId", order_id),
                param[str | None]("quoteId", quote_id),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1ConvertOrderStatusResponse],
            error_mapper=order_status_user_data_error_mapper,
            request_options=request_options,
        )

    async def place_limit_order_user_data(
        self,
        base_asset: str,
        quote_asset: str,
        limit_price: float,
        side: SideOrStr,
        timestamp: int,
        signature: str,
        *,
        base_amount: float | None = None,
        quote_amount: float | None = None,
        wallet_type: WalletTypeOrStr | None = None,
        expired_type: ExpiredTypeOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1ConvertLimitPlaceOrderResponse, PlaceLimitOrderUserDataErrorBody]:
        """Enable users to place a limit order

        - baseAsset or quoteAsset can be determined via exchangeInfo endpoint.
        - Limit price is defined from baseAsset to quoteAsset.
        - Either baseAmount or quoteAmount is used.

        Weight(UID): 500

        Args:
            base_asset: Value sent with the request.
            quote_asset: Value sent with the request.
            limit_price: Symbol limit price (from baseAsset to quoteAsset)
            side: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            base_amount: Base asset amount. (One of baseAmount or quoteAmount is required)
            quote_amount: Quote asset amount. (One of baseAmount or quoteAmount is required)
            wallet_type: SPOT or FUNDING or SPOT_FUNDING. It is to use which type of assets. Default is SPOT.
            expired_type: 1_D, 3_D, 7_D, 30_D (D means day)
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/convert/limit/placeOrder"),
            query_params=[
                param[str]("baseAsset", base_asset),
                param[str]("quoteAsset", quote_asset),
                param[float]("limitPrice", limit_price),
                param[SideOrStr]("side", side),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[float | None]("baseAmount", base_amount),
                param[float | None]("quoteAmount", quote_amount),
                param[WalletTypeOrStr | None]("walletType", wallet_type),
                param[ExpiredTypeOrStr | None]("expiredType", expired_type),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1ConvertLimitPlaceOrderResponse],
            error_mapper=place_limit_order_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_limit_open_orders_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1ConvertLimitQueryOpenOrdersResponse, QueryLimitOpenOrdersUserDataErrorBody]:
        """Enable users to query for all existing limit orders

        Weight(UID): 3000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/convert/limit/queryOpenOrders"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1ConvertLimitQueryOpenOrdersResponse],
            error_mapper=query_limit_open_orders_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_order_quantity_precision_per_asset_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1ConvertAssetInfoResponse], QueryOrderQuantityPrecisionPerAssetUserDataErrorBody]:
        """Query for supported asset precision information

        Weight(IP): 100

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/convert/assetInfo"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1ConvertAssetInfoResponse]],
            error_mapper=query_order_quantity_precision_per_asset_user_data_error_mapper,
            request_options=request_options,
        )

    async def send_quote_request_user_data(
        self,
        from_asset: str,
        to_asset: str,
        timestamp: int,
        signature: str,
        *,
        from_amount: float | None = None,
        to_amount: float | None = None,
        valid_time: str | None = None,
        wallet_type: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1ConvertGetQuoteResponse, SendQuoteRequestUserDataErrorBody]:
        """Request a quote for the requested token pairs

        Weight(UID): 200

        Args:
            from_asset: Value sent with the request.
            to_asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            from_amount: When specified, it is the amount you will be debited after the conversion
            to_amount: When specified, it is the amount you will be debited after the conversion
            valid_time: 10s, 30s, 1m, 2m, default 10s
            wallet_type: SPOT or FUNDING. Default is SPOT
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/convert/getQuote"),
            query_params=[
                param[str]("fromAsset", from_asset),
                param[str]("toAsset", to_asset),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[float | None]("fromAmount", from_amount),
                param[float | None]("toAmount", to_amount),
                param[str | None]("validTime", valid_time),
                param[str | None]("walletType", wallet_type),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1ConvertGetQuoteResponse],
            error_mapper=send_quote_request_user_data_error_mapper,
            request_options=request_options,
        )
