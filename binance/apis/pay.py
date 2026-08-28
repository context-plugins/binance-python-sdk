from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder, param
from ..errors.get_pay_trade_history_user_data_error import (
    GetPayTradeHistoryUserDataErrorBody,
    get_pay_trade_history_user_data_error_mapper,
)
from ..models.sapi_v1_pay_transactions_response import SapiV1PayTransactionsResponse
from ..server.server import Server


class Pay:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = PayWithRawResponse(client, server, auth)

    def get_pay_trade_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1PayTransactionsResponse:
        """- If startTime and endTime are not sent, the recent 90 days' data will be returned.
        - The max interval between startTime and endTime is 90 days.
        - Support for querying orders within the last 18 months.

        Weight(UID): 3000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: default 100, max 100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pay History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_pay_trade_history_user_data(
            timestamp,
            signature,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> PayWithRawResponse:
        return self._with_raw_response


class AsyncPay:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncPayWithRawResponse(client, server, auth)

    async def get_pay_trade_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1PayTransactionsResponse:
        """- If startTime and endTime are not sent, the recent 90 days' data will be returned.
        - The max interval between startTime and endTime is 90 days.
        - Support for querying orders within the last 18 months.

        Weight(UID): 3000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: default 100, max 100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pay History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_pay_trade_history_user_data(
                timestamp,
                signature,
                start_time=start_time,
                end_time=end_time,
                limit=limit,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncPayWithRawResponse:
        return self._with_raw_response


class PayWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_pay_trade_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1PayTransactionsResponse, GetPayTradeHistoryUserDataErrorBody]:
        """- If startTime and endTime are not sent, the recent 90 days' data will be returned.
        - The max interval between startTime and endTime is 90 days.
        - Support for querying orders within the last 18 months.

        Weight(UID): 3000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: default 100, max 100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/pay/transactions"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1PayTransactionsResponse],
            error_mapper=get_pay_trade_history_user_data_error_mapper,
            request_options=request_options,
        )


class AsyncPayWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_pay_trade_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1PayTransactionsResponse, GetPayTradeHistoryUserDataErrorBody]:
        """- If startTime and endTime are not sent, the recent 90 days' data will be returned.
        - The max interval between startTime and endTime is 90 days.
        - Support for querying orders within the last 18 months.

        Weight(UID): 3000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: default 100, max 100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/pay/transactions"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1PayTransactionsResponse],
            error_mapper=get_pay_trade_history_user_data_error_mapper,
            request_options=request_options,
        )
