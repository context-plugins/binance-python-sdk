from __future__ import annotations

from typing import Any
from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
    raw_error_response,
)
from ..errors.account_api_trading_status_user_data_error import (
    AccountApiTradingStatusUserDataErrorBody,
    account_api_trading_status_user_data_error_mapper,
)
from ..errors.account_info_user_data_error import AccountInfoUserDataErrorBody, account_info_user_data_error_mapper
from ..errors.account_status_user_data_error import (
    AccountStatusUserDataErrorBody,
    account_status_user_data_error_mapper,
)
from ..errors.all_coins_information_user_data_error import (
    AllCoinsInformationUserDataErrorBody,
    all_coins_information_user_data_error_mapper,
)
from ..errors.asset_detail_user_data_error import AssetDetailUserDataErrorBody, asset_detail_user_data_error_mapper
from ..errors.asset_dividend_record_user_data_error import (
    AssetDividendRecordUserDataErrorBody,
    asset_dividend_record_user_data_error_mapper,
)
from ..errors.convert_transfer_user_data_error import (
    ConvertTransferUserDataErrorBody,
    convert_transfer_user_data_error_mapper,
)
from ..errors.daily_account_snapshot_user_data_error import (
    DailyAccountSnapshotUserDataErrorBody,
    daily_account_snapshot_user_data_error_mapper,
)
from ..errors.deposit_address_supporting_network_user_data_error import (
    DepositAddressSupportingNetworkUserDataErrorBody,
    deposit_address_supporting_network_user_data_error_mapper,
)
from ..errors.deposit_history_supporting_network_user_data_error import (
    DepositHistorySupportingNetworkUserDataErrorBody,
    deposit_history_supporting_network_user_data_error_mapper,
)
from ..errors.disable_fast_withdraw_switch_user_data_error import (
    DisableFastWithdrawSwitchUserDataErrorBody,
    disable_fast_withdraw_switch_user_data_error_mapper,
)
from ..errors.dust_log_user_data_error import DustLogUserDataErrorBody, dust_log_user_data_error_mapper
from ..errors.dust_transfer_user_data_error import DustTransferUserDataErrorBody, dust_transfer_user_data_error_mapper
from ..errors.enable_fast_withdraw_switch_user_data_error import (
    EnableFastWithdrawSwitchUserDataErrorBody,
    enable_fast_withdraw_switch_user_data_error_mapper,
)
from ..errors.fetch_deposit_address_list_with_network_user_data_error import (
    FetchDepositAddressListWithNetworkUserDataErrorBody,
    fetch_deposit_address_list_with_network_user_data_error_mapper,
)
from ..errors.fetch_withdraw_address_list_user_data_error import (
    FetchWithdrawAddressListUserDataErrorBody,
    fetch_withdraw_address_list_user_data_error_mapper,
)
from ..errors.funding_wallet_user_data_error import (
    FundingWalletUserDataErrorBody,
    funding_wallet_user_data_error_mapper,
)
from ..errors.get_api_key_permission_user_data_error import (
    GetApiKeyPermissionUserDataErrorBody,
    get_api_key_permission_user_data_error_mapper,
)
from ..errors.get_assets_that_can_be_converted_into_bnb_user_data_error import (
    GetAssetsThatCanBeConvertedIntoBnbUserDataErrorBody,
    get_assets_that_can_be_converted_into_bnb_user_data_error_mapper,
)
from ..errors.get_cloud_mining_payment_and_refund_history_user_data_error import (
    GetCloudMiningPaymentAndRefundHistoryUserDataErrorBody,
    get_cloud_mining_payment_and_refund_history_user_data_error_mapper,
)
from ..errors.get_symbols_delist_schedule_for_spot_market_data_error import (
    GetSymbolsDelistScheduleForSpotMarketDataErrorBody,
    get_symbols_delist_schedule_for_spot_market_data_error_mapper,
)
from ..errors.one_click_arrival_deposit_apply_user_data_error import (
    OneClickArrivalDepositApplyUserDataErrorBody,
    one_click_arrival_deposit_apply_user_data_error_mapper,
)
from ..errors.query_auto_converting_stable_coins_user_data_error import (
    QueryAutoConvertingStableCoinsUserDataErrorBody,
    query_auto_converting_stable_coins_user_data_error_mapper,
)
from ..errors.query_convert_transfer_user_data_error import (
    QueryConvertTransferUserDataErrorBody,
    query_convert_transfer_user_data_error_mapper,
)
from ..errors.query_user_delegation_history_for_master_account_user_data_error import (
    QueryUserDelegationHistoryForMasterAccountUserDataErrorBody,
    query_user_delegation_history_for_master_account_user_data_error_mapper,
)
from ..errors.query_user_universal_transfer_history_user_data_error import (
    QueryUserUniversalTransferHistoryUserDataErrorBody,
    query_user_universal_transfer_history_user_data_error_mapper,
)
from ..errors.query_user_wallet_balance_user_data_error import (
    QueryUserWalletBalanceUserDataErrorBody,
    query_user_wallet_balance_user_data_error_mapper,
)
from ..errors.switch_on_off_busd_and_stable_coins_conversion_user_data_user_data_error import (
    SwitchOnOffBusdAndStableCoinsConversionUserDataUserDataErrorBody,
    switch_on_off_busd_and_stable_coins_conversion_user_data_user_data_error_mapper,
)
from ..errors.trade_fee_user_data_error import TradeFeeUserDataErrorBody, trade_fee_user_data_error_mapper
from ..errors.user_asset_user_data_error import UserAssetUserDataErrorBody, user_asset_user_data_error_mapper
from ..errors.user_universal_transfer_user_data_error import (
    UserUniversalTransferUserDataErrorBody,
    user_universal_transfer_user_data_error_mapper,
)
from ..errors.withdraw_history_supporting_network_user_data_error import (
    WithdrawHistorySupportingNetworkUserDataErrorBody,
    withdraw_history_supporting_network_user_data_error_mapper,
)
from ..errors.withdraw_user_data_error import WithdrawUserDataErrorBody, withdraw_user_data_error_mapper
from ..models.enums.account_type import AccountTypeOrStr
from ..models.enums.account_type3 import AccountType3OrStr
from ..models.enums.need_btc_valuation import NeedBtcValuationOrStr
from ..models.enums.type6 import Type6OrStr
from ..models.enums.type7 import Type7OrStr
from ..models.sapi_v1_account_api_restrictions_response import SapiV1AccountApiRestrictionsResponse
from ..models.sapi_v1_account_api_trading_status_response import SapiV1AccountApiTradingStatusResponse
from ..models.sapi_v1_account_info_response import SapiV1AccountInfoResponse
from ..models.sapi_v1_account_status_response import SapiV1AccountStatusResponse
from ..models.sapi_v1_asset_asset_detail_response import SapiV1AssetAssetDetailResponse
from ..models.sapi_v1_asset_asset_dividend_response import SapiV1AssetAssetDividendResponse
from ..models.sapi_v1_asset_convert_transfer_query_by_page_response import SapiV1AssetConvertTransferQueryByPageResponse
from ..models.sapi_v1_asset_convert_transfer_response import SapiV1AssetConvertTransferResponse
from ..models.sapi_v1_asset_custody_transfer_history_response import SapiV1AssetCustodyTransferHistoryResponse
from ..models.sapi_v1_asset_dribblet_response import SapiV1AssetDribbletResponse
from ..models.sapi_v1_asset_dust_btc_response import SapiV1AssetDustBtcResponse
from ..models.sapi_v1_asset_dust_response import SapiV1AssetDustResponse
from ..models.sapi_v1_asset_get_funding_asset_response import SapiV1AssetGetFundingAssetResponse
from ..models.sapi_v1_asset_ledger_transfer_cloud_mining_query_by_page_response import (
    SapiV1AssetLedgerTransferCloudMiningQueryByPageResponse,
)
from ..models.sapi_v1_asset_trade_fee_response import SapiV1AssetTradeFeeResponse
from ..models.sapi_v1_asset_transfer_response import SapiV1AssetTransferResponse
from ..models.sapi_v1_asset_transfer_response1 import SapiV1AssetTransferResponse1
from ..models.sapi_v1_asset_wallet_balance_response import SapiV1AssetWalletBalanceResponse
from ..models.sapi_v1_capital_config_getall_response import SapiV1CapitalConfigGetallResponse
from ..models.sapi_v1_capital_contract_convertible_coins_response import SapiV1CapitalContractConvertibleCoinsResponse
from ..models.sapi_v1_capital_deposit_address_list_response import SapiV1CapitalDepositAddressListResponse
from ..models.sapi_v1_capital_deposit_address_response import SapiV1CapitalDepositAddressResponse
from ..models.sapi_v1_capital_deposit_credit_apply_response import SapiV1CapitalDepositCreditApplyResponse
from ..models.sapi_v1_capital_deposit_hisrec_response import SapiV1CapitalDepositHisrecResponse
from ..models.sapi_v1_capital_withdraw_address_list_response import SapiV1CapitalWithdrawAddressListResponse
from ..models.sapi_v1_capital_withdraw_apply_response import SapiV1CapitalWithdrawApplyResponse
from ..models.sapi_v1_capital_withdraw_history_response import SapiV1CapitalWithdrawHistoryResponse
from ..models.sapi_v1_spot_delist_schedule_response import SapiV1SpotDelistScheduleResponse
from ..models.sapi_v1_system_status_response import SapiV1SystemStatusResponse
from ..models.sapi_v3_asset_get_user_asset_response import SapiV3AssetGetUserAssetResponse
from ..models.unions.sapi_v1_account_snapshot_response import SapiV1AccountSnapshotResponse
from ..server.server import Server


class Wallet:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = WalletWithRawResponse(client, server, auth)

    def account_api_trading_status_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AccountApiTradingStatusResponse:
        """Fetch account API trading status with details.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Account API trading status

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.account_api_trading_status_user_data(
            timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def account_status_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AccountStatusResponse:
        """Fetch account status detail.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.account_status_user_data(
            timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def account_info_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AccountInfoResponse:
        """Fetch account info detail.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Account info detail

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.account_info_user_data(
            timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def all_coins_information_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1CapitalConfigGetallResponse]:
        """Get information of coins (available for deposit and withdraw) for user.

        Weight(IP): 10

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            All coins details information

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.all_coins_information_user_data(
            timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def asset_detail_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AssetAssetDetailResponse:
        """Fetch details of assets supported on Binance.

        - Please get network and other deposit or withdraw details from ``GET /sapi/v1/capital/config/getall``.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Asset detail

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.asset_detail_user_data(
            timestamp, signature, asset=asset, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def asset_dividend_record_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = 20,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AssetAssetDividendResponse:
        """Query asset Dividend Record

        Weight(IP): 10

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Records of asset devidend

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.asset_dividend_record_user_data(
            timestamp,
            signature,
            asset=asset,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def convert_transfer_user_data(
        self,
        client_tran_id: str,
        asset: str,
        amount: float,
        target_asset: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AssetConvertTransferResponse:
        """Convert transfer, convert between BUSD and stablecoins. If the clientId has been used before, will not do the
        convert transfer, the original transfer will be returned.

        Weight(UID): 5

        Args:
            client_tran_id: The unique flag, the min length is 20
            asset: Value sent with the request.
            amount: Value sent with the request.
            target_asset: Target asset you want to convert
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Conversion Information

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.convert_transfer_user_data(
            client_tran_id,
            asset,
            amount,
            target_asset,
            timestamp,
            signature,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def daily_account_snapshot_user_data(
        self,
        type_: Type6OrStr,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = 7,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AccountSnapshotResponse:
        """- The query time period must be less than 30 days
        - Support query within the last one month only
        - If startTimeand endTime not sent, return records of the last 7 days by default

        Weight(IP): 2400

        Args:
            type_: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Account Snapshot

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.daily_account_snapshot_user_data(
            type_,
            timestamp,
            signature,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def deposit_address_supporting_network_user_data(
        self,
        coin: str,
        timestamp: int,
        signature: str,
        *,
        network: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1CapitalDepositAddressResponse:
        """Fetch deposit address with network.

        - If network is not send, return with default network of the coin.
        - You can get network and isDefault in networkList in the response of Get /sapi/v1/capital/config/getall (HMAC
            SHA256).

        Weight(IP): 10

        Args:
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
        return self._with_raw_response.deposit_address_supporting_network_user_data(
            coin, timestamp, signature, network=network, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def deposit_history_supporting_network_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        coin: str | None = None,
        status: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        offset: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1CapitalDepositHisrecResponse]:
        """Fetch deposit history.

        - Please notice the default ``startTime`` and ``endTime`` to make sure that time interval is within 0-90 days.
        - If both ``startTime`` and ``endTime`` are sent, time between ``startTime`` and ``endTime`` must be less than
            90 days.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            coin: Coin name
            status: * ``0`` - pending * ``6`` - credited but cannot withdraw * ``1`` - success
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            offset: Value sent with the request.
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of deposits

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.deposit_history_supporting_network_user_data(
            timestamp,
            signature,
            coin=coin,
            status=status,
            start_time=start_time,
            end_time=end_time,
            offset=offset,
            limit=limit,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def disable_fast_withdraw_switch_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """- This request will disable fastwithdraw switch under your account.
        - You need to enable "trade" option for the api key which requests this endpoint.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.disable_fast_withdraw_switch_user_data(
            timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def dust_transfer_user_data(
        self,
        asset: list[str],
        timestamp: int,
        signature: str,
        *,
        account_type: AccountTypeOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AssetDustResponse:
        """Convert dust assets to BNB.

        Weight(UID): 10

        Args:
            asset: The asset being converted. For example, asset=BTC&asset=USDT
            timestamp: UTC timestamp in ms
            signature: Signature
            account_type: SPOT or MARGIN, default SPOT
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Dust log records

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.dust_transfer_user_data(
            asset,
            timestamp,
            signature,
            account_type=account_type,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def dust_log_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        account_type: AccountTypeOrStr | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AssetDribbletResponse:
        """Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            account_type: SPOT or MARGIN, default SPOT
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Dust log records

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.dust_log_user_data(
            timestamp,
            signature,
            account_type=account_type,
            start_time=start_time,
            end_time=end_time,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def enable_fast_withdraw_switch_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """- This request will enable fastwithdraw switch under your account. You need to enable "trade" option for the
            api key which requests this endpoint.
        - When Fast Withdraw Switch is on, transferring funds to a Binance account will be done instantly. There is no
            on-chain transaction, no transaction ID and no withdrawal fee.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.enable_fast_withdraw_switch_user_data(
            timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def fetch_deposit_address_list_with_network_user_data(
        self,
        coin: str,
        timestamp: int,
        signature: str,
        *,
        network: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1CapitalDepositAddressListResponse]:
        """Fetch deposit address list with network.

        Weight(IP): 10

        Args:
            coin: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            network: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Coin address

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.fetch_deposit_address_list_with_network_user_data(
            coin, timestamp, signature, network=network, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def fetch_withdraw_address_list_user_data(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[SapiV1CapitalWithdrawAddressListResponse]:
        """Fetch withdraw address list

        Weight(IP): 10

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Withdraw address list

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.fetch_withdraw_address_list_user_data(request_options=request_options).unwrap()

    def funding_wallet_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        need_btc_valuation: NeedBtcValuationOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1AssetGetFundingAssetResponse]:
        """- Currently supports querying the following business assets：Binance Pay, Binance Card, Binance Gift Card,
            Stock Token

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            need_btc_valuation: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Funding asset detail

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.funding_wallet_user_data(
            timestamp,
            signature,
            asset=asset,
            need_btc_valuation=need_btc_valuation,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_api_key_permission_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AccountApiRestrictionsResponse:
        """Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            API Key permissions

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_api_key_permission_user_data(
            timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def get_assets_that_can_be_converted_into_bnb_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        account_type: AccountTypeOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AssetDustBtcResponse:
        """Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            account_type: SPOT or MARGIN, default SPOT
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Account assets available to be converted to BNB

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_assets_that_can_be_converted_into_bnb_user_data(
            timestamp, signature, account_type=account_type, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def get_cloud_mining_payment_and_refund_history_user_data(
        self,
        start_time: int,
        end_time: int,
        timestamp: int,
        signature: str,
        *,
        tran_id: int | None = None,
        client_tran_id: str | None = None,
        asset: str | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AssetLedgerTransferCloudMiningQueryByPageResponse:
        """The query of Cloud-Mining payment and refund history

        Weight(UID): 600

        Args:
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            timestamp: UTC timestamp in ms
            signature: Signature
            tran_id: The transaction id
            client_tran_id: The unique flag
            asset: If it is blank, we will query all assets
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Cloud Mining Payment and Refund History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_cloud_mining_payment_and_refund_history_user_data(
            start_time,
            end_time,
            timestamp,
            signature,
            tran_id=tran_id,
            client_tran_id=client_tran_id,
            asset=asset,
            current=current,
            size=size,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_symbols_delist_schedule_for_spot_market_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1SpotDelistScheduleResponse]:
        """Get symbols delist schedule for spot

        Weight(IP): 100

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Symbols delist schedule

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_symbols_delist_schedule_for_spot_market_data(
            timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def one_click_arrival_deposit_apply_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        deposit_id: int | None = None,
        tx_id: str | None = None,
        sub_account_id: int | None = None,
        sub_user_id: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1CapitalDepositCreditApplyResponse:
        """Apply deposit credit for expired address (One click arrival)

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            deposit_id: Deposit record Id, priority use
            tx_id: Deposit txId, used when depositId is not specified
            sub_account_id: Value sent with the request.
            sub_user_id: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            deposit result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.one_click_arrival_deposit_apply_user_data(
            timestamp,
            signature,
            deposit_id=deposit_id,
            tx_id=tx_id,
            sub_account_id=sub_account_id,
            sub_user_id=sub_user_id,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def query_convert_transfer_user_data(
        self,
        start_time: int,
        end_time: int,
        timestamp: int,
        signature: str,
        *,
        tran_id: int | None = None,
        asset: str | None = None,
        account_type: AccountType3OrStr | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AssetConvertTransferQueryByPageResponse:
        """Weight(UID): 5

        Args:
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            timestamp: UTC timestamp in ms
            signature: Signature
            tran_id: The transaction id
            asset: If it is blank, we will match deducted asset and target asset.
            account_type: MAIN: main account. CARD: funding account. If it is blank, we will query spot and card wallet,
                otherwise, we just query the corresponding wallet
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Query Convert Transfer

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_convert_transfer_user_data(
            start_time,
            end_time,
            timestamp,
            signature,
            tran_id=tran_id,
            asset=asset,
            account_type=account_type,
            current=current,
            size=size,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def query_user_delegation_history_for_master_account_user_data(
        self,
        email: str,
        start_time: int,
        end_time: int,
        asset: str,
        timestamp: int,
        signature: str,
        *,
        type_: str | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AssetCustodyTransferHistoryResponse:
        """Query User Delegation History

        Weight(IP): 60

        Args:
            email: Value sent with the request.
            start_time: Value sent with the request.
            end_time: Value sent with the request.
            asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            type_: Value sent with the request.
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Delegation History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_user_delegation_history_for_master_account_user_data(
            email,
            start_time,
            end_time,
            asset,
            timestamp,
            signature,
            type_=type_,
            current=current,
            size=size,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def query_user_universal_transfer_history_user_data(
        self,
        type_: Type7OrStr,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        from_symbol: str | None = None,
        to_symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AssetTransferResponse:
        """- ``fromSymbol`` must be sent when type are ISOLATEDMARGIN_MARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
        - ``toSymbol`` must be sent when type are MARGIN_ISOLATEDMARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
        - Support query within the last 6 months only
        - If ``startTime`` and ``endTime`` not sent, return records of the last 7 days by default

        Weight(IP): 1

        Args:
            type_: Universal transfer type
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            from_symbol: Must be sent when type are ISOLATEDMARGIN_MARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
            to_symbol: Must be sent when type are MARGIN_ISOLATEDMARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Universal transfer history

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_user_universal_transfer_history_user_data(
            type_,
            timestamp,
            signature,
            start_time=start_time,
            end_time=end_time,
            current=current,
            size=size,
            from_symbol=from_symbol,
            to_symbol=to_symbol,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def query_user_wallet_balance_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1AssetWalletBalanceResponse]:
        """Query User Wallet Balance

        Weight(IP): 60

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            wallet balance

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_user_wallet_balance_user_data(
            timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def query_auto_converting_stable_coins_user_data(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> SapiV1CapitalContractConvertibleCoinsResponse:
        """Get a user's auto-conversion settings in deposit/withdrawal

        Weight(UID): 600'

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            User's auto-conversion settings i

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_auto_converting_stable_coins_user_data(
            request_options=request_options
        ).unwrap()

    def switch_on_off_busd_and_stable_coins_conversion_user_data_user_data(
        self, coin: str, enable: bool, *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """User can use it to turn on or turn off the BUSD auto-conversion from/to a specific stable coin.

        Weight(UID): 600'

        Args:
            coin: Must be USDC, USDP or TUSD
            enable: true: turn on the auto-conversion. false: turn off the auto-conversion
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.switch_on_off_busd_and_stable_coins_conversion_user_data_user_data(
            coin, enable, request_options=request_options
        ).unwrap()

    def system_status_system(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> SapiV1SystemStatusResponse:
        """Fetch system status.

        Weight(IP): 1

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.system_status_system(request_options=request_options).unwrap()

    def trade_fee_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1AssetTradeFeeResponse]:
        """Fetch trade fee

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            symbol: Trading symbol, e.g. BNBUSDT
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Trade fee info per symbol

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.trade_fee_user_data(
            timestamp, signature, symbol=symbol, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def user_asset_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        need_btc_valuation: NeedBtcValuationOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV3AssetGetUserAssetResponse]:
        """Get user assets, just for positive data.

        Weight(IP): 5

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            need_btc_valuation: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            User assets

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.user_asset_user_data(
            timestamp,
            signature,
            asset=asset,
            need_btc_valuation=need_btc_valuation,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def user_universal_transfer_user_data(
        self,
        type_: Type7OrStr,
        asset: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        from_symbol: str | None = None,
        to_symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AssetTransferResponse1:
        """You need to enable ``Permits Universal Transfer`` option for the api key which requests this endpoint.

        - ``fromSymbol`` must be sent when type are ISOLATEDMARGIN_MARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
        - ``toSymbol`` must be sent when type are MARGIN_ISOLATEDMARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN

        ENUM of transfer types:
          - MAIN_UMFUTURE Spot account transfer to USDⓈ-M Futures account
          - MAIN_CMFUTURE Spot account transfer to COIN-M Futures account
          - MAIN_MARGIN Spot account transfer to Margin(cross)account
          - UMFUTURE_MAIN USDⓈ-M Futures account transfer to Spot account
          - UMFUTURE_MARGIN USDⓈ-M Futures account transfer to Margin(cross)account
          - CMFUTURE_MAIN COIN-M Futures account transfer to Spot account
          - CMFUTURE_MARGIN COIN-M Futures account transfer to Margin(cross) account
          - MARGIN_MAIN Margin(cross)account transfer to Spot account
          - MARGIN_UMFUTURE Margin(cross)account transfer to USDⓈ-M Futures
          - MARGIN_CMFUTURE Margin(cross)account transfer to COIN-M Futures
          - ISOLATEDMARGIN_MARGIN Isolated margin account transfer to Margin(cross) account
          - MARGIN_ISOLATEDMARGIN Margin(cross) account transfer to Isolated margin account
          - ISOLATEDMARGIN_ISOLATEDMARGIN Isolated margin account transfer to Isolated margin account
          - MAIN_FUNDING Spot account transfer to Funding account
          - FUNDING_MAIN Funding account transfer to Spot account
          - FUNDING_UMFUTURE Funding account transfer to UMFUTURE account
          - UMFUTURE_FUNDING UMFUTURE account transfer to Funding account
          - MARGIN_FUNDING MARGIN account transfer to Funding account
          - FUNDING_MARGIN Funding account transfer to Margin account
          - FUNDING_CMFUTURE Funding account transfer to CMFUTURE account
          - CMFUTURE_FUNDING CMFUTURE account transfer to Funding account
          - MAIN_OPTION Spot account transfer to Options account
          - OPTION_MAIN Options account transfer to Spot account
          - UMFUTURE_OPTION USDⓈ-M Futures account transfer to Options account
          - OPTION_UMFUTURE Options account transfer to USDⓈ-M Futures account
          - MARGIN_OPTION Margin(cross)account transfer to Options account
          - OPTION_MARGIN Options account transfer to Margin(cross)account
          - FUNDING_OPTION Funding account transfer to Options account
          - OPTION_FUNDING Options account transfer to Funding account
          - MAIN_PORTFOLIO_MARGIN Spot account transfer to Portfolio Margin account
          - PORTFOLIO_MARGIN_MAIN Portfolio Margin account transfer to Spot account
          - MAIN_ISOLATED_MARGIN Spot account transfer to Isolated margin account
          - ISOLATED_MARGIN_MAIN Isolated margin account transfer to Spot account

        Weight(IP): 1

        Args:
            type_: Universal transfer type
            asset: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            from_symbol: Must be sent when type are ISOLATEDMARGIN_MARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
            to_symbol: Must be sent when type are MARGIN_ISOLATEDMARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Transfer id

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.user_universal_transfer_user_data(
            type_,
            asset,
            amount,
            timestamp,
            signature,
            from_symbol=from_symbol,
            to_symbol=to_symbol,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def withdraw_user_data(
        self,
        coin: str,
        address: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        withdraw_order_id: str | None = None,
        network: str | None = None,
        address_tag: str | None = None,
        transaction_fee_flag: bool | None = False,
        name: str | None = None,
        wallet_type: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1CapitalWithdrawApplyResponse:
        """Submit a withdraw request.

        - If ``network`` not send, return with default network of the coin.
        - You can get ``network`` and ``isDefault`` in ``networkList`` of a coin in the response of ``Get
            /sapi/v1/capital/config/getall (HMAC SHA256)``.

        Weight(IP): 1

        Args:
            coin: Coin name
            address: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            withdraw_order_id: Client id for withdraw
            network: Value sent with the request.
            address_tag: Secondary address identifier for coins like XRP,XMR etc.
            transaction_fee_flag: When making internal transfer - ``true`` -> returning the fee to the destination
                account; - ``false`` -> returning the fee back to the departure account.
            name: Value sent with the request.
            wallet_type: The wallet type for withdraw，0-Spot wallet, 1- Funding wallet. Default is Spot wallet
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Transafer Id

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.withdraw_user_data(
            coin,
            address,
            amount,
            timestamp,
            signature,
            withdraw_order_id=withdraw_order_id,
            network=network,
            address_tag=address_tag,
            transaction_fee_flag=transaction_fee_flag,
            name=name,
            wallet_type=wallet_type,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def withdraw_history_supporting_network_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        coin: str | None = None,
        withdraw_order_id: str | None = None,
        status: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        offset: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1CapitalWithdrawHistoryResponse]:
        """Fetch withdraw history.

        This endpoint specifically uses per second UID rate limit, user's total second level IP rate limit is
        180000/second. Response from the endpoint contains header key X-SAPI-USED-UID-WEIGHT-1S, which defines weight
        used by the current IP.

        - ``network`` may not be in the response for old withdraw.
        - Please notice the default ``startTime`` and ``endTime`` to make sure that time interval is within 0-90 days.
        - If both ``startTime`` and ``endTime`` are sent, time between ``startTime`` and ``endTime`` must be less than
            90 days
        - If withdrawOrderId is sent, time between startTime and endTime must be less than 7 days.
        - If withdrawOrderId is sent, startTime and endTime are not sent, will return last 7 days records by default.

        Weight(UID): 18000 Request Limit: 10 requests per second

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            coin: Coin name
            withdraw_order_id: Value sent with the request.
            status: * ``0`` - Email Sent * ``1`` - Cancelled * ``2`` - Awaiting Approval * ``3`` - Rejected * ``4`` -
                Processing * ``5`` - Failure * ``6`` - Completed
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            offset: Value sent with the request.
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of withdraw history

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.withdraw_history_supporting_network_user_data(
            timestamp,
            signature,
            coin=coin,
            withdraw_order_id=withdraw_order_id,
            status=status,
            start_time=start_time,
            end_time=end_time,
            offset=offset,
            limit=limit,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> WalletWithRawResponse:
        return self._with_raw_response


class AsyncWallet:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncWalletWithRawResponse(client, server, auth)

    async def account_api_trading_status_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AccountApiTradingStatusResponse:
        """Fetch account API trading status with details.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Account API trading status

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.account_api_trading_status_user_data(
                timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def account_status_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AccountStatusResponse:
        """Fetch account status detail.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.account_status_user_data(
                timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def account_info_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AccountInfoResponse:
        """Fetch account info detail.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Account info detail

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.account_info_user_data(
                timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def all_coins_information_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1CapitalConfigGetallResponse]:
        """Get information of coins (available for deposit and withdraw) for user.

        Weight(IP): 10

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            All coins details information

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.all_coins_information_user_data(
                timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def asset_detail_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AssetAssetDetailResponse:
        """Fetch details of assets supported on Binance.

        - Please get network and other deposit or withdraw details from ``GET /sapi/v1/capital/config/getall``.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Asset detail

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.asset_detail_user_data(
                timestamp, signature, asset=asset, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def asset_dividend_record_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = 20,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AssetAssetDividendResponse:
        """Query asset Dividend Record

        Weight(IP): 10

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Records of asset devidend

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.asset_dividend_record_user_data(
                timestamp,
                signature,
                asset=asset,
                start_time=start_time,
                end_time=end_time,
                limit=limit,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def convert_transfer_user_data(
        self,
        client_tran_id: str,
        asset: str,
        amount: float,
        target_asset: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AssetConvertTransferResponse:
        """Convert transfer, convert between BUSD and stablecoins. If the clientId has been used before, will not do the
        convert transfer, the original transfer will be returned.

        Weight(UID): 5

        Args:
            client_tran_id: The unique flag, the min length is 20
            asset: Value sent with the request.
            amount: Value sent with the request.
            target_asset: Target asset you want to convert
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Conversion Information

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.convert_transfer_user_data(
                client_tran_id,
                asset,
                amount,
                target_asset,
                timestamp,
                signature,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def daily_account_snapshot_user_data(
        self,
        type_: Type6OrStr,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = 7,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AccountSnapshotResponse:
        """- The query time period must be less than 30 days
        - Support query within the last one month only
        - If startTimeand endTime not sent, return records of the last 7 days by default

        Weight(IP): 2400

        Args:
            type_: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Account Snapshot

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.daily_account_snapshot_user_data(
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

    async def deposit_address_supporting_network_user_data(
        self,
        coin: str,
        timestamp: int,
        signature: str,
        *,
        network: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1CapitalDepositAddressResponse:
        """Fetch deposit address with network.

        - If network is not send, return with default network of the coin.
        - You can get network and isDefault in networkList in the response of Get /sapi/v1/capital/config/getall (HMAC
            SHA256).

        Weight(IP): 10

        Args:
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
            await self._with_raw_response.deposit_address_supporting_network_user_data(
                coin, timestamp, signature, network=network, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def deposit_history_supporting_network_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        coin: str | None = None,
        status: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        offset: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1CapitalDepositHisrecResponse]:
        """Fetch deposit history.

        - Please notice the default ``startTime`` and ``endTime`` to make sure that time interval is within 0-90 days.
        - If both ``startTime`` and ``endTime`` are sent, time between ``startTime`` and ``endTime`` must be less than
            90 days.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            coin: Coin name
            status: * ``0`` - pending * ``6`` - credited but cannot withdraw * ``1`` - success
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            offset: Value sent with the request.
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of deposits

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.deposit_history_supporting_network_user_data(
                timestamp,
                signature,
                coin=coin,
                status=status,
                start_time=start_time,
                end_time=end_time,
                offset=offset,
                limit=limit,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def disable_fast_withdraw_switch_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """- This request will disable fastwithdraw switch under your account.
        - You need to enable "trade" option for the api key which requests this endpoint.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.disable_fast_withdraw_switch_user_data(
                timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def dust_transfer_user_data(
        self,
        asset: list[str],
        timestamp: int,
        signature: str,
        *,
        account_type: AccountTypeOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AssetDustResponse:
        """Convert dust assets to BNB.

        Weight(UID): 10

        Args:
            asset: The asset being converted. For example, asset=BTC&asset=USDT
            timestamp: UTC timestamp in ms
            signature: Signature
            account_type: SPOT or MARGIN, default SPOT
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Dust log records

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.dust_transfer_user_data(
                asset,
                timestamp,
                signature,
                account_type=account_type,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def dust_log_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        account_type: AccountTypeOrStr | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AssetDribbletResponse:
        """Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            account_type: SPOT or MARGIN, default SPOT
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Dust log records

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.dust_log_user_data(
                timestamp,
                signature,
                account_type=account_type,
                start_time=start_time,
                end_time=end_time,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def enable_fast_withdraw_switch_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """- This request will enable fastwithdraw switch under your account. You need to enable "trade" option for the
            api key which requests this endpoint.
        - When Fast Withdraw Switch is on, transferring funds to a Binance account will be done instantly. There is no
            on-chain transaction, no transaction ID and no withdrawal fee.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.enable_fast_withdraw_switch_user_data(
                timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def fetch_deposit_address_list_with_network_user_data(
        self,
        coin: str,
        timestamp: int,
        signature: str,
        *,
        network: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1CapitalDepositAddressListResponse]:
        """Fetch deposit address list with network.

        Weight(IP): 10

        Args:
            coin: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            network: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Coin address

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.fetch_deposit_address_list_with_network_user_data(
                coin, timestamp, signature, network=network, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def fetch_withdraw_address_list_user_data(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[SapiV1CapitalWithdrawAddressListResponse]:
        """Fetch withdraw address list

        Weight(IP): 10

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Withdraw address list

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.fetch_withdraw_address_list_user_data(request_options=request_options)
        ).unwrap()

    async def funding_wallet_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        need_btc_valuation: NeedBtcValuationOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1AssetGetFundingAssetResponse]:
        """- Currently supports querying the following business assets：Binance Pay, Binance Card, Binance Gift Card,
            Stock Token

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            need_btc_valuation: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Funding asset detail

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.funding_wallet_user_data(
                timestamp,
                signature,
                asset=asset,
                need_btc_valuation=need_btc_valuation,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def get_api_key_permission_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AccountApiRestrictionsResponse:
        """Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            API Key permissions

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_api_key_permission_user_data(
                timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def get_assets_that_can_be_converted_into_bnb_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        account_type: AccountTypeOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AssetDustBtcResponse:
        """Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            account_type: SPOT or MARGIN, default SPOT
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Account assets available to be converted to BNB

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_assets_that_can_be_converted_into_bnb_user_data(
                timestamp,
                signature,
                account_type=account_type,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def get_cloud_mining_payment_and_refund_history_user_data(
        self,
        start_time: int,
        end_time: int,
        timestamp: int,
        signature: str,
        *,
        tran_id: int | None = None,
        client_tran_id: str | None = None,
        asset: str | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AssetLedgerTransferCloudMiningQueryByPageResponse:
        """The query of Cloud-Mining payment and refund history

        Weight(UID): 600

        Args:
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            timestamp: UTC timestamp in ms
            signature: Signature
            tran_id: The transaction id
            client_tran_id: The unique flag
            asset: If it is blank, we will query all assets
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Cloud Mining Payment and Refund History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_cloud_mining_payment_and_refund_history_user_data(
                start_time,
                end_time,
                timestamp,
                signature,
                tran_id=tran_id,
                client_tran_id=client_tran_id,
                asset=asset,
                current=current,
                size=size,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def get_symbols_delist_schedule_for_spot_market_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1SpotDelistScheduleResponse]:
        """Get symbols delist schedule for spot

        Weight(IP): 100

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Symbols delist schedule

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_symbols_delist_schedule_for_spot_market_data(
                timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def one_click_arrival_deposit_apply_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        deposit_id: int | None = None,
        tx_id: str | None = None,
        sub_account_id: int | None = None,
        sub_user_id: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1CapitalDepositCreditApplyResponse:
        """Apply deposit credit for expired address (One click arrival)

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            deposit_id: Deposit record Id, priority use
            tx_id: Deposit txId, used when depositId is not specified
            sub_account_id: Value sent with the request.
            sub_user_id: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            deposit result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.one_click_arrival_deposit_apply_user_data(
                timestamp,
                signature,
                deposit_id=deposit_id,
                tx_id=tx_id,
                sub_account_id=sub_account_id,
                sub_user_id=sub_user_id,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def query_convert_transfer_user_data(
        self,
        start_time: int,
        end_time: int,
        timestamp: int,
        signature: str,
        *,
        tran_id: int | None = None,
        asset: str | None = None,
        account_type: AccountType3OrStr | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AssetConvertTransferQueryByPageResponse:
        """Weight(UID): 5

        Args:
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            timestamp: UTC timestamp in ms
            signature: Signature
            tran_id: The transaction id
            asset: If it is blank, we will match deducted asset and target asset.
            account_type: MAIN: main account. CARD: funding account. If it is blank, we will query spot and card wallet,
                otherwise, we just query the corresponding wallet
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Query Convert Transfer

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_convert_transfer_user_data(
                start_time,
                end_time,
                timestamp,
                signature,
                tran_id=tran_id,
                asset=asset,
                account_type=account_type,
                current=current,
                size=size,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def query_user_delegation_history_for_master_account_user_data(
        self,
        email: str,
        start_time: int,
        end_time: int,
        asset: str,
        timestamp: int,
        signature: str,
        *,
        type_: str | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AssetCustodyTransferHistoryResponse:
        """Query User Delegation History

        Weight(IP): 60

        Args:
            email: Value sent with the request.
            start_time: Value sent with the request.
            end_time: Value sent with the request.
            asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            type_: Value sent with the request.
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Delegation History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_user_delegation_history_for_master_account_user_data(
                email,
                start_time,
                end_time,
                asset,
                timestamp,
                signature,
                type_=type_,
                current=current,
                size=size,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def query_user_universal_transfer_history_user_data(
        self,
        type_: Type7OrStr,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        from_symbol: str | None = None,
        to_symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AssetTransferResponse:
        """- ``fromSymbol`` must be sent when type are ISOLATEDMARGIN_MARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
        - ``toSymbol`` must be sent when type are MARGIN_ISOLATEDMARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
        - Support query within the last 6 months only
        - If ``startTime`` and ``endTime`` not sent, return records of the last 7 days by default

        Weight(IP): 1

        Args:
            type_: Universal transfer type
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            from_symbol: Must be sent when type are ISOLATEDMARGIN_MARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
            to_symbol: Must be sent when type are MARGIN_ISOLATEDMARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Universal transfer history

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_user_universal_transfer_history_user_data(
                type_,
                timestamp,
                signature,
                start_time=start_time,
                end_time=end_time,
                current=current,
                size=size,
                from_symbol=from_symbol,
                to_symbol=to_symbol,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def query_user_wallet_balance_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1AssetWalletBalanceResponse]:
        """Query User Wallet Balance

        Weight(IP): 60

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            wallet balance

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_user_wallet_balance_user_data(
                timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def query_auto_converting_stable_coins_user_data(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> SapiV1CapitalContractConvertibleCoinsResponse:
        """Get a user's auto-conversion settings in deposit/withdrawal

        Weight(UID): 600'

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            User's auto-conversion settings i

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_auto_converting_stable_coins_user_data(request_options=request_options)
        ).unwrap()

    async def switch_on_off_busd_and_stable_coins_conversion_user_data_user_data(
        self, coin: str, enable: bool, *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """User can use it to turn on or turn off the BUSD auto-conversion from/to a specific stable coin.

        Weight(UID): 600'

        Args:
            coin: Must be USDC, USDP or TUSD
            enable: true: turn on the auto-conversion. false: turn off the auto-conversion
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.switch_on_off_busd_and_stable_coins_conversion_user_data_user_data(
                coin, enable, request_options=request_options
            )
        ).unwrap()

    async def system_status_system(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> SapiV1SystemStatusResponse:
        """Fetch system status.

        Weight(IP): 1

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.system_status_system(request_options=request_options)).unwrap()

    async def trade_fee_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1AssetTradeFeeResponse]:
        """Fetch trade fee

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            symbol: Trading symbol, e.g. BNBUSDT
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Trade fee info per symbol

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.trade_fee_user_data(
                timestamp, signature, symbol=symbol, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def user_asset_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        need_btc_valuation: NeedBtcValuationOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV3AssetGetUserAssetResponse]:
        """Get user assets, just for positive data.

        Weight(IP): 5

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            need_btc_valuation: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            User assets

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.user_asset_user_data(
                timestamp,
                signature,
                asset=asset,
                need_btc_valuation=need_btc_valuation,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def user_universal_transfer_user_data(
        self,
        type_: Type7OrStr,
        asset: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        from_symbol: str | None = None,
        to_symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1AssetTransferResponse1:
        """You need to enable ``Permits Universal Transfer`` option for the api key which requests this endpoint.

        - ``fromSymbol`` must be sent when type are ISOLATEDMARGIN_MARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
        - ``toSymbol`` must be sent when type are MARGIN_ISOLATEDMARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN

        ENUM of transfer types:
          - MAIN_UMFUTURE Spot account transfer to USDⓈ-M Futures account
          - MAIN_CMFUTURE Spot account transfer to COIN-M Futures account
          - MAIN_MARGIN Spot account transfer to Margin(cross)account
          - UMFUTURE_MAIN USDⓈ-M Futures account transfer to Spot account
          - UMFUTURE_MARGIN USDⓈ-M Futures account transfer to Margin(cross)account
          - CMFUTURE_MAIN COIN-M Futures account transfer to Spot account
          - CMFUTURE_MARGIN COIN-M Futures account transfer to Margin(cross) account
          - MARGIN_MAIN Margin(cross)account transfer to Spot account
          - MARGIN_UMFUTURE Margin(cross)account transfer to USDⓈ-M Futures
          - MARGIN_CMFUTURE Margin(cross)account transfer to COIN-M Futures
          - ISOLATEDMARGIN_MARGIN Isolated margin account transfer to Margin(cross) account
          - MARGIN_ISOLATEDMARGIN Margin(cross) account transfer to Isolated margin account
          - ISOLATEDMARGIN_ISOLATEDMARGIN Isolated margin account transfer to Isolated margin account
          - MAIN_FUNDING Spot account transfer to Funding account
          - FUNDING_MAIN Funding account transfer to Spot account
          - FUNDING_UMFUTURE Funding account transfer to UMFUTURE account
          - UMFUTURE_FUNDING UMFUTURE account transfer to Funding account
          - MARGIN_FUNDING MARGIN account transfer to Funding account
          - FUNDING_MARGIN Funding account transfer to Margin account
          - FUNDING_CMFUTURE Funding account transfer to CMFUTURE account
          - CMFUTURE_FUNDING CMFUTURE account transfer to Funding account
          - MAIN_OPTION Spot account transfer to Options account
          - OPTION_MAIN Options account transfer to Spot account
          - UMFUTURE_OPTION USDⓈ-M Futures account transfer to Options account
          - OPTION_UMFUTURE Options account transfer to USDⓈ-M Futures account
          - MARGIN_OPTION Margin(cross)account transfer to Options account
          - OPTION_MARGIN Options account transfer to Margin(cross)account
          - FUNDING_OPTION Funding account transfer to Options account
          - OPTION_FUNDING Options account transfer to Funding account
          - MAIN_PORTFOLIO_MARGIN Spot account transfer to Portfolio Margin account
          - PORTFOLIO_MARGIN_MAIN Portfolio Margin account transfer to Spot account
          - MAIN_ISOLATED_MARGIN Spot account transfer to Isolated margin account
          - ISOLATED_MARGIN_MAIN Isolated margin account transfer to Spot account

        Weight(IP): 1

        Args:
            type_: Universal transfer type
            asset: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            from_symbol: Must be sent when type are ISOLATEDMARGIN_MARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
            to_symbol: Must be sent when type are MARGIN_ISOLATEDMARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Transfer id

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.user_universal_transfer_user_data(
                type_,
                asset,
                amount,
                timestamp,
                signature,
                from_symbol=from_symbol,
                to_symbol=to_symbol,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def withdraw_user_data(
        self,
        coin: str,
        address: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        withdraw_order_id: str | None = None,
        network: str | None = None,
        address_tag: str | None = None,
        transaction_fee_flag: bool | None = False,
        name: str | None = None,
        wallet_type: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1CapitalWithdrawApplyResponse:
        """Submit a withdraw request.

        - If ``network`` not send, return with default network of the coin.
        - You can get ``network`` and ``isDefault`` in ``networkList`` of a coin in the response of ``Get
            /sapi/v1/capital/config/getall (HMAC SHA256)``.

        Weight(IP): 1

        Args:
            coin: Coin name
            address: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            withdraw_order_id: Client id for withdraw
            network: Value sent with the request.
            address_tag: Secondary address identifier for coins like XRP,XMR etc.
            transaction_fee_flag: When making internal transfer - ``true`` -> returning the fee to the destination
                account; - ``false`` -> returning the fee back to the departure account.
            name: Value sent with the request.
            wallet_type: The wallet type for withdraw，0-Spot wallet, 1- Funding wallet. Default is Spot wallet
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Transafer Id

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.withdraw_user_data(
                coin,
                address,
                amount,
                timestamp,
                signature,
                withdraw_order_id=withdraw_order_id,
                network=network,
                address_tag=address_tag,
                transaction_fee_flag=transaction_fee_flag,
                name=name,
                wallet_type=wallet_type,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def withdraw_history_supporting_network_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        coin: str | None = None,
        withdraw_order_id: str | None = None,
        status: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        offset: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1CapitalWithdrawHistoryResponse]:
        """Fetch withdraw history.

        This endpoint specifically uses per second UID rate limit, user's total second level IP rate limit is
        180000/second. Response from the endpoint contains header key X-SAPI-USED-UID-WEIGHT-1S, which defines weight
        used by the current IP.

        - ``network`` may not be in the response for old withdraw.
        - Please notice the default ``startTime`` and ``endTime`` to make sure that time interval is within 0-90 days.
        - If both ``startTime`` and ``endTime`` are sent, time between ``startTime`` and ``endTime`` must be less than
            90 days
        - If withdrawOrderId is sent, time between startTime and endTime must be less than 7 days.
        - If withdrawOrderId is sent, startTime and endTime are not sent, will return last 7 days records by default.

        Weight(UID): 18000 Request Limit: 10 requests per second

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            coin: Coin name
            withdraw_order_id: Value sent with the request.
            status: * ``0`` - Email Sent * ``1`` - Cancelled * ``2`` - Awaiting Approval * ``3`` - Rejected * ``4`` -
                Processing * ``5`` - Failure * ``6`` - Completed
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            offset: Value sent with the request.
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of withdraw history

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.withdraw_history_supporting_network_user_data(
                timestamp,
                signature,
                coin=coin,
                withdraw_order_id=withdraw_order_id,
                status=status,
                start_time=start_time,
                end_time=end_time,
                offset=offset,
                limit=limit,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncWalletWithRawResponse:
        return self._with_raw_response


class WalletWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def account_api_trading_status_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AccountApiTradingStatusResponse, AccountApiTradingStatusUserDataErrorBody]:
        """Fetch account API trading status with details.

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
            url_template=self._server.default("/sapi/v1/account/apiTradingStatus"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AccountApiTradingStatusResponse],
            error_mapper=account_api_trading_status_user_data_error_mapper,
            request_options=request_options,
        )

    def account_status_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AccountStatusResponse, AccountStatusUserDataErrorBody]:
        """Fetch account status detail.

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
            url_template=self._server.default("/sapi/v1/account/status"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AccountStatusResponse],
            error_mapper=account_status_user_data_error_mapper,
            request_options=request_options,
        )

    def account_info_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AccountInfoResponse, AccountInfoUserDataErrorBody]:
        """Fetch account info detail.

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
            url_template=self._server.default("/sapi/v1/account/info"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AccountInfoResponse],
            error_mapper=account_info_user_data_error_mapper,
            request_options=request_options,
        )

    def all_coins_information_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1CapitalConfigGetallResponse], AllCoinsInformationUserDataErrorBody]:
        """Get information of coins (available for deposit and withdraw) for user.

        Weight(IP): 10

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/capital/config/getall"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1CapitalConfigGetallResponse]],
            error_mapper=all_coins_information_user_data_error_mapper,
            request_options=request_options,
        )

    def asset_detail_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AssetAssetDetailResponse, AssetDetailUserDataErrorBody]:
        """Fetch details of assets supported on Binance.

        - Please get network and other deposit or withdraw details from ``GET /sapi/v1/capital/config/getall``.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/asset/assetDetail"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("asset", asset),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AssetAssetDetailResponse],
            error_mapper=asset_detail_user_data_error_mapper,
            request_options=request_options,
        )

    def asset_dividend_record_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = 20,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AssetAssetDividendResponse, AssetDividendRecordUserDataErrorBody]:
        """Query asset Dividend Record

        Weight(IP): 10

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/asset/assetDividend"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("asset", asset),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AssetAssetDividendResponse],
            error_mapper=asset_dividend_record_user_data_error_mapper,
            request_options=request_options,
        )

    def convert_transfer_user_data(
        self,
        client_tran_id: str,
        asset: str,
        amount: float,
        target_asset: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AssetConvertTransferResponse, ConvertTransferUserDataErrorBody]:
        """Convert transfer, convert between BUSD and stablecoins. If the clientId has been used before, will not do the
        convert transfer, the original transfer will be returned.

        Weight(UID): 5

        Args:
            client_tran_id: The unique flag, the min length is 20
            asset: Value sent with the request.
            amount: Value sent with the request.
            target_asset: Target asset you want to convert
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/asset/convert-transfer"),
            query_params=[
                param[str]("clientTranId", client_tran_id),
                param[str]("asset", asset),
                param[float]("amount", amount),
                param[str]("targetAsset", target_asset),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AssetConvertTransferResponse],
            error_mapper=convert_transfer_user_data_error_mapper,
            request_options=request_options,
        )

    def daily_account_snapshot_user_data(
        self,
        type_: Type6OrStr,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = 7,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AccountSnapshotResponse, DailyAccountSnapshotUserDataErrorBody]:
        """- The query time period must be less than 30 days
        - Support query within the last one month only
        - If startTimeand endTime not sent, return records of the last 7 days by default

        Weight(IP): 2400

        Args:
            type_: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/accountSnapshot"),
            query_params=[
                param[Type6OrStr]("type", type_),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AccountSnapshotResponse],
            error_mapper=daily_account_snapshot_user_data_error_mapper,
            request_options=request_options,
        )

    def deposit_address_supporting_network_user_data(
        self,
        coin: str,
        timestamp: int,
        signature: str,
        *,
        network: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1CapitalDepositAddressResponse, DepositAddressSupportingNetworkUserDataErrorBody]:
        """Fetch deposit address with network.

        - If network is not send, return with default network of the coin.
        - You can get network and isDefault in networkList in the response of Get /sapi/v1/capital/config/getall (HMAC
            SHA256).

        Weight(IP): 10

        Args:
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
            url_template=self._server.default("/sapi/v1/capital/deposit/address"),
            query_params=[
                param[str]("coin", coin),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("network", network),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1CapitalDepositAddressResponse],
            error_mapper=deposit_address_supporting_network_user_data_error_mapper,
            request_options=request_options,
        )

    def deposit_history_supporting_network_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        coin: str | None = None,
        status: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        offset: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1CapitalDepositHisrecResponse], DepositHistorySupportingNetworkUserDataErrorBody]:
        """Fetch deposit history.

        - Please notice the default ``startTime`` and ``endTime`` to make sure that time interval is within 0-90 days.
        - If both ``startTime`` and ``endTime`` are sent, time between ``startTime`` and ``endTime`` must be less than
            90 days.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            coin: Coin name
            status: * ``0`` - pending * ``6`` - credited but cannot withdraw * ``1`` - success
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            offset: Value sent with the request.
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/capital/deposit/hisrec"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("coin", coin),
                param[int | None]("status", status),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("offset", offset),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1CapitalDepositHisrecResponse]],
            error_mapper=deposit_history_supporting_network_user_data_error_mapper,
            request_options=request_options,
        )

    def disable_fast_withdraw_switch_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, DisableFastWithdrawSwitchUserDataErrorBody]:
        """- This request will disable fastwithdraw switch under your account.
        - You need to enable "trade" option for the api key which requests this endpoint.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/account/disableFastWithdrawSwitch"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[Any],
            error_mapper=disable_fast_withdraw_switch_user_data_error_mapper,
            request_options=request_options,
        )

    def dust_transfer_user_data(
        self,
        asset: list[str],
        timestamp: int,
        signature: str,
        *,
        account_type: AccountTypeOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AssetDustResponse, DustTransferUserDataErrorBody]:
        """Convert dust assets to BNB.

        Weight(UID): 10

        Args:
            asset: The asset being converted. For example, asset=BTC&asset=USDT
            timestamp: UTC timestamp in ms
            signature: Signature
            account_type: SPOT or MARGIN, default SPOT
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/asset/dust"),
            query_params=[
                param[list[str]]("asset", asset),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[AccountTypeOrStr | None]("accountType", account_type),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AssetDustResponse],
            error_mapper=dust_transfer_user_data_error_mapper,
            request_options=request_options,
        )

    def dust_log_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        account_type: AccountTypeOrStr | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AssetDribbletResponse, DustLogUserDataErrorBody]:
        """Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            account_type: SPOT or MARGIN, default SPOT
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/asset/dribblet"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[AccountTypeOrStr | None]("accountType", account_type),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AssetDribbletResponse],
            error_mapper=dust_log_user_data_error_mapper,
            request_options=request_options,
        )

    def enable_fast_withdraw_switch_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, EnableFastWithdrawSwitchUserDataErrorBody]:
        """- This request will enable fastwithdraw switch under your account. You need to enable "trade" option for the
            api key which requests this endpoint.
        - When Fast Withdraw Switch is on, transferring funds to a Binance account will be done instantly. There is no
            on-chain transaction, no transaction ID and no withdrawal fee.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/account/enableFastWithdrawSwitch"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[Any],
            error_mapper=enable_fast_withdraw_switch_user_data_error_mapper,
            request_options=request_options,
        )

    def fetch_deposit_address_list_with_network_user_data(
        self,
        coin: str,
        timestamp: int,
        signature: str,
        *,
        network: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1CapitalDepositAddressListResponse], FetchDepositAddressListWithNetworkUserDataErrorBody]:
        """Fetch deposit address list with network.

        Weight(IP): 10

        Args:
            coin: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            network: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/capital/deposit/address/list"),
            query_params=[
                param[str]("coin", coin),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("network", network),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1CapitalDepositAddressListResponse]],
            error_mapper=fetch_deposit_address_list_with_network_user_data_error_mapper,
            request_options=request_options,
        )

    def fetch_withdraw_address_list_user_data(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[SapiV1CapitalWithdrawAddressListResponse], FetchWithdrawAddressListUserDataErrorBody]:
        """Fetch withdraw address list

        Weight(IP): 10

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/capital/withdraw/address/list"),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1CapitalWithdrawAddressListResponse]],
            error_mapper=fetch_withdraw_address_list_user_data_error_mapper,
            request_options=request_options,
        )

    def funding_wallet_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        need_btc_valuation: NeedBtcValuationOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1AssetGetFundingAssetResponse], FundingWalletUserDataErrorBody]:
        """- Currently supports querying the following business assets：Binance Pay, Binance Card, Binance Gift Card,
            Stock Token

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            need_btc_valuation: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/asset/get-funding-asset"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("asset", asset),
                param[NeedBtcValuationOrStr | None]("needBtcValuation", need_btc_valuation),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1AssetGetFundingAssetResponse]],
            error_mapper=funding_wallet_user_data_error_mapper,
            request_options=request_options,
        )

    def get_api_key_permission_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AccountApiRestrictionsResponse, GetApiKeyPermissionUserDataErrorBody]:
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
            url_template=self._server.default("/sapi/v1/account/apiRestrictions"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AccountApiRestrictionsResponse],
            error_mapper=get_api_key_permission_user_data_error_mapper,
            request_options=request_options,
        )

    def get_assets_that_can_be_converted_into_bnb_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        account_type: AccountTypeOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AssetDustBtcResponse, GetAssetsThatCanBeConvertedIntoBnbUserDataErrorBody]:
        """Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            account_type: SPOT or MARGIN, default SPOT
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/asset/dust-btc"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[AccountTypeOrStr | None]("accountType", account_type),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AssetDustBtcResponse],
            error_mapper=get_assets_that_can_be_converted_into_bnb_user_data_error_mapper,
            request_options=request_options,
        )

    def get_cloud_mining_payment_and_refund_history_user_data(
        self,
        start_time: int,
        end_time: int,
        timestamp: int,
        signature: str,
        *,
        tran_id: int | None = None,
        client_tran_id: str | None = None,
        asset: str | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1AssetLedgerTransferCloudMiningQueryByPageResponse, GetCloudMiningPaymentAndRefundHistoryUserDataErrorBody
    ]:
        """The query of Cloud-Mining payment and refund history

        Weight(UID): 600

        Args:
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            timestamp: UTC timestamp in ms
            signature: Signature
            tran_id: The transaction id
            client_tran_id: The unique flag
            asset: If it is blank, we will query all assets
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/asset/ledger-transfer/cloud-mining/queryByPage"),
            query_params=[
                param[int]("startTime", start_time),
                param[int]("endTime", end_time),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("tranId", tran_id),
                param[str | None]("clientTranId", client_tran_id),
                param[str | None]("asset", asset),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AssetLedgerTransferCloudMiningQueryByPageResponse],
            error_mapper=get_cloud_mining_payment_and_refund_history_user_data_error_mapper,
            request_options=request_options,
        )

    def get_symbols_delist_schedule_for_spot_market_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1SpotDelistScheduleResponse], GetSymbolsDelistScheduleForSpotMarketDataErrorBody]:
        """Get symbols delist schedule for spot

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
            url_template=self._server.default("/sapi/v1/spot/delist-schedule"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1SpotDelistScheduleResponse]],
            error_mapper=get_symbols_delist_schedule_for_spot_market_data_error_mapper,
            request_options=request_options,
        )

    def one_click_arrival_deposit_apply_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        deposit_id: int | None = None,
        tx_id: str | None = None,
        sub_account_id: int | None = None,
        sub_user_id: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1CapitalDepositCreditApplyResponse, OneClickArrivalDepositApplyUserDataErrorBody]:
        """Apply deposit credit for expired address (One click arrival)

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            deposit_id: Deposit record Id, priority use
            tx_id: Deposit txId, used when depositId is not specified
            sub_account_id: Value sent with the request.
            sub_user_id: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/capital/deposit/credit-apply"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("depositId", deposit_id),
                param[str | None]("txId", tx_id),
                param[int | None]("subAccountId", sub_account_id),
                param[int | None]("subUserId", sub_user_id),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1CapitalDepositCreditApplyResponse],
            error_mapper=one_click_arrival_deposit_apply_user_data_error_mapper,
            request_options=request_options,
        )

    def query_convert_transfer_user_data(
        self,
        start_time: int,
        end_time: int,
        timestamp: int,
        signature: str,
        *,
        tran_id: int | None = None,
        asset: str | None = None,
        account_type: AccountType3OrStr | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AssetConvertTransferQueryByPageResponse, QueryConvertTransferUserDataErrorBody]:
        """Weight(UID): 5

        Args:
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            timestamp: UTC timestamp in ms
            signature: Signature
            tran_id: The transaction id
            asset: If it is blank, we will match deducted asset and target asset.
            account_type: MAIN: main account. CARD: funding account. If it is blank, we will query spot and card wallet,
                otherwise, we just query the corresponding wallet
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/asset/convert-transfer/queryByPage"),
            query_params=[
                param[int]("startTime", start_time),
                param[int]("endTime", end_time),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("tranId", tran_id),
                param[str | None]("asset", asset),
                param[AccountType3OrStr | None]("accountType", account_type),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AssetConvertTransferQueryByPageResponse],
            error_mapper=query_convert_transfer_user_data_error_mapper,
            request_options=request_options,
        )

    def query_user_delegation_history_for_master_account_user_data(
        self,
        email: str,
        start_time: int,
        end_time: int,
        asset: str,
        timestamp: int,
        signature: str,
        *,
        type_: str | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1AssetCustodyTransferHistoryResponse, QueryUserDelegationHistoryForMasterAccountUserDataErrorBody
    ]:
        """Query User Delegation History

        Weight(IP): 60

        Args:
            email: Value sent with the request.
            start_time: Value sent with the request.
            end_time: Value sent with the request.
            asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            type_: Value sent with the request.
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/asset/custody/transfer-history"),
            query_params=[
                param[str]("email", email),
                param[int]("startTime", start_time),
                param[int]("endTime", end_time),
                param[str]("asset", asset),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("type", type_),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AssetCustodyTransferHistoryResponse],
            error_mapper=query_user_delegation_history_for_master_account_user_data_error_mapper,
            request_options=request_options,
        )

    def query_user_universal_transfer_history_user_data(
        self,
        type_: Type7OrStr,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        from_symbol: str | None = None,
        to_symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AssetTransferResponse, QueryUserUniversalTransferHistoryUserDataErrorBody]:
        """- ``fromSymbol`` must be sent when type are ISOLATEDMARGIN_MARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
        - ``toSymbol`` must be sent when type are MARGIN_ISOLATEDMARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
        - Support query within the last 6 months only
        - If ``startTime`` and ``endTime`` not sent, return records of the last 7 days by default

        Weight(IP): 1

        Args:
            type_: Universal transfer type
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            from_symbol: Must be sent when type are ISOLATEDMARGIN_MARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
            to_symbol: Must be sent when type are MARGIN_ISOLATEDMARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/asset/transfer"),
            query_params=[
                param[Type7OrStr]("type", type_),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[str | None]("fromSymbol", from_symbol),
                param[str | None]("toSymbol", to_symbol),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AssetTransferResponse],
            error_mapper=query_user_universal_transfer_history_user_data_error_mapper,
            request_options=request_options,
        )

    def query_user_wallet_balance_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1AssetWalletBalanceResponse], QueryUserWalletBalanceUserDataErrorBody]:
        """Query User Wallet Balance

        Weight(IP): 60

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/asset/wallet/balance"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1AssetWalletBalanceResponse]],
            error_mapper=query_user_wallet_balance_user_data_error_mapper,
            request_options=request_options,
        )

    def query_auto_converting_stable_coins_user_data(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SapiV1CapitalContractConvertibleCoinsResponse, QueryAutoConvertingStableCoinsUserDataErrorBody]:
        """Get a user's auto-conversion settings in deposit/withdrawal

        Weight(UID): 600'

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/capital/contract/convertible-coins"),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1CapitalContractConvertibleCoinsResponse],
            error_mapper=query_auto_converting_stable_coins_user_data_error_mapper,
            request_options=request_options,
        )

    def switch_on_off_busd_and_stable_coins_conversion_user_data_user_data(
        self, coin: str, enable: bool, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, SwitchOnOffBusdAndStableCoinsConversionUserDataUserDataErrorBody]:
        """User can use it to turn on or turn off the BUSD auto-conversion from/to a specific stable coin.

        Weight(UID): 600'

        Args:
            coin: Must be USDC, USDP or TUSD
            enable: true: turn on the auto-conversion. false: turn off the auto-conversion
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/capital/contract/convertible-coins"),
            query_params=[param[str]("coin", coin), param[bool]("enable", enable)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[Any],
            error_mapper=switch_on_off_busd_and_stable_coins_conversion_user_data_user_data_error_mapper,
            request_options=request_options,
        )

    def system_status_system(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SapiV1SystemStatusResponse, RawError]:
        """Fetch system status.

        Weight(IP): 1

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/system/status"),
            decoder=json_decoder[SapiV1SystemStatusResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def trade_fee_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1AssetTradeFeeResponse], TradeFeeUserDataErrorBody]:
        """Fetch trade fee

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            symbol: Trading symbol, e.g. BNBUSDT
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/asset/tradeFee"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("symbol", symbol),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1AssetTradeFeeResponse]],
            error_mapper=trade_fee_user_data_error_mapper,
            request_options=request_options,
        )

    def user_asset_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        need_btc_valuation: NeedBtcValuationOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV3AssetGetUserAssetResponse], UserAssetUserDataErrorBody]:
        """Get user assets, just for positive data.

        Weight(IP): 5

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            need_btc_valuation: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v3/asset/getUserAsset"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("asset", asset),
                param[NeedBtcValuationOrStr | None]("needBtcValuation", need_btc_valuation),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV3AssetGetUserAssetResponse]],
            error_mapper=user_asset_user_data_error_mapper,
            request_options=request_options,
        )

    def user_universal_transfer_user_data(
        self,
        type_: Type7OrStr,
        asset: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        from_symbol: str | None = None,
        to_symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AssetTransferResponse1, UserUniversalTransferUserDataErrorBody]:
        """You need to enable ``Permits Universal Transfer`` option for the api key which requests this endpoint.

        - ``fromSymbol`` must be sent when type are ISOLATEDMARGIN_MARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
        - ``toSymbol`` must be sent when type are MARGIN_ISOLATEDMARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN

        ENUM of transfer types:
          - MAIN_UMFUTURE Spot account transfer to USDⓈ-M Futures account
          - MAIN_CMFUTURE Spot account transfer to COIN-M Futures account
          - MAIN_MARGIN Spot account transfer to Margin(cross)account
          - UMFUTURE_MAIN USDⓈ-M Futures account transfer to Spot account
          - UMFUTURE_MARGIN USDⓈ-M Futures account transfer to Margin(cross)account
          - CMFUTURE_MAIN COIN-M Futures account transfer to Spot account
          - CMFUTURE_MARGIN COIN-M Futures account transfer to Margin(cross) account
          - MARGIN_MAIN Margin(cross)account transfer to Spot account
          - MARGIN_UMFUTURE Margin(cross)account transfer to USDⓈ-M Futures
          - MARGIN_CMFUTURE Margin(cross)account transfer to COIN-M Futures
          - ISOLATEDMARGIN_MARGIN Isolated margin account transfer to Margin(cross) account
          - MARGIN_ISOLATEDMARGIN Margin(cross) account transfer to Isolated margin account
          - ISOLATEDMARGIN_ISOLATEDMARGIN Isolated margin account transfer to Isolated margin account
          - MAIN_FUNDING Spot account transfer to Funding account
          - FUNDING_MAIN Funding account transfer to Spot account
          - FUNDING_UMFUTURE Funding account transfer to UMFUTURE account
          - UMFUTURE_FUNDING UMFUTURE account transfer to Funding account
          - MARGIN_FUNDING MARGIN account transfer to Funding account
          - FUNDING_MARGIN Funding account transfer to Margin account
          - FUNDING_CMFUTURE Funding account transfer to CMFUTURE account
          - CMFUTURE_FUNDING CMFUTURE account transfer to Funding account
          - MAIN_OPTION Spot account transfer to Options account
          - OPTION_MAIN Options account transfer to Spot account
          - UMFUTURE_OPTION USDⓈ-M Futures account transfer to Options account
          - OPTION_UMFUTURE Options account transfer to USDⓈ-M Futures account
          - MARGIN_OPTION Margin(cross)account transfer to Options account
          - OPTION_MARGIN Options account transfer to Margin(cross)account
          - FUNDING_OPTION Funding account transfer to Options account
          - OPTION_FUNDING Options account transfer to Funding account
          - MAIN_PORTFOLIO_MARGIN Spot account transfer to Portfolio Margin account
          - PORTFOLIO_MARGIN_MAIN Portfolio Margin account transfer to Spot account
          - MAIN_ISOLATED_MARGIN Spot account transfer to Isolated margin account
          - ISOLATED_MARGIN_MAIN Isolated margin account transfer to Spot account

        Weight(IP): 1

        Args:
            type_: Universal transfer type
            asset: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            from_symbol: Must be sent when type are ISOLATEDMARGIN_MARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
            to_symbol: Must be sent when type are MARGIN_ISOLATEDMARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/asset/transfer"),
            query_params=[
                param[Type7OrStr]("type", type_),
                param[str]("asset", asset),
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("fromSymbol", from_symbol),
                param[str | None]("toSymbol", to_symbol),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AssetTransferResponse1],
            error_mapper=user_universal_transfer_user_data_error_mapper,
            request_options=request_options,
        )

    def withdraw_user_data(
        self,
        coin: str,
        address: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        withdraw_order_id: str | None = None,
        network: str | None = None,
        address_tag: str | None = None,
        transaction_fee_flag: bool | None = False,
        name: str | None = None,
        wallet_type: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1CapitalWithdrawApplyResponse, WithdrawUserDataErrorBody]:
        """Submit a withdraw request.

        - If ``network`` not send, return with default network of the coin.
        - You can get ``network`` and ``isDefault`` in ``networkList`` of a coin in the response of ``Get
            /sapi/v1/capital/config/getall (HMAC SHA256)``.

        Weight(IP): 1

        Args:
            coin: Coin name
            address: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            withdraw_order_id: Client id for withdraw
            network: Value sent with the request.
            address_tag: Secondary address identifier for coins like XRP,XMR etc.
            transaction_fee_flag: When making internal transfer - ``true`` -> returning the fee to the destination
                account; - ``false`` -> returning the fee back to the departure account.
            name: Value sent with the request.
            wallet_type: The wallet type for withdraw，0-Spot wallet, 1- Funding wallet. Default is Spot wallet
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/capital/withdraw/apply"),
            query_params=[
                param[str]("coin", coin),
                param[str]("address", address),
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("withdrawOrderId", withdraw_order_id),
                param[str | None]("network", network),
                param[str | None]("addressTag", address_tag),
                param[bool | None]("transactionFeeFlag", transaction_fee_flag),
                param[str | None]("name", name),
                param[int | None]("walletType", wallet_type),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1CapitalWithdrawApplyResponse],
            error_mapper=withdraw_user_data_error_mapper,
            request_options=request_options,
        )

    def withdraw_history_supporting_network_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        coin: str | None = None,
        withdraw_order_id: str | None = None,
        status: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        offset: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1CapitalWithdrawHistoryResponse], WithdrawHistorySupportingNetworkUserDataErrorBody]:
        """Fetch withdraw history.

        This endpoint specifically uses per second UID rate limit, user's total second level IP rate limit is
        180000/second. Response from the endpoint contains header key X-SAPI-USED-UID-WEIGHT-1S, which defines weight
        used by the current IP.

        - ``network`` may not be in the response for old withdraw.
        - Please notice the default ``startTime`` and ``endTime`` to make sure that time interval is within 0-90 days.
        - If both ``startTime`` and ``endTime`` are sent, time between ``startTime`` and ``endTime`` must be less than
            90 days
        - If withdrawOrderId is sent, time between startTime and endTime must be less than 7 days.
        - If withdrawOrderId is sent, startTime and endTime are not sent, will return last 7 days records by default.

        Weight(UID): 18000 Request Limit: 10 requests per second

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            coin: Coin name
            withdraw_order_id: Value sent with the request.
            status: * ``0`` - Email Sent * ``1`` - Cancelled * ``2`` - Awaiting Approval * ``3`` - Rejected * ``4`` -
                Processing * ``5`` - Failure * ``6`` - Completed
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            offset: Value sent with the request.
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/capital/withdraw/history"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("coin", coin),
                param[str | None]("withdrawOrderId", withdraw_order_id),
                param[int | None]("status", status),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("offset", offset),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1CapitalWithdrawHistoryResponse]],
            error_mapper=withdraw_history_supporting_network_user_data_error_mapper,
            request_options=request_options,
        )


class AsyncWalletWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def account_api_trading_status_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AccountApiTradingStatusResponse, AccountApiTradingStatusUserDataErrorBody]:
        """Fetch account API trading status with details.

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
            url_template=self._server.default("/sapi/v1/account/apiTradingStatus"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AccountApiTradingStatusResponse],
            error_mapper=account_api_trading_status_user_data_error_mapper,
            request_options=request_options,
        )

    async def account_status_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AccountStatusResponse, AccountStatusUserDataErrorBody]:
        """Fetch account status detail.

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
            url_template=self._server.default("/sapi/v1/account/status"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AccountStatusResponse],
            error_mapper=account_status_user_data_error_mapper,
            request_options=request_options,
        )

    async def account_info_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AccountInfoResponse, AccountInfoUserDataErrorBody]:
        """Fetch account info detail.

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
            url_template=self._server.default("/sapi/v1/account/info"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AccountInfoResponse],
            error_mapper=account_info_user_data_error_mapper,
            request_options=request_options,
        )

    async def all_coins_information_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1CapitalConfigGetallResponse], AllCoinsInformationUserDataErrorBody]:
        """Get information of coins (available for deposit and withdraw) for user.

        Weight(IP): 10

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/capital/config/getall"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1CapitalConfigGetallResponse]],
            error_mapper=all_coins_information_user_data_error_mapper,
            request_options=request_options,
        )

    async def asset_detail_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AssetAssetDetailResponse, AssetDetailUserDataErrorBody]:
        """Fetch details of assets supported on Binance.

        - Please get network and other deposit or withdraw details from ``GET /sapi/v1/capital/config/getall``.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/asset/assetDetail"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("asset", asset),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AssetAssetDetailResponse],
            error_mapper=asset_detail_user_data_error_mapper,
            request_options=request_options,
        )

    async def asset_dividend_record_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = 20,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AssetAssetDividendResponse, AssetDividendRecordUserDataErrorBody]:
        """Query asset Dividend Record

        Weight(IP): 10

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/asset/assetDividend"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("asset", asset),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AssetAssetDividendResponse],
            error_mapper=asset_dividend_record_user_data_error_mapper,
            request_options=request_options,
        )

    async def convert_transfer_user_data(
        self,
        client_tran_id: str,
        asset: str,
        amount: float,
        target_asset: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AssetConvertTransferResponse, ConvertTransferUserDataErrorBody]:
        """Convert transfer, convert between BUSD and stablecoins. If the clientId has been used before, will not do the
        convert transfer, the original transfer will be returned.

        Weight(UID): 5

        Args:
            client_tran_id: The unique flag, the min length is 20
            asset: Value sent with the request.
            amount: Value sent with the request.
            target_asset: Target asset you want to convert
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/asset/convert-transfer"),
            query_params=[
                param[str]("clientTranId", client_tran_id),
                param[str]("asset", asset),
                param[float]("amount", amount),
                param[str]("targetAsset", target_asset),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AssetConvertTransferResponse],
            error_mapper=convert_transfer_user_data_error_mapper,
            request_options=request_options,
        )

    async def daily_account_snapshot_user_data(
        self,
        type_: Type6OrStr,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = 7,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AccountSnapshotResponse, DailyAccountSnapshotUserDataErrorBody]:
        """- The query time period must be less than 30 days
        - Support query within the last one month only
        - If startTimeand endTime not sent, return records of the last 7 days by default

        Weight(IP): 2400

        Args:
            type_: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/accountSnapshot"),
            query_params=[
                param[Type6OrStr]("type", type_),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AccountSnapshotResponse],
            error_mapper=daily_account_snapshot_user_data_error_mapper,
            request_options=request_options,
        )

    async def deposit_address_supporting_network_user_data(
        self,
        coin: str,
        timestamp: int,
        signature: str,
        *,
        network: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1CapitalDepositAddressResponse, DepositAddressSupportingNetworkUserDataErrorBody]:
        """Fetch deposit address with network.

        - If network is not send, return with default network of the coin.
        - You can get network and isDefault in networkList in the response of Get /sapi/v1/capital/config/getall (HMAC
            SHA256).

        Weight(IP): 10

        Args:
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
            url_template=self._server.default("/sapi/v1/capital/deposit/address"),
            query_params=[
                param[str]("coin", coin),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("network", network),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1CapitalDepositAddressResponse],
            error_mapper=deposit_address_supporting_network_user_data_error_mapper,
            request_options=request_options,
        )

    async def deposit_history_supporting_network_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        coin: str | None = None,
        status: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        offset: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1CapitalDepositHisrecResponse], DepositHistorySupportingNetworkUserDataErrorBody]:
        """Fetch deposit history.

        - Please notice the default ``startTime`` and ``endTime`` to make sure that time interval is within 0-90 days.
        - If both ``startTime`` and ``endTime`` are sent, time between ``startTime`` and ``endTime`` must be less than
            90 days.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            coin: Coin name
            status: * ``0`` - pending * ``6`` - credited but cannot withdraw * ``1`` - success
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            offset: Value sent with the request.
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/capital/deposit/hisrec"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("coin", coin),
                param[int | None]("status", status),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("offset", offset),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1CapitalDepositHisrecResponse]],
            error_mapper=deposit_history_supporting_network_user_data_error_mapper,
            request_options=request_options,
        )

    async def disable_fast_withdraw_switch_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, DisableFastWithdrawSwitchUserDataErrorBody]:
        """- This request will disable fastwithdraw switch under your account.
        - You need to enable "trade" option for the api key which requests this endpoint.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/account/disableFastWithdrawSwitch"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[Any],
            error_mapper=disable_fast_withdraw_switch_user_data_error_mapper,
            request_options=request_options,
        )

    async def dust_transfer_user_data(
        self,
        asset: list[str],
        timestamp: int,
        signature: str,
        *,
        account_type: AccountTypeOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AssetDustResponse, DustTransferUserDataErrorBody]:
        """Convert dust assets to BNB.

        Weight(UID): 10

        Args:
            asset: The asset being converted. For example, asset=BTC&asset=USDT
            timestamp: UTC timestamp in ms
            signature: Signature
            account_type: SPOT or MARGIN, default SPOT
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/asset/dust"),
            query_params=[
                param[list[str]]("asset", asset),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[AccountTypeOrStr | None]("accountType", account_type),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AssetDustResponse],
            error_mapper=dust_transfer_user_data_error_mapper,
            request_options=request_options,
        )

    async def dust_log_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        account_type: AccountTypeOrStr | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AssetDribbletResponse, DustLogUserDataErrorBody]:
        """Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            account_type: SPOT or MARGIN, default SPOT
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/asset/dribblet"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[AccountTypeOrStr | None]("accountType", account_type),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AssetDribbletResponse],
            error_mapper=dust_log_user_data_error_mapper,
            request_options=request_options,
        )

    async def enable_fast_withdraw_switch_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, EnableFastWithdrawSwitchUserDataErrorBody]:
        """- This request will enable fastwithdraw switch under your account. You need to enable "trade" option for the
            api key which requests this endpoint.
        - When Fast Withdraw Switch is on, transferring funds to a Binance account will be done instantly. There is no
            on-chain transaction, no transaction ID and no withdrawal fee.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/account/enableFastWithdrawSwitch"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[Any],
            error_mapper=enable_fast_withdraw_switch_user_data_error_mapper,
            request_options=request_options,
        )

    async def fetch_deposit_address_list_with_network_user_data(
        self,
        coin: str,
        timestamp: int,
        signature: str,
        *,
        network: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1CapitalDepositAddressListResponse], FetchDepositAddressListWithNetworkUserDataErrorBody]:
        """Fetch deposit address list with network.

        Weight(IP): 10

        Args:
            coin: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            network: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/capital/deposit/address/list"),
            query_params=[
                param[str]("coin", coin),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("network", network),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1CapitalDepositAddressListResponse]],
            error_mapper=fetch_deposit_address_list_with_network_user_data_error_mapper,
            request_options=request_options,
        )

    async def fetch_withdraw_address_list_user_data(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[SapiV1CapitalWithdrawAddressListResponse], FetchWithdrawAddressListUserDataErrorBody]:
        """Fetch withdraw address list

        Weight(IP): 10

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/capital/withdraw/address/list"),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1CapitalWithdrawAddressListResponse]],
            error_mapper=fetch_withdraw_address_list_user_data_error_mapper,
            request_options=request_options,
        )

    async def funding_wallet_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        need_btc_valuation: NeedBtcValuationOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1AssetGetFundingAssetResponse], FundingWalletUserDataErrorBody]:
        """- Currently supports querying the following business assets：Binance Pay, Binance Card, Binance Gift Card,
            Stock Token

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            need_btc_valuation: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/asset/get-funding-asset"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("asset", asset),
                param[NeedBtcValuationOrStr | None]("needBtcValuation", need_btc_valuation),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1AssetGetFundingAssetResponse]],
            error_mapper=funding_wallet_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_api_key_permission_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AccountApiRestrictionsResponse, GetApiKeyPermissionUserDataErrorBody]:
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
            url_template=self._server.default("/sapi/v1/account/apiRestrictions"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AccountApiRestrictionsResponse],
            error_mapper=get_api_key_permission_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_assets_that_can_be_converted_into_bnb_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        account_type: AccountTypeOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AssetDustBtcResponse, GetAssetsThatCanBeConvertedIntoBnbUserDataErrorBody]:
        """Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            account_type: SPOT or MARGIN, default SPOT
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/asset/dust-btc"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[AccountTypeOrStr | None]("accountType", account_type),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AssetDustBtcResponse],
            error_mapper=get_assets_that_can_be_converted_into_bnb_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_cloud_mining_payment_and_refund_history_user_data(
        self,
        start_time: int,
        end_time: int,
        timestamp: int,
        signature: str,
        *,
        tran_id: int | None = None,
        client_tran_id: str | None = None,
        asset: str | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1AssetLedgerTransferCloudMiningQueryByPageResponse, GetCloudMiningPaymentAndRefundHistoryUserDataErrorBody
    ]:
        """The query of Cloud-Mining payment and refund history

        Weight(UID): 600

        Args:
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            timestamp: UTC timestamp in ms
            signature: Signature
            tran_id: The transaction id
            client_tran_id: The unique flag
            asset: If it is blank, we will query all assets
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/asset/ledger-transfer/cloud-mining/queryByPage"),
            query_params=[
                param[int]("startTime", start_time),
                param[int]("endTime", end_time),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("tranId", tran_id),
                param[str | None]("clientTranId", client_tran_id),
                param[str | None]("asset", asset),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AssetLedgerTransferCloudMiningQueryByPageResponse],
            error_mapper=get_cloud_mining_payment_and_refund_history_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_symbols_delist_schedule_for_spot_market_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1SpotDelistScheduleResponse], GetSymbolsDelistScheduleForSpotMarketDataErrorBody]:
        """Get symbols delist schedule for spot

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
            url_template=self._server.default("/sapi/v1/spot/delist-schedule"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1SpotDelistScheduleResponse]],
            error_mapper=get_symbols_delist_schedule_for_spot_market_data_error_mapper,
            request_options=request_options,
        )

    async def one_click_arrival_deposit_apply_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        deposit_id: int | None = None,
        tx_id: str | None = None,
        sub_account_id: int | None = None,
        sub_user_id: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1CapitalDepositCreditApplyResponse, OneClickArrivalDepositApplyUserDataErrorBody]:
        """Apply deposit credit for expired address (One click arrival)

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            deposit_id: Deposit record Id, priority use
            tx_id: Deposit txId, used when depositId is not specified
            sub_account_id: Value sent with the request.
            sub_user_id: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/capital/deposit/credit-apply"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("depositId", deposit_id),
                param[str | None]("txId", tx_id),
                param[int | None]("subAccountId", sub_account_id),
                param[int | None]("subUserId", sub_user_id),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1CapitalDepositCreditApplyResponse],
            error_mapper=one_click_arrival_deposit_apply_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_convert_transfer_user_data(
        self,
        start_time: int,
        end_time: int,
        timestamp: int,
        signature: str,
        *,
        tran_id: int | None = None,
        asset: str | None = None,
        account_type: AccountType3OrStr | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AssetConvertTransferQueryByPageResponse, QueryConvertTransferUserDataErrorBody]:
        """Weight(UID): 5

        Args:
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            timestamp: UTC timestamp in ms
            signature: Signature
            tran_id: The transaction id
            asset: If it is blank, we will match deducted asset and target asset.
            account_type: MAIN: main account. CARD: funding account. If it is blank, we will query spot and card wallet,
                otherwise, we just query the corresponding wallet
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/asset/convert-transfer/queryByPage"),
            query_params=[
                param[int]("startTime", start_time),
                param[int]("endTime", end_time),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("tranId", tran_id),
                param[str | None]("asset", asset),
                param[AccountType3OrStr | None]("accountType", account_type),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AssetConvertTransferQueryByPageResponse],
            error_mapper=query_convert_transfer_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_user_delegation_history_for_master_account_user_data(
        self,
        email: str,
        start_time: int,
        end_time: int,
        asset: str,
        timestamp: int,
        signature: str,
        *,
        type_: str | None = None,
        current: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SapiV1AssetCustodyTransferHistoryResponse, QueryUserDelegationHistoryForMasterAccountUserDataErrorBody
    ]:
        """Query User Delegation History

        Weight(IP): 60

        Args:
            email: Value sent with the request.
            start_time: Value sent with the request.
            end_time: Value sent with the request.
            asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            type_: Value sent with the request.
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/asset/custody/transfer-history"),
            query_params=[
                param[str]("email", email),
                param[int]("startTime", start_time),
                param[int]("endTime", end_time),
                param[str]("asset", asset),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("type", type_),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AssetCustodyTransferHistoryResponse],
            error_mapper=query_user_delegation_history_for_master_account_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_user_universal_transfer_history_user_data(
        self,
        type_: Type7OrStr,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        current: int | None = None,
        size: int | None = None,
        from_symbol: str | None = None,
        to_symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AssetTransferResponse, QueryUserUniversalTransferHistoryUserDataErrorBody]:
        """- ``fromSymbol`` must be sent when type are ISOLATEDMARGIN_MARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
        - ``toSymbol`` must be sent when type are MARGIN_ISOLATEDMARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
        - Support query within the last 6 months only
        - If ``startTime`` and ``endTime`` not sent, return records of the last 7 days by default

        Weight(IP): 1

        Args:
            type_: Universal transfer type
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            current: Current querying page. Start from 1. Default:1
            size: Default:10 Max:100
            from_symbol: Must be sent when type are ISOLATEDMARGIN_MARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
            to_symbol: Must be sent when type are MARGIN_ISOLATEDMARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/asset/transfer"),
            query_params=[
                param[Type7OrStr]("type", type_),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("current", current),
                param[int | None]("size", size),
                param[str | None]("fromSymbol", from_symbol),
                param[str | None]("toSymbol", to_symbol),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AssetTransferResponse],
            error_mapper=query_user_universal_transfer_history_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_user_wallet_balance_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1AssetWalletBalanceResponse], QueryUserWalletBalanceUserDataErrorBody]:
        """Query User Wallet Balance

        Weight(IP): 60

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/asset/wallet/balance"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1AssetWalletBalanceResponse]],
            error_mapper=query_user_wallet_balance_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_auto_converting_stable_coins_user_data(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SapiV1CapitalContractConvertibleCoinsResponse, QueryAutoConvertingStableCoinsUserDataErrorBody]:
        """Get a user's auto-conversion settings in deposit/withdrawal

        Weight(UID): 600'

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/capital/contract/convertible-coins"),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1CapitalContractConvertibleCoinsResponse],
            error_mapper=query_auto_converting_stable_coins_user_data_error_mapper,
            request_options=request_options,
        )

    async def switch_on_off_busd_and_stable_coins_conversion_user_data_user_data(
        self, coin: str, enable: bool, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, SwitchOnOffBusdAndStableCoinsConversionUserDataUserDataErrorBody]:
        """User can use it to turn on or turn off the BUSD auto-conversion from/to a specific stable coin.

        Weight(UID): 600'

        Args:
            coin: Must be USDC, USDP or TUSD
            enable: true: turn on the auto-conversion. false: turn off the auto-conversion
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/capital/contract/convertible-coins"),
            query_params=[param[str]("coin", coin), param[bool]("enable", enable)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[Any],
            error_mapper=switch_on_off_busd_and_stable_coins_conversion_user_data_user_data_error_mapper,
            request_options=request_options,
        )

    async def system_status_system(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SapiV1SystemStatusResponse, RawError]:
        """Fetch system status.

        Weight(IP): 1

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/system/status"),
            decoder=json_decoder[SapiV1SystemStatusResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def trade_fee_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1AssetTradeFeeResponse], TradeFeeUserDataErrorBody]:
        """Fetch trade fee

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            symbol: Trading symbol, e.g. BNBUSDT
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/asset/tradeFee"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("symbol", symbol),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1AssetTradeFeeResponse]],
            error_mapper=trade_fee_user_data_error_mapper,
            request_options=request_options,
        )

    async def user_asset_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        need_btc_valuation: NeedBtcValuationOrStr | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV3AssetGetUserAssetResponse], UserAssetUserDataErrorBody]:
        """Get user assets, just for positive data.

        Weight(IP): 5

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: Value sent with the request.
            need_btc_valuation: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v3/asset/getUserAsset"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("asset", asset),
                param[NeedBtcValuationOrStr | None]("needBtcValuation", need_btc_valuation),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV3AssetGetUserAssetResponse]],
            error_mapper=user_asset_user_data_error_mapper,
            request_options=request_options,
        )

    async def user_universal_transfer_user_data(
        self,
        type_: Type7OrStr,
        asset: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        from_symbol: str | None = None,
        to_symbol: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1AssetTransferResponse1, UserUniversalTransferUserDataErrorBody]:
        """You need to enable ``Permits Universal Transfer`` option for the api key which requests this endpoint.

        - ``fromSymbol`` must be sent when type are ISOLATEDMARGIN_MARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
        - ``toSymbol`` must be sent when type are MARGIN_ISOLATEDMARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN

        ENUM of transfer types:
          - MAIN_UMFUTURE Spot account transfer to USDⓈ-M Futures account
          - MAIN_CMFUTURE Spot account transfer to COIN-M Futures account
          - MAIN_MARGIN Spot account transfer to Margin(cross)account
          - UMFUTURE_MAIN USDⓈ-M Futures account transfer to Spot account
          - UMFUTURE_MARGIN USDⓈ-M Futures account transfer to Margin(cross)account
          - CMFUTURE_MAIN COIN-M Futures account transfer to Spot account
          - CMFUTURE_MARGIN COIN-M Futures account transfer to Margin(cross) account
          - MARGIN_MAIN Margin(cross)account transfer to Spot account
          - MARGIN_UMFUTURE Margin(cross)account transfer to USDⓈ-M Futures
          - MARGIN_CMFUTURE Margin(cross)account transfer to COIN-M Futures
          - ISOLATEDMARGIN_MARGIN Isolated margin account transfer to Margin(cross) account
          - MARGIN_ISOLATEDMARGIN Margin(cross) account transfer to Isolated margin account
          - ISOLATEDMARGIN_ISOLATEDMARGIN Isolated margin account transfer to Isolated margin account
          - MAIN_FUNDING Spot account transfer to Funding account
          - FUNDING_MAIN Funding account transfer to Spot account
          - FUNDING_UMFUTURE Funding account transfer to UMFUTURE account
          - UMFUTURE_FUNDING UMFUTURE account transfer to Funding account
          - MARGIN_FUNDING MARGIN account transfer to Funding account
          - FUNDING_MARGIN Funding account transfer to Margin account
          - FUNDING_CMFUTURE Funding account transfer to CMFUTURE account
          - CMFUTURE_FUNDING CMFUTURE account transfer to Funding account
          - MAIN_OPTION Spot account transfer to Options account
          - OPTION_MAIN Options account transfer to Spot account
          - UMFUTURE_OPTION USDⓈ-M Futures account transfer to Options account
          - OPTION_UMFUTURE Options account transfer to USDⓈ-M Futures account
          - MARGIN_OPTION Margin(cross)account transfer to Options account
          - OPTION_MARGIN Options account transfer to Margin(cross)account
          - FUNDING_OPTION Funding account transfer to Options account
          - OPTION_FUNDING Options account transfer to Funding account
          - MAIN_PORTFOLIO_MARGIN Spot account transfer to Portfolio Margin account
          - PORTFOLIO_MARGIN_MAIN Portfolio Margin account transfer to Spot account
          - MAIN_ISOLATED_MARGIN Spot account transfer to Isolated margin account
          - ISOLATED_MARGIN_MAIN Isolated margin account transfer to Spot account

        Weight(IP): 1

        Args:
            type_: Universal transfer type
            asset: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            from_symbol: Must be sent when type are ISOLATEDMARGIN_MARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
            to_symbol: Must be sent when type are MARGIN_ISOLATEDMARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/asset/transfer"),
            query_params=[
                param[Type7OrStr]("type", type_),
                param[str]("asset", asset),
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("fromSymbol", from_symbol),
                param[str | None]("toSymbol", to_symbol),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1AssetTransferResponse1],
            error_mapper=user_universal_transfer_user_data_error_mapper,
            request_options=request_options,
        )

    async def withdraw_user_data(
        self,
        coin: str,
        address: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        withdraw_order_id: str | None = None,
        network: str | None = None,
        address_tag: str | None = None,
        transaction_fee_flag: bool | None = False,
        name: str | None = None,
        wallet_type: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1CapitalWithdrawApplyResponse, WithdrawUserDataErrorBody]:
        """Submit a withdraw request.

        - If ``network`` not send, return with default network of the coin.
        - You can get ``network`` and ``isDefault`` in ``networkList`` of a coin in the response of ``Get
            /sapi/v1/capital/config/getall (HMAC SHA256)``.

        Weight(IP): 1

        Args:
            coin: Coin name
            address: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            withdraw_order_id: Client id for withdraw
            network: Value sent with the request.
            address_tag: Secondary address identifier for coins like XRP,XMR etc.
            transaction_fee_flag: When making internal transfer - ``true`` -> returning the fee to the destination
                account; - ``false`` -> returning the fee back to the departure account.
            name: Value sent with the request.
            wallet_type: The wallet type for withdraw，0-Spot wallet, 1- Funding wallet. Default is Spot wallet
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/capital/withdraw/apply"),
            query_params=[
                param[str]("coin", coin),
                param[str]("address", address),
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("withdrawOrderId", withdraw_order_id),
                param[str | None]("network", network),
                param[str | None]("addressTag", address_tag),
                param[bool | None]("transactionFeeFlag", transaction_fee_flag),
                param[str | None]("name", name),
                param[int | None]("walletType", wallet_type),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1CapitalWithdrawApplyResponse],
            error_mapper=withdraw_user_data_error_mapper,
            request_options=request_options,
        )

    async def withdraw_history_supporting_network_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        coin: str | None = None,
        withdraw_order_id: str | None = None,
        status: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        offset: int | None = None,
        limit: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SapiV1CapitalWithdrawHistoryResponse], WithdrawHistorySupportingNetworkUserDataErrorBody]:
        """Fetch withdraw history.

        This endpoint specifically uses per second UID rate limit, user's total second level IP rate limit is
        180000/second. Response from the endpoint contains header key X-SAPI-USED-UID-WEIGHT-1S, which defines weight
        used by the current IP.

        - ``network`` may not be in the response for old withdraw.
        - Please notice the default ``startTime`` and ``endTime`` to make sure that time interval is within 0-90 days.
        - If both ``startTime`` and ``endTime`` are sent, time between ``startTime`` and ``endTime`` must be less than
            90 days
        - If withdrawOrderId is sent, time between startTime and endTime must be less than 7 days.
        - If withdrawOrderId is sent, startTime and endTime are not sent, will return last 7 days records by default.

        Weight(UID): 18000 Request Limit: 10 requests per second

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            coin: Coin name
            withdraw_order_id: Value sent with the request.
            status: * ``0`` - Email Sent * ``1`` - Cancelled * ``2`` - Awaiting Approval * ``3`` - Rejected * ``4`` -
                Processing * ``5`` - Failure * ``6`` - Completed
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            offset: Value sent with the request.
            limit: Default 500; max 1000.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/capital/withdraw/history"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("coin", coin),
                param[str | None]("withdrawOrderId", withdraw_order_id),
                param[int | None]("status", status),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("offset", offset),
                param[int | None]("limit", limit),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1CapitalWithdrawHistoryResponse]],
            error_mapper=withdraw_history_supporting_network_user_data_error_mapper,
            request_options=request_options,
        )
