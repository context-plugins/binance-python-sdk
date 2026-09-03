from __future__ import annotations

from typing import Any
from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
    raw_error_response,
)
from ..errors.close_a_listen_key_user_stream_error import (
    CloseAListenKeyUserStreamErrorBody,
    close_a_listen_key_user_stream_error_mapper,
)
from ..errors.ping_keep_alive_a_listen_key_user_stream_api_error import (
    PingKeepAliveAListenKeyUserStreamApiErrorBody,
    ping_keep_alive_a_listen_key_user_stream_api_error_mapper,
)
from ..models.api_v3_user_data_stream_response import ApiV3UserDataStreamResponse
from ..server.server import Server


class Stream:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = StreamWithRawResponse(client, server, auth)

    def close_a_listen_key_user_stream(
        self, *, listen_key: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Close out a user data stream.

        Weight: 2

        Args:
            listen_key: User websocket listen key
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.close_a_listen_key_user_stream(
            listen_key=listen_key, request_options=request_options
        ).unwrap()

    def create_a_listen_key_user_stream(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV3UserDataStreamResponse:
        """Start a new user data stream. The stream will close after 60 minutes unless a keepalive is sent. If the
        account has an active ``listenKey``, that ``listenKey`` will be returned and its validity will be extended for
        60 minutes.

        Weight: 2

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Listen key

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_a_listen_key_user_stream(request_options=request_options).unwrap()

    def ping_keep_alive_a_listen_key_user_stream(
        self, *, listen_key: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Keepalive a user data stream to prevent a time out. User data streams will close after 60 minutes. It's
        recommended to send a ping about every 30 minutes.

        Weight: 2

        Args:
            listen_key: User websocket listen key
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.ping_keep_alive_a_listen_key_user_stream(
            listen_key=listen_key, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> StreamWithRawResponse:
        return self._with_raw_response


class AsyncStream:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncStreamWithRawResponse(client, server, auth)

    async def close_a_listen_key_user_stream(
        self, *, listen_key: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Close out a user data stream.

        Weight: 2

        Args:
            listen_key: User websocket listen key
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.close_a_listen_key_user_stream(
                listen_key=listen_key, request_options=request_options
            )
        ).unwrap()

    async def create_a_listen_key_user_stream(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV3UserDataStreamResponse:
        """Start a new user data stream. The stream will close after 60 minutes unless a keepalive is sent. If the
        account has an active ``listenKey``, that ``listenKey`` will be returned and its validity will be extended for
        60 minutes.

        Weight: 2

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Listen key

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_a_listen_key_user_stream(request_options=request_options)).unwrap()

    async def ping_keep_alive_a_listen_key_user_stream(
        self, *, listen_key: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Keepalive a user data stream to prevent a time out. User data streams will close after 60 minutes. It's
        recommended to send a ping about every 30 minutes.

        Weight: 2

        Args:
            listen_key: User websocket listen key
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.ping_keep_alive_a_listen_key_user_stream(
                listen_key=listen_key, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncStreamWithRawResponse:
        return self._with_raw_response


class StreamWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def close_a_listen_key_user_stream(
        self, *, listen_key: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, CloseAListenKeyUserStreamErrorBody]:
        """Close out a user data stream.

        Weight: 2

        Args:
            listen_key: User websocket listen key
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/api/v3/userDataStream"),
            query_params=[param[str | None]("listenKey", listen_key)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[Any],
            error_mapper=close_a_listen_key_user_stream_error_mapper,
            request_options=request_options,
        )

    def create_a_listen_key_user_stream(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV3UserDataStreamResponse, RawError]:
        """Start a new user data stream. The stream will close after 60 minutes unless a keepalive is sent. If the
        account has an active ``listenKey``, that ``listenKey`` will be returned and its validity will be extended for
        60 minutes.

        Weight: 2

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/v3/userDataStream"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ApiV3UserDataStreamResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def ping_keep_alive_a_listen_key_user_stream(
        self, *, listen_key: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, PingKeepAliveAListenKeyUserStreamApiErrorBody]:
        """Keepalive a user data stream to prevent a time out. User data streams will close after 60 minutes. It's
        recommended to send a ping about every 30 minutes.

        Weight: 2

        Args:
            listen_key: User websocket listen key
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/api/v3/userDataStream"),
            query_params=[param[str | None]("listenKey", listen_key)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[Any],
            error_mapper=ping_keep_alive_a_listen_key_user_stream_api_error_mapper,
            request_options=request_options,
        )


class AsyncStreamWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def close_a_listen_key_user_stream(
        self, *, listen_key: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, CloseAListenKeyUserStreamErrorBody]:
        """Close out a user data stream.

        Weight: 2

        Args:
            listen_key: User websocket listen key
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/api/v3/userDataStream"),
            query_params=[param[str | None]("listenKey", listen_key)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[Any],
            error_mapper=close_a_listen_key_user_stream_error_mapper,
            request_options=request_options,
        )

    async def create_a_listen_key_user_stream(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV3UserDataStreamResponse, RawError]:
        """Start a new user data stream. The stream will close after 60 minutes unless a keepalive is sent. If the
        account has an active ``listenKey``, that ``listenKey`` will be returned and its validity will be extended for
        60 minutes.

        Weight: 2

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/v3/userDataStream"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ApiV3UserDataStreamResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def ping_keep_alive_a_listen_key_user_stream(
        self, *, listen_key: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, PingKeepAliveAListenKeyUserStreamApiErrorBody]:
        """Keepalive a user data stream to prevent a time out. User data streams will close after 60 minutes. It's
        recommended to send a ping about every 30 minutes.

        Weight: 2

        Args:
            listen_key: User websocket listen key
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/api/v3/userDataStream"),
            query_params=[param[str | None]("listenKey", listen_key)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[Any],
            error_mapper=ping_keep_alive_a_listen_key_user_stream_api_error_mapper,
            request_options=request_options,
        )
