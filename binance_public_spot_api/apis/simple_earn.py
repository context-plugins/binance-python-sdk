from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder, param
from ..errors.get_collateral_record_user_data_error import (
    GetCollateralRecordUserDataErrorBody,
    get_collateral_record_user_data_error_mapper,
)
from ..errors.get_flexible_personal_left_quota_user_data_error import (
    GetFlexiblePersonalLeftQuotaUserDataErrorBody,
    get_flexible_personal_left_quota_user_data_error_mapper,
)
from ..errors.get_flexible_product_position_user_data_error import (
    GetFlexibleProductPositionUserDataErrorBody,
    get_flexible_product_position_user_data_error_mapper,
)
from ..errors.get_flexible_redemption_record_user_data_error import (
    GetFlexibleRedemptionRecordUserDataErrorBody,
    get_flexible_redemption_record_user_data_error_mapper,
)
from ..errors.get_flexible_rewards_history_user_data_error import (
    GetFlexibleRewardsHistoryUserDataErrorBody,
    get_flexible_rewards_history_user_data_error_mapper,
)
from ..errors.get_flexible_subscription_preview_user_data_error import (
    GetFlexibleSubscriptionPreviewUserDataErrorBody,
    get_flexible_subscription_preview_user_data_error_mapper,
)
from ..errors.get_flexible_subscription_record_user_data_error import (
    GetFlexibleSubscriptionRecordUserDataErrorBody,
    get_flexible_subscription_record_user_data_error_mapper,
)
from ..errors.get_locked_personal_left_quota_user_data_error import (
    GetLockedPersonalLeftQuotaUserDataErrorBody,
    get_locked_personal_left_quota_user_data_error_mapper,
)
from ..errors.get_locked_product_position_user_data_error import (
    GetLockedProductPositionUserDataErrorBody,
    get_locked_product_position_user_data_error_mapper,
)
from ..errors.get_locked_redemption_record_user_data_error import (
    GetLockedRedemptionRecordUserDataErrorBody,
    get_locked_redemption_record_user_data_error_mapper,
)
from ..errors.get_locked_rewards_history_user_data_error import (
    GetLockedRewardsHistoryUserDataErrorBody,
    get_locked_rewards_history_user_data_error_mapper,
)
from ..errors.get_locked_subscription_preview_user_data_error import (
    GetLockedSubscriptionPreviewUserDataErrorBody,
    get_locked_subscription_preview_user_data_error_mapper,
)
from ..errors.get_locked_subscription_record_user_data_error import (
    GetLockedSubscriptionRecordUserDataErrorBody,
    get_locked_subscription_record_user_data_error_mapper,
)
from ..errors.get_rate_history_user_data_error import (
    GetRateHistoryUserDataErrorBody,
    get_rate_history_user_data_error_mapper,
)
from ..errors.get_simple_earn_flexible_product_list_user_data_error import (
    GetSimpleEarnFlexibleProductListUserDataErrorBody,
    get_simple_earn_flexible_product_list_user_data_error_mapper,
)
from ..errors.get_simple_earn_locked_product_list_user_data_error import (
    GetSimpleEarnLockedProductListUserDataErrorBody,
    get_simple_earn_locked_product_list_user_data_error_mapper,
)
from ..errors.redeem_flexible_product_trade_error import (
    RedeemFlexibleProductTradeErrorBody,
    redeem_flexible_product_trade_error_mapper,
)
from ..errors.redeem_locked_product_trade_error import (
    RedeemLockedProductTradeErrorBody,
    redeem_locked_product_trade_error_mapper,
)
from ..errors.set_flexible_auto_subscribe_user_data_error import (
    SetFlexibleAutoSubscribeUserDataErrorBody,
    set_flexible_auto_subscribe_user_data_error_mapper,
)
from ..errors.set_locked_auto_subscribe_user_data_error import (
    SetLockedAutoSubscribeUserDataErrorBody,
    set_locked_auto_subscribe_user_data_error_mapper,
)
from ..errors.set_locked_product_redeem_option_user_data_error import (
    SetLockedProductRedeemOptionUserDataErrorBody,
    set_locked_product_redeem_option_user_data_error_mapper,
)
from ..errors.simple_account_user_data_error import (
    SimpleAccountUserDataErrorBody,
    simple_account_user_data_error_mapper,
)
from ..errors.subscribe_flexible_product_trade_error import (
    SubscribeFlexibleProductTradeErrorBody,
    subscribe_flexible_product_trade_error_mapper,
)
from ..errors.subscribe_locked_product_trade_error import (
    SubscribeLockedProductTradeErrorBody,
    subscribe_locked_product_trade_error_mapper,
)
from ..models.enums.redeem_to import RedeemToOrStr
from ..models.sapi_v1_simple_earn_account_response import SapiV1SimpleEarnAccountResponse
from ..models.sapi_v1_simple_earn_flexible_history_collateral_record_response import (
    SapiV1SimpleEarnFlexibleHistoryCollateralRecordResponse,
)
from ..models.sapi_v1_simple_earn_flexible_history_rate_history_response import (
    SapiV1SimpleEarnFlexibleHistoryRateHistoryResponse,
)
from ..models.sapi_v1_simple_earn_flexible_history_redemption_record_response import (
    SapiV1SimpleEarnFlexibleHistoryRedemptionRecordResponse,
)
from ..models.sapi_v1_simple_earn_flexible_history_rewards_record_response import (
    SapiV1SimpleEarnFlexibleHistoryRewardsRecordResponse,
)
from ..models.sapi_v1_simple_earn_flexible_history_subscription_record_response import (
    SapiV1SimpleEarnFlexibleHistorySubscriptionRecordResponse,
)
from ..models.sapi_v1_simple_earn_flexible_list_response import SapiV1SimpleEarnFlexibleListResponse
from ..models.sapi_v1_simple_earn_flexible_personal_left_quota_response import (
    SapiV1SimpleEarnFlexiblePersonalLeftQuotaResponse,
)
from ..models.sapi_v1_simple_earn_flexible_position_response import SapiV1SimpleEarnFlexiblePositionResponse
from ..models.sapi_v1_simple_earn_flexible_redeem_response import SapiV1SimpleEarnFlexibleRedeemResponse
from ..models.sapi_v1_simple_earn_flexible_set_auto_subscribe_response import (
    SapiV1SimpleEarnFlexibleSetAutoSubscribeResponse,
)
from ..models.sapi_v1_simple_earn_flexible_subscribe_response import SapiV1SimpleEarnFlexibleSubscribeResponse
from ..models.sapi_v1_simple_earn_flexible_subscription_preview_response import (
    SapiV1SimpleEarnFlexibleSubscriptionPreviewResponse,
)
from ..models.sapi_v1_simple_earn_locked_history_redemption_record_response import (
    SapiV1SimpleEarnLockedHistoryRedemptionRecordResponse,
)
from ..models.sapi_v1_simple_earn_locked_history_rewards_record_response import (
    SapiV1SimpleEarnLockedHistoryRewardsRecordResponse,
)
from ..models.sapi_v1_simple_earn_locked_history_subscription_record_response import (
    SapiV1SimpleEarnLockedHistorySubscriptionRecordResponse,
)
from ..models.sapi_v1_simple_earn_locked_list_response import SapiV1SimpleEarnLockedListResponse
from ..models.sapi_v1_simple_earn_locked_personal_left_quota_response import (
    SapiV1SimpleEarnLockedPersonalLeftQuotaResponse,
)
from ..models.sapi_v1_simple_earn_locked_position_response import SapiV1SimpleEarnLockedPositionResponse
from ..models.sapi_v1_simple_earn_locked_redeem_response import SapiV1SimpleEarnLockedRedeemResponse
from ..models.sapi_v1_simple_earn_locked_set_auto_subscribe_response import (
    SapiV1SimpleEarnLockedSetAutoSubscribeResponse,
)
from ..models.sapi_v1_simple_earn_locked_set_redeem_option_response import SapiV1SimpleEarnLockedSetRedeemOptionResponse
from ..models.sapi_v1_simple_earn_locked_subscribe_response import SapiV1SimpleEarnLockedSubscribeResponse
from ..models.sapi_v1_simple_earn_locked_subscription_preview_response import (
    SapiV1SimpleEarnLockedSubscriptionPreviewResponse,
)
from ..server.server import Server


class SimpleEarn:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SimpleEarnWithRawResponse(client, server, auth)

    def get_collateral_record_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        product_id: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnFlexibleHistoryCollateralRecordResponse:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            product_id: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Collateral Record

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_collateral_record_user_data(
            timestamp,
            signature,
            product_id=product_id,
            start_time=start_time,
            end_time=end_time,
            current=current,
            size=size,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_flexible_personal_left_quota_user_data(
        self,
        product_id: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnFlexiblePersonalLeftQuotaResponse:
        """Weight(IP): 150

        Args:
            product_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Flexible Personal Left Quota

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_flexible_personal_left_quota_user_data(
            product_id, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def get_flexible_product_position_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        product_id: str | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnFlexiblePositionResponse:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            product_id: Value sent with the request.
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Flexible Product Position

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_flexible_product_position_user_data(
            timestamp,
            signature,
            asset=asset,
            product_id=product_id,
            current=current,
            size=size,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_flexible_redemption_record_user_data(
        self,
        *,
        product_id: str | None = None,
        redeem_id: str | None = None,
        asset: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnFlexibleHistoryRedemptionRecordResponse:
        """Weight(IP): 150

        Args:
            product_id: Value sent with the request.
            redeem_id: Value sent with the request.
            asset: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Flexible Redemption Record

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_flexible_redemption_record_user_data(
            product_id=product_id,
            redeem_id=redeem_id,
            asset=asset,
            start_time=start_time,
            end_time=end_time,
            current=current,
            size=size,
            request_options=request_options,
        ).unwrap()

    def get_flexible_rewards_history_user_data(
        self,
        type_: str,
        *,
        product_id: str | None = None,
        asset: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnFlexibleHistoryRewardsRecordResponse:
        """Weight(IP): 150

        Args:
            type_: "BONUS", "REALTIME", "REWARDS"
            product_id: Value sent with the request.
            asset: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Flexible Rewards History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_flexible_rewards_history_user_data(
            type_,
            product_id=product_id,
            asset=asset,
            start_time=start_time,
            end_time=end_time,
            request_options=request_options,
        ).unwrap()

    def get_flexible_subscription_preview_user_data(
        self,
        product_id: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnFlexibleSubscriptionPreviewResponse:
        """Weight(IP): 150

        Args:
            product_id: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Flexible Subscription Preview

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_flexible_subscription_preview_user_data(
            product_id, amount, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def get_flexible_subscription_record_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        product_id: str | None = None,
        purchase_id: str | None = None,
        asset: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnFlexibleHistorySubscriptionRecordResponse:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            product_id: Value sent with the request.
            purchase_id: Value sent with the request.
            asset: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Flexible Product Position

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_flexible_subscription_record_user_data(
            timestamp,
            signature,
            product_id=product_id,
            purchase_id=purchase_id,
            asset=asset,
            start_time=start_time,
            end_time=end_time,
            current=current,
            size=size,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_locked_personal_left_quota_user_data(
        self,
        project_id: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnLockedPersonalLeftQuotaResponse:
        """Weight(IP): 150

        Args:
            project_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Locked Personal Left Quota

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_locked_personal_left_quota_user_data(
            project_id, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def get_locked_product_position_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        position_id: str | None = None,
        project_id: str | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnLockedPositionResponse:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            position_id: Value sent with the request.
            project_id: Value sent with the request.
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Locked Product Position

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_locked_product_position_user_data(
            timestamp,
            signature,
            asset=asset,
            position_id=position_id,
            project_id=project_id,
            current=current,
            size=size,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_locked_redemption_record_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        position_id: str | None = None,
        redeem_id: str | None = None,
        asset: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnLockedHistoryRedemptionRecordResponse:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            position_id: Value sent with the request.
            redeem_id: Value sent with the request.
            asset: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Locked Redemption Record

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_locked_redemption_record_user_data(
            timestamp,
            signature,
            position_id=position_id,
            redeem_id=redeem_id,
            asset=asset,
            start_time=start_time,
            end_time=end_time,
            current=current,
            size=size,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_locked_rewards_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        position_id: str | None = None,
        asset: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnLockedHistoryRewardsRecordResponse:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            position_id: Value sent with the request.
            asset: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Locked Rewards History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_locked_rewards_history_user_data(
            timestamp,
            signature,
            position_id=position_id,
            asset=asset,
            start_time=start_time,
            end_time=end_time,
            size=size,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_locked_subscription_preview_user_data(
        self,
        project_id: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        auto_subscribe: bool | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1SimpleEarnLockedSubscriptionPreviewResponse]:
        """Weight(IP): 150

        Args:
            project_id: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            auto_subscribe: true or false, default true.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Locked Product Subscription Response

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_locked_subscription_preview_user_data(
            project_id,
            amount,
            timestamp,
            signature,
            auto_subscribe=auto_subscribe,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_locked_subscription_record_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        purchase_id: str | None = None,
        asset: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnLockedHistorySubscriptionRecordResponse:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            purchase_id: Value sent with the request.
            asset: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Locked Subscription Record

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_locked_subscription_record_user_data(
            timestamp,
            signature,
            purchase_id=purchase_id,
            asset=asset,
            start_time=start_time,
            end_time=end_time,
            current=current,
            size=size,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_rate_history_user_data(
        self,
        product_id: str,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnFlexibleHistoryRateHistoryResponse:
        """Weight(IP): 150

        Args:
            product_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Rate History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_rate_history_user_data(
            product_id,
            timestamp,
            signature,
            start_time=start_time,
            end_time=end_time,
            current=current,
            size=size,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_simple_earn_flexible_product_list_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnFlexibleListResponse:
        """Get available Simple Earn flexible product list

        Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Simple Earn Flexible Product List

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_simple_earn_flexible_product_list_user_data(
            timestamp,
            signature,
            asset=asset,
            current=current,
            size=size,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_simple_earn_locked_product_list_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnLockedListResponse:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Simple Earn Locked Product List

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_simple_earn_locked_product_list_user_data(
            timestamp,
            signature,
            asset=asset,
            current=current,
            size=size,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def redeem_flexible_product_trade(
        self,
        product_id: str,
        timestamp: int,
        signature: str,
        *,
        redeem_all: bool | None = None,
        amount: float | None = None,
        dest_account: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnFlexibleRedeemResponse:
        """Weight(IP): 1

        Rate Limit: 1/3s per account

        Args:
            product_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            redeem_all: true or false, default to false
            amount: if redeemAll is false, amount is mandatory
            dest_account: SPOT,FUND,ALL, default SPOT
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Redeem Flexible Product

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.redeem_flexible_product_trade(
            product_id,
            timestamp,
            signature,
            redeem_all=redeem_all,
            amount=amount,
            dest_account=dest_account,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def redeem_locked_product_trade(
        self,
        position_id: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnLockedRedeemResponse:
        """Weight(IP): 1

        Rate Limit: 1/3s per account

        Args:
            position_id: 1234
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Redeem Locked Product

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.redeem_locked_product_trade(
            position_id, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def set_flexible_auto_subscribe_user_data(
        self,
        product_id: str,
        auto_subscribe: bool,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnFlexibleSetAutoSubscribeResponse:
        """Weight(IP): 150

        Args:
            product_id: Value sent with the request.
            auto_subscribe: true or false
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Flexible Product Subscription Response

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.set_flexible_auto_subscribe_user_data(
            product_id, auto_subscribe, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def set_locked_auto_subscribe_user_data(
        self,
        position_id: str,
        auto_subscribe: bool,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnLockedSetAutoSubscribeResponse:
        """Weight(IP): 150

        Args:
            position_id: Value sent with the request.
            auto_subscribe: true or false
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Locked Auto Subscribe

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.set_locked_auto_subscribe_user_data(
            position_id, auto_subscribe, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def set_locked_product_redeem_option_user_data(
        self,
        position_id: str,
        timestamp: int,
        signature: str,
        *,
        redeem_to: RedeemToOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnLockedSetRedeemOptionResponse:
        """Set redeem option for Locked product

        Weight(IP): 50

        Args:
            position_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            redeem_to: SPOT,FLEXIBLE, default FLEXIBLE
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Locked Product Redeem Option

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.set_locked_product_redeem_option_user_data(
            position_id,
            timestamp,
            signature,
            redeem_to=redeem_to,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def simple_account_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnAccountResponse:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Account Information

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.simple_account_user_data(
            timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def subscribe_flexible_product_trade(
        self,
        product_id: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        auto_subscribe: bool | None = None,
        source_account: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnFlexibleSubscribeResponse:
        """Weight(IP): 1

        Rate Limit: 1/3s per account

        Args:
            product_id: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            auto_subscribe: true or false, default true.
            source_account: SPOT,FUND,ALL, default SPOT
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Flexible Product Subscription Response

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.subscribe_flexible_product_trade(
            product_id,
            amount,
            timestamp,
            signature,
            auto_subscribe=auto_subscribe,
            source_account=source_account,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def subscribe_locked_product_trade(
        self,
        project_id: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        auto_subscribe: bool | None = None,
        source_account: str | None = None,
        redeem_to: RedeemToOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnLockedSubscribeResponse:
        """Weight(IP): 1

        Rate Limit: 1/3s per account

        Args:
            project_id: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            auto_subscribe: true or false, default true.
            source_account: SPOT,FUND,ALL, default SPOT
            redeem_to: SPOT,FLEXIBLE, default FLEXIBLE
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Locked Product Subscription Response

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.subscribe_locked_product_trade(
            project_id,
            amount,
            timestamp,
            signature,
            auto_subscribe=auto_subscribe,
            source_account=source_account,
            redeem_to=redeem_to,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> SimpleEarnWithRawResponse:
        return self._with_raw_response


class AsyncSimpleEarn:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSimpleEarnWithRawResponse(client, server, auth)

    async def get_collateral_record_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        product_id: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnFlexibleHistoryCollateralRecordResponse:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            product_id: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Collateral Record

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_collateral_record_user_data(
                timestamp,
                signature,
                product_id=product_id,
                start_time=start_time,
                end_time=end_time,
                current=current,
                size=size,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def get_flexible_personal_left_quota_user_data(
        self,
        product_id: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnFlexiblePersonalLeftQuotaResponse:
        """Weight(IP): 150

        Args:
            product_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Flexible Personal Left Quota

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_flexible_personal_left_quota_user_data(
                product_id, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def get_flexible_product_position_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        product_id: str | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnFlexiblePositionResponse:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            product_id: Value sent with the request.
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Flexible Product Position

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_flexible_product_position_user_data(
                timestamp,
                signature,
                asset=asset,
                product_id=product_id,
                current=current,
                size=size,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def get_flexible_redemption_record_user_data(
        self,
        *,
        product_id: str | None = None,
        redeem_id: str | None = None,
        asset: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnFlexibleHistoryRedemptionRecordResponse:
        """Weight(IP): 150

        Args:
            product_id: Value sent with the request.
            redeem_id: Value sent with the request.
            asset: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Flexible Redemption Record

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_flexible_redemption_record_user_data(
                product_id=product_id,
                redeem_id=redeem_id,
                asset=asset,
                start_time=start_time,
                end_time=end_time,
                current=current,
                size=size,
                request_options=request_options,
            )
        ).unwrap()

    async def get_flexible_rewards_history_user_data(
        self,
        type_: str,
        *,
        product_id: str | None = None,
        asset: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnFlexibleHistoryRewardsRecordResponse:
        """Weight(IP): 150

        Args:
            type_: "BONUS", "REALTIME", "REWARDS"
            product_id: Value sent with the request.
            asset: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Flexible Rewards History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_flexible_rewards_history_user_data(
                type_,
                product_id=product_id,
                asset=asset,
                start_time=start_time,
                end_time=end_time,
                request_options=request_options,
            )
        ).unwrap()

    async def get_flexible_subscription_preview_user_data(
        self,
        product_id: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnFlexibleSubscriptionPreviewResponse:
        """Weight(IP): 150

        Args:
            product_id: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Flexible Subscription Preview

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_flexible_subscription_preview_user_data(
                product_id, amount, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def get_flexible_subscription_record_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        product_id: str | None = None,
        purchase_id: str | None = None,
        asset: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnFlexibleHistorySubscriptionRecordResponse:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            product_id: Value sent with the request.
            purchase_id: Value sent with the request.
            asset: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Flexible Product Position

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_flexible_subscription_record_user_data(
                timestamp,
                signature,
                product_id=product_id,
                purchase_id=purchase_id,
                asset=asset,
                start_time=start_time,
                end_time=end_time,
                current=current,
                size=size,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def get_locked_personal_left_quota_user_data(
        self,
        project_id: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnLockedPersonalLeftQuotaResponse:
        """Weight(IP): 150

        Args:
            project_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Locked Personal Left Quota

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_locked_personal_left_quota_user_data(
                project_id, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def get_locked_product_position_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        position_id: str | None = None,
        project_id: str | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnLockedPositionResponse:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            position_id: Value sent with the request.
            project_id: Value sent with the request.
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Locked Product Position

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_locked_product_position_user_data(
                timestamp,
                signature,
                asset=asset,
                position_id=position_id,
                project_id=project_id,
                current=current,
                size=size,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def get_locked_redemption_record_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        position_id: str | None = None,
        redeem_id: str | None = None,
        asset: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnLockedHistoryRedemptionRecordResponse:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            position_id: Value sent with the request.
            redeem_id: Value sent with the request.
            asset: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Locked Redemption Record

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_locked_redemption_record_user_data(
                timestamp,
                signature,
                position_id=position_id,
                redeem_id=redeem_id,
                asset=asset,
                start_time=start_time,
                end_time=end_time,
                current=current,
                size=size,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def get_locked_rewards_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        position_id: str | None = None,
        asset: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnLockedHistoryRewardsRecordResponse:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            position_id: Value sent with the request.
            asset: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Locked Rewards History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_locked_rewards_history_user_data(
                timestamp,
                signature,
                position_id=position_id,
                asset=asset,
                start_time=start_time,
                end_time=end_time,
                size=size,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def get_locked_subscription_preview_user_data(
        self,
        project_id: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        auto_subscribe: bool | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1SimpleEarnLockedSubscriptionPreviewResponse]:
        """Weight(IP): 150

        Args:
            project_id: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            auto_subscribe: true or false, default true.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Locked Product Subscription Response

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_locked_subscription_preview_user_data(
                project_id,
                amount,
                timestamp,
                signature,
                auto_subscribe=auto_subscribe,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def get_locked_subscription_record_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        purchase_id: str | None = None,
        asset: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnLockedHistorySubscriptionRecordResponse:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            purchase_id: Value sent with the request.
            asset: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Locked Subscription Record

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_locked_subscription_record_user_data(
                timestamp,
                signature,
                purchase_id=purchase_id,
                asset=asset,
                start_time=start_time,
                end_time=end_time,
                current=current,
                size=size,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def get_rate_history_user_data(
        self,
        product_id: str,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnFlexibleHistoryRateHistoryResponse:
        """Weight(IP): 150

        Args:
            product_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Rate History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_rate_history_user_data(
                product_id,
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

    async def get_simple_earn_flexible_product_list_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnFlexibleListResponse:
        """Get available Simple Earn flexible product list

        Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Simple Earn Flexible Product List

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_simple_earn_flexible_product_list_user_data(
                timestamp,
                signature,
                asset=asset,
                current=current,
                size=size,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def get_simple_earn_locked_product_list_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnLockedListResponse:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Simple Earn Locked Product List

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_simple_earn_locked_product_list_user_data(
                timestamp,
                signature,
                asset=asset,
                current=current,
                size=size,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def redeem_flexible_product_trade(
        self,
        product_id: str,
        timestamp: int,
        signature: str,
        *,
        redeem_all: bool | None = None,
        amount: float | None = None,
        dest_account: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnFlexibleRedeemResponse:
        """Weight(IP): 1

        Rate Limit: 1/3s per account

        Args:
            product_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            redeem_all: true or false, default to false
            amount: if redeemAll is false, amount is mandatory
            dest_account: SPOT,FUND,ALL, default SPOT
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Redeem Flexible Product

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.redeem_flexible_product_trade(
                product_id,
                timestamp,
                signature,
                redeem_all=redeem_all,
                amount=amount,
                dest_account=dest_account,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def redeem_locked_product_trade(
        self,
        position_id: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnLockedRedeemResponse:
        """Weight(IP): 1

        Rate Limit: 1/3s per account

        Args:
            position_id: 1234
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Redeem Locked Product

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.redeem_locked_product_trade(
                position_id, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def set_flexible_auto_subscribe_user_data(
        self,
        product_id: str,
        auto_subscribe: bool,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnFlexibleSetAutoSubscribeResponse:
        """Weight(IP): 150

        Args:
            product_id: Value sent with the request.
            auto_subscribe: true or false
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Flexible Product Subscription Response

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.set_flexible_auto_subscribe_user_data(
                product_id,
                auto_subscribe,
                timestamp,
                signature,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def set_locked_auto_subscribe_user_data(
        self,
        position_id: str,
        auto_subscribe: bool,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnLockedSetAutoSubscribeResponse:
        """Weight(IP): 150

        Args:
            position_id: Value sent with the request.
            auto_subscribe: true or false
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Locked Auto Subscribe

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.set_locked_auto_subscribe_user_data(
                position_id,
                auto_subscribe,
                timestamp,
                signature,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def set_locked_product_redeem_option_user_data(
        self,
        position_id: str,
        timestamp: int,
        signature: str,
        *,
        redeem_to: RedeemToOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnLockedSetRedeemOptionResponse:
        """Set redeem option for Locked product

        Weight(IP): 50

        Args:
            position_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            redeem_to: SPOT,FLEXIBLE, default FLEXIBLE
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Locked Product Redeem Option

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.set_locked_product_redeem_option_user_data(
                position_id,
                timestamp,
                signature,
                redeem_to=redeem_to,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def simple_account_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnAccountResponse:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Account Information

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.simple_account_user_data(
                timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def subscribe_flexible_product_trade(
        self,
        product_id: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        auto_subscribe: bool | None = None,
        source_account: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnFlexibleSubscribeResponse:
        """Weight(IP): 1

        Rate Limit: 1/3s per account

        Args:
            product_id: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            auto_subscribe: true or false, default true.
            source_account: SPOT,FUND,ALL, default SPOT
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Flexible Product Subscription Response

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.subscribe_flexible_product_trade(
                product_id,
                amount,
                timestamp,
                signature,
                auto_subscribe=auto_subscribe,
                source_account=source_account,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def subscribe_locked_product_trade(
        self,
        project_id: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        auto_subscribe: bool | None = None,
        source_account: str | None = None,
        redeem_to: RedeemToOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SimpleEarnLockedSubscribeResponse:
        """Weight(IP): 1

        Rate Limit: 1/3s per account

        Args:
            project_id: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            auto_subscribe: true or false, default true.
            source_account: SPOT,FUND,ALL, default SPOT
            redeem_to: SPOT,FLEXIBLE, default FLEXIBLE
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Locked Product Subscription Response

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.subscribe_locked_product_trade(
                project_id,
                amount,
                timestamp,
                signature,
                auto_subscribe=auto_subscribe,
                source_account=source_account,
                redeem_to=redeem_to,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSimpleEarnWithRawResponse:
        return self._with_raw_response


class SimpleEarnWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_collateral_record_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        product_id: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SimpleEarnFlexibleHistoryCollateralRecordResponse, GetCollateralRecordUserDataErrorBody]:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            product_id: Value sent with the request.
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
            url_template=self._server.default("/sapi/v1/simple-earn/flexible/history/collateralRecord"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("productId", product_id),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnFlexibleHistoryCollateralRecordResponse],
            error_mapper=get_collateral_record_user_data_error_mapper,
            request_options=request_options,
        )

    def get_flexible_personal_left_quota_user_data(
        self,
        product_id: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SimpleEarnFlexiblePersonalLeftQuotaResponse, GetFlexiblePersonalLeftQuotaUserDataErrorBody]:
        """Weight(IP): 150

        Args:
            product_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/simple-earn/flexible/personalLeftQuota"),
            query_params=[
                param[str]("productId", product_id),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnFlexiblePersonalLeftQuotaResponse],
            error_mapper=get_flexible_personal_left_quota_user_data_error_mapper,
            request_options=request_options,
        )

    def get_flexible_product_position_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        product_id: str | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SimpleEarnFlexiblePositionResponse, GetFlexibleProductPositionUserDataErrorBody]:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            product_id: Value sent with the request.
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/simple-earn/flexible/position"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("asset", asset),
                param[str | None]("productId", product_id),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnFlexiblePositionResponse],
            error_mapper=get_flexible_product_position_user_data_error_mapper,
            request_options=request_options,
        )

    def get_flexible_redemption_record_user_data(
        self,
        *,
        product_id: str | None = None,
        redeem_id: str | None = None,
        asset: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1SimpleEarnFlexibleHistoryRedemptionRecordResponse, GetFlexibleRedemptionRecordUserDataErrorBody
    ]:
        """Weight(IP): 150

        Args:
            product_id: Value sent with the request.
            redeem_id: Value sent with the request.
            asset: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/simple-earn/flexible/history/redemptionRecord"),
            query_params=[
                param[str | None]("productId", product_id),
                param[str | None]("redeemId", redeem_id),
                param[str | None]("asset", asset),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[int | None]("size", size),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnFlexibleHistoryRedemptionRecordResponse],
            error_mapper=get_flexible_redemption_record_user_data_error_mapper,
            request_options=request_options,
        )

    def get_flexible_rewards_history_user_data(
        self,
        type_: str,
        *,
        product_id: str | None = None,
        asset: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SimpleEarnFlexibleHistoryRewardsRecordResponse, GetFlexibleRewardsHistoryUserDataErrorBody]:
        """Weight(IP): 150

        Args:
            type_: "BONUS", "REALTIME", "REWARDS"
            product_id: Value sent with the request.
            asset: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/simple-earn/flexible/history/rewardsRecord"),
            query_params=[
                param[str]("type", type_),
                param[str | None]("productId", product_id),
                param[str | None]("asset", asset),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnFlexibleHistoryRewardsRecordResponse],
            error_mapper=get_flexible_rewards_history_user_data_error_mapper,
            request_options=request_options,
        )

    def get_flexible_subscription_preview_user_data(
        self,
        product_id: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1SimpleEarnFlexibleSubscriptionPreviewResponse, GetFlexibleSubscriptionPreviewUserDataErrorBody
    ]:
        """Weight(IP): 150

        Args:
            product_id: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/simple-earn/flexible/subscriptionPreview"),
            query_params=[
                param[str]("productId", product_id),
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnFlexibleSubscriptionPreviewResponse],
            error_mapper=get_flexible_subscription_preview_user_data_error_mapper,
            request_options=request_options,
        )

    def get_flexible_subscription_record_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        product_id: str | None = None,
        purchase_id: str | None = None,
        asset: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1SimpleEarnFlexibleHistorySubscriptionRecordResponse, GetFlexibleSubscriptionRecordUserDataErrorBody
    ]:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            product_id: Value sent with the request.
            purchase_id: Value sent with the request.
            asset: Value sent with the request.
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
            url_template=self._server.default("/sapi/v1/simple-earn/flexible/history/subscriptionRecord"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("productId", product_id),
                param[str | None]("purchaseId", purchase_id),
                param[str | None]("asset", asset),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnFlexibleHistorySubscriptionRecordResponse],
            error_mapper=get_flexible_subscription_record_user_data_error_mapper,
            request_options=request_options,
        )

    def get_locked_personal_left_quota_user_data(
        self,
        project_id: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SimpleEarnLockedPersonalLeftQuotaResponse, GetLockedPersonalLeftQuotaUserDataErrorBody]:
        """Weight(IP): 150

        Args:
            project_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/simple-earn/locked/personalLeftQuota"),
            query_params=[
                param[str]("projectId", project_id),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnLockedPersonalLeftQuotaResponse],
            error_mapper=get_locked_personal_left_quota_user_data_error_mapper,
            request_options=request_options,
        )

    def get_locked_product_position_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        position_id: str | None = None,
        project_id: str | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SimpleEarnLockedPositionResponse, GetLockedProductPositionUserDataErrorBody]:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            position_id: Value sent with the request.
            project_id: Value sent with the request.
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/simple-earn/locked/position"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("asset", asset),
                param[str | None]("positionId", position_id),
                param[str | None]("projectId", project_id),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnLockedPositionResponse],
            error_mapper=get_locked_product_position_user_data_error_mapper,
            request_options=request_options,
        )

    def get_locked_redemption_record_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        position_id: str | None = None,
        redeem_id: str | None = None,
        asset: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SimpleEarnLockedHistoryRedemptionRecordResponse, GetLockedRedemptionRecordUserDataErrorBody]:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            position_id: Value sent with the request.
            redeem_id: Value sent with the request.
            asset: Value sent with the request.
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
            url_template=self._server.default("/sapi/v1/simple-earn/locked/history/redemptionRecord"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("positionId", position_id),
                param[str | None]("redeemId", redeem_id),
                param[str | None]("asset", asset),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnLockedHistoryRedemptionRecordResponse],
            error_mapper=get_locked_redemption_record_user_data_error_mapper,
            request_options=request_options,
        )

    def get_locked_rewards_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        position_id: str | None = None,
        asset: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SimpleEarnLockedHistoryRewardsRecordResponse, GetLockedRewardsHistoryUserDataErrorBody]:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            position_id: Value sent with the request.
            asset: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/simple-earn/locked/history/rewardsRecord"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("positionId", position_id),
                param[str | None]("asset", asset),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnLockedHistoryRewardsRecordResponse],
            error_mapper=get_locked_rewards_history_user_data_error_mapper,
            request_options=request_options,
        )

    def get_locked_subscription_preview_user_data(
        self,
        project_id: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        auto_subscribe: bool | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        list[SapiV1SimpleEarnLockedSubscriptionPreviewResponse], GetLockedSubscriptionPreviewUserDataErrorBody
    ]:
        """Weight(IP): 150

        Args:
            project_id: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            auto_subscribe: true or false, default true.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/simple-earn/locked/subscriptionPreview"),
            query_params=[
                param[str]("projectId", project_id),
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[bool | None]("autoSubscribe", auto_subscribe),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1SimpleEarnLockedSubscriptionPreviewResponse]],
            error_mapper=get_locked_subscription_preview_user_data_error_mapper,
            request_options=request_options,
        )

    def get_locked_subscription_record_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        purchase_id: str | None = None,
        asset: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1SimpleEarnLockedHistorySubscriptionRecordResponse, GetLockedSubscriptionRecordUserDataErrorBody
    ]:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            purchase_id: Value sent with the request.
            asset: Value sent with the request.
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
            url_template=self._server.default("/sapi/v1/simple-earn/locked/history/subscriptionRecord"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("purchaseId", purchase_id),
                param[str | None]("asset", asset),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnLockedHistorySubscriptionRecordResponse],
            error_mapper=get_locked_subscription_record_user_data_error_mapper,
            request_options=request_options,
        )

    def get_rate_history_user_data(
        self,
        product_id: str,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SimpleEarnFlexibleHistoryRateHistoryResponse, GetRateHistoryUserDataErrorBody]:
        """Weight(IP): 150

        Args:
            product_id: Value sent with the request.
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
            url_template=self._server.default("/sapi/v1/simple-earn/flexible/history/rateHistory"),
            query_params=[
                param[str]("productId", product_id),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnFlexibleHistoryRateHistoryResponse],
            error_mapper=get_rate_history_user_data_error_mapper,
            request_options=request_options,
        )

    def get_simple_earn_flexible_product_list_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SimpleEarnFlexibleListResponse, GetSimpleEarnFlexibleProductListUserDataErrorBody]:
        """Get available Simple Earn flexible product list

        Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/simple-earn/flexible/list"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("asset", asset),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnFlexibleListResponse],
            error_mapper=get_simple_earn_flexible_product_list_user_data_error_mapper,
            request_options=request_options,
        )

    def get_simple_earn_locked_product_list_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SimpleEarnLockedListResponse, GetSimpleEarnLockedProductListUserDataErrorBody]:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/simple-earn/locked/list"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("asset", asset),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnLockedListResponse],
            error_mapper=get_simple_earn_locked_product_list_user_data_error_mapper,
            request_options=request_options,
        )

    def redeem_flexible_product_trade(
        self,
        product_id: str,
        timestamp: int,
        signature: str,
        *,
        redeem_all: bool | None = None,
        amount: float | None = None,
        dest_account: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SimpleEarnFlexibleRedeemResponse, RedeemFlexibleProductTradeErrorBody]:
        """Weight(IP): 1

        Rate Limit: 1/3s per account

        Args:
            product_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            redeem_all: true or false, default to false
            amount: if redeemAll is false, amount is mandatory
            dest_account: SPOT,FUND,ALL, default SPOT
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/simple-earn/flexible/redeem"),
            query_params=[
                param[str]("productId", product_id),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[bool | None]("redeemAll", redeem_all),
                param[float | None]("amount", amount),
                param[str | None]("destAccount", dest_account),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnFlexibleRedeemResponse],
            error_mapper=redeem_flexible_product_trade_error_mapper,
            request_options=request_options,
        )

    def redeem_locked_product_trade(
        self,
        position_id: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SimpleEarnLockedRedeemResponse, RedeemLockedProductTradeErrorBody]:
        """Weight(IP): 1

        Rate Limit: 1/3s per account

        Args:
            position_id: 1234
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/simple-earn/locked/redeem"),
            query_params=[
                param[str]("positionId", position_id),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnLockedRedeemResponse],
            error_mapper=redeem_locked_product_trade_error_mapper,
            request_options=request_options,
        )

    def set_flexible_auto_subscribe_user_data(
        self,
        product_id: str,
        auto_subscribe: bool,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SimpleEarnFlexibleSetAutoSubscribeResponse, SetFlexibleAutoSubscribeUserDataErrorBody]:
        """Weight(IP): 150

        Args:
            product_id: Value sent with the request.
            auto_subscribe: true or false
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/simple-earn/flexible/setAutoSubscribe"),
            query_params=[
                param[str]("productId", product_id),
                param[bool]("autoSubscribe", auto_subscribe),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnFlexibleSetAutoSubscribeResponse],
            error_mapper=set_flexible_auto_subscribe_user_data_error_mapper,
            request_options=request_options,
        )

    def set_locked_auto_subscribe_user_data(
        self,
        position_id: str,
        auto_subscribe: bool,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SimpleEarnLockedSetAutoSubscribeResponse, SetLockedAutoSubscribeUserDataErrorBody]:
        """Weight(IP): 150

        Args:
            position_id: Value sent with the request.
            auto_subscribe: true or false
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/simple-earn/locked/setAutoSubscribe"),
            query_params=[
                param[str]("positionId", position_id),
                param[bool]("autoSubscribe", auto_subscribe),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnLockedSetAutoSubscribeResponse],
            error_mapper=set_locked_auto_subscribe_user_data_error_mapper,
            request_options=request_options,
        )

    def set_locked_product_redeem_option_user_data(
        self,
        position_id: str,
        timestamp: int,
        signature: str,
        *,
        redeem_to: RedeemToOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SimpleEarnLockedSetRedeemOptionResponse, SetLockedProductRedeemOptionUserDataErrorBody]:
        """Set redeem option for Locked product

        Weight(IP): 50

        Args:
            position_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            redeem_to: SPOT,FLEXIBLE, default FLEXIBLE
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/simple-earn/locked/setRedeemOption"),
            query_params=[
                param[str]("positionId", position_id),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[RedeemToOrStr | None]("redeemTo", redeem_to),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnLockedSetRedeemOptionResponse],
            error_mapper=set_locked_product_redeem_option_user_data_error_mapper,
            request_options=request_options,
        )

    def simple_account_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SimpleEarnAccountResponse, SimpleAccountUserDataErrorBody]:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/simple-earn/account"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnAccountResponse],
            error_mapper=simple_account_user_data_error_mapper,
            request_options=request_options,
        )

    def subscribe_flexible_product_trade(
        self,
        product_id: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        auto_subscribe: bool | None = None,
        source_account: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SimpleEarnFlexibleSubscribeResponse, SubscribeFlexibleProductTradeErrorBody]:
        """Weight(IP): 1

        Rate Limit: 1/3s per account

        Args:
            product_id: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            auto_subscribe: true or false, default true.
            source_account: SPOT,FUND,ALL, default SPOT
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/simple-earn/flexible/subscribe"),
            query_params=[
                param[str]("productId", product_id),
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[bool | None]("autoSubscribe", auto_subscribe),
                param[str | None]("sourceAccount", source_account),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnFlexibleSubscribeResponse],
            error_mapper=subscribe_flexible_product_trade_error_mapper,
            request_options=request_options,
        )

    def subscribe_locked_product_trade(
        self,
        project_id: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        auto_subscribe: bool | None = None,
        source_account: str | None = None,
        redeem_to: RedeemToOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SimpleEarnLockedSubscribeResponse, SubscribeLockedProductTradeErrorBody]:
        """Weight(IP): 1

        Rate Limit: 1/3s per account

        Args:
            project_id: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            auto_subscribe: true or false, default true.
            source_account: SPOT,FUND,ALL, default SPOT
            redeem_to: SPOT,FLEXIBLE, default FLEXIBLE
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/simple-earn/locked/subscribe"),
            query_params=[
                param[str]("projectId", project_id),
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[bool | None]("autoSubscribe", auto_subscribe),
                param[str | None]("sourceAccount", source_account),
                param[RedeemToOrStr | None]("redeemTo", redeem_to),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnLockedSubscribeResponse],
            error_mapper=subscribe_locked_product_trade_error_mapper,
            request_options=request_options,
        )


class AsyncSimpleEarnWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_collateral_record_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        product_id: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SimpleEarnFlexibleHistoryCollateralRecordResponse, GetCollateralRecordUserDataErrorBody]:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            product_id: Value sent with the request.
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
            url_template=self._server.default("/sapi/v1/simple-earn/flexible/history/collateralRecord"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("productId", product_id),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnFlexibleHistoryCollateralRecordResponse],
            error_mapper=get_collateral_record_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_flexible_personal_left_quota_user_data(
        self,
        product_id: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SimpleEarnFlexiblePersonalLeftQuotaResponse, GetFlexiblePersonalLeftQuotaUserDataErrorBody]:
        """Weight(IP): 150

        Args:
            product_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/simple-earn/flexible/personalLeftQuota"),
            query_params=[
                param[str]("productId", product_id),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnFlexiblePersonalLeftQuotaResponse],
            error_mapper=get_flexible_personal_left_quota_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_flexible_product_position_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        product_id: str | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SimpleEarnFlexiblePositionResponse, GetFlexibleProductPositionUserDataErrorBody]:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            product_id: Value sent with the request.
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/simple-earn/flexible/position"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("asset", asset),
                param[str | None]("productId", product_id),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnFlexiblePositionResponse],
            error_mapper=get_flexible_product_position_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_flexible_redemption_record_user_data(
        self,
        *,
        product_id: str | None = None,
        redeem_id: str | None = None,
        asset: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1SimpleEarnFlexibleHistoryRedemptionRecordResponse, GetFlexibleRedemptionRecordUserDataErrorBody
    ]:
        """Weight(IP): 150

        Args:
            product_id: Value sent with the request.
            redeem_id: Value sent with the request.
            asset: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/simple-earn/flexible/history/redemptionRecord"),
            query_params=[
                param[str | None]("productId", product_id),
                param[str | None]("redeemId", redeem_id),
                param[str | None]("asset", asset),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[int | None]("size", size),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnFlexibleHistoryRedemptionRecordResponse],
            error_mapper=get_flexible_redemption_record_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_flexible_rewards_history_user_data(
        self,
        type_: str,
        *,
        product_id: str | None = None,
        asset: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SimpleEarnFlexibleHistoryRewardsRecordResponse, GetFlexibleRewardsHistoryUserDataErrorBody]:
        """Weight(IP): 150

        Args:
            type_: "BONUS", "REALTIME", "REWARDS"
            product_id: Value sent with the request.
            asset: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/simple-earn/flexible/history/rewardsRecord"),
            query_params=[
                param[str]("type", type_),
                param[str | None]("productId", product_id),
                param[str | None]("asset", asset),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnFlexibleHistoryRewardsRecordResponse],
            error_mapper=get_flexible_rewards_history_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_flexible_subscription_preview_user_data(
        self,
        product_id: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1SimpleEarnFlexibleSubscriptionPreviewResponse, GetFlexibleSubscriptionPreviewUserDataErrorBody
    ]:
        """Weight(IP): 150

        Args:
            product_id: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/simple-earn/flexible/subscriptionPreview"),
            query_params=[
                param[str]("productId", product_id),
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnFlexibleSubscriptionPreviewResponse],
            error_mapper=get_flexible_subscription_preview_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_flexible_subscription_record_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        product_id: str | None = None,
        purchase_id: str | None = None,
        asset: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1SimpleEarnFlexibleHistorySubscriptionRecordResponse, GetFlexibleSubscriptionRecordUserDataErrorBody
    ]:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            product_id: Value sent with the request.
            purchase_id: Value sent with the request.
            asset: Value sent with the request.
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
            url_template=self._server.default("/sapi/v1/simple-earn/flexible/history/subscriptionRecord"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("productId", product_id),
                param[str | None]("purchaseId", purchase_id),
                param[str | None]("asset", asset),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnFlexibleHistorySubscriptionRecordResponse],
            error_mapper=get_flexible_subscription_record_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_locked_personal_left_quota_user_data(
        self,
        project_id: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SimpleEarnLockedPersonalLeftQuotaResponse, GetLockedPersonalLeftQuotaUserDataErrorBody]:
        """Weight(IP): 150

        Args:
            project_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/simple-earn/locked/personalLeftQuota"),
            query_params=[
                param[str]("projectId", project_id),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnLockedPersonalLeftQuotaResponse],
            error_mapper=get_locked_personal_left_quota_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_locked_product_position_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        position_id: str | None = None,
        project_id: str | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SimpleEarnLockedPositionResponse, GetLockedProductPositionUserDataErrorBody]:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            position_id: Value sent with the request.
            project_id: Value sent with the request.
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/simple-earn/locked/position"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("asset", asset),
                param[str | None]("positionId", position_id),
                param[str | None]("projectId", project_id),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnLockedPositionResponse],
            error_mapper=get_locked_product_position_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_locked_redemption_record_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        position_id: str | None = None,
        redeem_id: str | None = None,
        asset: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SimpleEarnLockedHistoryRedemptionRecordResponse, GetLockedRedemptionRecordUserDataErrorBody]:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            position_id: Value sent with the request.
            redeem_id: Value sent with the request.
            asset: Value sent with the request.
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
            url_template=self._server.default("/sapi/v1/simple-earn/locked/history/redemptionRecord"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("positionId", position_id),
                param[str | None]("redeemId", redeem_id),
                param[str | None]("asset", asset),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnLockedHistoryRedemptionRecordResponse],
            error_mapper=get_locked_redemption_record_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_locked_rewards_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        position_id: str | None = None,
        asset: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SimpleEarnLockedHistoryRewardsRecordResponse, GetLockedRewardsHistoryUserDataErrorBody]:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            position_id: Value sent with the request.
            asset: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/simple-earn/locked/history/rewardsRecord"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("positionId", position_id),
                param[str | None]("asset", asset),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnLockedHistoryRewardsRecordResponse],
            error_mapper=get_locked_rewards_history_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_locked_subscription_preview_user_data(
        self,
        project_id: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        auto_subscribe: bool | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        list[SapiV1SimpleEarnLockedSubscriptionPreviewResponse], GetLockedSubscriptionPreviewUserDataErrorBody
    ]:
        """Weight(IP): 150

        Args:
            project_id: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            auto_subscribe: true or false, default true.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/simple-earn/locked/subscriptionPreview"),
            query_params=[
                param[str]("projectId", project_id),
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[bool | None]("autoSubscribe", auto_subscribe),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1SimpleEarnLockedSubscriptionPreviewResponse]],
            error_mapper=get_locked_subscription_preview_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_locked_subscription_record_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        purchase_id: str | None = None,
        asset: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1SimpleEarnLockedHistorySubscriptionRecordResponse, GetLockedSubscriptionRecordUserDataErrorBody
    ]:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            purchase_id: Value sent with the request.
            asset: Value sent with the request.
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
            url_template=self._server.default("/sapi/v1/simple-earn/locked/history/subscriptionRecord"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("purchaseId", purchase_id),
                param[str | None]("asset", asset),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnLockedHistorySubscriptionRecordResponse],
            error_mapper=get_locked_subscription_record_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_rate_history_user_data(
        self,
        product_id: str,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SimpleEarnFlexibleHistoryRateHistoryResponse, GetRateHistoryUserDataErrorBody]:
        """Weight(IP): 150

        Args:
            product_id: Value sent with the request.
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
            url_template=self._server.default("/sapi/v1/simple-earn/flexible/history/rateHistory"),
            query_params=[
                param[str]("productId", product_id),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnFlexibleHistoryRateHistoryResponse],
            error_mapper=get_rate_history_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_simple_earn_flexible_product_list_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SimpleEarnFlexibleListResponse, GetSimpleEarnFlexibleProductListUserDataErrorBody]:
        """Get available Simple Earn flexible product list

        Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/simple-earn/flexible/list"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("asset", asset),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnFlexibleListResponse],
            error_mapper=get_simple_earn_flexible_product_list_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_simple_earn_locked_product_list_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SimpleEarnLockedListResponse, GetSimpleEarnLockedProductListUserDataErrorBody]:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/simple-earn/locked/list"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("asset", asset),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnLockedListResponse],
            error_mapper=get_simple_earn_locked_product_list_user_data_error_mapper,
            request_options=request_options,
        )

    async def redeem_flexible_product_trade(
        self,
        product_id: str,
        timestamp: int,
        signature: str,
        *,
        redeem_all: bool | None = None,
        amount: float | None = None,
        dest_account: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SimpleEarnFlexibleRedeemResponse, RedeemFlexibleProductTradeErrorBody]:
        """Weight(IP): 1

        Rate Limit: 1/3s per account

        Args:
            product_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            redeem_all: true or false, default to false
            amount: if redeemAll is false, amount is mandatory
            dest_account: SPOT,FUND,ALL, default SPOT
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/simple-earn/flexible/redeem"),
            query_params=[
                param[str]("productId", product_id),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[bool | None]("redeemAll", redeem_all),
                param[float | None]("amount", amount),
                param[str | None]("destAccount", dest_account),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnFlexibleRedeemResponse],
            error_mapper=redeem_flexible_product_trade_error_mapper,
            request_options=request_options,
        )

    async def redeem_locked_product_trade(
        self,
        position_id: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SimpleEarnLockedRedeemResponse, RedeemLockedProductTradeErrorBody]:
        """Weight(IP): 1

        Rate Limit: 1/3s per account

        Args:
            position_id: 1234
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/simple-earn/locked/redeem"),
            query_params=[
                param[str]("positionId", position_id),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnLockedRedeemResponse],
            error_mapper=redeem_locked_product_trade_error_mapper,
            request_options=request_options,
        )

    async def set_flexible_auto_subscribe_user_data(
        self,
        product_id: str,
        auto_subscribe: bool,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SimpleEarnFlexibleSetAutoSubscribeResponse, SetFlexibleAutoSubscribeUserDataErrorBody]:
        """Weight(IP): 150

        Args:
            product_id: Value sent with the request.
            auto_subscribe: true or false
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/simple-earn/flexible/setAutoSubscribe"),
            query_params=[
                param[str]("productId", product_id),
                param[bool]("autoSubscribe", auto_subscribe),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnFlexibleSetAutoSubscribeResponse],
            error_mapper=set_flexible_auto_subscribe_user_data_error_mapper,
            request_options=request_options,
        )

    async def set_locked_auto_subscribe_user_data(
        self,
        position_id: str,
        auto_subscribe: bool,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SimpleEarnLockedSetAutoSubscribeResponse, SetLockedAutoSubscribeUserDataErrorBody]:
        """Weight(IP): 150

        Args:
            position_id: Value sent with the request.
            auto_subscribe: true or false
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/simple-earn/locked/setAutoSubscribe"),
            query_params=[
                param[str]("positionId", position_id),
                param[bool]("autoSubscribe", auto_subscribe),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnLockedSetAutoSubscribeResponse],
            error_mapper=set_locked_auto_subscribe_user_data_error_mapper,
            request_options=request_options,
        )

    async def set_locked_product_redeem_option_user_data(
        self,
        position_id: str,
        timestamp: int,
        signature: str,
        *,
        redeem_to: RedeemToOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SimpleEarnLockedSetRedeemOptionResponse, SetLockedProductRedeemOptionUserDataErrorBody]:
        """Set redeem option for Locked product

        Weight(IP): 50

        Args:
            position_id: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            redeem_to: SPOT,FLEXIBLE, default FLEXIBLE
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/simple-earn/locked/setRedeemOption"),
            query_params=[
                param[str]("positionId", position_id),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[RedeemToOrStr | None]("redeemTo", redeem_to),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnLockedSetRedeemOptionResponse],
            error_mapper=set_locked_product_redeem_option_user_data_error_mapper,
            request_options=request_options,
        )

    async def simple_account_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SimpleEarnAccountResponse, SimpleAccountUserDataErrorBody]:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/simple-earn/account"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnAccountResponse],
            error_mapper=simple_account_user_data_error_mapper,
            request_options=request_options,
        )

    async def subscribe_flexible_product_trade(
        self,
        product_id: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        auto_subscribe: bool | None = None,
        source_account: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SimpleEarnFlexibleSubscribeResponse, SubscribeFlexibleProductTradeErrorBody]:
        """Weight(IP): 1

        Rate Limit: 1/3s per account

        Args:
            product_id: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            auto_subscribe: true or false, default true.
            source_account: SPOT,FUND,ALL, default SPOT
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/simple-earn/flexible/subscribe"),
            query_params=[
                param[str]("productId", product_id),
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[bool | None]("autoSubscribe", auto_subscribe),
                param[str | None]("sourceAccount", source_account),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnFlexibleSubscribeResponse],
            error_mapper=subscribe_flexible_product_trade_error_mapper,
            request_options=request_options,
        )

    async def subscribe_locked_product_trade(
        self,
        project_id: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        auto_subscribe: bool | None = None,
        source_account: str | None = None,
        redeem_to: RedeemToOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SimpleEarnLockedSubscribeResponse, SubscribeLockedProductTradeErrorBody]:
        """Weight(IP): 1

        Rate Limit: 1/3s per account

        Args:
            project_id: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            auto_subscribe: true or false, default true.
            source_account: SPOT,FUND,ALL, default SPOT
            redeem_to: SPOT,FLEXIBLE, default FLEXIBLE
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/simple-earn/locked/subscribe"),
            query_params=[
                param[str]("projectId", project_id),
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[bool | None]("autoSubscribe", auto_subscribe),
                param[str | None]("sourceAccount", source_account),
                param[RedeemToOrStr | None]("redeemTo", redeem_to),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SimpleEarnLockedSubscribeResponse],
            error_mapper=subscribe_locked_product_trade_error_mapper,
            request_options=request_options,
        )
