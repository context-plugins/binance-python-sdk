from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder, param
from ..errors.change_fixed_activity_position_to_daily_position_user_data_error import (
    ChangeFixedActivityPositionToDailyPositionUserDataErrorBody,
    change_fixed_activity_position_to_daily_position_user_data_error_mapper,
)
from ..errors.get_fixed_activity_project_list_user_data_error import (
    GetFixedActivityProjectListUserDataErrorBody,
    get_fixed_activity_project_list_user_data_error_mapper,
)
from ..errors.get_fixed_activity_project_position_user_data_error import (
    GetFixedActivityProjectPositionUserDataErrorBody,
    get_fixed_activity_project_position_user_data_error_mapper,
)
from ..errors.purchase_fixed_activity_project_user_data_error import (
    PurchaseFixedActivityProjectUserDataErrorBody,
    purchase_fixed_activity_project_user_data_error_mapper,
)
from ..models.enums.sort_by import SortByOrStr
from ..models.enums.status import StatusOrStr
from ..models.enums.type8 import Type8OrStr
from ..models.sapi_v1_lending_customized_fixed_purchase_response import SapiV1LendingCustomizedFixedPurchaseResponse
from ..models.sapi_v1_lending_position_changed_response import SapiV1LendingPositionChangedResponse
from ..models.sapi_v1_lending_project_list_response import SapiV1LendingProjectListResponse
from ..models.sapi_v1_lending_project_position_list_response import SapiV1LendingProjectPositionListResponse
from ..server.server import Server


class Savings:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SavingsWithRawResponse(client, server, auth)

    def change_fixed_activity_position_to_daily_position_user_data(
        self,
        project_id: str,
        lot: str,
        timestamp: int,
        signature: str,
        *,
        position_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LendingPositionChangedResponse:
        """- PositionId is mandatory parameter for fixed position.

        Weight(IP): 1

        Args:
            project_id: Value sent with the request.
            lot: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            position_id: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Purchase information

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.change_fixed_activity_position_to_daily_position_user_data(
            project_id,
            lot,
            timestamp,
            signature,
            position_id=position_id,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_fixed_activity_project_list_user_data(
        self,
        type_: Type8OrStr,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        status: StatusOrStr | None = None,
        is_sort_asc: bool | None = None,
        sort_by: SortByOrStr | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1LendingProjectListResponse]:
        """Weight(IP): 1

        Args:
            type_: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            status: Default ``ALL``
            is_sort_asc: default "true"
            sort_by: Default ``START_TIME``
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of fixed projects

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_fixed_activity_project_list_user_data(
            type_,
            timestamp,
            signature,
            asset=asset,
            status=status,
            is_sort_asc=is_sort_asc,
            sort_by=sort_by,
            current=current,
            size=size,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_fixed_activity_project_position_user_data(
        self,
        asset: str,
        timestamp: int,
        signature: str,
        *,
        project_id: str | None = None,
        status: StatusOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1LendingProjectPositionListResponse]:
        """Weight(IP): 1

        Args:
            asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            project_id: Value sent with the request.
            status: Default ``ALL``
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of fixed project positions

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_fixed_activity_project_position_user_data(
            asset,
            timestamp,
            signature,
            project_id=project_id,
            status=status,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def purchase_fixed_activity_project_user_data(
        self,
        project_id: str,
        lot: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LendingCustomizedFixedPurchaseResponse:
        """Weight(IP): 1

        Args:
            project_id: Value sent with the request.
            lot: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Generated Purchase Id

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.purchase_fixed_activity_project_user_data(
            project_id, lot, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> SavingsWithRawResponse:
        return self._with_raw_response


class AsyncSavings:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSavingsWithRawResponse(client, server, auth)

    async def change_fixed_activity_position_to_daily_position_user_data(
        self,
        project_id: str,
        lot: str,
        timestamp: int,
        signature: str,
        *,
        position_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LendingPositionChangedResponse:
        """- PositionId is mandatory parameter for fixed position.

        Weight(IP): 1

        Args:
            project_id: Value sent with the request.
            lot: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            position_id: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Purchase information

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.change_fixed_activity_position_to_daily_position_user_data(
                project_id,
                lot,
                timestamp,
                signature,
                position_id=position_id,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def get_fixed_activity_project_list_user_data(
        self,
        type_: Type8OrStr,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        status: StatusOrStr | None = None,
        is_sort_asc: bool | None = None,
        sort_by: SortByOrStr | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1LendingProjectListResponse]:
        """Weight(IP): 1

        Args:
            type_: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            status: Default ``ALL``
            is_sort_asc: default "true"
            sort_by: Default ``START_TIME``
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of fixed projects

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_fixed_activity_project_list_user_data(
                type_,
                timestamp,
                signature,
                asset=asset,
                status=status,
                is_sort_asc=is_sort_asc,
                sort_by=sort_by,
                current=current,
                size=size,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def get_fixed_activity_project_position_user_data(
        self,
        asset: str,
        timestamp: int,
        signature: str,
        *,
        project_id: str | None = None,
        status: StatusOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1LendingProjectPositionListResponse]:
        """Weight(IP): 1

        Args:
            asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            project_id: Value sent with the request.
            status: Default ``ALL``
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of fixed project positions

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_fixed_activity_project_position_user_data(
                asset,
                timestamp,
                signature,
                project_id=project_id,
                status=status,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def purchase_fixed_activity_project_user_data(
        self,
        project_id: str,
        lot: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LendingCustomizedFixedPurchaseResponse:
        """Weight(IP): 1

        Args:
            project_id: Value sent with the request.
            lot: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Generated Purchase Id

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.purchase_fixed_activity_project_user_data(
                project_id, lot, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSavingsWithRawResponse:
        return self._with_raw_response


class SavingsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def change_fixed_activity_position_to_daily_position_user_data(
        self,
        project_id: str,
        lot: str,
        timestamp: int,
        signature: str,
        *,
        position_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LendingPositionChangedResponse, ChangeFixedActivityPositionToDailyPositionUserDataErrorBody]:
        """- PositionId is mandatory parameter for fixed position.

        Weight(IP): 1

        Args:
            project_id: Value sent with the request.
            lot: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            position_id: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/lending/positionChanged"),
            query_params=[
                param[str]("projectId", project_id),
                param[str]("lot", lot),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("positionId", position_id),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LendingPositionChangedResponse],
            error_mapper=change_fixed_activity_position_to_daily_position_user_data_error_mapper,
            request_options=request_options,
        )

    def get_fixed_activity_project_list_user_data(
        self,
        type_: Type8OrStr,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        status: StatusOrStr | None = None,
        is_sort_asc: bool | None = None,
        sort_by: SortByOrStr | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1LendingProjectListResponse], GetFixedActivityProjectListUserDataErrorBody]:
        """Weight(IP): 1

        Args:
            type_: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            status: Default ``ALL``
            is_sort_asc: default "true"
            sort_by: Default ``START_TIME``
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/lending/project/list"),
            query_params=[
                param[Type8OrStr]("type", type_),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("asset", asset),
                param[StatusOrStr | None]("status", status),
                param[bool | None]("isSortAsc", is_sort_asc),
                param[SortByOrStr | None]("sortBy", sort_by),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1LendingProjectListResponse]],
            error_mapper=get_fixed_activity_project_list_user_data_error_mapper,
            request_options=request_options,
        )

    def get_fixed_activity_project_position_user_data(
        self,
        asset: str,
        timestamp: int,
        signature: str,
        *,
        project_id: str | None = None,
        status: StatusOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1LendingProjectPositionListResponse], GetFixedActivityProjectPositionUserDataErrorBody]:
        """Weight(IP): 1

        Args:
            asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            project_id: Value sent with the request.
            status: Default ``ALL``
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/lending/project/position/list"),
            query_params=[
                param[str]("asset", asset),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("projectId", project_id),
                param[StatusOrStr | None]("status", status),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1LendingProjectPositionListResponse]],
            error_mapper=get_fixed_activity_project_position_user_data_error_mapper,
            request_options=request_options,
        )

    def purchase_fixed_activity_project_user_data(
        self,
        project_id: str,
        lot: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LendingCustomizedFixedPurchaseResponse, PurchaseFixedActivityProjectUserDataErrorBody]:
        """Weight(IP): 1

        Args:
            project_id: Value sent with the request.
            lot: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/lending/customizedFixed/purchase"),
            query_params=[
                param[str]("projectId", project_id),
                param[str]("lot", lot),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LendingCustomizedFixedPurchaseResponse],
            error_mapper=purchase_fixed_activity_project_user_data_error_mapper,
            request_options=request_options,
        )


class AsyncSavingsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def change_fixed_activity_position_to_daily_position_user_data(
        self,
        project_id: str,
        lot: str,
        timestamp: int,
        signature: str,
        *,
        position_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LendingPositionChangedResponse, ChangeFixedActivityPositionToDailyPositionUserDataErrorBody]:
        """- PositionId is mandatory parameter for fixed position.

        Weight(IP): 1

        Args:
            project_id: Value sent with the request.
            lot: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            position_id: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/lending/positionChanged"),
            query_params=[
                param[str]("projectId", project_id),
                param[str]("lot", lot),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("positionId", position_id),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LendingPositionChangedResponse],
            error_mapper=change_fixed_activity_position_to_daily_position_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_fixed_activity_project_list_user_data(
        self,
        type_: Type8OrStr,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        status: StatusOrStr | None = None,
        is_sort_asc: bool | None = None,
        sort_by: SortByOrStr | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1LendingProjectListResponse], GetFixedActivityProjectListUserDataErrorBody]:
        """Weight(IP): 1

        Args:
            type_: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            status: Default ``ALL``
            is_sort_asc: default "true"
            sort_by: Default ``START_TIME``
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/lending/project/list"),
            query_params=[
                param[Type8OrStr]("type", type_),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("asset", asset),
                param[StatusOrStr | None]("status", status),
                param[bool | None]("isSortAsc", is_sort_asc),
                param[SortByOrStr | None]("sortBy", sort_by),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1LendingProjectListResponse]],
            error_mapper=get_fixed_activity_project_list_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_fixed_activity_project_position_user_data(
        self,
        asset: str,
        timestamp: int,
        signature: str,
        *,
        project_id: str | None = None,
        status: StatusOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1LendingProjectPositionListResponse], GetFixedActivityProjectPositionUserDataErrorBody]:
        """Weight(IP): 1

        Args:
            asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            project_id: Value sent with the request.
            status: Default ``ALL``
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/lending/project/position/list"),
            query_params=[
                param[str]("asset", asset),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("projectId", project_id),
                param[StatusOrStr | None]("status", status),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1LendingProjectPositionListResponse]],
            error_mapper=get_fixed_activity_project_position_user_data_error_mapper,
            request_options=request_options,
        )

    async def purchase_fixed_activity_project_user_data(
        self,
        project_id: str,
        lot: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LendingCustomizedFixedPurchaseResponse, PurchaseFixedActivityProjectUserDataErrorBody]:
        """Weight(IP): 1

        Args:
            project_id: Value sent with the request.
            lot: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/lending/customizedFixed/purchase"),
            query_params=[
                param[str]("projectId", project_id),
                param[str]("lot", lot),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LendingCustomizedFixedPurchaseResponse],
            error_mapper=purchase_fixed_activity_project_user_data_error_mapper,
            request_options=request_options,
        )
