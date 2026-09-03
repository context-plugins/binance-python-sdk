from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder, param
from ..errors.blvt_info_market_data_error import BlvtInfoMarketDataErrorBody, blvt_info_market_data_error_mapper
from ..errors.blvt_user_limit_info_user_data_error import (
    BlvtUserLimitInfoUserDataErrorBody,
    blvt_user_limit_info_user_data_error_mapper,
)
from ..errors.query_subscription_record_user_data_error import (
    QuerySubscriptionRecordUserDataErrorBody,
    query_subscription_record_user_data_error_mapper,
)
from ..errors.redeem_blvt_user_data_error import RedeemBlvtUserDataErrorBody, redeem_blvt_user_data_error_mapper
from ..errors.redemption_record_user_data_error import (
    RedemptionRecordUserDataErrorBody,
    redemption_record_user_data_error_mapper,
)
from ..errors.subscribe_blvt_user_data_error import (
    SubscribeBlvtUserDataErrorBody,
    subscribe_blvt_user_data_error_mapper,
)
from ..models.sapi_v1_blvt_redeem_record_response import SapiV1BlvtRedeemRecordResponse
from ..models.sapi_v1_blvt_redeem_response import SapiV1BlvtRedeemResponse
from ..models.sapi_v1_blvt_subscribe_record_response import SapiV1BlvtSubscribeRecordResponse
from ..models.sapi_v1_blvt_subscribe_response import SapiV1BlvtSubscribeResponse
from ..models.sapi_v1_blvt_token_info_response import SapiV1BlvtTokenInfoResponse
from ..models.sapi_v1_blvt_user_limit_response import SapiV1BlvtUserLimitResponse
from ..server.server import Server


class Blvt:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = BlvtWithRawResponse(client, server, auth)

    def blvt_info_market_data(
        self, *, token_name: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> list[SapiV1BlvtTokenInfoResponse]:
        """Weight(IP): 1

        Args:
            token_name: BTCDOWN, BTCUP
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of token information

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.blvt_info_market_data(
            token_name=token_name, request_options=request_options
        ).unwrap()

    def blvt_user_limit_info_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        token_name: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1BlvtUserLimitResponse]:
        """Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            token_name: BTCDOWN, BTCUP
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of token limits

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.blvt_user_limit_info_user_data(
            timestamp, signature, token_name=token_name, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def query_subscription_record_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        token_name: str | None = None,
        id: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1BlvtSubscribeRecordResponse:
        """- Only the data of the latest 90 days is available

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            token_name: BTCDOWN, BTCUP
            id: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of subscription record

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_subscription_record_user_data(
            timestamp,
            signature,
            token_name=token_name,
            id=id,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def redeem_blvt_user_data(
        self,
        token_name: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1BlvtRedeemResponse:
        """Weight(IP): 1

        Args:
            token_name: BTCDOWN, BTCUP
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Redemption record

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.redeem_blvt_user_data(
            token_name, amount, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def redemption_record_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        token_name: str | None = None,
        id: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1BlvtRedeemRecordResponse]:
        """- Only the data of the latest 90 days is available

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            token_name: BTCDOWN, BTCUP
            id: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: default 1000, max 1000
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of redemption record

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.redemption_record_user_data(
            timestamp,
            signature,
            token_name=token_name,
            id=id,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def subscribe_blvt_user_data(
        self,
        token_name: str,
        cost: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1BlvtSubscribeResponse:
        """Weight(IP): 1

        Args:
            token_name: BTCDOWN, BTCUP
            cost: Spot balance
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Subscription Info

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.subscribe_blvt_user_data(
            token_name, cost, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> BlvtWithRawResponse:
        return self._with_raw_response


class AsyncBlvt:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncBlvtWithRawResponse(client, server, auth)

    async def blvt_info_market_data(
        self, *, token_name: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> list[SapiV1BlvtTokenInfoResponse]:
        """Weight(IP): 1

        Args:
            token_name: BTCDOWN, BTCUP
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of token information

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.blvt_info_market_data(token_name=token_name, request_options=request_options)
        ).unwrap()

    async def blvt_user_limit_info_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        token_name: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1BlvtUserLimitResponse]:
        """Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            token_name: BTCDOWN, BTCUP
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of token limits

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.blvt_user_limit_info_user_data(
                timestamp, signature, token_name=token_name, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def query_subscription_record_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        token_name: str | None = None,
        id: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1BlvtSubscribeRecordResponse:
        """- Only the data of the latest 90 days is available

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            token_name: BTCDOWN, BTCUP
            id: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of subscription record

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_subscription_record_user_data(
                timestamp,
                signature,
                token_name=token_name,
                id=id,
                start_time=start_time,
                end_time=end_time,
                limit=limit,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def redeem_blvt_user_data(
        self,
        token_name: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1BlvtRedeemResponse:
        """Weight(IP): 1

        Args:
            token_name: BTCDOWN, BTCUP
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Redemption record

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.redeem_blvt_user_data(
                token_name, amount, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def redemption_record_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        token_name: str | None = None,
        id: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1BlvtRedeemRecordResponse]:
        """- Only the data of the latest 90 days is available

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            token_name: BTCDOWN, BTCUP
            id: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: default 1000, max 1000
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of redemption record

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.redemption_record_user_data(
                timestamp,
                signature,
                token_name=token_name,
                id=id,
                start_time=start_time,
                end_time=end_time,
                limit=limit,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def subscribe_blvt_user_data(
        self,
        token_name: str,
        cost: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1BlvtSubscribeResponse:
        """Weight(IP): 1

        Args:
            token_name: BTCDOWN, BTCUP
            cost: Spot balance
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Subscription Info

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.subscribe_blvt_user_data(
                token_name, cost, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncBlvtWithRawResponse:
        return self._with_raw_response


class BlvtWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def blvt_info_market_data(
        self, *, token_name: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[SapiV1BlvtTokenInfoResponse], BlvtInfoMarketDataErrorBody]:
        """Weight(IP): 1

        Args:
            token_name: BTCDOWN, BTCUP
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/blvt/tokenInfo"),
            query_params=[param[str | None]("tokenName", token_name)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1BlvtTokenInfoResponse]],
            error_mapper=blvt_info_market_data_error_mapper,
            request_options=request_options,
        )

    def blvt_user_limit_info_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        token_name: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1BlvtUserLimitResponse], BlvtUserLimitInfoUserDataErrorBody]:
        """Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            token_name: BTCDOWN, BTCUP
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/blvt/userLimit"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("tokenName", token_name),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1BlvtUserLimitResponse]],
            error_mapper=blvt_user_limit_info_user_data_error_mapper,
            request_options=request_options,
        )

    def query_subscription_record_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        token_name: str | None = None,
        id: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1BlvtSubscribeRecordResponse, QuerySubscriptionRecordUserDataErrorBody]:
        """- Only the data of the latest 90 days is available

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            token_name: BTCDOWN, BTCUP
            id: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/blvt/subscribe/record"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("tokenName", token_name),
                param[int | None]("id", id),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1BlvtSubscribeRecordResponse],
            error_mapper=query_subscription_record_user_data_error_mapper,
            request_options=request_options,
        )

    def redeem_blvt_user_data(
        self,
        token_name: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1BlvtRedeemResponse, RedeemBlvtUserDataErrorBody]:
        """Weight(IP): 1

        Args:
            token_name: BTCDOWN, BTCUP
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/blvt/redeem"),
            query_params=[
                param[str]("tokenName", token_name),
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1BlvtRedeemResponse],
            error_mapper=redeem_blvt_user_data_error_mapper,
            request_options=request_options,
        )

    def redemption_record_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        token_name: str | None = None,
        id: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1BlvtRedeemRecordResponse], RedemptionRecordUserDataErrorBody]:
        """- Only the data of the latest 90 days is available

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            token_name: BTCDOWN, BTCUP
            id: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: default 1000, max 1000
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/blvt/redeem/record"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("tokenName", token_name),
                param[int | None]("id", id),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1BlvtRedeemRecordResponse]],
            error_mapper=redemption_record_user_data_error_mapper,
            request_options=request_options,
        )

    def subscribe_blvt_user_data(
        self,
        token_name: str,
        cost: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1BlvtSubscribeResponse, SubscribeBlvtUserDataErrorBody]:
        """Weight(IP): 1

        Args:
            token_name: BTCDOWN, BTCUP
            cost: Spot balance
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/blvt/subscribe"),
            query_params=[
                param[str]("tokenName", token_name),
                param[float]("cost", cost),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1BlvtSubscribeResponse],
            error_mapper=subscribe_blvt_user_data_error_mapper,
            request_options=request_options,
        )


class AsyncBlvtWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def blvt_info_market_data(
        self, *, token_name: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[SapiV1BlvtTokenInfoResponse], BlvtInfoMarketDataErrorBody]:
        """Weight(IP): 1

        Args:
            token_name: BTCDOWN, BTCUP
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/blvt/tokenInfo"),
            query_params=[param[str | None]("tokenName", token_name)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1BlvtTokenInfoResponse]],
            error_mapper=blvt_info_market_data_error_mapper,
            request_options=request_options,
        )

    async def blvt_user_limit_info_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        token_name: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1BlvtUserLimitResponse], BlvtUserLimitInfoUserDataErrorBody]:
        """Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            token_name: BTCDOWN, BTCUP
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/blvt/userLimit"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("tokenName", token_name),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1BlvtUserLimitResponse]],
            error_mapper=blvt_user_limit_info_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_subscription_record_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        token_name: str | None = None,
        id: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1BlvtSubscribeRecordResponse, QuerySubscriptionRecordUserDataErrorBody]:
        """- Only the data of the latest 90 days is available

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            token_name: BTCDOWN, BTCUP
            id: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/blvt/subscribe/record"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("tokenName", token_name),
                param[int | None]("id", id),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1BlvtSubscribeRecordResponse],
            error_mapper=query_subscription_record_user_data_error_mapper,
            request_options=request_options,
        )

    async def redeem_blvt_user_data(
        self,
        token_name: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1BlvtRedeemResponse, RedeemBlvtUserDataErrorBody]:
        """Weight(IP): 1

        Args:
            token_name: BTCDOWN, BTCUP
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/blvt/redeem"),
            query_params=[
                param[str]("tokenName", token_name),
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1BlvtRedeemResponse],
            error_mapper=redeem_blvt_user_data_error_mapper,
            request_options=request_options,
        )

    async def redemption_record_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        token_name: str | None = None,
        id: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1BlvtRedeemRecordResponse], RedemptionRecordUserDataErrorBody]:
        """- Only the data of the latest 90 days is available

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            token_name: BTCDOWN, BTCUP
            id: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: default 1000, max 1000
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/blvt/redeem/record"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("tokenName", token_name),
                param[int | None]("id", id),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1BlvtRedeemRecordResponse]],
            error_mapper=redemption_record_user_data_error_mapper,
            request_options=request_options,
        )

    async def subscribe_blvt_user_data(
        self,
        token_name: str,
        cost: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1BlvtSubscribeResponse, SubscribeBlvtUserDataErrorBody]:
        """Weight(IP): 1

        Args:
            token_name: BTCDOWN, BTCUP
            cost: Spot balance
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/blvt/subscribe"),
            query_params=[
                param[str]("tokenName", token_name),
                param[float]("cost", cost),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1BlvtSubscribeResponse],
            error_mapper=subscribe_blvt_user_data_error_mapper,
            request_options=request_options,
        )
