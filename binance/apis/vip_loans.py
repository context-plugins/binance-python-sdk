from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder, param
from ..errors.check_locked_value_of_vip_collateral_account_user_data_error import (
    CheckLockedValueOfVipCollateralAccountUserDataErrorBody,
    check_locked_value_of_vip_collateral_account_user_data_error_mapper,
)
from ..errors.get_borrow_interest_rate_user_data_error import (
    GetBorrowInterestRateUserDataErrorBody,
    get_borrow_interest_rate_user_data_error_mapper,
)
from ..errors.get_collateral_asset_data_user_data_error import (
    GetCollateralAssetDataUserDataErrorBody,
    get_collateral_asset_data_user_data_error_mapper,
)
from ..errors.get_loanable_assets_data_error import (
    GetLoanableAssetsDataErrorBody,
    get_loanable_assets_data_error_mapper,
)
from ..errors.get_vip_loan_ongoing_orders_user_data_error import (
    GetVipLoanOngoingOrdersUserDataErrorBody,
    get_vip_loan_ongoing_orders_user_data_error_mapper,
)
from ..errors.get_vip_loan_repayment_history_user_data_error import (
    GetVipLoanRepaymentHistoryUserDataErrorBody,
    get_vip_loan_repayment_history_user_data_error_mapper,
)
from ..errors.query_application_status_user_data_error import (
    QueryApplicationStatusUserDataErrorBody,
    query_application_status_user_data_error_mapper,
)
from ..errors.vip_loan_borrow_error import VipLoanBorrowErrorBody, vip_loan_borrow_error_mapper
from ..errors.vip_loan_renew_error import VipLoanRenewErrorBody, vip_loan_renew_error_mapper
from ..errors.vip_loan_repay_trade_error import VipLoanRepayTradeErrorBody, vip_loan_repay_trade_error_mapper
from ..models.enums.is_flexible_rate import IsFlexibleRateOrStr
from ..models.sapi_v1_loan_vip_borrow_response import SapiV1LoanVipBorrowResponse
from ..models.sapi_v1_loan_vip_collateral_account_response import SapiV1LoanVipCollateralAccountResponse
from ..models.sapi_v1_loan_vip_collateral_data_response import SapiV1LoanVipCollateralDataResponse
from ..models.sapi_v1_loan_vip_loanable_data_response import SapiV1LoanVipLoanableDataResponse
from ..models.sapi_v1_loan_vip_ongoing_orders_response import SapiV1LoanVipOngoingOrdersResponse
from ..models.sapi_v1_loan_vip_renew_response import SapiV1LoanVipRenewResponse
from ..models.sapi_v1_loan_vip_repay_history_response import SapiV1LoanVipRepayHistoryResponse
from ..models.sapi_v1_loan_vip_repay_response import SapiV1LoanVipRepayResponse
from ..models.sapi_v1_loan_vip_request_data_response import SapiV1LoanVipRequestDataResponse
from ..models.sapi_v1_loan_vip_request_interest_rate_response import SapiV1LoanVipRequestInterestRateResponse
from ..server.server import Server


class VipLoans:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VipLoansWithRawResponse(client, server, auth)

    def check_locked_value_of_vip_collateral_account_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        collateral_account_id: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanVipCollateralAccountResponse:
        """VIP loan is available for VIP users only.

        Weight(IP): 6000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order id
            collateral_account_id: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            VIP Locked Value

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.check_locked_value_of_vip_collateral_account_user_data(
            timestamp,
            signature,
            order_id=order_id,
            collateral_account_id=collateral_account_id,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_borrow_interest_rate_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1LoanVipRequestInterestRateResponse]:
        """Get borrow interest rate.

        Weight(UID): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Max 10 assets, Multiple split by ","
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Borrow interest rate

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_borrow_interest_rate_user_data(
            timestamp, signature, loan_coin=loan_coin, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def get_collateral_asset_data_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        collateral_coin: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanVipCollateralDataResponse:
        """Get collateral asset data.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            collateral_coin: Coin used as collateral
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Collateral Asset Data

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_collateral_asset_data_user_data(
            timestamp,
            signature,
            collateral_coin=collateral_coin,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_loanable_assets_data(
        self,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        vip_level: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanVipLoanableDataResponse:
        """Get interest rate and borrow limit of loanable assets. The borrow limit is shown in USD value.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            vip_level: Defaults to user's vip level
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Loanable Assets Data

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_loanable_assets_data(
            timestamp,
            signature,
            loan_coin=loan_coin,
            vip_level=vip_level,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_vip_loan_ongoing_orders_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        collateral_account_id: int | None = None,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanVipOngoingOrdersResponse:
        """VIP loan is available for VIP users only.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order id
            collateral_account_id: Value sent with the request.
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            current: Current querying page. Start from 1. Default:1
            limit: Default 10; max 100.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Ongoing VIP Loan Orders

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_vip_loan_ongoing_orders_user_data(
            timestamp,
            signature,
            order_id=order_id,
            collateral_account_id=collateral_account_id,
            loan_coin=loan_coin,
            collateral_coin=collateral_coin,
            current=current,
            limit=limit,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_vip_loan_repayment_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        loan_coin: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanVipRepayHistoryResponse:
        """VIP loan is available for VIP users only.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order id
            loan_coin: Coin loaned
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            limit: Default 10; max 100.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            VIP Loan Repayment History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_vip_loan_repayment_history_user_data(
            timestamp,
            signature,
            order_id=order_id,
            loan_coin=loan_coin,
            start_time=start_time,
            end_time=end_time,
            current=current,
            limit=limit,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def query_application_status_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanVipRequestDataResponse:
        """Get Application Status

        Weight(UID): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            current: Current querying page. Start from 1. Default:1
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Application Status

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_application_status_user_data(
            timestamp, signature, current=current, limit=limit, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def vip_loan_borrow(
        self,
        loan_account_id: int,
        loan_amount: float,
        collateral_account_id: str,
        collateral_coin: str,
        is_flexible_rate: IsFlexibleRateOrStr,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        loan_term: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanVipBorrowResponse:
        """VIP loan is available for VIP users only.

        Weight(UID): 6000

        Args:
            loan_account_id: Value sent with the request.
            loan_amount: Value sent with the request.
            collateral_account_id: Value sent with the request.
            collateral_coin: Value sent with the request.
            is_flexible_rate: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            loan_term: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Collateral Assets Data

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.vip_loan_borrow(
            loan_account_id,
            loan_amount,
            collateral_account_id,
            collateral_coin,
            is_flexible_rate,
            timestamp,
            signature,
            loan_coin=loan_coin,
            loan_term=loan_term,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def vip_loan_renew(
        self,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        loan_term: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanVipRenewResponse:
        """VIP loan is available for VIP users only.

        Weight(UID): 6000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order id
            loan_term: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Loan renew result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.vip_loan_renew(
            timestamp,
            signature,
            order_id=order_id,
            loan_term=loan_term,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def vip_loan_repay_trade(
        self,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanVipRepayResponse:
        """VIP loan is available for VIP users only.

        Weight(UID): 6000

        Args:
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order id
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            VIP Loan Repayment

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.vip_loan_repay_trade(
            amount, timestamp, signature, order_id=order_id, recv_window=recv_window, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> VipLoansWithRawResponse:
        return self._with_raw_response


class AsyncVipLoans:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVipLoansWithRawResponse(client, server, auth)

    async def check_locked_value_of_vip_collateral_account_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        collateral_account_id: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanVipCollateralAccountResponse:
        """VIP loan is available for VIP users only.

        Weight(IP): 6000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order id
            collateral_account_id: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            VIP Locked Value

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.check_locked_value_of_vip_collateral_account_user_data(
                timestamp,
                signature,
                order_id=order_id,
                collateral_account_id=collateral_account_id,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def get_borrow_interest_rate_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1LoanVipRequestInterestRateResponse]:
        """Get borrow interest rate.

        Weight(UID): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Max 10 assets, Multiple split by ","
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Borrow interest rate

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_borrow_interest_rate_user_data(
                timestamp, signature, loan_coin=loan_coin, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def get_collateral_asset_data_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        collateral_coin: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanVipCollateralDataResponse:
        """Get collateral asset data.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            collateral_coin: Coin used as collateral
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Collateral Asset Data

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_collateral_asset_data_user_data(
                timestamp,
                signature,
                collateral_coin=collateral_coin,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def get_loanable_assets_data(
        self,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        vip_level: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanVipLoanableDataResponse:
        """Get interest rate and borrow limit of loanable assets. The borrow limit is shown in USD value.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            vip_level: Defaults to user's vip level
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Loanable Assets Data

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_loanable_assets_data(
                timestamp,
                signature,
                loan_coin=loan_coin,
                vip_level=vip_level,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def get_vip_loan_ongoing_orders_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        collateral_account_id: int | None = None,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanVipOngoingOrdersResponse:
        """VIP loan is available for VIP users only.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order id
            collateral_account_id: Value sent with the request.
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            current: Current querying page. Start from 1. Default:1
            limit: Default 10; max 100.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Ongoing VIP Loan Orders

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_vip_loan_ongoing_orders_user_data(
                timestamp,
                signature,
                order_id=order_id,
                collateral_account_id=collateral_account_id,
                loan_coin=loan_coin,
                collateral_coin=collateral_coin,
                current=current,
                limit=limit,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def get_vip_loan_repayment_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        loan_coin: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanVipRepayHistoryResponse:
        """VIP loan is available for VIP users only.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order id
            loan_coin: Coin loaned
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            limit: Default 10; max 100.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            VIP Loan Repayment History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_vip_loan_repayment_history_user_data(
                timestamp,
                signature,
                order_id=order_id,
                loan_coin=loan_coin,
                start_time=start_time,
                end_time=end_time,
                current=current,
                limit=limit,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def query_application_status_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanVipRequestDataResponse:
        """Get Application Status

        Weight(UID): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            current: Current querying page. Start from 1. Default:1
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Application Status

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_application_status_user_data(
                timestamp,
                signature,
                current=current,
                limit=limit,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def vip_loan_borrow(
        self,
        loan_account_id: int,
        loan_amount: float,
        collateral_account_id: str,
        collateral_coin: str,
        is_flexible_rate: IsFlexibleRateOrStr,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        loan_term: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanVipBorrowResponse:
        """VIP loan is available for VIP users only.

        Weight(UID): 6000

        Args:
            loan_account_id: Value sent with the request.
            loan_amount: Value sent with the request.
            collateral_account_id: Value sent with the request.
            collateral_coin: Value sent with the request.
            is_flexible_rate: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            loan_term: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Collateral Assets Data

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.vip_loan_borrow(
                loan_account_id,
                loan_amount,
                collateral_account_id,
                collateral_coin,
                is_flexible_rate,
                timestamp,
                signature,
                loan_coin=loan_coin,
                loan_term=loan_term,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def vip_loan_renew(
        self,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        loan_term: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanVipRenewResponse:
        """VIP loan is available for VIP users only.

        Weight(UID): 6000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order id
            loan_term: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Loan renew result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.vip_loan_renew(
                timestamp,
                signature,
                order_id=order_id,
                loan_term=loan_term,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def vip_loan_repay_trade(
        self,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanVipRepayResponse:
        """VIP loan is available for VIP users only.

        Weight(UID): 6000

        Args:
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order id
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            VIP Loan Repayment

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.vip_loan_repay_trade(
                amount,
                timestamp,
                signature,
                order_id=order_id,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVipLoansWithRawResponse:
        return self._with_raw_response


class VipLoansWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def check_locked_value_of_vip_collateral_account_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        collateral_account_id: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanVipCollateralAccountResponse, CheckLockedValueOfVipCollateralAccountUserDataErrorBody]:
        """VIP loan is available for VIP users only.

        Weight(IP): 6000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order id
            collateral_account_id: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/loan/vip/collateral/account"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("orderId", order_id),
                param[int | None]("collateralAccountId", collateral_account_id),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanVipCollateralAccountResponse],
            error_mapper=check_locked_value_of_vip_collateral_account_user_data_error_mapper,
            request_options=request_options,
        )

    def get_borrow_interest_rate_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1LoanVipRequestInterestRateResponse], GetBorrowInterestRateUserDataErrorBody]:
        """Get borrow interest rate.

        Weight(UID): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Max 10 assets, Multiple split by ","
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/loan/vip/request/interestRate"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("loanCoin", loan_coin),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1LoanVipRequestInterestRateResponse]],
            error_mapper=get_borrow_interest_rate_user_data_error_mapper,
            request_options=request_options,
        )

    def get_collateral_asset_data_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        collateral_coin: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanVipCollateralDataResponse, GetCollateralAssetDataUserDataErrorBody]:
        """Get collateral asset data.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            collateral_coin: Coin used as collateral
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/loan/vip/collateral/data"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("collateralCoin", collateral_coin),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanVipCollateralDataResponse],
            error_mapper=get_collateral_asset_data_user_data_error_mapper,
            request_options=request_options,
        )

    def get_loanable_assets_data(
        self,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        vip_level: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanVipLoanableDataResponse, GetLoanableAssetsDataErrorBody]:
        """Get interest rate and borrow limit of loanable assets. The borrow limit is shown in USD value.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            vip_level: Defaults to user's vip level
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/loan/vip/loanable/data"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("loanCoin", loan_coin),
                param[int | None]("vipLevel", vip_level),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanVipLoanableDataResponse],
            error_mapper=get_loanable_assets_data_error_mapper,
            request_options=request_options,
        )

    def get_vip_loan_ongoing_orders_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        collateral_account_id: int | None = None,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanVipOngoingOrdersResponse, GetVipLoanOngoingOrdersUserDataErrorBody]:
        """VIP loan is available for VIP users only.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order id
            collateral_account_id: Value sent with the request.
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            current: Current querying page. Start from 1. Default:1
            limit: Default 10; max 100.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/loan/vip/ongoing/orders"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("orderId", order_id),
                param[int | None]("collateralAccountId", collateral_account_id),
                param[str | None]("loanCoin", loan_coin),
                param[str | None]("collateralCoin", collateral_coin),
                param[int | None]("current", current),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanVipOngoingOrdersResponse],
            error_mapper=get_vip_loan_ongoing_orders_user_data_error_mapper,
            request_options=request_options,
        )

    def get_vip_loan_repayment_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        loan_coin: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanVipRepayHistoryResponse, GetVipLoanRepaymentHistoryUserDataErrorBody]:
        """VIP loan is available for VIP users only.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order id
            loan_coin: Coin loaned
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            limit: Default 10; max 100.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/loan/vip/repay/history"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("orderId", order_id),
                param[str | None]("loanCoin", loan_coin),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanVipRepayHistoryResponse],
            error_mapper=get_vip_loan_repayment_history_user_data_error_mapper,
            request_options=request_options,
        )

    def query_application_status_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanVipRequestDataResponse, QueryApplicationStatusUserDataErrorBody]:
        """Get Application Status

        Weight(UID): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            current: Current querying page. Start from 1. Default:1
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/loan/vip/request/data"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("current", current),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanVipRequestDataResponse],
            error_mapper=query_application_status_user_data_error_mapper,
            request_options=request_options,
        )

    def vip_loan_borrow(
        self,
        loan_account_id: int,
        loan_amount: float,
        collateral_account_id: str,
        collateral_coin: str,
        is_flexible_rate: IsFlexibleRateOrStr,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        loan_term: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanVipBorrowResponse, VipLoanBorrowErrorBody]:
        """VIP loan is available for VIP users only.

        Weight(UID): 6000

        Args:
            loan_account_id: Value sent with the request.
            loan_amount: Value sent with the request.
            collateral_account_id: Value sent with the request.
            collateral_coin: Value sent with the request.
            is_flexible_rate: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            loan_term: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/loan/vip/borrow"),
            query_params=[
                param[int]("loanAccountId", loan_account_id),
                param[float]("loanAmount", loan_amount),
                param[str]("collateralAccountId", collateral_account_id),
                param[str]("collateralCoin", collateral_coin),
                param[IsFlexibleRateOrStr]("isFlexibleRate", is_flexible_rate),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("loanCoin", loan_coin),
                param[int | None]("loanTerm", loan_term),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanVipBorrowResponse],
            error_mapper=vip_loan_borrow_error_mapper,
            request_options=request_options,
        )

    def vip_loan_renew(
        self,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        loan_term: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanVipRenewResponse, VipLoanRenewErrorBody]:
        """VIP loan is available for VIP users only.

        Weight(UID): 6000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order id
            loan_term: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/loan/vip/renew"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("orderId", order_id),
                param[int | None]("loanTerm", loan_term),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanVipRenewResponse],
            error_mapper=vip_loan_renew_error_mapper,
            request_options=request_options,
        )

    def vip_loan_repay_trade(
        self,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanVipRepayResponse, VipLoanRepayTradeErrorBody]:
        """VIP loan is available for VIP users only.

        Weight(UID): 6000

        Args:
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order id
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/loan/vip/repay"),
            query_params=[
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("orderId", order_id),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanVipRepayResponse],
            error_mapper=vip_loan_repay_trade_error_mapper,
            request_options=request_options,
        )


class AsyncVipLoansWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def check_locked_value_of_vip_collateral_account_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        collateral_account_id: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanVipCollateralAccountResponse, CheckLockedValueOfVipCollateralAccountUserDataErrorBody]:
        """VIP loan is available for VIP users only.

        Weight(IP): 6000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order id
            collateral_account_id: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/loan/vip/collateral/account"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("orderId", order_id),
                param[int | None]("collateralAccountId", collateral_account_id),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanVipCollateralAccountResponse],
            error_mapper=check_locked_value_of_vip_collateral_account_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_borrow_interest_rate_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1LoanVipRequestInterestRateResponse], GetBorrowInterestRateUserDataErrorBody]:
        """Get borrow interest rate.

        Weight(UID): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Max 10 assets, Multiple split by ","
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/loan/vip/request/interestRate"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("loanCoin", loan_coin),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1LoanVipRequestInterestRateResponse]],
            error_mapper=get_borrow_interest_rate_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_collateral_asset_data_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        collateral_coin: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanVipCollateralDataResponse, GetCollateralAssetDataUserDataErrorBody]:
        """Get collateral asset data.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            collateral_coin: Coin used as collateral
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/loan/vip/collateral/data"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("collateralCoin", collateral_coin),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanVipCollateralDataResponse],
            error_mapper=get_collateral_asset_data_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_loanable_assets_data(
        self,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        vip_level: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanVipLoanableDataResponse, GetLoanableAssetsDataErrorBody]:
        """Get interest rate and borrow limit of loanable assets. The borrow limit is shown in USD value.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            vip_level: Defaults to user's vip level
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/loan/vip/loanable/data"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("loanCoin", loan_coin),
                param[int | None]("vipLevel", vip_level),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanVipLoanableDataResponse],
            error_mapper=get_loanable_assets_data_error_mapper,
            request_options=request_options,
        )

    async def get_vip_loan_ongoing_orders_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        collateral_account_id: int | None = None,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanVipOngoingOrdersResponse, GetVipLoanOngoingOrdersUserDataErrorBody]:
        """VIP loan is available for VIP users only.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order id
            collateral_account_id: Value sent with the request.
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            current: Current querying page. Start from 1. Default:1
            limit: Default 10; max 100.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/loan/vip/ongoing/orders"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("orderId", order_id),
                param[int | None]("collateralAccountId", collateral_account_id),
                param[str | None]("loanCoin", loan_coin),
                param[str | None]("collateralCoin", collateral_coin),
                param[int | None]("current", current),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanVipOngoingOrdersResponse],
            error_mapper=get_vip_loan_ongoing_orders_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_vip_loan_repayment_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        loan_coin: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanVipRepayHistoryResponse, GetVipLoanRepaymentHistoryUserDataErrorBody]:
        """VIP loan is available for VIP users only.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order id
            loan_coin: Coin loaned
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            limit: Default 10; max 100.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/loan/vip/repay/history"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("orderId", order_id),
                param[str | None]("loanCoin", loan_coin),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanVipRepayHistoryResponse],
            error_mapper=get_vip_loan_repayment_history_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_application_status_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanVipRequestDataResponse, QueryApplicationStatusUserDataErrorBody]:
        """Get Application Status

        Weight(UID): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            current: Current querying page. Start from 1. Default:1
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/loan/vip/request/data"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("current", current),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanVipRequestDataResponse],
            error_mapper=query_application_status_user_data_error_mapper,
            request_options=request_options,
        )

    async def vip_loan_borrow(
        self,
        loan_account_id: int,
        loan_amount: float,
        collateral_account_id: str,
        collateral_coin: str,
        is_flexible_rate: IsFlexibleRateOrStr,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        loan_term: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanVipBorrowResponse, VipLoanBorrowErrorBody]:
        """VIP loan is available for VIP users only.

        Weight(UID): 6000

        Args:
            loan_account_id: Value sent with the request.
            loan_amount: Value sent with the request.
            collateral_account_id: Value sent with the request.
            collateral_coin: Value sent with the request.
            is_flexible_rate: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            loan_term: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/loan/vip/borrow"),
            query_params=[
                param[int]("loanAccountId", loan_account_id),
                param[float]("loanAmount", loan_amount),
                param[str]("collateralAccountId", collateral_account_id),
                param[str]("collateralCoin", collateral_coin),
                param[IsFlexibleRateOrStr]("isFlexibleRate", is_flexible_rate),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("loanCoin", loan_coin),
                param[int | None]("loanTerm", loan_term),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanVipBorrowResponse],
            error_mapper=vip_loan_borrow_error_mapper,
            request_options=request_options,
        )

    async def vip_loan_renew(
        self,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        loan_term: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanVipRenewResponse, VipLoanRenewErrorBody]:
        """VIP loan is available for VIP users only.

        Weight(UID): 6000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order id
            loan_term: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/loan/vip/renew"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("orderId", order_id),
                param[int | None]("loanTerm", loan_term),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanVipRenewResponse],
            error_mapper=vip_loan_renew_error_mapper,
            request_options=request_options,
        )

    async def vip_loan_repay_trade(
        self,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanVipRepayResponse, VipLoanRepayTradeErrorBody]:
        """VIP loan is available for VIP users only.

        Weight(UID): 6000

        Args:
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order id
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/loan/vip/repay"),
            query_params=[
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("orderId", order_id),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanVipRepayResponse],
            error_mapper=vip_loan_repay_trade_error_mapper,
            request_options=request_options,
        )
