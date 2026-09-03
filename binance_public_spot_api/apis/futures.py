from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder, param
from ..errors.get_future_account_transaction_history_list_user_data_error import (
    GetFutureAccountTransactionHistoryListUserDataErrorBody,
    get_future_account_transaction_history_list_user_data_error_mapper,
)
from ..errors.get_future_tick_level_orderbook_historical_data_download_link_user_data_error import (
    GetFutureTickLevelOrderbookHistoricalDataDownloadLinkUserDataErrorBody,
    get_future_tick_level_orderbook_historical_data_download_link_user_data_error_mapper,
)
from ..errors.new_future_account_transfer_user_data_error import (
    NewFutureAccountTransferUserDataErrorBody,
    new_future_account_transfer_user_data_error_mapper,
)
from ..models.enums.data_type import DataTypeOrStr
from ..models.sapi_v1_futures_hist_data_link_response import SapiV1FuturesHistDataLinkResponse
from ..models.sapi_v1_futures_transfer_response import SapiV1FuturesTransferResponse
from ..models.sapi_v1_futures_transfer_response1 import SapiV1FuturesTransferResponse1
from ..server.server import Server


class Futures:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FuturesWithRawResponse(client, server, auth)

    def get_future_account_transaction_history_list_user_data(
        self,
        asset: str,
        start_time: int,
        timestamp: int,
        signature: str,
        *,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1FuturesTransferResponse1:
        """Weight(IP): 10

        Args:
            asset: Value sent with the request.
            start_time: UTC timestamp in ms
            timestamp: UTC timestamp in ms
            signature: Signature
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Futures Transfer Query

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_future_account_transaction_history_list_user_data(
            asset,
            start_time,
            timestamp,
            signature,
            end_time=end_time,
            current=current,
            size=size,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_future_tick_level_orderbook_historical_data_download_link_user_data(
        self,
        symbol: str,
        data_type: DataTypeOrStr,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1FuturesHistDataLinkResponse:
        """Weight(IP): 1

        Args:
            symbol: Value sent with the request.
            data_type: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            data link

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_future_tick_level_orderbook_historical_data_download_link_user_data(
            symbol,
            data_type,
            timestamp,
            signature,
            start_time=start_time,
            end_time=end_time,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def new_future_account_transfer_user_data(
        self,
        asset: str,
        amount: float,
        type_: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1FuturesTransferResponse:
        """Execute transfer between spot account and futures account.

        Weight(IP): 1

        Args:
            asset: Value sent with the request.
            amount: Value sent with the request.
            type_: 1: transfer from spot account to USDT-Ⓜ futures account. 2: transfer from USDT-Ⓜ futures account to
                spot account. 3: transfer from spot account to COIN-Ⓜ futures account. 4: transfer from COIN-Ⓜ futures
                account to spot account.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Futures Transfer

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.new_future_account_transfer_user_data(
            asset, amount, type_, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> FuturesWithRawResponse:
        return self._with_raw_response


class AsyncFutures:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFuturesWithRawResponse(client, server, auth)

    async def get_future_account_transaction_history_list_user_data(
        self,
        asset: str,
        start_time: int,
        timestamp: int,
        signature: str,
        *,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1FuturesTransferResponse1:
        """Weight(IP): 10

        Args:
            asset: Value sent with the request.
            start_time: UTC timestamp in ms
            timestamp: UTC timestamp in ms
            signature: Signature
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Futures Transfer Query

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_future_account_transaction_history_list_user_data(
                asset,
                start_time,
                timestamp,
                signature,
                end_time=end_time,
                current=current,
                size=size,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def get_future_tick_level_orderbook_historical_data_download_link_user_data(
        self,
        symbol: str,
        data_type: DataTypeOrStr,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1FuturesHistDataLinkResponse:
        """Weight(IP): 1

        Args:
            symbol: Value sent with the request.
            data_type: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            data link

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_future_tick_level_orderbook_historical_data_download_link_user_data(
                symbol,
                data_type,
                timestamp,
                signature,
                start_time=start_time,
                end_time=end_time,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def new_future_account_transfer_user_data(
        self,
        asset: str,
        amount: float,
        type_: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1FuturesTransferResponse:
        """Execute transfer between spot account and futures account.

        Weight(IP): 1

        Args:
            asset: Value sent with the request.
            amount: Value sent with the request.
            type_: 1: transfer from spot account to USDT-Ⓜ futures account. 2: transfer from USDT-Ⓜ futures account to
                spot account. 3: transfer from spot account to COIN-Ⓜ futures account. 4: transfer from COIN-Ⓜ futures
                account to spot account.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Futures Transfer

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.new_future_account_transfer_user_data(
                asset, amount, type_, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncFuturesWithRawResponse:
        return self._with_raw_response


class FuturesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_future_account_transaction_history_list_user_data(
        self,
        asset: str,
        start_time: int,
        timestamp: int,
        signature: str,
        *,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1FuturesTransferResponse1, GetFutureAccountTransactionHistoryListUserDataErrorBody]:
        """Weight(IP): 10

        Args:
            asset: Value sent with the request.
            start_time: UTC timestamp in ms
            timestamp: UTC timestamp in ms
            signature: Signature
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/futures/transfer"),
            query_params=[
                param[str]("asset", asset),
                param[int]("startTime", start_time),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1FuturesTransferResponse1],
            error_mapper=get_future_account_transaction_history_list_user_data_error_mapper,
            request_options=request_options,
        )

    def get_future_tick_level_orderbook_historical_data_download_link_user_data(
        self,
        symbol: str,
        data_type: DataTypeOrStr,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1FuturesHistDataLinkResponse, GetFutureTickLevelOrderbookHistoricalDataDownloadLinkUserDataErrorBody
    ]:
        """Weight(IP): 1

        Args:
            symbol: Value sent with the request.
            data_type: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/futures/histDataLink"),
            query_params=[
                param[str]("symbol", symbol),
                param[DataTypeOrStr]("dataType", data_type),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1FuturesHistDataLinkResponse],
            error_mapper=get_future_tick_level_orderbook_historical_data_download_link_user_data_error_mapper,
            request_options=request_options,
        )

    def new_future_account_transfer_user_data(
        self,
        asset: str,
        amount: float,
        type_: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1FuturesTransferResponse, NewFutureAccountTransferUserDataErrorBody]:
        """Execute transfer between spot account and futures account.

        Weight(IP): 1

        Args:
            asset: Value sent with the request.
            amount: Value sent with the request.
            type_: 1: transfer from spot account to USDT-Ⓜ futures account. 2: transfer from USDT-Ⓜ futures account to
                spot account. 3: transfer from spot account to COIN-Ⓜ futures account. 4: transfer from COIN-Ⓜ futures
                account to spot account.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/futures/transfer"),
            query_params=[
                param[str]("asset", asset),
                param[float]("amount", amount),
                param[int]("type", type_),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1FuturesTransferResponse],
            error_mapper=new_future_account_transfer_user_data_error_mapper,
            request_options=request_options,
        )


class AsyncFuturesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_future_account_transaction_history_list_user_data(
        self,
        asset: str,
        start_time: int,
        timestamp: int,
        signature: str,
        *,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1FuturesTransferResponse1, GetFutureAccountTransactionHistoryListUserDataErrorBody]:
        """Weight(IP): 10

        Args:
            asset: Value sent with the request.
            start_time: UTC timestamp in ms
            timestamp: UTC timestamp in ms
            signature: Signature
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/futures/transfer"),
            query_params=[
                param[str]("asset", asset),
                param[int]("startTime", start_time),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1FuturesTransferResponse1],
            error_mapper=get_future_account_transaction_history_list_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_future_tick_level_orderbook_historical_data_download_link_user_data(
        self,
        symbol: str,
        data_type: DataTypeOrStr,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1FuturesHistDataLinkResponse, GetFutureTickLevelOrderbookHistoricalDataDownloadLinkUserDataErrorBody
    ]:
        """Weight(IP): 1

        Args:
            symbol: Value sent with the request.
            data_type: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/futures/histDataLink"),
            query_params=[
                param[str]("symbol", symbol),
                param[DataTypeOrStr]("dataType", data_type),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1FuturesHistDataLinkResponse],
            error_mapper=get_future_tick_level_orderbook_historical_data_download_link_user_data_error_mapper,
            request_options=request_options,
        )

    async def new_future_account_transfer_user_data(
        self,
        asset: str,
        amount: float,
        type_: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1FuturesTransferResponse, NewFutureAccountTransferUserDataErrorBody]:
        """Execute transfer between spot account and futures account.

        Weight(IP): 1

        Args:
            asset: Value sent with the request.
            amount: Value sent with the request.
            type_: 1: transfer from spot account to USDT-Ⓜ futures account. 2: transfer from USDT-Ⓜ futures account to
                spot account. 3: transfer from spot account to COIN-Ⓜ futures account. 4: transfer from COIN-Ⓜ futures
                account to spot account.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/futures/transfer"),
            query_params=[
                param[str]("asset", asset),
                param[float]("amount", amount),
                param[int]("type", type_),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1FuturesTransferResponse],
            error_mapper=new_future_account_transfer_user_data_error_mapper,
            request_options=request_options,
        )
