from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder, param
from ..errors.get_c2_c_trade_history_user_data_error import (
    GetC2CTradeHistoryUserDataErrorBody,
    get_c2_c_trade_history_user_data_error_mapper,
)
from ..models.enums.trade_type import TradeTypeOrStr
from ..models.sapi_v1_c2_c_order_match_list_user_order_history_response import (
    SapiV1C2COrderMatchListUserOrderHistoryResponse,
)
from ..server.server import Server


class C2C:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = C2CWithRawResponse(client, server, auth)

    def get_c2_c_trade_history_user_data(
        self,
        trade_type: TradeTypeOrStr,
        timestamp: int,
        signature: str,
        *,
        start_timestamp: int | None = None,
        end_timestamp: int | None = None,
        page: int | None = None,
        rows: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1C2COrderMatchListUserOrderHistoryResponse:
        """- If startTimestamp and endTimestamp are not sent, the recent 30-day data will be returned.
        - The max interval between startTimestamp and endTimestamp is 30 days.

        Weight(IP): 1

        Args:
            trade_type: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            start_timestamp: UTC timestamp in ms
            end_timestamp: UTC timestamp in ms
            page: Default 1
            rows: default 100, max 100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Trades history

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_c2_c_trade_history_user_data(
            trade_type,
            timestamp,
            signature,
            start_timestamp=start_timestamp,
            end_timestamp=end_timestamp,
            page=page,
            rows=rows,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> C2CWithRawResponse:
        return self._with_raw_response


class AsyncC2C:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncC2CWithRawResponse(client, server, auth)

    async def get_c2_c_trade_history_user_data(
        self,
        trade_type: TradeTypeOrStr,
        timestamp: int,
        signature: str,
        *,
        start_timestamp: int | None = None,
        end_timestamp: int | None = None,
        page: int | None = None,
        rows: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1C2COrderMatchListUserOrderHistoryResponse:
        """- If startTimestamp and endTimestamp are not sent, the recent 30-day data will be returned.
        - The max interval between startTimestamp and endTimestamp is 30 days.

        Weight(IP): 1

        Args:
            trade_type: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            start_timestamp: UTC timestamp in ms
            end_timestamp: UTC timestamp in ms
            page: Default 1
            rows: default 100, max 100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Trades history

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_c2_c_trade_history_user_data(
                trade_type,
                timestamp,
                signature,
                start_timestamp=start_timestamp,
                end_timestamp=end_timestamp,
                page=page,
                rows=rows,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncC2CWithRawResponse:
        return self._with_raw_response


class C2CWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_c2_c_trade_history_user_data(
        self,
        trade_type: TradeTypeOrStr,
        timestamp: int,
        signature: str,
        *,
        start_timestamp: int | None = None,
        end_timestamp: int | None = None,
        page: int | None = None,
        rows: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1C2COrderMatchListUserOrderHistoryResponse, GetC2CTradeHistoryUserDataErrorBody]:
        """- If startTimestamp and endTimestamp are not sent, the recent 30-day data will be returned.
        - The max interval between startTimestamp and endTimestamp is 30 days.

        Weight(IP): 1

        Args:
            trade_type: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            start_timestamp: UTC timestamp in ms
            end_timestamp: UTC timestamp in ms
            page: Default 1
            rows: default 100, max 100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/c2c/orderMatch/listUserOrderHistory"),
            query_params=[
                param[TradeTypeOrStr]("tradeType", trade_type),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTimestamp", start_timestamp),
                param[int | None]("endTimestamp", end_timestamp),
                param[int | None]("page", page),
                param[int | None]("rows", rows),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1C2COrderMatchListUserOrderHistoryResponse],
            error_mapper=get_c2_c_trade_history_user_data_error_mapper,
            request_options=request_options,
        )


class AsyncC2CWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_c2_c_trade_history_user_data(
        self,
        trade_type: TradeTypeOrStr,
        timestamp: int,
        signature: str,
        *,
        start_timestamp: int | None = None,
        end_timestamp: int | None = None,
        page: int | None = None,
        rows: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1C2COrderMatchListUserOrderHistoryResponse, GetC2CTradeHistoryUserDataErrorBody]:
        """- If startTimestamp and endTimestamp are not sent, the recent 30-day data will be returned.
        - The max interval between startTimestamp and endTimestamp is 30 days.

        Weight(IP): 1

        Args:
            trade_type: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            start_timestamp: UTC timestamp in ms
            end_timestamp: UTC timestamp in ms
            page: Default 1
            rows: default 100, max 100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/c2c/orderMatch/listUserOrderHistory"),
            query_params=[
                param[TradeTypeOrStr]("tradeType", trade_type),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTimestamp", start_timestamp),
                param[int | None]("endTimestamp", end_timestamp),
                param[int | None]("page", page),
                param[int | None]("rows", rows),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1C2COrderMatchListUserOrderHistoryResponse],
            error_mapper=get_c2_c_trade_history_user_data_error_mapper,
            request_options=request_options,
        )
