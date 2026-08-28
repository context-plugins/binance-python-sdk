from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder, param
from ..errors.eth_staking_account_v2_user_data_error import (
    EthStakingAccountV2UserDataErrorBody,
    eth_staking_account_v2_user_data_error_mapper,
)
from ..errors.get_beth_rewards_distribution_history_user_data_error import (
    GetBethRewardsDistributionHistoryUserDataErrorBody,
    get_beth_rewards_distribution_history_user_data_error_mapper,
)
from ..errors.get_current_eth_staking_quota_user_data_error import (
    GetCurrentEthStakingQuotaUserDataErrorBody,
    get_current_eth_staking_quota_user_data_error_mapper,
)
from ..errors.get_eth_redemption_history_user_data_error import (
    GetEthRedemptionHistoryUserDataErrorBody,
    get_eth_redemption_history_user_data_error_mapper,
)
from ..errors.get_eth_staking_history_user_data_error import (
    GetEthStakingHistoryUserDataErrorBody,
    get_eth_staking_history_user_data_error_mapper,
)
from ..errors.get_wbeth_rate_history_user_data_error import (
    GetWbethRateHistoryUserDataErrorBody,
    get_wbeth_rate_history_user_data_error_mapper,
)
from ..errors.get_wbeth_rewards_history_user_data_error import (
    GetWbethRewardsHistoryUserDataErrorBody,
    get_wbeth_rewards_history_user_data_error_mapper,
)
from ..errors.get_wbeth_unwrap_history_user_data_error import (
    GetWbethUnwrapHistoryUserDataErrorBody,
    get_wbeth_unwrap_history_user_data_error_mapper,
)
from ..errors.get_wbeth_wrap_history_user_data_error import (
    GetWbethWrapHistoryUserDataErrorBody,
    get_wbeth_wrap_history_user_data_error_mapper,
)
from ..errors.redeem_eth_trade_error import RedeemEthTradeErrorBody, redeem_eth_trade_error_mapper
from ..errors.subscribe_eth_staking_v2_trade_error import (
    SubscribeEthStakingV2TradeErrorBody,
    subscribe_eth_staking_v2_trade_error_mapper,
)
from ..errors.wrap_beth_trade_error import WrapBethTradeErrorBody, wrap_beth_trade_error_mapper
from ..models.sapi_v1_eth_staking_eth_history_rate_history_response import SapiV1EthStakingEthHistoryRateHistoryResponse
from ..models.sapi_v1_eth_staking_eth_history_redemption_history_response import (
    SapiV1EthStakingEthHistoryRedemptionHistoryResponse,
)
from ..models.sapi_v1_eth_staking_eth_history_rewards_history_response import (
    SapiV1EthStakingEthHistoryRewardsHistoryResponse,
)
from ..models.sapi_v1_eth_staking_eth_history_staking_history_response import (
    SapiV1EthStakingEthHistoryStakingHistoryResponse,
)
from ..models.sapi_v1_eth_staking_eth_history_wbeth_rewards_history_response import (
    SapiV1EthStakingEthHistoryWbethRewardsHistoryResponse,
)
from ..models.sapi_v1_eth_staking_eth_quota_response import SapiV1EthStakingEthQuotaResponse
from ..models.sapi_v1_eth_staking_eth_redeem_response import SapiV1EthStakingEthRedeemResponse
from ..models.sapi_v1_eth_staking_wbeth_history_unwrap_history_response import (
    SapiV1EthStakingWbethHistoryUnwrapHistoryResponse,
)
from ..models.sapi_v1_eth_staking_wbeth_history_wrap_history_response import (
    SapiV1EthStakingWbethHistoryWrapHistoryResponse,
)
from ..models.sapi_v1_eth_staking_wbeth_wrap_response import SapiV1EthStakingWbethWrapResponse
from ..models.sapi_v2_eth_staking_account_response import SapiV2EthStakingAccountResponse
from ..models.sapi_v2_eth_staking_eth_stake_response import SapiV2EthStakingEthStakeResponse
from ..server.server import Server


class Staking:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = StakingWithRawResponse(client, server, auth)

    def eth_staking_account_v2_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV2EthStakingAccountResponse:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            ETH Staking account

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.eth_staking_account_v2_user_data(
            timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def get_beth_rewards_distribution_history_user_data(
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
    ) -> SapiV1EthStakingEthHistoryRewardsHistoryResponse:
        """- The time between startTime and endTime cannot be longer than 3 months.
        - If startTime and endTime are both not sent, then the last 30 days' data will be returned.
        - If startTime is sent but endTime is not sent, the next 30 days' data beginning from startTime will be
            returned.
        - If endTime is sent but startTime is not sent, the 30 days' data before endTime will be returned.

        Weight(IP): 150

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
            BETH rewards distribution history

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_beth_rewards_distribution_history_user_data(
            timestamp,
            signature,
            start_time=start_time,
            end_time=end_time,
            current=current,
            size=size,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_eth_redemption_history_user_data(
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
    ) -> SapiV1EthStakingEthHistoryRedemptionHistoryResponse:
        """- The time between startTime and endTime cannot be longer than 3 months.
        - If startTime and endTime are both not sent, then the last 30 days' data will be returned.
        - If startTime is sent but endTime is not sent, the next 30 days' data beginning from startTime will be
            returned.
        - If endTime is sent but startTime is not sent, the 30 days' data before endTime will be returned.

        Weight(IP): 150

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
            ETH redemption history

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_eth_redemption_history_user_data(
            timestamp,
            signature,
            start_time=start_time,
            end_time=end_time,
            current=current,
            size=size,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_eth_staking_history_user_data(
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
    ) -> SapiV1EthStakingEthHistoryStakingHistoryResponse:
        """- The time between startTime and endTime cannot be longer than 3 months.
        - If startTime and endTime are both not sent, then the last 30 days' data will be returned.
        - If startTime is sent but endTime is not sent, the next 30 days' data beginning from startTime will be
            returned.
        - If endTime is sent but startTime is not sent, the 30 days' data before endTime will be returned.

        Weight(IP): 150

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
            ETH staking history

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_eth_staking_history_user_data(
            timestamp,
            signature,
            start_time=start_time,
            end_time=end_time,
            current=current,
            size=size,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_wbeth_rate_history_user_data(
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
    ) -> SapiV1EthStakingEthHistoryRateHistoryResponse:
        """- The time between startTime and endTime cannot be longer than 3 months.
        - If startTime and endTime are both not sent, then the last 30 days' data will be returned.
        - If startTime is sent but endTime is not sent, the next 30 days' data beginning from startTime will be
            returned.
        - If endTime is sent but startTime is not sent, the 30 days' data before endTime will be returned.

        Weight(IP): 150

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
            WBETH Rate History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_wbeth_rate_history_user_data(
            timestamp,
            signature,
            start_time=start_time,
            end_time=end_time,
            current=current,
            size=size,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_wbeth_rewards_history_user_data(
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
    ) -> SapiV1EthStakingEthHistoryWbethRewardsHistoryResponse:
        """- The time between startTime and endTime cannot be longer than 3 months.
        - If startTime and endTime are both not sent, then the last 30 days' data will be returned.
        - If startTime is sent but endTime is not sent, the next 30 days' data beginning from startTime will be
            returned.
        - If endTime is sent but startTime is not sent, the 30 days' data before endTime will be returned.

        Weight(IP): 150

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
            WBETH rewards history

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_wbeth_rewards_history_user_data(
            timestamp,
            signature,
            start_time=start_time,
            end_time=end_time,
            current=current,
            size=size,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_wbeth_unwrap_history_user_data(
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
    ) -> SapiV1EthStakingWbethHistoryUnwrapHistoryResponse:
        """- The time between startTime and endTime cannot be longer than 3 months.
        - If startTime and endTime are both not sent, then the last 30 days' data will be returned.
        - If startTime is sent but endTime is not sent, the next 30 days' data beginning from startTime will be
            returned.
        - If endTime is sent but startTime is not sent, the 30 days' data before endTime will be returned.

        Weight(IP): 150

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
            WBETH unwrap history

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_wbeth_unwrap_history_user_data(
            timestamp,
            signature,
            start_time=start_time,
            end_time=end_time,
            current=current,
            size=size,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_wbeth_wrap_history_user_data(
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
    ) -> SapiV1EthStakingWbethHistoryWrapHistoryResponse:
        """- The time between startTime and endTime cannot be longer than 3 months.
        - If startTime and endTime are both not sent, then the last 30 days' data will be returned.
        - If startTime is sent but endTime is not sent, the next 30 days' data beginning from startTime will be
            returned.
        - If endTime is sent but startTime is not sent, the 30 days' data before endTime will be returned.

        Weight(IP): 150

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
            WBETH wrap history

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_wbeth_wrap_history_user_data(
            timestamp,
            signature,
            start_time=start_time,
            end_time=end_time,
            current=current,
            size=size,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def get_current_eth_staking_quota_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1EthStakingEthQuotaResponse:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Eth staking quota

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_current_eth_staking_quota_user_data(
            timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def redeem_eth_trade(
        self,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1EthStakingEthRedeemResponse:
        """Redeem WBETH or BETH and get ETH

        - You need to open Enable Spot & Margin Trading permission for the API Key which requests this endpoint.

        Weight(IP): 150

        Args:
            amount: Amount in BETH, limit 8 decimals
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: WBETH or BETH, default to BETH
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Returned ETH

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.redeem_eth_trade(
            amount, timestamp, signature, asset=asset, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def subscribe_eth_staking_v2_trade(
        self,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV2EthStakingEthStakeResponse:
        """Stake ETH to get WBETH

        - You need to open Enable Spot & Margin Trading permission for the API Key which requests this endpoint.

        Weight(IP): 150

        Args:
            amount: Amount in ETH, limit 4 decimals
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Subscribed WBETH

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.subscribe_eth_staking_v2_trade(
            amount, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def wrap_beth_trade(
        self,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1EthStakingWbethWrapResponse:
        """- You need to open Enable Spot & Margin Trading permission for the API Key which requests this endpoint.

        Weight(IP): 150

        Args:
            amount: Amount in BETH, limit 4 decimals
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Wrap BETH

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.wrap_beth_trade(
            amount, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> StakingWithRawResponse:
        return self._with_raw_response


class AsyncStaking:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncStakingWithRawResponse(client, server, auth)

    async def eth_staking_account_v2_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV2EthStakingAccountResponse:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            ETH Staking account

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.eth_staking_account_v2_user_data(
                timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def get_beth_rewards_distribution_history_user_data(
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
    ) -> SapiV1EthStakingEthHistoryRewardsHistoryResponse:
        """- The time between startTime and endTime cannot be longer than 3 months.
        - If startTime and endTime are both not sent, then the last 30 days' data will be returned.
        - If startTime is sent but endTime is not sent, the next 30 days' data beginning from startTime will be
            returned.
        - If endTime is sent but startTime is not sent, the 30 days' data before endTime will be returned.

        Weight(IP): 150

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
            BETH rewards distribution history

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_beth_rewards_distribution_history_user_data(
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

    async def get_eth_redemption_history_user_data(
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
    ) -> SapiV1EthStakingEthHistoryRedemptionHistoryResponse:
        """- The time between startTime and endTime cannot be longer than 3 months.
        - If startTime and endTime are both not sent, then the last 30 days' data will be returned.
        - If startTime is sent but endTime is not sent, the next 30 days' data beginning from startTime will be
            returned.
        - If endTime is sent but startTime is not sent, the 30 days' data before endTime will be returned.

        Weight(IP): 150

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
            ETH redemption history

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_eth_redemption_history_user_data(
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

    async def get_eth_staking_history_user_data(
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
    ) -> SapiV1EthStakingEthHistoryStakingHistoryResponse:
        """- The time between startTime and endTime cannot be longer than 3 months.
        - If startTime and endTime are both not sent, then the last 30 days' data will be returned.
        - If startTime is sent but endTime is not sent, the next 30 days' data beginning from startTime will be
            returned.
        - If endTime is sent but startTime is not sent, the 30 days' data before endTime will be returned.

        Weight(IP): 150

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
            ETH staking history

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_eth_staking_history_user_data(
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

    async def get_wbeth_rate_history_user_data(
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
    ) -> SapiV1EthStakingEthHistoryRateHistoryResponse:
        """- The time between startTime and endTime cannot be longer than 3 months.
        - If startTime and endTime are both not sent, then the last 30 days' data will be returned.
        - If startTime is sent but endTime is not sent, the next 30 days' data beginning from startTime will be
            returned.
        - If endTime is sent but startTime is not sent, the 30 days' data before endTime will be returned.

        Weight(IP): 150

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
            WBETH Rate History

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_wbeth_rate_history_user_data(
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

    async def get_wbeth_rewards_history_user_data(
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
    ) -> SapiV1EthStakingEthHistoryWbethRewardsHistoryResponse:
        """- The time between startTime and endTime cannot be longer than 3 months.
        - If startTime and endTime are both not sent, then the last 30 days' data will be returned.
        - If startTime is sent but endTime is not sent, the next 30 days' data beginning from startTime will be
            returned.
        - If endTime is sent but startTime is not sent, the 30 days' data before endTime will be returned.

        Weight(IP): 150

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
            WBETH rewards history

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_wbeth_rewards_history_user_data(
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

    async def get_wbeth_unwrap_history_user_data(
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
    ) -> SapiV1EthStakingWbethHistoryUnwrapHistoryResponse:
        """- The time between startTime and endTime cannot be longer than 3 months.
        - If startTime and endTime are both not sent, then the last 30 days' data will be returned.
        - If startTime is sent but endTime is not sent, the next 30 days' data beginning from startTime will be
            returned.
        - If endTime is sent but startTime is not sent, the 30 days' data before endTime will be returned.

        Weight(IP): 150

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
            WBETH unwrap history

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_wbeth_unwrap_history_user_data(
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

    async def get_wbeth_wrap_history_user_data(
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
    ) -> SapiV1EthStakingWbethHistoryWrapHistoryResponse:
        """- The time between startTime and endTime cannot be longer than 3 months.
        - If startTime and endTime are both not sent, then the last 30 days' data will be returned.
        - If startTime is sent but endTime is not sent, the next 30 days' data beginning from startTime will be
            returned.
        - If endTime is sent but startTime is not sent, the 30 days' data before endTime will be returned.

        Weight(IP): 150

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
            WBETH wrap history

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_wbeth_wrap_history_user_data(
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

    async def get_current_eth_staking_quota_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1EthStakingEthQuotaResponse:
        """Weight(IP): 150

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Eth staking quota

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_current_eth_staking_quota_user_data(
                timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def redeem_eth_trade(
        self,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1EthStakingEthRedeemResponse:
        """Redeem WBETH or BETH and get ETH

        - You need to open Enable Spot & Margin Trading permission for the API Key which requests this endpoint.

        Weight(IP): 150

        Args:
            amount: Amount in BETH, limit 8 decimals
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: WBETH or BETH, default to BETH
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Returned ETH

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.redeem_eth_trade(
                amount, timestamp, signature, asset=asset, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def subscribe_eth_staking_v2_trade(
        self,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV2EthStakingEthStakeResponse:
        """Stake ETH to get WBETH

        - You need to open Enable Spot & Margin Trading permission for the API Key which requests this endpoint.

        Weight(IP): 150

        Args:
            amount: Amount in ETH, limit 4 decimals
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Subscribed WBETH

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.subscribe_eth_staking_v2_trade(
                amount, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def wrap_beth_trade(
        self,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1EthStakingWbethWrapResponse:
        """- You need to open Enable Spot & Margin Trading permission for the API Key which requests this endpoint.

        Weight(IP): 150

        Args:
            amount: Amount in BETH, limit 4 decimals
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Wrap BETH

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.wrap_beth_trade(
                amount, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncStakingWithRawResponse:
        return self._with_raw_response


class StakingWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def eth_staking_account_v2_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV2EthStakingAccountResponse, EthStakingAccountV2UserDataErrorBody]:
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
            url_template=self._server.default("/sapi/v2/eth-staking/account"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV2EthStakingAccountResponse],
            error_mapper=eth_staking_account_v2_user_data_error_mapper,
            request_options=request_options,
        )

    def get_beth_rewards_distribution_history_user_data(
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
        SapiV1EthStakingEthHistoryRewardsHistoryResponse, GetBethRewardsDistributionHistoryUserDataErrorBody
    ]:
        """- The time between startTime and endTime cannot be longer than 3 months.
        - If startTime and endTime are both not sent, then the last 30 days' data will be returned.
        - If startTime is sent but endTime is not sent, the next 30 days' data beginning from startTime will be
            returned.
        - If endTime is sent but startTime is not sent, the 30 days' data before endTime will be returned.

        Weight(IP): 150

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
            url_template=self._server.default("/sapi/v1/eth-staking/eth/history/rewardsHistory"),
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
            decoder=json_decoder[SapiV1EthStakingEthHistoryRewardsHistoryResponse],
            error_mapper=get_beth_rewards_distribution_history_user_data_error_mapper,
            request_options=request_options,
        )

    def get_eth_redemption_history_user_data(
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
    ) -> ApiResult[SapiV1EthStakingEthHistoryRedemptionHistoryResponse, GetEthRedemptionHistoryUserDataErrorBody]:
        """- The time between startTime and endTime cannot be longer than 3 months.
        - If startTime and endTime are both not sent, then the last 30 days' data will be returned.
        - If startTime is sent but endTime is not sent, the next 30 days' data beginning from startTime will be
            returned.
        - If endTime is sent but startTime is not sent, the 30 days' data before endTime will be returned.

        Weight(IP): 150

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
            url_template=self._server.default("/sapi/v1/eth-staking/eth/history/redemptionHistory"),
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
            decoder=json_decoder[SapiV1EthStakingEthHistoryRedemptionHistoryResponse],
            error_mapper=get_eth_redemption_history_user_data_error_mapper,
            request_options=request_options,
        )

    def get_eth_staking_history_user_data(
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
    ) -> ApiResult[SapiV1EthStakingEthHistoryStakingHistoryResponse, GetEthStakingHistoryUserDataErrorBody]:
        """- The time between startTime and endTime cannot be longer than 3 months.
        - If startTime and endTime are both not sent, then the last 30 days' data will be returned.
        - If startTime is sent but endTime is not sent, the next 30 days' data beginning from startTime will be
            returned.
        - If endTime is sent but startTime is not sent, the 30 days' data before endTime will be returned.

        Weight(IP): 150

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
            url_template=self._server.default("/sapi/v1/eth-staking/eth/history/stakingHistory"),
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
            decoder=json_decoder[SapiV1EthStakingEthHistoryStakingHistoryResponse],
            error_mapper=get_eth_staking_history_user_data_error_mapper,
            request_options=request_options,
        )

    def get_wbeth_rate_history_user_data(
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
    ) -> ApiResult[SapiV1EthStakingEthHistoryRateHistoryResponse, GetWbethRateHistoryUserDataErrorBody]:
        """- The time between startTime and endTime cannot be longer than 3 months.
        - If startTime and endTime are both not sent, then the last 30 days' data will be returned.
        - If startTime is sent but endTime is not sent, the next 30 days' data beginning from startTime will be
            returned.
        - If endTime is sent but startTime is not sent, the 30 days' data before endTime will be returned.

        Weight(IP): 150

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
            url_template=self._server.default("/sapi/v1/eth-staking/eth/history/rateHistory"),
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
            decoder=json_decoder[SapiV1EthStakingEthHistoryRateHistoryResponse],
            error_mapper=get_wbeth_rate_history_user_data_error_mapper,
            request_options=request_options,
        )

    def get_wbeth_rewards_history_user_data(
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
    ) -> ApiResult[SapiV1EthStakingEthHistoryWbethRewardsHistoryResponse, GetWbethRewardsHistoryUserDataErrorBody]:
        """- The time between startTime and endTime cannot be longer than 3 months.
        - If startTime and endTime are both not sent, then the last 30 days' data will be returned.
        - If startTime is sent but endTime is not sent, the next 30 days' data beginning from startTime will be
            returned.
        - If endTime is sent but startTime is not sent, the 30 days' data before endTime will be returned.

        Weight(IP): 150

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
            url_template=self._server.default("/sapi/v1/eth-staking/eth/history/wbethRewardsHistory"),
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
            decoder=json_decoder[SapiV1EthStakingEthHistoryWbethRewardsHistoryResponse],
            error_mapper=get_wbeth_rewards_history_user_data_error_mapper,
            request_options=request_options,
        )

    def get_wbeth_unwrap_history_user_data(
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
    ) -> ApiResult[SapiV1EthStakingWbethHistoryUnwrapHistoryResponse, GetWbethUnwrapHistoryUserDataErrorBody]:
        """- The time between startTime and endTime cannot be longer than 3 months.
        - If startTime and endTime are both not sent, then the last 30 days' data will be returned.
        - If startTime is sent but endTime is not sent, the next 30 days' data beginning from startTime will be
            returned.
        - If endTime is sent but startTime is not sent, the 30 days' data before endTime will be returned.

        Weight(IP): 150

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
            url_template=self._server.default("/sapi/v1/eth-staking/wbeth/history/unwrapHistory"),
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
            decoder=json_decoder[SapiV1EthStakingWbethHistoryUnwrapHistoryResponse],
            error_mapper=get_wbeth_unwrap_history_user_data_error_mapper,
            request_options=request_options,
        )

    def get_wbeth_wrap_history_user_data(
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
    ) -> ApiResult[SapiV1EthStakingWbethHistoryWrapHistoryResponse, GetWbethWrapHistoryUserDataErrorBody]:
        """- The time between startTime and endTime cannot be longer than 3 months.
        - If startTime and endTime are both not sent, then the last 30 days' data will be returned.
        - If startTime is sent but endTime is not sent, the next 30 days' data beginning from startTime will be
            returned.
        - If endTime is sent but startTime is not sent, the 30 days' data before endTime will be returned.

        Weight(IP): 150

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
            url_template=self._server.default("/sapi/v1/eth-staking/wbeth/history/wrapHistory"),
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
            decoder=json_decoder[SapiV1EthStakingWbethHistoryWrapHistoryResponse],
            error_mapper=get_wbeth_wrap_history_user_data_error_mapper,
            request_options=request_options,
        )

    def get_current_eth_staking_quota_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1EthStakingEthQuotaResponse, GetCurrentEthStakingQuotaUserDataErrorBody]:
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
            url_template=self._server.default("/sapi/v1/eth-staking/eth/quota"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1EthStakingEthQuotaResponse],
            error_mapper=get_current_eth_staking_quota_user_data_error_mapper,
            request_options=request_options,
        )

    def redeem_eth_trade(
        self,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1EthStakingEthRedeemResponse, RedeemEthTradeErrorBody]:
        """Redeem WBETH or BETH and get ETH

        - You need to open Enable Spot & Margin Trading permission for the API Key which requests this endpoint.

        Weight(IP): 150

        Args:
            amount: Amount in BETH, limit 8 decimals
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: WBETH or BETH, default to BETH
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/eth-staking/eth/redeem"),
            query_params=[
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("asset", asset),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1EthStakingEthRedeemResponse],
            error_mapper=redeem_eth_trade_error_mapper,
            request_options=request_options,
        )

    def subscribe_eth_staking_v2_trade(
        self,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV2EthStakingEthStakeResponse, SubscribeEthStakingV2TradeErrorBody]:
        """Stake ETH to get WBETH

        - You need to open Enable Spot & Margin Trading permission for the API Key which requests this endpoint.

        Weight(IP): 150

        Args:
            amount: Amount in ETH, limit 4 decimals
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v2/eth-staking/eth/stake"),
            query_params=[
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV2EthStakingEthStakeResponse],
            error_mapper=subscribe_eth_staking_v2_trade_error_mapper,
            request_options=request_options,
        )

    def wrap_beth_trade(
        self,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1EthStakingWbethWrapResponse, WrapBethTradeErrorBody]:
        """- You need to open Enable Spot & Margin Trading permission for the API Key which requests this endpoint.

        Weight(IP): 150

        Args:
            amount: Amount in BETH, limit 4 decimals
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/eth-staking/wbeth/wrap"),
            query_params=[
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1EthStakingWbethWrapResponse],
            error_mapper=wrap_beth_trade_error_mapper,
            request_options=request_options,
        )


class AsyncStakingWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def eth_staking_account_v2_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV2EthStakingAccountResponse, EthStakingAccountV2UserDataErrorBody]:
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
            url_template=self._server.default("/sapi/v2/eth-staking/account"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV2EthStakingAccountResponse],
            error_mapper=eth_staking_account_v2_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_beth_rewards_distribution_history_user_data(
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
        SapiV1EthStakingEthHistoryRewardsHistoryResponse, GetBethRewardsDistributionHistoryUserDataErrorBody
    ]:
        """- The time between startTime and endTime cannot be longer than 3 months.
        - If startTime and endTime are both not sent, then the last 30 days' data will be returned.
        - If startTime is sent but endTime is not sent, the next 30 days' data beginning from startTime will be
            returned.
        - If endTime is sent but startTime is not sent, the 30 days' data before endTime will be returned.

        Weight(IP): 150

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
            url_template=self._server.default("/sapi/v1/eth-staking/eth/history/rewardsHistory"),
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
            decoder=json_decoder[SapiV1EthStakingEthHistoryRewardsHistoryResponse],
            error_mapper=get_beth_rewards_distribution_history_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_eth_redemption_history_user_data(
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
    ) -> ApiResult[SapiV1EthStakingEthHistoryRedemptionHistoryResponse, GetEthRedemptionHistoryUserDataErrorBody]:
        """- The time between startTime and endTime cannot be longer than 3 months.
        - If startTime and endTime are both not sent, then the last 30 days' data will be returned.
        - If startTime is sent but endTime is not sent, the next 30 days' data beginning from startTime will be
            returned.
        - If endTime is sent but startTime is not sent, the 30 days' data before endTime will be returned.

        Weight(IP): 150

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
            url_template=self._server.default("/sapi/v1/eth-staking/eth/history/redemptionHistory"),
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
            decoder=json_decoder[SapiV1EthStakingEthHistoryRedemptionHistoryResponse],
            error_mapper=get_eth_redemption_history_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_eth_staking_history_user_data(
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
    ) -> ApiResult[SapiV1EthStakingEthHistoryStakingHistoryResponse, GetEthStakingHistoryUserDataErrorBody]:
        """- The time between startTime and endTime cannot be longer than 3 months.
        - If startTime and endTime are both not sent, then the last 30 days' data will be returned.
        - If startTime is sent but endTime is not sent, the next 30 days' data beginning from startTime will be
            returned.
        - If endTime is sent but startTime is not sent, the 30 days' data before endTime will be returned.

        Weight(IP): 150

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
            url_template=self._server.default("/sapi/v1/eth-staking/eth/history/stakingHistory"),
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
            decoder=json_decoder[SapiV1EthStakingEthHistoryStakingHistoryResponse],
            error_mapper=get_eth_staking_history_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_wbeth_rate_history_user_data(
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
    ) -> ApiResult[SapiV1EthStakingEthHistoryRateHistoryResponse, GetWbethRateHistoryUserDataErrorBody]:
        """- The time between startTime and endTime cannot be longer than 3 months.
        - If startTime and endTime are both not sent, then the last 30 days' data will be returned.
        - If startTime is sent but endTime is not sent, the next 30 days' data beginning from startTime will be
            returned.
        - If endTime is sent but startTime is not sent, the 30 days' data before endTime will be returned.

        Weight(IP): 150

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
            url_template=self._server.default("/sapi/v1/eth-staking/eth/history/rateHistory"),
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
            decoder=json_decoder[SapiV1EthStakingEthHistoryRateHistoryResponse],
            error_mapper=get_wbeth_rate_history_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_wbeth_rewards_history_user_data(
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
    ) -> ApiResult[SapiV1EthStakingEthHistoryWbethRewardsHistoryResponse, GetWbethRewardsHistoryUserDataErrorBody]:
        """- The time between startTime and endTime cannot be longer than 3 months.
        - If startTime and endTime are both not sent, then the last 30 days' data will be returned.
        - If startTime is sent but endTime is not sent, the next 30 days' data beginning from startTime will be
            returned.
        - If endTime is sent but startTime is not sent, the 30 days' data before endTime will be returned.

        Weight(IP): 150

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
            url_template=self._server.default("/sapi/v1/eth-staking/eth/history/wbethRewardsHistory"),
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
            decoder=json_decoder[SapiV1EthStakingEthHistoryWbethRewardsHistoryResponse],
            error_mapper=get_wbeth_rewards_history_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_wbeth_unwrap_history_user_data(
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
    ) -> ApiResult[SapiV1EthStakingWbethHistoryUnwrapHistoryResponse, GetWbethUnwrapHistoryUserDataErrorBody]:
        """- The time between startTime and endTime cannot be longer than 3 months.
        - If startTime and endTime are both not sent, then the last 30 days' data will be returned.
        - If startTime is sent but endTime is not sent, the next 30 days' data beginning from startTime will be
            returned.
        - If endTime is sent but startTime is not sent, the 30 days' data before endTime will be returned.

        Weight(IP): 150

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
            url_template=self._server.default("/sapi/v1/eth-staking/wbeth/history/unwrapHistory"),
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
            decoder=json_decoder[SapiV1EthStakingWbethHistoryUnwrapHistoryResponse],
            error_mapper=get_wbeth_unwrap_history_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_wbeth_wrap_history_user_data(
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
    ) -> ApiResult[SapiV1EthStakingWbethHistoryWrapHistoryResponse, GetWbethWrapHistoryUserDataErrorBody]:
        """- The time between startTime and endTime cannot be longer than 3 months.
        - If startTime and endTime are both not sent, then the last 30 days' data will be returned.
        - If startTime is sent but endTime is not sent, the next 30 days' data beginning from startTime will be
            returned.
        - If endTime is sent but startTime is not sent, the 30 days' data before endTime will be returned.

        Weight(IP): 150

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
            url_template=self._server.default("/sapi/v1/eth-staking/wbeth/history/wrapHistory"),
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
            decoder=json_decoder[SapiV1EthStakingWbethHistoryWrapHistoryResponse],
            error_mapper=get_wbeth_wrap_history_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_current_eth_staking_quota_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1EthStakingEthQuotaResponse, GetCurrentEthStakingQuotaUserDataErrorBody]:
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
            url_template=self._server.default("/sapi/v1/eth-staking/eth/quota"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1EthStakingEthQuotaResponse],
            error_mapper=get_current_eth_staking_quota_user_data_error_mapper,
            request_options=request_options,
        )

    async def redeem_eth_trade(
        self,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        asset: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1EthStakingEthRedeemResponse, RedeemEthTradeErrorBody]:
        """Redeem WBETH or BETH and get ETH

        - You need to open Enable Spot & Margin Trading permission for the API Key which requests this endpoint.

        Weight(IP): 150

        Args:
            amount: Amount in BETH, limit 8 decimals
            timestamp: UTC timestamp in ms
            signature: Signature
            asset: WBETH or BETH, default to BETH
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/eth-staking/eth/redeem"),
            query_params=[
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("asset", asset),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1EthStakingEthRedeemResponse],
            error_mapper=redeem_eth_trade_error_mapper,
            request_options=request_options,
        )

    async def subscribe_eth_staking_v2_trade(
        self,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV2EthStakingEthStakeResponse, SubscribeEthStakingV2TradeErrorBody]:
        """Stake ETH to get WBETH

        - You need to open Enable Spot & Margin Trading permission for the API Key which requests this endpoint.

        Weight(IP): 150

        Args:
            amount: Amount in ETH, limit 4 decimals
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v2/eth-staking/eth/stake"),
            query_params=[
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV2EthStakingEthStakeResponse],
            error_mapper=subscribe_eth_staking_v2_trade_error_mapper,
            request_options=request_options,
        )

    async def wrap_beth_trade(
        self,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1EthStakingWbethWrapResponse, WrapBethTradeErrorBody]:
        """- You need to open Enable Spot & Margin Trading permission for the API Key which requests this endpoint.

        Weight(IP): 150

        Args:
            amount: Amount in BETH, limit 4 decimals
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/eth-staking/wbeth/wrap"),
            query_params=[
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1EthStakingWbethWrapResponse],
            error_mapper=wrap_beth_trade_error_mapper,
            request_options=request_options,
        )
