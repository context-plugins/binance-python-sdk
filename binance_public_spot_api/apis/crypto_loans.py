from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder, param
from ..errors.adjust_ltv_flexible_loan_adjust_ltv_trade_error import (
    AdjustLtvFlexibleLoanAdjustLtvTradeErrorBody,
    adjust_ltv_flexible_loan_adjust_ltv_trade_error_mapper,
)
from ..errors.adjust_ltv_get_flexible_loan_ltv_adjustment_history_user_data_error import (
    AdjustLtvGetFlexibleLoanLtvAdjustmentHistoryUserDataErrorBody,
    adjust_ltv_get_flexible_loan_ltv_adjustment_history_user_data_error_mapper,
)
from ..errors.borrow_flexible_loan_borrow_trade_error import (
    BorrowFlexibleLoanBorrowTradeErrorBody,
    borrow_flexible_loan_borrow_trade_error_mapper,
)
from ..errors.borrow_get_flexible_loan_borrow_history_user_data_error import (
    BorrowGetFlexibleLoanBorrowHistoryUserDataErrorBody,
    borrow_get_flexible_loan_borrow_history_user_data_error_mapper,
)
from ..errors.borrow_get_flexible_loan_ongoing_orders_user_data_error import (
    BorrowGetFlexibleLoanOngoingOrdersUserDataErrorBody,
    borrow_get_flexible_loan_ongoing_orders_user_data_error_mapper,
)
from ..errors.check_collateral_repay_rate_user_data_error import (
    CheckCollateralRepayRateUserDataErrorBody,
    check_collateral_repay_rate_user_data_error_mapper,
)
from ..errors.crypto_loan_adjust_ltv_trade_error import (
    CryptoLoanAdjustLtvTradeErrorBody,
    crypto_loan_adjust_ltv_trade_error_mapper,
)
from ..errors.crypto_loan_borrow_trade_error import (
    CryptoLoanBorrowTradeErrorBody,
    crypto_loan_borrow_trade_error_mapper,
)
from ..errors.crypto_loan_customize_margin_call_trade_error import (
    CryptoLoanCustomizeMarginCallTradeErrorBody,
    crypto_loan_customize_margin_call_trade_error_mapper,
)
from ..errors.crypto_loan_repay_trade_error import CryptoLoanRepayTradeErrorBody, crypto_loan_repay_trade_error_mapper
from ..errors.get_collateral_assets_data_user_data_error import (
    GetCollateralAssetsDataUserDataErrorBody,
    get_collateral_assets_data_user_data_error_mapper,
)
from ..errors.get_crypto_loans_borrow_history_user_data_error import (
    GetCryptoLoansBorrowHistoryUserDataErrorBody,
    get_crypto_loans_borrow_history_user_data_error_mapper,
)
from ..errors.get_crypto_loans_income_history_user_data_error import (
    GetCryptoLoansIncomeHistoryUserDataErrorBody,
    get_crypto_loans_income_history_user_data_error_mapper,
)
from ..errors.get_flexible_loan_assets_data_user_data_error import (
    GetFlexibleLoanAssetsDataUserDataErrorBody,
    get_flexible_loan_assets_data_user_data_error_mapper,
)
from ..errors.get_flexible_loan_collateral_assets_data_user_data_error import (
    GetFlexibleLoanCollateralAssetsDataUserDataErrorBody,
    get_flexible_loan_collateral_assets_data_user_data_error_mapper,
)
from ..errors.get_loan_ltv_adjustment_history_user_data_error import (
    GetLoanLtvAdjustmentHistoryUserDataErrorBody,
    get_loan_ltv_adjustment_history_user_data_error_mapper,
)
from ..errors.get_loan_ongoing_orders_user_data_error import (
    GetLoanOngoingOrdersUserDataErrorBody,
    get_loan_ongoing_orders_user_data_error_mapper,
)
from ..errors.get_loan_repayment_history_user_data_error import (
    GetLoanRepaymentHistoryUserDataErrorBody,
    get_loan_repayment_history_user_data_error_mapper,
)
from ..errors.get_loanable_assets_data_user_data_error import (
    GetLoanableAssetsDataUserDataErrorBody,
    get_loanable_assets_data_user_data_error_mapper,
)
from ..errors.repay_flexible_loan_repay_trade_error import (
    RepayFlexibleLoanRepayTradeErrorBody,
    repay_flexible_loan_repay_trade_error_mapper,
)
from ..errors.repay_get_flexible_loan_repayment_history_user_data_error import (
    RepayGetFlexibleLoanRepaymentHistoryUserDataErrorBody,
    repay_get_flexible_loan_repayment_history_user_data_error_mapper,
)
from ..models.enums.direction import DirectionOrStr
from ..models.enums.type9 import Type9OrStr
from ..models.sapi_v1_loan_adjust_ltv_response import SapiV1LoanAdjustLtvResponse
from ..models.sapi_v1_loan_borrow_history_response import SapiV1LoanBorrowHistoryResponse
from ..models.sapi_v1_loan_borrow_response import SapiV1LoanBorrowResponse
from ..models.sapi_v1_loan_collateral_data_response import SapiV1LoanCollateralDataResponse
from ..models.sapi_v1_loan_customize_margin_call_response import SapiV1LoanCustomizeMarginCallResponse
from ..models.sapi_v1_loan_income_response import SapiV1LoanIncomeResponse
from ..models.sapi_v1_loan_loanable_data_response import SapiV1LoanLoanableDataResponse
from ..models.sapi_v1_loan_ltv_adjustment_history_response import SapiV1LoanLtvAdjustmentHistoryResponse
from ..models.sapi_v1_loan_ongoing_orders_response import SapiV1LoanOngoingOrdersResponse
from ..models.sapi_v1_loan_repay_collateral_rate_response import SapiV1LoanRepayCollateralRateResponse
from ..models.sapi_v1_loan_repay_history_response import SapiV1LoanRepayHistoryResponse
from ..models.sapi_v2_loan_flexible_adjust_ltv_response import SapiV2LoanFlexibleAdjustLtvResponse
from ..models.sapi_v2_loan_flexible_borrow_history_response import SapiV2LoanFlexibleBorrowHistoryResponse
from ..models.sapi_v2_loan_flexible_borrow_response import SapiV2LoanFlexibleBorrowResponse
from ..models.sapi_v2_loan_flexible_collateral_data_response import SapiV2LoanFlexibleCollateralDataResponse
from ..models.sapi_v2_loan_flexible_loanable_data_response import SapiV2LoanFlexibleLoanableDataResponse
from ..models.sapi_v2_loan_flexible_ltv_adjustment_history_response import (
    SapiV2LoanFlexibleLtvAdjustmentHistoryResponse,
)
from ..models.sapi_v2_loan_flexible_ongoing_orders_response import SapiV2LoanFlexibleOngoingOrdersResponse
from ..models.sapi_v2_loan_flexible_repay_history_response import SapiV2LoanFlexibleRepayHistoryResponse
from ..models.sapi_v2_loan_flexible_repay_response import SapiV2LoanFlexibleRepayResponse
from ..models.unions.sapi_v1_loan_repay_response import SapiV1LoanRepayResponse
from ..server.server import Server


class CryptoLoans:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CryptoLoansWithRawResponse(client, server, auth)

    def adjust_ltv_flexible_loan_adjust_ltv_trade(
        self,
        adjustment_amount: float,
        direction: DirectionOrStr,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV2LoanFlexibleAdjustLtvResponse:
        """- API Key needs Spot & Margin Trading permission for this endpoint

        Weight(UID): 6000

        Args:
            adjustment_amount: Value sent with the request.
            direction: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            adjust LTV result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.adjust_ltv_flexible_loan_adjust_ltv_trade(
            adjustment_amount,
            direction,
            timestamp,
            signature,
            loan_coin=loan_coin,
            collateral_coin=collateral_coin,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def adjust_ltv_get_flexible_loan_ltv_adjustment_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV2LoanFlexibleLtvAdjustmentHistoryResponse:
        """- If startTime and endTime are not sent, the recent 90-day data will be returned.
        - The max interval between startTime and endTime is 180 days.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            LTV adjustment history

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.adjust_ltv_get_flexible_loan_ltv_adjustment_history_user_data(
            timestamp,
            signature,
            loan_coin=loan_coin,
            collateral_coin=collateral_coin,
            start_time=start_time,
            end_time=end_time,
            current=current,
            limit=limit,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def borrow_flexible_loan_borrow_trade(
        self,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        loan_amount: float | None = None,
        collateral_coin: str | None = None,
        collateral_amount: float | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV2LoanFlexibleBorrowResponse:
        """- Only available for master account

        Weight(UID): 6000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            loan_amount: Loan amount
            collateral_coin: Coin used as collateral
            collateral_amount: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Collateral Assets Data

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.borrow_flexible_loan_borrow_trade(
            timestamp,
            signature,
            loan_coin=loan_coin,
            loan_amount=loan_amount,
            collateral_coin=collateral_coin,
            collateral_amount=collateral_amount,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def borrow_get_flexible_loan_borrow_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV2LoanFlexibleBorrowHistoryResponse:
        """- If startTime and endTime are not sent, the recent 90-day data will be returned.
        - The max interval between startTime and endTime is 180 days.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Loan borrow histroy

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.borrow_get_flexible_loan_borrow_history_user_data(
            timestamp,
            signature,
            loan_coin=loan_coin,
            collateral_coin=collateral_coin,
            start_time=start_time,
            end_time=end_time,
            current=current,
            limit=limit,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def borrow_get_flexible_loan_ongoing_orders_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV2LoanFlexibleOngoingOrdersResponse:
        """Weight(IP): 300

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            current: Current querying page. Start from 1. Default:1
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Collateral Assets Data

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.borrow_get_flexible_loan_ongoing_orders_user_data(
            timestamp,
            signature,
            loan_coin=loan_coin,
            collateral_coin=collateral_coin,
            current=current,
            limit=limit,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def check_collateral_repay_rate_user_data(
        self,
        loan_coin: str,
        collateral_coin: str,
        repay_amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanRepayCollateralRateResponse:
        """Get the the rate of collateral coin / loan coin when using collateral repay, the rate will be valid within 8
        second.

        Weight(IP): 6000

        Args:
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            repay_amount: repay amount of loanCoin
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Collateral Assets Data

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.check_collateral_repay_rate_user_data(
            loan_coin,
            collateral_coin,
            repay_amount,
            timestamp,
            signature,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def crypto_loan_adjust_ltv_trade(
        self,
        order_id: int,
        amount: float,
        direction: DirectionOrStr,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanAdjustLtvResponse:
        """Weight(UID): 6000

        Args:
            order_id: Order ID
            amount: Amount
            direction: 'ADDITIONAL', 'REDUCED'
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            LTV Adjust

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.crypto_loan_adjust_ltv_trade(
            order_id, amount, direction, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def crypto_loan_borrow_trade(
        self,
        loan_coin: str,
        collateral_coin: str,
        loan_term: int,
        timestamp: int,
        signature: str,
        *,
        loan_amount: float | None = None,
        collateral_amount: float | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanBorrowResponse:
        """Weight(UID): 6000

        Args:
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            loan_term: 7/14/30/90/180 days
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_amount: Loan amount
            collateral_amount: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Borrow Information

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.crypto_loan_borrow_trade(
            loan_coin,
            collateral_coin,
            loan_term,
            timestamp,
            signature,
            loan_amount=loan_amount,
            collateral_amount=collateral_amount,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def crypto_loan_customize_margin_call_trade(
        self,
        margin_call: float,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        collateral_coin: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanCustomizeMarginCallResponse:
        """Customize margin call for ongoing orders only.

        Weight(UID): 6000

        Args:
            margin_call: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Mandatory when collateralCoin is empty. Send either orderId or collateralCoin, if both parameters
                are sent, take orderId only.
            collateral_coin: Coin used as collateral
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Collateral Assets Data

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.crypto_loan_customize_margin_call_trade(
            margin_call,
            timestamp,
            signature,
            order_id=order_id,
            collateral_coin=collateral_coin,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def crypto_loan_repay_trade(
        self,
        order_id: int,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        type_: int | None = None,
        collateral_return: bool | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanRepayResponse:
        """Weight(UID): 6000

        Args:
            order_id: Order ID
            amount: Repayment Amount
            timestamp: UTC timestamp in ms
            signature: Signature
            type_: Default: 1. 1 for 'repay with borrowed coin'; 2 for 'repay with collateral'.
            collateral_return: Default: TRUE. TRUE: Return extra collateral to spot account; FALSE: Keep extra
                collateral in the order.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Repayment Information

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.crypto_loan_repay_trade(
            order_id,
            amount,
            timestamp,
            signature,
            type_=type_,
            collateral_return=collateral_return,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_collateral_assets_data_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        collateral_coin: str | None = None,
        vip_level: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanCollateralDataResponse:
        """Get LTV information and collateral limit of collateral assets. The collateral limit is shown in USD value.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            collateral_coin: Coin used as collateral
            vip_level: Defaults to user's vip level
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Collateral Assets Data

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_collateral_assets_data_user_data(
            timestamp,
            signature,
            collateral_coin=collateral_coin,
            vip_level=vip_level,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_crypto_loans_borrow_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanBorrowHistoryResponse:
        """- If startTime and endTime are not sent, the recent 90-day data will be returned.
        - The max interval between startTime and endTime is 180 days.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: orderId in POST /sapi/v1/loan/borrow
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            limit: default 10, max 100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Borrow History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_crypto_loans_borrow_history_user_data(
            timestamp,
            signature,
            order_id=order_id,
            loan_coin=loan_coin,
            collateral_coin=collateral_coin,
            start_time=start_time,
            end_time=end_time,
            current=current,
            limit=limit,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_crypto_loans_income_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        type_: Type9OrStr | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1LoanIncomeResponse]:
        """- If startTime and endTime are not sent, the recent 7-day data will be returned.
        - The max interval between startTime and endTime is 30 days.

        Weight(UID): 6000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            type_: All types will be returned by default. * ``borrowIn`` * ``collateralSpent`` * ``repayAmount`` *
                ``collateralReturn`` - Collateral return after repayment * ``addCollateral`` * ``removeCollateral`` *
                ``collateralReturnAfterLiquidation``
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: default 20, max 100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Loan History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_crypto_loans_income_history_user_data(
            timestamp,
            signature,
            asset=asset,
            type_=type_,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_flexible_loan_assets_data_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV2LoanFlexibleLoanableDataResponse:
        """Get interest rate and borrow limit of flexible loanable assets. The borrow limit is shown in USD value.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Loan asset data

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_flexible_loan_assets_data_user_data(
            timestamp, signature, loan_coin=loan_coin, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def get_flexible_loan_collateral_assets_data_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        collateral_coin: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV2LoanFlexibleCollateralDataResponse:
        """Get LTV information and collateral limit of flexible loan's collateral assets. The collateral limit is shown
        in USD value.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            collateral_coin: Coin used as collateral
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Loan asset data

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_flexible_loan_collateral_assets_data_user_data(
            timestamp,
            signature,
            collateral_coin=collateral_coin,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_loan_ltv_adjustment_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanLtvAdjustmentHistoryResponse:
        """If startTime and endTime are not sent, the recent 90-day data will be returned. The max interval between
        startTime and endTime is 180 days.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order ID
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            limit: default 10, max 100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            LTV Adjustment History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_loan_ltv_adjustment_history_user_data(
            timestamp,
            signature,
            order_id=order_id,
            loan_coin=loan_coin,
            collateral_coin=collateral_coin,
            start_time=start_time,
            end_time=end_time,
            current=current,
            limit=limit,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_loan_ongoing_orders_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanOngoingOrdersResponse:
        """Weight(IP): 300

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: orderId in POST /sapi/v1/loan/borrow
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            current: Current querying page. Start from 1; default:1, max:1000
            limit: default 10, max 100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Ongoing Orders

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_loan_ongoing_orders_user_data(
            timestamp,
            signature,
            order_id=order_id,
            loan_coin=loan_coin,
            collateral_coin=collateral_coin,
            current=current,
            limit=limit,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_loan_repayment_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanRepayHistoryResponse:
        """If startTime and endTime are not sent, the recent 90-day data will be returned. The max interval between
        startTime and endTime is 180 days.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order ID
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            limit: default 10, max 100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Loan Repayment History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_loan_repayment_history_user_data(
            timestamp,
            signature,
            order_id=order_id,
            loan_coin=loan_coin,
            collateral_coin=collateral_coin,
            start_time=start_time,
            end_time=end_time,
            current=current,
            limit=limit,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_loanable_assets_data_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        vip_level: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanLoanableDataResponse:
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
        return self._with_raw_response.get_loanable_assets_data_user_data(
            timestamp,
            signature,
            loan_coin=loan_coin,
            vip_level=vip_level,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def repay_flexible_loan_repay_trade(
        self,
        repay_amount: float,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        collateral_return: bool | None = None,
        full_repayment: bool | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV2LoanFlexibleRepayResponse:
        """- repayAmount is mandatory even fullRepayment = FALSE

        Weight(IP): 6000

        Args:
            repay_amount: repay amount of loanCoin
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            collateral_return: Default: TRUE. TRUE: Return extra collateral to earn account; FALSE: Keep extra
                collateral in the order, and lower LTV.
            full_repayment: Default: FALSE. TRUE: Full repayment; FALSE: Partial repayment, based on loanAmount
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Loan repay

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.repay_flexible_loan_repay_trade(
            repay_amount,
            timestamp,
            signature,
            loan_coin=loan_coin,
            collateral_coin=collateral_coin,
            collateral_return=collateral_return,
            full_repayment=full_repayment,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def repay_get_flexible_loan_repayment_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV2LoanFlexibleRepayHistoryResponse:
        """- If startTime and endTime are not sent, the recent 90-day data will be returned.
        - The max interval between startTime and endTime is 180 days.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Loan repay history

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.repay_get_flexible_loan_repayment_history_user_data(
            timestamp,
            signature,
            loan_coin=loan_coin,
            collateral_coin=collateral_coin,
            start_time=start_time,
            end_time=end_time,
            current=current,
            limit=limit,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> CryptoLoansWithRawResponse:
        return self._with_raw_response


class AsyncCryptoLoans:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCryptoLoansWithRawResponse(client, server, auth)

    async def adjust_ltv_flexible_loan_adjust_ltv_trade(
        self,
        adjustment_amount: float,
        direction: DirectionOrStr,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV2LoanFlexibleAdjustLtvResponse:
        """- API Key needs Spot & Margin Trading permission for this endpoint

        Weight(UID): 6000

        Args:
            adjustment_amount: Value sent with the request.
            direction: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            adjust LTV result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.adjust_ltv_flexible_loan_adjust_ltv_trade(
                adjustment_amount,
                direction,
                timestamp,
                signature,
                loan_coin=loan_coin,
                collateral_coin=collateral_coin,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def adjust_ltv_get_flexible_loan_ltv_adjustment_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV2LoanFlexibleLtvAdjustmentHistoryResponse:
        """- If startTime and endTime are not sent, the recent 90-day data will be returned.
        - The max interval between startTime and endTime is 180 days.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            LTV adjustment history

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.adjust_ltv_get_flexible_loan_ltv_adjustment_history_user_data(
                timestamp,
                signature,
                loan_coin=loan_coin,
                collateral_coin=collateral_coin,
                start_time=start_time,
                end_time=end_time,
                current=current,
                limit=limit,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def borrow_flexible_loan_borrow_trade(
        self,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        loan_amount: float | None = None,
        collateral_coin: str | None = None,
        collateral_amount: float | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV2LoanFlexibleBorrowResponse:
        """- Only available for master account

        Weight(UID): 6000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            loan_amount: Loan amount
            collateral_coin: Coin used as collateral
            collateral_amount: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Collateral Assets Data

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.borrow_flexible_loan_borrow_trade(
                timestamp,
                signature,
                loan_coin=loan_coin,
                loan_amount=loan_amount,
                collateral_coin=collateral_coin,
                collateral_amount=collateral_amount,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def borrow_get_flexible_loan_borrow_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV2LoanFlexibleBorrowHistoryResponse:
        """- If startTime and endTime are not sent, the recent 90-day data will be returned.
        - The max interval between startTime and endTime is 180 days.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Loan borrow histroy

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.borrow_get_flexible_loan_borrow_history_user_data(
                timestamp,
                signature,
                loan_coin=loan_coin,
                collateral_coin=collateral_coin,
                start_time=start_time,
                end_time=end_time,
                current=current,
                limit=limit,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def borrow_get_flexible_loan_ongoing_orders_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV2LoanFlexibleOngoingOrdersResponse:
        """Weight(IP): 300

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            current: Current querying page. Start from 1. Default:1
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Collateral Assets Data

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.borrow_get_flexible_loan_ongoing_orders_user_data(
                timestamp,
                signature,
                loan_coin=loan_coin,
                collateral_coin=collateral_coin,
                current=current,
                limit=limit,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def check_collateral_repay_rate_user_data(
        self,
        loan_coin: str,
        collateral_coin: str,
        repay_amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanRepayCollateralRateResponse:
        """Get the the rate of collateral coin / loan coin when using collateral repay, the rate will be valid within 8
        second.

        Weight(IP): 6000

        Args:
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            repay_amount: repay amount of loanCoin
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Collateral Assets Data

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.check_collateral_repay_rate_user_data(
                loan_coin,
                collateral_coin,
                repay_amount,
                timestamp,
                signature,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def crypto_loan_adjust_ltv_trade(
        self,
        order_id: int,
        amount: float,
        direction: DirectionOrStr,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanAdjustLtvResponse:
        """Weight(UID): 6000

        Args:
            order_id: Order ID
            amount: Amount
            direction: 'ADDITIONAL', 'REDUCED'
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            LTV Adjust

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.crypto_loan_adjust_ltv_trade(
                order_id,
                amount,
                direction,
                timestamp,
                signature,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def crypto_loan_borrow_trade(
        self,
        loan_coin: str,
        collateral_coin: str,
        loan_term: int,
        timestamp: int,
        signature: str,
        *,
        loan_amount: float | None = None,
        collateral_amount: float | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanBorrowResponse:
        """Weight(UID): 6000

        Args:
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            loan_term: 7/14/30/90/180 days
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_amount: Loan amount
            collateral_amount: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Borrow Information

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.crypto_loan_borrow_trade(
                loan_coin,
                collateral_coin,
                loan_term,
                timestamp,
                signature,
                loan_amount=loan_amount,
                collateral_amount=collateral_amount,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def crypto_loan_customize_margin_call_trade(
        self,
        margin_call: float,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        collateral_coin: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanCustomizeMarginCallResponse:
        """Customize margin call for ongoing orders only.

        Weight(UID): 6000

        Args:
            margin_call: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Mandatory when collateralCoin is empty. Send either orderId or collateralCoin, if both parameters
                are sent, take orderId only.
            collateral_coin: Coin used as collateral
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Collateral Assets Data

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.crypto_loan_customize_margin_call_trade(
                margin_call,
                timestamp,
                signature,
                order_id=order_id,
                collateral_coin=collateral_coin,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def crypto_loan_repay_trade(
        self,
        order_id: int,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        type_: int | None = None,
        collateral_return: bool | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanRepayResponse:
        """Weight(UID): 6000

        Args:
            order_id: Order ID
            amount: Repayment Amount
            timestamp: UTC timestamp in ms
            signature: Signature
            type_: Default: 1. 1 for 'repay with borrowed coin'; 2 for 'repay with collateral'.
            collateral_return: Default: TRUE. TRUE: Return extra collateral to spot account; FALSE: Keep extra
                collateral in the order.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Repayment Information

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.crypto_loan_repay_trade(
                order_id,
                amount,
                timestamp,
                signature,
                type_=type_,
                collateral_return=collateral_return,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def get_collateral_assets_data_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        collateral_coin: str | None = None,
        vip_level: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanCollateralDataResponse:
        """Get LTV information and collateral limit of collateral assets. The collateral limit is shown in USD value.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            collateral_coin: Coin used as collateral
            vip_level: Defaults to user's vip level
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Collateral Assets Data

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_collateral_assets_data_user_data(
                timestamp,
                signature,
                collateral_coin=collateral_coin,
                vip_level=vip_level,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def get_crypto_loans_borrow_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanBorrowHistoryResponse:
        """- If startTime and endTime are not sent, the recent 90-day data will be returned.
        - The max interval between startTime and endTime is 180 days.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: orderId in POST /sapi/v1/loan/borrow
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            limit: default 10, max 100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Borrow History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_crypto_loans_borrow_history_user_data(
                timestamp,
                signature,
                order_id=order_id,
                loan_coin=loan_coin,
                collateral_coin=collateral_coin,
                start_time=start_time,
                end_time=end_time,
                current=current,
                limit=limit,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def get_crypto_loans_income_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        type_: Type9OrStr | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1LoanIncomeResponse]:
        """- If startTime and endTime are not sent, the recent 7-day data will be returned.
        - The max interval between startTime and endTime is 30 days.

        Weight(UID): 6000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            type_: All types will be returned by default. * ``borrowIn`` * ``collateralSpent`` * ``repayAmount`` *
                ``collateralReturn`` - Collateral return after repayment * ``addCollateral`` * ``removeCollateral`` *
                ``collateralReturnAfterLiquidation``
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: default 20, max 100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Loan History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_crypto_loans_income_history_user_data(
                timestamp,
                signature,
                asset=asset,
                type_=type_,
                start_time=start_time,
                end_time=end_time,
                limit=limit,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def get_flexible_loan_assets_data_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV2LoanFlexibleLoanableDataResponse:
        """Get interest rate and borrow limit of flexible loanable assets. The borrow limit is shown in USD value.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Loan asset data

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_flexible_loan_assets_data_user_data(
                timestamp, signature, loan_coin=loan_coin, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def get_flexible_loan_collateral_assets_data_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        collateral_coin: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV2LoanFlexibleCollateralDataResponse:
        """Get LTV information and collateral limit of flexible loan's collateral assets. The collateral limit is shown
        in USD value.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            collateral_coin: Coin used as collateral
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Loan asset data

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_flexible_loan_collateral_assets_data_user_data(
                timestamp,
                signature,
                collateral_coin=collateral_coin,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def get_loan_ltv_adjustment_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanLtvAdjustmentHistoryResponse:
        """If startTime and endTime are not sent, the recent 90-day data will be returned. The max interval between
        startTime and endTime is 180 days.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order ID
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            limit: default 10, max 100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            LTV Adjustment History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_loan_ltv_adjustment_history_user_data(
                timestamp,
                signature,
                order_id=order_id,
                loan_coin=loan_coin,
                collateral_coin=collateral_coin,
                start_time=start_time,
                end_time=end_time,
                current=current,
                limit=limit,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def get_loan_ongoing_orders_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanOngoingOrdersResponse:
        """Weight(IP): 300

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: orderId in POST /sapi/v1/loan/borrow
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            current: Current querying page. Start from 1; default:1, max:1000
            limit: default 10, max 100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Ongoing Orders

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_loan_ongoing_orders_user_data(
                timestamp,
                signature,
                order_id=order_id,
                loan_coin=loan_coin,
                collateral_coin=collateral_coin,
                current=current,
                limit=limit,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def get_loan_repayment_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanRepayHistoryResponse:
        """If startTime and endTime are not sent, the recent 90-day data will be returned. The max interval between
        startTime and endTime is 180 days.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order ID
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            limit: default 10, max 100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Loan Repayment History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_loan_repayment_history_user_data(
                timestamp,
                signature,
                order_id=order_id,
                loan_coin=loan_coin,
                collateral_coin=collateral_coin,
                start_time=start_time,
                end_time=end_time,
                current=current,
                limit=limit,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def get_loanable_assets_data_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        vip_level: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LoanLoanableDataResponse:
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
            await self._with_raw_response.get_loanable_assets_data_user_data(
                timestamp,
                signature,
                loan_coin=loan_coin,
                vip_level=vip_level,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def repay_flexible_loan_repay_trade(
        self,
        repay_amount: float,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        collateral_return: bool | None = None,
        full_repayment: bool | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV2LoanFlexibleRepayResponse:
        """- repayAmount is mandatory even fullRepayment = FALSE

        Weight(IP): 6000

        Args:
            repay_amount: repay amount of loanCoin
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            collateral_return: Default: TRUE. TRUE: Return extra collateral to earn account; FALSE: Keep extra
                collateral in the order, and lower LTV.
            full_repayment: Default: FALSE. TRUE: Full repayment; FALSE: Partial repayment, based on loanAmount
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Loan repay

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.repay_flexible_loan_repay_trade(
                repay_amount,
                timestamp,
                signature,
                loan_coin=loan_coin,
                collateral_coin=collateral_coin,
                collateral_return=collateral_return,
                full_repayment=full_repayment,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def repay_get_flexible_loan_repayment_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV2LoanFlexibleRepayHistoryResponse:
        """- If startTime and endTime are not sent, the recent 90-day data will be returned.
        - The max interval between startTime and endTime is 180 days.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Loan repay history

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.repay_get_flexible_loan_repayment_history_user_data(
                timestamp,
                signature,
                loan_coin=loan_coin,
                collateral_coin=collateral_coin,
                start_time=start_time,
                end_time=end_time,
                current=current,
                limit=limit,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncCryptoLoansWithRawResponse:
        return self._with_raw_response


class CryptoLoansWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def adjust_ltv_flexible_loan_adjust_ltv_trade(
        self,
        adjustment_amount: float,
        direction: DirectionOrStr,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV2LoanFlexibleAdjustLtvResponse, AdjustLtvFlexibleLoanAdjustLtvTradeErrorBody]:
        """- API Key needs Spot & Margin Trading permission for this endpoint

        Weight(UID): 6000

        Args:
            adjustment_amount: Value sent with the request.
            direction: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v2/loan/flexible/adjust/ltv"),
            query_params=[
                param[float]("adjustmentAmount", adjustment_amount),
                param[DirectionOrStr]("direction", direction),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("loanCoin", loan_coin),
                param[str | None]("collateralCoin", collateral_coin),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV2LoanFlexibleAdjustLtvResponse],
            error_mapper=adjust_ltv_flexible_loan_adjust_ltv_trade_error_mapper,
            request_options=request_options,
        )

    def adjust_ltv_get_flexible_loan_ltv_adjustment_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV2LoanFlexibleLtvAdjustmentHistoryResponse, AdjustLtvGetFlexibleLoanLtvAdjustmentHistoryUserDataErrorBody
    ]:
        """- If startTime and endTime are not sent, the recent 90-day data will be returned.
        - The max interval between startTime and endTime is 180 days.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v2/loan/flexible/ltv/adjustment/history"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("loanCoin", loan_coin),
                param[str | None]("collateralCoin", collateral_coin),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV2LoanFlexibleLtvAdjustmentHistoryResponse],
            error_mapper=adjust_ltv_get_flexible_loan_ltv_adjustment_history_user_data_error_mapper,
            request_options=request_options,
        )

    def borrow_flexible_loan_borrow_trade(
        self,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        loan_amount: float | None = None,
        collateral_coin: str | None = None,
        collateral_amount: float | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV2LoanFlexibleBorrowResponse, BorrowFlexibleLoanBorrowTradeErrorBody]:
        """- Only available for master account

        Weight(UID): 6000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            loan_amount: Loan amount
            collateral_coin: Coin used as collateral
            collateral_amount: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v2/loan/flexible/borrow"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("loanCoin", loan_coin),
                param[float | None]("loanAmount", loan_amount),
                param[str | None]("collateralCoin", collateral_coin),
                param[float | None]("collateralAmount", collateral_amount),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV2LoanFlexibleBorrowResponse],
            error_mapper=borrow_flexible_loan_borrow_trade_error_mapper,
            request_options=request_options,
        )

    def borrow_get_flexible_loan_borrow_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV2LoanFlexibleBorrowHistoryResponse, BorrowGetFlexibleLoanBorrowHistoryUserDataErrorBody]:
        """- If startTime and endTime are not sent, the recent 90-day data will be returned.
        - The max interval between startTime and endTime is 180 days.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v2/loan/flexible/borrow/history"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("loanCoin", loan_coin),
                param[str | None]("collateralCoin", collateral_coin),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV2LoanFlexibleBorrowHistoryResponse],
            error_mapper=borrow_get_flexible_loan_borrow_history_user_data_error_mapper,
            request_options=request_options,
        )

    def borrow_get_flexible_loan_ongoing_orders_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV2LoanFlexibleOngoingOrdersResponse, BorrowGetFlexibleLoanOngoingOrdersUserDataErrorBody]:
        """Weight(IP): 300

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            current: Current querying page. Start from 1. Default:1
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v2/loan/flexible/ongoing/orders"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("loanCoin", loan_coin),
                param[str | None]("collateralCoin", collateral_coin),
                param[int | None]("current", current),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV2LoanFlexibleOngoingOrdersResponse],
            error_mapper=borrow_get_flexible_loan_ongoing_orders_user_data_error_mapper,
            request_options=request_options,
        )

    def check_collateral_repay_rate_user_data(
        self,
        loan_coin: str,
        collateral_coin: str,
        repay_amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanRepayCollateralRateResponse, CheckCollateralRepayRateUserDataErrorBody]:
        """Get the the rate of collateral coin / loan coin when using collateral repay, the rate will be valid within 8
        second.

        Weight(IP): 6000

        Args:
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            repay_amount: repay amount of loanCoin
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/loan/repay/collateral/rate"),
            query_params=[
                param[str]("loanCoin", loan_coin),
                param[str]("collateralCoin", collateral_coin),
                param[float]("repayAmount", repay_amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanRepayCollateralRateResponse],
            error_mapper=check_collateral_repay_rate_user_data_error_mapper,
            request_options=request_options,
        )

    def crypto_loan_adjust_ltv_trade(
        self,
        order_id: int,
        amount: float,
        direction: DirectionOrStr,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanAdjustLtvResponse, CryptoLoanAdjustLtvTradeErrorBody]:
        """Weight(UID): 6000

        Args:
            order_id: Order ID
            amount: Amount
            direction: 'ADDITIONAL', 'REDUCED'
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/loan/adjust/ltv"),
            query_params=[
                param[int]("orderId", order_id),
                param[float]("amount", amount),
                param[DirectionOrStr]("direction", direction),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanAdjustLtvResponse],
            error_mapper=crypto_loan_adjust_ltv_trade_error_mapper,
            request_options=request_options,
        )

    def crypto_loan_borrow_trade(
        self,
        loan_coin: str,
        collateral_coin: str,
        loan_term: int,
        timestamp: int,
        signature: str,
        *,
        loan_amount: float | None = None,
        collateral_amount: float | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanBorrowResponse, CryptoLoanBorrowTradeErrorBody]:
        """Weight(UID): 6000

        Args:
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            loan_term: 7/14/30/90/180 days
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_amount: Loan amount
            collateral_amount: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/loan/borrow"),
            query_params=[
                param[str]("loanCoin", loan_coin),
                param[str]("collateralCoin", collateral_coin),
                param[int]("loanTerm", loan_term),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[float | None]("loanAmount", loan_amount),
                param[float | None]("collateralAmount", collateral_amount),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanBorrowResponse],
            error_mapper=crypto_loan_borrow_trade_error_mapper,
            request_options=request_options,
        )

    def crypto_loan_customize_margin_call_trade(
        self,
        margin_call: float,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        collateral_coin: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanCustomizeMarginCallResponse, CryptoLoanCustomizeMarginCallTradeErrorBody]:
        """Customize margin call for ongoing orders only.

        Weight(UID): 6000

        Args:
            margin_call: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Mandatory when collateralCoin is empty. Send either orderId or collateralCoin, if both parameters
                are sent, take orderId only.
            collateral_coin: Coin used as collateral
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/loan/customize/margin_call"),
            query_params=[
                param[float]("marginCall", margin_call),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("orderId", order_id),
                param[str | None]("collateralCoin", collateral_coin),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanCustomizeMarginCallResponse],
            error_mapper=crypto_loan_customize_margin_call_trade_error_mapper,
            request_options=request_options,
        )

    def crypto_loan_repay_trade(
        self,
        order_id: int,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        type_: int | None = None,
        collateral_return: bool | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanRepayResponse, CryptoLoanRepayTradeErrorBody]:
        """Weight(UID): 6000

        Args:
            order_id: Order ID
            amount: Repayment Amount
            timestamp: UTC timestamp in ms
            signature: Signature
            type_: Default: 1. 1 for 'repay with borrowed coin'; 2 for 'repay with collateral'.
            collateral_return: Default: TRUE. TRUE: Return extra collateral to spot account; FALSE: Keep extra
                collateral in the order.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/loan/repay"),
            query_params=[
                param[int]("orderId", order_id),
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("type", type_),
                param[bool | None]("collateralReturn", collateral_return),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanRepayResponse],
            error_mapper=crypto_loan_repay_trade_error_mapper,
            request_options=request_options,
        )

    def get_collateral_assets_data_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        collateral_coin: str | None = None,
        vip_level: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanCollateralDataResponse, GetCollateralAssetsDataUserDataErrorBody]:
        """Get LTV information and collateral limit of collateral assets. The collateral limit is shown in USD value.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            collateral_coin: Coin used as collateral
            vip_level: Defaults to user's vip level
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/loan/collateral/data"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("collateralCoin", collateral_coin),
                param[int | None]("vipLevel", vip_level),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanCollateralDataResponse],
            error_mapper=get_collateral_assets_data_user_data_error_mapper,
            request_options=request_options,
        )

    def get_crypto_loans_borrow_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanBorrowHistoryResponse, GetCryptoLoansBorrowHistoryUserDataErrorBody]:
        """- If startTime and endTime are not sent, the recent 90-day data will be returned.
        - The max interval between startTime and endTime is 180 days.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: orderId in POST /sapi/v1/loan/borrow
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            limit: default 10, max 100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/loan/borrow/history"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("orderId", order_id),
                param[str | None]("loanCoin", loan_coin),
                param[str | None]("collateralCoin", collateral_coin),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanBorrowHistoryResponse],
            error_mapper=get_crypto_loans_borrow_history_user_data_error_mapper,
            request_options=request_options,
        )

    def get_crypto_loans_income_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        type_: Type9OrStr | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1LoanIncomeResponse], GetCryptoLoansIncomeHistoryUserDataErrorBody]:
        """- If startTime and endTime are not sent, the recent 7-day data will be returned.
        - The max interval between startTime and endTime is 30 days.

        Weight(UID): 6000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            type_: All types will be returned by default. * ``borrowIn`` * ``collateralSpent`` * ``repayAmount`` *
                ``collateralReturn`` - Collateral return after repayment * ``addCollateral`` * ``removeCollateral`` *
                ``collateralReturnAfterLiquidation``
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: default 20, max 100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/loan/income"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("asset", asset),
                param[Type9OrStr | None]("type", type_),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1LoanIncomeResponse]],
            error_mapper=get_crypto_loans_income_history_user_data_error_mapper,
            request_options=request_options,
        )

    def get_flexible_loan_assets_data_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV2LoanFlexibleLoanableDataResponse, GetFlexibleLoanAssetsDataUserDataErrorBody]:
        """Get interest rate and borrow limit of flexible loanable assets. The borrow limit is shown in USD value.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v2/loan/flexible/loanable/data"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("loanCoin", loan_coin),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV2LoanFlexibleLoanableDataResponse],
            error_mapper=get_flexible_loan_assets_data_user_data_error_mapper,
            request_options=request_options,
        )

    def get_flexible_loan_collateral_assets_data_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        collateral_coin: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV2LoanFlexibleCollateralDataResponse, GetFlexibleLoanCollateralAssetsDataUserDataErrorBody]:
        """Get LTV information and collateral limit of flexible loan's collateral assets. The collateral limit is shown
        in USD value.

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
            url_template=self._server.default("/sapi/v2/loan/flexible/collateral/data"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("collateralCoin", collateral_coin),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV2LoanFlexibleCollateralDataResponse],
            error_mapper=get_flexible_loan_collateral_assets_data_user_data_error_mapper,
            request_options=request_options,
        )

    def get_loan_ltv_adjustment_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanLtvAdjustmentHistoryResponse, GetLoanLtvAdjustmentHistoryUserDataErrorBody]:
        """If startTime and endTime are not sent, the recent 90-day data will be returned. The max interval between
        startTime and endTime is 180 days.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order ID
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            limit: default 10, max 100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/loan/ltv/adjustment/history"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("orderId", order_id),
                param[str | None]("loanCoin", loan_coin),
                param[str | None]("collateralCoin", collateral_coin),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanLtvAdjustmentHistoryResponse],
            error_mapper=get_loan_ltv_adjustment_history_user_data_error_mapper,
            request_options=request_options,
        )

    def get_loan_ongoing_orders_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanOngoingOrdersResponse, GetLoanOngoingOrdersUserDataErrorBody]:
        """Weight(IP): 300

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: orderId in POST /sapi/v1/loan/borrow
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            current: Current querying page. Start from 1; default:1, max:1000
            limit: default 10, max 100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/loan/ongoing/orders"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("orderId", order_id),
                param[str | None]("loanCoin", loan_coin),
                param[str | None]("collateralCoin", collateral_coin),
                param[int | None]("current", current),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanOngoingOrdersResponse],
            error_mapper=get_loan_ongoing_orders_user_data_error_mapper,
            request_options=request_options,
        )

    def get_loan_repayment_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanRepayHistoryResponse, GetLoanRepaymentHistoryUserDataErrorBody]:
        """If startTime and endTime are not sent, the recent 90-day data will be returned. The max interval between
        startTime and endTime is 180 days.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order ID
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            limit: default 10, max 100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/loan/repay/history"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("orderId", order_id),
                param[str | None]("loanCoin", loan_coin),
                param[str | None]("collateralCoin", collateral_coin),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanRepayHistoryResponse],
            error_mapper=get_loan_repayment_history_user_data_error_mapper,
            request_options=request_options,
        )

    def get_loanable_assets_data_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        vip_level: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanLoanableDataResponse, GetLoanableAssetsDataUserDataErrorBody]:
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
            url_template=self._server.default("/sapi/v1/loan/loanable/data"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("loanCoin", loan_coin),
                param[int | None]("vipLevel", vip_level),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanLoanableDataResponse],
            error_mapper=get_loanable_assets_data_user_data_error_mapper,
            request_options=request_options,
        )

    def repay_flexible_loan_repay_trade(
        self,
        repay_amount: float,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        collateral_return: bool | None = None,
        full_repayment: bool | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV2LoanFlexibleRepayResponse, RepayFlexibleLoanRepayTradeErrorBody]:
        """- repayAmount is mandatory even fullRepayment = FALSE

        Weight(IP): 6000

        Args:
            repay_amount: repay amount of loanCoin
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            collateral_return: Default: TRUE. TRUE: Return extra collateral to earn account; FALSE: Keep extra
                collateral in the order, and lower LTV.
            full_repayment: Default: FALSE. TRUE: Full repayment; FALSE: Partial repayment, based on loanAmount
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v2/loan/flexible/repay"),
            query_params=[
                param[float]("repayAmount", repay_amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("loanCoin", loan_coin),
                param[str | None]("collateralCoin", collateral_coin),
                param[bool | None]("collateralReturn", collateral_return),
                param[bool | None]("fullRepayment", full_repayment),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV2LoanFlexibleRepayResponse],
            error_mapper=repay_flexible_loan_repay_trade_error_mapper,
            request_options=request_options,
        )

    def repay_get_flexible_loan_repayment_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV2LoanFlexibleRepayHistoryResponse, RepayGetFlexibleLoanRepaymentHistoryUserDataErrorBody]:
        """- If startTime and endTime are not sent, the recent 90-day data will be returned.
        - The max interval between startTime and endTime is 180 days.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v2/loan/flexible/repay/history"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("loanCoin", loan_coin),
                param[str | None]("collateralCoin", collateral_coin),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV2LoanFlexibleRepayHistoryResponse],
            error_mapper=repay_get_flexible_loan_repayment_history_user_data_error_mapper,
            request_options=request_options,
        )


class AsyncCryptoLoansWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def adjust_ltv_flexible_loan_adjust_ltv_trade(
        self,
        adjustment_amount: float,
        direction: DirectionOrStr,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV2LoanFlexibleAdjustLtvResponse, AdjustLtvFlexibleLoanAdjustLtvTradeErrorBody]:
        """- API Key needs Spot & Margin Trading permission for this endpoint

        Weight(UID): 6000

        Args:
            adjustment_amount: Value sent with the request.
            direction: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v2/loan/flexible/adjust/ltv"),
            query_params=[
                param[float]("adjustmentAmount", adjustment_amount),
                param[DirectionOrStr]("direction", direction),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("loanCoin", loan_coin),
                param[str | None]("collateralCoin", collateral_coin),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV2LoanFlexibleAdjustLtvResponse],
            error_mapper=adjust_ltv_flexible_loan_adjust_ltv_trade_error_mapper,
            request_options=request_options,
        )

    async def adjust_ltv_get_flexible_loan_ltv_adjustment_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV2LoanFlexibleLtvAdjustmentHistoryResponse, AdjustLtvGetFlexibleLoanLtvAdjustmentHistoryUserDataErrorBody
    ]:
        """- If startTime and endTime are not sent, the recent 90-day data will be returned.
        - The max interval between startTime and endTime is 180 days.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v2/loan/flexible/ltv/adjustment/history"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("loanCoin", loan_coin),
                param[str | None]("collateralCoin", collateral_coin),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV2LoanFlexibleLtvAdjustmentHistoryResponse],
            error_mapper=adjust_ltv_get_flexible_loan_ltv_adjustment_history_user_data_error_mapper,
            request_options=request_options,
        )

    async def borrow_flexible_loan_borrow_trade(
        self,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        loan_amount: float | None = None,
        collateral_coin: str | None = None,
        collateral_amount: float | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV2LoanFlexibleBorrowResponse, BorrowFlexibleLoanBorrowTradeErrorBody]:
        """- Only available for master account

        Weight(UID): 6000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            loan_amount: Loan amount
            collateral_coin: Coin used as collateral
            collateral_amount: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v2/loan/flexible/borrow"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("loanCoin", loan_coin),
                param[float | None]("loanAmount", loan_amount),
                param[str | None]("collateralCoin", collateral_coin),
                param[float | None]("collateralAmount", collateral_amount),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV2LoanFlexibleBorrowResponse],
            error_mapper=borrow_flexible_loan_borrow_trade_error_mapper,
            request_options=request_options,
        )

    async def borrow_get_flexible_loan_borrow_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV2LoanFlexibleBorrowHistoryResponse, BorrowGetFlexibleLoanBorrowHistoryUserDataErrorBody]:
        """- If startTime and endTime are not sent, the recent 90-day data will be returned.
        - The max interval between startTime and endTime is 180 days.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v2/loan/flexible/borrow/history"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("loanCoin", loan_coin),
                param[str | None]("collateralCoin", collateral_coin),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV2LoanFlexibleBorrowHistoryResponse],
            error_mapper=borrow_get_flexible_loan_borrow_history_user_data_error_mapper,
            request_options=request_options,
        )

    async def borrow_get_flexible_loan_ongoing_orders_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV2LoanFlexibleOngoingOrdersResponse, BorrowGetFlexibleLoanOngoingOrdersUserDataErrorBody]:
        """Weight(IP): 300

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            current: Current querying page. Start from 1. Default:1
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v2/loan/flexible/ongoing/orders"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("loanCoin", loan_coin),
                param[str | None]("collateralCoin", collateral_coin),
                param[int | None]("current", current),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV2LoanFlexibleOngoingOrdersResponse],
            error_mapper=borrow_get_flexible_loan_ongoing_orders_user_data_error_mapper,
            request_options=request_options,
        )

    async def check_collateral_repay_rate_user_data(
        self,
        loan_coin: str,
        collateral_coin: str,
        repay_amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanRepayCollateralRateResponse, CheckCollateralRepayRateUserDataErrorBody]:
        """Get the the rate of collateral coin / loan coin when using collateral repay, the rate will be valid within 8
        second.

        Weight(IP): 6000

        Args:
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            repay_amount: repay amount of loanCoin
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/loan/repay/collateral/rate"),
            query_params=[
                param[str]("loanCoin", loan_coin),
                param[str]("collateralCoin", collateral_coin),
                param[float]("repayAmount", repay_amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanRepayCollateralRateResponse],
            error_mapper=check_collateral_repay_rate_user_data_error_mapper,
            request_options=request_options,
        )

    async def crypto_loan_adjust_ltv_trade(
        self,
        order_id: int,
        amount: float,
        direction: DirectionOrStr,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanAdjustLtvResponse, CryptoLoanAdjustLtvTradeErrorBody]:
        """Weight(UID): 6000

        Args:
            order_id: Order ID
            amount: Amount
            direction: 'ADDITIONAL', 'REDUCED'
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/loan/adjust/ltv"),
            query_params=[
                param[int]("orderId", order_id),
                param[float]("amount", amount),
                param[DirectionOrStr]("direction", direction),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanAdjustLtvResponse],
            error_mapper=crypto_loan_adjust_ltv_trade_error_mapper,
            request_options=request_options,
        )

    async def crypto_loan_borrow_trade(
        self,
        loan_coin: str,
        collateral_coin: str,
        loan_term: int,
        timestamp: int,
        signature: str,
        *,
        loan_amount: float | None = None,
        collateral_amount: float | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanBorrowResponse, CryptoLoanBorrowTradeErrorBody]:
        """Weight(UID): 6000

        Args:
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            loan_term: 7/14/30/90/180 days
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_amount: Loan amount
            collateral_amount: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/loan/borrow"),
            query_params=[
                param[str]("loanCoin", loan_coin),
                param[str]("collateralCoin", collateral_coin),
                param[int]("loanTerm", loan_term),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[float | None]("loanAmount", loan_amount),
                param[float | None]("collateralAmount", collateral_amount),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanBorrowResponse],
            error_mapper=crypto_loan_borrow_trade_error_mapper,
            request_options=request_options,
        )

    async def crypto_loan_customize_margin_call_trade(
        self,
        margin_call: float,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        collateral_coin: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanCustomizeMarginCallResponse, CryptoLoanCustomizeMarginCallTradeErrorBody]:
        """Customize margin call for ongoing orders only.

        Weight(UID): 6000

        Args:
            margin_call: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Mandatory when collateralCoin is empty. Send either orderId or collateralCoin, if both parameters
                are sent, take orderId only.
            collateral_coin: Coin used as collateral
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/loan/customize/margin_call"),
            query_params=[
                param[float]("marginCall", margin_call),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("orderId", order_id),
                param[str | None]("collateralCoin", collateral_coin),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanCustomizeMarginCallResponse],
            error_mapper=crypto_loan_customize_margin_call_trade_error_mapper,
            request_options=request_options,
        )

    async def crypto_loan_repay_trade(
        self,
        order_id: int,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        type_: int | None = None,
        collateral_return: bool | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanRepayResponse, CryptoLoanRepayTradeErrorBody]:
        """Weight(UID): 6000

        Args:
            order_id: Order ID
            amount: Repayment Amount
            timestamp: UTC timestamp in ms
            signature: Signature
            type_: Default: 1. 1 for 'repay with borrowed coin'; 2 for 'repay with collateral'.
            collateral_return: Default: TRUE. TRUE: Return extra collateral to spot account; FALSE: Keep extra
                collateral in the order.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/loan/repay"),
            query_params=[
                param[int]("orderId", order_id),
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("type", type_),
                param[bool | None]("collateralReturn", collateral_return),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanRepayResponse],
            error_mapper=crypto_loan_repay_trade_error_mapper,
            request_options=request_options,
        )

    async def get_collateral_assets_data_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        collateral_coin: str | None = None,
        vip_level: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanCollateralDataResponse, GetCollateralAssetsDataUserDataErrorBody]:
        """Get LTV information and collateral limit of collateral assets. The collateral limit is shown in USD value.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            collateral_coin: Coin used as collateral
            vip_level: Defaults to user's vip level
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/loan/collateral/data"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("collateralCoin", collateral_coin),
                param[int | None]("vipLevel", vip_level),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanCollateralDataResponse],
            error_mapper=get_collateral_assets_data_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_crypto_loans_borrow_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanBorrowHistoryResponse, GetCryptoLoansBorrowHistoryUserDataErrorBody]:
        """- If startTime and endTime are not sent, the recent 90-day data will be returned.
        - The max interval between startTime and endTime is 180 days.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: orderId in POST /sapi/v1/loan/borrow
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            limit: default 10, max 100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/loan/borrow/history"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("orderId", order_id),
                param[str | None]("loanCoin", loan_coin),
                param[str | None]("collateralCoin", collateral_coin),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanBorrowHistoryResponse],
            error_mapper=get_crypto_loans_borrow_history_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_crypto_loans_income_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        type_: Type9OrStr | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1LoanIncomeResponse], GetCryptoLoansIncomeHistoryUserDataErrorBody]:
        """- If startTime and endTime are not sent, the recent 7-day data will be returned.
        - The max interval between startTime and endTime is 30 days.

        Weight(UID): 6000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            type_: All types will be returned by default. * ``borrowIn`` * ``collateralSpent`` * ``repayAmount`` *
                ``collateralReturn`` - Collateral return after repayment * ``addCollateral`` * ``removeCollateral`` *
                ``collateralReturnAfterLiquidation``
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: default 20, max 100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/loan/income"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("asset", asset),
                param[Type9OrStr | None]("type", type_),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1LoanIncomeResponse]],
            error_mapper=get_crypto_loans_income_history_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_flexible_loan_assets_data_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV2LoanFlexibleLoanableDataResponse, GetFlexibleLoanAssetsDataUserDataErrorBody]:
        """Get interest rate and borrow limit of flexible loanable assets. The borrow limit is shown in USD value.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v2/loan/flexible/loanable/data"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("loanCoin", loan_coin),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV2LoanFlexibleLoanableDataResponse],
            error_mapper=get_flexible_loan_assets_data_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_flexible_loan_collateral_assets_data_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        collateral_coin: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV2LoanFlexibleCollateralDataResponse, GetFlexibleLoanCollateralAssetsDataUserDataErrorBody]:
        """Get LTV information and collateral limit of flexible loan's collateral assets. The collateral limit is shown
        in USD value.

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
            url_template=self._server.default("/sapi/v2/loan/flexible/collateral/data"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("collateralCoin", collateral_coin),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV2LoanFlexibleCollateralDataResponse],
            error_mapper=get_flexible_loan_collateral_assets_data_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_loan_ltv_adjustment_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanLtvAdjustmentHistoryResponse, GetLoanLtvAdjustmentHistoryUserDataErrorBody]:
        """If startTime and endTime are not sent, the recent 90-day data will be returned. The max interval between
        startTime and endTime is 180 days.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order ID
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            limit: default 10, max 100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/loan/ltv/adjustment/history"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("orderId", order_id),
                param[str | None]("loanCoin", loan_coin),
                param[str | None]("collateralCoin", collateral_coin),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanLtvAdjustmentHistoryResponse],
            error_mapper=get_loan_ltv_adjustment_history_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_loan_ongoing_orders_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanOngoingOrdersResponse, GetLoanOngoingOrdersUserDataErrorBody]:
        """Weight(IP): 300

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: orderId in POST /sapi/v1/loan/borrow
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            current: Current querying page. Start from 1; default:1, max:1000
            limit: default 10, max 100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/loan/ongoing/orders"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("orderId", order_id),
                param[str | None]("loanCoin", loan_coin),
                param[str | None]("collateralCoin", collateral_coin),
                param[int | None]("current", current),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanOngoingOrdersResponse],
            error_mapper=get_loan_ongoing_orders_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_loan_repayment_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        order_id: int | None = None,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanRepayHistoryResponse, GetLoanRepaymentHistoryUserDataErrorBody]:
        """If startTime and endTime are not sent, the recent 90-day data will be returned. The max interval between
        startTime and endTime is 180 days.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            order_id: Order ID
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            limit: default 10, max 100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/loan/repay/history"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("orderId", order_id),
                param[str | None]("loanCoin", loan_coin),
                param[str | None]("collateralCoin", collateral_coin),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanRepayHistoryResponse],
            error_mapper=get_loan_repayment_history_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_loanable_assets_data_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        vip_level: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LoanLoanableDataResponse, GetLoanableAssetsDataUserDataErrorBody]:
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
            url_template=self._server.default("/sapi/v1/loan/loanable/data"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("loanCoin", loan_coin),
                param[int | None]("vipLevel", vip_level),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LoanLoanableDataResponse],
            error_mapper=get_loanable_assets_data_user_data_error_mapper,
            request_options=request_options,
        )

    async def repay_flexible_loan_repay_trade(
        self,
        repay_amount: float,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        collateral_return: bool | None = None,
        full_repayment: bool | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV2LoanFlexibleRepayResponse, RepayFlexibleLoanRepayTradeErrorBody]:
        """- repayAmount is mandatory even fullRepayment = FALSE

        Weight(IP): 6000

        Args:
            repay_amount: repay amount of loanCoin
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            collateral_return: Default: TRUE. TRUE: Return extra collateral to earn account; FALSE: Keep extra
                collateral in the order, and lower LTV.
            full_repayment: Default: FALSE. TRUE: Full repayment; FALSE: Partial repayment, based on loanAmount
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v2/loan/flexible/repay"),
            query_params=[
                param[float]("repayAmount", repay_amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("loanCoin", loan_coin),
                param[str | None]("collateralCoin", collateral_coin),
                param[bool | None]("collateralReturn", collateral_return),
                param[bool | None]("fullRepayment", full_repayment),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV2LoanFlexibleRepayResponse],
            error_mapper=repay_flexible_loan_repay_trade_error_mapper,
            request_options=request_options,
        )

    async def repay_get_flexible_loan_repayment_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        loan_coin: str | None = None,
        collateral_coin: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV2LoanFlexibleRepayHistoryResponse, RepayGetFlexibleLoanRepaymentHistoryUserDataErrorBody]:
        """- If startTime and endTime are not sent, the recent 90-day data will be returned.
        - The max interval between startTime and endTime is 180 days.

        Weight(IP): 400

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            loan_coin: Coin loaned
            collateral_coin: Coin used as collateral
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v2/loan/flexible/repay/history"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("loanCoin", loan_coin),
                param[str | None]("collateralCoin", collateral_coin),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV2LoanFlexibleRepayHistoryResponse],
            error_mapper=repay_get_flexible_loan_repayment_history_user_data_error_mapper,
            request_options=request_options,
        )
