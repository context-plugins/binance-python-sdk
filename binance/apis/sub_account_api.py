from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder, param
from ..errors.create_a_virtual_sub_account_for_master_account_error import (
    CreateAVirtualSubAccountForMasterAccountErrorBody,
    create_a_virtual_sub_account_for_master_account_error_mapper,
)
from ..errors.delete_ip_list_for_a_sub_account_api_key_for_master_account_error import (
    DeleteIpListForASubAccountApiKeyForMasterAccountErrorBody,
    delete_ip_list_for_a_sub_account_api_key_for_master_account_error_mapper,
)
from ..errors.deposit_assets_into_the_managed_sub_account_for_investor_master_account_error import (
    DepositAssetsIntoTheManagedSubAccountForInvestorMasterAccountErrorBody,
    deposit_assets_into_the_managed_sub_account_for_investor_master_account_error_mapper,
)
from ..errors.detail_on_sub_account_s_futures_account_for_master_account_error import (
    DetailOnSubAccountSFuturesAccountForMasterAccountErrorBody,
    detail_on_sub_account_s_futures_account_for_master_account_error_mapper,
)
from ..errors.detail_on_sub_account_s_futures_account_v2_for_master_account_error import (
    DetailOnSubAccountSFuturesAccountV2ForMasterAccountErrorBody,
    detail_on_sub_account_s_futures_account_v2_for_master_account_error_mapper,
)
from ..errors.detail_on_sub_account_s_margin_account_for_master_account_error import (
    DetailOnSubAccountSMarginAccountForMasterAccountErrorBody,
    detail_on_sub_account_s_margin_account_for_master_account_error_mapper,
)
from ..errors.enable_futures_for_sub_account_for_master_account_error import (
    EnableFuturesForSubAccountForMasterAccountErrorBody,
    enable_futures_for_sub_account_for_master_account_error_mapper,
)
from ..errors.enable_leverage_token_for_sub_account_for_master_account_error import (
    EnableLeverageTokenForSubAccountForMasterAccountErrorBody,
    enable_leverage_token_for_sub_account_for_master_account_error_mapper,
)
from ..errors.enable_margin_for_sub_account_for_master_account_error import (
    EnableMarginForSubAccountForMasterAccountErrorBody,
    enable_margin_for_sub_account_for_master_account_error_mapper,
)
from ..errors.enable_options_for_sub_account_for_master_account_user_data_error import (
    EnableOptionsForSubAccountForMasterAccountUserDataErrorBody,
    enable_options_for_sub_account_for_master_account_user_data_error_mapper,
)
from ..errors.futures_position_risk_of_sub_account_for_master_account_error import (
    FuturesPositionRiskOfSubAccountForMasterAccountErrorBody,
    futures_position_risk_of_sub_account_for_master_account_error_mapper,
)
from ..errors.futures_position_risk_of_sub_account_v2_for_master_account_error import (
    FuturesPositionRiskOfSubAccountV2ForMasterAccountErrorBody,
    futures_position_risk_of_sub_account_v2_for_master_account_error_mapper,
)
from ..errors.get_ip_restriction_for_a_sub_account_api_key_for_master_account_error import (
    GetIpRestrictionForASubAccountApiKeyForMasterAccountErrorBody,
    get_ip_restriction_for_a_sub_account_api_key_for_master_account_error_mapper,
)
from ..errors.get_managed_sub_account_deposit_address_for_investor_master_account_error import (
    GetManagedSubAccountDepositAddressForInvestorMasterAccountErrorBody,
    get_managed_sub_account_deposit_address_for_investor_master_account_error_mapper,
)
from ..errors.managed_sub_account_asset_details_for_investor_master_account_error import (
    ManagedSubAccountAssetDetailsForInvestorMasterAccountErrorBody,
    managed_sub_account_asset_details_for_investor_master_account_error_mapper,
)
from ..errors.managed_sub_account_snapshot_for_investor_master_account_error import (
    ManagedSubAccountSnapshotForInvestorMasterAccountErrorBody,
    managed_sub_account_snapshot_for_investor_master_account_error_mapper,
)
from ..errors.margin_transfer_for_sub_account_for_master_account_error import (
    MarginTransferForSubAccountForMasterAccountErrorBody,
    margin_transfer_for_sub_account_for_master_account_error_mapper,
)
from ..errors.query_managed_sub_account_futures_asset_details_for_investor_master_account_error import (
    QueryManagedSubAccountFuturesAssetDetailsForInvestorMasterAccountErrorBody,
    query_managed_sub_account_futures_asset_details_for_investor_master_account_error_mapper,
)
from ..errors.query_managed_sub_account_list_for_investor_error import (
    QueryManagedSubAccountListForInvestorErrorBody,
    query_managed_sub_account_list_for_investor_error_mapper,
)
from ..errors.query_managed_sub_account_margin_asset_details_for_investor_master_account_error import (
    QueryManagedSubAccountMarginAssetDetailsForInvestorMasterAccountErrorBody,
    query_managed_sub_account_margin_asset_details_for_investor_master_account_error_mapper,
)
from ..errors.query_managed_sub_account_transfer_log_for_investor_master_account_error import (
    QueryManagedSubAccountTransferLogForInvestorMasterAccountErrorBody,
    query_managed_sub_account_transfer_log_for_investor_master_account_error_mapper,
)
from ..errors.query_managed_sub_account_transfer_log_for_trading_team_master_account_error import (
    QueryManagedSubAccountTransferLogForTradingTeamMasterAccountErrorBody,
    query_managed_sub_account_transfer_log_for_trading_team_master_account_error_mapper,
)
from ..errors.query_managed_sub_account_transfer_log_for_trading_team_sub_account_user_data_error import (
    QueryManagedSubAccountTransferLogForTradingTeamSubAccountUserDataErrorBody,
    query_managed_sub_account_transfer_log_for_trading_team_sub_account_user_data_error_mapper,
)
from ..errors.query_sub_account_assets_for_master_account_error import (
    QuerySubAccountAssetsForMasterAccountErrorBody,
    query_sub_account_assets_for_master_account_error_mapper,
)
from ..errors.query_sub_account_list_for_master_account_error import (
    QuerySubAccountListForMasterAccountErrorBody,
    query_sub_account_list_for_master_account_error_mapper,
)
from ..errors.query_sub_account_transaction_statistics_for_master_account_error import (
    QuerySubAccountTransactionStatisticsForMasterAccountErrorBody,
    query_sub_account_transaction_statistics_for_master_account_error_mapper,
)
from ..errors.sub_account_assets_for_master_account_error import (
    SubAccountAssetsForMasterAccountErrorBody,
    sub_account_assets_for_master_account_error_mapper,
)
from ..errors.sub_account_deposit_history_for_master_account_error import (
    SubAccountDepositHistoryForMasterAccountErrorBody,
    sub_account_deposit_history_for_master_account_error_mapper,
)
from ..errors.sub_account_futures_asset_transfer_for_master_account_error import (
    SubAccountFuturesAssetTransferForMasterAccountErrorBody,
    sub_account_futures_asset_transfer_for_master_account_error_mapper,
)
from ..errors.sub_account_futures_asset_transfer_history_for_master_account_error import (
    SubAccountFuturesAssetTransferHistoryForMasterAccountErrorBody,
    sub_account_futures_asset_transfer_history_for_master_account_error_mapper,
)
from ..errors.sub_account_s_status_on_margin_futures_for_master_account_error import (
    SubAccountSStatusOnMarginFuturesForMasterAccountErrorBody,
    sub_account_s_status_on_margin_futures_for_master_account_error_mapper,
)
from ..errors.sub_account_spot_asset_transfer_history_for_master_account_error import (
    SubAccountSpotAssetTransferHistoryForMasterAccountErrorBody,
    sub_account_spot_asset_transfer_history_for_master_account_error_mapper,
)
from ..errors.sub_account_spot_assets_summary_for_master_account2_error import (
    SubAccountSpotAssetsSummaryForMasterAccount2ErrorBody,
    sub_account_spot_assets_summary_for_master_account2_error_mapper,
)
from ..errors.sub_account_spot_assets_summary_for_master_account_error import (
    SubAccountSpotAssetsSummaryForMasterAccountErrorBody,
    sub_account_spot_assets_summary_for_master_account_error_mapper,
)
from ..errors.sub_account_transfer_history_for_sub_account_error import (
    SubAccountTransferHistoryForSubAccountErrorBody,
    sub_account_transfer_history_for_sub_account_error_mapper,
)
from ..errors.summary_of_sub_account_s_futures_account_for_master_account_error import (
    SummaryOfSubAccountSFuturesAccountForMasterAccountErrorBody,
    summary_of_sub_account_s_futures_account_for_master_account_error_mapper,
)
from ..errors.summary_of_sub_account_s_futures_account_v2_for_master_account_error import (
    SummaryOfSubAccountSFuturesAccountV2ForMasterAccountErrorBody,
    summary_of_sub_account_s_futures_account_v2_for_master_account_error_mapper,
)
from ..errors.summary_of_sub_account_s_margin_account_for_master_account_error import (
    SummaryOfSubAccountSMarginAccountForMasterAccountErrorBody,
    summary_of_sub_account_s_margin_account_for_master_account_error_mapper,
)
from ..errors.transfer_for_sub_account_for_master_account_error import (
    TransferForSubAccountForMasterAccountErrorBody,
    transfer_for_sub_account_for_master_account_error_mapper,
)
from ..errors.transfer_to_master_for_sub_account_error import (
    TransferToMasterForSubAccountErrorBody,
    transfer_to_master_for_sub_account_error_mapper,
)
from ..errors.transfer_to_sub_account_of_same_master_for_sub_account_error import (
    TransferToSubAccountOfSameMasterForSubAccountErrorBody,
    transfer_to_sub_account_of_same_master_for_sub_account_error_mapper,
)
from ..errors.universal_transfer_for_master_account_error import (
    UniversalTransferForMasterAccountErrorBody,
    universal_transfer_for_master_account_error_mapper,
)
from ..errors.universal_transfer_history_for_master_account_error import (
    UniversalTransferHistoryForMasterAccountErrorBody,
    universal_transfer_history_for_master_account_error_mapper,
)
from ..errors.update_ip_restriction_for_sub_account_api_key_for_master_account_error import (
    UpdateIpRestrictionForSubAccountApiKeyForMasterAccountErrorBody,
    update_ip_restriction_for_sub_account_api_key_for_master_account_error_mapper,
)
from ..errors.withdrawl_assets_from_the_managed_sub_account_for_investor_master_account_error import (
    WithdrawlAssetsFromTheManagedSubAccountForInvestorMasterAccountErrorBody,
    withdrawl_assets_from_the_managed_sub_account_for_investor_master_account_error_mapper,
)
from ..models.enums.from_account_type import FromAccountTypeOrStr
from ..models.enums.is_freeze import IsFreezeOrStr
from ..models.enums.to_account_type import ToAccountTypeOrStr
from ..models.enums.transfer_function_account_type import TransferFunctionAccountTypeOrStr
from ..models.enums.transfers import TransfersOrStr
from ..models.sapi_v1_capital_deposit_sub_address_response import SapiV1CapitalDepositSubAddressResponse
from ..models.sapi_v1_capital_deposit_sub_hisrec_response import SapiV1CapitalDepositSubHisrecResponse
from ..models.sapi_v1_managed_subaccount_account_snapshot_response import SapiV1ManagedSubaccountAccountSnapshotResponse
from ..models.sapi_v1_managed_subaccount_asset_response import SapiV1ManagedSubaccountAssetResponse
from ..models.sapi_v1_managed_subaccount_deposit_address_response import SapiV1ManagedSubaccountDepositAddressResponse
from ..models.sapi_v1_managed_subaccount_deposit_response import SapiV1ManagedSubaccountDepositResponse
from ..models.sapi_v1_managed_subaccount_fetch_future_asset_response import (
    SapiV1ManagedSubaccountFetchFutureAssetResponse,
)
from ..models.sapi_v1_managed_subaccount_info_response import SapiV1ManagedSubaccountInfoResponse
from ..models.sapi_v1_managed_subaccount_margin_asset_response import SapiV1ManagedSubaccountMarginAssetResponse
from ..models.sapi_v1_managed_subaccount_query_trans_log_for_investor_response import (
    SapiV1ManagedSubaccountQueryTransLogForInvestorResponse,
)
from ..models.sapi_v1_managed_subaccount_query_trans_log_for_trade_parent_response import (
    SapiV1ManagedSubaccountQueryTransLogForTradeParentResponse,
)
from ..models.sapi_v1_managed_subaccount_query_trans_log_response import SapiV1ManagedSubaccountQueryTransLogResponse
from ..models.sapi_v1_managed_subaccount_withdraw_response import SapiV1ManagedSubaccountWithdrawResponse
from ..models.sapi_v1_sub_account_blvt_enable_response import SapiV1SubAccountBlvtEnableResponse
from ..models.sapi_v1_sub_account_eoptions_enable_response import SapiV1SubAccountEoptionsEnableResponse
from ..models.sapi_v1_sub_account_futures_account_response import SapiV1SubAccountFuturesAccountResponse
from ..models.sapi_v1_sub_account_futures_account_summary_response import SapiV1SubAccountFuturesAccountSummaryResponse
from ..models.sapi_v1_sub_account_futures_enable_response import SapiV1SubAccountFuturesEnableResponse
from ..models.sapi_v1_sub_account_futures_internal_transfer_response import (
    SapiV1SubAccountFuturesInternalTransferResponse,
)
from ..models.sapi_v1_sub_account_futures_internal_transfer_response1 import (
    SapiV1SubAccountFuturesInternalTransferResponse1,
)
from ..models.sapi_v1_sub_account_futures_position_risk_response import SapiV1SubAccountFuturesPositionRiskResponse
from ..models.sapi_v1_sub_account_futures_transfer_response import SapiV1SubAccountFuturesTransferResponse
from ..models.sapi_v1_sub_account_list_response import SapiV1SubAccountListResponse
from ..models.sapi_v1_sub_account_margin_account_response import SapiV1SubAccountMarginAccountResponse
from ..models.sapi_v1_sub_account_margin_account_summary_response import SapiV1SubAccountMarginAccountSummaryResponse
from ..models.sapi_v1_sub_account_margin_enable_response import SapiV1SubAccountMarginEnableResponse
from ..models.sapi_v1_sub_account_margin_transfer_response import SapiV1SubAccountMarginTransferResponse
from ..models.sapi_v1_sub_account_spot_summary_response import SapiV1SubAccountSpotSummaryResponse
from ..models.sapi_v1_sub_account_status_response import SapiV1SubAccountStatusResponse
from ..models.sapi_v1_sub_account_sub_account_api_ip_restriction_ip_list_response import (
    SapiV1SubAccountSubAccountApiIpRestrictionIpListResponse,
)
from ..models.sapi_v1_sub_account_sub_account_api_ip_restriction_response import (
    SapiV1SubAccountSubAccountApiIpRestrictionResponse,
)
from ..models.sapi_v1_sub_account_sub_transfer_history_response import SapiV1SubAccountSubTransferHistoryResponse
from ..models.sapi_v1_sub_account_transaction_statistics_response import SapiV1SubAccountTransactionStatisticsResponse
from ..models.sapi_v1_sub_account_transfer_sub_to_master_response import SapiV1SubAccountTransferSubToMasterResponse
from ..models.sapi_v1_sub_account_transfer_sub_to_sub_response import SapiV1SubAccountTransferSubToSubResponse
from ..models.sapi_v1_sub_account_transfer_sub_user_history_response import (
    SapiV1SubAccountTransferSubUserHistoryResponse,
)
from ..models.sapi_v1_sub_account_universal_transfer_response import SapiV1SubAccountUniversalTransferResponse
from ..models.sapi_v1_sub_account_universal_transfer_response1 import SapiV1SubAccountUniversalTransferResponse1
from ..models.sapi_v1_sub_account_virtual_sub_account_response import SapiV1SubAccountVirtualSubAccountResponse
from ..models.sapi_v2_sub_account_sub_account_api_ip_restriction_response import (
    SapiV2SubAccountSubAccountApiIpRestrictionResponse,
)
from ..models.sapi_v3_sub_account_assets_response import SapiV3SubAccountAssetsResponse
from ..models.sapi_v4_sub_account_assets_response import SapiV4SubAccountAssetsResponse
from ..models.unions.sapi_v2_sub_account_futures_account_response import SapiV2SubAccountFuturesAccountResponse
from ..models.unions.sapi_v2_sub_account_futures_account_summary_response import (
    SapiV2SubAccountFuturesAccountSummaryResponse,
)
from ..models.unions.sapi_v2_sub_account_futures_position_risk_response import (
    SapiV2SubAccountFuturesPositionRiskResponse,
)
from ..server.server import Server


class SubAccountApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SubAccountApiWithRawResponse(client, server, auth)

    def create_a_virtual_sub_account_for_master_account(
        self,
        sub_account_string: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountVirtualSubAccountResponse:
        """- This request will generate a virtual sub account under your master account.
        - You need to enable "trade" option for the api key which requests this endpoint.

        Weight(IP): 1

        Args:
            sub_account_string: Please input a string. We will create a virtual email using that string for you to
                register
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Return the created virtual email

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.create_a_virtual_sub_account_for_master_account(
            sub_account_string, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def delete_ip_list_for_a_sub_account_api_key_for_master_account(
        self,
        email: str,
        sub_account_api_key: str,
        timestamp: int,
        signature: str,
        *,
        ip_address: str | None = None,
        third_party_name: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountSubAccountApiIpRestrictionIpListResponse:
        """Weight(UID): 3000

        Args:
            email: Sub-account email
            sub_account_api_key: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            ip_address: Can be added in batches, separated by commas
            third_party_name: third party IP list name
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Delete IP information

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.delete_ip_list_for_a_sub_account_api_key_for_master_account(
            email,
            sub_account_api_key,
            timestamp,
            signature,
            ip_address=ip_address,
            third_party_name=third_party_name,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def deposit_assets_into_the_managed_sub_account_for_investor_master_account(
        self,
        to_email: str,
        asset: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1ManagedSubaccountDepositResponse:
        """Weight(IP): 1

        Args:
            to_email: Recipient email
            asset: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Transfer id

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.deposit_assets_into_the_managed_sub_account_for_investor_master_account(
            to_email, asset, amount, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def detail_on_sub_account_s_futures_account_for_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountFuturesAccountResponse:
        """Weight(IP): 10

        Args:
            email: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Futures account details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.detail_on_sub_account_s_futures_account_for_master_account(
            email, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def detail_on_sub_account_s_futures_account_v2_for_master_account(
        self,
        email: str,
        futures_type: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV2SubAccountFuturesAccountResponse:
        """Weight(IP): 1

        Args:
            email: Sub-account email
            futures_type: * ``1`` - USDT Margined Futures * ``2`` - COIN Margined Futures
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            USDT or COIN Margined Futures Details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.detail_on_sub_account_s_futures_account_v2_for_master_account(
            email, futures_type, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def detail_on_sub_account_s_margin_account_for_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountMarginAccountResponse:
        """Weight(IP): 10

        Args:
            email: Sub-account email
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Margin sub-account details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.detail_on_sub_account_s_margin_account_for_master_account(
            email, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def enable_futures_for_sub_account_for_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountFuturesEnableResponse:
        """Weight(IP): 1

        Args:
            email: Sub-account email
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Futures status

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.enable_futures_for_sub_account_for_master_account(
            email, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def enable_leverage_token_for_sub_account_for_master_account(
        self,
        email: str,
        enable_blvt: bool,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountBlvtEnableResponse:
        """Weight(IP): 1

        Args:
            email: Sub-account email
            enable_blvt: Only true for now
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            BLVT status

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.enable_leverage_token_for_sub_account_for_master_account(
            email, enable_blvt, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def enable_margin_for_sub_account_for_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountMarginEnableResponse:
        """Weight(IP): 1

        Args:
            email: Sub-account email
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Margin status

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.enable_margin_for_sub_account_for_master_account(
            email, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def enable_options_for_sub_account_for_master_account_user_data(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountEoptionsEnableResponse:
        """Enable Options for Sub-account (For Master Account).

        Weight(IP): 1

        Args:
            email: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Sub account EOptions status

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.enable_options_for_sub_account_for_master_account_user_data(
            email, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def futures_position_risk_of_sub_account_for_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1SubAccountFuturesPositionRiskResponse]:
        """Weight(IP): 10

        Args:
            email: Sub-account email
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Futures account summary

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.futures_position_risk_of_sub_account_for_master_account(
            email, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def futures_position_risk_of_sub_account_v2_for_master_account(
        self,
        email: str,
        futures_type: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV2SubAccountFuturesPositionRiskResponse:
        """Weight(IP): 1

        Args:
            email: Sub-account email
            futures_type: * ``1`` - USDT Margined Futures * ``2`` - COIN Margined Futures
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            USDT or COIN Margined Futures Position Risk

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.futures_position_risk_of_sub_account_v2_for_master_account(
            email, futures_type, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def get_ip_restriction_for_a_sub_account_api_key_for_master_account(
        self,
        email: str,
        sub_account_api_key: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountSubAccountApiIpRestrictionResponse:
        """Weight(UID): 3000

        Args:
            email: Sub-account email
            sub_account_api_key: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            IP Restriction information

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_ip_restriction_for_a_sub_account_api_key_for_master_account(
            email, sub_account_api_key, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def get_managed_sub_account_deposit_address_for_investor_master_account(
        self,
        email: str,
        coin: str,
        timestamp: int,
        signature: str,
        *,
        network: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1ManagedSubaccountDepositAddressResponse:
        """Get investor's managed sub-account deposit address

        Weight(UID): 1

        Args:
            email: Value sent with the request.
            coin: Coin name
            timestamp: UTC timestamp in ms
            signature: Signature
            network: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Managed sub deposit address

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_managed_sub_account_deposit_address_for_investor_master_account(
            email, coin, timestamp, signature, network=network, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def managed_sub_account_asset_details_for_investor_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1ManagedSubaccountAssetResponse]:
        """Weight(IP): 1

        Args:
            email: Sub-account email
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of asset details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.managed_sub_account_asset_details_for_investor_master_account(
            email, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def managed_sub_account_snapshot_for_investor_master_account(
        self,
        email: str,
        type_: str,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1ManagedSubaccountAccountSnapshotResponse:
        """- The query time period must be less then 30 days
        - Support query within the last one month only
        - If ``startTime`` and ``endTime`` not sent, return records of the last 7 days by default

        Weight(IP): 2400

        Args:
            email: Sub-account email
            type_: "SPOT", "MARGIN"(cross), "FUTURES"(UM)
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: min 7, max 30, default 7
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Sub-account spot snapshot

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.managed_sub_account_snapshot_for_investor_master_account(
            email,
            type_,
            timestamp,
            signature,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def margin_transfer_for_sub_account_for_master_account(
        self,
        email: str,
        asset: str,
        amount: float,
        type_: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountMarginTransferResponse:
        """Weight(IP): 1

        Args:
            email: Sub-account email
            asset: Value sent with the request.
            amount: Value sent with the request.
            type_: * ``1`` - transfer from subaccount's spot account to margin account * ``2`` - transfer from
                subaccount's margin account to its spot account
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Transfer id

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.margin_transfer_for_sub_account_for_master_account(
            email, asset, amount, type_, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def query_managed_sub_account_transfer_log_for_investor_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        transfers: str | None = None,
        transfer_function_account_type: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1ManagedSubaccountQueryTransLogForInvestorResponse:
        """Investor can use this api to query managed sub account transfer log. This endpoint is available for investor
        of Managed Sub-Account. A Managed Sub-Account is an account type for investors who value flexibility in asset
        allocation and account application, while delegating trades to a professional trading team.

        Weight(IP): 1

        Args:
            email: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            page: Default 1
            limit: Default 500; max 1000.
            transfers: Transfer Direction (FROM/TO)
            transfer_function_account_type: Transfer function account type
                (SPOT/MARGIN/ISOLATED_MARGIN/USDT_FUTURE/COIN_FUTURE)
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Managed sub account transfer logs (for invest account)

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_managed_sub_account_transfer_log_for_investor_master_account(
            email,
            timestamp,
            signature,
            start_time=start_time,
            end_time=end_time,
            page=page,
            limit=limit,
            transfers=transfers,
            transfer_function_account_type=transfer_function_account_type,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def query_managed_sub_account_transfer_log_for_trading_team_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        transfers: str | None = None,
        transfer_function_account_type: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1ManagedSubaccountQueryTransLogForTradeParentResponse:
        """Trading team can use this api to query managed sub account transfer log. This endpoint is available for
        trading team of Managed Sub-Account. A Managed Sub-Account is an account type for investors who value
        flexibility in asset allocation and account application, while delegating trades to a professional trading team

        Weight(IP): 60

        Args:
            email: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            page: Default 1
            limit: Default 500; max 1000.
            transfers: Transfer Direction (FROM/TO)
            transfer_function_account_type: Transfer function account type
                (SPOT/MARGIN/ISOLATED_MARGIN/USDT_FUTURE/COIN_FUTURE)
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Managed sub account transfer logs (for trading team)

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_managed_sub_account_transfer_log_for_trading_team_master_account(
            email,
            timestamp,
            signature,
            start_time=start_time,
            end_time=end_time,
            page=page,
            limit=limit,
            transfers=transfers,
            transfer_function_account_type=transfer_function_account_type,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def query_managed_sub_account_transfer_log_for_trading_team_sub_account_user_data(
        self,
        transfers: TransfersOrStr,
        transfer_function_account_type: TransferFunctionAccountTypeOrStr,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1ManagedSubaccountQueryTransLogResponse:
        """Query Managed Sub Account Transfer Log (For Trading Team Sub Account)

        Weight(UID): 60

        Args:
            transfers: Transfer Direction
            transfer_function_account_type: Transfer function account type
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            page: Default 1
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Managed sub deposit address

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_managed_sub_account_transfer_log_for_trading_team_sub_account_user_data(
            transfers,
            transfer_function_account_type,
            timestamp,
            signature,
            start_time=start_time,
            end_time=end_time,
            page=page,
            limit=limit,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def query_managed_sub_account_futures_asset_details_for_investor_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1ManagedSubaccountFetchFutureAssetResponse:
        """Investor can use this api to query managed sub account futures asset details

        Args:
            email: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Sub account futures assset details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_managed_sub_account_futures_asset_details_for_investor_master_account(
            email, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def query_managed_sub_account_list_for_investor(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        page: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1ManagedSubaccountInfoResponse:
        """Get investor's managed sub-account list.

        Weight(UID): 60

        Args:
            email: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            page: Default 1
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Managed sub account list

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_managed_sub_account_list_for_investor(
            email,
            timestamp,
            signature,
            page=page,
            limit=limit,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def query_managed_sub_account_margin_asset_details_for_investor_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1ManagedSubaccountMarginAssetResponse:
        """Investor can use this api to query managed sub account margin asset details

        Args:
            email: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Sub account margin assset details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_managed_sub_account_margin_asset_details_for_investor_master_account(
            email, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def query_sub_account_assets_for_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV4SubAccountAssetsResponse:
        """Fetch sub-account assets

        Weight(UID): 60

        Args:
            email: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Sub account balances

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_sub_account_assets_for_master_account(
            email, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def query_sub_account_list_for_master_account(
        self,
        timestamp: int,
        signature: str,
        *,
        email: str | None = None,
        is_freeze: IsFreezeOrStr | None = None,
        page: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountListResponse:
        """Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            email: Sub-account email
            is_freeze: Value sent with the request.
            page: Default 1
            limit: Default 1; max 200
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of sub-accounts

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_sub_account_list_for_master_account(
            timestamp,
            signature,
            email=email,
            is_freeze=is_freeze,
            page=page,
            limit=limit,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def query_sub_account_transaction_statistics_for_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountTransactionStatisticsResponse:
        """Query Sub-account Transaction statistics (For Master Account).

        Weight(UID): 60

        Args:
            email: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Sub account transaction statistics

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_sub_account_transaction_statistics_for_master_account(
            email, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def sub_account_assets_for_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV3SubAccountAssetsResponse:
        """Fetch sub-account assets

        Weight(IP): 1

        Args:
            email: Sub-account email
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of assets balances

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.sub_account_assets_for_master_account(
            email, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def sub_account_deposit_history_for_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        coin: str | None = None,
        status: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        offset: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1CapitalDepositSubHisrecResponse]:
        """Fetch sub-account deposit history

        Weight(IP): 1

        Args:
            email: Sub-account email
            timestamp: UTC timestamp in ms
            signature: Signature
            coin: Coin name
            status: 0(0:pending,6: credited but cannot withdraw, 1:success)
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Value sent with the request.
            offset: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Sub-account deposit history

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.sub_account_deposit_history_for_master_account(
            email,
            timestamp,
            signature,
            coin=coin,
            status=status,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
            offset=offset,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def sub_account_futures_asset_transfer_for_master_account(
        self,
        from_email: str,
        to_email: str,
        futures_type: int,
        asset: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountFuturesInternalTransferResponse1:
        """- Master account can transfer max 2000 times a minute

        Weight(IP): 1

        Args:
            from_email: Sender email
            to_email: Recipient email
            futures_type: 1:USDT-margined Futures,2: Coin-margined Futures
            asset: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Futures Asset Transfer Info

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.sub_account_futures_asset_transfer_for_master_account(
            from_email,
            to_email,
            futures_type,
            asset,
            amount,
            timestamp,
            signature,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def sub_account_futures_asset_transfer_history_for_master_account(
        self,
        email: str,
        futures_type: int,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountFuturesInternalTransferResponse:
        """Weight(IP): 1

        Args:
            email: Sub-account email
            futures_type: 1:USDT-margined Futures, 2: Coin-margined Futures
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            page: Default 1
            limit: Default value: 50, Max value: 500
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Sub-account Futures Asset Transfer History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.sub_account_futures_asset_transfer_history_for_master_account(
            email,
            futures_type,
            timestamp,
            signature,
            start_time=start_time,
            end_time=end_time,
            page=page,
            limit=limit,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def sub_account_spot_asset_transfer_history_for_master_account(
        self,
        timestamp: int,
        signature: str,
        *,
        from_email: str | None = None,
        to_email: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1SubAccountSubTransferHistoryResponse]:
        """- fromEmail and toEmail cannot be sent at the same time.
        - Return fromEmail equal master account email by default.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            from_email: Sub-account email
            to_email: Sub-account email
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            page: Default 1
            limit: Default 1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Sub-account Spot Asset Transfer History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.sub_account_spot_asset_transfer_history_for_master_account(
            timestamp,
            signature,
            from_email=from_email,
            to_email=to_email,
            start_time=start_time,
            end_time=end_time,
            page=page,
            limit=limit,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def sub_account_spot_assets_summary_for_master_account(
        self,
        timestamp: int,
        signature: str,
        *,
        email: str | None = None,
        page: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountSpotSummaryResponse:
        """Get BTC valued asset summary of subaccounts.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            email: Sub-account email
            page: Default 1
            size: Default:10 Max:20
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Summary of Sub-account Spot Assets

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.sub_account_spot_assets_summary_for_master_account(
            timestamp,
            signature,
            email=email,
            page=page,
            size=size,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def sub_account_spot_assets_summary_for_master_account_2(
        self,
        email: str,
        coin: str,
        timestamp: int,
        signature: str,
        *,
        network: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1CapitalDepositSubAddressResponse:
        """Fetch sub-account deposit address

        Weight(IP): 1

        Args:
            email: Sub-account email
            coin: Coin name
            timestamp: UTC timestamp in ms
            signature: Signature
            network: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Deposit address info

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.sub_account_spot_assets_summary_for_master_account_2(
            email, coin, timestamp, signature, network=network, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def sub_account_transfer_history_for_sub_account(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        type_: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1SubAccountTransferSubUserHistoryResponse]:
        """- If ``type`` is not sent, the records of type 2: transfer out will be returned by default.
        - If ``startTime`` and ``endTime`` are not sent, the recent 30-day data will be returned.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            type_: * ``1`` - transfer in * ``2`` - transfer out
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Transfer id

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.sub_account_transfer_history_for_sub_account(
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

    def sub_account_s_status_on_margin_futures_for_master_account(
        self,
        timestamp: int,
        signature: str,
        *,
        email: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1SubAccountStatusResponse]:
        """- If no ``email`` sent, all sub-accounts' information will be returned.

        Weight(IP): 10

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            email: Sub-account email
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Status on Margin/Futures

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.sub_account_s_status_on_margin_futures_for_master_account(
            timestamp, signature, email=email, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def summary_of_sub_account_s_futures_account_for_master_account(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountFuturesAccountSummaryResponse:
        """Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Futures account summary

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.summary_of_sub_account_s_futures_account_for_master_account(
            timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def summary_of_sub_account_s_futures_account_v2_for_master_account(
        self,
        futures_type: int,
        timestamp: int,
        signature: str,
        *,
        page: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV2SubAccountFuturesAccountSummaryResponse:
        """Weight(IP): 10

        Args:
            futures_type: * ``1`` - USDT Margined Futures * ``2`` - COIN Margined Futures
            timestamp: UTC timestamp in ms
            signature: Signature
            page: Default 1
            limit: Default 10, Max 20
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            USDT or COIN Margined Futures Summary

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.summary_of_sub_account_s_futures_account_v2_for_master_account(
            futures_type,
            timestamp,
            signature,
            page=page,
            limit=limit,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def summary_of_sub_account_s_margin_account_for_master_account(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountMarginAccountSummaryResponse:
        """Weight(IP): 10

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Margin sub-account details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.summary_of_sub_account_s_margin_account_for_master_account(
            timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def transfer_for_sub_account_for_master_account(
        self,
        email: str,
        asset: str,
        amount: float,
        type_: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountFuturesTransferResponse:
        """Weight(IP): 1

        Args:
            email: Sub-account email
            asset: Value sent with the request.
            amount: Value sent with the request.
            type_: * ``1`` - transfer from subaccount's spot account to its USDT-margined futures account * ``2`` -
                transfer from subaccount's USDT-margined futures account to its spot account * ``3`` - transfer from
                subaccount's spot account to its COIN-margined futures account * ``4`` - transfer from subaccount's
                COIN-margined futures account to its spot account
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Transfer id

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.transfer_for_sub_account_for_master_account(
            email, asset, amount, type_, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def transfer_to_master_for_sub_account(
        self,
        asset: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountTransferSubToMasterResponse:
        """Weight(IP): 1

        Args:
            asset: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Transfer id

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.transfer_to_master_for_sub_account(
            asset, amount, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def transfer_to_sub_account_of_same_master_for_sub_account(
        self,
        to_email: str,
        asset: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountTransferSubToSubResponse:
        """Weight(IP): 1

        Args:
            to_email: Recipient email
            asset: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Transfer id

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.transfer_to_sub_account_of_same_master_for_sub_account(
            to_email, asset, amount, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def universal_transfer_for_master_account(
        self,
        from_account_type: FromAccountTypeOrStr,
        to_account_type: ToAccountTypeOrStr,
        asset: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        from_email: str | None = None,
        to_email: str | None = None,
        client_tran_id: str | None = None,
        symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountUniversalTransferResponse1:
        """- You need to enable "internal transfer" option for the api key which requests this endpoint.
        - Transfer from master account by default if fromEmail is not sent.
        - Transfer to master account by default if toEmail is not sent.
        - Supported transfer scenarios:
          - Master account SPOT transfer to sub-account SPOT,USDT_FUTURE,COIN_FUTURE,MARGIN(Cross),ISOLATED_MARGIN
          - Sub-account SPOT,USDT_FUTURE,COIN_FUTURE,MARGIN(Cross),ISOLATED_MARGIN transfer to master account SPOT
          - Transfer between two sub-account SPOT accounts

        Weight(IP): 1

        Args:
            from_account_type: Value sent with the request.
            to_account_type: Value sent with the request.
            asset: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            from_email: Sub-account email
            to_email: Sub-account email
            client_tran_id: Value sent with the request.
            symbol: Only supported under ISOLATED_MARGIN type
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Transfer id

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.universal_transfer_for_master_account(
            from_account_type,
            to_account_type,
            asset,
            amount,
            timestamp,
            signature,
            from_email=from_email,
            to_email=to_email,
            client_tran_id=client_tran_id,
            symbol=symbol,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def universal_transfer_history_for_master_account(
        self,
        timestamp: int,
        signature: str,
        *,
        from_email: str | None = None,
        to_email: str | None = None,
        client_tran_id: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1SubAccountUniversalTransferResponse]:
        """- ``fromEmail`` and ``toEmail`` cannot be sent at the same time.
        - Return ``fromEmail`` equal master account email by default.
        - The query time period must be less then 30 days.
        - If startTime and endTime not sent, return records of the last 30 days by default.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            from_email: Sub-account email
            to_email: Sub-account email
            client_tran_id: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            page: Default 1
            limit: Default 500, Max 500
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Transfer History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.universal_transfer_history_for_master_account(
            timestamp,
            signature,
            from_email=from_email,
            to_email=to_email,
            client_tran_id=client_tran_id,
            start_time=start_time,
            end_time=end_time,
            page=page,
            limit=limit,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def update_ip_restriction_for_sub_account_api_key_for_master_account(
        self,
        email: str,
        sub_account_api_key: str,
        status: str,
        timestamp: int,
        signature: str,
        *,
        third_party_name: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV2SubAccountSubAccountApiIpRestrictionResponse:
        """Update IP Restriction for Sub-Account API key

        Weight(UID): 3000

        Args:
            email: Sub-account email
            sub_account_api_key: Value sent with the request.
            status: IP Restriction status. 1 = IP Unrestricted. 2 = Restrict access to trusted IPs only. 3 = Restrict
                access to users' trusted third party IPs only
            timestamp: UTC timestamp in ms
            signature: Signature
            third_party_name: third party IP list name
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Update IP Restriction

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.update_ip_restriction_for_sub_account_api_key_for_master_account(
            email,
            sub_account_api_key,
            status,
            timestamp,
            signature,
            third_party_name=third_party_name,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def withdrawl_assets_from_the_managed_sub_account_for_investor_master_account(
        self,
        from_email: str,
        asset: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        transfer_date: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1ManagedSubaccountWithdrawResponse:
        """Weight(IP): 1

        Args:
            from_email: Sender email
            asset: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            transfer_date: Withdrawals is automatically occur on the transfer date(UTC0). If a date is not selected, the
                withdrawal occurs right now
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Transfer id

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.withdrawl_assets_from_the_managed_sub_account_for_investor_master_account(
            from_email,
            asset,
            amount,
            timestamp,
            signature,
            transfer_date=transfer_date,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> SubAccountApiWithRawResponse:
        return self._with_raw_response


class AsyncSubAccountApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSubAccountApiWithRawResponse(client, server, auth)

    async def create_a_virtual_sub_account_for_master_account(
        self,
        sub_account_string: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountVirtualSubAccountResponse:
        """- This request will generate a virtual sub account under your master account.
        - You need to enable "trade" option for the api key which requests this endpoint.

        Weight(IP): 1

        Args:
            sub_account_string: Please input a string. We will create a virtual email using that string for you to
                register
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Return the created virtual email

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.create_a_virtual_sub_account_for_master_account(
                sub_account_string, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def delete_ip_list_for_a_sub_account_api_key_for_master_account(
        self,
        email: str,
        sub_account_api_key: str,
        timestamp: int,
        signature: str,
        *,
        ip_address: str | None = None,
        third_party_name: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountSubAccountApiIpRestrictionIpListResponse:
        """Weight(UID): 3000

        Args:
            email: Sub-account email
            sub_account_api_key: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            ip_address: Can be added in batches, separated by commas
            third_party_name: third party IP list name
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Delete IP information

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.delete_ip_list_for_a_sub_account_api_key_for_master_account(
                email,
                sub_account_api_key,
                timestamp,
                signature,
                ip_address=ip_address,
                third_party_name=third_party_name,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def deposit_assets_into_the_managed_sub_account_for_investor_master_account(
        self,
        to_email: str,
        asset: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1ManagedSubaccountDepositResponse:
        """Weight(IP): 1

        Args:
            to_email: Recipient email
            asset: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Transfer id

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.deposit_assets_into_the_managed_sub_account_for_investor_master_account(
                to_email, asset, amount, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def detail_on_sub_account_s_futures_account_for_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountFuturesAccountResponse:
        """Weight(IP): 10

        Args:
            email: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Futures account details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.detail_on_sub_account_s_futures_account_for_master_account(
                email, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def detail_on_sub_account_s_futures_account_v2_for_master_account(
        self,
        email: str,
        futures_type: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV2SubAccountFuturesAccountResponse:
        """Weight(IP): 1

        Args:
            email: Sub-account email
            futures_type: * ``1`` - USDT Margined Futures * ``2`` - COIN Margined Futures
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            USDT or COIN Margined Futures Details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.detail_on_sub_account_s_futures_account_v2_for_master_account(
                email, futures_type, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def detail_on_sub_account_s_margin_account_for_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountMarginAccountResponse:
        """Weight(IP): 10

        Args:
            email: Sub-account email
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Margin sub-account details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.detail_on_sub_account_s_margin_account_for_master_account(
                email, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def enable_futures_for_sub_account_for_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountFuturesEnableResponse:
        """Weight(IP): 1

        Args:
            email: Sub-account email
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Futures status

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.enable_futures_for_sub_account_for_master_account(
                email, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def enable_leverage_token_for_sub_account_for_master_account(
        self,
        email: str,
        enable_blvt: bool,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountBlvtEnableResponse:
        """Weight(IP): 1

        Args:
            email: Sub-account email
            enable_blvt: Only true for now
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            BLVT status

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.enable_leverage_token_for_sub_account_for_master_account(
                email, enable_blvt, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def enable_margin_for_sub_account_for_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountMarginEnableResponse:
        """Weight(IP): 1

        Args:
            email: Sub-account email
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Margin status

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.enable_margin_for_sub_account_for_master_account(
                email, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def enable_options_for_sub_account_for_master_account_user_data(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountEoptionsEnableResponse:
        """Enable Options for Sub-account (For Master Account).

        Weight(IP): 1

        Args:
            email: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Sub account EOptions status

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.enable_options_for_sub_account_for_master_account_user_data(
                email, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def futures_position_risk_of_sub_account_for_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1SubAccountFuturesPositionRiskResponse]:
        """Weight(IP): 10

        Args:
            email: Sub-account email
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Futures account summary

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.futures_position_risk_of_sub_account_for_master_account(
                email, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def futures_position_risk_of_sub_account_v2_for_master_account(
        self,
        email: str,
        futures_type: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV2SubAccountFuturesPositionRiskResponse:
        """Weight(IP): 1

        Args:
            email: Sub-account email
            futures_type: * ``1`` - USDT Margined Futures * ``2`` - COIN Margined Futures
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            USDT or COIN Margined Futures Position Risk

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.futures_position_risk_of_sub_account_v2_for_master_account(
                email, futures_type, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def get_ip_restriction_for_a_sub_account_api_key_for_master_account(
        self,
        email: str,
        sub_account_api_key: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountSubAccountApiIpRestrictionResponse:
        """Weight(UID): 3000

        Args:
            email: Sub-account email
            sub_account_api_key: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            IP Restriction information

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_ip_restriction_for_a_sub_account_api_key_for_master_account(
                email,
                sub_account_api_key,
                timestamp,
                signature,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def get_managed_sub_account_deposit_address_for_investor_master_account(
        self,
        email: str,
        coin: str,
        timestamp: int,
        signature: str,
        *,
        network: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1ManagedSubaccountDepositAddressResponse:
        """Get investor's managed sub-account deposit address

        Weight(UID): 1

        Args:
            email: Value sent with the request.
            coin: Coin name
            timestamp: UTC timestamp in ms
            signature: Signature
            network: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Managed sub deposit address

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_managed_sub_account_deposit_address_for_investor_master_account(
                email,
                coin,
                timestamp,
                signature,
                network=network,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def managed_sub_account_asset_details_for_investor_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1ManagedSubaccountAssetResponse]:
        """Weight(IP): 1

        Args:
            email: Sub-account email
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of asset details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.managed_sub_account_asset_details_for_investor_master_account(
                email, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def managed_sub_account_snapshot_for_investor_master_account(
        self,
        email: str,
        type_: str,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1ManagedSubaccountAccountSnapshotResponse:
        """- The query time period must be less then 30 days
        - Support query within the last one month only
        - If ``startTime`` and ``endTime`` not sent, return records of the last 7 days by default

        Weight(IP): 2400

        Args:
            email: Sub-account email
            type_: "SPOT", "MARGIN"(cross), "FUTURES"(UM)
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: min 7, max 30, default 7
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Sub-account spot snapshot

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.managed_sub_account_snapshot_for_investor_master_account(
                email,
                type_,
                timestamp,
                signature,
                start_time=start_time,
                end_time=end_time,
                limit=limit,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def margin_transfer_for_sub_account_for_master_account(
        self,
        email: str,
        asset: str,
        amount: float,
        type_: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountMarginTransferResponse:
        """Weight(IP): 1

        Args:
            email: Sub-account email
            asset: Value sent with the request.
            amount: Value sent with the request.
            type_: * ``1`` - transfer from subaccount's spot account to margin account * ``2`` - transfer from
                subaccount's margin account to its spot account
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Transfer id

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.margin_transfer_for_sub_account_for_master_account(
                email,
                asset,
                amount,
                type_,
                timestamp,
                signature,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def query_managed_sub_account_transfer_log_for_investor_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        transfers: str | None = None,
        transfer_function_account_type: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1ManagedSubaccountQueryTransLogForInvestorResponse:
        """Investor can use this api to query managed sub account transfer log. This endpoint is available for investor
        of Managed Sub-Account. A Managed Sub-Account is an account type for investors who value flexibility in asset
        allocation and account application, while delegating trades to a professional trading team.

        Weight(IP): 1

        Args:
            email: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            page: Default 1
            limit: Default 500; max 1000.
            transfers: Transfer Direction (FROM/TO)
            transfer_function_account_type: Transfer function account type
                (SPOT/MARGIN/ISOLATED_MARGIN/USDT_FUTURE/COIN_FUTURE)
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Managed sub account transfer logs (for invest account)

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_managed_sub_account_transfer_log_for_investor_master_account(
                email,
                timestamp,
                signature,
                start_time=start_time,
                end_time=end_time,
                page=page,
                limit=limit,
                transfers=transfers,
                transfer_function_account_type=transfer_function_account_type,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def query_managed_sub_account_transfer_log_for_trading_team_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        transfers: str | None = None,
        transfer_function_account_type: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1ManagedSubaccountQueryTransLogForTradeParentResponse:
        """Trading team can use this api to query managed sub account transfer log. This endpoint is available for
        trading team of Managed Sub-Account. A Managed Sub-Account is an account type for investors who value
        flexibility in asset allocation and account application, while delegating trades to a professional trading team

        Weight(IP): 60

        Args:
            email: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            page: Default 1
            limit: Default 500; max 1000.
            transfers: Transfer Direction (FROM/TO)
            transfer_function_account_type: Transfer function account type
                (SPOT/MARGIN/ISOLATED_MARGIN/USDT_FUTURE/COIN_FUTURE)
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Managed sub account transfer logs (for trading team)

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_managed_sub_account_transfer_log_for_trading_team_master_account(
                email,
                timestamp,
                signature,
                start_time=start_time,
                end_time=end_time,
                page=page,
                limit=limit,
                transfers=transfers,
                transfer_function_account_type=transfer_function_account_type,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def query_managed_sub_account_transfer_log_for_trading_team_sub_account_user_data(
        self,
        transfers: TransfersOrStr,
        transfer_function_account_type: TransferFunctionAccountTypeOrStr,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1ManagedSubaccountQueryTransLogResponse:
        """Query Managed Sub Account Transfer Log (For Trading Team Sub Account)

        Weight(UID): 60

        Args:
            transfers: Transfer Direction
            transfer_function_account_type: Transfer function account type
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            page: Default 1
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Managed sub deposit address

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_managed_sub_account_transfer_log_for_trading_team_sub_account_user_data(
                transfers,
                transfer_function_account_type,
                timestamp,
                signature,
                start_time=start_time,
                end_time=end_time,
                page=page,
                limit=limit,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def query_managed_sub_account_futures_asset_details_for_investor_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1ManagedSubaccountFetchFutureAssetResponse:
        """Investor can use this api to query managed sub account futures asset details

        Args:
            email: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Sub account futures assset details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_managed_sub_account_futures_asset_details_for_investor_master_account(
                email, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def query_managed_sub_account_list_for_investor(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        page: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1ManagedSubaccountInfoResponse:
        """Get investor's managed sub-account list.

        Weight(UID): 60

        Args:
            email: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            page: Default 1
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Managed sub account list

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_managed_sub_account_list_for_investor(
                email,
                timestamp,
                signature,
                page=page,
                limit=limit,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def query_managed_sub_account_margin_asset_details_for_investor_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1ManagedSubaccountMarginAssetResponse:
        """Investor can use this api to query managed sub account margin asset details

        Args:
            email: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Sub account margin assset details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_managed_sub_account_margin_asset_details_for_investor_master_account(
                email, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def query_sub_account_assets_for_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV4SubAccountAssetsResponse:
        """Fetch sub-account assets

        Weight(UID): 60

        Args:
            email: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Sub account balances

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_sub_account_assets_for_master_account(
                email, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def query_sub_account_list_for_master_account(
        self,
        timestamp: int,
        signature: str,
        *,
        email: str | None = None,
        is_freeze: IsFreezeOrStr | None = None,
        page: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountListResponse:
        """Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            email: Sub-account email
            is_freeze: Value sent with the request.
            page: Default 1
            limit: Default 1; max 200
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of sub-accounts

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_sub_account_list_for_master_account(
                timestamp,
                signature,
                email=email,
                is_freeze=is_freeze,
                page=page,
                limit=limit,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def query_sub_account_transaction_statistics_for_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountTransactionStatisticsResponse:
        """Query Sub-account Transaction statistics (For Master Account).

        Weight(UID): 60

        Args:
            email: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Sub account transaction statistics

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_sub_account_transaction_statistics_for_master_account(
                email, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def sub_account_assets_for_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV3SubAccountAssetsResponse:
        """Fetch sub-account assets

        Weight(IP): 1

        Args:
            email: Sub-account email
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of assets balances

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.sub_account_assets_for_master_account(
                email, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def sub_account_deposit_history_for_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        coin: str | None = None,
        status: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        offset: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1CapitalDepositSubHisrecResponse]:
        """Fetch sub-account deposit history

        Weight(IP): 1

        Args:
            email: Sub-account email
            timestamp: UTC timestamp in ms
            signature: Signature
            coin: Coin name
            status: 0(0:pending,6: credited but cannot withdraw, 1:success)
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Value sent with the request.
            offset: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Sub-account deposit history

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.sub_account_deposit_history_for_master_account(
                email,
                timestamp,
                signature,
                coin=coin,
                status=status,
                start_time=start_time,
                end_time=end_time,
                limit=limit,
                offset=offset,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def sub_account_futures_asset_transfer_for_master_account(
        self,
        from_email: str,
        to_email: str,
        futures_type: int,
        asset: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountFuturesInternalTransferResponse1:
        """- Master account can transfer max 2000 times a minute

        Weight(IP): 1

        Args:
            from_email: Sender email
            to_email: Recipient email
            futures_type: 1:USDT-margined Futures,2: Coin-margined Futures
            asset: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Futures Asset Transfer Info

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.sub_account_futures_asset_transfer_for_master_account(
                from_email,
                to_email,
                futures_type,
                asset,
                amount,
                timestamp,
                signature,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def sub_account_futures_asset_transfer_history_for_master_account(
        self,
        email: str,
        futures_type: int,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountFuturesInternalTransferResponse:
        """Weight(IP): 1

        Args:
            email: Sub-account email
            futures_type: 1:USDT-margined Futures, 2: Coin-margined Futures
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            page: Default 1
            limit: Default value: 50, Max value: 500
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Sub-account Futures Asset Transfer History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.sub_account_futures_asset_transfer_history_for_master_account(
                email,
                futures_type,
                timestamp,
                signature,
                start_time=start_time,
                end_time=end_time,
                page=page,
                limit=limit,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def sub_account_spot_asset_transfer_history_for_master_account(
        self,
        timestamp: int,
        signature: str,
        *,
        from_email: str | None = None,
        to_email: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1SubAccountSubTransferHistoryResponse]:
        """- fromEmail and toEmail cannot be sent at the same time.
        - Return fromEmail equal master account email by default.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            from_email: Sub-account email
            to_email: Sub-account email
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            page: Default 1
            limit: Default 1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Sub-account Spot Asset Transfer History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.sub_account_spot_asset_transfer_history_for_master_account(
                timestamp,
                signature,
                from_email=from_email,
                to_email=to_email,
                start_time=start_time,
                end_time=end_time,
                page=page,
                limit=limit,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def sub_account_spot_assets_summary_for_master_account(
        self,
        timestamp: int,
        signature: str,
        *,
        email: str | None = None,
        page: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountSpotSummaryResponse:
        """Get BTC valued asset summary of subaccounts.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            email: Sub-account email
            page: Default 1
            size: Default:10 Max:20
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Summary of Sub-account Spot Assets

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.sub_account_spot_assets_summary_for_master_account(
                timestamp,
                signature,
                email=email,
                page=page,
                size=size,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def sub_account_spot_assets_summary_for_master_account_2(
        self,
        email: str,
        coin: str,
        timestamp: int,
        signature: str,
        *,
        network: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1CapitalDepositSubAddressResponse:
        """Fetch sub-account deposit address

        Weight(IP): 1

        Args:
            email: Sub-account email
            coin: Coin name
            timestamp: UTC timestamp in ms
            signature: Signature
            network: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Deposit address info

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.sub_account_spot_assets_summary_for_master_account_2(
                email,
                coin,
                timestamp,
                signature,
                network=network,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def sub_account_transfer_history_for_sub_account(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        type_: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1SubAccountTransferSubUserHistoryResponse]:
        """- If ``type`` is not sent, the records of type 2: transfer out will be returned by default.
        - If ``startTime`` and ``endTime`` are not sent, the recent 30-day data will be returned.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            type_: * ``1`` - transfer in * ``2`` - transfer out
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Transfer id

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.sub_account_transfer_history_for_sub_account(
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

    async def sub_account_s_status_on_margin_futures_for_master_account(
        self,
        timestamp: int,
        signature: str,
        *,
        email: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1SubAccountStatusResponse]:
        """- If no ``email`` sent, all sub-accounts' information will be returned.

        Weight(IP): 10

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            email: Sub-account email
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Status on Margin/Futures

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.sub_account_s_status_on_margin_futures_for_master_account(
                timestamp, signature, email=email, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def summary_of_sub_account_s_futures_account_for_master_account(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountFuturesAccountSummaryResponse:
        """Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Futures account summary

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.summary_of_sub_account_s_futures_account_for_master_account(
                timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def summary_of_sub_account_s_futures_account_v2_for_master_account(
        self,
        futures_type: int,
        timestamp: int,
        signature: str,
        *,
        page: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV2SubAccountFuturesAccountSummaryResponse:
        """Weight(IP): 10

        Args:
            futures_type: * ``1`` - USDT Margined Futures * ``2`` - COIN Margined Futures
            timestamp: UTC timestamp in ms
            signature: Signature
            page: Default 1
            limit: Default 10, Max 20
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            USDT or COIN Margined Futures Summary

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.summary_of_sub_account_s_futures_account_v2_for_master_account(
                futures_type,
                timestamp,
                signature,
                page=page,
                limit=limit,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def summary_of_sub_account_s_margin_account_for_master_account(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountMarginAccountSummaryResponse:
        """Weight(IP): 10

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Margin sub-account details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.summary_of_sub_account_s_margin_account_for_master_account(
                timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def transfer_for_sub_account_for_master_account(
        self,
        email: str,
        asset: str,
        amount: float,
        type_: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountFuturesTransferResponse:
        """Weight(IP): 1

        Args:
            email: Sub-account email
            asset: Value sent with the request.
            amount: Value sent with the request.
            type_: * ``1`` - transfer from subaccount's spot account to its USDT-margined futures account * ``2`` -
                transfer from subaccount's USDT-margined futures account to its spot account * ``3`` - transfer from
                subaccount's spot account to its COIN-margined futures account * ``4`` - transfer from subaccount's
                COIN-margined futures account to its spot account
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Transfer id

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.transfer_for_sub_account_for_master_account(
                email,
                asset,
                amount,
                type_,
                timestamp,
                signature,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def transfer_to_master_for_sub_account(
        self,
        asset: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountTransferSubToMasterResponse:
        """Weight(IP): 1

        Args:
            asset: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Transfer id

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.transfer_to_master_for_sub_account(
                asset, amount, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def transfer_to_sub_account_of_same_master_for_sub_account(
        self,
        to_email: str,
        asset: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountTransferSubToSubResponse:
        """Weight(IP): 1

        Args:
            to_email: Recipient email
            asset: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Transfer id

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.transfer_to_sub_account_of_same_master_for_sub_account(
                to_email, asset, amount, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def universal_transfer_for_master_account(
        self,
        from_account_type: FromAccountTypeOrStr,
        to_account_type: ToAccountTypeOrStr,
        asset: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        from_email: str | None = None,
        to_email: str | None = None,
        client_tran_id: str | None = None,
        symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1SubAccountUniversalTransferResponse1:
        """- You need to enable "internal transfer" option for the api key which requests this endpoint.
        - Transfer from master account by default if fromEmail is not sent.
        - Transfer to master account by default if toEmail is not sent.
        - Supported transfer scenarios:
          - Master account SPOT transfer to sub-account SPOT,USDT_FUTURE,COIN_FUTURE,MARGIN(Cross),ISOLATED_MARGIN
          - Sub-account SPOT,USDT_FUTURE,COIN_FUTURE,MARGIN(Cross),ISOLATED_MARGIN transfer to master account SPOT
          - Transfer between two sub-account SPOT accounts

        Weight(IP): 1

        Args:
            from_account_type: Value sent with the request.
            to_account_type: Value sent with the request.
            asset: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            from_email: Sub-account email
            to_email: Sub-account email
            client_tran_id: Value sent with the request.
            symbol: Only supported under ISOLATED_MARGIN type
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Transfer id

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.universal_transfer_for_master_account(
                from_account_type,
                to_account_type,
                asset,
                amount,
                timestamp,
                signature,
                from_email=from_email,
                to_email=to_email,
                client_tran_id=client_tran_id,
                symbol=symbol,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def universal_transfer_history_for_master_account(
        self,
        timestamp: int,
        signature: str,
        *,
        from_email: str | None = None,
        to_email: str | None = None,
        client_tran_id: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1SubAccountUniversalTransferResponse]:
        """- ``fromEmail`` and ``toEmail`` cannot be sent at the same time.
        - Return ``fromEmail`` equal master account email by default.
        - The query time period must be less then 30 days.
        - If startTime and endTime not sent, return records of the last 30 days by default.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            from_email: Sub-account email
            to_email: Sub-account email
            client_tran_id: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            page: Default 1
            limit: Default 500, Max 500
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Transfer History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.universal_transfer_history_for_master_account(
                timestamp,
                signature,
                from_email=from_email,
                to_email=to_email,
                client_tran_id=client_tran_id,
                start_time=start_time,
                end_time=end_time,
                page=page,
                limit=limit,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def update_ip_restriction_for_sub_account_api_key_for_master_account(
        self,
        email: str,
        sub_account_api_key: str,
        status: str,
        timestamp: int,
        signature: str,
        *,
        third_party_name: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV2SubAccountSubAccountApiIpRestrictionResponse:
        """Update IP Restriction for Sub-Account API key

        Weight(UID): 3000

        Args:
            email: Sub-account email
            sub_account_api_key: Value sent with the request.
            status: IP Restriction status. 1 = IP Unrestricted. 2 = Restrict access to trusted IPs only. 3 = Restrict
                access to users' trusted third party IPs only
            timestamp: UTC timestamp in ms
            signature: Signature
            third_party_name: third party IP list name
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Update IP Restriction

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.update_ip_restriction_for_sub_account_api_key_for_master_account(
                email,
                sub_account_api_key,
                status,
                timestamp,
                signature,
                third_party_name=third_party_name,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def withdrawl_assets_from_the_managed_sub_account_for_investor_master_account(
        self,
        from_email: str,
        asset: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        transfer_date: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1ManagedSubaccountWithdrawResponse:
        """Weight(IP): 1

        Args:
            from_email: Sender email
            asset: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            transfer_date: Withdrawals is automatically occur on the transfer date(UTC0). If a date is not selected, the
                withdrawal occurs right now
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Transfer id

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.withdrawl_assets_from_the_managed_sub_account_for_investor_master_account(
                from_email,
                asset,
                amount,
                timestamp,
                signature,
                transfer_date=transfer_date,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSubAccountApiWithRawResponse:
        return self._with_raw_response


class SubAccountApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_a_virtual_sub_account_for_master_account(
        self,
        sub_account_string: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SubAccountVirtualSubAccountResponse, CreateAVirtualSubAccountForMasterAccountErrorBody]:
        """- This request will generate a virtual sub account under your master account.
        - You need to enable "trade" option for the api key which requests this endpoint.

        Weight(IP): 1

        Args:
            sub_account_string: Please input a string. We will create a virtual email using that string for you to
                register
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/sub-account/virtualSubAccount"),
            query_params=[
                param[str]("subAccountString", sub_account_string),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountVirtualSubAccountResponse],
            error_mapper=create_a_virtual_sub_account_for_master_account_error_mapper,
            request_options=request_options,
        )

    def delete_ip_list_for_a_sub_account_api_key_for_master_account(
        self,
        email: str,
        sub_account_api_key: str,
        timestamp: int,
        signature: str,
        *,
        ip_address: str | None = None,
        third_party_name: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1SubAccountSubAccountApiIpRestrictionIpListResponse,
        DeleteIpListForASubAccountApiKeyForMasterAccountErrorBody,
    ]:
        """Weight(UID): 3000

        Args:
            email: Sub-account email
            sub_account_api_key: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            ip_address: Can be added in batches, separated by commas
            third_party_name: third party IP list name
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/sapi/v1/sub-account/subAccountApi/ipRestriction/ipList"),
            query_params=[
                param[str]("email", email),
                param[str]("subAccountApiKey", sub_account_api_key),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("ipAddress", ip_address),
                param[str | None]("thirdPartyName", third_party_name),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountSubAccountApiIpRestrictionIpListResponse],
            error_mapper=delete_ip_list_for_a_sub_account_api_key_for_master_account_error_mapper,
            request_options=request_options,
        )

    def deposit_assets_into_the_managed_sub_account_for_investor_master_account(
        self,
        to_email: str,
        asset: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1ManagedSubaccountDepositResponse, DepositAssetsIntoTheManagedSubAccountForInvestorMasterAccountErrorBody
    ]:
        """Weight(IP): 1

        Args:
            to_email: Recipient email
            asset: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/managed-subaccount/deposit"),
            query_params=[
                param[str]("toEmail", to_email),
                param[str]("asset", asset),
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1ManagedSubaccountDepositResponse],
            error_mapper=deposit_assets_into_the_managed_sub_account_for_investor_master_account_error_mapper,
            request_options=request_options,
        )

    def detail_on_sub_account_s_futures_account_for_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SubAccountFuturesAccountResponse, DetailOnSubAccountSFuturesAccountForMasterAccountErrorBody]:
        """Weight(IP): 10

        Args:
            email: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/sub-account/futures/account"),
            query_params=[
                param[str]("email", email),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountFuturesAccountResponse],
            error_mapper=detail_on_sub_account_s_futures_account_for_master_account_error_mapper,
            request_options=request_options,
        )

    def detail_on_sub_account_s_futures_account_v2_for_master_account(
        self,
        email: str,
        futures_type: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV2SubAccountFuturesAccountResponse, DetailOnSubAccountSFuturesAccountV2ForMasterAccountErrorBody
    ]:
        """Weight(IP): 1

        Args:
            email: Sub-account email
            futures_type: * ``1`` - USDT Margined Futures * ``2`` - COIN Margined Futures
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v2/sub-account/futures/account"),
            query_params=[
                param[str]("email", email),
                param[int]("futuresType", futures_type),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV2SubAccountFuturesAccountResponse],
            error_mapper=detail_on_sub_account_s_futures_account_v2_for_master_account_error_mapper,
            request_options=request_options,
        )

    def detail_on_sub_account_s_margin_account_for_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SubAccountMarginAccountResponse, DetailOnSubAccountSMarginAccountForMasterAccountErrorBody]:
        """Weight(IP): 10

        Args:
            email: Sub-account email
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/sub-account/margin/account"),
            query_params=[
                param[str]("email", email),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountMarginAccountResponse],
            error_mapper=detail_on_sub_account_s_margin_account_for_master_account_error_mapper,
            request_options=request_options,
        )

    def enable_futures_for_sub_account_for_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SubAccountFuturesEnableResponse, EnableFuturesForSubAccountForMasterAccountErrorBody]:
        """Weight(IP): 1

        Args:
            email: Sub-account email
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/sub-account/futures/enable"),
            query_params=[
                param[str]("email", email),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountFuturesEnableResponse],
            error_mapper=enable_futures_for_sub_account_for_master_account_error_mapper,
            request_options=request_options,
        )

    def enable_leverage_token_for_sub_account_for_master_account(
        self,
        email: str,
        enable_blvt: bool,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SubAccountBlvtEnableResponse, EnableLeverageTokenForSubAccountForMasterAccountErrorBody]:
        """Weight(IP): 1

        Args:
            email: Sub-account email
            enable_blvt: Only true for now
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/sub-account/blvt/enable"),
            query_params=[
                param[str]("email", email),
                param[bool]("enableBlvt", enable_blvt),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountBlvtEnableResponse],
            error_mapper=enable_leverage_token_for_sub_account_for_master_account_error_mapper,
            request_options=request_options,
        )

    def enable_margin_for_sub_account_for_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SubAccountMarginEnableResponse, EnableMarginForSubAccountForMasterAccountErrorBody]:
        """Weight(IP): 1

        Args:
            email: Sub-account email
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/sub-account/margin/enable"),
            query_params=[
                param[str]("email", email),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountMarginEnableResponse],
            error_mapper=enable_margin_for_sub_account_for_master_account_error_mapper,
            request_options=request_options,
        )

    def enable_options_for_sub_account_for_master_account_user_data(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SubAccountEoptionsEnableResponse, EnableOptionsForSubAccountForMasterAccountUserDataErrorBody]:
        """Enable Options for Sub-account (For Master Account).

        Weight(IP): 1

        Args:
            email: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/sub-account/eoptions/enable"),
            query_params=[
                param[str]("email", email),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountEoptionsEnableResponse],
            error_mapper=enable_options_for_sub_account_for_master_account_user_data_error_mapper,
            request_options=request_options,
        )

    def futures_position_risk_of_sub_account_for_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        list[SapiV1SubAccountFuturesPositionRiskResponse], FuturesPositionRiskOfSubAccountForMasterAccountErrorBody
    ]:
        """Weight(IP): 10

        Args:
            email: Sub-account email
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/sub-account/futures/positionRisk"),
            query_params=[
                param[str]("email", email),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1SubAccountFuturesPositionRiskResponse]],
            error_mapper=futures_position_risk_of_sub_account_for_master_account_error_mapper,
            request_options=request_options,
        )

    def futures_position_risk_of_sub_account_v2_for_master_account(
        self,
        email: str,
        futures_type: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV2SubAccountFuturesPositionRiskResponse, FuturesPositionRiskOfSubAccountV2ForMasterAccountErrorBody
    ]:
        """Weight(IP): 1

        Args:
            email: Sub-account email
            futures_type: * ``1`` - USDT Margined Futures * ``2`` - COIN Margined Futures
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v2/sub-account/futures/positionRisk"),
            query_params=[
                param[str]("email", email),
                param[int]("futuresType", futures_type),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV2SubAccountFuturesPositionRiskResponse],
            error_mapper=futures_position_risk_of_sub_account_v2_for_master_account_error_mapper,
            request_options=request_options,
        )

    def get_ip_restriction_for_a_sub_account_api_key_for_master_account(
        self,
        email: str,
        sub_account_api_key: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1SubAccountSubAccountApiIpRestrictionResponse,
        GetIpRestrictionForASubAccountApiKeyForMasterAccountErrorBody,
    ]:
        """Weight(UID): 3000

        Args:
            email: Sub-account email
            sub_account_api_key: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/sub-account/subAccountApi/ipRestriction"),
            query_params=[
                param[str]("email", email),
                param[str]("subAccountApiKey", sub_account_api_key),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountSubAccountApiIpRestrictionResponse],
            error_mapper=get_ip_restriction_for_a_sub_account_api_key_for_master_account_error_mapper,
            request_options=request_options,
        )

    def get_managed_sub_account_deposit_address_for_investor_master_account(
        self,
        email: str,
        coin: str,
        timestamp: int,
        signature: str,
        *,
        network: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1ManagedSubaccountDepositAddressResponse,
        GetManagedSubAccountDepositAddressForInvestorMasterAccountErrorBody,
    ]:
        """Get investor's managed sub-account deposit address

        Weight(UID): 1

        Args:
            email: Value sent with the request.
            coin: Coin name
            timestamp: UTC timestamp in ms
            signature: Signature
            network: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/managed-subaccount/deposit/address"),
            query_params=[
                param[str]("email", email),
                param[str]("coin", coin),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("network", network),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1ManagedSubaccountDepositAddressResponse],
            error_mapper=get_managed_sub_account_deposit_address_for_investor_master_account_error_mapper,
            request_options=request_options,
        )

    def managed_sub_account_asset_details_for_investor_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        list[SapiV1ManagedSubaccountAssetResponse], ManagedSubAccountAssetDetailsForInvestorMasterAccountErrorBody
    ]:
        """Weight(IP): 1

        Args:
            email: Sub-account email
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/managed-subaccount/asset"),
            query_params=[
                param[str]("email", email),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1ManagedSubaccountAssetResponse]],
            error_mapper=managed_sub_account_asset_details_for_investor_master_account_error_mapper,
            request_options=request_options,
        )

    def managed_sub_account_snapshot_for_investor_master_account(
        self,
        email: str,
        type_: str,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1ManagedSubaccountAccountSnapshotResponse, ManagedSubAccountSnapshotForInvestorMasterAccountErrorBody
    ]:
        """- The query time period must be less then 30 days
        - Support query within the last one month only
        - If ``startTime`` and ``endTime`` not sent, return records of the last 7 days by default

        Weight(IP): 2400

        Args:
            email: Sub-account email
            type_: "SPOT", "MARGIN"(cross), "FUTURES"(UM)
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: min 7, max 30, default 7
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/managed-subaccount/accountSnapshot"),
            query_params=[
                param[str]("email", email),
                param[str]("type", type_),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            decoder=json_decoder[SapiV1ManagedSubaccountAccountSnapshotResponse],
            error_mapper=managed_sub_account_snapshot_for_investor_master_account_error_mapper,
            request_options=request_options,
        )

    def margin_transfer_for_sub_account_for_master_account(
        self,
        email: str,
        asset: str,
        amount: float,
        type_: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SubAccountMarginTransferResponse, MarginTransferForSubAccountForMasterAccountErrorBody]:
        """Weight(IP): 1

        Args:
            email: Sub-account email
            asset: Value sent with the request.
            amount: Value sent with the request.
            type_: * ``1`` - transfer from subaccount's spot account to margin account * ``2`` - transfer from
                subaccount's margin account to its spot account
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/sub-account/margin/transfer"),
            query_params=[
                param[str]("email", email),
                param[str]("asset", asset),
                param[float]("amount", amount),
                param[int]("type", type_),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountMarginTransferResponse],
            error_mapper=margin_transfer_for_sub_account_for_master_account_error_mapper,
            request_options=request_options,
        )

    def query_managed_sub_account_transfer_log_for_investor_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        transfers: str | None = None,
        transfer_function_account_type: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1ManagedSubaccountQueryTransLogForInvestorResponse,
        QueryManagedSubAccountTransferLogForInvestorMasterAccountErrorBody,
    ]:
        """Investor can use this api to query managed sub account transfer log. This endpoint is available for investor
        of Managed Sub-Account. A Managed Sub-Account is an account type for investors who value flexibility in asset
        allocation and account application, while delegating trades to a professional trading team.

        Weight(IP): 1

        Args:
            email: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            page: Default 1
            limit: Default 500; max 1000.
            transfers: Transfer Direction (FROM/TO)
            transfer_function_account_type: Transfer function account type
                (SPOT/MARGIN/ISOLATED_MARGIN/USDT_FUTURE/COIN_FUTURE)
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/managed-subaccount/queryTransLogForInvestor"),
            query_params=[
                param[str]("email", email),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("page", page),
                param[int | None]("limit", limit),
                param[str | None]("transfers", transfers),
                param[str | None]("transferFunctionAccountType", transfer_function_account_type),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1ManagedSubaccountQueryTransLogForInvestorResponse],
            error_mapper=query_managed_sub_account_transfer_log_for_investor_master_account_error_mapper,
            request_options=request_options,
        )

    def query_managed_sub_account_transfer_log_for_trading_team_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        transfers: str | None = None,
        transfer_function_account_type: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1ManagedSubaccountQueryTransLogForTradeParentResponse,
        QueryManagedSubAccountTransferLogForTradingTeamMasterAccountErrorBody,
    ]:
        """Trading team can use this api to query managed sub account transfer log. This endpoint is available for
        trading team of Managed Sub-Account. A Managed Sub-Account is an account type for investors who value
        flexibility in asset allocation and account application, while delegating trades to a professional trading team

        Weight(IP): 60

        Args:
            email: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            page: Default 1
            limit: Default 500; max 1000.
            transfers: Transfer Direction (FROM/TO)
            transfer_function_account_type: Transfer function account type
                (SPOT/MARGIN/ISOLATED_MARGIN/USDT_FUTURE/COIN_FUTURE)
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/managed-subaccount/queryTransLogForTradeParent"),
            query_params=[
                param[str]("email", email),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("page", page),
                param[int | None]("limit", limit),
                param[str | None]("transfers", transfers),
                param[str | None]("transferFunctionAccountType", transfer_function_account_type),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1ManagedSubaccountQueryTransLogForTradeParentResponse],
            error_mapper=query_managed_sub_account_transfer_log_for_trading_team_master_account_error_mapper,
            request_options=request_options,
        )

    def query_managed_sub_account_transfer_log_for_trading_team_sub_account_user_data(
        self,
        transfers: TransfersOrStr,
        transfer_function_account_type: TransferFunctionAccountTypeOrStr,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1ManagedSubaccountQueryTransLogResponse,
        QueryManagedSubAccountTransferLogForTradingTeamSubAccountUserDataErrorBody,
    ]:
        """Query Managed Sub Account Transfer Log (For Trading Team Sub Account)

        Weight(UID): 60

        Args:
            transfers: Transfer Direction
            transfer_function_account_type: Transfer function account type
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            page: Default 1
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/managed-subaccount/query-trans-log"),
            query_params=[
                param[TransfersOrStr]("transfers", transfers),
                param[TransferFunctionAccountTypeOrStr]("transferFunctionAccountType", transfer_function_account_type),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("page", page),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1ManagedSubaccountQueryTransLogResponse],
            error_mapper=query_managed_sub_account_transfer_log_for_trading_team_sub_account_user_data_error_mapper,
            request_options=request_options,
        )

    def query_managed_sub_account_futures_asset_details_for_investor_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1ManagedSubaccountFetchFutureAssetResponse,
        QueryManagedSubAccountFuturesAssetDetailsForInvestorMasterAccountErrorBody,
    ]:
        """Investor can use this api to query managed sub account futures asset details

        Args:
            email: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/managed-subaccount/fetch-future-asset"),
            query_params=[
                param[str]("email", email),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1ManagedSubaccountFetchFutureAssetResponse],
            error_mapper=query_managed_sub_account_futures_asset_details_for_investor_master_account_error_mapper,
            request_options=request_options,
        )

    def query_managed_sub_account_list_for_investor(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        page: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1ManagedSubaccountInfoResponse, QueryManagedSubAccountListForInvestorErrorBody]:
        """Get investor's managed sub-account list.

        Weight(UID): 60

        Args:
            email: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            page: Default 1
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/managed-subaccount/info"),
            query_params=[
                param[str]("email", email),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("page", page),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1ManagedSubaccountInfoResponse],
            error_mapper=query_managed_sub_account_list_for_investor_error_mapper,
            request_options=request_options,
        )

    def query_managed_sub_account_margin_asset_details_for_investor_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1ManagedSubaccountMarginAssetResponse,
        QueryManagedSubAccountMarginAssetDetailsForInvestorMasterAccountErrorBody,
    ]:
        """Investor can use this api to query managed sub account margin asset details

        Args:
            email: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/managed-subaccount/marginAsset"),
            query_params=[
                param[str]("email", email),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1ManagedSubaccountMarginAssetResponse],
            error_mapper=query_managed_sub_account_margin_asset_details_for_investor_master_account_error_mapper,
            request_options=request_options,
        )

    def query_sub_account_assets_for_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV4SubAccountAssetsResponse, QuerySubAccountAssetsForMasterAccountErrorBody]:
        """Fetch sub-account assets

        Weight(UID): 60

        Args:
            email: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v4/sub-account/assets"),
            query_params=[
                param[str]("email", email),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV4SubAccountAssetsResponse],
            error_mapper=query_sub_account_assets_for_master_account_error_mapper,
            request_options=request_options,
        )

    def query_sub_account_list_for_master_account(
        self,
        timestamp: int,
        signature: str,
        *,
        email: str | None = None,
        is_freeze: IsFreezeOrStr | None = None,
        page: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SubAccountListResponse, QuerySubAccountListForMasterAccountErrorBody]:
        """Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            email: Sub-account email
            is_freeze: Value sent with the request.
            page: Default 1
            limit: Default 1; max 200
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/sub-account/list"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("email", email),
                param[IsFreezeOrStr | None]("isFreeze", is_freeze),
                param[int | None]("page", page),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountListResponse],
            error_mapper=query_sub_account_list_for_master_account_error_mapper,
            request_options=request_options,
        )

    def query_sub_account_transaction_statistics_for_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1SubAccountTransactionStatisticsResponse, QuerySubAccountTransactionStatisticsForMasterAccountErrorBody
    ]:
        """Query Sub-account Transaction statistics (For Master Account).

        Weight(UID): 60

        Args:
            email: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/sub-account/transaction-statistics"),
            query_params=[
                param[str]("email", email),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountTransactionStatisticsResponse],
            error_mapper=query_sub_account_transaction_statistics_for_master_account_error_mapper,
            request_options=request_options,
        )

    def sub_account_assets_for_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV3SubAccountAssetsResponse, SubAccountAssetsForMasterAccountErrorBody]:
        """Fetch sub-account assets

        Weight(IP): 1

        Args:
            email: Sub-account email
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v3/sub-account/assets"),
            query_params=[
                param[str]("email", email),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV3SubAccountAssetsResponse],
            error_mapper=sub_account_assets_for_master_account_error_mapper,
            request_options=request_options,
        )

    def sub_account_deposit_history_for_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        coin: str | None = None,
        status: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        offset: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1CapitalDepositSubHisrecResponse], SubAccountDepositHistoryForMasterAccountErrorBody]:
        """Fetch sub-account deposit history

        Weight(IP): 1

        Args:
            email: Sub-account email
            timestamp: UTC timestamp in ms
            signature: Signature
            coin: Coin name
            status: 0(0:pending,6: credited but cannot withdraw, 1:success)
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Value sent with the request.
            offset: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/capital/deposit/subHisrec"),
            query_params=[
                param[str]("email", email),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("coin", coin),
                param[int | None]("status", status),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1CapitalDepositSubHisrecResponse]],
            error_mapper=sub_account_deposit_history_for_master_account_error_mapper,
            request_options=request_options,
        )

    def sub_account_futures_asset_transfer_for_master_account(
        self,
        from_email: str,
        to_email: str,
        futures_type: int,
        asset: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1SubAccountFuturesInternalTransferResponse1, SubAccountFuturesAssetTransferForMasterAccountErrorBody
    ]:
        """- Master account can transfer max 2000 times a minute

        Weight(IP): 1

        Args:
            from_email: Sender email
            to_email: Recipient email
            futures_type: 1:USDT-margined Futures,2: Coin-margined Futures
            asset: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/sub-account/futures/internalTransfer"),
            query_params=[
                param[str]("fromEmail", from_email),
                param[str]("toEmail", to_email),
                param[int]("futuresType", futures_type),
                param[str]("asset", asset),
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountFuturesInternalTransferResponse1],
            error_mapper=sub_account_futures_asset_transfer_for_master_account_error_mapper,
            request_options=request_options,
        )

    def sub_account_futures_asset_transfer_history_for_master_account(
        self,
        email: str,
        futures_type: int,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1SubAccountFuturesInternalTransferResponse, SubAccountFuturesAssetTransferHistoryForMasterAccountErrorBody
    ]:
        """Weight(IP): 1

        Args:
            email: Sub-account email
            futures_type: 1:USDT-margined Futures, 2: Coin-margined Futures
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            page: Default 1
            limit: Default value: 50, Max value: 500
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/sub-account/futures/internalTransfer"),
            query_params=[
                param[str]("email", email),
                param[int]("futuresType", futures_type),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("page", page),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountFuturesInternalTransferResponse],
            error_mapper=sub_account_futures_asset_transfer_history_for_master_account_error_mapper,
            request_options=request_options,
        )

    def sub_account_spot_asset_transfer_history_for_master_account(
        self,
        timestamp: int,
        signature: str,
        *,
        from_email: str | None = None,
        to_email: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        list[SapiV1SubAccountSubTransferHistoryResponse], SubAccountSpotAssetTransferHistoryForMasterAccountErrorBody
    ]:
        """- fromEmail and toEmail cannot be sent at the same time.
        - Return fromEmail equal master account email by default.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            from_email: Sub-account email
            to_email: Sub-account email
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            page: Default 1
            limit: Default 1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/sub-account/sub/transfer/history"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("fromEmail", from_email),
                param[str | None]("toEmail", to_email),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("page", page),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1SubAccountSubTransferHistoryResponse]],
            error_mapper=sub_account_spot_asset_transfer_history_for_master_account_error_mapper,
            request_options=request_options,
        )

    def sub_account_spot_assets_summary_for_master_account(
        self,
        timestamp: int,
        signature: str,
        *,
        email: str | None = None,
        page: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SubAccountSpotSummaryResponse, SubAccountSpotAssetsSummaryForMasterAccountErrorBody]:
        """Get BTC valued asset summary of subaccounts.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            email: Sub-account email
            page: Default 1
            size: Default:10 Max:20
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/sub-account/spotSummary"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("email", email),
                param[int | None]("page", page),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountSpotSummaryResponse],
            error_mapper=sub_account_spot_assets_summary_for_master_account_error_mapper,
            request_options=request_options,
        )

    def sub_account_spot_assets_summary_for_master_account_2(
        self,
        email: str,
        coin: str,
        timestamp: int,
        signature: str,
        *,
        network: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1CapitalDepositSubAddressResponse, SubAccountSpotAssetsSummaryForMasterAccount2ErrorBody]:
        """Fetch sub-account deposit address

        Weight(IP): 1

        Args:
            email: Sub-account email
            coin: Coin name
            timestamp: UTC timestamp in ms
            signature: Signature
            network: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/capital/deposit/subAddress"),
            query_params=[
                param[str]("email", email),
                param[str]("coin", coin),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("network", network),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1CapitalDepositSubAddressResponse],
            error_mapper=sub_account_spot_assets_summary_for_master_account2_error_mapper,
            request_options=request_options,
        )

    def sub_account_transfer_history_for_sub_account(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        type_: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        list[SapiV1SubAccountTransferSubUserHistoryResponse], SubAccountTransferHistoryForSubAccountErrorBody
    ]:
        """- If ``type`` is not sent, the records of type 2: transfer out will be returned by default.
        - If ``startTime`` and ``endTime`` are not sent, the recent 30-day data will be returned.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            type_: * ``1`` - transfer in * ``2`` - transfer out
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/sub-account/transfer/subUserHistory"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("asset", asset),
                param[int | None]("type", type_),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1SubAccountTransferSubUserHistoryResponse]],
            error_mapper=sub_account_transfer_history_for_sub_account_error_mapper,
            request_options=request_options,
        )

    def sub_account_s_status_on_margin_futures_for_master_account(
        self,
        timestamp: int,
        signature: str,
        *,
        email: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1SubAccountStatusResponse], SubAccountSStatusOnMarginFuturesForMasterAccountErrorBody]:
        """- If no ``email`` sent, all sub-accounts' information will be returned.

        Weight(IP): 10

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            email: Sub-account email
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/sub-account/status"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("email", email),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1SubAccountStatusResponse]],
            error_mapper=sub_account_s_status_on_margin_futures_for_master_account_error_mapper,
            request_options=request_options,
        )

    def summary_of_sub_account_s_futures_account_for_master_account(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1SubAccountFuturesAccountSummaryResponse, SummaryOfSubAccountSFuturesAccountForMasterAccountErrorBody
    ]:
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
            url_template=self._server.default("/sapi/v1/sub-account/futures/accountSummary"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountFuturesAccountSummaryResponse],
            error_mapper=summary_of_sub_account_s_futures_account_for_master_account_error_mapper,
            request_options=request_options,
        )

    def summary_of_sub_account_s_futures_account_v2_for_master_account(
        self,
        futures_type: int,
        timestamp: int,
        signature: str,
        *,
        page: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV2SubAccountFuturesAccountSummaryResponse, SummaryOfSubAccountSFuturesAccountV2ForMasterAccountErrorBody
    ]:
        """Weight(IP): 10

        Args:
            futures_type: * ``1`` - USDT Margined Futures * ``2`` - COIN Margined Futures
            timestamp: UTC timestamp in ms
            signature: Signature
            page: Default 1
            limit: Default 10, Max 20
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v2/sub-account/futures/accountSummary"),
            query_params=[
                param[int]("futuresType", futures_type),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("page", page),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV2SubAccountFuturesAccountSummaryResponse],
            error_mapper=summary_of_sub_account_s_futures_account_v2_for_master_account_error_mapper,
            request_options=request_options,
        )

    def summary_of_sub_account_s_margin_account_for_master_account(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1SubAccountMarginAccountSummaryResponse, SummaryOfSubAccountSMarginAccountForMasterAccountErrorBody
    ]:
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
            url_template=self._server.default("/sapi/v1/sub-account/margin/accountSummary"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountMarginAccountSummaryResponse],
            error_mapper=summary_of_sub_account_s_margin_account_for_master_account_error_mapper,
            request_options=request_options,
        )

    def transfer_for_sub_account_for_master_account(
        self,
        email: str,
        asset: str,
        amount: float,
        type_: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SubAccountFuturesTransferResponse, TransferForSubAccountForMasterAccountErrorBody]:
        """Weight(IP): 1

        Args:
            email: Sub-account email
            asset: Value sent with the request.
            amount: Value sent with the request.
            type_: * ``1`` - transfer from subaccount's spot account to its USDT-margined futures account * ``2`` -
                transfer from subaccount's USDT-margined futures account to its spot account * ``3`` - transfer from
                subaccount's spot account to its COIN-margined futures account * ``4`` - transfer from subaccount's
                COIN-margined futures account to its spot account
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/sub-account/futures/transfer"),
            query_params=[
                param[str]("email", email),
                param[str]("asset", asset),
                param[float]("amount", amount),
                param[int]("type", type_),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountFuturesTransferResponse],
            error_mapper=transfer_for_sub_account_for_master_account_error_mapper,
            request_options=request_options,
        )

    def transfer_to_master_for_sub_account(
        self,
        asset: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SubAccountTransferSubToMasterResponse, TransferToMasterForSubAccountErrorBody]:
        """Weight(IP): 1

        Args:
            asset: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/sub-account/transfer/subToMaster"),
            query_params=[
                param[str]("asset", asset),
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountTransferSubToMasterResponse],
            error_mapper=transfer_to_master_for_sub_account_error_mapper,
            request_options=request_options,
        )

    def transfer_to_sub_account_of_same_master_for_sub_account(
        self,
        to_email: str,
        asset: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SubAccountTransferSubToSubResponse, TransferToSubAccountOfSameMasterForSubAccountErrorBody]:
        """Weight(IP): 1

        Args:
            to_email: Recipient email
            asset: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/sub-account/transfer/subToSub"),
            query_params=[
                param[str]("toEmail", to_email),
                param[str]("asset", asset),
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountTransferSubToSubResponse],
            error_mapper=transfer_to_sub_account_of_same_master_for_sub_account_error_mapper,
            request_options=request_options,
        )

    def universal_transfer_for_master_account(
        self,
        from_account_type: FromAccountTypeOrStr,
        to_account_type: ToAccountTypeOrStr,
        asset: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        from_email: str | None = None,
        to_email: str | None = None,
        client_tran_id: str | None = None,
        symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SubAccountUniversalTransferResponse1, UniversalTransferForMasterAccountErrorBody]:
        """- You need to enable "internal transfer" option for the api key which requests this endpoint.
        - Transfer from master account by default if fromEmail is not sent.
        - Transfer to master account by default if toEmail is not sent.
        - Supported transfer scenarios:
          - Master account SPOT transfer to sub-account SPOT,USDT_FUTURE,COIN_FUTURE,MARGIN(Cross),ISOLATED_MARGIN
          - Sub-account SPOT,USDT_FUTURE,COIN_FUTURE,MARGIN(Cross),ISOLATED_MARGIN transfer to master account SPOT
          - Transfer between two sub-account SPOT accounts

        Weight(IP): 1

        Args:
            from_account_type: Value sent with the request.
            to_account_type: Value sent with the request.
            asset: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            from_email: Sub-account email
            to_email: Sub-account email
            client_tran_id: Value sent with the request.
            symbol: Only supported under ISOLATED_MARGIN type
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/sub-account/universalTransfer"),
            query_params=[
                param[FromAccountTypeOrStr]("fromAccountType", from_account_type),
                param[ToAccountTypeOrStr]("toAccountType", to_account_type),
                param[str]("asset", asset),
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("fromEmail", from_email),
                param[str | None]("toEmail", to_email),
                param[str | None]("clientTranId", client_tran_id),
                param[str | None]("symbol", symbol),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountUniversalTransferResponse1],
            error_mapper=universal_transfer_for_master_account_error_mapper,
            request_options=request_options,
        )

    def universal_transfer_history_for_master_account(
        self,
        timestamp: int,
        signature: str,
        *,
        from_email: str | None = None,
        to_email: str | None = None,
        client_tran_id: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1SubAccountUniversalTransferResponse], UniversalTransferHistoryForMasterAccountErrorBody]:
        """- ``fromEmail`` and ``toEmail`` cannot be sent at the same time.
        - Return ``fromEmail`` equal master account email by default.
        - The query time period must be less then 30 days.
        - If startTime and endTime not sent, return records of the last 30 days by default.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            from_email: Sub-account email
            to_email: Sub-account email
            client_tran_id: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            page: Default 1
            limit: Default 500, Max 500
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/sub-account/universalTransfer"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("fromEmail", from_email),
                param[str | None]("toEmail", to_email),
                param[str | None]("clientTranId", client_tran_id),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("page", page),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1SubAccountUniversalTransferResponse]],
            error_mapper=universal_transfer_history_for_master_account_error_mapper,
            request_options=request_options,
        )

    def update_ip_restriction_for_sub_account_api_key_for_master_account(
        self,
        email: str,
        sub_account_api_key: str,
        status: str,
        timestamp: int,
        signature: str,
        *,
        third_party_name: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV2SubAccountSubAccountApiIpRestrictionResponse,
        UpdateIpRestrictionForSubAccountApiKeyForMasterAccountErrorBody,
    ]:
        """Update IP Restriction for Sub-Account API key

        Weight(UID): 3000

        Args:
            email: Sub-account email
            sub_account_api_key: Value sent with the request.
            status: IP Restriction status. 1 = IP Unrestricted. 2 = Restrict access to trusted IPs only. 3 = Restrict
                access to users' trusted third party IPs only
            timestamp: UTC timestamp in ms
            signature: Signature
            third_party_name: third party IP list name
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v2/sub-account/subAccountApi/ipRestriction"),
            query_params=[
                param[str]("email", email),
                param[str]("subAccountApiKey", sub_account_api_key),
                param[str]("status", status),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("thirdPartyName", third_party_name),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV2SubAccountSubAccountApiIpRestrictionResponse],
            error_mapper=update_ip_restriction_for_sub_account_api_key_for_master_account_error_mapper,
            request_options=request_options,
        )

    def withdrawl_assets_from_the_managed_sub_account_for_investor_master_account(
        self,
        from_email: str,
        asset: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        transfer_date: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1ManagedSubaccountWithdrawResponse,
        WithdrawlAssetsFromTheManagedSubAccountForInvestorMasterAccountErrorBody,
    ]:
        """Weight(IP): 1

        Args:
            from_email: Sender email
            asset: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            transfer_date: Withdrawals is automatically occur on the transfer date(UTC0). If a date is not selected, the
                withdrawal occurs right now
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/managed-subaccount/withdraw"),
            query_params=[
                param[str]("fromEmail", from_email),
                param[str]("asset", asset),
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("transferDate", transfer_date),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1ManagedSubaccountWithdrawResponse],
            error_mapper=withdrawl_assets_from_the_managed_sub_account_for_investor_master_account_error_mapper,
            request_options=request_options,
        )


class AsyncSubAccountApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_a_virtual_sub_account_for_master_account(
        self,
        sub_account_string: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SubAccountVirtualSubAccountResponse, CreateAVirtualSubAccountForMasterAccountErrorBody]:
        """- This request will generate a virtual sub account under your master account.
        - You need to enable "trade" option for the api key which requests this endpoint.

        Weight(IP): 1

        Args:
            sub_account_string: Please input a string. We will create a virtual email using that string for you to
                register
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/sub-account/virtualSubAccount"),
            query_params=[
                param[str]("subAccountString", sub_account_string),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountVirtualSubAccountResponse],
            error_mapper=create_a_virtual_sub_account_for_master_account_error_mapper,
            request_options=request_options,
        )

    async def delete_ip_list_for_a_sub_account_api_key_for_master_account(
        self,
        email: str,
        sub_account_api_key: str,
        timestamp: int,
        signature: str,
        *,
        ip_address: str | None = None,
        third_party_name: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1SubAccountSubAccountApiIpRestrictionIpListResponse,
        DeleteIpListForASubAccountApiKeyForMasterAccountErrorBody,
    ]:
        """Weight(UID): 3000

        Args:
            email: Sub-account email
            sub_account_api_key: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            ip_address: Can be added in batches, separated by commas
            third_party_name: third party IP list name
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/sapi/v1/sub-account/subAccountApi/ipRestriction/ipList"),
            query_params=[
                param[str]("email", email),
                param[str]("subAccountApiKey", sub_account_api_key),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("ipAddress", ip_address),
                param[str | None]("thirdPartyName", third_party_name),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountSubAccountApiIpRestrictionIpListResponse],
            error_mapper=delete_ip_list_for_a_sub_account_api_key_for_master_account_error_mapper,
            request_options=request_options,
        )

    async def deposit_assets_into_the_managed_sub_account_for_investor_master_account(
        self,
        to_email: str,
        asset: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1ManagedSubaccountDepositResponse, DepositAssetsIntoTheManagedSubAccountForInvestorMasterAccountErrorBody
    ]:
        """Weight(IP): 1

        Args:
            to_email: Recipient email
            asset: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/managed-subaccount/deposit"),
            query_params=[
                param[str]("toEmail", to_email),
                param[str]("asset", asset),
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1ManagedSubaccountDepositResponse],
            error_mapper=deposit_assets_into_the_managed_sub_account_for_investor_master_account_error_mapper,
            request_options=request_options,
        )

    async def detail_on_sub_account_s_futures_account_for_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SubAccountFuturesAccountResponse, DetailOnSubAccountSFuturesAccountForMasterAccountErrorBody]:
        """Weight(IP): 10

        Args:
            email: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/sub-account/futures/account"),
            query_params=[
                param[str]("email", email),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountFuturesAccountResponse],
            error_mapper=detail_on_sub_account_s_futures_account_for_master_account_error_mapper,
            request_options=request_options,
        )

    async def detail_on_sub_account_s_futures_account_v2_for_master_account(
        self,
        email: str,
        futures_type: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV2SubAccountFuturesAccountResponse, DetailOnSubAccountSFuturesAccountV2ForMasterAccountErrorBody
    ]:
        """Weight(IP): 1

        Args:
            email: Sub-account email
            futures_type: * ``1`` - USDT Margined Futures * ``2`` - COIN Margined Futures
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v2/sub-account/futures/account"),
            query_params=[
                param[str]("email", email),
                param[int]("futuresType", futures_type),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV2SubAccountFuturesAccountResponse],
            error_mapper=detail_on_sub_account_s_futures_account_v2_for_master_account_error_mapper,
            request_options=request_options,
        )

    async def detail_on_sub_account_s_margin_account_for_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SubAccountMarginAccountResponse, DetailOnSubAccountSMarginAccountForMasterAccountErrorBody]:
        """Weight(IP): 10

        Args:
            email: Sub-account email
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/sub-account/margin/account"),
            query_params=[
                param[str]("email", email),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountMarginAccountResponse],
            error_mapper=detail_on_sub_account_s_margin_account_for_master_account_error_mapper,
            request_options=request_options,
        )

    async def enable_futures_for_sub_account_for_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SubAccountFuturesEnableResponse, EnableFuturesForSubAccountForMasterAccountErrorBody]:
        """Weight(IP): 1

        Args:
            email: Sub-account email
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/sub-account/futures/enable"),
            query_params=[
                param[str]("email", email),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountFuturesEnableResponse],
            error_mapper=enable_futures_for_sub_account_for_master_account_error_mapper,
            request_options=request_options,
        )

    async def enable_leverage_token_for_sub_account_for_master_account(
        self,
        email: str,
        enable_blvt: bool,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SubAccountBlvtEnableResponse, EnableLeverageTokenForSubAccountForMasterAccountErrorBody]:
        """Weight(IP): 1

        Args:
            email: Sub-account email
            enable_blvt: Only true for now
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/sub-account/blvt/enable"),
            query_params=[
                param[str]("email", email),
                param[bool]("enableBlvt", enable_blvt),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountBlvtEnableResponse],
            error_mapper=enable_leverage_token_for_sub_account_for_master_account_error_mapper,
            request_options=request_options,
        )

    async def enable_margin_for_sub_account_for_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SubAccountMarginEnableResponse, EnableMarginForSubAccountForMasterAccountErrorBody]:
        """Weight(IP): 1

        Args:
            email: Sub-account email
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/sub-account/margin/enable"),
            query_params=[
                param[str]("email", email),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountMarginEnableResponse],
            error_mapper=enable_margin_for_sub_account_for_master_account_error_mapper,
            request_options=request_options,
        )

    async def enable_options_for_sub_account_for_master_account_user_data(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SubAccountEoptionsEnableResponse, EnableOptionsForSubAccountForMasterAccountUserDataErrorBody]:
        """Enable Options for Sub-account (For Master Account).

        Weight(IP): 1

        Args:
            email: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/sub-account/eoptions/enable"),
            query_params=[
                param[str]("email", email),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountEoptionsEnableResponse],
            error_mapper=enable_options_for_sub_account_for_master_account_user_data_error_mapper,
            request_options=request_options,
        )

    async def futures_position_risk_of_sub_account_for_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        list[SapiV1SubAccountFuturesPositionRiskResponse], FuturesPositionRiskOfSubAccountForMasterAccountErrorBody
    ]:
        """Weight(IP): 10

        Args:
            email: Sub-account email
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/sub-account/futures/positionRisk"),
            query_params=[
                param[str]("email", email),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1SubAccountFuturesPositionRiskResponse]],
            error_mapper=futures_position_risk_of_sub_account_for_master_account_error_mapper,
            request_options=request_options,
        )

    async def futures_position_risk_of_sub_account_v2_for_master_account(
        self,
        email: str,
        futures_type: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV2SubAccountFuturesPositionRiskResponse, FuturesPositionRiskOfSubAccountV2ForMasterAccountErrorBody
    ]:
        """Weight(IP): 1

        Args:
            email: Sub-account email
            futures_type: * ``1`` - USDT Margined Futures * ``2`` - COIN Margined Futures
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v2/sub-account/futures/positionRisk"),
            query_params=[
                param[str]("email", email),
                param[int]("futuresType", futures_type),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV2SubAccountFuturesPositionRiskResponse],
            error_mapper=futures_position_risk_of_sub_account_v2_for_master_account_error_mapper,
            request_options=request_options,
        )

    async def get_ip_restriction_for_a_sub_account_api_key_for_master_account(
        self,
        email: str,
        sub_account_api_key: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1SubAccountSubAccountApiIpRestrictionResponse,
        GetIpRestrictionForASubAccountApiKeyForMasterAccountErrorBody,
    ]:
        """Weight(UID): 3000

        Args:
            email: Sub-account email
            sub_account_api_key: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/sub-account/subAccountApi/ipRestriction"),
            query_params=[
                param[str]("email", email),
                param[str]("subAccountApiKey", sub_account_api_key),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountSubAccountApiIpRestrictionResponse],
            error_mapper=get_ip_restriction_for_a_sub_account_api_key_for_master_account_error_mapper,
            request_options=request_options,
        )

    async def get_managed_sub_account_deposit_address_for_investor_master_account(
        self,
        email: str,
        coin: str,
        timestamp: int,
        signature: str,
        *,
        network: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1ManagedSubaccountDepositAddressResponse,
        GetManagedSubAccountDepositAddressForInvestorMasterAccountErrorBody,
    ]:
        """Get investor's managed sub-account deposit address

        Weight(UID): 1

        Args:
            email: Value sent with the request.
            coin: Coin name
            timestamp: UTC timestamp in ms
            signature: Signature
            network: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/managed-subaccount/deposit/address"),
            query_params=[
                param[str]("email", email),
                param[str]("coin", coin),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("network", network),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1ManagedSubaccountDepositAddressResponse],
            error_mapper=get_managed_sub_account_deposit_address_for_investor_master_account_error_mapper,
            request_options=request_options,
        )

    async def managed_sub_account_asset_details_for_investor_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        list[SapiV1ManagedSubaccountAssetResponse], ManagedSubAccountAssetDetailsForInvestorMasterAccountErrorBody
    ]:
        """Weight(IP): 1

        Args:
            email: Sub-account email
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/managed-subaccount/asset"),
            query_params=[
                param[str]("email", email),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1ManagedSubaccountAssetResponse]],
            error_mapper=managed_sub_account_asset_details_for_investor_master_account_error_mapper,
            request_options=request_options,
        )

    async def managed_sub_account_snapshot_for_investor_master_account(
        self,
        email: str,
        type_: str,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1ManagedSubaccountAccountSnapshotResponse, ManagedSubAccountSnapshotForInvestorMasterAccountErrorBody
    ]:
        """- The query time period must be less then 30 days
        - Support query within the last one month only
        - If ``startTime`` and ``endTime`` not sent, return records of the last 7 days by default

        Weight(IP): 2400

        Args:
            email: Sub-account email
            type_: "SPOT", "MARGIN"(cross), "FUTURES"(UM)
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: min 7, max 30, default 7
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/managed-subaccount/accountSnapshot"),
            query_params=[
                param[str]("email", email),
                param[str]("type", type_),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            decoder=json_decoder[SapiV1ManagedSubaccountAccountSnapshotResponse],
            error_mapper=managed_sub_account_snapshot_for_investor_master_account_error_mapper,
            request_options=request_options,
        )

    async def margin_transfer_for_sub_account_for_master_account(
        self,
        email: str,
        asset: str,
        amount: float,
        type_: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SubAccountMarginTransferResponse, MarginTransferForSubAccountForMasterAccountErrorBody]:
        """Weight(IP): 1

        Args:
            email: Sub-account email
            asset: Value sent with the request.
            amount: Value sent with the request.
            type_: * ``1`` - transfer from subaccount's spot account to margin account * ``2`` - transfer from
                subaccount's margin account to its spot account
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/sub-account/margin/transfer"),
            query_params=[
                param[str]("email", email),
                param[str]("asset", asset),
                param[float]("amount", amount),
                param[int]("type", type_),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountMarginTransferResponse],
            error_mapper=margin_transfer_for_sub_account_for_master_account_error_mapper,
            request_options=request_options,
        )

    async def query_managed_sub_account_transfer_log_for_investor_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        transfers: str | None = None,
        transfer_function_account_type: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1ManagedSubaccountQueryTransLogForInvestorResponse,
        QueryManagedSubAccountTransferLogForInvestorMasterAccountErrorBody,
    ]:
        """Investor can use this api to query managed sub account transfer log. This endpoint is available for investor
        of Managed Sub-Account. A Managed Sub-Account is an account type for investors who value flexibility in asset
        allocation and account application, while delegating trades to a professional trading team.

        Weight(IP): 1

        Args:
            email: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            page: Default 1
            limit: Default 500; max 1000.
            transfers: Transfer Direction (FROM/TO)
            transfer_function_account_type: Transfer function account type
                (SPOT/MARGIN/ISOLATED_MARGIN/USDT_FUTURE/COIN_FUTURE)
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/managed-subaccount/queryTransLogForInvestor"),
            query_params=[
                param[str]("email", email),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("page", page),
                param[int | None]("limit", limit),
                param[str | None]("transfers", transfers),
                param[str | None]("transferFunctionAccountType", transfer_function_account_type),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1ManagedSubaccountQueryTransLogForInvestorResponse],
            error_mapper=query_managed_sub_account_transfer_log_for_investor_master_account_error_mapper,
            request_options=request_options,
        )

    async def query_managed_sub_account_transfer_log_for_trading_team_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        transfers: str | None = None,
        transfer_function_account_type: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1ManagedSubaccountQueryTransLogForTradeParentResponse,
        QueryManagedSubAccountTransferLogForTradingTeamMasterAccountErrorBody,
    ]:
        """Trading team can use this api to query managed sub account transfer log. This endpoint is available for
        trading team of Managed Sub-Account. A Managed Sub-Account is an account type for investors who value
        flexibility in asset allocation and account application, while delegating trades to a professional trading team

        Weight(IP): 60

        Args:
            email: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            page: Default 1
            limit: Default 500; max 1000.
            transfers: Transfer Direction (FROM/TO)
            transfer_function_account_type: Transfer function account type
                (SPOT/MARGIN/ISOLATED_MARGIN/USDT_FUTURE/COIN_FUTURE)
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/managed-subaccount/queryTransLogForTradeParent"),
            query_params=[
                param[str]("email", email),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("page", page),
                param[int | None]("limit", limit),
                param[str | None]("transfers", transfers),
                param[str | None]("transferFunctionAccountType", transfer_function_account_type),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1ManagedSubaccountQueryTransLogForTradeParentResponse],
            error_mapper=query_managed_sub_account_transfer_log_for_trading_team_master_account_error_mapper,
            request_options=request_options,
        )

    async def query_managed_sub_account_transfer_log_for_trading_team_sub_account_user_data(
        self,
        transfers: TransfersOrStr,
        transfer_function_account_type: TransferFunctionAccountTypeOrStr,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1ManagedSubaccountQueryTransLogResponse,
        QueryManagedSubAccountTransferLogForTradingTeamSubAccountUserDataErrorBody,
    ]:
        """Query Managed Sub Account Transfer Log (For Trading Team Sub Account)

        Weight(UID): 60

        Args:
            transfers: Transfer Direction
            transfer_function_account_type: Transfer function account type
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            page: Default 1
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/managed-subaccount/query-trans-log"),
            query_params=[
                param[TransfersOrStr]("transfers", transfers),
                param[TransferFunctionAccountTypeOrStr]("transferFunctionAccountType", transfer_function_account_type),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("page", page),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1ManagedSubaccountQueryTransLogResponse],
            error_mapper=query_managed_sub_account_transfer_log_for_trading_team_sub_account_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_managed_sub_account_futures_asset_details_for_investor_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1ManagedSubaccountFetchFutureAssetResponse,
        QueryManagedSubAccountFuturesAssetDetailsForInvestorMasterAccountErrorBody,
    ]:
        """Investor can use this api to query managed sub account futures asset details

        Args:
            email: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/managed-subaccount/fetch-future-asset"),
            query_params=[
                param[str]("email", email),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1ManagedSubaccountFetchFutureAssetResponse],
            error_mapper=query_managed_sub_account_futures_asset_details_for_investor_master_account_error_mapper,
            request_options=request_options,
        )

    async def query_managed_sub_account_list_for_investor(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        page: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1ManagedSubaccountInfoResponse, QueryManagedSubAccountListForInvestorErrorBody]:
        """Get investor's managed sub-account list.

        Weight(UID): 60

        Args:
            email: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            page: Default 1
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/managed-subaccount/info"),
            query_params=[
                param[str]("email", email),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("page", page),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1ManagedSubaccountInfoResponse],
            error_mapper=query_managed_sub_account_list_for_investor_error_mapper,
            request_options=request_options,
        )

    async def query_managed_sub_account_margin_asset_details_for_investor_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1ManagedSubaccountMarginAssetResponse,
        QueryManagedSubAccountMarginAssetDetailsForInvestorMasterAccountErrorBody,
    ]:
        """Investor can use this api to query managed sub account margin asset details

        Args:
            email: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/managed-subaccount/marginAsset"),
            query_params=[
                param[str]("email", email),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1ManagedSubaccountMarginAssetResponse],
            error_mapper=query_managed_sub_account_margin_asset_details_for_investor_master_account_error_mapper,
            request_options=request_options,
        )

    async def query_sub_account_assets_for_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV4SubAccountAssetsResponse, QuerySubAccountAssetsForMasterAccountErrorBody]:
        """Fetch sub-account assets

        Weight(UID): 60

        Args:
            email: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v4/sub-account/assets"),
            query_params=[
                param[str]("email", email),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV4SubAccountAssetsResponse],
            error_mapper=query_sub_account_assets_for_master_account_error_mapper,
            request_options=request_options,
        )

    async def query_sub_account_list_for_master_account(
        self,
        timestamp: int,
        signature: str,
        *,
        email: str | None = None,
        is_freeze: IsFreezeOrStr | None = None,
        page: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SubAccountListResponse, QuerySubAccountListForMasterAccountErrorBody]:
        """Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            email: Sub-account email
            is_freeze: Value sent with the request.
            page: Default 1
            limit: Default 1; max 200
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/sub-account/list"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("email", email),
                param[IsFreezeOrStr | None]("isFreeze", is_freeze),
                param[int | None]("page", page),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountListResponse],
            error_mapper=query_sub_account_list_for_master_account_error_mapper,
            request_options=request_options,
        )

    async def query_sub_account_transaction_statistics_for_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1SubAccountTransactionStatisticsResponse, QuerySubAccountTransactionStatisticsForMasterAccountErrorBody
    ]:
        """Query Sub-account Transaction statistics (For Master Account).

        Weight(UID): 60

        Args:
            email: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/sub-account/transaction-statistics"),
            query_params=[
                param[str]("email", email),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountTransactionStatisticsResponse],
            error_mapper=query_sub_account_transaction_statistics_for_master_account_error_mapper,
            request_options=request_options,
        )

    async def sub_account_assets_for_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV3SubAccountAssetsResponse, SubAccountAssetsForMasterAccountErrorBody]:
        """Fetch sub-account assets

        Weight(IP): 1

        Args:
            email: Sub-account email
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v3/sub-account/assets"),
            query_params=[
                param[str]("email", email),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV3SubAccountAssetsResponse],
            error_mapper=sub_account_assets_for_master_account_error_mapper,
            request_options=request_options,
        )

    async def sub_account_deposit_history_for_master_account(
        self,
        email: str,
        timestamp: int,
        signature: str,
        *,
        coin: str | None = None,
        status: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        offset: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1CapitalDepositSubHisrecResponse], SubAccountDepositHistoryForMasterAccountErrorBody]:
        """Fetch sub-account deposit history

        Weight(IP): 1

        Args:
            email: Sub-account email
            timestamp: UTC timestamp in ms
            signature: Signature
            coin: Coin name
            status: 0(0:pending,6: credited but cannot withdraw, 1:success)
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Value sent with the request.
            offset: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/capital/deposit/subHisrec"),
            query_params=[
                param[str]("email", email),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("coin", coin),
                param[int | None]("status", status),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1CapitalDepositSubHisrecResponse]],
            error_mapper=sub_account_deposit_history_for_master_account_error_mapper,
            request_options=request_options,
        )

    async def sub_account_futures_asset_transfer_for_master_account(
        self,
        from_email: str,
        to_email: str,
        futures_type: int,
        asset: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1SubAccountFuturesInternalTransferResponse1, SubAccountFuturesAssetTransferForMasterAccountErrorBody
    ]:
        """- Master account can transfer max 2000 times a minute

        Weight(IP): 1

        Args:
            from_email: Sender email
            to_email: Recipient email
            futures_type: 1:USDT-margined Futures,2: Coin-margined Futures
            asset: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/sub-account/futures/internalTransfer"),
            query_params=[
                param[str]("fromEmail", from_email),
                param[str]("toEmail", to_email),
                param[int]("futuresType", futures_type),
                param[str]("asset", asset),
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountFuturesInternalTransferResponse1],
            error_mapper=sub_account_futures_asset_transfer_for_master_account_error_mapper,
            request_options=request_options,
        )

    async def sub_account_futures_asset_transfer_history_for_master_account(
        self,
        email: str,
        futures_type: int,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1SubAccountFuturesInternalTransferResponse, SubAccountFuturesAssetTransferHistoryForMasterAccountErrorBody
    ]:
        """Weight(IP): 1

        Args:
            email: Sub-account email
            futures_type: 1:USDT-margined Futures, 2: Coin-margined Futures
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            page: Default 1
            limit: Default value: 50, Max value: 500
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/sub-account/futures/internalTransfer"),
            query_params=[
                param[str]("email", email),
                param[int]("futuresType", futures_type),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("page", page),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountFuturesInternalTransferResponse],
            error_mapper=sub_account_futures_asset_transfer_history_for_master_account_error_mapper,
            request_options=request_options,
        )

    async def sub_account_spot_asset_transfer_history_for_master_account(
        self,
        timestamp: int,
        signature: str,
        *,
        from_email: str | None = None,
        to_email: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        list[SapiV1SubAccountSubTransferHistoryResponse], SubAccountSpotAssetTransferHistoryForMasterAccountErrorBody
    ]:
        """- fromEmail and toEmail cannot be sent at the same time.
        - Return fromEmail equal master account email by default.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            from_email: Sub-account email
            to_email: Sub-account email
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            page: Default 1
            limit: Default 1
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/sub-account/sub/transfer/history"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("fromEmail", from_email),
                param[str | None]("toEmail", to_email),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("page", page),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1SubAccountSubTransferHistoryResponse]],
            error_mapper=sub_account_spot_asset_transfer_history_for_master_account_error_mapper,
            request_options=request_options,
        )

    async def sub_account_spot_assets_summary_for_master_account(
        self,
        timestamp: int,
        signature: str,
        *,
        email: str | None = None,
        page: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SubAccountSpotSummaryResponse, SubAccountSpotAssetsSummaryForMasterAccountErrorBody]:
        """Get BTC valued asset summary of subaccounts.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            email: Sub-account email
            page: Default 1
            size: Default:10 Max:20
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/sub-account/spotSummary"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("email", email),
                param[int | None]("page", page),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountSpotSummaryResponse],
            error_mapper=sub_account_spot_assets_summary_for_master_account_error_mapper,
            request_options=request_options,
        )

    async def sub_account_spot_assets_summary_for_master_account_2(
        self,
        email: str,
        coin: str,
        timestamp: int,
        signature: str,
        *,
        network: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1CapitalDepositSubAddressResponse, SubAccountSpotAssetsSummaryForMasterAccount2ErrorBody]:
        """Fetch sub-account deposit address

        Weight(IP): 1

        Args:
            email: Sub-account email
            coin: Coin name
            timestamp: UTC timestamp in ms
            signature: Signature
            network: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/capital/deposit/subAddress"),
            query_params=[
                param[str]("email", email),
                param[str]("coin", coin),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("network", network),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1CapitalDepositSubAddressResponse],
            error_mapper=sub_account_spot_assets_summary_for_master_account2_error_mapper,
            request_options=request_options,
        )

    async def sub_account_transfer_history_for_sub_account(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        type_: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        list[SapiV1SubAccountTransferSubUserHistoryResponse], SubAccountTransferHistoryForSubAccountErrorBody
    ]:
        """- If ``type`` is not sent, the records of type 2: transfer out will be returned by default.
        - If ``startTime`` and ``endTime`` are not sent, the recent 30-day data will be returned.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            type_: * ``1`` - transfer in * ``2`` - transfer out
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/sub-account/transfer/subUserHistory"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("asset", asset),
                param[int | None]("type", type_),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1SubAccountTransferSubUserHistoryResponse]],
            error_mapper=sub_account_transfer_history_for_sub_account_error_mapper,
            request_options=request_options,
        )

    async def sub_account_s_status_on_margin_futures_for_master_account(
        self,
        timestamp: int,
        signature: str,
        *,
        email: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1SubAccountStatusResponse], SubAccountSStatusOnMarginFuturesForMasterAccountErrorBody]:
        """- If no ``email`` sent, all sub-accounts' information will be returned.

        Weight(IP): 10

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            email: Sub-account email
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/sub-account/status"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("email", email),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1SubAccountStatusResponse]],
            error_mapper=sub_account_s_status_on_margin_futures_for_master_account_error_mapper,
            request_options=request_options,
        )

    async def summary_of_sub_account_s_futures_account_for_master_account(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1SubAccountFuturesAccountSummaryResponse, SummaryOfSubAccountSFuturesAccountForMasterAccountErrorBody
    ]:
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
            url_template=self._server.default("/sapi/v1/sub-account/futures/accountSummary"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountFuturesAccountSummaryResponse],
            error_mapper=summary_of_sub_account_s_futures_account_for_master_account_error_mapper,
            request_options=request_options,
        )

    async def summary_of_sub_account_s_futures_account_v2_for_master_account(
        self,
        futures_type: int,
        timestamp: int,
        signature: str,
        *,
        page: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV2SubAccountFuturesAccountSummaryResponse, SummaryOfSubAccountSFuturesAccountV2ForMasterAccountErrorBody
    ]:
        """Weight(IP): 10

        Args:
            futures_type: * ``1`` - USDT Margined Futures * ``2`` - COIN Margined Futures
            timestamp: UTC timestamp in ms
            signature: Signature
            page: Default 1
            limit: Default 10, Max 20
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v2/sub-account/futures/accountSummary"),
            query_params=[
                param[int]("futuresType", futures_type),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("page", page),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV2SubAccountFuturesAccountSummaryResponse],
            error_mapper=summary_of_sub_account_s_futures_account_v2_for_master_account_error_mapper,
            request_options=request_options,
        )

    async def summary_of_sub_account_s_margin_account_for_master_account(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1SubAccountMarginAccountSummaryResponse, SummaryOfSubAccountSMarginAccountForMasterAccountErrorBody
    ]:
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
            url_template=self._server.default("/sapi/v1/sub-account/margin/accountSummary"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountMarginAccountSummaryResponse],
            error_mapper=summary_of_sub_account_s_margin_account_for_master_account_error_mapper,
            request_options=request_options,
        )

    async def transfer_for_sub_account_for_master_account(
        self,
        email: str,
        asset: str,
        amount: float,
        type_: int,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SubAccountFuturesTransferResponse, TransferForSubAccountForMasterAccountErrorBody]:
        """Weight(IP): 1

        Args:
            email: Sub-account email
            asset: Value sent with the request.
            amount: Value sent with the request.
            type_: * ``1`` - transfer from subaccount's spot account to its USDT-margined futures account * ``2`` -
                transfer from subaccount's USDT-margined futures account to its spot account * ``3`` - transfer from
                subaccount's spot account to its COIN-margined futures account * ``4`` - transfer from subaccount's
                COIN-margined futures account to its spot account
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/sub-account/futures/transfer"),
            query_params=[
                param[str]("email", email),
                param[str]("asset", asset),
                param[float]("amount", amount),
                param[int]("type", type_),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountFuturesTransferResponse],
            error_mapper=transfer_for_sub_account_for_master_account_error_mapper,
            request_options=request_options,
        )

    async def transfer_to_master_for_sub_account(
        self,
        asset: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SubAccountTransferSubToMasterResponse, TransferToMasterForSubAccountErrorBody]:
        """Weight(IP): 1

        Args:
            asset: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/sub-account/transfer/subToMaster"),
            query_params=[
                param[str]("asset", asset),
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountTransferSubToMasterResponse],
            error_mapper=transfer_to_master_for_sub_account_error_mapper,
            request_options=request_options,
        )

    async def transfer_to_sub_account_of_same_master_for_sub_account(
        self,
        to_email: str,
        asset: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SubAccountTransferSubToSubResponse, TransferToSubAccountOfSameMasterForSubAccountErrorBody]:
        """Weight(IP): 1

        Args:
            to_email: Recipient email
            asset: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/sub-account/transfer/subToSub"),
            query_params=[
                param[str]("toEmail", to_email),
                param[str]("asset", asset),
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountTransferSubToSubResponse],
            error_mapper=transfer_to_sub_account_of_same_master_for_sub_account_error_mapper,
            request_options=request_options,
        )

    async def universal_transfer_for_master_account(
        self,
        from_account_type: FromAccountTypeOrStr,
        to_account_type: ToAccountTypeOrStr,
        asset: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        from_email: str | None = None,
        to_email: str | None = None,
        client_tran_id: str | None = None,
        symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1SubAccountUniversalTransferResponse1, UniversalTransferForMasterAccountErrorBody]:
        """- You need to enable "internal transfer" option for the api key which requests this endpoint.
        - Transfer from master account by default if fromEmail is not sent.
        - Transfer to master account by default if toEmail is not sent.
        - Supported transfer scenarios:
          - Master account SPOT transfer to sub-account SPOT,USDT_FUTURE,COIN_FUTURE,MARGIN(Cross),ISOLATED_MARGIN
          - Sub-account SPOT,USDT_FUTURE,COIN_FUTURE,MARGIN(Cross),ISOLATED_MARGIN transfer to master account SPOT
          - Transfer between two sub-account SPOT accounts

        Weight(IP): 1

        Args:
            from_account_type: Value sent with the request.
            to_account_type: Value sent with the request.
            asset: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            from_email: Sub-account email
            to_email: Sub-account email
            client_tran_id: Value sent with the request.
            symbol: Only supported under ISOLATED_MARGIN type
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/sub-account/universalTransfer"),
            query_params=[
                param[FromAccountTypeOrStr]("fromAccountType", from_account_type),
                param[ToAccountTypeOrStr]("toAccountType", to_account_type),
                param[str]("asset", asset),
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("fromEmail", from_email),
                param[str | None]("toEmail", to_email),
                param[str | None]("clientTranId", client_tran_id),
                param[str | None]("symbol", symbol),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1SubAccountUniversalTransferResponse1],
            error_mapper=universal_transfer_for_master_account_error_mapper,
            request_options=request_options,
        )

    async def universal_transfer_history_for_master_account(
        self,
        timestamp: int,
        signature: str,
        *,
        from_email: str | None = None,
        to_email: str | None = None,
        client_tran_id: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1SubAccountUniversalTransferResponse], UniversalTransferHistoryForMasterAccountErrorBody]:
        """- ``fromEmail`` and ``toEmail`` cannot be sent at the same time.
        - Return ``fromEmail`` equal master account email by default.
        - The query time period must be less then 30 days.
        - If startTime and endTime not sent, return records of the last 30 days by default.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            from_email: Sub-account email
            to_email: Sub-account email
            client_tran_id: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            page: Default 1
            limit: Default 500, Max 500
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/sub-account/universalTransfer"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("fromEmail", from_email),
                param[str | None]("toEmail", to_email),
                param[str | None]("clientTranId", client_tran_id),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("page", page),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1SubAccountUniversalTransferResponse]],
            error_mapper=universal_transfer_history_for_master_account_error_mapper,
            request_options=request_options,
        )

    async def update_ip_restriction_for_sub_account_api_key_for_master_account(
        self,
        email: str,
        sub_account_api_key: str,
        status: str,
        timestamp: int,
        signature: str,
        *,
        third_party_name: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV2SubAccountSubAccountApiIpRestrictionResponse,
        UpdateIpRestrictionForSubAccountApiKeyForMasterAccountErrorBody,
    ]:
        """Update IP Restriction for Sub-Account API key

        Weight(UID): 3000

        Args:
            email: Sub-account email
            sub_account_api_key: Value sent with the request.
            status: IP Restriction status. 1 = IP Unrestricted. 2 = Restrict access to trusted IPs only. 3 = Restrict
                access to users' trusted third party IPs only
            timestamp: UTC timestamp in ms
            signature: Signature
            third_party_name: third party IP list name
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v2/sub-account/subAccountApi/ipRestriction"),
            query_params=[
                param[str]("email", email),
                param[str]("subAccountApiKey", sub_account_api_key),
                param[str]("status", status),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("thirdPartyName", third_party_name),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV2SubAccountSubAccountApiIpRestrictionResponse],
            error_mapper=update_ip_restriction_for_sub_account_api_key_for_master_account_error_mapper,
            request_options=request_options,
        )

    async def withdrawl_assets_from_the_managed_sub_account_for_investor_master_account(
        self,
        from_email: str,
        asset: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        transfer_date: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1ManagedSubaccountWithdrawResponse,
        WithdrawlAssetsFromTheManagedSubAccountForInvestorMasterAccountErrorBody,
    ]:
        """Weight(IP): 1

        Args:
            from_email: Sender email
            asset: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            transfer_date: Withdrawals is automatically occur on the transfer date(UTC0). If a date is not selected, the
                withdrawal occurs right now
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/managed-subaccount/withdraw"),
            query_params=[
                param[str]("fromEmail", from_email),
                param[str]("asset", asset),
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("transferDate", transfer_date),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1ManagedSubaccountWithdrawResponse],
            error_mapper=withdrawl_assets_from_the_managed_sub_account_for_investor_master_account_error_mapper,
            request_options=request_options,
        )
