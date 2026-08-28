from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder, param
from ..errors.change_plan_status_error import ChangePlanStatusErrorBody, change_plan_status_error_mapper
from ..errors.get_list_of_plans_error import GetListOfPlansErrorBody, get_list_of_plans_error_mapper
from ..errors.get_target_asset_list_user_data_error import (
    GetTargetAssetListUserDataErrorBody,
    get_target_asset_list_user_data_error_mapper,
)
from ..errors.get_target_asset_roi_data_user_data_error import (
    GetTargetAssetRoiDataUserDataErrorBody,
    get_target_asset_roi_data_user_data_error_mapper,
)
from ..errors.index_linked_plan_rebalance_details_user_data_error import (
    IndexLinkedPlanRebalanceDetailsUserDataErrorBody,
    index_linked_plan_rebalance_details_user_data_error_mapper,
)
from ..errors.index_linked_plan_redemption_history_user_data_error import (
    IndexLinkedPlanRedemptionHistoryUserDataErrorBody,
    index_linked_plan_redemption_history_user_data_error_mapper,
)
from ..errors.index_linked_plan_redemption_trade_error import (
    IndexLinkedPlanRedemptionTradeErrorBody,
    index_linked_plan_redemption_trade_error_mapper,
)
from ..errors.investment_plan_adjustment_error import (
    InvestmentPlanAdjustmentErrorBody,
    investment_plan_adjustment_error_mapper,
)
from ..errors.investment_plan_creation_user_data_error import (
    InvestmentPlanCreationUserDataErrorBody,
    investment_plan_creation_user_data_error_mapper,
)
from ..errors.one_time_transaction_trade_error import (
    OneTimeTransactionTradeErrorBody,
    one_time_transaction_trade_error_mapper,
)
from ..errors.query_all_source_asset_and_target_asset_user_data_error import (
    QueryAllSourceAssetAndTargetAssetUserDataErrorBody,
    query_all_source_asset_and_target_asset_user_data_error_mapper,
)
from ..errors.query_holding_details_of_the_plan_error import (
    QueryHoldingDetailsOfThePlanErrorBody,
    query_holding_details_of_the_plan_error_mapper,
)
from ..errors.query_index_details_user_data_error import (
    QueryIndexDetailsUserDataErrorBody,
    query_index_details_user_data_error_mapper,
)
from ..errors.query_index_linked_plan_position_details_user_data_error import (
    QueryIndexLinkedPlanPositionDetailsUserDataErrorBody,
    query_index_linked_plan_position_details_user_data_error_mapper,
)
from ..errors.query_one_time_transaction_status_user_data_error import (
    QueryOneTimeTransactionStatusUserDataErrorBody,
    query_one_time_transaction_status_user_data_error_mapper,
)
from ..errors.query_source_asset_list_user_data_error import (
    QuerySourceAssetListUserDataErrorBody,
    query_source_asset_list_user_data_error_mapper,
)
from ..errors.query_subscription_transaction_history_error import (
    QuerySubscriptionTransactionHistoryErrorBody,
    query_subscription_transaction_history_error_mapper,
)
from ..models.detail1 import Detail1, Detail1Dict
from ..models.detail5 import Detail5, Detail5Dict
from ..models.enums.plan_type import PlanTypeOrStr
from ..models.enums.plan_type1 import PlanType1OrStr
from ..models.enums.source_type import SourceTypeOrStr
from ..models.enums.status1 import Status1OrStr
from ..models.enums.subscription_cycle import SubscriptionCycleOrStr
from ..models.enums.subscription_start_weekday import SubscriptionStartWeekdayOrStr
from ..models.sapi_v1_lending_auto_invest_all_asset_response import SapiV1LendingAutoInvestAllAssetResponse
from ..models.sapi_v1_lending_auto_invest_history_list_response import SapiV1LendingAutoInvestHistoryListResponse
from ..models.sapi_v1_lending_auto_invest_index_info_response import SapiV1LendingAutoInvestIndexInfoResponse
from ..models.sapi_v1_lending_auto_invest_index_user_summary_response import (
    SapiV1LendingAutoInvestIndexUserSummaryResponse,
)
from ..models.sapi_v1_lending_auto_invest_one_off_response import SapiV1LendingAutoInvestOneOffResponse
from ..models.sapi_v1_lending_auto_invest_one_off_status_response import SapiV1LendingAutoInvestOneOffStatusResponse
from ..models.sapi_v1_lending_auto_invest_plan_add_response import SapiV1LendingAutoInvestPlanAddResponse
from ..models.sapi_v1_lending_auto_invest_plan_edit_response import SapiV1LendingAutoInvestPlanEditResponse
from ..models.sapi_v1_lending_auto_invest_plan_edit_status_response import SapiV1LendingAutoInvestPlanEditStatusResponse
from ..models.sapi_v1_lending_auto_invest_plan_id_response import SapiV1LendingAutoInvestPlanIdResponse
from ..models.sapi_v1_lending_auto_invest_plan_list_response import SapiV1LendingAutoInvestPlanListResponse
from ..models.sapi_v1_lending_auto_invest_rebalance_history_response import (
    SapiV1LendingAutoInvestRebalanceHistoryResponse,
)
from ..models.sapi_v1_lending_auto_invest_redeem_history_response import SapiV1LendingAutoInvestRedeemHistoryResponse
from ..models.sapi_v1_lending_auto_invest_redeem_response import SapiV1LendingAutoInvestRedeemResponse
from ..models.sapi_v1_lending_auto_invest_source_asset_list_response import (
    SapiV1LendingAutoInvestSourceAssetListResponse,
)
from ..models.sapi_v1_lending_auto_invest_target_asset_list_response import (
    SapiV1LendingAutoInvestTargetAssetListResponse,
)
from ..models.sapi_v1_lending_auto_invest_target_asset_roi_list_response import (
    SapiV1LendingAutoInvestTargetAssetRoiListResponse,
)
from ..server.server import Server


class AutoInvest:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AutoInvestWithRawResponse(client, server, auth)

    def change_plan_status(
        self,
        plan_id: int,
        status: Status1OrStr,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LendingAutoInvestPlanEditStatusResponse:
        """Change Plan Status

        Weight(IP): 1

        Args:
            plan_id: Value sent with the request.
            status: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Plan result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.change_plan_status(
            plan_id, status, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def get_list_of_plans(
        self,
        plan_type: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LendingAutoInvestPlanListResponse:
        """Query plan lists

        Weight(IP): 1

        Args:
            plan_type: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Plan result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_list_of_plans(
            plan_type, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def get_target_asset_roi_data_user_data(
        self,
        target_asset: str,
        his_roi_type: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1LendingAutoInvestTargetAssetRoiListResponse]:
        """ROI return list for target asset

        Weight(IP): 1

        Args:
            target_asset: Value sent with the request.
            his_roi_type: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Target asset list

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_target_asset_roi_data_user_data(
            target_asset, his_roi_type, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def get_target_asset_list_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        target_asset: str | None = None,
        size: int | None = None,
        current: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LendingAutoInvestTargetAssetListResponse:
        """Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            target_asset: Value sent with the request.
            size: Default:10 Max:100
            current: Current querying page. Start from 1. Default:1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Target asset list

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_target_asset_list_user_data(
            timestamp,
            signature,
            target_asset=target_asset,
            size=size,
            current=current,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def index_linked_plan_rebalance_details_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1LendingAutoInvestRebalanceHistoryResponse]:
        """Get the history of Index Linked Plan Redemption transactions

        Max 30 day difference between startTime and endTime If no startTime and endTime, default to show past 30 day
        records

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Rebalance Details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.index_linked_plan_rebalance_details_user_data(
            timestamp,
            signature,
            start_time=start_time,
            end_time=end_time,
            current=current,
            size=size,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def index_linked_plan_redemption_trade(
        self,
        index_id: int,
        redemption_percentage: int,
        timestamp: int,
        signature: str,
        *,
        request_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LendingAutoInvestRedeemResponse:
        """To redeem index-Linked plan holdings

        Weight(IP): 1

        Args:
            index_id: PORTFOLIO plan's Id
            redemption_percentage: user redeem percentage,10/20/100.
            timestamp: UTC timestamp in ms
            signature: Signature
            request_id: sourceType + unique, transactionId and requestId cannot be empty at the same time
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Redemption result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.index_linked_plan_redemption_trade(
            index_id,
            redemption_percentage,
            timestamp,
            signature,
            request_id=request_id,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def index_linked_plan_redemption_history_user_data(
        self,
        request_id: int,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        asset: str | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1LendingAutoInvestRedeemHistoryResponse]:
        """Get the history of Index Linked Plan Redemption transactions

        Max 30 day difference between startTime and endTime If no startTime and endTime, default to show past 30 day
        records

        Weight(IP): 1

        Args:
            request_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            asset: Value sent with the request.
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Redemption history

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.index_linked_plan_redemption_history_user_data(
            request_id,
            timestamp,
            signature,
            start_time=start_time,
            end_time=end_time,
            current=current,
            asset=asset,
            size=size,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def investment_plan_adjustment(
        self,
        plan_id: int,
        subscription_amount: float,
        subscription_cycle: SubscriptionCycleOrStr,
        subscription_start_time: int,
        source_asset: str,
        timestamp: int,
        signature: str,
        *,
        subscription_start_day: int | None = None,
        subscription_start_weekday: SubscriptionStartWeekdayOrStr | None = None,
        flexible_allowed_to_use: bool | None = None,
        details: list[Detail1 | Detail1Dict] | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LendingAutoInvestPlanEditResponse:
        """Query Source Asset to be used for investment

        Weight(IP): 1

        Args:
            plan_id: Value sent with the request.
            subscription_amount: Value sent with the request.
            subscription_cycle: Value sent with the request.
            subscription_start_time: Value sent with the request.
            source_asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            subscription_start_day: Value sent with the request.
            subscription_start_weekday: Value sent with the request.
            flexible_allowed_to_use: Value sent with the request.
            details: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Plan result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.investment_plan_adjustment(
            plan_id,
            subscription_amount,
            subscription_cycle,
            subscription_start_time,
            source_asset,
            timestamp,
            signature,
            subscription_start_day=subscription_start_day,
            subscription_start_weekday=subscription_start_weekday,
            flexible_allowed_to_use=flexible_allowed_to_use,
            details=details,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def investment_plan_creation_user_data(
        self,
        source_type: SourceTypeOrStr,
        plan_type: PlanTypeOrStr,
        subscription_amount: float,
        subscription_cycle: SubscriptionCycleOrStr,
        subscription_start_time: int,
        source_asset: str,
        details: list[Detail1 | Detail1Dict],
        timestamp: int,
        signature: str,
        *,
        request_id: str | None = None,
        index_id: int | None = None,
        subscription_start_day: int | None = None,
        subscription_start_weekday: SubscriptionStartWeekdayOrStr | None = None,
        flexible_allowed_to_use: bool | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LendingAutoInvestPlanAddResponse:
        """Post an investment plan creation

        Weight(IP): 1

        Args:
            source_type: Value sent with the request.
            plan_type: Value sent with the request.
            subscription_amount: Value sent with the request.
            subscription_cycle: Value sent with the request.
            subscription_start_time: Value sent with the request.
            source_asset: Value sent with the request.
            details: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            request_id: Value sent with the request.
            index_id: Value sent with the request.
            subscription_start_day: Value sent with the request.
            subscription_start_weekday: Value sent with the request.
            flexible_allowed_to_use: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Plan result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.investment_plan_creation_user_data(
            source_type,
            plan_type,
            subscription_amount,
            subscription_cycle,
            subscription_start_time,
            source_asset,
            details,
            timestamp,
            signature,
            request_id=request_id,
            index_id=index_id,
            subscription_start_day=subscription_start_day,
            subscription_start_weekday=subscription_start_weekday,
            flexible_allowed_to_use=flexible_allowed_to_use,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def one_time_transaction_trade(
        self,
        source_type: str,
        subscription_amount: float,
        source_asset: str,
        timestamp: int,
        signature: str,
        *,
        request_id: str | None = None,
        flexible_allowed_to_use: bool | None = None,
        plan_id: int | None = None,
        index_id: int | None = None,
        details: list[Detail5 | Detail5Dict] | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LendingAutoInvestOneOffResponse:
        """One time transaction

        Weight(IP): 1

        Args:
            source_type: Value sent with the request.
            subscription_amount: Value sent with the request.
            source_asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            request_id: Value sent with the request.
            flexible_allowed_to_use: Value sent with the request.
            plan_id: Value sent with the request.
            index_id: Value sent with the request.
            details: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            transaction result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.one_time_transaction_trade(
            source_type,
            subscription_amount,
            source_asset,
            timestamp,
            signature,
            request_id=request_id,
            flexible_allowed_to_use=flexible_allowed_to_use,
            plan_id=plan_id,
            index_id=index_id,
            details=details,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def query_index_details_user_data(
        self,
        index_id: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LendingAutoInvestIndexInfoResponse:
        """Query index details

        Weight(IP): 1

        Args:
            index_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Index result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_index_details_user_data(
            index_id, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def query_index_linked_plan_position_details_user_data(
        self,
        index_id: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LendingAutoInvestIndexUserSummaryResponse:
        """Details on users Index-Linked plan position details

        Weight(IP): 1

        Args:
            index_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Position Details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_index_linked_plan_position_details_user_data(
            index_id, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def query_one_time_transaction_status_user_data(
        self,
        transaction_id: int,
        timestamp: int,
        signature: str,
        *,
        request_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LendingAutoInvestOneOffStatusResponse:
        """Transaction status for one-time transaction

        Weight(IP): 1

        Args:
            transaction_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            request_id: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            transaction result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_one_time_transaction_status_user_data(
            transaction_id,
            timestamp,
            signature,
            request_id=request_id,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def query_all_source_asset_and_target_asset_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LendingAutoInvestAllAssetResponse:
        """Query all source assets and target assets

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Target asset

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_all_source_asset_and_target_asset_user_data(
            timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def query_holding_details_of_the_plan(
        self,
        timestamp: int,
        signature: str,
        *,
        plan_id: int | None = None,
        request_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LendingAutoInvestPlanIdResponse:
        """Query holding details of the plan

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            plan_id: Value sent with the request.
            request_id: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Plan result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_holding_details_of_the_plan(
            timestamp,
            signature,
            plan_id=plan_id,
            request_id=request_id,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def query_source_asset_list_user_data(
        self,
        usage_type: str,
        timestamp: int,
        signature: str,
        *,
        target_asset: str | None = None,
        index_id: int | None = None,
        flexible_allowed_to_use: bool | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LendingAutoInvestSourceAssetListResponse:
        """Query Source Asset to be used for investment

        Weight(IP): 1

        Args:
            usage_type: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            target_asset: Value sent with the request.
            index_id: Value sent with the request.
            flexible_allowed_to_use: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Asset list

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_source_asset_list_user_data(
            usage_type,
            timestamp,
            signature,
            target_asset=target_asset,
            index_id=index_id,
            flexible_allowed_to_use=flexible_allowed_to_use,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def query_subscription_transaction_history(
        self,
        timestamp: int,
        signature: str,
        *,
        plan_id: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        target_asset: int | None = None,
        plan_type: PlanType1OrStr | None = None,
        size: int | None = None,
        current: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1LendingAutoInvestHistoryListResponse]:
        """Query subscription transaction history of a plan

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            plan_id: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            target_asset: Value sent with the request.
            plan_type: Value sent with the request.
            size: Default:10 Max:100
            current: Current querying page. Start from 1. Default:1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Plan result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_subscription_transaction_history(
            timestamp,
            signature,
            plan_id=plan_id,
            start_time=start_time,
            end_time=end_time,
            target_asset=target_asset,
            plan_type=plan_type,
            size=size,
            current=current,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> AutoInvestWithRawResponse:
        return self._with_raw_response


class AsyncAutoInvest:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAutoInvestWithRawResponse(client, server, auth)

    async def change_plan_status(
        self,
        plan_id: int,
        status: Status1OrStr,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LendingAutoInvestPlanEditStatusResponse:
        """Change Plan Status

        Weight(IP): 1

        Args:
            plan_id: Value sent with the request.
            status: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Plan result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.change_plan_status(
                plan_id, status, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def get_list_of_plans(
        self,
        plan_type: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LendingAutoInvestPlanListResponse:
        """Query plan lists

        Weight(IP): 1

        Args:
            plan_type: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Plan result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_list_of_plans(
                plan_type, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def get_target_asset_roi_data_user_data(
        self,
        target_asset: str,
        his_roi_type: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1LendingAutoInvestTargetAssetRoiListResponse]:
        """ROI return list for target asset

        Weight(IP): 1

        Args:
            target_asset: Value sent with the request.
            his_roi_type: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Target asset list

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_target_asset_roi_data_user_data(
                target_asset,
                his_roi_type,
                timestamp,
                signature,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def get_target_asset_list_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        target_asset: str | None = None,
        size: int | None = None,
        current: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LendingAutoInvestTargetAssetListResponse:
        """Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            target_asset: Value sent with the request.
            size: Default:10 Max:100
            current: Current querying page. Start from 1. Default:1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Target asset list

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_target_asset_list_user_data(
                timestamp,
                signature,
                target_asset=target_asset,
                size=size,
                current=current,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def index_linked_plan_rebalance_details_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1LendingAutoInvestRebalanceHistoryResponse]:
        """Get the history of Index Linked Plan Redemption transactions

        Max 30 day difference between startTime and endTime If no startTime and endTime, default to show past 30 day
        records

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Rebalance Details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.index_linked_plan_rebalance_details_user_data(
                timestamp,
                signature,
                start_time=start_time,
                end_time=end_time,
                current=current,
                size=size,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def index_linked_plan_redemption_trade(
        self,
        index_id: int,
        redemption_percentage: int,
        timestamp: int,
        signature: str,
        *,
        request_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LendingAutoInvestRedeemResponse:
        """To redeem index-Linked plan holdings

        Weight(IP): 1

        Args:
            index_id: PORTFOLIO plan's Id
            redemption_percentage: user redeem percentage,10/20/100.
            timestamp: UTC timestamp in ms
            signature: Signature
            request_id: sourceType + unique, transactionId and requestId cannot be empty at the same time
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Redemption result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.index_linked_plan_redemption_trade(
                index_id,
                redemption_percentage,
                timestamp,
                signature,
                request_id=request_id,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def index_linked_plan_redemption_history_user_data(
        self,
        request_id: int,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        asset: str | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1LendingAutoInvestRedeemHistoryResponse]:
        """Get the history of Index Linked Plan Redemption transactions

        Max 30 day difference between startTime and endTime If no startTime and endTime, default to show past 30 day
        records

        Weight(IP): 1

        Args:
            request_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            asset: Value sent with the request.
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Redemption history

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.index_linked_plan_redemption_history_user_data(
                request_id,
                timestamp,
                signature,
                start_time=start_time,
                end_time=end_time,
                current=current,
                asset=asset,
                size=size,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def investment_plan_adjustment(
        self,
        plan_id: int,
        subscription_amount: float,
        subscription_cycle: SubscriptionCycleOrStr,
        subscription_start_time: int,
        source_asset: str,
        timestamp: int,
        signature: str,
        *,
        subscription_start_day: int | None = None,
        subscription_start_weekday: SubscriptionStartWeekdayOrStr | None = None,
        flexible_allowed_to_use: bool | None = None,
        details: list[Detail1 | Detail1Dict] | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LendingAutoInvestPlanEditResponse:
        """Query Source Asset to be used for investment

        Weight(IP): 1

        Args:
            plan_id: Value sent with the request.
            subscription_amount: Value sent with the request.
            subscription_cycle: Value sent with the request.
            subscription_start_time: Value sent with the request.
            source_asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            subscription_start_day: Value sent with the request.
            subscription_start_weekday: Value sent with the request.
            flexible_allowed_to_use: Value sent with the request.
            details: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Plan result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.investment_plan_adjustment(
                plan_id,
                subscription_amount,
                subscription_cycle,
                subscription_start_time,
                source_asset,
                timestamp,
                signature,
                subscription_start_day=subscription_start_day,
                subscription_start_weekday=subscription_start_weekday,
                flexible_allowed_to_use=flexible_allowed_to_use,
                details=details,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def investment_plan_creation_user_data(
        self,
        source_type: SourceTypeOrStr,
        plan_type: PlanTypeOrStr,
        subscription_amount: float,
        subscription_cycle: SubscriptionCycleOrStr,
        subscription_start_time: int,
        source_asset: str,
        details: list[Detail1 | Detail1Dict],
        timestamp: int,
        signature: str,
        *,
        request_id: str | None = None,
        index_id: int | None = None,
        subscription_start_day: int | None = None,
        subscription_start_weekday: SubscriptionStartWeekdayOrStr | None = None,
        flexible_allowed_to_use: bool | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LendingAutoInvestPlanAddResponse:
        """Post an investment plan creation

        Weight(IP): 1

        Args:
            source_type: Value sent with the request.
            plan_type: Value sent with the request.
            subscription_amount: Value sent with the request.
            subscription_cycle: Value sent with the request.
            subscription_start_time: Value sent with the request.
            source_asset: Value sent with the request.
            details: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            request_id: Value sent with the request.
            index_id: Value sent with the request.
            subscription_start_day: Value sent with the request.
            subscription_start_weekday: Value sent with the request.
            flexible_allowed_to_use: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Plan result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.investment_plan_creation_user_data(
                source_type,
                plan_type,
                subscription_amount,
                subscription_cycle,
                subscription_start_time,
                source_asset,
                details,
                timestamp,
                signature,
                request_id=request_id,
                index_id=index_id,
                subscription_start_day=subscription_start_day,
                subscription_start_weekday=subscription_start_weekday,
                flexible_allowed_to_use=flexible_allowed_to_use,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def one_time_transaction_trade(
        self,
        source_type: str,
        subscription_amount: float,
        source_asset: str,
        timestamp: int,
        signature: str,
        *,
        request_id: str | None = None,
        flexible_allowed_to_use: bool | None = None,
        plan_id: int | None = None,
        index_id: int | None = None,
        details: list[Detail5 | Detail5Dict] | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LendingAutoInvestOneOffResponse:
        """One time transaction

        Weight(IP): 1

        Args:
            source_type: Value sent with the request.
            subscription_amount: Value sent with the request.
            source_asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            request_id: Value sent with the request.
            flexible_allowed_to_use: Value sent with the request.
            plan_id: Value sent with the request.
            index_id: Value sent with the request.
            details: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            transaction result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.one_time_transaction_trade(
                source_type,
                subscription_amount,
                source_asset,
                timestamp,
                signature,
                request_id=request_id,
                flexible_allowed_to_use=flexible_allowed_to_use,
                plan_id=plan_id,
                index_id=index_id,
                details=details,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def query_index_details_user_data(
        self,
        index_id: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LendingAutoInvestIndexInfoResponse:
        """Query index details

        Weight(IP): 1

        Args:
            index_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Index result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_index_details_user_data(
                index_id, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def query_index_linked_plan_position_details_user_data(
        self,
        index_id: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LendingAutoInvestIndexUserSummaryResponse:
        """Details on users Index-Linked plan position details

        Weight(IP): 1

        Args:
            index_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Position Details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_index_linked_plan_position_details_user_data(
                index_id, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def query_one_time_transaction_status_user_data(
        self,
        transaction_id: int,
        timestamp: int,
        signature: str,
        *,
        request_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LendingAutoInvestOneOffStatusResponse:
        """Transaction status for one-time transaction

        Weight(IP): 1

        Args:
            transaction_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            request_id: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            transaction result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_one_time_transaction_status_user_data(
                transaction_id,
                timestamp,
                signature,
                request_id=request_id,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def query_all_source_asset_and_target_asset_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LendingAutoInvestAllAssetResponse:
        """Query all source assets and target assets

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Target asset

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_all_source_asset_and_target_asset_user_data(
                timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def query_holding_details_of_the_plan(
        self,
        timestamp: int,
        signature: str,
        *,
        plan_id: int | None = None,
        request_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LendingAutoInvestPlanIdResponse:
        """Query holding details of the plan

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            plan_id: Value sent with the request.
            request_id: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Plan result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_holding_details_of_the_plan(
                timestamp,
                signature,
                plan_id=plan_id,
                request_id=request_id,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def query_source_asset_list_user_data(
        self,
        usage_type: str,
        timestamp: int,
        signature: str,
        *,
        target_asset: str | None = None,
        index_id: int | None = None,
        flexible_allowed_to_use: bool | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1LendingAutoInvestSourceAssetListResponse:
        """Query Source Asset to be used for investment

        Weight(IP): 1

        Args:
            usage_type: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            target_asset: Value sent with the request.
            index_id: Value sent with the request.
            flexible_allowed_to_use: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Asset list

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_source_asset_list_user_data(
                usage_type,
                timestamp,
                signature,
                target_asset=target_asset,
                index_id=index_id,
                flexible_allowed_to_use=flexible_allowed_to_use,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def query_subscription_transaction_history(
        self,
        timestamp: int,
        signature: str,
        *,
        plan_id: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        target_asset: int | None = None,
        plan_type: PlanType1OrStr | None = None,
        size: int | None = None,
        current: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1LendingAutoInvestHistoryListResponse]:
        """Query subscription transaction history of a plan

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            plan_id: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            target_asset: Value sent with the request.
            plan_type: Value sent with the request.
            size: Default:10 Max:100
            current: Current querying page. Start from 1. Default:1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Plan result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_subscription_transaction_history(
                timestamp,
                signature,
                plan_id=plan_id,
                start_time=start_time,
                end_time=end_time,
                target_asset=target_asset,
                plan_type=plan_type,
                size=size,
                current=current,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncAutoInvestWithRawResponse:
        return self._with_raw_response


class AutoInvestWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def change_plan_status(
        self,
        plan_id: int,
        status: Status1OrStr,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LendingAutoInvestPlanEditStatusResponse, ChangePlanStatusErrorBody]:
        """Change Plan Status

        Weight(IP): 1

        Args:
            plan_id: Value sent with the request.
            status: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/lending/auto-invest/plan/edit-status"),
            query_params=[
                param[int]("planId", plan_id),
                param[Status1OrStr]("status", status),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LendingAutoInvestPlanEditStatusResponse],
            error_mapper=change_plan_status_error_mapper,
            request_options=request_options,
        )

    def get_list_of_plans(
        self,
        plan_type: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LendingAutoInvestPlanListResponse, GetListOfPlansErrorBody]:
        """Query plan lists

        Weight(IP): 1

        Args:
            plan_type: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/lending/auto-invest/plan/list"),
            query_params=[
                param[str]("planType", plan_type),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LendingAutoInvestPlanListResponse],
            error_mapper=get_list_of_plans_error_mapper,
            request_options=request_options,
        )

    def get_target_asset_roi_data_user_data(
        self,
        target_asset: str,
        his_roi_type: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1LendingAutoInvestTargetAssetRoiListResponse], GetTargetAssetRoiDataUserDataErrorBody]:
        """ROI return list for target asset

        Weight(IP): 1

        Args:
            target_asset: Value sent with the request.
            his_roi_type: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/lending/auto-invest/target-asset/roi/list"),
            query_params=[
                param[str]("targetAsset", target_asset),
                param[str]("hisRoiType", his_roi_type),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1LendingAutoInvestTargetAssetRoiListResponse]],
            error_mapper=get_target_asset_roi_data_user_data_error_mapper,
            request_options=request_options,
        )

    def get_target_asset_list_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        target_asset: str | None = None,
        size: int | None = None,
        current: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LendingAutoInvestTargetAssetListResponse, GetTargetAssetListUserDataErrorBody]:
        """Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            target_asset: Value sent with the request.
            size: Default:10 Max:100
            current: Current querying page. Start from 1. Default:1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/lending/auto-invest/target-asset/list"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("targetAsset", target_asset),
                param[int | None]("size", size),
                param[int | None]("current", current),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LendingAutoInvestTargetAssetListResponse],
            error_mapper=get_target_asset_list_user_data_error_mapper,
            request_options=request_options,
        )

    def index_linked_plan_rebalance_details_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        list[SapiV1LendingAutoInvestRebalanceHistoryResponse], IndexLinkedPlanRebalanceDetailsUserDataErrorBody
    ]:
        """Get the history of Index Linked Plan Redemption transactions

        Max 30 day difference between startTime and endTime If no startTime and endTime, default to show past 30 day
        records

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/lending/auto-invest/rebalance/history"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1LendingAutoInvestRebalanceHistoryResponse]],
            error_mapper=index_linked_plan_rebalance_details_user_data_error_mapper,
            request_options=request_options,
        )

    def index_linked_plan_redemption_trade(
        self,
        index_id: int,
        redemption_percentage: int,
        timestamp: int,
        signature: str,
        *,
        request_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LendingAutoInvestRedeemResponse, IndexLinkedPlanRedemptionTradeErrorBody]:
        """To redeem index-Linked plan holdings

        Weight(IP): 1

        Args:
            index_id: PORTFOLIO plan's Id
            redemption_percentage: user redeem percentage,10/20/100.
            timestamp: UTC timestamp in ms
            signature: Signature
            request_id: sourceType + unique, transactionId and requestId cannot be empty at the same time
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/lending/auto-invest/redeem"),
            query_params=[
                param[int]("indexId", index_id),
                param[int]("redemptionPercentage", redemption_percentage),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("requestId", request_id),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LendingAutoInvestRedeemResponse],
            error_mapper=index_linked_plan_redemption_trade_error_mapper,
            request_options=request_options,
        )

    def index_linked_plan_redemption_history_user_data(
        self,
        request_id: int,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        asset: str | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        list[SapiV1LendingAutoInvestRedeemHistoryResponse], IndexLinkedPlanRedemptionHistoryUserDataErrorBody
    ]:
        """Get the history of Index Linked Plan Redemption transactions

        Max 30 day difference between startTime and endTime If no startTime and endTime, default to show past 30 day
        records

        Weight(IP): 1

        Args:
            request_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            asset: Value sent with the request.
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/lending/auto-invest/redeem/history"),
            query_params=[
                param[int]("requestId", request_id),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[str | None]("asset", asset),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1LendingAutoInvestRedeemHistoryResponse]],
            error_mapper=index_linked_plan_redemption_history_user_data_error_mapper,
            request_options=request_options,
        )

    def investment_plan_adjustment(
        self,
        plan_id: int,
        subscription_amount: float,
        subscription_cycle: SubscriptionCycleOrStr,
        subscription_start_time: int,
        source_asset: str,
        timestamp: int,
        signature: str,
        *,
        subscription_start_day: int | None = None,
        subscription_start_weekday: SubscriptionStartWeekdayOrStr | None = None,
        flexible_allowed_to_use: bool | None = None,
        details: list[Detail1 | Detail1Dict] | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LendingAutoInvestPlanEditResponse, InvestmentPlanAdjustmentErrorBody]:
        """Query Source Asset to be used for investment

        Weight(IP): 1

        Args:
            plan_id: Value sent with the request.
            subscription_amount: Value sent with the request.
            subscription_cycle: Value sent with the request.
            subscription_start_time: Value sent with the request.
            source_asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            subscription_start_day: Value sent with the request.
            subscription_start_weekday: Value sent with the request.
            flexible_allowed_to_use: Value sent with the request.
            details: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/lending/auto-invest/plan/edit"),
            query_params=[
                param[int]("planId", plan_id),
                param[float]("subscriptionAmount", subscription_amount),
                param[SubscriptionCycleOrStr]("subscriptionCycle", subscription_cycle),
                param[int]("subscriptionStartTime", subscription_start_time),
                param[str]("sourceAsset", source_asset),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("subscriptionStartDay", subscription_start_day),
                param[SubscriptionStartWeekdayOrStr | None]("subscriptionStartWeekday", subscription_start_weekday),
                param[bool | None]("flexibleAllowedToUse", flexible_allowed_to_use),
                param[list[Detail1 | Detail1Dict] | None]("details", details),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LendingAutoInvestPlanEditResponse],
            error_mapper=investment_plan_adjustment_error_mapper,
            request_options=request_options,
        )

    def investment_plan_creation_user_data(
        self,
        source_type: SourceTypeOrStr,
        plan_type: PlanTypeOrStr,
        subscription_amount: float,
        subscription_cycle: SubscriptionCycleOrStr,
        subscription_start_time: int,
        source_asset: str,
        details: list[Detail1 | Detail1Dict],
        timestamp: int,
        signature: str,
        *,
        request_id: str | None = None,
        index_id: int | None = None,
        subscription_start_day: int | None = None,
        subscription_start_weekday: SubscriptionStartWeekdayOrStr | None = None,
        flexible_allowed_to_use: bool | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LendingAutoInvestPlanAddResponse, InvestmentPlanCreationUserDataErrorBody]:
        """Post an investment plan creation

        Weight(IP): 1

        Args:
            source_type: Value sent with the request.
            plan_type: Value sent with the request.
            subscription_amount: Value sent with the request.
            subscription_cycle: Value sent with the request.
            subscription_start_time: Value sent with the request.
            source_asset: Value sent with the request.
            details: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            request_id: Value sent with the request.
            index_id: Value sent with the request.
            subscription_start_day: Value sent with the request.
            subscription_start_weekday: Value sent with the request.
            flexible_allowed_to_use: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/lending/auto-invest/plan/add"),
            query_params=[
                param[SourceTypeOrStr]("sourceType", source_type),
                param[PlanTypeOrStr]("planType", plan_type),
                param[float]("subscriptionAmount", subscription_amount),
                param[SubscriptionCycleOrStr]("subscriptionCycle", subscription_cycle),
                param[int]("subscriptionStartTime", subscription_start_time),
                param[str]("sourceAsset", source_asset),
                param[list[Detail1 | Detail1Dict]]("details", details),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("requestId", request_id),
                param[int | None]("IndexId", index_id),
                param[int | None]("subscriptionStartDay", subscription_start_day),
                param[SubscriptionStartWeekdayOrStr | None]("subscriptionStartWeekday", subscription_start_weekday),
                param[bool | None]("flexibleAllowedToUse", flexible_allowed_to_use),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LendingAutoInvestPlanAddResponse],
            error_mapper=investment_plan_creation_user_data_error_mapper,
            request_options=request_options,
        )

    def one_time_transaction_trade(
        self,
        source_type: str,
        subscription_amount: float,
        source_asset: str,
        timestamp: int,
        signature: str,
        *,
        request_id: str | None = None,
        flexible_allowed_to_use: bool | None = None,
        plan_id: int | None = None,
        index_id: int | None = None,
        details: list[Detail5 | Detail5Dict] | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LendingAutoInvestOneOffResponse, OneTimeTransactionTradeErrorBody]:
        """One time transaction

        Weight(IP): 1

        Args:
            source_type: Value sent with the request.
            subscription_amount: Value sent with the request.
            source_asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            request_id: Value sent with the request.
            flexible_allowed_to_use: Value sent with the request.
            plan_id: Value sent with the request.
            index_id: Value sent with the request.
            details: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/lending/auto-invest/one-off"),
            query_params=[
                param[str]("sourceType", source_type),
                param[float]("subscriptionAmount", subscription_amount),
                param[str]("sourceAsset", source_asset),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("requestId", request_id),
                param[bool | None]("flexibleAllowedToUse", flexible_allowed_to_use),
                param[int | None]("planId", plan_id),
                param[int | None]("indexId", index_id),
                param[list[Detail5 | Detail5Dict] | None]("details", details),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LendingAutoInvestOneOffResponse],
            error_mapper=one_time_transaction_trade_error_mapper,
            request_options=request_options,
        )

    def query_index_details_user_data(
        self,
        index_id: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LendingAutoInvestIndexInfoResponse, QueryIndexDetailsUserDataErrorBody]:
        """Query index details

        Weight(IP): 1

        Args:
            index_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/lending/auto-invest/index/info"),
            query_params=[
                param[int]("indexId", index_id),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LendingAutoInvestIndexInfoResponse],
            error_mapper=query_index_details_user_data_error_mapper,
            request_options=request_options,
        )

    def query_index_linked_plan_position_details_user_data(
        self,
        index_id: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1LendingAutoInvestIndexUserSummaryResponse, QueryIndexLinkedPlanPositionDetailsUserDataErrorBody
    ]:
        """Details on users Index-Linked plan position details

        Weight(IP): 1

        Args:
            index_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/lending/auto-invest/index/user-summary"),
            query_params=[
                param[int]("indexId", index_id),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LendingAutoInvestIndexUserSummaryResponse],
            error_mapper=query_index_linked_plan_position_details_user_data_error_mapper,
            request_options=request_options,
        )

    def query_one_time_transaction_status_user_data(
        self,
        transaction_id: int,
        timestamp: int,
        signature: str,
        *,
        request_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LendingAutoInvestOneOffStatusResponse, QueryOneTimeTransactionStatusUserDataErrorBody]:
        """Transaction status for one-time transaction

        Weight(IP): 1

        Args:
            transaction_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            request_id: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/lending/auto-invest/one-off/status"),
            query_params=[
                param[int]("transactionId", transaction_id),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("requestId", request_id),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LendingAutoInvestOneOffStatusResponse],
            error_mapper=query_one_time_transaction_status_user_data_error_mapper,
            request_options=request_options,
        )

    def query_all_source_asset_and_target_asset_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LendingAutoInvestAllAssetResponse, QueryAllSourceAssetAndTargetAssetUserDataErrorBody]:
        """Query all source assets and target assets

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
            url_template=self._server.default("/sapi/v1/lending/auto-invest/all/asset"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LendingAutoInvestAllAssetResponse],
            error_mapper=query_all_source_asset_and_target_asset_user_data_error_mapper,
            request_options=request_options,
        )

    def query_holding_details_of_the_plan(
        self,
        timestamp: int,
        signature: str,
        *,
        plan_id: int | None = None,
        request_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LendingAutoInvestPlanIdResponse, QueryHoldingDetailsOfThePlanErrorBody]:
        """Query holding details of the plan

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            plan_id: Value sent with the request.
            request_id: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/lending/auto-invest/plan/id"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("planId", plan_id),
                param[str | None]("requestId", request_id),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LendingAutoInvestPlanIdResponse],
            error_mapper=query_holding_details_of_the_plan_error_mapper,
            request_options=request_options,
        )

    def query_source_asset_list_user_data(
        self,
        usage_type: str,
        timestamp: int,
        signature: str,
        *,
        target_asset: str | None = None,
        index_id: int | None = None,
        flexible_allowed_to_use: bool | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LendingAutoInvestSourceAssetListResponse, QuerySourceAssetListUserDataErrorBody]:
        """Query Source Asset to be used for investment

        Weight(IP): 1

        Args:
            usage_type: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            target_asset: Value sent with the request.
            index_id: Value sent with the request.
            flexible_allowed_to_use: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/lending/auto-invest/source-asset/list"),
            query_params=[
                param[str]("usageType", usage_type),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("targetAsset", target_asset),
                param[int | None]("indexId", index_id),
                param[bool | None]("flexibleAllowedToUse", flexible_allowed_to_use),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LendingAutoInvestSourceAssetListResponse],
            error_mapper=query_source_asset_list_user_data_error_mapper,
            request_options=request_options,
        )

    def query_subscription_transaction_history(
        self,
        timestamp: int,
        signature: str,
        *,
        plan_id: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        target_asset: int | None = None,
        plan_type: PlanType1OrStr | None = None,
        size: int | None = None,
        current: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1LendingAutoInvestHistoryListResponse], QuerySubscriptionTransactionHistoryErrorBody]:
        """Query subscription transaction history of a plan

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            plan_id: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            target_asset: Value sent with the request.
            plan_type: Value sent with the request.
            size: Default:10 Max:100
            current: Current querying page. Start from 1. Default:1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/lending/auto-invest/history/list"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("planId", plan_id),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("targetAsset", target_asset),
                param[PlanType1OrStr | None]("planType", plan_type),
                param[int | None]("size", size),
                param[int | None]("current", current),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1LendingAutoInvestHistoryListResponse]],
            error_mapper=query_subscription_transaction_history_error_mapper,
            request_options=request_options,
        )


class AsyncAutoInvestWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def change_plan_status(
        self,
        plan_id: int,
        status: Status1OrStr,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LendingAutoInvestPlanEditStatusResponse, ChangePlanStatusErrorBody]:
        """Change Plan Status

        Weight(IP): 1

        Args:
            plan_id: Value sent with the request.
            status: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/lending/auto-invest/plan/edit-status"),
            query_params=[
                param[int]("planId", plan_id),
                param[Status1OrStr]("status", status),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LendingAutoInvestPlanEditStatusResponse],
            error_mapper=change_plan_status_error_mapper,
            request_options=request_options,
        )

    async def get_list_of_plans(
        self,
        plan_type: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LendingAutoInvestPlanListResponse, GetListOfPlansErrorBody]:
        """Query plan lists

        Weight(IP): 1

        Args:
            plan_type: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/lending/auto-invest/plan/list"),
            query_params=[
                param[str]("planType", plan_type),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LendingAutoInvestPlanListResponse],
            error_mapper=get_list_of_plans_error_mapper,
            request_options=request_options,
        )

    async def get_target_asset_roi_data_user_data(
        self,
        target_asset: str,
        his_roi_type: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1LendingAutoInvestTargetAssetRoiListResponse], GetTargetAssetRoiDataUserDataErrorBody]:
        """ROI return list for target asset

        Weight(IP): 1

        Args:
            target_asset: Value sent with the request.
            his_roi_type: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/lending/auto-invest/target-asset/roi/list"),
            query_params=[
                param[str]("targetAsset", target_asset),
                param[str]("hisRoiType", his_roi_type),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1LendingAutoInvestTargetAssetRoiListResponse]],
            error_mapper=get_target_asset_roi_data_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_target_asset_list_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        target_asset: str | None = None,
        size: int | None = None,
        current: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LendingAutoInvestTargetAssetListResponse, GetTargetAssetListUserDataErrorBody]:
        """Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            target_asset: Value sent with the request.
            size: Default:10 Max:100
            current: Current querying page. Start from 1. Default:1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/lending/auto-invest/target-asset/list"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("targetAsset", target_asset),
                param[int | None]("size", size),
                param[int | None]("current", current),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LendingAutoInvestTargetAssetListResponse],
            error_mapper=get_target_asset_list_user_data_error_mapper,
            request_options=request_options,
        )

    async def index_linked_plan_rebalance_details_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        list[SapiV1LendingAutoInvestRebalanceHistoryResponse], IndexLinkedPlanRebalanceDetailsUserDataErrorBody
    ]:
        """Get the history of Index Linked Plan Redemption transactions

        Max 30 day difference between startTime and endTime If no startTime and endTime, default to show past 30 day
        records

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/lending/auto-invest/rebalance/history"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1LendingAutoInvestRebalanceHistoryResponse]],
            error_mapper=index_linked_plan_rebalance_details_user_data_error_mapper,
            request_options=request_options,
        )

    async def index_linked_plan_redemption_trade(
        self,
        index_id: int,
        redemption_percentage: int,
        timestamp: int,
        signature: str,
        *,
        request_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LendingAutoInvestRedeemResponse, IndexLinkedPlanRedemptionTradeErrorBody]:
        """To redeem index-Linked plan holdings

        Weight(IP): 1

        Args:
            index_id: PORTFOLIO plan's Id
            redemption_percentage: user redeem percentage,10/20/100.
            timestamp: UTC timestamp in ms
            signature: Signature
            request_id: sourceType + unique, transactionId and requestId cannot be empty at the same time
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/lending/auto-invest/redeem"),
            query_params=[
                param[int]("indexId", index_id),
                param[int]("redemptionPercentage", redemption_percentage),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("requestId", request_id),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LendingAutoInvestRedeemResponse],
            error_mapper=index_linked_plan_redemption_trade_error_mapper,
            request_options=request_options,
        )

    async def index_linked_plan_redemption_history_user_data(
        self,
        request_id: int,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        asset: str | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        list[SapiV1LendingAutoInvestRedeemHistoryResponse], IndexLinkedPlanRedemptionHistoryUserDataErrorBody
    ]:
        """Get the history of Index Linked Plan Redemption transactions

        Max 30 day difference between startTime and endTime If no startTime and endTime, default to show past 30 day
        records

        Weight(IP): 1

        Args:
            request_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            asset: Value sent with the request.
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/lending/auto-invest/redeem/history"),
            query_params=[
                param[int]("requestId", request_id),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[str | None]("asset", asset),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1LendingAutoInvestRedeemHistoryResponse]],
            error_mapper=index_linked_plan_redemption_history_user_data_error_mapper,
            request_options=request_options,
        )

    async def investment_plan_adjustment(
        self,
        plan_id: int,
        subscription_amount: float,
        subscription_cycle: SubscriptionCycleOrStr,
        subscription_start_time: int,
        source_asset: str,
        timestamp: int,
        signature: str,
        *,
        subscription_start_day: int | None = None,
        subscription_start_weekday: SubscriptionStartWeekdayOrStr | None = None,
        flexible_allowed_to_use: bool | None = None,
        details: list[Detail1 | Detail1Dict] | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LendingAutoInvestPlanEditResponse, InvestmentPlanAdjustmentErrorBody]:
        """Query Source Asset to be used for investment

        Weight(IP): 1

        Args:
            plan_id: Value sent with the request.
            subscription_amount: Value sent with the request.
            subscription_cycle: Value sent with the request.
            subscription_start_time: Value sent with the request.
            source_asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            subscription_start_day: Value sent with the request.
            subscription_start_weekday: Value sent with the request.
            flexible_allowed_to_use: Value sent with the request.
            details: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/lending/auto-invest/plan/edit"),
            query_params=[
                param[int]("planId", plan_id),
                param[float]("subscriptionAmount", subscription_amount),
                param[SubscriptionCycleOrStr]("subscriptionCycle", subscription_cycle),
                param[int]("subscriptionStartTime", subscription_start_time),
                param[str]("sourceAsset", source_asset),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("subscriptionStartDay", subscription_start_day),
                param[SubscriptionStartWeekdayOrStr | None]("subscriptionStartWeekday", subscription_start_weekday),
                param[bool | None]("flexibleAllowedToUse", flexible_allowed_to_use),
                param[list[Detail1 | Detail1Dict] | None]("details", details),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LendingAutoInvestPlanEditResponse],
            error_mapper=investment_plan_adjustment_error_mapper,
            request_options=request_options,
        )

    async def investment_plan_creation_user_data(
        self,
        source_type: SourceTypeOrStr,
        plan_type: PlanTypeOrStr,
        subscription_amount: float,
        subscription_cycle: SubscriptionCycleOrStr,
        subscription_start_time: int,
        source_asset: str,
        details: list[Detail1 | Detail1Dict],
        timestamp: int,
        signature: str,
        *,
        request_id: str | None = None,
        index_id: int | None = None,
        subscription_start_day: int | None = None,
        subscription_start_weekday: SubscriptionStartWeekdayOrStr | None = None,
        flexible_allowed_to_use: bool | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LendingAutoInvestPlanAddResponse, InvestmentPlanCreationUserDataErrorBody]:
        """Post an investment plan creation

        Weight(IP): 1

        Args:
            source_type: Value sent with the request.
            plan_type: Value sent with the request.
            subscription_amount: Value sent with the request.
            subscription_cycle: Value sent with the request.
            subscription_start_time: Value sent with the request.
            source_asset: Value sent with the request.
            details: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            request_id: Value sent with the request.
            index_id: Value sent with the request.
            subscription_start_day: Value sent with the request.
            subscription_start_weekday: Value sent with the request.
            flexible_allowed_to_use: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/lending/auto-invest/plan/add"),
            query_params=[
                param[SourceTypeOrStr]("sourceType", source_type),
                param[PlanTypeOrStr]("planType", plan_type),
                param[float]("subscriptionAmount", subscription_amount),
                param[SubscriptionCycleOrStr]("subscriptionCycle", subscription_cycle),
                param[int]("subscriptionStartTime", subscription_start_time),
                param[str]("sourceAsset", source_asset),
                param[list[Detail1 | Detail1Dict]]("details", details),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("requestId", request_id),
                param[int | None]("IndexId", index_id),
                param[int | None]("subscriptionStartDay", subscription_start_day),
                param[SubscriptionStartWeekdayOrStr | None]("subscriptionStartWeekday", subscription_start_weekday),
                param[bool | None]("flexibleAllowedToUse", flexible_allowed_to_use),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LendingAutoInvestPlanAddResponse],
            error_mapper=investment_plan_creation_user_data_error_mapper,
            request_options=request_options,
        )

    async def one_time_transaction_trade(
        self,
        source_type: str,
        subscription_amount: float,
        source_asset: str,
        timestamp: int,
        signature: str,
        *,
        request_id: str | None = None,
        flexible_allowed_to_use: bool | None = None,
        plan_id: int | None = None,
        index_id: int | None = None,
        details: list[Detail5 | Detail5Dict] | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LendingAutoInvestOneOffResponse, OneTimeTransactionTradeErrorBody]:
        """One time transaction

        Weight(IP): 1

        Args:
            source_type: Value sent with the request.
            subscription_amount: Value sent with the request.
            source_asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            request_id: Value sent with the request.
            flexible_allowed_to_use: Value sent with the request.
            plan_id: Value sent with the request.
            index_id: Value sent with the request.
            details: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/lending/auto-invest/one-off"),
            query_params=[
                param[str]("sourceType", source_type),
                param[float]("subscriptionAmount", subscription_amount),
                param[str]("sourceAsset", source_asset),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("requestId", request_id),
                param[bool | None]("flexibleAllowedToUse", flexible_allowed_to_use),
                param[int | None]("planId", plan_id),
                param[int | None]("indexId", index_id),
                param[list[Detail5 | Detail5Dict] | None]("details", details),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LendingAutoInvestOneOffResponse],
            error_mapper=one_time_transaction_trade_error_mapper,
            request_options=request_options,
        )

    async def query_index_details_user_data(
        self,
        index_id: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LendingAutoInvestIndexInfoResponse, QueryIndexDetailsUserDataErrorBody]:
        """Query index details

        Weight(IP): 1

        Args:
            index_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/lending/auto-invest/index/info"),
            query_params=[
                param[int]("indexId", index_id),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LendingAutoInvestIndexInfoResponse],
            error_mapper=query_index_details_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_index_linked_plan_position_details_user_data(
        self,
        index_id: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1LendingAutoInvestIndexUserSummaryResponse, QueryIndexLinkedPlanPositionDetailsUserDataErrorBody
    ]:
        """Details on users Index-Linked plan position details

        Weight(IP): 1

        Args:
            index_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/lending/auto-invest/index/user-summary"),
            query_params=[
                param[int]("indexId", index_id),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LendingAutoInvestIndexUserSummaryResponse],
            error_mapper=query_index_linked_plan_position_details_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_one_time_transaction_status_user_data(
        self,
        transaction_id: int,
        timestamp: int,
        signature: str,
        *,
        request_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LendingAutoInvestOneOffStatusResponse, QueryOneTimeTransactionStatusUserDataErrorBody]:
        """Transaction status for one-time transaction

        Weight(IP): 1

        Args:
            transaction_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            request_id: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/lending/auto-invest/one-off/status"),
            query_params=[
                param[int]("transactionId", transaction_id),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("requestId", request_id),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LendingAutoInvestOneOffStatusResponse],
            error_mapper=query_one_time_transaction_status_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_all_source_asset_and_target_asset_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LendingAutoInvestAllAssetResponse, QueryAllSourceAssetAndTargetAssetUserDataErrorBody]:
        """Query all source assets and target assets

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
            url_template=self._server.default("/sapi/v1/lending/auto-invest/all/asset"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LendingAutoInvestAllAssetResponse],
            error_mapper=query_all_source_asset_and_target_asset_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_holding_details_of_the_plan(
        self,
        timestamp: int,
        signature: str,
        *,
        plan_id: int | None = None,
        request_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LendingAutoInvestPlanIdResponse, QueryHoldingDetailsOfThePlanErrorBody]:
        """Query holding details of the plan

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            plan_id: Value sent with the request.
            request_id: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/lending/auto-invest/plan/id"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("planId", plan_id),
                param[str | None]("requestId", request_id),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LendingAutoInvestPlanIdResponse],
            error_mapper=query_holding_details_of_the_plan_error_mapper,
            request_options=request_options,
        )

    async def query_source_asset_list_user_data(
        self,
        usage_type: str,
        timestamp: int,
        signature: str,
        *,
        target_asset: str | None = None,
        index_id: int | None = None,
        flexible_allowed_to_use: bool | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1LendingAutoInvestSourceAssetListResponse, QuerySourceAssetListUserDataErrorBody]:
        """Query Source Asset to be used for investment

        Weight(IP): 1

        Args:
            usage_type: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            target_asset: Value sent with the request.
            index_id: Value sent with the request.
            flexible_allowed_to_use: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/lending/auto-invest/source-asset/list"),
            query_params=[
                param[str]("usageType", usage_type),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("targetAsset", target_asset),
                param[int | None]("indexId", index_id),
                param[bool | None]("flexibleAllowedToUse", flexible_allowed_to_use),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1LendingAutoInvestSourceAssetListResponse],
            error_mapper=query_source_asset_list_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_subscription_transaction_history(
        self,
        timestamp: int,
        signature: str,
        *,
        plan_id: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        target_asset: int | None = None,
        plan_type: PlanType1OrStr | None = None,
        size: int | None = None,
        current: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1LendingAutoInvestHistoryListResponse], QuerySubscriptionTransactionHistoryErrorBody]:
        """Query subscription transaction history of a plan

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            plan_id: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            target_asset: Value sent with the request.
            plan_type: Value sent with the request.
            size: Default:10 Max:100
            current: Current querying page. Start from 1. Default:1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/lending/auto-invest/history/list"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("planId", plan_id),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("targetAsset", target_asset),
                param[PlanType1OrStr | None]("planType", plan_type),
                param[int | None]("size", size),
                param[int | None]("current", current),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1LendingAutoInvestHistoryListResponse]],
            error_mapper=query_subscription_transaction_history_error_mapper,
            request_options=request_options,
        )
