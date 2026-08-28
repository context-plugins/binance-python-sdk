from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder, param
from ..errors.get_nft_asset_user_data_error import GetNftAssetUserDataErrorBody, get_nft_asset_user_data_error_mapper
from ..errors.get_nft_deposit_history_user_data_error import (
    GetNftDepositHistoryUserDataErrorBody,
    get_nft_deposit_history_user_data_error_mapper,
)
from ..errors.get_nft_transaction_history_user_data_error import (
    GetNftTransactionHistoryUserDataErrorBody,
    get_nft_transaction_history_user_data_error_mapper,
)
from ..errors.get_nft_withdraw_history_user_data_error import (
    GetNftWithdrawHistoryUserDataErrorBody,
    get_nft_withdraw_history_user_data_error_mapper,
)
from ..models.sapi_v1_nft_history_deposit_response import SapiV1NftHistoryDepositResponse
from ..models.sapi_v1_nft_history_transactions_response import SapiV1NftHistoryTransactionsResponse
from ..models.sapi_v1_nft_history_withdraw_response import SapiV1NftHistoryWithdrawResponse
from ..models.sapi_v1_nft_user_get_asset_response import SapiV1NftUserGetAssetResponse
from ..server.server import Server


class Nft:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NftWithRawResponse(client, server, auth)

    def get_nft_asset_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        limit: int | None = None,
        page: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1NftUserGetAssetResponse:
        """Weight(UID): 3000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            limit: Default 50, Max 50
            page: Default 1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Asset Information

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_nft_asset_user_data(
            timestamp, signature, limit=limit, page=page, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def get_nft_deposit_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        page: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1NftHistoryDepositResponse:
        """- The max interval between startTime and endTime is 90 days.
        - If startTime and endTime are not sent, the recent 7 days' data will be returned.

        Weight(UID): 3000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default 50, Max 50
            page: Default 1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            NFT Deposit History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_nft_deposit_history_user_data(
            timestamp,
            signature,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
            page=page,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_nft_transaction_history_user_data(
        self,
        order_type: int,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        page: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1NftHistoryTransactionsResponse:
        """- The max interval between startTime and endTime is 90 days.
        - If startTime and endTime are not sent, the recent 7 days' data will be returned.

        Weight(UID): 3000

        Args:
            order_type: 0: purchase order, 1: sell order, 2: royalty income, 3: primary market order, 4: mint fee
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default 50, Max 50
            page: Default 1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            NFT Transaction History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_nft_transaction_history_user_data(
            order_type,
            timestamp,
            signature,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
            page=page,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_nft_withdraw_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        page: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1NftHistoryWithdrawResponse:
        """- The max interval between startTime and endTime is 90 days.
        - If startTime and endTime are not sent, the recent 7 days' data will be returned.

        Weight(UID): 3000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default 50, Max 50
            page: Default 1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            NFT Withdraw History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_nft_withdraw_history_user_data(
            timestamp,
            signature,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
            page=page,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> NftWithRawResponse:
        return self._with_raw_response


class AsyncNft:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNftWithRawResponse(client, server, auth)

    async def get_nft_asset_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        limit: int | None = None,
        page: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1NftUserGetAssetResponse:
        """Weight(UID): 3000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            limit: Default 50, Max 50
            page: Default 1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Asset Information

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_nft_asset_user_data(
                timestamp, signature, limit=limit, page=page, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def get_nft_deposit_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        page: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1NftHistoryDepositResponse:
        """- The max interval between startTime and endTime is 90 days.
        - If startTime and endTime are not sent, the recent 7 days' data will be returned.

        Weight(UID): 3000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default 50, Max 50
            page: Default 1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            NFT Deposit History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_nft_deposit_history_user_data(
                timestamp,
                signature,
                start_time=start_time,
                end_time=end_time,
                limit=limit,
                page=page,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def get_nft_transaction_history_user_data(
        self,
        order_type: int,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        page: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1NftHistoryTransactionsResponse:
        """- The max interval between startTime and endTime is 90 days.
        - If startTime and endTime are not sent, the recent 7 days' data will be returned.

        Weight(UID): 3000

        Args:
            order_type: 0: purchase order, 1: sell order, 2: royalty income, 3: primary market order, 4: mint fee
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default 50, Max 50
            page: Default 1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            NFT Transaction History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_nft_transaction_history_user_data(
                order_type,
                timestamp,
                signature,
                start_time=start_time,
                end_time=end_time,
                limit=limit,
                page=page,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def get_nft_withdraw_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        page: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1NftHistoryWithdrawResponse:
        """- The max interval between startTime and endTime is 90 days.
        - If startTime and endTime are not sent, the recent 7 days' data will be returned.

        Weight(UID): 3000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default 50, Max 50
            page: Default 1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            NFT Withdraw History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_nft_withdraw_history_user_data(
                timestamp,
                signature,
                start_time=start_time,
                end_time=end_time,
                limit=limit,
                page=page,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncNftWithRawResponse:
        return self._with_raw_response


class NftWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_nft_asset_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        limit: int | None = None,
        page: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1NftUserGetAssetResponse, GetNftAssetUserDataErrorBody]:
        """Weight(UID): 3000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            limit: Default 50, Max 50
            page: Default 1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/nft/user/getAsset"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("limit", limit),
                param[int | None]("page", page),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1NftUserGetAssetResponse],
            error_mapper=get_nft_asset_user_data_error_mapper,
            request_options=request_options,
        )

    def get_nft_deposit_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        page: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1NftHistoryDepositResponse, GetNftDepositHistoryUserDataErrorBody]:
        """- The max interval between startTime and endTime is 90 days.
        - If startTime and endTime are not sent, the recent 7 days' data will be returned.

        Weight(UID): 3000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default 50, Max 50
            page: Default 1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/nft/history/deposit"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("limit", limit),
                param[int | None]("page", page),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1NftHistoryDepositResponse],
            error_mapper=get_nft_deposit_history_user_data_error_mapper,
            request_options=request_options,
        )

    def get_nft_transaction_history_user_data(
        self,
        order_type: int,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        page: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1NftHistoryTransactionsResponse, GetNftTransactionHistoryUserDataErrorBody]:
        """- The max interval between startTime and endTime is 90 days.
        - If startTime and endTime are not sent, the recent 7 days' data will be returned.

        Weight(UID): 3000

        Args:
            order_type: 0: purchase order, 1: sell order, 2: royalty income, 3: primary market order, 4: mint fee
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default 50, Max 50
            page: Default 1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/nft/history/transactions"),
            query_params=[
                param[int]("orderType", order_type),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("limit", limit),
                param[int | None]("page", page),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1NftHistoryTransactionsResponse],
            error_mapper=get_nft_transaction_history_user_data_error_mapper,
            request_options=request_options,
        )

    def get_nft_withdraw_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        page: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1NftHistoryWithdrawResponse, GetNftWithdrawHistoryUserDataErrorBody]:
        """- The max interval between startTime and endTime is 90 days.
        - If startTime and endTime are not sent, the recent 7 days' data will be returned.

        Weight(UID): 3000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default 50, Max 50
            page: Default 1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/nft/history/withdraw"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("limit", limit),
                param[int | None]("page", page),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1NftHistoryWithdrawResponse],
            error_mapper=get_nft_withdraw_history_user_data_error_mapper,
            request_options=request_options,
        )


class AsyncNftWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_nft_asset_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        limit: int | None = None,
        page: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1NftUserGetAssetResponse, GetNftAssetUserDataErrorBody]:
        """Weight(UID): 3000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            limit: Default 50, Max 50
            page: Default 1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/nft/user/getAsset"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("limit", limit),
                param[int | None]("page", page),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1NftUserGetAssetResponse],
            error_mapper=get_nft_asset_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_nft_deposit_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        page: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1NftHistoryDepositResponse, GetNftDepositHistoryUserDataErrorBody]:
        """- The max interval between startTime and endTime is 90 days.
        - If startTime and endTime are not sent, the recent 7 days' data will be returned.

        Weight(UID): 3000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default 50, Max 50
            page: Default 1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/nft/history/deposit"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("limit", limit),
                param[int | None]("page", page),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1NftHistoryDepositResponse],
            error_mapper=get_nft_deposit_history_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_nft_transaction_history_user_data(
        self,
        order_type: int,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        page: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1NftHistoryTransactionsResponse, GetNftTransactionHistoryUserDataErrorBody]:
        """- The max interval between startTime and endTime is 90 days.
        - If startTime and endTime are not sent, the recent 7 days' data will be returned.

        Weight(UID): 3000

        Args:
            order_type: 0: purchase order, 1: sell order, 2: royalty income, 3: primary market order, 4: mint fee
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default 50, Max 50
            page: Default 1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/nft/history/transactions"),
            query_params=[
                param[int]("orderType", order_type),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("limit", limit),
                param[int | None]("page", page),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1NftHistoryTransactionsResponse],
            error_mapper=get_nft_transaction_history_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_nft_withdraw_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        page: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1NftHistoryWithdrawResponse, GetNftWithdrawHistoryUserDataErrorBody]:
        """- The max interval between startTime and endTime is 90 days.
        - If startTime and endTime are not sent, the recent 7 days' data will be returned.

        Weight(UID): 3000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default 50, Max 50
            page: Default 1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/nft/history/withdraw"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("limit", limit),
                param[int | None]("page", page),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1NftHistoryWithdrawResponse],
            error_mapper=get_nft_withdraw_history_user_data_error_mapper,
            request_options=request_options,
        )
