from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder, param
from ..errors.fiat_deposit_withdraw_history_user_data_error import (
    FiatDepositWithdrawHistoryUserDataErrorBody,
    fiat_deposit_withdraw_history_user_data_error_mapper,
)
from ..errors.fiat_payments_history_user_data_error import (
    FiatPaymentsHistoryUserDataErrorBody,
    fiat_payments_history_user_data_error_mapper,
)
from ..models.sapi_v1_fiat_orders_response import SapiV1FiatOrdersResponse
from ..models.sapi_v1_fiat_payments_response import SapiV1FiatPaymentsResponse
from ..server.server import Server


class Fiat:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FiatWithRawResponse(client, server, auth)

    def fiat_deposit_withdraw_history_user_data(
        self,
        transaction_type: int,
        timestamp: int,
        signature: str,
        *,
        begin_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        rows: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1FiatOrdersResponse:
        """- If beginTime and endTime are not sent, the recent 30-day data will be returned.

        Weight(UID): 90000

        Args:
            transaction_type: * ``0`` - deposit * ``1`` - withdraw
            timestamp: UTC timestamp in ms
            signature: Signature
            begin_time: Value sent with the request.
            end_time: UTC timestamp in ms
            page: Default 1
            rows: Default 100, max 500
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            History of deposit/withdraw orders

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.fiat_deposit_withdraw_history_user_data(
            transaction_type,
            timestamp,
            signature,
            begin_time=begin_time,
            end_time=end_time,
            page=page,
            rows=rows,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def fiat_payments_history_user_data(
        self,
        transaction_type: int,
        timestamp: int,
        signature: str,
        *,
        begin_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        rows: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1FiatPaymentsResponse:
        """- If beginTime and endTime are not sent, the recent 30-day data will be returned.

        Weight(IP): 1

        Args:
            transaction_type: * ``0`` - deposit * ``1`` - withdraw
            timestamp: UTC timestamp in ms
            signature: Signature
            begin_time: Value sent with the request.
            end_time: UTC timestamp in ms
            page: Default 1
            rows: Default 100, max 500
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            History of fiat payments

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.fiat_payments_history_user_data(
            transaction_type,
            timestamp,
            signature,
            begin_time=begin_time,
            end_time=end_time,
            page=page,
            rows=rows,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> FiatWithRawResponse:
        return self._with_raw_response


class AsyncFiat:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFiatWithRawResponse(client, server, auth)

    async def fiat_deposit_withdraw_history_user_data(
        self,
        transaction_type: int,
        timestamp: int,
        signature: str,
        *,
        begin_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        rows: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1FiatOrdersResponse:
        """- If beginTime and endTime are not sent, the recent 30-day data will be returned.

        Weight(UID): 90000

        Args:
            transaction_type: * ``0`` - deposit * ``1`` - withdraw
            timestamp: UTC timestamp in ms
            signature: Signature
            begin_time: Value sent with the request.
            end_time: UTC timestamp in ms
            page: Default 1
            rows: Default 100, max 500
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            History of deposit/withdraw orders

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.fiat_deposit_withdraw_history_user_data(
                transaction_type,
                timestamp,
                signature,
                begin_time=begin_time,
                end_time=end_time,
                page=page,
                rows=rows,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def fiat_payments_history_user_data(
        self,
        transaction_type: int,
        timestamp: int,
        signature: str,
        *,
        begin_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        rows: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1FiatPaymentsResponse:
        """- If beginTime and endTime are not sent, the recent 30-day data will be returned.

        Weight(IP): 1

        Args:
            transaction_type: * ``0`` - deposit * ``1`` - withdraw
            timestamp: UTC timestamp in ms
            signature: Signature
            begin_time: Value sent with the request.
            end_time: UTC timestamp in ms
            page: Default 1
            rows: Default 100, max 500
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            History of fiat payments

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.fiat_payments_history_user_data(
                transaction_type,
                timestamp,
                signature,
                begin_time=begin_time,
                end_time=end_time,
                page=page,
                rows=rows,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncFiatWithRawResponse:
        return self._with_raw_response


class FiatWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fiat_deposit_withdraw_history_user_data(
        self,
        transaction_type: int,
        timestamp: int,
        signature: str,
        *,
        begin_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        rows: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1FiatOrdersResponse, FiatDepositWithdrawHistoryUserDataErrorBody]:
        """- If beginTime and endTime are not sent, the recent 30-day data will be returned.

        Weight(UID): 90000

        Args:
            transaction_type: * ``0`` - deposit * ``1`` - withdraw
            timestamp: UTC timestamp in ms
            signature: Signature
            begin_time: Value sent with the request.
            end_time: UTC timestamp in ms
            page: Default 1
            rows: Default 100, max 500
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/fiat/orders"),
            query_params=[
                param[int]("transactionType", transaction_type),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("beginTime", begin_time),
                param[int | None]("endTime", end_time),
                param[int | None]("page", page),
                param[int | None]("rows", rows),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1FiatOrdersResponse],
            error_mapper=fiat_deposit_withdraw_history_user_data_error_mapper,
            request_options=request_options,
        )

    def fiat_payments_history_user_data(
        self,
        transaction_type: int,
        timestamp: int,
        signature: str,
        *,
        begin_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        rows: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1FiatPaymentsResponse, FiatPaymentsHistoryUserDataErrorBody]:
        """- If beginTime and endTime are not sent, the recent 30-day data will be returned.

        Weight(IP): 1

        Args:
            transaction_type: * ``0`` - deposit * ``1`` - withdraw
            timestamp: UTC timestamp in ms
            signature: Signature
            begin_time: Value sent with the request.
            end_time: UTC timestamp in ms
            page: Default 1
            rows: Default 100, max 500
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/fiat/payments"),
            query_params=[
                param[int]("transactionType", transaction_type),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("beginTime", begin_time),
                param[int | None]("endTime", end_time),
                param[int | None]("page", page),
                param[int | None]("rows", rows),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1FiatPaymentsResponse],
            error_mapper=fiat_payments_history_user_data_error_mapper,
            request_options=request_options,
        )


class AsyncFiatWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fiat_deposit_withdraw_history_user_data(
        self,
        transaction_type: int,
        timestamp: int,
        signature: str,
        *,
        begin_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        rows: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1FiatOrdersResponse, FiatDepositWithdrawHistoryUserDataErrorBody]:
        """- If beginTime and endTime are not sent, the recent 30-day data will be returned.

        Weight(UID): 90000

        Args:
            transaction_type: * ``0`` - deposit * ``1`` - withdraw
            timestamp: UTC timestamp in ms
            signature: Signature
            begin_time: Value sent with the request.
            end_time: UTC timestamp in ms
            page: Default 1
            rows: Default 100, max 500
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/fiat/orders"),
            query_params=[
                param[int]("transactionType", transaction_type),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("beginTime", begin_time),
                param[int | None]("endTime", end_time),
                param[int | None]("page", page),
                param[int | None]("rows", rows),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1FiatOrdersResponse],
            error_mapper=fiat_deposit_withdraw_history_user_data_error_mapper,
            request_options=request_options,
        )

    async def fiat_payments_history_user_data(
        self,
        transaction_type: int,
        timestamp: int,
        signature: str,
        *,
        begin_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        rows: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1FiatPaymentsResponse, FiatPaymentsHistoryUserDataErrorBody]:
        """- If beginTime and endTime are not sent, the recent 30-day data will be returned.

        Weight(IP): 1

        Args:
            transaction_type: * ``0`` - deposit * ``1`` - withdraw
            timestamp: UTC timestamp in ms
            signature: Signature
            begin_time: Value sent with the request.
            end_time: UTC timestamp in ms
            page: Default 1
            rows: Default 100, max 500
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/fiat/payments"),
            query_params=[
                param[int]("transactionType", transaction_type),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("beginTime", begin_time),
                param[int | None]("endTime", end_time),
                param[int | None]("page", page),
                param[int | None]("rows", rows),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1FiatPaymentsResponse],
            error_mapper=fiat_payments_history_user_data_error_mapper,
            request_options=request_options,
        )
