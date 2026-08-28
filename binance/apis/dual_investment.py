from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder, param
from ..errors.change_auto_compound_status_user_data_error import (
    ChangeAutoCompoundStatusUserDataErrorBody,
    change_auto_compound_status_user_data_error_mapper,
)
from ..errors.check_dual_investment_accounts_user_data_error import (
    CheckDualInvestmentAccountsUserDataErrorBody,
    check_dual_investment_accounts_user_data_error_mapper,
)
from ..errors.get_dual_investment_positions_user_data_error import (
    GetDualInvestmentPositionsUserDataErrorBody,
    get_dual_investment_positions_user_data_error_mapper,
)
from ..errors.get_dual_investment_product_list_user_data_error import (
    GetDualInvestmentProductListUserDataErrorBody,
    get_dual_investment_product_list_user_data_error_mapper,
)
from ..errors.subscribe_dual_investment_products_user_data_error import (
    SubscribeDualInvestmentProductsUserDataErrorBody,
    subscribe_dual_investment_products_user_data_error_mapper,
)
from ..models.enums.auto_compound_plan import AutoCompoundPlanOrStr
from ..models.enums.option_type import OptionTypeOrStr
from ..models.enums.status2 import Status2OrStr
from ..models.sapi_v1_dci_product_accounts_response import SapiV1DciProductAccountsResponse
from ..models.sapi_v1_dci_product_auto_compound_edit_status_response import (
    SapiV1DciProductAutoCompoundEditStatusResponse,
)
from ..models.sapi_v1_dci_product_list_response import SapiV1DciProductListResponse
from ..models.sapi_v1_dci_product_positions_response import SapiV1DciProductPositionsResponse
from ..models.sapi_v1_dci_product_subscribe_response import SapiV1DciProductSubscribeResponse
from ..server.server import Server


class DualInvestment:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = DualInvestmentWithRawResponse(client, server, auth)

    def change_auto_compound_status_user_data(
        self,
        position_id: int,
        auto_compound_plan: AutoCompoundPlanOrStr,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1DciProductAutoCompoundEditStatusResponse:
        """Change Auto-Compound status

        - 15:31 ~ 16:00 UTC+8 This function is disabled

        Weight(IP): 1

        Rate Limit: Maximum 1 time/s per account

        Args:
            position_id: Get positionId from /sapi/v1/dci/product/positions
            auto_compound_plan: NONE: switch off the plan, STANDARD: standard plan, ADVANCED: advanced plan;
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Change Auto-Compound status response

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.change_auto_compound_status_user_data(
            position_id,
            auto_compound_plan,
            timestamp,
            signature,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def check_dual_investment_accounts_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1DciProductAccountsResponse:
        """Check Dual Investment accounts

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Dual Investment accounts

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.check_dual_investment_accounts_user_data(
            timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def get_dual_investment_positions_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        status: Status2OrStr | None = None,
        page_size: str | None = None,
        page_index: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1DciProductPositionsResponse:
        """Get Dual Investment positions (batch)

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            status: - PENDING: Products are purchasing, will give results later; - PURCHASE_SUCCESS: purchase
                successfully; - SETTLED: Products are finish settling; - PURCHASE_FAIL: fail to purchase; - REFUNDING:
                refund ongoing; - REFUND_SUCCESS: refund to spot account successfully; - SETTLING: Products are
                settling. If don't fill this field, will response all the position status.
            page_size: MIN 1, MAX 100; Default 100
            page_index: Page number, default is first page, start form 1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Dual Investment product list

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_dual_investment_positions_user_data(
            timestamp,
            signature,
            status=status,
            page_size=page_size,
            page_index=page_index,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_dual_investment_product_list_user_data(
        self,
        option_type: OptionTypeOrStr,
        exercised_coin: str,
        invest_coin: str,
        timestamp: int,
        signature: str,
        *,
        page_size: str | None = None,
        page_index: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1DciProductListResponse:
        """Get Dual Investment product list

        Weight(IP): 1

        Args:
            option_type: Input CALL or PUT
            exercised_coin: Target exercised asset, e.g.: if you subscribe to a high sell product (call option), you
                should input: - optionType: CALL, - exercisedCoin: USDT, - investCoin: BNB; if you subscribe to a low
                buy product (put option), you should input: - optionType: PUT, - exercisedCoin: BNB, - investCoin: USDT;
            invest_coin: Asset used for subscribing, e.g.: if you subscribe to a high sell product (call option), you
                should input: - optionType: CALL, - exercisedCoin: USDT, - investCoin: BNB; if you subscribe to a low
                buy product (put option), you should input: - optionType: PUT, - exercisedCoin: BNB, - investCoin: USDT;
            timestamp: UTC timestamp in ms
            signature: Signature
            page_size: MIN 1, MAX 100; Default 100
            page_index: Page number, default is first page, start form 1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Dual Investment product list

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_dual_investment_product_list_user_data(
            option_type,
            exercised_coin,
            invest_coin,
            timestamp,
            signature,
            page_size=page_size,
            page_index=page_index,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def subscribe_dual_investment_products_user_data(
        self,
        id: str,
        order_id: str,
        deposit_amount: float,
        auto_compound_plan: AutoCompoundPlanOrStr,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1DciProductSubscribeResponse:
        """Subscribe Dual Investment products

        - ``Products are not available.`` means that the APR changes to lower value, or the orders are not available.
        - ``Failed`` is a system or network errors.

        Weight(IP): 1

        Args:
            id: get id from /sapi/v1/dci/product/list
            order_id: get orderId from /sapi/v1/dci/product/list
            deposit_amount: Value sent with the request.
            auto_compound_plan: NONE: switch off the plan, STANDARD: standard plan, ADVANCED: advanced plan;
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Dual Investment product subscription response

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.subscribe_dual_investment_products_user_data(
            id,
            order_id,
            deposit_amount,
            auto_compound_plan,
            timestamp,
            signature,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> DualInvestmentWithRawResponse:
        return self._with_raw_response


class AsyncDualInvestment:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncDualInvestmentWithRawResponse(client, server, auth)

    async def change_auto_compound_status_user_data(
        self,
        position_id: int,
        auto_compound_plan: AutoCompoundPlanOrStr,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1DciProductAutoCompoundEditStatusResponse:
        """Change Auto-Compound status

        - 15:31 ~ 16:00 UTC+8 This function is disabled

        Weight(IP): 1

        Rate Limit: Maximum 1 time/s per account

        Args:
            position_id: Get positionId from /sapi/v1/dci/product/positions
            auto_compound_plan: NONE: switch off the plan, STANDARD: standard plan, ADVANCED: advanced plan;
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Change Auto-Compound status response

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.change_auto_compound_status_user_data(
                position_id,
                auto_compound_plan,
                timestamp,
                signature,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def check_dual_investment_accounts_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1DciProductAccountsResponse:
        """Check Dual Investment accounts

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Dual Investment accounts

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.check_dual_investment_accounts_user_data(
                timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def get_dual_investment_positions_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        status: Status2OrStr | None = None,
        page_size: str | None = None,
        page_index: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1DciProductPositionsResponse:
        """Get Dual Investment positions (batch)

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            status: - PENDING: Products are purchasing, will give results later; - PURCHASE_SUCCESS: purchase
                successfully; - SETTLED: Products are finish settling; - PURCHASE_FAIL: fail to purchase; - REFUNDING:
                refund ongoing; - REFUND_SUCCESS: refund to spot account successfully; - SETTLING: Products are
                settling. If don't fill this field, will response all the position status.
            page_size: MIN 1, MAX 100; Default 100
            page_index: Page number, default is first page, start form 1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Dual Investment product list

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_dual_investment_positions_user_data(
                timestamp,
                signature,
                status=status,
                page_size=page_size,
                page_index=page_index,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def get_dual_investment_product_list_user_data(
        self,
        option_type: OptionTypeOrStr,
        exercised_coin: str,
        invest_coin: str,
        timestamp: int,
        signature: str,
        *,
        page_size: str | None = None,
        page_index: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1DciProductListResponse:
        """Get Dual Investment product list

        Weight(IP): 1

        Args:
            option_type: Input CALL or PUT
            exercised_coin: Target exercised asset, e.g.: if you subscribe to a high sell product (call option), you
                should input: - optionType: CALL, - exercisedCoin: USDT, - investCoin: BNB; if you subscribe to a low
                buy product (put option), you should input: - optionType: PUT, - exercisedCoin: BNB, - investCoin: USDT;
            invest_coin: Asset used for subscribing, e.g.: if you subscribe to a high sell product (call option), you
                should input: - optionType: CALL, - exercisedCoin: USDT, - investCoin: BNB; if you subscribe to a low
                buy product (put option), you should input: - optionType: PUT, - exercisedCoin: BNB, - investCoin: USDT;
            timestamp: UTC timestamp in ms
            signature: Signature
            page_size: MIN 1, MAX 100; Default 100
            page_index: Page number, default is first page, start form 1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Dual Investment product list

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_dual_investment_product_list_user_data(
                option_type,
                exercised_coin,
                invest_coin,
                timestamp,
                signature,
                page_size=page_size,
                page_index=page_index,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def subscribe_dual_investment_products_user_data(
        self,
        id: str,
        order_id: str,
        deposit_amount: float,
        auto_compound_plan: AutoCompoundPlanOrStr,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1DciProductSubscribeResponse:
        """Subscribe Dual Investment products

        - ``Products are not available.`` means that the APR changes to lower value, or the orders are not available.
        - ``Failed`` is a system or network errors.

        Weight(IP): 1

        Args:
            id: get id from /sapi/v1/dci/product/list
            order_id: get orderId from /sapi/v1/dci/product/list
            deposit_amount: Value sent with the request.
            auto_compound_plan: NONE: switch off the plan, STANDARD: standard plan, ADVANCED: advanced plan;
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Dual Investment product subscription response

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.subscribe_dual_investment_products_user_data(
                id,
                order_id,
                deposit_amount,
                auto_compound_plan,
                timestamp,
                signature,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncDualInvestmentWithRawResponse:
        return self._with_raw_response


class DualInvestmentWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def change_auto_compound_status_user_data(
        self,
        position_id: int,
        auto_compound_plan: AutoCompoundPlanOrStr,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1DciProductAutoCompoundEditStatusResponse, ChangeAutoCompoundStatusUserDataErrorBody]:
        """Change Auto-Compound status

        - 15:31 ~ 16:00 UTC+8 This function is disabled

        Weight(IP): 1

        Rate Limit: Maximum 1 time/s per account

        Args:
            position_id: Get positionId from /sapi/v1/dci/product/positions
            auto_compound_plan: NONE: switch off the plan, STANDARD: standard plan, ADVANCED: advanced plan;
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/dci/product/auto_compound/edit-status"),
            query_params=[
                param[int]("positionId", position_id),
                param[AutoCompoundPlanOrStr]("autoCompoundPlan", auto_compound_plan),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1DciProductAutoCompoundEditStatusResponse],
            error_mapper=change_auto_compound_status_user_data_error_mapper,
            request_options=request_options,
        )

    def check_dual_investment_accounts_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1DciProductAccountsResponse, CheckDualInvestmentAccountsUserDataErrorBody]:
        """Check Dual Investment accounts

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/dci/product/accounts"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1DciProductAccountsResponse],
            error_mapper=check_dual_investment_accounts_user_data_error_mapper,
            request_options=request_options,
        )

    def get_dual_investment_positions_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        status: Status2OrStr | None = None,
        page_size: str | None = None,
        page_index: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1DciProductPositionsResponse, GetDualInvestmentPositionsUserDataErrorBody]:
        """Get Dual Investment positions (batch)

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            status: - PENDING: Products are purchasing, will give results later; - PURCHASE_SUCCESS: purchase
                successfully; - SETTLED: Products are finish settling; - PURCHASE_FAIL: fail to purchase; - REFUNDING:
                refund ongoing; - REFUND_SUCCESS: refund to spot account successfully; - SETTLING: Products are
                settling. If don't fill this field, will response all the position status.
            page_size: MIN 1, MAX 100; Default 100
            page_index: Page number, default is first page, start form 1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/dci/product/positions"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[Status2OrStr | None]("status", status),
                param[str | None]("pageSize", page_size),
                param[int | None]("pageIndex", page_index),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1DciProductPositionsResponse],
            error_mapper=get_dual_investment_positions_user_data_error_mapper,
            request_options=request_options,
        )

    def get_dual_investment_product_list_user_data(
        self,
        option_type: OptionTypeOrStr,
        exercised_coin: str,
        invest_coin: str,
        timestamp: int,
        signature: str,
        *,
        page_size: str | None = None,
        page_index: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1DciProductListResponse, GetDualInvestmentProductListUserDataErrorBody]:
        """Get Dual Investment product list

        Weight(IP): 1

        Args:
            option_type: Input CALL or PUT
            exercised_coin: Target exercised asset, e.g.: if you subscribe to a high sell product (call option), you
                should input: - optionType: CALL, - exercisedCoin: USDT, - investCoin: BNB; if you subscribe to a low
                buy product (put option), you should input: - optionType: PUT, - exercisedCoin: BNB, - investCoin: USDT;
            invest_coin: Asset used for subscribing, e.g.: if you subscribe to a high sell product (call option), you
                should input: - optionType: CALL, - exercisedCoin: USDT, - investCoin: BNB; if you subscribe to a low
                buy product (put option), you should input: - optionType: PUT, - exercisedCoin: BNB, - investCoin: USDT;
            timestamp: UTC timestamp in ms
            signature: Signature
            page_size: MIN 1, MAX 100; Default 100
            page_index: Page number, default is first page, start form 1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/dci/product/list"),
            query_params=[
                param[OptionTypeOrStr]("optionType", option_type),
                param[str]("exercisedCoin", exercised_coin),
                param[str]("investCoin", invest_coin),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("pageSize", page_size),
                param[int | None]("pageIndex", page_index),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1DciProductListResponse],
            error_mapper=get_dual_investment_product_list_user_data_error_mapper,
            request_options=request_options,
        )

    def subscribe_dual_investment_products_user_data(
        self,
        id: str,
        order_id: str,
        deposit_amount: float,
        auto_compound_plan: AutoCompoundPlanOrStr,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1DciProductSubscribeResponse, SubscribeDualInvestmentProductsUserDataErrorBody]:
        """Subscribe Dual Investment products

        - ``Products are not available.`` means that the APR changes to lower value, or the orders are not available.
        - ``Failed`` is a system or network errors.

        Weight(IP): 1

        Args:
            id: get id from /sapi/v1/dci/product/list
            order_id: get orderId from /sapi/v1/dci/product/list
            deposit_amount: Value sent with the request.
            auto_compound_plan: NONE: switch off the plan, STANDARD: standard plan, ADVANCED: advanced plan;
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/dci/product/subscribe"),
            query_params=[
                param[str]("id", id),
                param[str]("orderId", order_id),
                param[float]("depositAmount", deposit_amount),
                param[AutoCompoundPlanOrStr]("autoCompoundPlan", auto_compound_plan),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1DciProductSubscribeResponse],
            error_mapper=subscribe_dual_investment_products_user_data_error_mapper,
            request_options=request_options,
        )


class AsyncDualInvestmentWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def change_auto_compound_status_user_data(
        self,
        position_id: int,
        auto_compound_plan: AutoCompoundPlanOrStr,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1DciProductAutoCompoundEditStatusResponse, ChangeAutoCompoundStatusUserDataErrorBody]:
        """Change Auto-Compound status

        - 15:31 ~ 16:00 UTC+8 This function is disabled

        Weight(IP): 1

        Rate Limit: Maximum 1 time/s per account

        Args:
            position_id: Get positionId from /sapi/v1/dci/product/positions
            auto_compound_plan: NONE: switch off the plan, STANDARD: standard plan, ADVANCED: advanced plan;
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/dci/product/auto_compound/edit-status"),
            query_params=[
                param[int]("positionId", position_id),
                param[AutoCompoundPlanOrStr]("autoCompoundPlan", auto_compound_plan),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1DciProductAutoCompoundEditStatusResponse],
            error_mapper=change_auto_compound_status_user_data_error_mapper,
            request_options=request_options,
        )

    async def check_dual_investment_accounts_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1DciProductAccountsResponse, CheckDualInvestmentAccountsUserDataErrorBody]:
        """Check Dual Investment accounts

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/dci/product/accounts"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1DciProductAccountsResponse],
            error_mapper=check_dual_investment_accounts_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_dual_investment_positions_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        status: Status2OrStr | None = None,
        page_size: str | None = None,
        page_index: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1DciProductPositionsResponse, GetDualInvestmentPositionsUserDataErrorBody]:
        """Get Dual Investment positions (batch)

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            status: - PENDING: Products are purchasing, will give results later; - PURCHASE_SUCCESS: purchase
                successfully; - SETTLED: Products are finish settling; - PURCHASE_FAIL: fail to purchase; - REFUNDING:
                refund ongoing; - REFUND_SUCCESS: refund to spot account successfully; - SETTLING: Products are
                settling. If don't fill this field, will response all the position status.
            page_size: MIN 1, MAX 100; Default 100
            page_index: Page number, default is first page, start form 1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/dci/product/positions"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[Status2OrStr | None]("status", status),
                param[str | None]("pageSize", page_size),
                param[int | None]("pageIndex", page_index),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1DciProductPositionsResponse],
            error_mapper=get_dual_investment_positions_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_dual_investment_product_list_user_data(
        self,
        option_type: OptionTypeOrStr,
        exercised_coin: str,
        invest_coin: str,
        timestamp: int,
        signature: str,
        *,
        page_size: str | None = None,
        page_index: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1DciProductListResponse, GetDualInvestmentProductListUserDataErrorBody]:
        """Get Dual Investment product list

        Weight(IP): 1

        Args:
            option_type: Input CALL or PUT
            exercised_coin: Target exercised asset, e.g.: if you subscribe to a high sell product (call option), you
                should input: - optionType: CALL, - exercisedCoin: USDT, - investCoin: BNB; if you subscribe to a low
                buy product (put option), you should input: - optionType: PUT, - exercisedCoin: BNB, - investCoin: USDT;
            invest_coin: Asset used for subscribing, e.g.: if you subscribe to a high sell product (call option), you
                should input: - optionType: CALL, - exercisedCoin: USDT, - investCoin: BNB; if you subscribe to a low
                buy product (put option), you should input: - optionType: PUT, - exercisedCoin: BNB, - investCoin: USDT;
            timestamp: UTC timestamp in ms
            signature: Signature
            page_size: MIN 1, MAX 100; Default 100
            page_index: Page number, default is first page, start form 1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/dci/product/list"),
            query_params=[
                param[OptionTypeOrStr]("optionType", option_type),
                param[str]("exercisedCoin", exercised_coin),
                param[str]("investCoin", invest_coin),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("pageSize", page_size),
                param[int | None]("pageIndex", page_index),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1DciProductListResponse],
            error_mapper=get_dual_investment_product_list_user_data_error_mapper,
            request_options=request_options,
        )

    async def subscribe_dual_investment_products_user_data(
        self,
        id: str,
        order_id: str,
        deposit_amount: float,
        auto_compound_plan: AutoCompoundPlanOrStr,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1DciProductSubscribeResponse, SubscribeDualInvestmentProductsUserDataErrorBody]:
        """Subscribe Dual Investment products

        - ``Products are not available.`` means that the APR changes to lower value, or the orders are not available.
        - ``Failed`` is a system or network errors.

        Weight(IP): 1

        Args:
            id: get id from /sapi/v1/dci/product/list
            order_id: get orderId from /sapi/v1/dci/product/list
            deposit_amount: Value sent with the request.
            auto_compound_plan: NONE: switch off the plan, STANDARD: standard plan, ADVANCED: advanced plan;
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/dci/product/subscribe"),
            query_params=[
                param[str]("id", id),
                param[str]("orderId", order_id),
                param[float]("depositAmount", deposit_amount),
                param[AutoCompoundPlanOrStr]("autoCompoundPlan", auto_compound_plan),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1DciProductSubscribeResponse],
            error_mapper=subscribe_dual_investment_products_user_data_error_mapper,
            request_options=request_options,
        )
