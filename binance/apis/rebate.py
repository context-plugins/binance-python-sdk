from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder, param
from ..errors.get_spot_rebate_history_records_user_data_error import (
    GetSpotRebateHistoryRecordsUserDataErrorBody,
    get_spot_rebate_history_records_user_data_error_mapper,
)
from ..models.sapi_v1_rebate_tax_query_response import SapiV1RebateTaxQueryResponse
from ..server.server import Server


class Rebate:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = RebateWithRawResponse(client, server, auth)

    def get_spot_rebate_history_records_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1RebateTaxQueryResponse:
        """- The max interval between startTime and endTime is 90 days.
        - If startTime and endTime are not sent, the recent 7 days' data will be returned.
        - The earliest startTime is supported on June 10, 2020

        Weight(UID): 3000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            page: default 1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Rebate History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_spot_rebate_history_records_user_data(
            timestamp,
            signature,
            start_time=start_time,
            end_time=end_time,
            page=page,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> RebateWithRawResponse:
        return self._with_raw_response


class AsyncRebate:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncRebateWithRawResponse(client, server, auth)

    async def get_spot_rebate_history_records_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1RebateTaxQueryResponse:
        """- The max interval between startTime and endTime is 90 days.
        - If startTime and endTime are not sent, the recent 7 days' data will be returned.
        - The earliest startTime is supported on June 10, 2020

        Weight(UID): 3000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            page: default 1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Rebate History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_spot_rebate_history_records_user_data(
                timestamp,
                signature,
                start_time=start_time,
                end_time=end_time,
                page=page,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncRebateWithRawResponse:
        return self._with_raw_response


class RebateWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_spot_rebate_history_records_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1RebateTaxQueryResponse, GetSpotRebateHistoryRecordsUserDataErrorBody]:
        """- The max interval between startTime and endTime is 90 days.
        - If startTime and endTime are not sent, the recent 7 days' data will be returned.
        - The earliest startTime is supported on June 10, 2020

        Weight(UID): 3000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            page: default 1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/rebate/taxQuery"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("page", page),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1RebateTaxQueryResponse],
            error_mapper=get_spot_rebate_history_records_user_data_error_mapper,
            request_options=request_options,
        )


class AsyncRebateWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_spot_rebate_history_records_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1RebateTaxQueryResponse, GetSpotRebateHistoryRecordsUserDataErrorBody]:
        """- The max interval between startTime and endTime is 90 days.
        - If startTime and endTime are not sent, the recent 7 days' data will be returned.
        - The earliest startTime is supported on June 10, 2020

        Weight(UID): 3000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            page: default 1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/rebate/taxQuery"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("page", page),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1RebateTaxQueryResponse],
            error_mapper=get_spot_rebate_history_records_user_data_error_mapper,
            request_options=request_options,
        )
