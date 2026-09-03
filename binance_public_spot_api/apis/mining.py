from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder, param
from ..errors.account_list_user_data_error import AccountListUserDataErrorBody, account_list_user_data_error_mapper
from ..errors.acquiring_algorithm_market_data_error import (
    AcquiringAlgorithmMarketDataErrorBody,
    acquiring_algorithm_market_data_error_mapper,
)
from ..errors.acquiring_coin_name_market_data_error import (
    AcquiringCoinNameMarketDataErrorBody,
    acquiring_coin_name_market_data_error_mapper,
)
from ..errors.cancel_hashrate_resale_configuration_user_data_error import (
    CancelHashrateResaleConfigurationUserDataErrorBody,
    cancel_hashrate_resale_configuration_user_data_error_mapper,
)
from ..errors.earnings_list_user_data_error import EarningsListUserDataErrorBody, earnings_list_user_data_error_mapper
from ..errors.extra_bonus_list_user_data_error import (
    ExtraBonusListUserDataErrorBody,
    extra_bonus_list_user_data_error_mapper,
)
from ..errors.hashrate_resale_details_user_data_error import (
    HashrateResaleDetailsUserDataErrorBody,
    hashrate_resale_details_user_data_error_mapper,
)
from ..errors.hashrate_resale_list_user_data_error import (
    HashrateResaleListUserDataErrorBody,
    hashrate_resale_list_user_data_error_mapper,
)
from ..errors.hashrate_resale_request_user_data_error import (
    HashrateResaleRequestUserDataErrorBody,
    hashrate_resale_request_user_data_error_mapper,
)
from ..errors.mining_account_earning_user_data_error import (
    MiningAccountEarningUserDataErrorBody,
    mining_account_earning_user_data_error_mapper,
)
from ..errors.request_for_detail_miner_list_user_data_error import (
    RequestForDetailMinerListUserDataErrorBody,
    request_for_detail_miner_list_user_data_error_mapper,
)
from ..errors.request_for_miner_list_user_data_error import (
    RequestForMinerListUserDataErrorBody,
    request_for_miner_list_user_data_error_mapper,
)
from ..errors.statistic_list_user_data_error import (
    StatisticListUserDataErrorBody,
    statistic_list_user_data_error_mapper,
)
from ..models.sapi_v1_mining_hash_transfer_config_cancel_response import SapiV1MiningHashTransferConfigCancelResponse
from ..models.sapi_v1_mining_hash_transfer_config_details_list_response import (
    SapiV1MiningHashTransferConfigDetailsListResponse,
)
from ..models.sapi_v1_mining_hash_transfer_config_response import SapiV1MiningHashTransferConfigResponse
from ..models.sapi_v1_mining_hash_transfer_profit_details_response import SapiV1MiningHashTransferProfitDetailsResponse
from ..models.sapi_v1_mining_payment_list_response import SapiV1MiningPaymentListResponse
from ..models.sapi_v1_mining_payment_other_response import SapiV1MiningPaymentOtherResponse
from ..models.sapi_v1_mining_payment_uid_response import SapiV1MiningPaymentUidResponse
from ..models.sapi_v1_mining_pub_algo_list_response import SapiV1MiningPubAlgoListResponse
from ..models.sapi_v1_mining_pub_coin_list_response import SapiV1MiningPubCoinListResponse
from ..models.sapi_v1_mining_statistics_user_list_response import SapiV1MiningStatisticsUserListResponse
from ..models.sapi_v1_mining_statistics_user_status_response import SapiV1MiningStatisticsUserStatusResponse
from ..models.sapi_v1_mining_worker_detail_response import SapiV1MiningWorkerDetailResponse
from ..models.sapi_v1_mining_worker_list_response import SapiV1MiningWorkerListResponse
from ..server.server import Server


class Mining:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MiningWithRawResponse(client, server, auth)

    def account_list_user_data(
        self,
        algo: str,
        user_name: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MiningStatisticsUserListResponse:
        """Weight(IP): 5

        Args:
            algo: Algorithm(sha256)
            user_name: Mining Account
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of mining accounts

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.account_list_user_data(
            algo, user_name, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def acquiring_algorithm_market_data(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> SapiV1MiningPubAlgoListResponse:
        """Weight(IP): 1

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Algorithm information

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.acquiring_algorithm_market_data(request_options=request_options).unwrap()

    def acquiring_coin_name_market_data(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> SapiV1MiningPubCoinListResponse:
        """Weight(IP): 1

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Coin information

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.acquiring_coin_name_market_data(request_options=request_options).unwrap()

    def cancel_hashrate_resale_configuration_user_data(
        self,
        config_id: str,
        user_name: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MiningHashTransferConfigCancelResponse:
        """Weight(IP): 5

        Args:
            config_id: Mining ID
            user_name: Mining Account
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success flag

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.cancel_hashrate_resale_configuration_user_data(
            config_id, user_name, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def earnings_list_user_data(
        self,
        algo: str,
        user_name: str,
        timestamp: int,
        signature: str,
        *,
        coin: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        page_index: int | None = None,
        page_size: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MiningPaymentListResponse:
        """Weight(IP): 5

        Args:
            algo: Algorithm(sha256)
            user_name: Mining Account
            timestamp: UTC timestamp in ms
            signature: Signature
            coin: Coin name
            start_date: Search date, millisecond timestamp, while empty query all
            end_date: Search date, millisecond timestamp, while empty query all
            page_index: Page number, default is first page, start form 1
            page_size: Number of pages, minimum 10, maximum 200
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of earnings

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.earnings_list_user_data(
            algo,
            user_name,
            timestamp,
            signature,
            coin=coin,
            start_date=start_date,
            end_date=end_date,
            page_index=page_index,
            page_size=page_size,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def extra_bonus_list_user_data(
        self,
        algo: str,
        user_name: str,
        timestamp: int,
        signature: str,
        *,
        coin: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        page_index: int | None = None,
        page_size: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MiningPaymentOtherResponse:
        """Weight(IP): 5

        Args:
            algo: Algorithm(sha256)
            user_name: Mining Account
            timestamp: UTC timestamp in ms
            signature: Signature
            coin: Coin name
            start_date: Search date, millisecond timestamp, while empty query all
            end_date: Search date, millisecond timestamp, while empty query all
            page_index: Page number, default is first page, start form 1
            page_size: Number of pages, minimum 10, maximum 200
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of extra bonuses

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.extra_bonus_list_user_data(
            algo,
            user_name,
            timestamp,
            signature,
            coin=coin,
            start_date=start_date,
            end_date=end_date,
            page_index=page_index,
            page_size=page_size,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def hashrate_resale_details_user_data(
        self,
        config_id: str,
        user_name: str,
        timestamp: int,
        signature: str,
        *,
        page_index: int | None = None,
        page_size: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MiningHashTransferProfitDetailsResponse:
        """Weight(IP): 5

        Args:
            config_id: Mining ID
            user_name: Mining Account
            timestamp: UTC timestamp in ms
            signature: Signature
            page_index: Page number, default is first page, start form 1
            page_size: Number of pages, minimum 10, maximum 200
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of hashrate resale details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.hashrate_resale_details_user_data(
            config_id,
            user_name,
            timestamp,
            signature,
            page_index=page_index,
            page_size=page_size,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def hashrate_resale_list_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        page_index: int | None = None,
        page_size: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MiningHashTransferConfigDetailsListResponse:
        """Weight(IP): 5

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            page_index: Page number, default is first page, start form 1
            page_size: Number of pages, minimum 10, maximum 200
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of hashrate resales

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.hashrate_resale_list_user_data(
            timestamp,
            signature,
            page_index=page_index,
            page_size=page_size,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def hashrate_resale_request_user_data(
        self,
        user_name: str,
        algo: str,
        to_pool_user: str,
        hash_rate: str,
        timestamp: int,
        signature: str,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MiningHashTransferConfigResponse:
        """Weight(IP): 5

        Args:
            user_name: Mining Account
            algo: Algorithm(sha256)
            to_pool_user: Mining Account
            hash_rate: Resale hashrate h/s must be transferred (BTC is greater than 500000000000 ETH is greater than
                500000)
            timestamp: UTC timestamp in ms
            signature: Signature
            start_date: Search date, millisecond timestamp, while empty query all
            end_date: Search date, millisecond timestamp, while empty query all
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Mining Account Id

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.hashrate_resale_request_user_data(
            user_name,
            algo,
            to_pool_user,
            hash_rate,
            timestamp,
            signature,
            start_date=start_date,
            end_date=end_date,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def mining_account_earning_user_data(
        self,
        algo: str,
        timestamp: int,
        signature: str,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        page_index: int | None = None,
        page_size: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MiningPaymentUidResponse:
        """Weight(IP): 5

        Args:
            algo: Algorithm(sha256)
            timestamp: UTC timestamp in ms
            signature: Signature
            start_date: Search date, millisecond timestamp, while empty query all
            end_date: Search date, millisecond timestamp, while empty query all
            page_index: Page number, default is first page, start form 1
            page_size: Number of pages, minimum 10, maximum 200
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Mining account earnings

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.mining_account_earning_user_data(
            algo,
            timestamp,
            signature,
            start_date=start_date,
            end_date=end_date,
            page_index=page_index,
            page_size=page_size,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def request_for_detail_miner_list_user_data(
        self,
        algo: str,
        user_name: str,
        worker_name: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MiningWorkerDetailResponse:
        """Weight(IP): 5

        Args:
            algo: Algorithm(sha256)
            user_name: Mining Account
            worker_name: Miner’s name
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of workers' hashrates'

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.request_for_detail_miner_list_user_data(
            algo, user_name, worker_name, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def request_for_miner_list_user_data(
        self,
        algo: str,
        user_name: str,
        timestamp: int,
        signature: str,
        *,
        page_index: int | None = None,
        sort: int | None = None,
        sort_column: int | None = None,
        worker_status: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MiningWorkerListResponse:
        """Weight(IP): 5

        Args:
            algo: Algorithm(sha256)
            user_name: Mining Account
            timestamp: UTC timestamp in ms
            signature: Signature
            page_index: Page number, default is first page, start form 1
            sort: sort sequence(default=0)0 positive sequence, 1 negative sequence
            sort_column: Sort by( default 1): 1: miner name, 2: real-time computing power, 3: daily average computing
                power, 4: real-time rejection rate, 5: last submission time
            worker_status: miners status(default=0)0 all, 1 valid, 2 invalid, 3 failure
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of workers

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.request_for_miner_list_user_data(
            algo,
            user_name,
            timestamp,
            signature,
            page_index=page_index,
            sort=sort,
            sort_column=sort_column,
            worker_status=worker_status,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def statistic_list_user_data(
        self,
        algo: str,
        user_name: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MiningStatisticsUserStatusResponse:
        """Weight(IP): 5

        Args:
            algo: Algorithm(sha256)
            user_name: Mining Account
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Mining account statistics

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.statistic_list_user_data(
            algo, user_name, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> MiningWithRawResponse:
        return self._with_raw_response


class AsyncMining:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMiningWithRawResponse(client, server, auth)

    async def account_list_user_data(
        self,
        algo: str,
        user_name: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MiningStatisticsUserListResponse:
        """Weight(IP): 5

        Args:
            algo: Algorithm(sha256)
            user_name: Mining Account
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of mining accounts

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.account_list_user_data(
                algo, user_name, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def acquiring_algorithm_market_data(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> SapiV1MiningPubAlgoListResponse:
        """Weight(IP): 1

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Algorithm information

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return (await self._with_raw_response.acquiring_algorithm_market_data(request_options=request_options)).unwrap()

    async def acquiring_coin_name_market_data(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> SapiV1MiningPubCoinListResponse:
        """Weight(IP): 1

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Coin information

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return (await self._with_raw_response.acquiring_coin_name_market_data(request_options=request_options)).unwrap()

    async def cancel_hashrate_resale_configuration_user_data(
        self,
        config_id: str,
        user_name: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MiningHashTransferConfigCancelResponse:
        """Weight(IP): 5

        Args:
            config_id: Mining ID
            user_name: Mining Account
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success flag

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.cancel_hashrate_resale_configuration_user_data(
                config_id, user_name, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def earnings_list_user_data(
        self,
        algo: str,
        user_name: str,
        timestamp: int,
        signature: str,
        *,
        coin: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        page_index: int | None = None,
        page_size: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MiningPaymentListResponse:
        """Weight(IP): 5

        Args:
            algo: Algorithm(sha256)
            user_name: Mining Account
            timestamp: UTC timestamp in ms
            signature: Signature
            coin: Coin name
            start_date: Search date, millisecond timestamp, while empty query all
            end_date: Search date, millisecond timestamp, while empty query all
            page_index: Page number, default is first page, start form 1
            page_size: Number of pages, minimum 10, maximum 200
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of earnings

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.earnings_list_user_data(
                algo,
                user_name,
                timestamp,
                signature,
                coin=coin,
                start_date=start_date,
                end_date=end_date,
                page_index=page_index,
                page_size=page_size,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def extra_bonus_list_user_data(
        self,
        algo: str,
        user_name: str,
        timestamp: int,
        signature: str,
        *,
        coin: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        page_index: int | None = None,
        page_size: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MiningPaymentOtherResponse:
        """Weight(IP): 5

        Args:
            algo: Algorithm(sha256)
            user_name: Mining Account
            timestamp: UTC timestamp in ms
            signature: Signature
            coin: Coin name
            start_date: Search date, millisecond timestamp, while empty query all
            end_date: Search date, millisecond timestamp, while empty query all
            page_index: Page number, default is first page, start form 1
            page_size: Number of pages, minimum 10, maximum 200
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of extra bonuses

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.extra_bonus_list_user_data(
                algo,
                user_name,
                timestamp,
                signature,
                coin=coin,
                start_date=start_date,
                end_date=end_date,
                page_index=page_index,
                page_size=page_size,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def hashrate_resale_details_user_data(
        self,
        config_id: str,
        user_name: str,
        timestamp: int,
        signature: str,
        *,
        page_index: int | None = None,
        page_size: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MiningHashTransferProfitDetailsResponse:
        """Weight(IP): 5

        Args:
            config_id: Mining ID
            user_name: Mining Account
            timestamp: UTC timestamp in ms
            signature: Signature
            page_index: Page number, default is first page, start form 1
            page_size: Number of pages, minimum 10, maximum 200
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of hashrate resale details

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.hashrate_resale_details_user_data(
                config_id,
                user_name,
                timestamp,
                signature,
                page_index=page_index,
                page_size=page_size,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def hashrate_resale_list_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        page_index: int | None = None,
        page_size: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MiningHashTransferConfigDetailsListResponse:
        """Weight(IP): 5

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            page_index: Page number, default is first page, start form 1
            page_size: Number of pages, minimum 10, maximum 200
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of hashrate resales

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.hashrate_resale_list_user_data(
                timestamp,
                signature,
                page_index=page_index,
                page_size=page_size,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def hashrate_resale_request_user_data(
        self,
        user_name: str,
        algo: str,
        to_pool_user: str,
        hash_rate: str,
        timestamp: int,
        signature: str,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MiningHashTransferConfigResponse:
        """Weight(IP): 5

        Args:
            user_name: Mining Account
            algo: Algorithm(sha256)
            to_pool_user: Mining Account
            hash_rate: Resale hashrate h/s must be transferred (BTC is greater than 500000000000 ETH is greater than
                500000)
            timestamp: UTC timestamp in ms
            signature: Signature
            start_date: Search date, millisecond timestamp, while empty query all
            end_date: Search date, millisecond timestamp, while empty query all
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Mining Account Id

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.hashrate_resale_request_user_data(
                user_name,
                algo,
                to_pool_user,
                hash_rate,
                timestamp,
                signature,
                start_date=start_date,
                end_date=end_date,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def mining_account_earning_user_data(
        self,
        algo: str,
        timestamp: int,
        signature: str,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        page_index: int | None = None,
        page_size: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MiningPaymentUidResponse:
        """Weight(IP): 5

        Args:
            algo: Algorithm(sha256)
            timestamp: UTC timestamp in ms
            signature: Signature
            start_date: Search date, millisecond timestamp, while empty query all
            end_date: Search date, millisecond timestamp, while empty query all
            page_index: Page number, default is first page, start form 1
            page_size: Number of pages, minimum 10, maximum 200
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Mining account earnings

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.mining_account_earning_user_data(
                algo,
                timestamp,
                signature,
                start_date=start_date,
                end_date=end_date,
                page_index=page_index,
                page_size=page_size,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def request_for_detail_miner_list_user_data(
        self,
        algo: str,
        user_name: str,
        worker_name: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MiningWorkerDetailResponse:
        """Weight(IP): 5

        Args:
            algo: Algorithm(sha256)
            user_name: Mining Account
            worker_name: Miner’s name
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of workers' hashrates'

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.request_for_detail_miner_list_user_data(
                algo,
                user_name,
                worker_name,
                timestamp,
                signature,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def request_for_miner_list_user_data(
        self,
        algo: str,
        user_name: str,
        timestamp: int,
        signature: str,
        *,
        page_index: int | None = None,
        sort: int | None = None,
        sort_column: int | None = None,
        worker_status: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MiningWorkerListResponse:
        """Weight(IP): 5

        Args:
            algo: Algorithm(sha256)
            user_name: Mining Account
            timestamp: UTC timestamp in ms
            signature: Signature
            page_index: Page number, default is first page, start form 1
            sort: sort sequence(default=0)0 positive sequence, 1 negative sequence
            sort_column: Sort by( default 1): 1: miner name, 2: real-time computing power, 3: daily average computing
                power, 4: real-time rejection rate, 5: last submission time
            worker_status: miners status(default=0)0 all, 1 valid, 2 invalid, 3 failure
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of workers

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.request_for_miner_list_user_data(
                algo,
                user_name,
                timestamp,
                signature,
                page_index=page_index,
                sort=sort,
                sort_column=sort_column,
                worker_status=worker_status,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def statistic_list_user_data(
        self,
        algo: str,
        user_name: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1MiningStatisticsUserStatusResponse:
        """Weight(IP): 5

        Args:
            algo: Algorithm(sha256)
            user_name: Mining Account
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Mining account statistics

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.statistic_list_user_data(
                algo, user_name, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncMiningWithRawResponse:
        return self._with_raw_response


class MiningWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def account_list_user_data(
        self,
        algo: str,
        user_name: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MiningStatisticsUserListResponse, AccountListUserDataErrorBody]:
        """Weight(IP): 5

        Args:
            algo: Algorithm(sha256)
            user_name: Mining Account
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/mining/statistics/user/list"),
            query_params=[
                param[str]("algo", algo),
                param[str]("userName", user_name),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MiningStatisticsUserListResponse],
            error_mapper=account_list_user_data_error_mapper,
            request_options=request_options,
        )

    def acquiring_algorithm_market_data(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SapiV1MiningPubAlgoListResponse, AcquiringAlgorithmMarketDataErrorBody]:
        """Weight(IP): 1

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/mining/pub/algoList"),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MiningPubAlgoListResponse],
            error_mapper=acquiring_algorithm_market_data_error_mapper,
            request_options=request_options,
        )

    def acquiring_coin_name_market_data(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SapiV1MiningPubCoinListResponse, AcquiringCoinNameMarketDataErrorBody]:
        """Weight(IP): 1

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/mining/pub/coinList"),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MiningPubCoinListResponse],
            error_mapper=acquiring_coin_name_market_data_error_mapper,
            request_options=request_options,
        )

    def cancel_hashrate_resale_configuration_user_data(
        self,
        config_id: str,
        user_name: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MiningHashTransferConfigCancelResponse, CancelHashrateResaleConfigurationUserDataErrorBody]:
        """Weight(IP): 5

        Args:
            config_id: Mining ID
            user_name: Mining Account
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/mining/hash-transfer/config/cancel"),
            query_params=[
                param[str]("configId", config_id),
                param[str]("userName", user_name),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MiningHashTransferConfigCancelResponse],
            error_mapper=cancel_hashrate_resale_configuration_user_data_error_mapper,
            request_options=request_options,
        )

    def earnings_list_user_data(
        self,
        algo: str,
        user_name: str,
        timestamp: int,
        signature: str,
        *,
        coin: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        page_index: int | None = None,
        page_size: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MiningPaymentListResponse, EarningsListUserDataErrorBody]:
        """Weight(IP): 5

        Args:
            algo: Algorithm(sha256)
            user_name: Mining Account
            timestamp: UTC timestamp in ms
            signature: Signature
            coin: Coin name
            start_date: Search date, millisecond timestamp, while empty query all
            end_date: Search date, millisecond timestamp, while empty query all
            page_index: Page number, default is first page, start form 1
            page_size: Number of pages, minimum 10, maximum 200
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/mining/payment/list"),
            query_params=[
                param[str]("algo", algo),
                param[str]("userName", user_name),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("coin", coin),
                param[str | None]("startDate", start_date),
                param[str | None]("endDate", end_date),
                param[int | None]("pageIndex", page_index),
                param[str | None]("pageSize", page_size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MiningPaymentListResponse],
            error_mapper=earnings_list_user_data_error_mapper,
            request_options=request_options,
        )

    def extra_bonus_list_user_data(
        self,
        algo: str,
        user_name: str,
        timestamp: int,
        signature: str,
        *,
        coin: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        page_index: int | None = None,
        page_size: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MiningPaymentOtherResponse, ExtraBonusListUserDataErrorBody]:
        """Weight(IP): 5

        Args:
            algo: Algorithm(sha256)
            user_name: Mining Account
            timestamp: UTC timestamp in ms
            signature: Signature
            coin: Coin name
            start_date: Search date, millisecond timestamp, while empty query all
            end_date: Search date, millisecond timestamp, while empty query all
            page_index: Page number, default is first page, start form 1
            page_size: Number of pages, minimum 10, maximum 200
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/mining/payment/other"),
            query_params=[
                param[str]("algo", algo),
                param[str]("userName", user_name),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("coin", coin),
                param[str | None]("startDate", start_date),
                param[str | None]("endDate", end_date),
                param[int | None]("pageIndex", page_index),
                param[str | None]("pageSize", page_size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MiningPaymentOtherResponse],
            error_mapper=extra_bonus_list_user_data_error_mapper,
            request_options=request_options,
        )

    def hashrate_resale_details_user_data(
        self,
        config_id: str,
        user_name: str,
        timestamp: int,
        signature: str,
        *,
        page_index: int | None = None,
        page_size: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MiningHashTransferProfitDetailsResponse, HashrateResaleDetailsUserDataErrorBody]:
        """Weight(IP): 5

        Args:
            config_id: Mining ID
            user_name: Mining Account
            timestamp: UTC timestamp in ms
            signature: Signature
            page_index: Page number, default is first page, start form 1
            page_size: Number of pages, minimum 10, maximum 200
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/mining/hash-transfer/profit/details"),
            query_params=[
                param[str]("configId", config_id),
                param[str]("userName", user_name),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("pageIndex", page_index),
                param[str | None]("pageSize", page_size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MiningHashTransferProfitDetailsResponse],
            error_mapper=hashrate_resale_details_user_data_error_mapper,
            request_options=request_options,
        )

    def hashrate_resale_list_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        page_index: int | None = None,
        page_size: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MiningHashTransferConfigDetailsListResponse, HashrateResaleListUserDataErrorBody]:
        """Weight(IP): 5

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            page_index: Page number, default is first page, start form 1
            page_size: Number of pages, minimum 10, maximum 200
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/mining/hash-transfer/config/details/list"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("pageIndex", page_index),
                param[str | None]("pageSize", page_size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MiningHashTransferConfigDetailsListResponse],
            error_mapper=hashrate_resale_list_user_data_error_mapper,
            request_options=request_options,
        )

    def hashrate_resale_request_user_data(
        self,
        user_name: str,
        algo: str,
        to_pool_user: str,
        hash_rate: str,
        timestamp: int,
        signature: str,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MiningHashTransferConfigResponse, HashrateResaleRequestUserDataErrorBody]:
        """Weight(IP): 5

        Args:
            user_name: Mining Account
            algo: Algorithm(sha256)
            to_pool_user: Mining Account
            hash_rate: Resale hashrate h/s must be transferred (BTC is greater than 500000000000 ETH is greater than
                500000)
            timestamp: UTC timestamp in ms
            signature: Signature
            start_date: Search date, millisecond timestamp, while empty query all
            end_date: Search date, millisecond timestamp, while empty query all
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/mining/hash-transfer/config"),
            query_params=[
                param[str]("userName", user_name),
                param[str]("algo", algo),
                param[str]("toPoolUser", to_pool_user),
                param[str]("hashRate", hash_rate),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("startDate", start_date),
                param[str | None]("endDate", end_date),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MiningHashTransferConfigResponse],
            error_mapper=hashrate_resale_request_user_data_error_mapper,
            request_options=request_options,
        )

    def mining_account_earning_user_data(
        self,
        algo: str,
        timestamp: int,
        signature: str,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        page_index: int | None = None,
        page_size: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MiningPaymentUidResponse, MiningAccountEarningUserDataErrorBody]:
        """Weight(IP): 5

        Args:
            algo: Algorithm(sha256)
            timestamp: UTC timestamp in ms
            signature: Signature
            start_date: Search date, millisecond timestamp, while empty query all
            end_date: Search date, millisecond timestamp, while empty query all
            page_index: Page number, default is first page, start form 1
            page_size: Number of pages, minimum 10, maximum 200
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/mining/payment/uid"),
            query_params=[
                param[str]("algo", algo),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("startDate", start_date),
                param[str | None]("endDate", end_date),
                param[int | None]("pageIndex", page_index),
                param[str | None]("pageSize", page_size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MiningPaymentUidResponse],
            error_mapper=mining_account_earning_user_data_error_mapper,
            request_options=request_options,
        )

    def request_for_detail_miner_list_user_data(
        self,
        algo: str,
        user_name: str,
        worker_name: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MiningWorkerDetailResponse, RequestForDetailMinerListUserDataErrorBody]:
        """Weight(IP): 5

        Args:
            algo: Algorithm(sha256)
            user_name: Mining Account
            worker_name: Miner’s name
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/mining/worker/detail"),
            query_params=[
                param[str]("algo", algo),
                param[str]("userName", user_name),
                param[str]("workerName", worker_name),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MiningWorkerDetailResponse],
            error_mapper=request_for_detail_miner_list_user_data_error_mapper,
            request_options=request_options,
        )

    def request_for_miner_list_user_data(
        self,
        algo: str,
        user_name: str,
        timestamp: int,
        signature: str,
        *,
        page_index: int | None = None,
        sort: int | None = None,
        sort_column: int | None = None,
        worker_status: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MiningWorkerListResponse, RequestForMinerListUserDataErrorBody]:
        """Weight(IP): 5

        Args:
            algo: Algorithm(sha256)
            user_name: Mining Account
            timestamp: UTC timestamp in ms
            signature: Signature
            page_index: Page number, default is first page, start form 1
            sort: sort sequence(default=0)0 positive sequence, 1 negative sequence
            sort_column: Sort by( default 1): 1: miner name, 2: real-time computing power, 3: daily average computing
                power, 4: real-time rejection rate, 5: last submission time
            worker_status: miners status(default=0)0 all, 1 valid, 2 invalid, 3 failure
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/mining/worker/list"),
            query_params=[
                param[str]("algo", algo),
                param[str]("userName", user_name),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("pageIndex", page_index),
                param[int | None]("sort", sort),
                param[int | None]("sortColumn", sort_column),
                param[int | None]("workerStatus", worker_status),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MiningWorkerListResponse],
            error_mapper=request_for_miner_list_user_data_error_mapper,
            request_options=request_options,
        )

    def statistic_list_user_data(
        self,
        algo: str,
        user_name: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MiningStatisticsUserStatusResponse, StatisticListUserDataErrorBody]:
        """Weight(IP): 5

        Args:
            algo: Algorithm(sha256)
            user_name: Mining Account
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/mining/statistics/user/status"),
            query_params=[
                param[str]("algo", algo),
                param[str]("userName", user_name),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MiningStatisticsUserStatusResponse],
            error_mapper=statistic_list_user_data_error_mapper,
            request_options=request_options,
        )


class AsyncMiningWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def account_list_user_data(
        self,
        algo: str,
        user_name: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MiningStatisticsUserListResponse, AccountListUserDataErrorBody]:
        """Weight(IP): 5

        Args:
            algo: Algorithm(sha256)
            user_name: Mining Account
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/mining/statistics/user/list"),
            query_params=[
                param[str]("algo", algo),
                param[str]("userName", user_name),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MiningStatisticsUserListResponse],
            error_mapper=account_list_user_data_error_mapper,
            request_options=request_options,
        )

    async def acquiring_algorithm_market_data(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SapiV1MiningPubAlgoListResponse, AcquiringAlgorithmMarketDataErrorBody]:
        """Weight(IP): 1

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/mining/pub/algoList"),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MiningPubAlgoListResponse],
            error_mapper=acquiring_algorithm_market_data_error_mapper,
            request_options=request_options,
        )

    async def acquiring_coin_name_market_data(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SapiV1MiningPubCoinListResponse, AcquiringCoinNameMarketDataErrorBody]:
        """Weight(IP): 1

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/mining/pub/coinList"),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MiningPubCoinListResponse],
            error_mapper=acquiring_coin_name_market_data_error_mapper,
            request_options=request_options,
        )

    async def cancel_hashrate_resale_configuration_user_data(
        self,
        config_id: str,
        user_name: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MiningHashTransferConfigCancelResponse, CancelHashrateResaleConfigurationUserDataErrorBody]:
        """Weight(IP): 5

        Args:
            config_id: Mining ID
            user_name: Mining Account
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/mining/hash-transfer/config/cancel"),
            query_params=[
                param[str]("configId", config_id),
                param[str]("userName", user_name),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MiningHashTransferConfigCancelResponse],
            error_mapper=cancel_hashrate_resale_configuration_user_data_error_mapper,
            request_options=request_options,
        )

    async def earnings_list_user_data(
        self,
        algo: str,
        user_name: str,
        timestamp: int,
        signature: str,
        *,
        coin: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        page_index: int | None = None,
        page_size: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MiningPaymentListResponse, EarningsListUserDataErrorBody]:
        """Weight(IP): 5

        Args:
            algo: Algorithm(sha256)
            user_name: Mining Account
            timestamp: UTC timestamp in ms
            signature: Signature
            coin: Coin name
            start_date: Search date, millisecond timestamp, while empty query all
            end_date: Search date, millisecond timestamp, while empty query all
            page_index: Page number, default is first page, start form 1
            page_size: Number of pages, minimum 10, maximum 200
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/mining/payment/list"),
            query_params=[
                param[str]("algo", algo),
                param[str]("userName", user_name),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("coin", coin),
                param[str | None]("startDate", start_date),
                param[str | None]("endDate", end_date),
                param[int | None]("pageIndex", page_index),
                param[str | None]("pageSize", page_size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MiningPaymentListResponse],
            error_mapper=earnings_list_user_data_error_mapper,
            request_options=request_options,
        )

    async def extra_bonus_list_user_data(
        self,
        algo: str,
        user_name: str,
        timestamp: int,
        signature: str,
        *,
        coin: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        page_index: int | None = None,
        page_size: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MiningPaymentOtherResponse, ExtraBonusListUserDataErrorBody]:
        """Weight(IP): 5

        Args:
            algo: Algorithm(sha256)
            user_name: Mining Account
            timestamp: UTC timestamp in ms
            signature: Signature
            coin: Coin name
            start_date: Search date, millisecond timestamp, while empty query all
            end_date: Search date, millisecond timestamp, while empty query all
            page_index: Page number, default is first page, start form 1
            page_size: Number of pages, minimum 10, maximum 200
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/mining/payment/other"),
            query_params=[
                param[str]("algo", algo),
                param[str]("userName", user_name),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("coin", coin),
                param[str | None]("startDate", start_date),
                param[str | None]("endDate", end_date),
                param[int | None]("pageIndex", page_index),
                param[str | None]("pageSize", page_size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MiningPaymentOtherResponse],
            error_mapper=extra_bonus_list_user_data_error_mapper,
            request_options=request_options,
        )

    async def hashrate_resale_details_user_data(
        self,
        config_id: str,
        user_name: str,
        timestamp: int,
        signature: str,
        *,
        page_index: int | None = None,
        page_size: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MiningHashTransferProfitDetailsResponse, HashrateResaleDetailsUserDataErrorBody]:
        """Weight(IP): 5

        Args:
            config_id: Mining ID
            user_name: Mining Account
            timestamp: UTC timestamp in ms
            signature: Signature
            page_index: Page number, default is first page, start form 1
            page_size: Number of pages, minimum 10, maximum 200
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/mining/hash-transfer/profit/details"),
            query_params=[
                param[str]("configId", config_id),
                param[str]("userName", user_name),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("pageIndex", page_index),
                param[str | None]("pageSize", page_size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MiningHashTransferProfitDetailsResponse],
            error_mapper=hashrate_resale_details_user_data_error_mapper,
            request_options=request_options,
        )

    async def hashrate_resale_list_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        page_index: int | None = None,
        page_size: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MiningHashTransferConfigDetailsListResponse, HashrateResaleListUserDataErrorBody]:
        """Weight(IP): 5

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            page_index: Page number, default is first page, start form 1
            page_size: Number of pages, minimum 10, maximum 200
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/mining/hash-transfer/config/details/list"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("pageIndex", page_index),
                param[str | None]("pageSize", page_size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MiningHashTransferConfigDetailsListResponse],
            error_mapper=hashrate_resale_list_user_data_error_mapper,
            request_options=request_options,
        )

    async def hashrate_resale_request_user_data(
        self,
        user_name: str,
        algo: str,
        to_pool_user: str,
        hash_rate: str,
        timestamp: int,
        signature: str,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MiningHashTransferConfigResponse, HashrateResaleRequestUserDataErrorBody]:
        """Weight(IP): 5

        Args:
            user_name: Mining Account
            algo: Algorithm(sha256)
            to_pool_user: Mining Account
            hash_rate: Resale hashrate h/s must be transferred (BTC is greater than 500000000000 ETH is greater than
                500000)
            timestamp: UTC timestamp in ms
            signature: Signature
            start_date: Search date, millisecond timestamp, while empty query all
            end_date: Search date, millisecond timestamp, while empty query all
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/mining/hash-transfer/config"),
            query_params=[
                param[str]("userName", user_name),
                param[str]("algo", algo),
                param[str]("toPoolUser", to_pool_user),
                param[str]("hashRate", hash_rate),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("startDate", start_date),
                param[str | None]("endDate", end_date),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MiningHashTransferConfigResponse],
            error_mapper=hashrate_resale_request_user_data_error_mapper,
            request_options=request_options,
        )

    async def mining_account_earning_user_data(
        self,
        algo: str,
        timestamp: int,
        signature: str,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        page_index: int | None = None,
        page_size: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MiningPaymentUidResponse, MiningAccountEarningUserDataErrorBody]:
        """Weight(IP): 5

        Args:
            algo: Algorithm(sha256)
            timestamp: UTC timestamp in ms
            signature: Signature
            start_date: Search date, millisecond timestamp, while empty query all
            end_date: Search date, millisecond timestamp, while empty query all
            page_index: Page number, default is first page, start form 1
            page_size: Number of pages, minimum 10, maximum 200
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/mining/payment/uid"),
            query_params=[
                param[str]("algo", algo),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("startDate", start_date),
                param[str | None]("endDate", end_date),
                param[int | None]("pageIndex", page_index),
                param[str | None]("pageSize", page_size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MiningPaymentUidResponse],
            error_mapper=mining_account_earning_user_data_error_mapper,
            request_options=request_options,
        )

    async def request_for_detail_miner_list_user_data(
        self,
        algo: str,
        user_name: str,
        worker_name: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MiningWorkerDetailResponse, RequestForDetailMinerListUserDataErrorBody]:
        """Weight(IP): 5

        Args:
            algo: Algorithm(sha256)
            user_name: Mining Account
            worker_name: Miner’s name
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/mining/worker/detail"),
            query_params=[
                param[str]("algo", algo),
                param[str]("userName", user_name),
                param[str]("workerName", worker_name),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MiningWorkerDetailResponse],
            error_mapper=request_for_detail_miner_list_user_data_error_mapper,
            request_options=request_options,
        )

    async def request_for_miner_list_user_data(
        self,
        algo: str,
        user_name: str,
        timestamp: int,
        signature: str,
        *,
        page_index: int | None = None,
        sort: int | None = None,
        sort_column: int | None = None,
        worker_status: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MiningWorkerListResponse, RequestForMinerListUserDataErrorBody]:
        """Weight(IP): 5

        Args:
            algo: Algorithm(sha256)
            user_name: Mining Account
            timestamp: UTC timestamp in ms
            signature: Signature
            page_index: Page number, default is first page, start form 1
            sort: sort sequence(default=0)0 positive sequence, 1 negative sequence
            sort_column: Sort by( default 1): 1: miner name, 2: real-time computing power, 3: daily average computing
                power, 4: real-time rejection rate, 5: last submission time
            worker_status: miners status(default=0)0 all, 1 valid, 2 invalid, 3 failure
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/mining/worker/list"),
            query_params=[
                param[str]("algo", algo),
                param[str]("userName", user_name),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("pageIndex", page_index),
                param[int | None]("sort", sort),
                param[int | None]("sortColumn", sort_column),
                param[int | None]("workerStatus", worker_status),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MiningWorkerListResponse],
            error_mapper=request_for_miner_list_user_data_error_mapper,
            request_options=request_options,
        )

    async def statistic_list_user_data(
        self,
        algo: str,
        user_name: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1MiningStatisticsUserStatusResponse, StatisticListUserDataErrorBody]:
        """Weight(IP): 5

        Args:
            algo: Algorithm(sha256)
            user_name: Mining Account
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/mining/statistics/user/status"),
            query_params=[
                param[str]("algo", algo),
                param[str]("userName", user_name),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1MiningStatisticsUserStatusResponse],
            error_mapper=statistic_list_user_data_error_mapper,
            request_options=request_options,
        )
