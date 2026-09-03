from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder, param
from ..errors.adjust_cross_margin_max_leverage_user_data_error import (
    AdjustCrossMarginMaxLeverageUserDataErrorBody,
    adjust_cross_margin_max_leverage_user_data_error_mapper,
)
from ..errors.cross_margin_collateral_ratio_market_data_error import (
    CrossMarginCollateralRatioMarketDataErrorBody,
    cross_margin_collateral_ratio_market_data_error_mapper,
)
from ..errors.disable_isolated_margin_account_trade_error import (
    DisableIsolatedMarginAccountTradeErrorBody,
    disable_isolated_margin_account_trade_error_mapper,
)
from ..errors.enable_isolated_margin_account_trade_error import (
    EnableIsolatedMarginAccountTradeErrorBody,
    enable_isolated_margin_account_trade_error_mapper,
)
from ..errors.get_a_future_hourly_interest_rate_user_data_error import (
    GetAFutureHourlyInterestRateUserDataErrorBody,
    get_a_future_hourly_interest_rate_user_data_error_mapper,
)
from ..errors.get_all_cross_margin_pairs_market_data_error import (
    GetAllCrossMarginPairsMarketDataErrorBody,
    get_all_cross_margin_pairs_market_data_error_mapper,
)
from ..errors.get_all_isolated_margin_symbol_user_data_error import (
    GetAllIsolatedMarginSymbolUserDataErrorBody,
    get_all_isolated_margin_symbol_user_data_error_mapper,
)
from ..errors.get_all_margin_assets_market_data_error import (
    GetAllMarginAssetsMarketDataErrorBody,
    get_all_margin_assets_market_data_error_mapper,
)
from ..errors.get_bnb_burn_status_user_data_error import (
    GetBnbBurnStatusUserDataErrorBody,
    get_bnb_burn_status_user_data_error_mapper,
)
from ..errors.get_cross_margin_transfer_history_user_data_error import (
    GetCrossMarginTransferHistoryUserDataErrorBody,
    get_cross_margin_transfer_history_user_data_error_mapper,
)
from ..errors.get_cross_or_isolated_margin_capital_flow_user_data_error import (
    GetCrossOrIsolatedMarginCapitalFlowUserDataErrorBody,
    get_cross_or_isolated_margin_capital_flow_user_data_error_mapper,
)
from ..errors.get_force_liquidation_record_user_data_error import (
    GetForceLiquidationRecordUserDataErrorBody,
    get_force_liquidation_record_user_data_error_mapper,
)
from ..errors.get_interest_history_user_data_error import (
    GetInterestHistoryUserDataErrorBody,
    get_interest_history_user_data_error_mapper,
)
from ..errors.get_small_liability_exchange_coin_list_user_data_error import (
    GetSmallLiabilityExchangeCoinListUserDataErrorBody,
    get_small_liability_exchange_coin_list_user_data_error_mapper,
)
from ..errors.get_small_liability_exchange_history_user_data_error import (
    GetSmallLiabilityExchangeHistoryUserDataErrorBody,
    get_small_liability_exchange_history_user_data_error_mapper,
)
from ..errors.get_summary_of_margin_account_user_data_error import (
    GetSummaryOfMarginAccountUserDataErrorBody,
    get_summary_of_margin_account_user_data_error_mapper,
)
from ..errors.get_tokens_or_symbols_delist_schedule_for_cross_margin_and_isolated_margin_market_data_error import (
    GetTokensOrSymbolsDelistScheduleForCrossMarginAndIsolatedMarginMarketDataErrorBody,
    get_tokens_or_symbols_delist_schedule_for_cross_margin_and_isolated_margin_market_data_error_mapper,
)
from ..errors.margin_account_borrow_repay_margin_error import (
    MarginAccountBorrowRepayMarginErrorBody,
    margin_account_borrow_repay_margin_error_mapper,
)
from ..errors.margin_account_cancel_all_open_orders_on_a_symbol_trade_error import (
    MarginAccountCancelAllOpenOrdersOnASymbolTradeErrorBody,
    margin_account_cancel_all_open_orders_on_a_symbol_trade_error_mapper,
)
from ..errors.margin_account_cancel_oco_trade_error import (
    MarginAccountCancelOcoTradeErrorBody,
    margin_account_cancel_oco_trade_error_mapper,
)
from ..errors.margin_account_cancel_order_trade_error import (
    MarginAccountCancelOrderTradeErrorBody,
    margin_account_cancel_order_trade_error_mapper,
)
from ..errors.margin_account_new_oco_trade_error import (
    MarginAccountNewOcoTradeErrorBody,
    margin_account_new_oco_trade_error_mapper,
)
from ..errors.margin_account_new_order_trade_error import (
    MarginAccountNewOrderTradeErrorBody,
    margin_account_new_order_trade_error_mapper,
)
from ..errors.margin_account_new_oto_trade_error import (
    MarginAccountNewOtoTradeErrorBody,
    margin_account_new_oto_trade_error_mapper,
)
from ..errors.margin_account_new_otoco_trade_error import (
    MarginAccountNewOtocoTradeErrorBody,
    margin_account_new_otoco_trade_error_mapper,
)
from ..errors.margin_interest_rate_history_user_data_error import (
    MarginInterestRateHistoryUserDataErrorBody,
    margin_interest_rate_history_user_data_error_mapper,
)
from ..errors.margin_manual_liquidation_margin_error import (
    MarginManualLiquidationMarginErrorBody,
    margin_manual_liquidation_margin_error_mapper,
)
from ..errors.query_borrow_repay_records_in_margin_account_user_data_error import (
    QueryBorrowRepayRecordsInMarginAccountUserDataErrorBody,
    query_borrow_repay_records_in_margin_account_user_data_error_mapper,
)
from ..errors.query_cross_margin_account_details_user_data_error import (
    QueryCrossMarginAccountDetailsUserDataErrorBody,
    query_cross_margin_account_details_user_data_error_mapper,
)
from ..errors.query_cross_margin_fee_data_user_data_error import (
    QueryCrossMarginFeeDataUserDataErrorBody,
    query_cross_margin_fee_data_user_data_error_mapper,
)
from ..errors.query_current_margin_order_count_usage_trade_error import (
    QueryCurrentMarginOrderCountUsageTradeErrorBody,
    query_current_margin_order_count_usage_trade_error_mapper,
)
from ..errors.query_enabled_isolated_margin_account_limit_user_data_error import (
    QueryEnabledIsolatedMarginAccountLimitUserDataErrorBody,
    query_enabled_isolated_margin_account_limit_user_data_error_mapper,
)
from ..errors.query_isolated_margin_account_info_user_data_error import (
    QueryIsolatedMarginAccountInfoUserDataErrorBody,
    query_isolated_margin_account_info_user_data_error_mapper,
)
from ..errors.query_isolated_margin_fee_data_user_data_error import (
    QueryIsolatedMarginFeeDataUserDataErrorBody,
    query_isolated_margin_fee_data_user_data_error_mapper,
)
from ..errors.query_isolated_margin_tier_data_user_data_error import (
    QueryIsolatedMarginTierDataUserDataErrorBody,
    query_isolated_margin_tier_data_user_data_error_mapper,
)
from ..errors.query_liability_coin_leverage_bracket_in_cross_margin_pro_mode_market_data_error import (
    QueryLiabilityCoinLeverageBracketInCrossMarginProModeMarketDataErrorBody,
    query_liability_coin_leverage_bracket_in_cross_margin_pro_mode_market_data_error_mapper,
)
from ..errors.query_margin_account_s_all_oco_user_data_error import (
    QueryMarginAccountSAllOcoUserDataErrorBody,
    query_margin_account_s_all_oco_user_data_error_mapper,
)
from ..errors.query_margin_account_s_all_orders_user_data_error import (
    QueryMarginAccountSAllOrdersUserDataErrorBody,
    query_margin_account_s_all_orders_user_data_error_mapper,
)
from ..errors.query_margin_account_s_oco_user_data_error import (
    QueryMarginAccountSOcoUserDataErrorBody,
    query_margin_account_s_oco_user_data_error_mapper,
)
from ..errors.query_margin_account_s_open_oco_user_data_error import (
    QueryMarginAccountSOpenOcoUserDataErrorBody,
    query_margin_account_s_open_oco_user_data_error_mapper,
)
from ..errors.query_margin_account_s_open_orders_user_data_error import (
    QueryMarginAccountSOpenOrdersUserDataErrorBody,
    query_margin_account_s_open_orders_user_data_error_mapper,
)
from ..errors.query_margin_account_s_order_user_data_error import (
    QueryMarginAccountSOrderUserDataErrorBody,
    query_margin_account_s_order_user_data_error_mapper,
)
from ..errors.query_margin_account_s_trade_list_user_data_error import (
    QueryMarginAccountSTradeListUserDataErrorBody,
    query_margin_account_s_trade_list_user_data_error_mapper,
)
from ..errors.query_margin_available_inventory_user_data_error import (
    QueryMarginAvailableInventoryUserDataErrorBody,
    query_margin_available_inventory_user_data_error_mapper,
)
from ..errors.query_margin_price_index_market_data_error import (
    QueryMarginPriceIndexMarketDataErrorBody,
    query_margin_price_index_market_data_error_mapper,
)
from ..errors.query_max_borrow_user_data_error import (
    QueryMaxBorrowUserDataErrorBody,
    query_max_borrow_user_data_error_mapper,
)
from ..errors.query_max_transfer_out_amount_user_data_error import (
    QueryMaxTransferOutAmountUserDataErrorBody,
    query_max_transfer_out_amount_user_data_error_mapper,
)
from ..errors.toggle_bnb_burn_on_spot_trade_and_margin_interest_user_data_error import (
    ToggleBnbBurnOnSpotTradeAndMarginInterestUserDataErrorBody,
    toggle_bnb_burn_on_spot_trade_and_margin_interest_user_data_error_mapper,
)
from ..models.bnb_burn_status import BnbBurnStatus
from ..models.enums.interest_bnbburn import InterestBnbburnOrStr
from ..models.enums.is_isolated import IsIsolatedOrStr
from ..models.enums.new_order_resp_type import NewOrderRespTypeOrStr
from ..models.enums.pending_above_time_in_force import PendingAboveTimeInForceOrStr
from ..models.enums.pending_above_type import PendingAboveTypeOrStr
from ..models.enums.pending_below_time_in_force import PendingBelowTimeInForceOrStr
from ..models.enums.pending_below_type import PendingBelowTypeOrStr
from ..models.enums.pending_side import PendingSideOrStr
from ..models.enums.pending_time_in_force import PendingTimeInForceOrStr
from ..models.enums.pending_type import PendingTypeOrStr
from ..models.enums.self_trade_prevention_mode import SelfTradePreventionModeOrStr
from ..models.enums.side import SideOrStr
from ..models.enums.side_effect_type import SideEffectTypeOrStr
from ..models.enums.side_effect_type1 import SideEffectType1OrStr
from ..models.enums.spot_bnbburn import SpotBnbburnOrStr
from ..models.enums.stop_limit_time_in_force import StopLimitTimeInForceOrStr
from ..models.enums.time_in_force import TimeInForceOrStr
from ..models.enums.type1 import Type1OrStr
from ..models.enums.type2 import Type2OrStr
from ..models.enums.type3 import Type3OrStr
from ..models.enums.type4 import Type4OrStr
from ..models.enums.working_side import WorkingSideOrStr
from ..models.enums.working_time_in_force import WorkingTimeInForceOrStr
from ..models.enums.working_type import WorkingTypeOrStr
from ..models.isolated_margin_account_info import IsolatedMarginAccountInfo
from ..models.margin_oco_order import MarginOcoOrder
from ..models.margin_order import MarginOrder
from ..models.margin_order_detail import MarginOrderDetail
from ..models.margin_trade import MarginTrade
from ..models.sapi_v1_margin_account_response import SapiV1MarginAccountResponse
from ..models.sapi_v1_margin_all_assets_response import SapiV1MarginAllAssetsResponse
from ..models.sapi_v1_margin_all_order_list_response import SapiV1MarginAllOrderListResponse
from ..models.sapi_v1_margin_all_pairs_response import SapiV1MarginAllPairsResponse
from ..models.sapi_v1_margin_available_inventory_response import SapiV1MarginAvailableInventoryResponse
from ..models.sapi_v1_margin_borrow_repay_response import SapiV1MarginBorrowRepayResponse
from ..models.sapi_v1_margin_borrow_repay_response1 import SapiV1MarginBorrowRepayResponse1
from ..models.sapi_v1_margin_capital_flow_response import SapiV1MarginCapitalFlowResponse
from ..models.sapi_v1_margin_cross_margin_collateral_ratio_response import (
    SapiV1MarginCrossMarginCollateralRatioResponse,
)
from ..models.sapi_v1_margin_cross_margin_data_response import SapiV1MarginCrossMarginDataResponse
from ..models.sapi_v1_margin_delist_schedule_response import SapiV1MarginDelistScheduleResponse
from ..models.sapi_v1_margin_exchange_small_liability_history_response import (
    SapiV1MarginExchangeSmallLiabilityHistoryResponse,
)
from ..models.sapi_v1_margin_exchange_small_liability_response import SapiV1MarginExchangeSmallLiabilityResponse
from ..models.sapi_v1_margin_force_liquidation_rec_response import SapiV1MarginForceLiquidationRecResponse
from ..models.sapi_v1_margin_interest_history_response import SapiV1MarginInterestHistoryResponse
from ..models.sapi_v1_margin_interest_rate_history_response import SapiV1MarginInterestRateHistoryResponse
from ..models.sapi_v1_margin_isolated_account_limit_response import SapiV1MarginIsolatedAccountLimitResponse
from ..models.sapi_v1_margin_isolated_account_response import SapiV1MarginIsolatedAccountResponse
from ..models.sapi_v1_margin_isolated_all_pairs_response import SapiV1MarginIsolatedAllPairsResponse
from ..models.sapi_v1_margin_isolated_margin_data_response import SapiV1MarginIsolatedMarginDataResponse
from ..models.sapi_v1_margin_isolated_margin_tier_response import SapiV1MarginIsolatedMarginTierResponse
from ..models.sapi_v1_margin_leverage_bracket_response import SapiV1MarginLeverageBracketResponse
from ..models.sapi_v1_margin_manual_liquidation_response import SapiV1MarginManualLiquidationResponse
from ..models.sapi_v1_margin_max_borrowable_response import SapiV1MarginMaxBorrowableResponse
from ..models.sapi_v1_margin_max_leverage_response import SapiV1MarginMaxLeverageResponse
from ..models.sapi_v1_margin_max_transferable_response import SapiV1MarginMaxTransferableResponse
from ..models.sapi_v1_margin_next_hourly_interest_rate_response import SapiV1MarginNextHourlyInterestRateResponse
from ..models.sapi_v1_margin_open_order_list_response import SapiV1MarginOpenOrderListResponse
from ..models.sapi_v1_margin_order_list_response import SapiV1MarginOrderListResponse
from ..models.sapi_v1_margin_order_oco_response import SapiV1MarginOrderOcoResponse
from ..models.sapi_v1_margin_order_oto_response import SapiV1MarginOrderOtoResponse
from ..models.sapi_v1_margin_order_otoco_response import SapiV1MarginOrderOtocoResponse
from ..models.sapi_v1_margin_price_index_response import SapiV1MarginPriceIndexResponse
from ..models.sapi_v1_margin_rate_limit_order_response import SapiV1MarginRateLimitOrderResponse
from ..models.sapi_v1_margin_trade_coeff_response import SapiV1MarginTradeCoeffResponse
from ..models.sapi_v1_margin_transfer_response import SapiV1MarginTransferResponse
from ..models.unions.sapi_v1_margin_open_orders_response import SapiV1MarginOpenOrdersResponse
from ..models.unions.sapi_v1_margin_order_response import SapiV1MarginOrderResponse
from ..server.server import Server


class Margin:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MarginWithRawResponse(client, server, auth)

    def adjust_cross_margin_max_leverage_user_data(
        self,
        max_leverage: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MarginMaxLeverageResponse:
        """Adjust cross margin max leverage

        Weight(UID): 3000

        Args:
            max_leverage: Can only adjust 3 or 5
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Adjust result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.adjust_cross_margin_max_leverage_user_data(
            max_leverage, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def cross_margin_collateral_ratio_market_data(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[SapiV1MarginCrossMarginCollateralRatioResponse]:
        """Weight(IP): 100

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Margin collateral ratio

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.cross_margin_collateral_ratio_market_data(
            request_options=request_options
        ).unwrap()

    def disable_isolated_margin_account_trade(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MarginIsolatedAccountResponse:
        """Disable isolated margin account for a specific symbol. Each trading pair can only be deactivated once every
        24 hours .

        Weight(UID): 300

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Isolated Margin Account status

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.disable_isolated_margin_account_trade(
            symbol, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def enable_isolated_margin_account_trade(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MarginIsolatedAccountResponse:
        """Enable isolated margin account for a specific symbol.

        Weight(UID): 300

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Isolated Margin Account status

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.enable_isolated_margin_account_trade(
            symbol, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def get_all_cross_margin_pairs_market_data(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[SapiV1MarginAllPairsResponse]:
        """Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Margin pairs

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_all_cross_margin_pairs_market_data(
            symbol, request_options=request_options
        ).unwrap()

    def get_all_isolated_margin_symbol_user_data(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1MarginIsolatedAllPairsResponse]:
        """Weight(IP): 10

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            All Isolated Margin Symbols

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_all_isolated_margin_symbol_user_data(
            symbol, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def get_all_margin_assets_market_data(
        self, asset: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[SapiV1MarginAllAssetsResponse]:
        """Weight(IP): 1

        Args:
            asset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Assets details

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_all_margin_assets_market_data(
            asset, request_options=request_options
        ).unwrap()

    def get_bnb_burn_status_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BnbBurnStatus:
        """Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Status on BNB to pay for trading fees

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_bnb_burn_status_user_data(
            timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def get_cross_margin_transfer_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        type_: Type2OrStr | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        isolated_symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MarginTransferResponse:
        """- Response in descending order
        - Returns data for last 7 days by default
        - Set ``archived`` to ``true`` to query data from 6 months ago

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            type_: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            isolated_symbol: Isolated symbol
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Margin account transfer history, response in descending order

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_cross_margin_transfer_history_user_data(
            timestamp,
            signature,
            asset=asset,
            type_=type_,
            start_time=start_time,
            end_time=end_time,
            current=current,
            size=size,
            isolated_symbol=isolated_symbol,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_force_liquidation_record_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        isolated_symbol: str | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MarginForceLiquidationRecResponse:
        """- Response in descending order

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            isolated_symbol: Isolated symbol
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Force Liquidation History, response in descending order

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_force_liquidation_record_user_data(
            timestamp,
            signature,
            start_time=start_time,
            end_time=end_time,
            isolated_symbol=isolated_symbol,
            current=current,
            size=size,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_interest_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        isolated_symbol: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        archived: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MarginInterestHistoryResponse:
        """- Response in descending order
        - If ``isolatedSymbol`` is not sent, crossed margin data will be returned
        - Set ``archived`` to ``true`` to query data from 6 months ago
        - ``type`` in response has 4 enums:
          - ``PERIODIC`` interest charged per hour
          - ``ON_BORROW`` first interest charged on borrow
          - ``PERIODIC_CONVERTED`` interest charged per hour converted into BNB
          - ``ON_BORROW_CONVERTED`` first interest charged on borrow converted into BNB

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            isolated_symbol: Isolated symbol
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            archived: Default: false. Set to true for archived data from 6 months ago
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Interest History, response in descending order

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_interest_history_user_data(
            timestamp,
            signature,
            asset=asset,
            isolated_symbol=isolated_symbol,
            start_time=start_time,
            end_time=end_time,
            current=current,
            size=size,
            archived=archived,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_small_liability_exchange_coin_list_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1MarginExchangeSmallLiabilityResponse]:
        """Query the coins which can be small liability exchange

        Weight(UID): 100

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            coin list

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_small_liability_exchange_coin_list_user_data(
            timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def get_small_liability_exchange_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        current: int | None = None,
        size: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MarginExchangeSmallLiabilityHistoryResponse:
        """Get Small liability Exchange History

        Weight(UID): 100

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            coin list

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_small_liability_exchange_history_user_data(
            timestamp,
            signature,
            current=current,
            size=size,
            start_time=start_time,
            end_time=end_time,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_summary_of_margin_account_user_data(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MarginTradeCoeffResponse:
        """Get personal margin level information

        Weight(IP): 10

        Args:
            email: Email Address
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Summary of Margin Account

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_summary_of_margin_account_user_data(
            email, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def get_a_future_hourly_interest_rate_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        assets: str | None = None,
        is_isolated: IsIsolatedOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1MarginNextHourlyInterestRateResponse]:
        """Get user the next hourly estimate interest

        Weight(UID): 100

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            assets: List of assets, separated by commas, up to 20
            is_isolated: for isolated margin or not, "TRUE", "FALSE"
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            hourly interest

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_a_future_hourly_interest_rate_user_data(
            timestamp,
            signature,
            assets=assets,
            is_isolated=is_isolated,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_cross_or_isolated_margin_capital_flow_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        symbol: str | None = None,
        type_: Type3OrStr | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        from_id: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1MarginCapitalFlowResponse]:
        """Get cross or isolated margin capital flow

        Weight(IP): 100

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            symbol: Required when querying isolated data
            type_: Value sent with the request.
            start_time: Only supports querying the data of the last 90 days
            end_time: UTC timestamp in ms
            from_id: If fromId is set, the data with id > fromId will be returned. Otherwise the latest data will be
                returned
            limit: The number of data items returned each time is limited. Default 500; Max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Margin capital flow

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_cross_or_isolated_margin_capital_flow_user_data(
            timestamp,
            signature,
            asset=asset,
            symbol=symbol,
            type_=type_,
            start_time=start_time,
            end_time=end_time,
            from_id=from_id,
            limit=limit,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_tokens_or_symbols_delist_schedule_for_cross_margin_and_isolated_margin_market_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1MarginDelistScheduleResponse]:
        """Get tokens or symbols delist schedule for cross margin and isolated margin

        Weight(IP): 100

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            tokens or symbols delist schedule

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_tokens_or_symbols_delist_schedule_for_cross_margin_and_isolated_margin_market_data(
            timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def margin_account_cancel_oco_trade(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        order_list_id: int | None = None,
        list_client_order_id: str | None = None,
        new_client_order_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MarginOcoOrder:
        """Cancel an entire Order List for a margin account

        - Canceling an individual leg will cancel the entire OCO
        - Either ``orderListId`` or ``listClientOrderId`` must be provided

        Weight(UID): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            order_list_id: Order list id
            list_client_order_id: A unique Id for the entire orderList
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Margin OCO details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.margin_account_cancel_oco_trade(
            symbol,
            timestamp,
            signature,
            is_isolated=is_isolated,
            order_list_id=order_list_id,
            list_client_order_id=list_client_order_id,
            new_client_order_id=new_client_order_id,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def margin_account_cancel_order_trade(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        order_id: int | None = None,
        orig_client_order_id: str | None = None,
        new_client_order_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MarginOrder:
        """Cancel an active order for margin account.

        Either ``orderId`` or ``origClientOrderId`` must be sent.

        Weight(IP): 10

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            order_id: Order id
            orig_client_order_id: Order id from client
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Cancelled margin order details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.margin_account_cancel_order_trade(
            symbol,
            timestamp,
            signature,
            is_isolated=is_isolated,
            order_id=order_id,
            orig_client_order_id=orig_client_order_id,
            new_client_order_id=new_client_order_id,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def margin_account_cancel_all_open_orders_on_a_symbol_trade(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1MarginOpenOrdersResponse]:
        """- Cancels all active orders on a symbol for margin account.
        - This includes OCO orders.

        Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Cancelled margin orders

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.margin_account_cancel_all_open_orders_on_a_symbol_trade(
            symbol,
            timestamp,
            signature,
            is_isolated=is_isolated,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def margin_account_new_oco_trade(
        self,
        symbol: str,
        side: SideOrStr,
        quantity: float,
        price: float,
        stop_price: float,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        list_client_order_id: str | None = None,
        limit_client_order_id: str | None = None,
        limit_iceberg_qty: float | None = None,
        stop_client_order_id: str | None = None,
        stop_limit_price: float | None = None,
        stop_iceberg_qty: float | None = None,
        stop_limit_time_in_force: StopLimitTimeInForceOrStr | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        side_effect_type: SideEffectTypeOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MarginOrderOcoResponse:
        """Send in a new OCO for a margin account

        - Price Restrictions:
          - SELL: Limit Price > Last Price > Stop Price
          - BUY: Limit Price < Last Price < Stop Price
        - Quantity Restrictions:
          - Both legs must have the same quantity
          - ICEBERG quantities however do not have to be the same.
        - Order Rate Limit
          - OCO counts as 2 orders against the order rate limit.

        Weight(UID): 6

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            quantity: Value sent with the request.
            price: Order price
            stop_price: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            list_client_order_id: A unique Id for the entire orderList
            limit_client_order_id: A unique Id for the limit order
            limit_iceberg_qty: Value sent with the request.
            stop_client_order_id: A unique Id for the stop loss/stop loss limit leg
            stop_limit_price: If provided, stopLimitTimeInForce is required.
            stop_iceberg_qty: Value sent with the request.
            stop_limit_time_in_force: Value sent with the request.
            new_order_resp_type: Set the response JSON.
            side_effect_type: Default ``NO_SIDE_EFFECT``
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            New Margin OCO details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.margin_account_new_oco_trade(
            symbol,
            side,
            quantity,
            price,
            stop_price,
            timestamp,
            signature,
            is_isolated=is_isolated,
            list_client_order_id=list_client_order_id,
            limit_client_order_id=limit_client_order_id,
            limit_iceberg_qty=limit_iceberg_qty,
            stop_client_order_id=stop_client_order_id,
            stop_limit_price=stop_limit_price,
            stop_iceberg_qty=stop_iceberg_qty,
            stop_limit_time_in_force=stop_limit_time_in_force,
            new_order_resp_type=new_order_resp_type,
            side_effect_type=side_effect_type,
            self_trade_prevention_mode=self_trade_prevention_mode,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def margin_account_new_oto_trade(
        self,
        symbol: str,
        working_type: WorkingTypeOrStr,
        working_side: WorkingSideOrStr,
        working_price: float,
        working_quantity: float,
        working_iceberg_qty: float,
        pending_type: PendingTypeOrStr,
        pending_side: PendingSideOrStr,
        pending_quantity: float,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        list_client_order_id: str | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        side_effect_type: SideEffectType1OrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        auto_repay_at_cancel: bool | None = None,
        working_client_order_id: str | None = None,
        working_time_in_force: WorkingTimeInForceOrStr | None = None,
        pending_client_order_id: str | None = None,
        pending_price: float | None = None,
        pending_stop_price: float | None = None,
        pending_trailing_delta: float | None = None,
        pending_iceberg_qty: float | None = None,
        pending_time_in_force: PendingTimeInForceOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MarginOrderOtoResponse:
        """Post a new ``OTO`` order for margin account:
        - An ``OTO`` (One-Triggers-the-Other) is an order list comprised of 2 orders
        - The first order is called the working order and must be ``LIMIT`` or ``LIMIT_MAKER``. Initially, only the
            working order goes on the order book.
        - The second order is called the pending order. It can be any order type except for ``MARKET`` orders using
            parameter ``quoteOrderQty``. The pending order is only placed on the order book when the working order gets
            fully filled.
        - If either the working order or the pending order is cancelled individually, the other order in the order list
            will also be canceled or expired.
        - When the order list is placed, if the working order gets immediately fully filled, the placement response will
            show the working order as ``FILLED`` but the pending order will still appear as ``PENDING_NEW``. You need to
            query the status of the pending order again to see its updated status.
        - OTOs add 2 orders to the unfilled order count, ``EXCHANGE_MAX_NUM_ORDERS`` filter and ``MAX_NUM_ORDERS``
            filter.

        Weight(UID): 6

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            working_type: Supported values: LIMIT,LIMIT_MAKER
            working_side: BUY,SELL
            working_price: Value sent with the request.
            working_quantity: Sets the quantity for the working order.
            working_iceberg_qty: This can only be used if workingTimeInForce is GTC.
            pending_type: Supported values: Order Types Note that MARKET orders using quoteOrderQty are not supported.
            pending_side: BUY,SELL
            pending_quantity: Sets the quantity for the pending order.
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            list_client_order_id: Arbitrary unique ID among open order lists. Automatically generated if not sent. A new
                order list with the same ``listClientOrderId`` is accepted only when the previous one is filled or
                completely expired. ``listClientOrderId`` is distinct from the ``workingClientOrderId`` and the
                ``pendingClientOrderId``.
            new_order_resp_type: Set the response JSON.
            side_effect_type: Default ``NO_SIDE_EFFECT``
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            auto_repay_at_cancel: Only when MARGIN_BUY order takes effect, true means that the debt generated by the
                order needs to be repay after the order is cancelled. The default is true
            working_client_order_id: Arbitrary unique ID among open orders for the working order. Automatically
                generated if not sent.
            working_time_in_force: GTC, IOC, FOK
            pending_client_order_id: Arbitrary unique ID among open orders for the pending order. Automatically
                generated if not sent.
            pending_price: Value sent with the request.
            pending_stop_price: Value sent with the request.
            pending_trailing_delta: Value sent with the request.
            pending_iceberg_qty: This can only be used if pendingTimeInForce is GTC.
            pending_time_in_force: GTC, IOC, FOK
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OTO order

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.margin_account_new_oto_trade(
            symbol,
            working_type,
            working_side,
            working_price,
            working_quantity,
            working_iceberg_qty,
            pending_type,
            pending_side,
            pending_quantity,
            timestamp,
            signature,
            is_isolated=is_isolated,
            list_client_order_id=list_client_order_id,
            new_order_resp_type=new_order_resp_type,
            side_effect_type=side_effect_type,
            self_trade_prevention_mode=self_trade_prevention_mode,
            auto_repay_at_cancel=auto_repay_at_cancel,
            working_client_order_id=working_client_order_id,
            working_time_in_force=working_time_in_force,
            pending_client_order_id=pending_client_order_id,
            pending_price=pending_price,
            pending_stop_price=pending_stop_price,
            pending_trailing_delta=pending_trailing_delta,
            pending_iceberg_qty=pending_iceberg_qty,
            pending_time_in_force=pending_time_in_force,
            request_options=request_options,
        ).unwrap()

    def margin_account_new_otoco_trade(
        self,
        symbol: str,
        working_type: WorkingTypeOrStr,
        working_side: WorkingSideOrStr,
        working_price: float,
        working_quantity: float,
        working_iceberg_qty: float,
        pending_side: PendingSideOrStr,
        pending_quantity: float,
        pending_above_type: PendingAboveTypeOrStr,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        side_effect_type: SideEffectType1OrStr | None = None,
        auto_repay_at_cancel: bool | None = None,
        list_client_order_id: str | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        working_client_order_id: str | None = None,
        working_time_in_force: WorkingTimeInForceOrStr | None = None,
        pending_above_client_order_id: str | None = None,
        pending_above_price: float | None = None,
        pending_above_stop_price: float | None = None,
        pending_above_trailing_delta: float | None = None,
        pending_above_iceberg_qty: float | None = None,
        pending_above_time_in_force: PendingAboveTimeInForceOrStr | None = None,
        pending_below_type: PendingBelowTypeOrStr | None = None,
        pending_below_client_order_id: str | None = None,
        pending_below_price: float | None = None,
        pending_below_stop_price: float | None = None,
        pending_below_trailing_delta: float | None = None,
        pending_below_iceberg_qty: float | None = None,
        pending_below_time_in_force: PendingBelowTimeInForceOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MarginOrderOtocoResponse:
        """Post a new ``OTOCO`` order for margin account:
        - An ``OTOCO`` (One-Triggers-the-Other-Cancel-the-Other) is an order list comprised of 3 orders
        - The first order is called the working order and must be ``LIMIT`` or ``LIMIT_MAKER``. Initially, only the
            working order goes on the order book.
          - The behavior of the working order is the same as the ``OTO``.
        - ``OTOCO`` has 2 pending orders (pending above and pending below), forming an ``OCO`` pair. The pending orders
            are only placed on the order book when the working order gets fully filled.
          - The rules of the pending above and pending below follow the same rules as the Order List ``OCO``.
        - OTOCOs add 3 orders to the unfilled order count, ``EXCHANGE_MAX_NUM_ORDERS`` filter and ``MAX_NUM_ORDERS``
            filter.

        Weight(UID): 6

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            working_type: Supported values: LIMIT,LIMIT_MAKER
            working_side: BUY,SELL
            working_price: Value sent with the request.
            working_quantity: Sets the quantity for the working order.
            working_iceberg_qty: This can only be used if workingTimeInForce is GTC.
            pending_side: BUY,SELL
            pending_quantity: Sets the quantity for the pending order.
            pending_above_type: Supported values: LIMIT_MAKER, STOP_LOSS, and STOP_LOSS_LIMIT
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            side_effect_type: Default ``NO_SIDE_EFFECT``
            auto_repay_at_cancel: Only when MARGIN_BUY order takes effect, true means that the debt generated by the
                order needs to be repay after the order is cancelled. The default is true
            list_client_order_id: Arbitrary unique ID among open order lists. Automatically generated if not sent. A new
                order list with the same ``listClientOrderId`` is accepted only when the previous one is filled or
                completely expired. ``listClientOrderId`` is distinct from the ``workingClientOrderId`` and the
                ``pendingClientOrderId``.
            new_order_resp_type: Set the response JSON.
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            working_client_order_id: Arbitrary unique ID among open orders for the working order. Automatically
                generated if not sent.
            working_time_in_force: GTC, IOC, FOK
            pending_above_client_order_id: Arbitrary unique ID among open orders for the pending above order.
                Automatically generated if not sent.
            pending_above_price: Value sent with the request.
            pending_above_stop_price: Value sent with the request.
            pending_above_trailing_delta: Value sent with the request.
            pending_above_iceberg_qty: This can only be used if pendingAboveTimeInForce is GTC.
            pending_above_time_in_force: Value sent with the request.
            pending_below_type: Supported values: LIMIT_MAKER, STOP_LOSS, and STOP_LOSS_LIMIT
            pending_below_client_order_id: Arbitrary unique ID among open orders for the pending below order.
                Automatically generated if not sent.
            pending_below_price: Value sent with the request.
            pending_below_stop_price: Value sent with the request.
            pending_below_trailing_delta: Value sent with the request.
            pending_below_iceberg_qty: This can only be used if pendingBelowTimeInForce is GTC.
            pending_below_time_in_force: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OTOCO order

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.margin_account_new_otoco_trade(
            symbol,
            working_type,
            working_side,
            working_price,
            working_quantity,
            working_iceberg_qty,
            pending_side,
            pending_quantity,
            pending_above_type,
            timestamp,
            signature,
            is_isolated=is_isolated,
            side_effect_type=side_effect_type,
            auto_repay_at_cancel=auto_repay_at_cancel,
            list_client_order_id=list_client_order_id,
            new_order_resp_type=new_order_resp_type,
            self_trade_prevention_mode=self_trade_prevention_mode,
            working_client_order_id=working_client_order_id,
            working_time_in_force=working_time_in_force,
            pending_above_client_order_id=pending_above_client_order_id,
            pending_above_price=pending_above_price,
            pending_above_stop_price=pending_above_stop_price,
            pending_above_trailing_delta=pending_above_trailing_delta,
            pending_above_iceberg_qty=pending_above_iceberg_qty,
            pending_above_time_in_force=pending_above_time_in_force,
            pending_below_type=pending_below_type,
            pending_below_client_order_id=pending_below_client_order_id,
            pending_below_price=pending_below_price,
            pending_below_stop_price=pending_below_stop_price,
            pending_below_trailing_delta=pending_below_trailing_delta,
            pending_below_iceberg_qty=pending_below_iceberg_qty,
            pending_below_time_in_force=pending_below_time_in_force,
            request_options=request_options,
        ).unwrap()

    def margin_account_new_order_trade(
        self,
        symbol: str,
        side: SideOrStr,
        type_: Type1OrStr,
        quantity: float,
        auto_repay_at_cancel: bool,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        quote_order_qty: float | None = None,
        price: float | None = None,
        stop_price: float | None = None,
        new_client_order_id: str | None = None,
        iceberg_qty: float | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        side_effect_type: SideEffectTypeOrStr | None = None,
        time_in_force: TimeInForceOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MarginOrderResponse:
        """Post a new order for margin account.

        Weight(UID): 6

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            type_: Order type
            quantity: Value sent with the request.
            auto_repay_at_cancel: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            quote_order_qty: Quote quantity
            price: Order price
            stop_price: Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            iceberg_qty: Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.
            new_order_resp_type: Set the response JSON.
            side_effect_type: Default ``NO_SIDE_EFFECT``
            time_in_force: Order time in force
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Margin order info

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.margin_account_new_order_trade(
            symbol,
            side,
            type_,
            quantity,
            auto_repay_at_cancel,
            timestamp,
            signature,
            is_isolated=is_isolated,
            quote_order_qty=quote_order_qty,
            price=price,
            stop_price=stop_price,
            new_client_order_id=new_client_order_id,
            iceberg_qty=iceberg_qty,
            new_order_resp_type=new_order_resp_type,
            side_effect_type=side_effect_type,
            time_in_force=time_in_force,
            self_trade_prevention_mode=self_trade_prevention_mode,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def margin_interest_rate_history_user_data(
        self,
        asset: str,
        timestamp: int,
        signature: str,
        *,
        vip_level: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1MarginInterestRateHistoryResponse]:
        """The max interval between startTime and endTime is 30 days.

        Weight(IP): 1

        Args:
            asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            vip_level: Defaults to user's vip level
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Margin Interest Rate History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.margin_interest_rate_history_user_data(
            asset,
            timestamp,
            signature,
            vip_level=vip_level,
            start_time=start_time,
            end_time=end_time,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def margin_account_borrow_repay_margin(
        self,
        asset: str,
        is_isolated: str,
        symbol: str,
        amount: float,
        type_: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MarginBorrowRepayResponse:
        """Margin account borrow/repay(MARGIN)

        Weight(UID): 3000

        Args:
            asset: Value sent with the request.
            is_isolated: TRUE for isolated margin, FALSE for crossed margin
            symbol: Trading symbol, e.g. BNBUSDT
            amount: Value sent with the request.
            type_: BORROW or REPAY
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Margin account borrow/repay

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.margin_account_borrow_repay_margin(
            asset,
            is_isolated,
            symbol,
            amount,
            type_,
            timestamp,
            signature,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def margin_manual_liquidation_margin(
        self,
        type_: Type4OrStr,
        timestamp: int,
        signature: str,
        *,
        symbol: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1MarginManualLiquidationResponse]:
        """Margin manual liquidation

        Weight(UID): 3000

        Args:
            type_: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            symbol: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Margin manual liquidation

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.margin_manual_liquidation_margin(
            type_, timestamp, signature, symbol=symbol, request_options=request_options
        ).unwrap()

    def query_cross_margin_account_details_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MarginAccountResponse:
        """Weight(IP): 10

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Margin account details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_cross_margin_account_details_user_data(
            timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def query_cross_margin_fee_data_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        vip_level: int | None = None,
        coin: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1MarginCrossMarginDataResponse]:
        """Get cross margin fee data collection with any vip level or user's current specific data as
        https://www.binance.com/en/margin-fee

        Weight(IP): 1 when coin is specified; 5 when the coin parameter is omitted

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            vip_level: Defaults to user's vip level
            coin: Coin name
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Cross Margin Fee Data

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_cross_margin_fee_data_user_data(
            timestamp,
            signature,
            vip_level=vip_level,
            coin=coin,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def query_current_margin_order_count_usage_trade(
        self,
        timestamp: int,
        signature: str,
        *,
        is_isolated: str | None = None,
        symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1MarginRateLimitOrderResponse]:
        """Displays the user's current margin order count usage for all intervals.

        Weight(IP): 20

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            symbol: isolated symbol, mandatory for isolated margin
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Usage.

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_current_margin_order_count_usage_trade(
            timestamp,
            signature,
            is_isolated=is_isolated,
            symbol=symbol,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def query_enabled_isolated_margin_account_limit_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MarginIsolatedAccountLimitResponse:
        """Query enabled isolated margin account limit.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Number of enabled Isolated Margin Account and its limit

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_enabled_isolated_margin_account_limit_user_data(
            timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def query_isolated_margin_account_info_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        symbols: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> IsolatedMarginAccountInfo:
        """- If "symbols" is not sent, all isolated assets will be returned.
        - If "symbols" is sent, only the isolated assets of the sent symbols will be returned.

        Weight(IP): 10

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            symbols: Max 5 symbols can be sent; separated by ','
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Isolated Margin Account Info when "symbols" is not sent

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_isolated_margin_account_info_user_data(
            timestamp, signature, symbols=symbols, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def query_isolated_margin_fee_data_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        vip_level: int | None = None,
        symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1MarginIsolatedMarginDataResponse]:
        """Get isolated margin fee data collection with any vip level or user's current specific data as
        https://www.binance.com/en/margin-fee

        Weight(IP): 1 when a single is specified; 10 when the symbol parameter is omitted

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            vip_level: Defaults to user's vip level
            symbol: Trading symbol, e.g. BNBUSDT
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Isolated Margin Fee Data

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_isolated_margin_fee_data_user_data(
            timestamp,
            signature,
            vip_level=vip_level,
            symbol=symbol,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def query_isolated_margin_tier_data_user_data(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        tier: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1MarginIsolatedMarginTierResponse]:
        """Get isolated margin tier data collection with any tier as https://www.binance.com/en/margin-data

        Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            tier: All margin tier data will be returned if tier is omitted
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Isolated Margin Tier Data

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_isolated_margin_tier_data_user_data(
            symbol, timestamp, signature, tier=tier, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def query_liability_coin_leverage_bracket_in_cross_margin_pro_mode_market_data(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[SapiV1MarginLeverageBracketResponse]:
        """Liability Coin Leverage Bracket in Cross Margin Pro Mode

        Weight(IP): 1

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Leverage info

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_liability_coin_leverage_bracket_in_cross_margin_pro_mode_market_data(
            request_options=request_options
        ).unwrap()

    def query_margin_account_s_all_orders_user_data(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        order_id: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[MarginOrderDetail]:
        """- If ``orderId`` is set, it will get orders >= that orderId. Otherwise most recent orders are returned.
        - For some historical orders ``cummulativeQuoteQty`` will be < 0, meaning the data is not available at this
            time.

        Weight(IP): 200

        Request Limit: 60 times/min per IP

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            order_id: Order id
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Margin order list

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_margin_account_s_all_orders_user_data(
            symbol,
            timestamp,
            signature,
            is_isolated=is_isolated,
            order_id=order_id,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def query_margin_account_s_oco_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        symbol: str | None = None,
        order_list_id: int | None = None,
        orig_client_order_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MarginOrderListResponse:
        """Retrieves a specific OCO based on provided optional parameters

        - Either ``orderListId`` or ``origClientOrderId`` must be provided

        Weight(IP): 10

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            symbol: Mandatory for isolated margin, not supported for cross margin
            order_list_id: Order list id
            orig_client_order_id: Order id from client
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Margin OCO details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_margin_account_s_oco_user_data(
            timestamp,
            signature,
            is_isolated=is_isolated,
            symbol=symbol,
            order_list_id=order_list_id,
            orig_client_order_id=orig_client_order_id,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def query_margin_account_s_open_oco_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1MarginOpenOrderListResponse]:
        """Weight(IP): 10

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            symbol: Mandatory for isolated margin, not supported for cross margin
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of Open Margin OCO orders

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_margin_account_s_open_oco_user_data(
            timestamp,
            signature,
            is_isolated=is_isolated,
            symbol=symbol,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def query_margin_account_s_open_orders_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        symbol: str | None = None,
        is_isolated: IsIsolatedOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[MarginOrderDetail]:
        """- If the ``symbol`` is not sent, orders for all symbols will be returned in an array.
        - When all symbols are returned, the number of requests counted against the rate limiter is equal to the number
            of symbols currently trading on the exchange
        - If isIsolated ="TRUE", symbol must be sent.

        Weight(IP): 10

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            symbol: Trading symbol, e.g. BNBUSDT
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Margin open orders list

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_margin_account_s_open_orders_user_data(
            timestamp,
            signature,
            symbol=symbol,
            is_isolated=is_isolated,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def query_margin_account_s_order_user_data(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        order_id: int | None = None,
        orig_client_order_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MarginOrderDetail:
        """- Either ``orderId`` or ``origClientOrderId`` must be sent.
        - For some historical orders ``cummulativeQuoteQty`` will be < 0, meaning the data is not available at this
            time.

        Weight(IP): 10

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            order_id: Order id
            orig_client_order_id: Order id from client
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Interest History, response in descending order

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_margin_account_s_order_user_data(
            symbol,
            timestamp,
            signature,
            is_isolated=is_isolated,
            order_id=order_id,
            orig_client_order_id=orig_client_order_id,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def query_margin_account_s_trade_list_user_data(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        from_id: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[MarginTrade]:
        """- If ``fromId`` is set, it will get orders >= that ``fromId``. Otherwise most recent trades are returned.

        Weight(IP): 10

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            from_id: Trade id to fetch from. Default gets most recent trades.
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of margin trades

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_margin_account_s_trade_list_user_data(
            symbol,
            timestamp,
            signature,
            is_isolated=is_isolated,
            start_time=start_time,
            end_time=end_time,
            from_id=from_id,
            limit=limit,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def query_margin_account_s_all_oco_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        symbol: str | None = None,
        from_id: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1MarginAllOrderListResponse]:
        """Retrieves all OCO for a specific margin account based on provided optional parameters

        Weight(IP): 200

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            symbol: Mandatory for isolated margin, not supported for cross margin
            from_id: If supplied, neither ``startTime`` or ``endTime`` can be provided
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default Value: 500; Max Value: 1000
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of Margin OCO orders

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_margin_account_s_all_oco_user_data(
            timestamp,
            signature,
            is_isolated=is_isolated,
            symbol=symbol,
            from_id=from_id,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def query_margin_available_inventory_user_data(
        self, type_: Type4OrStr, timestamp: int, signature: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SapiV1MarginAvailableInventoryResponse:
        """Margin available Inventory query

        Weight(UID): 50

        Args:
            type_: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Margin available Inventory

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_margin_available_inventory_user_data(
            type_, timestamp, signature, request_options=request_options
        ).unwrap()

    def query_margin_price_index_market_data(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SapiV1MarginPriceIndexResponse:
        """Weight(IP): 10

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Price index

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_margin_price_index_market_data(
            symbol, request_options=request_options
        ).unwrap()

    def query_max_borrow_user_data(
        self,
        asset: str,
        timestamp: int,
        signature: str,
        *,
        isolated_symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MarginMaxBorrowableResponse:
        """- If ``isolatedSymbol`` is not sent, crossed margin data will be sent.
        - ``borrowLimit`` is also available from https://www.binance.com/en/margin-fee

        Weight(IP): 50

        Args:
            asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            isolated_symbol: Isolated symbol
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Details on max borrow amount

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_max_borrow_user_data(
            asset,
            timestamp,
            signature,
            isolated_symbol=isolated_symbol,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def query_max_transfer_out_amount_user_data(
        self,
        asset: str,
        timestamp: int,
        signature: str,
        *,
        isolated_symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MarginMaxTransferableResponse:
        """- If ``isolatedSymbol`` is not sent, crossed margin data will be sent.

        Weight(IP): 50

        Args:
            asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            isolated_symbol: Isolated symbol
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Details on max transferable amount

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_max_transfer_out_amount_user_data(
            asset,
            timestamp,
            signature,
            isolated_symbol=isolated_symbol,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def query_borrow_repay_records_in_margin_account_user_data(
        self,
        asset: str,
        type_: str,
        timestamp: int,
        signature: str,
        *,
        isolated_symbol: str | None = None,
        tx_id: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MarginBorrowRepayResponse1:
        """Query borrow/repay records in Margin account

        - txId or startTime must be sent. txId takes precedence. Response in descending order
        - If an asset is sent, data within 30 days before endTime; If an asset is not sent, data within 7 days before
            endTime
        - If neither startTime nor endTime is sent, the recent 7-day data will be returned.
        - startTime set as endTime - 7 days by default, endTime set as current time by default

        Weight(IP): 10

        Args:
            asset: Value sent with the request.
            type_: BORROW or REPAY
            timestamp: UTC timestamp in ms
            signature: Signature
            isolated_symbol: Isolated symbol
            tx_id: tranId in POST /sapi/v1/margin/loan
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Margin account borrow/repay

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_borrow_repay_records_in_margin_account_user_data(
            asset,
            type_,
            timestamp,
            signature,
            isolated_symbol=isolated_symbol,
            tx_id=tx_id,
            start_time=start_time,
            end_time=end_time,
            current=current,
            size=size,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def toggle_bnb_burn_on_spot_trade_and_margin_interest_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        spot_bnb_burn: SpotBnbburnOrStr | None = None,
        interest_bnb_burn: InterestBnbburnOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BnbBurnStatus:
        """- "spotBNBBurn" and "interestBNBBurn" should be sent at least one.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            spot_bnb_burn: Determines whether to use BNB to pay for trading fees on SPOT
            interest_bnb_burn: Determines whether to use BNB to pay for margin loan's interest
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Status on BNB to pay for trading fees

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.toggle_bnb_burn_on_spot_trade_and_margin_interest_user_data(
            timestamp,
            signature,
            spot_bnb_burn=spot_bnb_burn,
            interest_bnb_burn=interest_bnb_burn,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> MarginWithRawResponse:
        return self._with_raw_response


class AsyncMargin:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMarginWithRawResponse(client, server, auth)

    async def adjust_cross_margin_max_leverage_user_data(
        self,
        max_leverage: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MarginMaxLeverageResponse:
        """Adjust cross margin max leverage

        Weight(UID): 3000

        Args:
            max_leverage: Can only adjust 3 or 5
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Adjust result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.adjust_cross_margin_max_leverage_user_data(
                max_leverage, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def cross_margin_collateral_ratio_market_data(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[SapiV1MarginCrossMarginCollateralRatioResponse]:
        """Weight(IP): 100

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Margin collateral ratio

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.cross_margin_collateral_ratio_market_data(request_options=request_options)
        ).unwrap()

    async def disable_isolated_margin_account_trade(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MarginIsolatedAccountResponse:
        """Disable isolated margin account for a specific symbol. Each trading pair can only be deactivated once every
        24 hours .

        Weight(UID): 300

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Isolated Margin Account status

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.disable_isolated_margin_account_trade(
                symbol, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def enable_isolated_margin_account_trade(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MarginIsolatedAccountResponse:
        """Enable isolated margin account for a specific symbol.

        Weight(UID): 300

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Isolated Margin Account status

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.enable_isolated_margin_account_trade(
                symbol, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def get_all_cross_margin_pairs_market_data(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[SapiV1MarginAllPairsResponse]:
        """Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Margin pairs

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_all_cross_margin_pairs_market_data(
                symbol, request_options=request_options
            )
        ).unwrap()

    async def get_all_isolated_margin_symbol_user_data(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1MarginIsolatedAllPairsResponse]:
        """Weight(IP): 10

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            All Isolated Margin Symbols

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_all_isolated_margin_symbol_user_data(
                symbol, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def get_all_margin_assets_market_data(
        self, asset: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[SapiV1MarginAllAssetsResponse]:
        """Weight(IP): 1

        Args:
            asset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Assets details

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_all_margin_assets_market_data(asset, request_options=request_options)
        ).unwrap()

    async def get_bnb_burn_status_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BnbBurnStatus:
        """Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Status on BNB to pay for trading fees

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_bnb_burn_status_user_data(
                timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def get_cross_margin_transfer_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        type_: Type2OrStr | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        isolated_symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MarginTransferResponse:
        """- Response in descending order
        - Returns data for last 7 days by default
        - Set ``archived`` to ``true`` to query data from 6 months ago

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            type_: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            isolated_symbol: Isolated symbol
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Margin account transfer history, response in descending order

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_cross_margin_transfer_history_user_data(
                timestamp,
                signature,
                asset=asset,
                type_=type_,
                start_time=start_time,
                end_time=end_time,
                current=current,
                size=size,
                isolated_symbol=isolated_symbol,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def get_force_liquidation_record_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        isolated_symbol: str | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MarginForceLiquidationRecResponse:
        """- Response in descending order

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            isolated_symbol: Isolated symbol
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Force Liquidation History, response in descending order

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_force_liquidation_record_user_data(
                timestamp,
                signature,
                start_time=start_time,
                end_time=end_time,
                isolated_symbol=isolated_symbol,
                current=current,
                size=size,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def get_interest_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        isolated_symbol: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        archived: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MarginInterestHistoryResponse:
        """- Response in descending order
        - If ``isolatedSymbol`` is not sent, crossed margin data will be returned
        - Set ``archived`` to ``true`` to query data from 6 months ago
        - ``type`` in response has 4 enums:
          - ``PERIODIC`` interest charged per hour
          - ``ON_BORROW`` first interest charged on borrow
          - ``PERIODIC_CONVERTED`` interest charged per hour converted into BNB
          - ``ON_BORROW_CONVERTED`` first interest charged on borrow converted into BNB

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            isolated_symbol: Isolated symbol
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            archived: Default: false. Set to true for archived data from 6 months ago
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Interest History, response in descending order

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_interest_history_user_data(
                timestamp,
                signature,
                asset=asset,
                isolated_symbol=isolated_symbol,
                start_time=start_time,
                end_time=end_time,
                current=current,
                size=size,
                archived=archived,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def get_small_liability_exchange_coin_list_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1MarginExchangeSmallLiabilityResponse]:
        """Query the coins which can be small liability exchange

        Weight(UID): 100

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            coin list

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_small_liability_exchange_coin_list_user_data(
                timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def get_small_liability_exchange_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        current: int | None = None,
        size: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MarginExchangeSmallLiabilityHistoryResponse:
        """Get Small liability Exchange History

        Weight(UID): 100

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            coin list

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_small_liability_exchange_history_user_data(
                timestamp,
                signature,
                current=current,
                size=size,
                start_time=start_time,
                end_time=end_time,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def get_summary_of_margin_account_user_data(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MarginTradeCoeffResponse:
        """Get personal margin level information

        Weight(IP): 10

        Args:
            email: Email Address
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Summary of Margin Account

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_summary_of_margin_account_user_data(
                email, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def get_a_future_hourly_interest_rate_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        assets: str | None = None,
        is_isolated: IsIsolatedOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1MarginNextHourlyInterestRateResponse]:
        """Get user the next hourly estimate interest

        Weight(UID): 100

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            assets: List of assets, separated by commas, up to 20
            is_isolated: for isolated margin or not, "TRUE", "FALSE"
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            hourly interest

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_a_future_hourly_interest_rate_user_data(
                timestamp,
                signature,
                assets=assets,
                is_isolated=is_isolated,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def get_cross_or_isolated_margin_capital_flow_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        symbol: str | None = None,
        type_: Type3OrStr | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        from_id: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1MarginCapitalFlowResponse]:
        """Get cross or isolated margin capital flow

        Weight(IP): 100

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            symbol: Required when querying isolated data
            type_: Value sent with the request.
            start_time: Only supports querying the data of the last 90 days
            end_time: UTC timestamp in ms
            from_id: If fromId is set, the data with id > fromId will be returned. Otherwise the latest data will be
                returned
            limit: The number of data items returned each time is limited. Default 500; Max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Margin capital flow

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_cross_or_isolated_margin_capital_flow_user_data(
                timestamp,
                signature,
                asset=asset,
                symbol=symbol,
                type_=type_,
                start_time=start_time,
                end_time=end_time,
                from_id=from_id,
                limit=limit,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def get_tokens_or_symbols_delist_schedule_for_cross_margin_and_isolated_margin_market_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1MarginDelistScheduleResponse]:
        """Get tokens or symbols delist schedule for cross margin and isolated margin

        Weight(IP): 100

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            tokens or symbols delist schedule

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_tokens_or_symbols_delist_schedule_for_cross_margin_and_isolated_margin_market_data(
                timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def margin_account_cancel_oco_trade(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        order_list_id: int | None = None,
        list_client_order_id: str | None = None,
        new_client_order_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MarginOcoOrder:
        """Cancel an entire Order List for a margin account

        - Canceling an individual leg will cancel the entire OCO
        - Either ``orderListId`` or ``listClientOrderId`` must be provided

        Weight(UID): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            order_list_id: Order list id
            list_client_order_id: A unique Id for the entire orderList
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Margin OCO details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.margin_account_cancel_oco_trade(
                symbol,
                timestamp,
                signature,
                is_isolated=is_isolated,
                order_list_id=order_list_id,
                list_client_order_id=list_client_order_id,
                new_client_order_id=new_client_order_id,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def margin_account_cancel_order_trade(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        order_id: int | None = None,
        orig_client_order_id: str | None = None,
        new_client_order_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MarginOrder:
        """Cancel an active order for margin account.

        Either ``orderId`` or ``origClientOrderId`` must be sent.

        Weight(IP): 10

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            order_id: Order id
            orig_client_order_id: Order id from client
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Cancelled margin order details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.margin_account_cancel_order_trade(
                symbol,
                timestamp,
                signature,
                is_isolated=is_isolated,
                order_id=order_id,
                orig_client_order_id=orig_client_order_id,
                new_client_order_id=new_client_order_id,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def margin_account_cancel_all_open_orders_on_a_symbol_trade(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1MarginOpenOrdersResponse]:
        """- Cancels all active orders on a symbol for margin account.
        - This includes OCO orders.

        Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Cancelled margin orders

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.margin_account_cancel_all_open_orders_on_a_symbol_trade(
                symbol,
                timestamp,
                signature,
                is_isolated=is_isolated,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def margin_account_new_oco_trade(
        self,
        symbol: str,
        side: SideOrStr,
        quantity: float,
        price: float,
        stop_price: float,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        list_client_order_id: str | None = None,
        limit_client_order_id: str | None = None,
        limit_iceberg_qty: float | None = None,
        stop_client_order_id: str | None = None,
        stop_limit_price: float | None = None,
        stop_iceberg_qty: float | None = None,
        stop_limit_time_in_force: StopLimitTimeInForceOrStr | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        side_effect_type: SideEffectTypeOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MarginOrderOcoResponse:
        """Send in a new OCO for a margin account

        - Price Restrictions:
          - SELL: Limit Price > Last Price > Stop Price
          - BUY: Limit Price < Last Price < Stop Price
        - Quantity Restrictions:
          - Both legs must have the same quantity
          - ICEBERG quantities however do not have to be the same.
        - Order Rate Limit
          - OCO counts as 2 orders against the order rate limit.

        Weight(UID): 6

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            quantity: Value sent with the request.
            price: Order price
            stop_price: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            list_client_order_id: A unique Id for the entire orderList
            limit_client_order_id: A unique Id for the limit order
            limit_iceberg_qty: Value sent with the request.
            stop_client_order_id: A unique Id for the stop loss/stop loss limit leg
            stop_limit_price: If provided, stopLimitTimeInForce is required.
            stop_iceberg_qty: Value sent with the request.
            stop_limit_time_in_force: Value sent with the request.
            new_order_resp_type: Set the response JSON.
            side_effect_type: Default ``NO_SIDE_EFFECT``
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            New Margin OCO details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.margin_account_new_oco_trade(
                symbol,
                side,
                quantity,
                price,
                stop_price,
                timestamp,
                signature,
                is_isolated=is_isolated,
                list_client_order_id=list_client_order_id,
                limit_client_order_id=limit_client_order_id,
                limit_iceberg_qty=limit_iceberg_qty,
                stop_client_order_id=stop_client_order_id,
                stop_limit_price=stop_limit_price,
                stop_iceberg_qty=stop_iceberg_qty,
                stop_limit_time_in_force=stop_limit_time_in_force,
                new_order_resp_type=new_order_resp_type,
                side_effect_type=side_effect_type,
                self_trade_prevention_mode=self_trade_prevention_mode,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def margin_account_new_oto_trade(
        self,
        symbol: str,
        working_type: WorkingTypeOrStr,
        working_side: WorkingSideOrStr,
        working_price: float,
        working_quantity: float,
        working_iceberg_qty: float,
        pending_type: PendingTypeOrStr,
        pending_side: PendingSideOrStr,
        pending_quantity: float,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        list_client_order_id: str | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        side_effect_type: SideEffectType1OrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        auto_repay_at_cancel: bool | None = None,
        working_client_order_id: str | None = None,
        working_time_in_force: WorkingTimeInForceOrStr | None = None,
        pending_client_order_id: str | None = None,
        pending_price: float | None = None,
        pending_stop_price: float | None = None,
        pending_trailing_delta: float | None = None,
        pending_iceberg_qty: float | None = None,
        pending_time_in_force: PendingTimeInForceOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MarginOrderOtoResponse:
        """Post a new ``OTO`` order for margin account:
        - An ``OTO`` (One-Triggers-the-Other) is an order list comprised of 2 orders
        - The first order is called the working order and must be ``LIMIT`` or ``LIMIT_MAKER``. Initially, only the
            working order goes on the order book.
        - The second order is called the pending order. It can be any order type except for ``MARKET`` orders using
            parameter ``quoteOrderQty``. The pending order is only placed on the order book when the working order gets
            fully filled.
        - If either the working order or the pending order is cancelled individually, the other order in the order list
            will also be canceled or expired.
        - When the order list is placed, if the working order gets immediately fully filled, the placement response will
            show the working order as ``FILLED`` but the pending order will still appear as ``PENDING_NEW``. You need to
            query the status of the pending order again to see its updated status.
        - OTOs add 2 orders to the unfilled order count, ``EXCHANGE_MAX_NUM_ORDERS`` filter and ``MAX_NUM_ORDERS``
            filter.

        Weight(UID): 6

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            working_type: Supported values: LIMIT,LIMIT_MAKER
            working_side: BUY,SELL
            working_price: Value sent with the request.
            working_quantity: Sets the quantity for the working order.
            working_iceberg_qty: This can only be used if workingTimeInForce is GTC.
            pending_type: Supported values: Order Types Note that MARKET orders using quoteOrderQty are not supported.
            pending_side: BUY,SELL
            pending_quantity: Sets the quantity for the pending order.
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            list_client_order_id: Arbitrary unique ID among open order lists. Automatically generated if not sent. A new
                order list with the same ``listClientOrderId`` is accepted only when the previous one is filled or
                completely expired. ``listClientOrderId`` is distinct from the ``workingClientOrderId`` and the
                ``pendingClientOrderId``.
            new_order_resp_type: Set the response JSON.
            side_effect_type: Default ``NO_SIDE_EFFECT``
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            auto_repay_at_cancel: Only when MARGIN_BUY order takes effect, true means that the debt generated by the
                order needs to be repay after the order is cancelled. The default is true
            working_client_order_id: Arbitrary unique ID among open orders for the working order. Automatically
                generated if not sent.
            working_time_in_force: GTC, IOC, FOK
            pending_client_order_id: Arbitrary unique ID among open orders for the pending order. Automatically
                generated if not sent.
            pending_price: Value sent with the request.
            pending_stop_price: Value sent with the request.
            pending_trailing_delta: Value sent with the request.
            pending_iceberg_qty: This can only be used if pendingTimeInForce is GTC.
            pending_time_in_force: GTC, IOC, FOK
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OTO order

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.margin_account_new_oto_trade(
                symbol,
                working_type,
                working_side,
                working_price,
                working_quantity,
                working_iceberg_qty,
                pending_type,
                pending_side,
                pending_quantity,
                timestamp,
                signature,
                is_isolated=is_isolated,
                list_client_order_id=list_client_order_id,
                new_order_resp_type=new_order_resp_type,
                side_effect_type=side_effect_type,
                self_trade_prevention_mode=self_trade_prevention_mode,
                auto_repay_at_cancel=auto_repay_at_cancel,
                working_client_order_id=working_client_order_id,
                working_time_in_force=working_time_in_force,
                pending_client_order_id=pending_client_order_id,
                pending_price=pending_price,
                pending_stop_price=pending_stop_price,
                pending_trailing_delta=pending_trailing_delta,
                pending_iceberg_qty=pending_iceberg_qty,
                pending_time_in_force=pending_time_in_force,
                request_options=request_options,
            )
        ).unwrap()

    async def margin_account_new_otoco_trade(
        self,
        symbol: str,
        working_type: WorkingTypeOrStr,
        working_side: WorkingSideOrStr,
        working_price: float,
        working_quantity: float,
        working_iceberg_qty: float,
        pending_side: PendingSideOrStr,
        pending_quantity: float,
        pending_above_type: PendingAboveTypeOrStr,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        side_effect_type: SideEffectType1OrStr | None = None,
        auto_repay_at_cancel: bool | None = None,
        list_client_order_id: str | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        working_client_order_id: str | None = None,
        working_time_in_force: WorkingTimeInForceOrStr | None = None,
        pending_above_client_order_id: str | None = None,
        pending_above_price: float | None = None,
        pending_above_stop_price: float | None = None,
        pending_above_trailing_delta: float | None = None,
        pending_above_iceberg_qty: float | None = None,
        pending_above_time_in_force: PendingAboveTimeInForceOrStr | None = None,
        pending_below_type: PendingBelowTypeOrStr | None = None,
        pending_below_client_order_id: str | None = None,
        pending_below_price: float | None = None,
        pending_below_stop_price: float | None = None,
        pending_below_trailing_delta: float | None = None,
        pending_below_iceberg_qty: float | None = None,
        pending_below_time_in_force: PendingBelowTimeInForceOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MarginOrderOtocoResponse:
        """Post a new ``OTOCO`` order for margin account:
        - An ``OTOCO`` (One-Triggers-the-Other-Cancel-the-Other) is an order list comprised of 3 orders
        - The first order is called the working order and must be ``LIMIT`` or ``LIMIT_MAKER``. Initially, only the
            working order goes on the order book.
          - The behavior of the working order is the same as the ``OTO``.
        - ``OTOCO`` has 2 pending orders (pending above and pending below), forming an ``OCO`` pair. The pending orders
            are only placed on the order book when the working order gets fully filled.
          - The rules of the pending above and pending below follow the same rules as the Order List ``OCO``.
        - OTOCOs add 3 orders to the unfilled order count, ``EXCHANGE_MAX_NUM_ORDERS`` filter and ``MAX_NUM_ORDERS``
            filter.

        Weight(UID): 6

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            working_type: Supported values: LIMIT,LIMIT_MAKER
            working_side: BUY,SELL
            working_price: Value sent with the request.
            working_quantity: Sets the quantity for the working order.
            working_iceberg_qty: This can only be used if workingTimeInForce is GTC.
            pending_side: BUY,SELL
            pending_quantity: Sets the quantity for the pending order.
            pending_above_type: Supported values: LIMIT_MAKER, STOP_LOSS, and STOP_LOSS_LIMIT
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            side_effect_type: Default ``NO_SIDE_EFFECT``
            auto_repay_at_cancel: Only when MARGIN_BUY order takes effect, true means that the debt generated by the
                order needs to be repay after the order is cancelled. The default is true
            list_client_order_id: Arbitrary unique ID among open order lists. Automatically generated if not sent. A new
                order list with the same ``listClientOrderId`` is accepted only when the previous one is filled or
                completely expired. ``listClientOrderId`` is distinct from the ``workingClientOrderId`` and the
                ``pendingClientOrderId``.
            new_order_resp_type: Set the response JSON.
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            working_client_order_id: Arbitrary unique ID among open orders for the working order. Automatically
                generated if not sent.
            working_time_in_force: GTC, IOC, FOK
            pending_above_client_order_id: Arbitrary unique ID among open orders for the pending above order.
                Automatically generated if not sent.
            pending_above_price: Value sent with the request.
            pending_above_stop_price: Value sent with the request.
            pending_above_trailing_delta: Value sent with the request.
            pending_above_iceberg_qty: This can only be used if pendingAboveTimeInForce is GTC.
            pending_above_time_in_force: Value sent with the request.
            pending_below_type: Supported values: LIMIT_MAKER, STOP_LOSS, and STOP_LOSS_LIMIT
            pending_below_client_order_id: Arbitrary unique ID among open orders for the pending below order.
                Automatically generated if not sent.
            pending_below_price: Value sent with the request.
            pending_below_stop_price: Value sent with the request.
            pending_below_trailing_delta: Value sent with the request.
            pending_below_iceberg_qty: This can only be used if pendingBelowTimeInForce is GTC.
            pending_below_time_in_force: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OTOCO order

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.margin_account_new_otoco_trade(
                symbol,
                working_type,
                working_side,
                working_price,
                working_quantity,
                working_iceberg_qty,
                pending_side,
                pending_quantity,
                pending_above_type,
                timestamp,
                signature,
                is_isolated=is_isolated,
                side_effect_type=side_effect_type,
                auto_repay_at_cancel=auto_repay_at_cancel,
                list_client_order_id=list_client_order_id,
                new_order_resp_type=new_order_resp_type,
                self_trade_prevention_mode=self_trade_prevention_mode,
                working_client_order_id=working_client_order_id,
                working_time_in_force=working_time_in_force,
                pending_above_client_order_id=pending_above_client_order_id,
                pending_above_price=pending_above_price,
                pending_above_stop_price=pending_above_stop_price,
                pending_above_trailing_delta=pending_above_trailing_delta,
                pending_above_iceberg_qty=pending_above_iceberg_qty,
                pending_above_time_in_force=pending_above_time_in_force,
                pending_below_type=pending_below_type,
                pending_below_client_order_id=pending_below_client_order_id,
                pending_below_price=pending_below_price,
                pending_below_stop_price=pending_below_stop_price,
                pending_below_trailing_delta=pending_below_trailing_delta,
                pending_below_iceberg_qty=pending_below_iceberg_qty,
                pending_below_time_in_force=pending_below_time_in_force,
                request_options=request_options,
            )
        ).unwrap()

    async def margin_account_new_order_trade(
        self,
        symbol: str,
        side: SideOrStr,
        type_: Type1OrStr,
        quantity: float,
        auto_repay_at_cancel: bool,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        quote_order_qty: float | None = None,
        price: float | None = None,
        stop_price: float | None = None,
        new_client_order_id: str | None = None,
        iceberg_qty: float | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        side_effect_type: SideEffectTypeOrStr | None = None,
        time_in_force: TimeInForceOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MarginOrderResponse:
        """Post a new order for margin account.

        Weight(UID): 6

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            type_: Order type
            quantity: Value sent with the request.
            auto_repay_at_cancel: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            quote_order_qty: Quote quantity
            price: Order price
            stop_price: Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            iceberg_qty: Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.
            new_order_resp_type: Set the response JSON.
            side_effect_type: Default ``NO_SIDE_EFFECT``
            time_in_force: Order time in force
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Margin order info

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.margin_account_new_order_trade(
                symbol,
                side,
                type_,
                quantity,
                auto_repay_at_cancel,
                timestamp,
                signature,
                is_isolated=is_isolated,
                quote_order_qty=quote_order_qty,
                price=price,
                stop_price=stop_price,
                new_client_order_id=new_client_order_id,
                iceberg_qty=iceberg_qty,
                new_order_resp_type=new_order_resp_type,
                side_effect_type=side_effect_type,
                time_in_force=time_in_force,
                self_trade_prevention_mode=self_trade_prevention_mode,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def margin_interest_rate_history_user_data(
        self,
        asset: str,
        timestamp: int,
        signature: str,
        *,
        vip_level: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1MarginInterestRateHistoryResponse]:
        """The max interval between startTime and endTime is 30 days.

        Weight(IP): 1

        Args:
            asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            vip_level: Defaults to user's vip level
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Margin Interest Rate History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.margin_interest_rate_history_user_data(
                asset,
                timestamp,
                signature,
                vip_level=vip_level,
                start_time=start_time,
                end_time=end_time,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def margin_account_borrow_repay_margin(
        self,
        asset: str,
        is_isolated: str,
        symbol: str,
        amount: float,
        type_: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MarginBorrowRepayResponse:
        """Margin account borrow/repay(MARGIN)

        Weight(UID): 3000

        Args:
            asset: Value sent with the request.
            is_isolated: TRUE for isolated margin, FALSE for crossed margin
            symbol: Trading symbol, e.g. BNBUSDT
            amount: Value sent with the request.
            type_: BORROW or REPAY
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Margin account borrow/repay

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.margin_account_borrow_repay_margin(
                asset,
                is_isolated,
                symbol,
                amount,
                type_,
                timestamp,
                signature,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def margin_manual_liquidation_margin(
        self,
        type_: Type4OrStr,
        timestamp: int,
        signature: str,
        *,
        symbol: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1MarginManualLiquidationResponse]:
        """Margin manual liquidation

        Weight(UID): 3000

        Args:
            type_: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            symbol: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Margin manual liquidation

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.margin_manual_liquidation_margin(
                type_, timestamp, signature, symbol=symbol, request_options=request_options
            )
        ).unwrap()

    async def query_cross_margin_account_details_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MarginAccountResponse:
        """Weight(IP): 10

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Margin account details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_cross_margin_account_details_user_data(
                timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def query_cross_margin_fee_data_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        vip_level: int | None = None,
        coin: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1MarginCrossMarginDataResponse]:
        """Get cross margin fee data collection with any vip level or user's current specific data as
        https://www.binance.com/en/margin-fee

        Weight(IP): 1 when coin is specified; 5 when the coin parameter is omitted

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            vip_level: Defaults to user's vip level
            coin: Coin name
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Cross Margin Fee Data

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_cross_margin_fee_data_user_data(
                timestamp,
                signature,
                vip_level=vip_level,
                coin=coin,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def query_current_margin_order_count_usage_trade(
        self,
        timestamp: int,
        signature: str,
        *,
        is_isolated: str | None = None,
        symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1MarginRateLimitOrderResponse]:
        """Displays the user's current margin order count usage for all intervals.

        Weight(IP): 20

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            symbol: isolated symbol, mandatory for isolated margin
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Usage.

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_current_margin_order_count_usage_trade(
                timestamp,
                signature,
                is_isolated=is_isolated,
                symbol=symbol,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def query_enabled_isolated_margin_account_limit_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MarginIsolatedAccountLimitResponse:
        """Query enabled isolated margin account limit.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Number of enabled Isolated Margin Account and its limit

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_enabled_isolated_margin_account_limit_user_data(
                timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def query_isolated_margin_account_info_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        symbols: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> IsolatedMarginAccountInfo:
        """- If "symbols" is not sent, all isolated assets will be returned.
        - If "symbols" is sent, only the isolated assets of the sent symbols will be returned.

        Weight(IP): 10

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            symbols: Max 5 symbols can be sent; separated by ','
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Isolated Margin Account Info when "symbols" is not sent

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_isolated_margin_account_info_user_data(
                timestamp, signature, symbols=symbols, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def query_isolated_margin_fee_data_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        vip_level: int | None = None,
        symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1MarginIsolatedMarginDataResponse]:
        """Get isolated margin fee data collection with any vip level or user's current specific data as
        https://www.binance.com/en/margin-fee

        Weight(IP): 1 when a single is specified; 10 when the symbol parameter is omitted

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            vip_level: Defaults to user's vip level
            symbol: Trading symbol, e.g. BNBUSDT
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Isolated Margin Fee Data

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_isolated_margin_fee_data_user_data(
                timestamp,
                signature,
                vip_level=vip_level,
                symbol=symbol,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def query_isolated_margin_tier_data_user_data(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        tier: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1MarginIsolatedMarginTierResponse]:
        """Get isolated margin tier data collection with any tier as https://www.binance.com/en/margin-data

        Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            tier: All margin tier data will be returned if tier is omitted
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Isolated Margin Tier Data

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_isolated_margin_tier_data_user_data(
                symbol, timestamp, signature, tier=tier, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def query_liability_coin_leverage_bracket_in_cross_margin_pro_mode_market_data(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[SapiV1MarginLeverageBracketResponse]:
        """Liability Coin Leverage Bracket in Cross Margin Pro Mode

        Weight(IP): 1

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Leverage info

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_liability_coin_leverage_bracket_in_cross_margin_pro_mode_market_data(
                request_options=request_options
            )
        ).unwrap()

    async def query_margin_account_s_all_orders_user_data(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        order_id: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[MarginOrderDetail]:
        """- If ``orderId`` is set, it will get orders >= that orderId. Otherwise most recent orders are returned.
        - For some historical orders ``cummulativeQuoteQty`` will be < 0, meaning the data is not available at this
            time.

        Weight(IP): 200

        Request Limit: 60 times/min per IP

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            order_id: Order id
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Margin order list

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_margin_account_s_all_orders_user_data(
                symbol,
                timestamp,
                signature,
                is_isolated=is_isolated,
                order_id=order_id,
                start_time=start_time,
                end_time=end_time,
                limit=limit,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def query_margin_account_s_oco_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        symbol: str | None = None,
        order_list_id: int | None = None,
        orig_client_order_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MarginOrderListResponse:
        """Retrieves a specific OCO based on provided optional parameters

        - Either ``orderListId`` or ``origClientOrderId`` must be provided

        Weight(IP): 10

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            symbol: Mandatory for isolated margin, not supported for cross margin
            order_list_id: Order list id
            orig_client_order_id: Order id from client
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Margin OCO details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_margin_account_s_oco_user_data(
                timestamp,
                signature,
                is_isolated=is_isolated,
                symbol=symbol,
                order_list_id=order_list_id,
                orig_client_order_id=orig_client_order_id,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def query_margin_account_s_open_oco_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1MarginOpenOrderListResponse]:
        """Weight(IP): 10

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            symbol: Mandatory for isolated margin, not supported for cross margin
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of Open Margin OCO orders

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_margin_account_s_open_oco_user_data(
                timestamp,
                signature,
                is_isolated=is_isolated,
                symbol=symbol,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def query_margin_account_s_open_orders_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        symbol: str | None = None,
        is_isolated: IsIsolatedOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[MarginOrderDetail]:
        """- If the ``symbol`` is not sent, orders for all symbols will be returned in an array.
        - When all symbols are returned, the number of requests counted against the rate limiter is equal to the number
            of symbols currently trading on the exchange
        - If isIsolated ="TRUE", symbol must be sent.

        Weight(IP): 10

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            symbol: Trading symbol, e.g. BNBUSDT
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Margin open orders list

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_margin_account_s_open_orders_user_data(
                timestamp,
                signature,
                symbol=symbol,
                is_isolated=is_isolated,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def query_margin_account_s_order_user_data(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        order_id: int | None = None,
        orig_client_order_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MarginOrderDetail:
        """- Either ``orderId`` or ``origClientOrderId`` must be sent.
        - For some historical orders ``cummulativeQuoteQty`` will be < 0, meaning the data is not available at this
            time.

        Weight(IP): 10

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            order_id: Order id
            orig_client_order_id: Order id from client
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Interest History, response in descending order

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_margin_account_s_order_user_data(
                symbol,
                timestamp,
                signature,
                is_isolated=is_isolated,
                order_id=order_id,
                orig_client_order_id=orig_client_order_id,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def query_margin_account_s_trade_list_user_data(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        from_id: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[MarginTrade]:
        """- If ``fromId`` is set, it will get orders >= that ``fromId``. Otherwise most recent trades are returned.

        Weight(IP): 10

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            from_id: Trade id to fetch from. Default gets most recent trades.
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of margin trades

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_margin_account_s_trade_list_user_data(
                symbol,
                timestamp,
                signature,
                is_isolated=is_isolated,
                start_time=start_time,
                end_time=end_time,
                from_id=from_id,
                limit=limit,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def query_margin_account_s_all_oco_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        symbol: str | None = None,
        from_id: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1MarginAllOrderListResponse]:
        """Retrieves all OCO for a specific margin account based on provided optional parameters

        Weight(IP): 200

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            symbol: Mandatory for isolated margin, not supported for cross margin
            from_id: If supplied, neither ``startTime`` or ``endTime`` can be provided
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default Value: 500; Max Value: 1000
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of Margin OCO orders

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_margin_account_s_all_oco_user_data(
                timestamp,
                signature,
                is_isolated=is_isolated,
                symbol=symbol,
                from_id=from_id,
                start_time=start_time,
                end_time=end_time,
                limit=limit,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def query_margin_available_inventory_user_data(
        self, type_: Type4OrStr, timestamp: int, signature: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SapiV1MarginAvailableInventoryResponse:
        """Margin available Inventory query

        Weight(UID): 50

        Args:
            type_: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Margin available Inventory

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_margin_available_inventory_user_data(
                type_, timestamp, signature, request_options=request_options
            )
        ).unwrap()

    async def query_margin_price_index_market_data(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SapiV1MarginPriceIndexResponse:
        """Weight(IP): 10

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Price index

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_margin_price_index_market_data(symbol, request_options=request_options)
        ).unwrap()

    async def query_max_borrow_user_data(
        self,
        asset: str,
        timestamp: int,
        signature: str,
        *,
        isolated_symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MarginMaxBorrowableResponse:
        """- If ``isolatedSymbol`` is not sent, crossed margin data will be sent.
        - ``borrowLimit`` is also available from https://www.binance.com/en/margin-fee

        Weight(IP): 50

        Args:
            asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            isolated_symbol: Isolated symbol
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Details on max borrow amount

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_max_borrow_user_data(
                asset,
                timestamp,
                signature,
                isolated_symbol=isolated_symbol,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def query_max_transfer_out_amount_user_data(
        self,
        asset: str,
        timestamp: int,
        signature: str,
        *,
        isolated_symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MarginMaxTransferableResponse:
        """- If ``isolatedSymbol`` is not sent, crossed margin data will be sent.

        Weight(IP): 50

        Args:
            asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            isolated_symbol: Isolated symbol
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Details on max transferable amount

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_max_transfer_out_amount_user_data(
                asset,
                timestamp,
                signature,
                isolated_symbol=isolated_symbol,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def query_borrow_repay_records_in_margin_account_user_data(
        self,
        asset: str,
        type_: str,
        timestamp: int,
        signature: str,
        *,
        isolated_symbol: str | None = None,
        tx_id: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MarginBorrowRepayResponse1:
        """Query borrow/repay records in Margin account

        - txId or startTime must be sent. txId takes precedence. Response in descending order
        - If an asset is sent, data within 30 days before endTime; If an asset is not sent, data within 7 days before
            endTime
        - If neither startTime nor endTime is sent, the recent 7-day data will be returned.
        - startTime set as endTime - 7 days by default, endTime set as current time by default

        Weight(IP): 10

        Args:
            asset: Value sent with the request.
            type_: BORROW or REPAY
            timestamp: UTC timestamp in ms
            signature: Signature
            isolated_symbol: Isolated symbol
            tx_id: tranId in POST /sapi/v1/margin/loan
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Margin account borrow/repay

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_borrow_repay_records_in_margin_account_user_data(
                asset,
                type_,
                timestamp,
                signature,
                isolated_symbol=isolated_symbol,
                tx_id=tx_id,
                start_time=start_time,
                end_time=end_time,
                current=current,
                size=size,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def toggle_bnb_burn_on_spot_trade_and_margin_interest_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        spot_bnb_burn: SpotBnbburnOrStr | None = None,
        interest_bnb_burn: InterestBnbburnOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BnbBurnStatus:
        """- "spotBNBBurn" and "interestBNBBurn" should be sent at least one.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            spot_bnb_burn: Determines whether to use BNB to pay for trading fees on SPOT
            interest_bnb_burn: Determines whether to use BNB to pay for margin loan's interest
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Status on BNB to pay for trading fees

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.toggle_bnb_burn_on_spot_trade_and_margin_interest_user_data(
                timestamp,
                signature,
                spot_bnb_burn=spot_bnb_burn,
                interest_bnb_burn=interest_bnb_burn,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncMarginWithRawResponse:
        return self._with_raw_response


class MarginWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def adjust_cross_margin_max_leverage_user_data(
        self,
        max_leverage: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MarginMaxLeverageResponse, AdjustCrossMarginMaxLeverageUserDataErrorBody]:
        """Adjust cross margin max leverage

        Weight(UID): 3000

        Args:
            max_leverage: Can only adjust 3 or 5
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/margin/max-leverage"),
            query_params=[
                param[int]("maxLeverage", max_leverage),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginMaxLeverageResponse],
            error_mapper=adjust_cross_margin_max_leverage_user_data_error_mapper,
            request_options=request_options,
        )

    def cross_margin_collateral_ratio_market_data(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[SapiV1MarginCrossMarginCollateralRatioResponse], CrossMarginCollateralRatioMarketDataErrorBody]:
        """Weight(IP): 100

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/crossMarginCollateralRatio"),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1MarginCrossMarginCollateralRatioResponse]],
            error_mapper=cross_margin_collateral_ratio_market_data_error_mapper,
            request_options=request_options,
        )

    def disable_isolated_margin_account_trade(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MarginIsolatedAccountResponse, DisableIsolatedMarginAccountTradeErrorBody]:
        """Disable isolated margin account for a specific symbol. Each trading pair can only be deactivated once every
        24 hours .

        Weight(UID): 300

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/sapi/v1/margin/isolated/account"),
            query_params=[
                param[str]("symbol", symbol),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginIsolatedAccountResponse],
            error_mapper=disable_isolated_margin_account_trade_error_mapper,
            request_options=request_options,
        )

    def enable_isolated_margin_account_trade(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MarginIsolatedAccountResponse, EnableIsolatedMarginAccountTradeErrorBody]:
        """Enable isolated margin account for a specific symbol.

        Weight(UID): 300

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/margin/isolated/account"),
            query_params=[
                param[str]("symbol", symbol),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginIsolatedAccountResponse],
            error_mapper=enable_isolated_margin_account_trade_error_mapper,
            request_options=request_options,
        )

    def get_all_cross_margin_pairs_market_data(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[SapiV1MarginAllPairsResponse], GetAllCrossMarginPairsMarketDataErrorBody]:
        """Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/allPairs"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1MarginAllPairsResponse]],
            error_mapper=get_all_cross_margin_pairs_market_data_error_mapper,
            request_options=request_options,
        )

    def get_all_isolated_margin_symbol_user_data(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1MarginIsolatedAllPairsResponse], GetAllIsolatedMarginSymbolUserDataErrorBody]:
        """Weight(IP): 10

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/isolated/allPairs"),
            query_params=[
                param[str]("symbol", symbol),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1MarginIsolatedAllPairsResponse]],
            error_mapper=get_all_isolated_margin_symbol_user_data_error_mapper,
            request_options=request_options,
        )

    def get_all_margin_assets_market_data(
        self, asset: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[SapiV1MarginAllAssetsResponse], GetAllMarginAssetsMarketDataErrorBody]:
        """Weight(IP): 1

        Args:
            asset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/allAssets"),
            query_params=[param[str]("asset", asset)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1MarginAllAssetsResponse]],
            error_mapper=get_all_margin_assets_market_data_error_mapper,
            request_options=request_options,
        )

    def get_bnb_burn_status_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BnbBurnStatus, GetBnbBurnStatusUserDataErrorBody]:
        """Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/bnbBurn"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[BnbBurnStatus],
            error_mapper=get_bnb_burn_status_user_data_error_mapper,
            request_options=request_options,
        )

    def get_cross_margin_transfer_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        type_: Type2OrStr | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        isolated_symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MarginTransferResponse, GetCrossMarginTransferHistoryUserDataErrorBody]:
        """- Response in descending order
        - Returns data for last 7 days by default
        - Set ``archived`` to ``true`` to query data from 6 months ago

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            type_: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            isolated_symbol: Isolated symbol
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/transfer"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("asset", asset),
                param[Type2OrStr | None]("type", type_),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[str | None]("isolatedSymbol", isolated_symbol),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginTransferResponse],
            error_mapper=get_cross_margin_transfer_history_user_data_error_mapper,
            request_options=request_options,
        )

    def get_force_liquidation_record_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        isolated_symbol: str | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MarginForceLiquidationRecResponse, GetForceLiquidationRecordUserDataErrorBody]:
        """- Response in descending order

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            isolated_symbol: Isolated symbol
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/forceLiquidationRec"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[str | None]("isolatedSymbol", isolated_symbol),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginForceLiquidationRecResponse],
            error_mapper=get_force_liquidation_record_user_data_error_mapper,
            request_options=request_options,
        )

    def get_interest_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        isolated_symbol: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        archived: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MarginInterestHistoryResponse, GetInterestHistoryUserDataErrorBody]:
        """- Response in descending order
        - If ``isolatedSymbol`` is not sent, crossed margin data will be returned
        - Set ``archived`` to ``true`` to query data from 6 months ago
        - ``type`` in response has 4 enums:
          - ``PERIODIC`` interest charged per hour
          - ``ON_BORROW`` first interest charged on borrow
          - ``PERIODIC_CONVERTED`` interest charged per hour converted into BNB
          - ``ON_BORROW_CONVERTED`` first interest charged on borrow converted into BNB

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            isolated_symbol: Isolated symbol
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            archived: Default: false. Set to true for archived data from 6 months ago
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/interestHistory"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("asset", asset),
                param[str | None]("isolatedSymbol", isolated_symbol),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[str | None]("archived", archived),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginInterestHistoryResponse],
            error_mapper=get_interest_history_user_data_error_mapper,
            request_options=request_options,
        )

    def get_small_liability_exchange_coin_list_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        list[SapiV1MarginExchangeSmallLiabilityResponse], GetSmallLiabilityExchangeCoinListUserDataErrorBody
    ]:
        """Query the coins which can be small liability exchange

        Weight(UID): 100

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/exchange-small-liability"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1MarginExchangeSmallLiabilityResponse]],
            error_mapper=get_small_liability_exchange_coin_list_user_data_error_mapper,
            request_options=request_options,
        )

    def get_small_liability_exchange_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        current: int | None = None,
        size: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1MarginExchangeSmallLiabilityHistoryResponse, GetSmallLiabilityExchangeHistoryUserDataErrorBody
    ]:
        """Get Small liability Exchange History

        Weight(UID): 100

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/exchange-small-liability-history"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginExchangeSmallLiabilityHistoryResponse],
            error_mapper=get_small_liability_exchange_history_user_data_error_mapper,
            request_options=request_options,
        )

    def get_summary_of_margin_account_user_data(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MarginTradeCoeffResponse, GetSummaryOfMarginAccountUserDataErrorBody]:
        """Get personal margin level information

        Weight(IP): 10

        Args:
            email: Email Address
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/tradeCoeff"),
            query_params=[
                param[str]("email", email),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginTradeCoeffResponse],
            error_mapper=get_summary_of_margin_account_user_data_error_mapper,
            request_options=request_options,
        )

    def get_a_future_hourly_interest_rate_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        assets: str | None = None,
        is_isolated: IsIsolatedOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1MarginNextHourlyInterestRateResponse], GetAFutureHourlyInterestRateUserDataErrorBody]:
        """Get user the next hourly estimate interest

        Weight(UID): 100

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            assets: List of assets, separated by commas, up to 20
            is_isolated: for isolated margin or not, "TRUE", "FALSE"
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/next-hourly-interest-rate"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("assets", assets),
                param[IsIsolatedOrStr | None]("isIsolated", is_isolated),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1MarginNextHourlyInterestRateResponse]],
            error_mapper=get_a_future_hourly_interest_rate_user_data_error_mapper,
            request_options=request_options,
        )

    def get_cross_or_isolated_margin_capital_flow_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        symbol: str | None = None,
        type_: Type3OrStr | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        from_id: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1MarginCapitalFlowResponse], GetCrossOrIsolatedMarginCapitalFlowUserDataErrorBody]:
        """Get cross or isolated margin capital flow

        Weight(IP): 100

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            symbol: Required when querying isolated data
            type_: Value sent with the request.
            start_time: Only supports querying the data of the last 90 days
            end_time: UTC timestamp in ms
            from_id: If fromId is set, the data with id > fromId will be returned. Otherwise the latest data will be
                returned
            limit: The number of data items returned each time is limited. Default 500; Max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/capital-flow"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("asset", asset),
                param[str | None]("symbol", symbol),
                param[Type3OrStr | None]("type", type_),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("fromId", from_id),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1MarginCapitalFlowResponse]],
            error_mapper=get_cross_or_isolated_margin_capital_flow_user_data_error_mapper,
            request_options=request_options,
        )

    def get_tokens_or_symbols_delist_schedule_for_cross_margin_and_isolated_margin_market_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        list[SapiV1MarginDelistScheduleResponse],
        GetTokensOrSymbolsDelistScheduleForCrossMarginAndIsolatedMarginMarketDataErrorBody,
    ]:
        """Get tokens or symbols delist schedule for cross margin and isolated margin

        Weight(IP): 100

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/delist-schedule"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1MarginDelistScheduleResponse]],
            error_mapper=get_tokens_or_symbols_delist_schedule_for_cross_margin_and_isolated_margin_market_data_error_mapper,
            request_options=request_options,
        )

    def margin_account_cancel_oco_trade(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        order_list_id: int | None = None,
        list_client_order_id: str | None = None,
        new_client_order_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MarginOcoOrder, MarginAccountCancelOcoTradeErrorBody]:
        """Cancel an entire Order List for a margin account

        - Canceling an individual leg will cancel the entire OCO
        - Either ``orderListId`` or ``listClientOrderId`` must be provided

        Weight(UID): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            order_list_id: Order list id
            list_client_order_id: A unique Id for the entire orderList
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/sapi/v1/margin/orderList"),
            query_params=[
                param[str]("symbol", symbol),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[IsIsolatedOrStr | None]("isIsolated", is_isolated),
                param[int | None]("orderListId", order_list_id),
                param[str | None]("listClientOrderId", list_client_order_id),
                param[str | None]("newClientOrderId", new_client_order_id),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[MarginOcoOrder],
            error_mapper=margin_account_cancel_oco_trade_error_mapper,
            request_options=request_options,
        )

    def margin_account_cancel_order_trade(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        order_id: int | None = None,
        orig_client_order_id: str | None = None,
        new_client_order_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MarginOrder, MarginAccountCancelOrderTradeErrorBody]:
        """Cancel an active order for margin account.

        Either ``orderId`` or ``origClientOrderId`` must be sent.

        Weight(IP): 10

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            order_id: Order id
            orig_client_order_id: Order id from client
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/sapi/v1/margin/order"),
            query_params=[
                param[str]("symbol", symbol),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[IsIsolatedOrStr | None]("isIsolated", is_isolated),
                param[int | None]("orderId", order_id),
                param[str | None]("origClientOrderId", orig_client_order_id),
                param[str | None]("newClientOrderId", new_client_order_id),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[MarginOrder],
            error_mapper=margin_account_cancel_order_trade_error_mapper,
            request_options=request_options,
        )

    def margin_account_cancel_all_open_orders_on_a_symbol_trade(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1MarginOpenOrdersResponse], MarginAccountCancelAllOpenOrdersOnASymbolTradeErrorBody]:
        """- Cancels all active orders on a symbol for margin account.
        - This includes OCO orders.

        Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/sapi/v1/margin/openOrders"),
            query_params=[
                param[str]("symbol", symbol),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[IsIsolatedOrStr | None]("isIsolated", is_isolated),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1MarginOpenOrdersResponse]],
            error_mapper=margin_account_cancel_all_open_orders_on_a_symbol_trade_error_mapper,
            request_options=request_options,
        )

    def margin_account_new_oco_trade(
        self,
        symbol: str,
        side: SideOrStr,
        quantity: float,
        price: float,
        stop_price: float,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        list_client_order_id: str | None = None,
        limit_client_order_id: str | None = None,
        limit_iceberg_qty: float | None = None,
        stop_client_order_id: str | None = None,
        stop_limit_price: float | None = None,
        stop_iceberg_qty: float | None = None,
        stop_limit_time_in_force: StopLimitTimeInForceOrStr | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        side_effect_type: SideEffectTypeOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MarginOrderOcoResponse, MarginAccountNewOcoTradeErrorBody]:
        """Send in a new OCO for a margin account

        - Price Restrictions:
          - SELL: Limit Price > Last Price > Stop Price
          - BUY: Limit Price < Last Price < Stop Price
        - Quantity Restrictions:
          - Both legs must have the same quantity
          - ICEBERG quantities however do not have to be the same.
        - Order Rate Limit
          - OCO counts as 2 orders against the order rate limit.

        Weight(UID): 6

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            quantity: Value sent with the request.
            price: Order price
            stop_price: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            list_client_order_id: A unique Id for the entire orderList
            limit_client_order_id: A unique Id for the limit order
            limit_iceberg_qty: Value sent with the request.
            stop_client_order_id: A unique Id for the stop loss/stop loss limit leg
            stop_limit_price: If provided, stopLimitTimeInForce is required.
            stop_iceberg_qty: Value sent with the request.
            stop_limit_time_in_force: Value sent with the request.
            new_order_resp_type: Set the response JSON.
            side_effect_type: Default ``NO_SIDE_EFFECT``
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/margin/order/oco"),
            query_params=[
                param[str]("symbol", symbol),
                param[SideOrStr]("side", side),
                param[float]("quantity", quantity),
                param[float]("price", price),
                param[float]("stopPrice", stop_price),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[IsIsolatedOrStr | None]("isIsolated", is_isolated),
                param[str | None]("listClientOrderId", list_client_order_id),
                param[str | None]("limitClientOrderId", limit_client_order_id),
                param[float | None]("limitIcebergQty", limit_iceberg_qty),
                param[str | None]("stopClientOrderId", stop_client_order_id),
                param[float | None]("stopLimitPrice", stop_limit_price),
                param[float | None]("stopIcebergQty", stop_iceberg_qty),
                param[StopLimitTimeInForceOrStr | None]("stopLimitTimeInForce", stop_limit_time_in_force),
                param[NewOrderRespTypeOrStr | None]("newOrderRespType", new_order_resp_type),
                param[SideEffectTypeOrStr | None]("sideEffectType", side_effect_type),
                param[SelfTradePreventionModeOrStr | None]("selfTradePreventionMode", self_trade_prevention_mode),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginOrderOcoResponse],
            error_mapper=margin_account_new_oco_trade_error_mapper,
            request_options=request_options,
        )

    def margin_account_new_oto_trade(
        self,
        symbol: str,
        working_type: WorkingTypeOrStr,
        working_side: WorkingSideOrStr,
        working_price: float,
        working_quantity: float,
        working_iceberg_qty: float,
        pending_type: PendingTypeOrStr,
        pending_side: PendingSideOrStr,
        pending_quantity: float,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        list_client_order_id: str | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        side_effect_type: SideEffectType1OrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        auto_repay_at_cancel: bool | None = None,
        working_client_order_id: str | None = None,
        working_time_in_force: WorkingTimeInForceOrStr | None = None,
        pending_client_order_id: str | None = None,
        pending_price: float | None = None,
        pending_stop_price: float | None = None,
        pending_trailing_delta: float | None = None,
        pending_iceberg_qty: float | None = None,
        pending_time_in_force: PendingTimeInForceOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MarginOrderOtoResponse, MarginAccountNewOtoTradeErrorBody]:
        """Post a new ``OTO`` order for margin account:
        - An ``OTO`` (One-Triggers-the-Other) is an order list comprised of 2 orders
        - The first order is called the working order and must be ``LIMIT`` or ``LIMIT_MAKER``. Initially, only the
            working order goes on the order book.
        - The second order is called the pending order. It can be any order type except for ``MARKET`` orders using
            parameter ``quoteOrderQty``. The pending order is only placed on the order book when the working order gets
            fully filled.
        - If either the working order or the pending order is cancelled individually, the other order in the order list
            will also be canceled or expired.
        - When the order list is placed, if the working order gets immediately fully filled, the placement response will
            show the working order as ``FILLED`` but the pending order will still appear as ``PENDING_NEW``. You need to
            query the status of the pending order again to see its updated status.
        - OTOs add 2 orders to the unfilled order count, ``EXCHANGE_MAX_NUM_ORDERS`` filter and ``MAX_NUM_ORDERS``
            filter.

        Weight(UID): 6

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            working_type: Supported values: LIMIT,LIMIT_MAKER
            working_side: BUY,SELL
            working_price: Value sent with the request.
            working_quantity: Sets the quantity for the working order.
            working_iceberg_qty: This can only be used if workingTimeInForce is GTC.
            pending_type: Supported values: Order Types Note that MARKET orders using quoteOrderQty are not supported.
            pending_side: BUY,SELL
            pending_quantity: Sets the quantity for the pending order.
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            list_client_order_id: Arbitrary unique ID among open order lists. Automatically generated if not sent. A new
                order list with the same ``listClientOrderId`` is accepted only when the previous one is filled or
                completely expired. ``listClientOrderId`` is distinct from the ``workingClientOrderId`` and the
                ``pendingClientOrderId``.
            new_order_resp_type: Set the response JSON.
            side_effect_type: Default ``NO_SIDE_EFFECT``
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            auto_repay_at_cancel: Only when MARGIN_BUY order takes effect, true means that the debt generated by the
                order needs to be repay after the order is cancelled. The default is true
            working_client_order_id: Arbitrary unique ID among open orders for the working order. Automatically
                generated if not sent.
            working_time_in_force: GTC, IOC, FOK
            pending_client_order_id: Arbitrary unique ID among open orders for the pending order. Automatically
                generated if not sent.
            pending_price: Value sent with the request.
            pending_stop_price: Value sent with the request.
            pending_trailing_delta: Value sent with the request.
            pending_iceberg_qty: This can only be used if pendingTimeInForce is GTC.
            pending_time_in_force: GTC, IOC, FOK
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/margin/order/oto"),
            query_params=[
                param[str]("symbol", symbol),
                param[WorkingTypeOrStr]("workingType", working_type),
                param[WorkingSideOrStr]("workingSide", working_side),
                param[float]("workingPrice", working_price),
                param[float]("workingQuantity", working_quantity),
                param[float]("workingIcebergQty", working_iceberg_qty),
                param[PendingTypeOrStr]("pendingType", pending_type),
                param[PendingSideOrStr]("pendingSide", pending_side),
                param[float]("pendingQuantity", pending_quantity),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[IsIsolatedOrStr | None]("isIsolated", is_isolated),
                param[str | None]("listClientOrderId", list_client_order_id),
                param[NewOrderRespTypeOrStr | None]("newOrderRespType", new_order_resp_type),
                param[SideEffectType1OrStr | None]("sideEffectType", side_effect_type),
                param[SelfTradePreventionModeOrStr | None]("selfTradePreventionMode", self_trade_prevention_mode),
                param[bool | None]("autoRepayAtCancel", auto_repay_at_cancel),
                param[str | None]("workingClientOrderId", working_client_order_id),
                param[WorkingTimeInForceOrStr | None]("workingTimeInForce", working_time_in_force),
                param[str | None]("pendingClientOrderId", pending_client_order_id),
                param[float | None]("pendingPrice", pending_price),
                param[float | None]("pendingStopPrice", pending_stop_price),
                param[float | None]("pendingTrailingDelta", pending_trailing_delta),
                param[float | None]("pendingIcebergQty", pending_iceberg_qty),
                param[PendingTimeInForceOrStr | None]("pendingTimeInForce", pending_time_in_force),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginOrderOtoResponse],
            error_mapper=margin_account_new_oto_trade_error_mapper,
            request_options=request_options,
        )

    def margin_account_new_otoco_trade(
        self,
        symbol: str,
        working_type: WorkingTypeOrStr,
        working_side: WorkingSideOrStr,
        working_price: float,
        working_quantity: float,
        working_iceberg_qty: float,
        pending_side: PendingSideOrStr,
        pending_quantity: float,
        pending_above_type: PendingAboveTypeOrStr,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        side_effect_type: SideEffectType1OrStr | None = None,
        auto_repay_at_cancel: bool | None = None,
        list_client_order_id: str | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        working_client_order_id: str | None = None,
        working_time_in_force: WorkingTimeInForceOrStr | None = None,
        pending_above_client_order_id: str | None = None,
        pending_above_price: float | None = None,
        pending_above_stop_price: float | None = None,
        pending_above_trailing_delta: float | None = None,
        pending_above_iceberg_qty: float | None = None,
        pending_above_time_in_force: PendingAboveTimeInForceOrStr | None = None,
        pending_below_type: PendingBelowTypeOrStr | None = None,
        pending_below_client_order_id: str | None = None,
        pending_below_price: float | None = None,
        pending_below_stop_price: float | None = None,
        pending_below_trailing_delta: float | None = None,
        pending_below_iceberg_qty: float | None = None,
        pending_below_time_in_force: PendingBelowTimeInForceOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MarginOrderOtocoResponse, MarginAccountNewOtocoTradeErrorBody]:
        """Post a new ``OTOCO`` order for margin account:
        - An ``OTOCO`` (One-Triggers-the-Other-Cancel-the-Other) is an order list comprised of 3 orders
        - The first order is called the working order and must be ``LIMIT`` or ``LIMIT_MAKER``. Initially, only the
            working order goes on the order book.
          - The behavior of the working order is the same as the ``OTO``.
        - ``OTOCO`` has 2 pending orders (pending above and pending below), forming an ``OCO`` pair. The pending orders
            are only placed on the order book when the working order gets fully filled.
          - The rules of the pending above and pending below follow the same rules as the Order List ``OCO``.
        - OTOCOs add 3 orders to the unfilled order count, ``EXCHANGE_MAX_NUM_ORDERS`` filter and ``MAX_NUM_ORDERS``
            filter.

        Weight(UID): 6

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            working_type: Supported values: LIMIT,LIMIT_MAKER
            working_side: BUY,SELL
            working_price: Value sent with the request.
            working_quantity: Sets the quantity for the working order.
            working_iceberg_qty: This can only be used if workingTimeInForce is GTC.
            pending_side: BUY,SELL
            pending_quantity: Sets the quantity for the pending order.
            pending_above_type: Supported values: LIMIT_MAKER, STOP_LOSS, and STOP_LOSS_LIMIT
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            side_effect_type: Default ``NO_SIDE_EFFECT``
            auto_repay_at_cancel: Only when MARGIN_BUY order takes effect, true means that the debt generated by the
                order needs to be repay after the order is cancelled. The default is true
            list_client_order_id: Arbitrary unique ID among open order lists. Automatically generated if not sent. A new
                order list with the same ``listClientOrderId`` is accepted only when the previous one is filled or
                completely expired. ``listClientOrderId`` is distinct from the ``workingClientOrderId`` and the
                ``pendingClientOrderId``.
            new_order_resp_type: Set the response JSON.
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            working_client_order_id: Arbitrary unique ID among open orders for the working order. Automatically
                generated if not sent.
            working_time_in_force: GTC, IOC, FOK
            pending_above_client_order_id: Arbitrary unique ID among open orders for the pending above order.
                Automatically generated if not sent.
            pending_above_price: Value sent with the request.
            pending_above_stop_price: Value sent with the request.
            pending_above_trailing_delta: Value sent with the request.
            pending_above_iceberg_qty: This can only be used if pendingAboveTimeInForce is GTC.
            pending_above_time_in_force: Value sent with the request.
            pending_below_type: Supported values: LIMIT_MAKER, STOP_LOSS, and STOP_LOSS_LIMIT
            pending_below_client_order_id: Arbitrary unique ID among open orders for the pending below order.
                Automatically generated if not sent.
            pending_below_price: Value sent with the request.
            pending_below_stop_price: Value sent with the request.
            pending_below_trailing_delta: Value sent with the request.
            pending_below_iceberg_qty: This can only be used if pendingBelowTimeInForce is GTC.
            pending_below_time_in_force: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/margin/order/otoco"),
            query_params=[
                param[str]("symbol", symbol),
                param[WorkingTypeOrStr]("workingType", working_type),
                param[WorkingSideOrStr]("workingSide", working_side),
                param[float]("workingPrice", working_price),
                param[float]("workingQuantity", working_quantity),
                param[float]("workingIcebergQty", working_iceberg_qty),
                param[PendingSideOrStr]("pendingSide", pending_side),
                param[float]("pendingQuantity", pending_quantity),
                param[PendingAboveTypeOrStr]("pendingAboveType", pending_above_type),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[IsIsolatedOrStr | None]("isIsolated", is_isolated),
                param[SideEffectType1OrStr | None]("sideEffectType", side_effect_type),
                param[bool | None]("autoRepayAtCancel", auto_repay_at_cancel),
                param[str | None]("listClientOrderId", list_client_order_id),
                param[NewOrderRespTypeOrStr | None]("newOrderRespType", new_order_resp_type),
                param[SelfTradePreventionModeOrStr | None]("selfTradePreventionMode", self_trade_prevention_mode),
                param[str | None]("workingClientOrderId", working_client_order_id),
                param[WorkingTimeInForceOrStr | None]("workingTimeInForce", working_time_in_force),
                param[str | None]("pendingAboveClientOrderId", pending_above_client_order_id),
                param[float | None]("pendingAbovePrice", pending_above_price),
                param[float | None]("pendingAboveStopPrice", pending_above_stop_price),
                param[float | None]("pendingAboveTrailingDelta", pending_above_trailing_delta),
                param[float | None]("pendingAboveIcebergQty", pending_above_iceberg_qty),
                param[PendingAboveTimeInForceOrStr | None]("pendingAboveTimeInForce", pending_above_time_in_force),
                param[PendingBelowTypeOrStr | None]("pendingBelowType", pending_below_type),
                param[str | None]("pendingBelowClientOrderId", pending_below_client_order_id),
                param[float | None]("pendingBelowPrice", pending_below_price),
                param[float | None]("pendingBelowStopPrice", pending_below_stop_price),
                param[float | None]("pendingBelowTrailingDelta", pending_below_trailing_delta),
                param[float | None]("pendingBelowIcebergQty", pending_below_iceberg_qty),
                param[PendingBelowTimeInForceOrStr | None]("pendingBelowTimeInForce", pending_below_time_in_force),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginOrderOtocoResponse],
            error_mapper=margin_account_new_otoco_trade_error_mapper,
            request_options=request_options,
        )

    def margin_account_new_order_trade(
        self,
        symbol: str,
        side: SideOrStr,
        type_: Type1OrStr,
        quantity: float,
        auto_repay_at_cancel: bool,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        quote_order_qty: float | None = None,
        price: float | None = None,
        stop_price: float | None = None,
        new_client_order_id: str | None = None,
        iceberg_qty: float | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        side_effect_type: SideEffectTypeOrStr | None = None,
        time_in_force: TimeInForceOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MarginOrderResponse, MarginAccountNewOrderTradeErrorBody]:
        """Post a new order for margin account.

        Weight(UID): 6

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            type_: Order type
            quantity: Value sent with the request.
            auto_repay_at_cancel: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            quote_order_qty: Quote quantity
            price: Order price
            stop_price: Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            iceberg_qty: Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.
            new_order_resp_type: Set the response JSON.
            side_effect_type: Default ``NO_SIDE_EFFECT``
            time_in_force: Order time in force
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/margin/order"),
            query_params=[
                param[str]("symbol", symbol),
                param[SideOrStr]("side", side),
                param[Type1OrStr]("type", type_),
                param[float]("quantity", quantity),
                param[bool]("autoRepayAtCancel", auto_repay_at_cancel),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[IsIsolatedOrStr | None]("isIsolated", is_isolated),
                param[float | None]("quoteOrderQty", quote_order_qty),
                param[float | None]("price", price),
                param[float | None]("stopPrice", stop_price),
                param[str | None]("newClientOrderId", new_client_order_id),
                param[float | None]("icebergQty", iceberg_qty),
                param[NewOrderRespTypeOrStr | None]("newOrderRespType", new_order_resp_type),
                param[SideEffectTypeOrStr | None]("sideEffectType", side_effect_type),
                param[TimeInForceOrStr | None]("timeInForce", time_in_force),
                param[SelfTradePreventionModeOrStr | None]("selfTradePreventionMode", self_trade_prevention_mode),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginOrderResponse],
            error_mapper=margin_account_new_order_trade_error_mapper,
            request_options=request_options,
        )

    def margin_interest_rate_history_user_data(
        self,
        asset: str,
        timestamp: int,
        signature: str,
        *,
        vip_level: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1MarginInterestRateHistoryResponse], MarginInterestRateHistoryUserDataErrorBody]:
        """The max interval between startTime and endTime is 30 days.

        Weight(IP): 1

        Args:
            asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            vip_level: Defaults to user's vip level
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/interestRateHistory"),
            query_params=[
                param[str]("asset", asset),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("vipLevel", vip_level),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1MarginInterestRateHistoryResponse]],
            error_mapper=margin_interest_rate_history_user_data_error_mapper,
            request_options=request_options,
        )

    def margin_account_borrow_repay_margin(
        self,
        asset: str,
        is_isolated: str,
        symbol: str,
        amount: float,
        type_: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MarginBorrowRepayResponse, MarginAccountBorrowRepayMarginErrorBody]:
        """Margin account borrow/repay(MARGIN)

        Weight(UID): 3000

        Args:
            asset: Value sent with the request.
            is_isolated: TRUE for isolated margin, FALSE for crossed margin
            symbol: Trading symbol, e.g. BNBUSDT
            amount: Value sent with the request.
            type_: BORROW or REPAY
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/margin/borrow-repay"),
            query_params=[
                param[str]("asset", asset),
                param[str]("isIsolated", is_isolated),
                param[str]("symbol", symbol),
                param[float]("amount", amount),
                param[str]("type", type_),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginBorrowRepayResponse],
            error_mapper=margin_account_borrow_repay_margin_error_mapper,
            request_options=request_options,
        )

    def margin_manual_liquidation_margin(
        self,
        type_: Type4OrStr,
        timestamp: int,
        signature: str,
        *,
        symbol: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1MarginManualLiquidationResponse], MarginManualLiquidationMarginErrorBody]:
        """Margin manual liquidation

        Weight(UID): 3000

        Args:
            type_: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            symbol: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/margin/manual-liquidation"),
            query_params=[
                param[Type4OrStr]("type", type_),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("symbol", symbol),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1MarginManualLiquidationResponse]],
            error_mapper=margin_manual_liquidation_margin_error_mapper,
            request_options=request_options,
        )

    def query_cross_margin_account_details_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MarginAccountResponse, QueryCrossMarginAccountDetailsUserDataErrorBody]:
        """Weight(IP): 10

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/account"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginAccountResponse],
            error_mapper=query_cross_margin_account_details_user_data_error_mapper,
            request_options=request_options,
        )

    def query_cross_margin_fee_data_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        vip_level: int | None = None,
        coin: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1MarginCrossMarginDataResponse], QueryCrossMarginFeeDataUserDataErrorBody]:
        """Get cross margin fee data collection with any vip level or user's current specific data as
        https://www.binance.com/en/margin-fee

        Weight(IP): 1 when coin is specified; 5 when the coin parameter is omitted

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            vip_level: Defaults to user's vip level
            coin: Coin name
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/crossMarginData"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("vipLevel", vip_level),
                param[str | None]("coin", coin),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1MarginCrossMarginDataResponse]],
            error_mapper=query_cross_margin_fee_data_user_data_error_mapper,
            request_options=request_options,
        )

    def query_current_margin_order_count_usage_trade(
        self,
        timestamp: int,
        signature: str,
        *,
        is_isolated: str | None = None,
        symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1MarginRateLimitOrderResponse], QueryCurrentMarginOrderCountUsageTradeErrorBody]:
        """Displays the user's current margin order count usage for all intervals.

        Weight(IP): 20

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            symbol: isolated symbol, mandatory for isolated margin
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/rateLimit/order"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("isIsolated", is_isolated),
                param[str | None]("symbol", symbol),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1MarginRateLimitOrderResponse]],
            error_mapper=query_current_margin_order_count_usage_trade_error_mapper,
            request_options=request_options,
        )

    def query_enabled_isolated_margin_account_limit_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MarginIsolatedAccountLimitResponse, QueryEnabledIsolatedMarginAccountLimitUserDataErrorBody]:
        """Query enabled isolated margin account limit.

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
            url_template=self._server.default("/sapi/v1/margin/isolated/accountLimit"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginIsolatedAccountLimitResponse],
            error_mapper=query_enabled_isolated_margin_account_limit_user_data_error_mapper,
            request_options=request_options,
        )

    def query_isolated_margin_account_info_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        symbols: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[IsolatedMarginAccountInfo, QueryIsolatedMarginAccountInfoUserDataErrorBody]:
        """- If "symbols" is not sent, all isolated assets will be returned.
        - If "symbols" is sent, only the isolated assets of the sent symbols will be returned.

        Weight(IP): 10

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            symbols: Max 5 symbols can be sent; separated by ','
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/isolated/account"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("symbols", symbols),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[IsolatedMarginAccountInfo],
            error_mapper=query_isolated_margin_account_info_user_data_error_mapper,
            request_options=request_options,
        )

    def query_isolated_margin_fee_data_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        vip_level: int | None = None,
        symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1MarginIsolatedMarginDataResponse], QueryIsolatedMarginFeeDataUserDataErrorBody]:
        """Get isolated margin fee data collection with any vip level or user's current specific data as
        https://www.binance.com/en/margin-fee

        Weight(IP): 1 when a single is specified; 10 when the symbol parameter is omitted

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            vip_level: Defaults to user's vip level
            symbol: Trading symbol, e.g. BNBUSDT
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/isolatedMarginData"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("vipLevel", vip_level),
                param[str | None]("symbol", symbol),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1MarginIsolatedMarginDataResponse]],
            error_mapper=query_isolated_margin_fee_data_user_data_error_mapper,
            request_options=request_options,
        )

    def query_isolated_margin_tier_data_user_data(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        tier: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1MarginIsolatedMarginTierResponse], QueryIsolatedMarginTierDataUserDataErrorBody]:
        """Get isolated margin tier data collection with any tier as https://www.binance.com/en/margin-data

        Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            tier: All margin tier data will be returned if tier is omitted
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/isolatedMarginTier"),
            query_params=[
                param[str]("symbol", symbol),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("tier", tier),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1MarginIsolatedMarginTierResponse]],
            error_mapper=query_isolated_margin_tier_data_user_data_error_mapper,
            request_options=request_options,
        )

    def query_liability_coin_leverage_bracket_in_cross_margin_pro_mode_market_data(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[
        list[SapiV1MarginLeverageBracketResponse],
        QueryLiabilityCoinLeverageBracketInCrossMarginProModeMarketDataErrorBody,
    ]:
        """Liability Coin Leverage Bracket in Cross Margin Pro Mode

        Weight(IP): 1

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/leverageBracket"),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1MarginLeverageBracketResponse]],
            error_mapper=query_liability_coin_leverage_bracket_in_cross_margin_pro_mode_market_data_error_mapper,
            request_options=request_options,
        )

    def query_margin_account_s_all_orders_user_data(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        order_id: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[MarginOrderDetail], QueryMarginAccountSAllOrdersUserDataErrorBody]:
        """- If ``orderId`` is set, it will get orders >= that orderId. Otherwise most recent orders are returned.
        - For some historical orders ``cummulativeQuoteQty`` will be < 0, meaning the data is not available at this
            time.

        Weight(IP): 200

        Request Limit: 60 times/min per IP

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            order_id: Order id
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/allOrders"),
            query_params=[
                param[str]("symbol", symbol),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[IsIsolatedOrStr | None]("isIsolated", is_isolated),
                param[int | None]("orderId", order_id),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[MarginOrderDetail]],
            error_mapper=query_margin_account_s_all_orders_user_data_error_mapper,
            request_options=request_options,
        )

    def query_margin_account_s_oco_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        symbol: str | None = None,
        order_list_id: int | None = None,
        orig_client_order_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MarginOrderListResponse, QueryMarginAccountSOcoUserDataErrorBody]:
        """Retrieves a specific OCO based on provided optional parameters

        - Either ``orderListId`` or ``origClientOrderId`` must be provided

        Weight(IP): 10

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            symbol: Mandatory for isolated margin, not supported for cross margin
            order_list_id: Order list id
            orig_client_order_id: Order id from client
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/orderList"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[IsIsolatedOrStr | None]("isIsolated", is_isolated),
                param[str | None]("symbol", symbol),
                param[int | None]("orderListId", order_list_id),
                param[str | None]("origClientOrderId", orig_client_order_id),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginOrderListResponse],
            error_mapper=query_margin_account_s_oco_user_data_error_mapper,
            request_options=request_options,
        )

    def query_margin_account_s_open_oco_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1MarginOpenOrderListResponse], QueryMarginAccountSOpenOcoUserDataErrorBody]:
        """Weight(IP): 10

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            symbol: Mandatory for isolated margin, not supported for cross margin
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/openOrderList"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[IsIsolatedOrStr | None]("isIsolated", is_isolated),
                param[str | None]("symbol", symbol),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1MarginOpenOrderListResponse]],
            error_mapper=query_margin_account_s_open_oco_user_data_error_mapper,
            request_options=request_options,
        )

    def query_margin_account_s_open_orders_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        symbol: str | None = None,
        is_isolated: IsIsolatedOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[MarginOrderDetail], QueryMarginAccountSOpenOrdersUserDataErrorBody]:
        """- If the ``symbol`` is not sent, orders for all symbols will be returned in an array.
        - When all symbols are returned, the number of requests counted against the rate limiter is equal to the number
            of symbols currently trading on the exchange
        - If isIsolated ="TRUE", symbol must be sent.

        Weight(IP): 10

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            symbol: Trading symbol, e.g. BNBUSDT
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/openOrders"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("symbol", symbol),
                param[IsIsolatedOrStr | None]("isIsolated", is_isolated),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[MarginOrderDetail]],
            error_mapper=query_margin_account_s_open_orders_user_data_error_mapper,
            request_options=request_options,
        )

    def query_margin_account_s_order_user_data(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        order_id: int | None = None,
        orig_client_order_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MarginOrderDetail, QueryMarginAccountSOrderUserDataErrorBody]:
        """- Either ``orderId`` or ``origClientOrderId`` must be sent.
        - For some historical orders ``cummulativeQuoteQty`` will be < 0, meaning the data is not available at this
            time.

        Weight(IP): 10

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            order_id: Order id
            orig_client_order_id: Order id from client
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/order"),
            query_params=[
                param[str]("symbol", symbol),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[IsIsolatedOrStr | None]("isIsolated", is_isolated),
                param[int | None]("orderId", order_id),
                param[str | None]("origClientOrderId", orig_client_order_id),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[MarginOrderDetail],
            error_mapper=query_margin_account_s_order_user_data_error_mapper,
            request_options=request_options,
        )

    def query_margin_account_s_trade_list_user_data(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        from_id: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[MarginTrade], QueryMarginAccountSTradeListUserDataErrorBody]:
        """- If ``fromId`` is set, it will get orders >= that ``fromId``. Otherwise most recent trades are returned.

        Weight(IP): 10

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            from_id: Trade id to fetch from. Default gets most recent trades.
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/myTrades"),
            query_params=[
                param[str]("symbol", symbol),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[IsIsolatedOrStr | None]("isIsolated", is_isolated),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("fromId", from_id),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[MarginTrade]],
            error_mapper=query_margin_account_s_trade_list_user_data_error_mapper,
            request_options=request_options,
        )

    def query_margin_account_s_all_oco_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        symbol: str | None = None,
        from_id: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1MarginAllOrderListResponse], QueryMarginAccountSAllOcoUserDataErrorBody]:
        """Retrieves all OCO for a specific margin account based on provided optional parameters

        Weight(IP): 200

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            symbol: Mandatory for isolated margin, not supported for cross margin
            from_id: If supplied, neither ``startTime`` or ``endTime`` can be provided
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default Value: 500; Max Value: 1000
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/allOrderList"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[IsIsolatedOrStr | None]("isIsolated", is_isolated),
                param[str | None]("symbol", symbol),
                param[str | None]("fromId", from_id),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1MarginAllOrderListResponse]],
            error_mapper=query_margin_account_s_all_oco_user_data_error_mapper,
            request_options=request_options,
        )

    def query_margin_available_inventory_user_data(
        self, type_: Type4OrStr, timestamp: int, signature: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SapiV1MarginAvailableInventoryResponse, QueryMarginAvailableInventoryUserDataErrorBody]:
        """Margin available Inventory query

        Weight(UID): 50

        Args:
            type_: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/available-inventory"),
            query_params=[
                param[Type4OrStr]("type", type_), param[int]("timestamp", timestamp), param[str]("signature", signature)
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginAvailableInventoryResponse],
            error_mapper=query_margin_available_inventory_user_data_error_mapper,
            request_options=request_options,
        )

    def query_margin_price_index_market_data(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SapiV1MarginPriceIndexResponse, QueryMarginPriceIndexMarketDataErrorBody]:
        """Weight(IP): 10

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/priceIndex"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginPriceIndexResponse],
            error_mapper=query_margin_price_index_market_data_error_mapper,
            request_options=request_options,
        )

    def query_max_borrow_user_data(
        self,
        asset: str,
        timestamp: int,
        signature: str,
        *,
        isolated_symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MarginMaxBorrowableResponse, QueryMaxBorrowUserDataErrorBody]:
        """- If ``isolatedSymbol`` is not sent, crossed margin data will be sent.
        - ``borrowLimit`` is also available from https://www.binance.com/en/margin-fee

        Weight(IP): 50

        Args:
            asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            isolated_symbol: Isolated symbol
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/maxBorrowable"),
            query_params=[
                param[str]("asset", asset),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("isolatedSymbol", isolated_symbol),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginMaxBorrowableResponse],
            error_mapper=query_max_borrow_user_data_error_mapper,
            request_options=request_options,
        )

    def query_max_transfer_out_amount_user_data(
        self,
        asset: str,
        timestamp: int,
        signature: str,
        *,
        isolated_symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MarginMaxTransferableResponse, QueryMaxTransferOutAmountUserDataErrorBody]:
        """- If ``isolatedSymbol`` is not sent, crossed margin data will be sent.

        Weight(IP): 50

        Args:
            asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            isolated_symbol: Isolated symbol
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/maxTransferable"),
            query_params=[
                param[str]("asset", asset),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("isolatedSymbol", isolated_symbol),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginMaxTransferableResponse],
            error_mapper=query_max_transfer_out_amount_user_data_error_mapper,
            request_options=request_options,
        )

    def query_borrow_repay_records_in_margin_account_user_data(
        self,
        asset: str,
        type_: str,
        timestamp: int,
        signature: str,
        *,
        isolated_symbol: str | None = None,
        tx_id: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MarginBorrowRepayResponse1, QueryBorrowRepayRecordsInMarginAccountUserDataErrorBody]:
        """Query borrow/repay records in Margin account

        - txId or startTime must be sent. txId takes precedence. Response in descending order
        - If an asset is sent, data within 30 days before endTime; If an asset is not sent, data within 7 days before
            endTime
        - If neither startTime nor endTime is sent, the recent 7-day data will be returned.
        - startTime set as endTime - 7 days by default, endTime set as current time by default

        Weight(IP): 10

        Args:
            asset: Value sent with the request.
            type_: BORROW or REPAY
            timestamp: UTC timestamp in ms
            signature: Signature
            isolated_symbol: Isolated symbol
            tx_id: tranId in POST /sapi/v1/margin/loan
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
            url_template=self._server.default("/sapi/v1/margin/borrow-repay"),
            query_params=[
                param[str]("asset", asset),
                param[str]("type", type_),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("isolatedSymbol", isolated_symbol),
                param[int | None]("txId", tx_id),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginBorrowRepayResponse1],
            error_mapper=query_borrow_repay_records_in_margin_account_user_data_error_mapper,
            request_options=request_options,
        )

    def toggle_bnb_burn_on_spot_trade_and_margin_interest_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        spot_bnb_burn: SpotBnbburnOrStr | None = None,
        interest_bnb_burn: InterestBnbburnOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BnbBurnStatus, ToggleBnbBurnOnSpotTradeAndMarginInterestUserDataErrorBody]:
        """- "spotBNBBurn" and "interestBNBBurn" should be sent at least one.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            spot_bnb_burn: Determines whether to use BNB to pay for trading fees on SPOT
            interest_bnb_burn: Determines whether to use BNB to pay for margin loan's interest
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/bnbBurn"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[SpotBnbburnOrStr | None]("spotBNBBurn", spot_bnb_burn),
                param[InterestBnbburnOrStr | None]("interestBNBBurn", interest_bnb_burn),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[BnbBurnStatus],
            error_mapper=toggle_bnb_burn_on_spot_trade_and_margin_interest_user_data_error_mapper,
            request_options=request_options,
        )


class AsyncMarginWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def adjust_cross_margin_max_leverage_user_data(
        self,
        max_leverage: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MarginMaxLeverageResponse, AdjustCrossMarginMaxLeverageUserDataErrorBody]:
        """Adjust cross margin max leverage

        Weight(UID): 3000

        Args:
            max_leverage: Can only adjust 3 or 5
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/margin/max-leverage"),
            query_params=[
                param[int]("maxLeverage", max_leverage),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginMaxLeverageResponse],
            error_mapper=adjust_cross_margin_max_leverage_user_data_error_mapper,
            request_options=request_options,
        )

    async def cross_margin_collateral_ratio_market_data(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[SapiV1MarginCrossMarginCollateralRatioResponse], CrossMarginCollateralRatioMarketDataErrorBody]:
        """Weight(IP): 100

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/crossMarginCollateralRatio"),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1MarginCrossMarginCollateralRatioResponse]],
            error_mapper=cross_margin_collateral_ratio_market_data_error_mapper,
            request_options=request_options,
        )

    async def disable_isolated_margin_account_trade(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MarginIsolatedAccountResponse, DisableIsolatedMarginAccountTradeErrorBody]:
        """Disable isolated margin account for a specific symbol. Each trading pair can only be deactivated once every
        24 hours .

        Weight(UID): 300

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/sapi/v1/margin/isolated/account"),
            query_params=[
                param[str]("symbol", symbol),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginIsolatedAccountResponse],
            error_mapper=disable_isolated_margin_account_trade_error_mapper,
            request_options=request_options,
        )

    async def enable_isolated_margin_account_trade(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MarginIsolatedAccountResponse, EnableIsolatedMarginAccountTradeErrorBody]:
        """Enable isolated margin account for a specific symbol.

        Weight(UID): 300

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/margin/isolated/account"),
            query_params=[
                param[str]("symbol", symbol),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginIsolatedAccountResponse],
            error_mapper=enable_isolated_margin_account_trade_error_mapper,
            request_options=request_options,
        )

    async def get_all_cross_margin_pairs_market_data(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[SapiV1MarginAllPairsResponse], GetAllCrossMarginPairsMarketDataErrorBody]:
        """Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/allPairs"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1MarginAllPairsResponse]],
            error_mapper=get_all_cross_margin_pairs_market_data_error_mapper,
            request_options=request_options,
        )

    async def get_all_isolated_margin_symbol_user_data(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1MarginIsolatedAllPairsResponse], GetAllIsolatedMarginSymbolUserDataErrorBody]:
        """Weight(IP): 10

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/isolated/allPairs"),
            query_params=[
                param[str]("symbol", symbol),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1MarginIsolatedAllPairsResponse]],
            error_mapper=get_all_isolated_margin_symbol_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_all_margin_assets_market_data(
        self, asset: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[SapiV1MarginAllAssetsResponse], GetAllMarginAssetsMarketDataErrorBody]:
        """Weight(IP): 1

        Args:
            asset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/allAssets"),
            query_params=[param[str]("asset", asset)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1MarginAllAssetsResponse]],
            error_mapper=get_all_margin_assets_market_data_error_mapper,
            request_options=request_options,
        )

    async def get_bnb_burn_status_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BnbBurnStatus, GetBnbBurnStatusUserDataErrorBody]:
        """Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/bnbBurn"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[BnbBurnStatus],
            error_mapper=get_bnb_burn_status_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_cross_margin_transfer_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        type_: Type2OrStr | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        isolated_symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MarginTransferResponse, GetCrossMarginTransferHistoryUserDataErrorBody]:
        """- Response in descending order
        - Returns data for last 7 days by default
        - Set ``archived`` to ``true`` to query data from 6 months ago

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            type_: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            isolated_symbol: Isolated symbol
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/transfer"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("asset", asset),
                param[Type2OrStr | None]("type", type_),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[str | None]("isolatedSymbol", isolated_symbol),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginTransferResponse],
            error_mapper=get_cross_margin_transfer_history_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_force_liquidation_record_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        isolated_symbol: str | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MarginForceLiquidationRecResponse, GetForceLiquidationRecordUserDataErrorBody]:
        """- Response in descending order

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            isolated_symbol: Isolated symbol
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/forceLiquidationRec"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[str | None]("isolatedSymbol", isolated_symbol),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginForceLiquidationRecResponse],
            error_mapper=get_force_liquidation_record_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_interest_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        isolated_symbol: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        archived: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MarginInterestHistoryResponse, GetInterestHistoryUserDataErrorBody]:
        """- Response in descending order
        - If ``isolatedSymbol`` is not sent, crossed margin data will be returned
        - Set ``archived`` to ``true`` to query data from 6 months ago
        - ``type`` in response has 4 enums:
          - ``PERIODIC`` interest charged per hour
          - ``ON_BORROW`` first interest charged on borrow
          - ``PERIODIC_CONVERTED`` interest charged per hour converted into BNB
          - ``ON_BORROW_CONVERTED`` first interest charged on borrow converted into BNB

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            isolated_symbol: Isolated symbol
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            archived: Default: false. Set to true for archived data from 6 months ago
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/interestHistory"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("asset", asset),
                param[str | None]("isolatedSymbol", isolated_symbol),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[str | None]("archived", archived),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginInterestHistoryResponse],
            error_mapper=get_interest_history_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_small_liability_exchange_coin_list_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        list[SapiV1MarginExchangeSmallLiabilityResponse], GetSmallLiabilityExchangeCoinListUserDataErrorBody
    ]:
        """Query the coins which can be small liability exchange

        Weight(UID): 100

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/exchange-small-liability"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1MarginExchangeSmallLiabilityResponse]],
            error_mapper=get_small_liability_exchange_coin_list_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_small_liability_exchange_history_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        current: int | None = None,
        size: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1MarginExchangeSmallLiabilityHistoryResponse, GetSmallLiabilityExchangeHistoryUserDataErrorBody
    ]:
        """Get Small liability Exchange History

        Weight(UID): 100

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/exchange-small-liability-history"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginExchangeSmallLiabilityHistoryResponse],
            error_mapper=get_small_liability_exchange_history_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_summary_of_margin_account_user_data(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MarginTradeCoeffResponse, GetSummaryOfMarginAccountUserDataErrorBody]:
        """Get personal margin level information

        Weight(IP): 10

        Args:
            email: Email Address
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/tradeCoeff"),
            query_params=[
                param[str]("email", email),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginTradeCoeffResponse],
            error_mapper=get_summary_of_margin_account_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_a_future_hourly_interest_rate_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        assets: str | None = None,
        is_isolated: IsIsolatedOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1MarginNextHourlyInterestRateResponse], GetAFutureHourlyInterestRateUserDataErrorBody]:
        """Get user the next hourly estimate interest

        Weight(UID): 100

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            assets: List of assets, separated by commas, up to 20
            is_isolated: for isolated margin or not, "TRUE", "FALSE"
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/next-hourly-interest-rate"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("assets", assets),
                param[IsIsolatedOrStr | None]("isIsolated", is_isolated),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1MarginNextHourlyInterestRateResponse]],
            error_mapper=get_a_future_hourly_interest_rate_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_cross_or_isolated_margin_capital_flow_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        symbol: str | None = None,
        type_: Type3OrStr | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        from_id: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1MarginCapitalFlowResponse], GetCrossOrIsolatedMarginCapitalFlowUserDataErrorBody]:
        """Get cross or isolated margin capital flow

        Weight(IP): 100

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            symbol: Required when querying isolated data
            type_: Value sent with the request.
            start_time: Only supports querying the data of the last 90 days
            end_time: UTC timestamp in ms
            from_id: If fromId is set, the data with id > fromId will be returned. Otherwise the latest data will be
                returned
            limit: The number of data items returned each time is limited. Default 500; Max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/capital-flow"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("asset", asset),
                param[str | None]("symbol", symbol),
                param[Type3OrStr | None]("type", type_),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("fromId", from_id),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1MarginCapitalFlowResponse]],
            error_mapper=get_cross_or_isolated_margin_capital_flow_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_tokens_or_symbols_delist_schedule_for_cross_margin_and_isolated_margin_market_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        list[SapiV1MarginDelistScheduleResponse],
        GetTokensOrSymbolsDelistScheduleForCrossMarginAndIsolatedMarginMarketDataErrorBody,
    ]:
        """Get tokens or symbols delist schedule for cross margin and isolated margin

        Weight(IP): 100

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/delist-schedule"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1MarginDelistScheduleResponse]],
            error_mapper=get_tokens_or_symbols_delist_schedule_for_cross_margin_and_isolated_margin_market_data_error_mapper,
            request_options=request_options,
        )

    async def margin_account_cancel_oco_trade(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        order_list_id: int | None = None,
        list_client_order_id: str | None = None,
        new_client_order_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MarginOcoOrder, MarginAccountCancelOcoTradeErrorBody]:
        """Cancel an entire Order List for a margin account

        - Canceling an individual leg will cancel the entire OCO
        - Either ``orderListId`` or ``listClientOrderId`` must be provided

        Weight(UID): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            order_list_id: Order list id
            list_client_order_id: A unique Id for the entire orderList
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/sapi/v1/margin/orderList"),
            query_params=[
                param[str]("symbol", symbol),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[IsIsolatedOrStr | None]("isIsolated", is_isolated),
                param[int | None]("orderListId", order_list_id),
                param[str | None]("listClientOrderId", list_client_order_id),
                param[str | None]("newClientOrderId", new_client_order_id),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[MarginOcoOrder],
            error_mapper=margin_account_cancel_oco_trade_error_mapper,
            request_options=request_options,
        )

    async def margin_account_cancel_order_trade(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        order_id: int | None = None,
        orig_client_order_id: str | None = None,
        new_client_order_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MarginOrder, MarginAccountCancelOrderTradeErrorBody]:
        """Cancel an active order for margin account.

        Either ``orderId`` or ``origClientOrderId`` must be sent.

        Weight(IP): 10

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            order_id: Order id
            orig_client_order_id: Order id from client
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/sapi/v1/margin/order"),
            query_params=[
                param[str]("symbol", symbol),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[IsIsolatedOrStr | None]("isIsolated", is_isolated),
                param[int | None]("orderId", order_id),
                param[str | None]("origClientOrderId", orig_client_order_id),
                param[str | None]("newClientOrderId", new_client_order_id),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[MarginOrder],
            error_mapper=margin_account_cancel_order_trade_error_mapper,
            request_options=request_options,
        )

    async def margin_account_cancel_all_open_orders_on_a_symbol_trade(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1MarginOpenOrdersResponse], MarginAccountCancelAllOpenOrdersOnASymbolTradeErrorBody]:
        """- Cancels all active orders on a symbol for margin account.
        - This includes OCO orders.

        Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/sapi/v1/margin/openOrders"),
            query_params=[
                param[str]("symbol", symbol),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[IsIsolatedOrStr | None]("isIsolated", is_isolated),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1MarginOpenOrdersResponse]],
            error_mapper=margin_account_cancel_all_open_orders_on_a_symbol_trade_error_mapper,
            request_options=request_options,
        )

    async def margin_account_new_oco_trade(
        self,
        symbol: str,
        side: SideOrStr,
        quantity: float,
        price: float,
        stop_price: float,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        list_client_order_id: str | None = None,
        limit_client_order_id: str | None = None,
        limit_iceberg_qty: float | None = None,
        stop_client_order_id: str | None = None,
        stop_limit_price: float | None = None,
        stop_iceberg_qty: float | None = None,
        stop_limit_time_in_force: StopLimitTimeInForceOrStr | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        side_effect_type: SideEffectTypeOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MarginOrderOcoResponse, MarginAccountNewOcoTradeErrorBody]:
        """Send in a new OCO for a margin account

        - Price Restrictions:
          - SELL: Limit Price > Last Price > Stop Price
          - BUY: Limit Price < Last Price < Stop Price
        - Quantity Restrictions:
          - Both legs must have the same quantity
          - ICEBERG quantities however do not have to be the same.
        - Order Rate Limit
          - OCO counts as 2 orders against the order rate limit.

        Weight(UID): 6

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            quantity: Value sent with the request.
            price: Order price
            stop_price: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            list_client_order_id: A unique Id for the entire orderList
            limit_client_order_id: A unique Id for the limit order
            limit_iceberg_qty: Value sent with the request.
            stop_client_order_id: A unique Id for the stop loss/stop loss limit leg
            stop_limit_price: If provided, stopLimitTimeInForce is required.
            stop_iceberg_qty: Value sent with the request.
            stop_limit_time_in_force: Value sent with the request.
            new_order_resp_type: Set the response JSON.
            side_effect_type: Default ``NO_SIDE_EFFECT``
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/margin/order/oco"),
            query_params=[
                param[str]("symbol", symbol),
                param[SideOrStr]("side", side),
                param[float]("quantity", quantity),
                param[float]("price", price),
                param[float]("stopPrice", stop_price),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[IsIsolatedOrStr | None]("isIsolated", is_isolated),
                param[str | None]("listClientOrderId", list_client_order_id),
                param[str | None]("limitClientOrderId", limit_client_order_id),
                param[float | None]("limitIcebergQty", limit_iceberg_qty),
                param[str | None]("stopClientOrderId", stop_client_order_id),
                param[float | None]("stopLimitPrice", stop_limit_price),
                param[float | None]("stopIcebergQty", stop_iceberg_qty),
                param[StopLimitTimeInForceOrStr | None]("stopLimitTimeInForce", stop_limit_time_in_force),
                param[NewOrderRespTypeOrStr | None]("newOrderRespType", new_order_resp_type),
                param[SideEffectTypeOrStr | None]("sideEffectType", side_effect_type),
                param[SelfTradePreventionModeOrStr | None]("selfTradePreventionMode", self_trade_prevention_mode),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginOrderOcoResponse],
            error_mapper=margin_account_new_oco_trade_error_mapper,
            request_options=request_options,
        )

    async def margin_account_new_oto_trade(
        self,
        symbol: str,
        working_type: WorkingTypeOrStr,
        working_side: WorkingSideOrStr,
        working_price: float,
        working_quantity: float,
        working_iceberg_qty: float,
        pending_type: PendingTypeOrStr,
        pending_side: PendingSideOrStr,
        pending_quantity: float,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        list_client_order_id: str | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        side_effect_type: SideEffectType1OrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        auto_repay_at_cancel: bool | None = None,
        working_client_order_id: str | None = None,
        working_time_in_force: WorkingTimeInForceOrStr | None = None,
        pending_client_order_id: str | None = None,
        pending_price: float | None = None,
        pending_stop_price: float | None = None,
        pending_trailing_delta: float | None = None,
        pending_iceberg_qty: float | None = None,
        pending_time_in_force: PendingTimeInForceOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MarginOrderOtoResponse, MarginAccountNewOtoTradeErrorBody]:
        """Post a new ``OTO`` order for margin account:
        - An ``OTO`` (One-Triggers-the-Other) is an order list comprised of 2 orders
        - The first order is called the working order and must be ``LIMIT`` or ``LIMIT_MAKER``. Initially, only the
            working order goes on the order book.
        - The second order is called the pending order. It can be any order type except for ``MARKET`` orders using
            parameter ``quoteOrderQty``. The pending order is only placed on the order book when the working order gets
            fully filled.
        - If either the working order or the pending order is cancelled individually, the other order in the order list
            will also be canceled or expired.
        - When the order list is placed, if the working order gets immediately fully filled, the placement response will
            show the working order as ``FILLED`` but the pending order will still appear as ``PENDING_NEW``. You need to
            query the status of the pending order again to see its updated status.
        - OTOs add 2 orders to the unfilled order count, ``EXCHANGE_MAX_NUM_ORDERS`` filter and ``MAX_NUM_ORDERS``
            filter.

        Weight(UID): 6

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            working_type: Supported values: LIMIT,LIMIT_MAKER
            working_side: BUY,SELL
            working_price: Value sent with the request.
            working_quantity: Sets the quantity for the working order.
            working_iceberg_qty: This can only be used if workingTimeInForce is GTC.
            pending_type: Supported values: Order Types Note that MARKET orders using quoteOrderQty are not supported.
            pending_side: BUY,SELL
            pending_quantity: Sets the quantity for the pending order.
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            list_client_order_id: Arbitrary unique ID among open order lists. Automatically generated if not sent. A new
                order list with the same ``listClientOrderId`` is accepted only when the previous one is filled or
                completely expired. ``listClientOrderId`` is distinct from the ``workingClientOrderId`` and the
                ``pendingClientOrderId``.
            new_order_resp_type: Set the response JSON.
            side_effect_type: Default ``NO_SIDE_EFFECT``
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            auto_repay_at_cancel: Only when MARGIN_BUY order takes effect, true means that the debt generated by the
                order needs to be repay after the order is cancelled. The default is true
            working_client_order_id: Arbitrary unique ID among open orders for the working order. Automatically
                generated if not sent.
            working_time_in_force: GTC, IOC, FOK
            pending_client_order_id: Arbitrary unique ID among open orders for the pending order. Automatically
                generated if not sent.
            pending_price: Value sent with the request.
            pending_stop_price: Value sent with the request.
            pending_trailing_delta: Value sent with the request.
            pending_iceberg_qty: This can only be used if pendingTimeInForce is GTC.
            pending_time_in_force: GTC, IOC, FOK
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/margin/order/oto"),
            query_params=[
                param[str]("symbol", symbol),
                param[WorkingTypeOrStr]("workingType", working_type),
                param[WorkingSideOrStr]("workingSide", working_side),
                param[float]("workingPrice", working_price),
                param[float]("workingQuantity", working_quantity),
                param[float]("workingIcebergQty", working_iceberg_qty),
                param[PendingTypeOrStr]("pendingType", pending_type),
                param[PendingSideOrStr]("pendingSide", pending_side),
                param[float]("pendingQuantity", pending_quantity),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[IsIsolatedOrStr | None]("isIsolated", is_isolated),
                param[str | None]("listClientOrderId", list_client_order_id),
                param[NewOrderRespTypeOrStr | None]("newOrderRespType", new_order_resp_type),
                param[SideEffectType1OrStr | None]("sideEffectType", side_effect_type),
                param[SelfTradePreventionModeOrStr | None]("selfTradePreventionMode", self_trade_prevention_mode),
                param[bool | None]("autoRepayAtCancel", auto_repay_at_cancel),
                param[str | None]("workingClientOrderId", working_client_order_id),
                param[WorkingTimeInForceOrStr | None]("workingTimeInForce", working_time_in_force),
                param[str | None]("pendingClientOrderId", pending_client_order_id),
                param[float | None]("pendingPrice", pending_price),
                param[float | None]("pendingStopPrice", pending_stop_price),
                param[float | None]("pendingTrailingDelta", pending_trailing_delta),
                param[float | None]("pendingIcebergQty", pending_iceberg_qty),
                param[PendingTimeInForceOrStr | None]("pendingTimeInForce", pending_time_in_force),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginOrderOtoResponse],
            error_mapper=margin_account_new_oto_trade_error_mapper,
            request_options=request_options,
        )

    async def margin_account_new_otoco_trade(
        self,
        symbol: str,
        working_type: WorkingTypeOrStr,
        working_side: WorkingSideOrStr,
        working_price: float,
        working_quantity: float,
        working_iceberg_qty: float,
        pending_side: PendingSideOrStr,
        pending_quantity: float,
        pending_above_type: PendingAboveTypeOrStr,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        side_effect_type: SideEffectType1OrStr | None = None,
        auto_repay_at_cancel: bool | None = None,
        list_client_order_id: str | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        working_client_order_id: str | None = None,
        working_time_in_force: WorkingTimeInForceOrStr | None = None,
        pending_above_client_order_id: str | None = None,
        pending_above_price: float | None = None,
        pending_above_stop_price: float | None = None,
        pending_above_trailing_delta: float | None = None,
        pending_above_iceberg_qty: float | None = None,
        pending_above_time_in_force: PendingAboveTimeInForceOrStr | None = None,
        pending_below_type: PendingBelowTypeOrStr | None = None,
        pending_below_client_order_id: str | None = None,
        pending_below_price: float | None = None,
        pending_below_stop_price: float | None = None,
        pending_below_trailing_delta: float | None = None,
        pending_below_iceberg_qty: float | None = None,
        pending_below_time_in_force: PendingBelowTimeInForceOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MarginOrderOtocoResponse, MarginAccountNewOtocoTradeErrorBody]:
        """Post a new ``OTOCO`` order for margin account:
        - An ``OTOCO`` (One-Triggers-the-Other-Cancel-the-Other) is an order list comprised of 3 orders
        - The first order is called the working order and must be ``LIMIT`` or ``LIMIT_MAKER``. Initially, only the
            working order goes on the order book.
          - The behavior of the working order is the same as the ``OTO``.
        - ``OTOCO`` has 2 pending orders (pending above and pending below), forming an ``OCO`` pair. The pending orders
            are only placed on the order book when the working order gets fully filled.
          - The rules of the pending above and pending below follow the same rules as the Order List ``OCO``.
        - OTOCOs add 3 orders to the unfilled order count, ``EXCHANGE_MAX_NUM_ORDERS`` filter and ``MAX_NUM_ORDERS``
            filter.

        Weight(UID): 6

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            working_type: Supported values: LIMIT,LIMIT_MAKER
            working_side: BUY,SELL
            working_price: Value sent with the request.
            working_quantity: Sets the quantity for the working order.
            working_iceberg_qty: This can only be used if workingTimeInForce is GTC.
            pending_side: BUY,SELL
            pending_quantity: Sets the quantity for the pending order.
            pending_above_type: Supported values: LIMIT_MAKER, STOP_LOSS, and STOP_LOSS_LIMIT
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            side_effect_type: Default ``NO_SIDE_EFFECT``
            auto_repay_at_cancel: Only when MARGIN_BUY order takes effect, true means that the debt generated by the
                order needs to be repay after the order is cancelled. The default is true
            list_client_order_id: Arbitrary unique ID among open order lists. Automatically generated if not sent. A new
                order list with the same ``listClientOrderId`` is accepted only when the previous one is filled or
                completely expired. ``listClientOrderId`` is distinct from the ``workingClientOrderId`` and the
                ``pendingClientOrderId``.
            new_order_resp_type: Set the response JSON.
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            working_client_order_id: Arbitrary unique ID among open orders for the working order. Automatically
                generated if not sent.
            working_time_in_force: GTC, IOC, FOK
            pending_above_client_order_id: Arbitrary unique ID among open orders for the pending above order.
                Automatically generated if not sent.
            pending_above_price: Value sent with the request.
            pending_above_stop_price: Value sent with the request.
            pending_above_trailing_delta: Value sent with the request.
            pending_above_iceberg_qty: This can only be used if pendingAboveTimeInForce is GTC.
            pending_above_time_in_force: Value sent with the request.
            pending_below_type: Supported values: LIMIT_MAKER, STOP_LOSS, and STOP_LOSS_LIMIT
            pending_below_client_order_id: Arbitrary unique ID among open orders for the pending below order.
                Automatically generated if not sent.
            pending_below_price: Value sent with the request.
            pending_below_stop_price: Value sent with the request.
            pending_below_trailing_delta: Value sent with the request.
            pending_below_iceberg_qty: This can only be used if pendingBelowTimeInForce is GTC.
            pending_below_time_in_force: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/margin/order/otoco"),
            query_params=[
                param[str]("symbol", symbol),
                param[WorkingTypeOrStr]("workingType", working_type),
                param[WorkingSideOrStr]("workingSide", working_side),
                param[float]("workingPrice", working_price),
                param[float]("workingQuantity", working_quantity),
                param[float]("workingIcebergQty", working_iceberg_qty),
                param[PendingSideOrStr]("pendingSide", pending_side),
                param[float]("pendingQuantity", pending_quantity),
                param[PendingAboveTypeOrStr]("pendingAboveType", pending_above_type),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[IsIsolatedOrStr | None]("isIsolated", is_isolated),
                param[SideEffectType1OrStr | None]("sideEffectType", side_effect_type),
                param[bool | None]("autoRepayAtCancel", auto_repay_at_cancel),
                param[str | None]("listClientOrderId", list_client_order_id),
                param[NewOrderRespTypeOrStr | None]("newOrderRespType", new_order_resp_type),
                param[SelfTradePreventionModeOrStr | None]("selfTradePreventionMode", self_trade_prevention_mode),
                param[str | None]("workingClientOrderId", working_client_order_id),
                param[WorkingTimeInForceOrStr | None]("workingTimeInForce", working_time_in_force),
                param[str | None]("pendingAboveClientOrderId", pending_above_client_order_id),
                param[float | None]("pendingAbovePrice", pending_above_price),
                param[float | None]("pendingAboveStopPrice", pending_above_stop_price),
                param[float | None]("pendingAboveTrailingDelta", pending_above_trailing_delta),
                param[float | None]("pendingAboveIcebergQty", pending_above_iceberg_qty),
                param[PendingAboveTimeInForceOrStr | None]("pendingAboveTimeInForce", pending_above_time_in_force),
                param[PendingBelowTypeOrStr | None]("pendingBelowType", pending_below_type),
                param[str | None]("pendingBelowClientOrderId", pending_below_client_order_id),
                param[float | None]("pendingBelowPrice", pending_below_price),
                param[float | None]("pendingBelowStopPrice", pending_below_stop_price),
                param[float | None]("pendingBelowTrailingDelta", pending_below_trailing_delta),
                param[float | None]("pendingBelowIcebergQty", pending_below_iceberg_qty),
                param[PendingBelowTimeInForceOrStr | None]("pendingBelowTimeInForce", pending_below_time_in_force),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginOrderOtocoResponse],
            error_mapper=margin_account_new_otoco_trade_error_mapper,
            request_options=request_options,
        )

    async def margin_account_new_order_trade(
        self,
        symbol: str,
        side: SideOrStr,
        type_: Type1OrStr,
        quantity: float,
        auto_repay_at_cancel: bool,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        quote_order_qty: float | None = None,
        price: float | None = None,
        stop_price: float | None = None,
        new_client_order_id: str | None = None,
        iceberg_qty: float | None = None,
        new_order_resp_type: NewOrderRespTypeOrStr | None = None,
        side_effect_type: SideEffectTypeOrStr | None = None,
        time_in_force: TimeInForceOrStr | None = None,
        self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MarginOrderResponse, MarginAccountNewOrderTradeErrorBody]:
        """Post a new order for margin account.

        Weight(UID): 6

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            side: Value sent with the request.
            type_: Order type
            quantity: Value sent with the request.
            auto_repay_at_cancel: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            quote_order_qty: Quote quantity
            price: Order price
            stop_price: Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
            new_client_order_id: Used to uniquely identify this cancel. Automatically generated by default
            iceberg_qty: Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.
            new_order_resp_type: Set the response JSON.
            side_effect_type: Default ``NO_SIDE_EFFECT``
            time_in_force: Order time in force
            self_trade_prevention_mode: The allowed enums is dependent on what is configured on the symbol. The possible
                supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/margin/order"),
            query_params=[
                param[str]("symbol", symbol),
                param[SideOrStr]("side", side),
                param[Type1OrStr]("type", type_),
                param[float]("quantity", quantity),
                param[bool]("autoRepayAtCancel", auto_repay_at_cancel),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[IsIsolatedOrStr | None]("isIsolated", is_isolated),
                param[float | None]("quoteOrderQty", quote_order_qty),
                param[float | None]("price", price),
                param[float | None]("stopPrice", stop_price),
                param[str | None]("newClientOrderId", new_client_order_id),
                param[float | None]("icebergQty", iceberg_qty),
                param[NewOrderRespTypeOrStr | None]("newOrderRespType", new_order_resp_type),
                param[SideEffectTypeOrStr | None]("sideEffectType", side_effect_type),
                param[TimeInForceOrStr | None]("timeInForce", time_in_force),
                param[SelfTradePreventionModeOrStr | None]("selfTradePreventionMode", self_trade_prevention_mode),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginOrderResponse],
            error_mapper=margin_account_new_order_trade_error_mapper,
            request_options=request_options,
        )

    async def margin_interest_rate_history_user_data(
        self,
        asset: str,
        timestamp: int,
        signature: str,
        *,
        vip_level: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1MarginInterestRateHistoryResponse], MarginInterestRateHistoryUserDataErrorBody]:
        """The max interval between startTime and endTime is 30 days.

        Weight(IP): 1

        Args:
            asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            vip_level: Defaults to user's vip level
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/interestRateHistory"),
            query_params=[
                param[str]("asset", asset),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("vipLevel", vip_level),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1MarginInterestRateHistoryResponse]],
            error_mapper=margin_interest_rate_history_user_data_error_mapper,
            request_options=request_options,
        )

    async def margin_account_borrow_repay_margin(
        self,
        asset: str,
        is_isolated: str,
        symbol: str,
        amount: float,
        type_: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MarginBorrowRepayResponse, MarginAccountBorrowRepayMarginErrorBody]:
        """Margin account borrow/repay(MARGIN)

        Weight(UID): 3000

        Args:
            asset: Value sent with the request.
            is_isolated: TRUE for isolated margin, FALSE for crossed margin
            symbol: Trading symbol, e.g. BNBUSDT
            amount: Value sent with the request.
            type_: BORROW or REPAY
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/margin/borrow-repay"),
            query_params=[
                param[str]("asset", asset),
                param[str]("isIsolated", is_isolated),
                param[str]("symbol", symbol),
                param[float]("amount", amount),
                param[str]("type", type_),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginBorrowRepayResponse],
            error_mapper=margin_account_borrow_repay_margin_error_mapper,
            request_options=request_options,
        )

    async def margin_manual_liquidation_margin(
        self,
        type_: Type4OrStr,
        timestamp: int,
        signature: str,
        *,
        symbol: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1MarginManualLiquidationResponse], MarginManualLiquidationMarginErrorBody]:
        """Margin manual liquidation

        Weight(UID): 3000

        Args:
            type_: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            symbol: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/margin/manual-liquidation"),
            query_params=[
                param[Type4OrStr]("type", type_),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("symbol", symbol),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1MarginManualLiquidationResponse]],
            error_mapper=margin_manual_liquidation_margin_error_mapper,
            request_options=request_options,
        )

    async def query_cross_margin_account_details_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MarginAccountResponse, QueryCrossMarginAccountDetailsUserDataErrorBody]:
        """Weight(IP): 10

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/account"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginAccountResponse],
            error_mapper=query_cross_margin_account_details_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_cross_margin_fee_data_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        vip_level: int | None = None,
        coin: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1MarginCrossMarginDataResponse], QueryCrossMarginFeeDataUserDataErrorBody]:
        """Get cross margin fee data collection with any vip level or user's current specific data as
        https://www.binance.com/en/margin-fee

        Weight(IP): 1 when coin is specified; 5 when the coin parameter is omitted

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            vip_level: Defaults to user's vip level
            coin: Coin name
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/crossMarginData"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("vipLevel", vip_level),
                param[str | None]("coin", coin),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1MarginCrossMarginDataResponse]],
            error_mapper=query_cross_margin_fee_data_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_current_margin_order_count_usage_trade(
        self,
        timestamp: int,
        signature: str,
        *,
        is_isolated: str | None = None,
        symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1MarginRateLimitOrderResponse], QueryCurrentMarginOrderCountUsageTradeErrorBody]:
        """Displays the user's current margin order count usage for all intervals.

        Weight(IP): 20

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            symbol: isolated symbol, mandatory for isolated margin
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/rateLimit/order"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("isIsolated", is_isolated),
                param[str | None]("symbol", symbol),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1MarginRateLimitOrderResponse]],
            error_mapper=query_current_margin_order_count_usage_trade_error_mapper,
            request_options=request_options,
        )

    async def query_enabled_isolated_margin_account_limit_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MarginIsolatedAccountLimitResponse, QueryEnabledIsolatedMarginAccountLimitUserDataErrorBody]:
        """Query enabled isolated margin account limit.

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
            url_template=self._server.default("/sapi/v1/margin/isolated/accountLimit"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginIsolatedAccountLimitResponse],
            error_mapper=query_enabled_isolated_margin_account_limit_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_isolated_margin_account_info_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        symbols: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[IsolatedMarginAccountInfo, QueryIsolatedMarginAccountInfoUserDataErrorBody]:
        """- If "symbols" is not sent, all isolated assets will be returned.
        - If "symbols" is sent, only the isolated assets of the sent symbols will be returned.

        Weight(IP): 10

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            symbols: Max 5 symbols can be sent; separated by ','
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/isolated/account"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("symbols", symbols),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[IsolatedMarginAccountInfo],
            error_mapper=query_isolated_margin_account_info_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_isolated_margin_fee_data_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        vip_level: int | None = None,
        symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1MarginIsolatedMarginDataResponse], QueryIsolatedMarginFeeDataUserDataErrorBody]:
        """Get isolated margin fee data collection with any vip level or user's current specific data as
        https://www.binance.com/en/margin-fee

        Weight(IP): 1 when a single is specified; 10 when the symbol parameter is omitted

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            vip_level: Defaults to user's vip level
            symbol: Trading symbol, e.g. BNBUSDT
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/isolatedMarginData"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("vipLevel", vip_level),
                param[str | None]("symbol", symbol),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1MarginIsolatedMarginDataResponse]],
            error_mapper=query_isolated_margin_fee_data_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_isolated_margin_tier_data_user_data(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        tier: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1MarginIsolatedMarginTierResponse], QueryIsolatedMarginTierDataUserDataErrorBody]:
        """Get isolated margin tier data collection with any tier as https://www.binance.com/en/margin-data

        Weight(IP): 1

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            tier: All margin tier data will be returned if tier is omitted
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/isolatedMarginTier"),
            query_params=[
                param[str]("symbol", symbol),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("tier", tier),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1MarginIsolatedMarginTierResponse]],
            error_mapper=query_isolated_margin_tier_data_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_liability_coin_leverage_bracket_in_cross_margin_pro_mode_market_data(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[
        list[SapiV1MarginLeverageBracketResponse],
        QueryLiabilityCoinLeverageBracketInCrossMarginProModeMarketDataErrorBody,
    ]:
        """Liability Coin Leverage Bracket in Cross Margin Pro Mode

        Weight(IP): 1

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/leverageBracket"),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1MarginLeverageBracketResponse]],
            error_mapper=query_liability_coin_leverage_bracket_in_cross_margin_pro_mode_market_data_error_mapper,
            request_options=request_options,
        )

    async def query_margin_account_s_all_orders_user_data(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        order_id: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[MarginOrderDetail], QueryMarginAccountSAllOrdersUserDataErrorBody]:
        """- If ``orderId`` is set, it will get orders >= that orderId. Otherwise most recent orders are returned.
        - For some historical orders ``cummulativeQuoteQty`` will be < 0, meaning the data is not available at this
            time.

        Weight(IP): 200

        Request Limit: 60 times/min per IP

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            order_id: Order id
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/allOrders"),
            query_params=[
                param[str]("symbol", symbol),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[IsIsolatedOrStr | None]("isIsolated", is_isolated),
                param[int | None]("orderId", order_id),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[MarginOrderDetail]],
            error_mapper=query_margin_account_s_all_orders_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_margin_account_s_oco_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        symbol: str | None = None,
        order_list_id: int | None = None,
        orig_client_order_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MarginOrderListResponse, QueryMarginAccountSOcoUserDataErrorBody]:
        """Retrieves a specific OCO based on provided optional parameters

        - Either ``orderListId`` or ``origClientOrderId`` must be provided

        Weight(IP): 10

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            symbol: Mandatory for isolated margin, not supported for cross margin
            order_list_id: Order list id
            orig_client_order_id: Order id from client
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/orderList"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[IsIsolatedOrStr | None]("isIsolated", is_isolated),
                param[str | None]("symbol", symbol),
                param[int | None]("orderListId", order_list_id),
                param[str | None]("origClientOrderId", orig_client_order_id),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginOrderListResponse],
            error_mapper=query_margin_account_s_oco_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_margin_account_s_open_oco_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1MarginOpenOrderListResponse], QueryMarginAccountSOpenOcoUserDataErrorBody]:
        """Weight(IP): 10

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            symbol: Mandatory for isolated margin, not supported for cross margin
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/openOrderList"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[IsIsolatedOrStr | None]("isIsolated", is_isolated),
                param[str | None]("symbol", symbol),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1MarginOpenOrderListResponse]],
            error_mapper=query_margin_account_s_open_oco_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_margin_account_s_open_orders_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        symbol: str | None = None,
        is_isolated: IsIsolatedOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[MarginOrderDetail], QueryMarginAccountSOpenOrdersUserDataErrorBody]:
        """- If the ``symbol`` is not sent, orders for all symbols will be returned in an array.
        - When all symbols are returned, the number of requests counted against the rate limiter is equal to the number
            of symbols currently trading on the exchange
        - If isIsolated ="TRUE", symbol must be sent.

        Weight(IP): 10

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            symbol: Trading symbol, e.g. BNBUSDT
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/openOrders"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("symbol", symbol),
                param[IsIsolatedOrStr | None]("isIsolated", is_isolated),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[MarginOrderDetail]],
            error_mapper=query_margin_account_s_open_orders_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_margin_account_s_order_user_data(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        order_id: int | None = None,
        orig_client_order_id: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MarginOrderDetail, QueryMarginAccountSOrderUserDataErrorBody]:
        """- Either ``orderId`` or ``origClientOrderId`` must be sent.
        - For some historical orders ``cummulativeQuoteQty`` will be < 0, meaning the data is not available at this
            time.

        Weight(IP): 10

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            order_id: Order id
            orig_client_order_id: Order id from client
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/order"),
            query_params=[
                param[str]("symbol", symbol),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[IsIsolatedOrStr | None]("isIsolated", is_isolated),
                param[int | None]("orderId", order_id),
                param[str | None]("origClientOrderId", orig_client_order_id),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[MarginOrderDetail],
            error_mapper=query_margin_account_s_order_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_margin_account_s_trade_list_user_data(
        self,
        symbol: str,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        from_id: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[MarginTrade], QueryMarginAccountSTradeListUserDataErrorBody]:
        """- If ``fromId`` is set, it will get orders >= that ``fromId``. Otherwise most recent trades are returned.

        Weight(IP): 10

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            from_id: Trade id to fetch from. Default gets most recent trades.
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/myTrades"),
            query_params=[
                param[str]("symbol", symbol),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[IsIsolatedOrStr | None]("isIsolated", is_isolated),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("fromId", from_id),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[MarginTrade]],
            error_mapper=query_margin_account_s_trade_list_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_margin_account_s_all_oco_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        is_isolated: IsIsolatedOrStr | None = None,
        symbol: str | None = None,
        from_id: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1MarginAllOrderListResponse], QueryMarginAccountSAllOcoUserDataErrorBody]:
        """Retrieves all OCO for a specific margin account based on provided optional parameters

        Weight(IP): 200

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            is_isolated: * ``TRUE`` - For isolated margin * ``FALSE`` - Default, not for isolated margin
            symbol: Mandatory for isolated margin, not supported for cross margin
            from_id: If supplied, neither ``startTime`` or ``endTime`` can be provided
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default Value: 500; Max Value: 1000
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/allOrderList"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[IsIsolatedOrStr | None]("isIsolated", is_isolated),
                param[str | None]("symbol", symbol),
                param[str | None]("fromId", from_id),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1MarginAllOrderListResponse]],
            error_mapper=query_margin_account_s_all_oco_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_margin_available_inventory_user_data(
        self, type_: Type4OrStr, timestamp: int, signature: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SapiV1MarginAvailableInventoryResponse, QueryMarginAvailableInventoryUserDataErrorBody]:
        """Margin available Inventory query

        Weight(UID): 50

        Args:
            type_: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/available-inventory"),
            query_params=[
                param[Type4OrStr]("type", type_), param[int]("timestamp", timestamp), param[str]("signature", signature)
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginAvailableInventoryResponse],
            error_mapper=query_margin_available_inventory_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_margin_price_index_market_data(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SapiV1MarginPriceIndexResponse, QueryMarginPriceIndexMarketDataErrorBody]:
        """Weight(IP): 10

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/priceIndex"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginPriceIndexResponse],
            error_mapper=query_margin_price_index_market_data_error_mapper,
            request_options=request_options,
        )

    async def query_max_borrow_user_data(
        self,
        asset: str,
        timestamp: int,
        signature: str,
        *,
        isolated_symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MarginMaxBorrowableResponse, QueryMaxBorrowUserDataErrorBody]:
        """- If ``isolatedSymbol`` is not sent, crossed margin data will be sent.
        - ``borrowLimit`` is also available from https://www.binance.com/en/margin-fee

        Weight(IP): 50

        Args:
            asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            isolated_symbol: Isolated symbol
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/maxBorrowable"),
            query_params=[
                param[str]("asset", asset),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("isolatedSymbol", isolated_symbol),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginMaxBorrowableResponse],
            error_mapper=query_max_borrow_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_max_transfer_out_amount_user_data(
        self,
        asset: str,
        timestamp: int,
        signature: str,
        *,
        isolated_symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MarginMaxTransferableResponse, QueryMaxTransferOutAmountUserDataErrorBody]:
        """- If ``isolatedSymbol`` is not sent, crossed margin data will be sent.

        Weight(IP): 50

        Args:
            asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            isolated_symbol: Isolated symbol
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/margin/maxTransferable"),
            query_params=[
                param[str]("asset", asset),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("isolatedSymbol", isolated_symbol),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginMaxTransferableResponse],
            error_mapper=query_max_transfer_out_amount_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_borrow_repay_records_in_margin_account_user_data(
        self,
        asset: str,
        type_: str,
        timestamp: int,
        signature: str,
        *,
        isolated_symbol: str | None = None,
        tx_id: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MarginBorrowRepayResponse1, QueryBorrowRepayRecordsInMarginAccountUserDataErrorBody]:
        """Query borrow/repay records in Margin account

        - txId or startTime must be sent. txId takes precedence. Response in descending order
        - If an asset is sent, data within 30 days before endTime; If an asset is not sent, data within 7 days before
            endTime
        - If neither startTime nor endTime is sent, the recent 7-day data will be returned.
        - startTime set as endTime - 7 days by default, endTime set as current time by default

        Weight(IP): 10

        Args:
            asset: Value sent with the request.
            type_: BORROW or REPAY
            timestamp: UTC timestamp in ms
            signature: Signature
            isolated_symbol: Isolated symbol
            tx_id: tranId in POST /sapi/v1/margin/loan
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
            url_template=self._server.default("/sapi/v1/margin/borrow-repay"),
            query_params=[
                param[str]("asset", asset),
                param[str]("type", type_),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("isolatedSymbol", isolated_symbol),
                param[int | None]("txId", tx_id),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MarginBorrowRepayResponse1],
            error_mapper=query_borrow_repay_records_in_margin_account_user_data_error_mapper,
            request_options=request_options,
        )

    async def toggle_bnb_burn_on_spot_trade_and_margin_interest_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        spot_bnb_burn: SpotBnbburnOrStr | None = None,
        interest_bnb_burn: InterestBnbburnOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BnbBurnStatus, ToggleBnbBurnOnSpotTradeAndMarginInterestUserDataErrorBody]:
        """- "spotBNBBurn" and "interestBNBBurn" should be sent at least one.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            spot_bnb_burn: Determines whether to use BNB to pay for trading fees on SPOT
            interest_bnb_burn: Determines whether to use BNB to pay for margin loan's interest
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/bnbBurn"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[SpotBnbburnOrStr | None]("spotBNBBurn", spot_bnb_burn),
                param[InterestBnbburnOrStr | None]("interestBNBBurn", interest_bnb_burn),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[BnbBurnStatus],
            error_mapper=toggle_bnb_burn_on_spot_trade_and_margin_interest_user_data_error_mapper,
            request_options=request_options,
        )
