from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder, param
from ..errors.bnb_transfer_user_data_error import BnbTransferUserDataErrorBody, bnb_transfer_user_data_error_mapper
from ..errors.change_auto_repay_futures_status_user_data_error import (
    ChangeAutoRepayFuturesStatusUserDataErrorBody,
    change_auto_repay_futures_status_user_data_error_mapper,
)
from ..errors.fund_auto_collection_user_data_error import (
    FundAutoCollectionUserDataErrorBody,
    fund_auto_collection_user_data_error_mapper,
)
from ..errors.fund_collection_by_asset_user_data_error import (
    FundCollectionByAssetUserDataErrorBody,
    fund_collection_by_asset_user_data_error_mapper,
)
from ..errors.get_auto_repay_futures_status_user_data_error import (
    GetAutoRepayFuturesStatusUserDataErrorBody,
    get_auto_repay_futures_status_user_data_error_mapper,
)
from ..errors.get_portfolio_margin_asset_leverage_user_data_error import (
    GetPortfolioMarginAssetLeverageUserDataErrorBody,
    get_portfolio_margin_asset_leverage_user_data_error_mapper,
)
from ..errors.portfolio_margin_account_user_data_error import (
    PortfolioMarginAccountUserDataErrorBody,
    portfolio_margin_account_user_data_error_mapper,
)
from ..errors.portfolio_margin_bankruptcy_loan_amount_user_data_error import (
    PortfolioMarginBankruptcyLoanAmountUserDataErrorBody,
    portfolio_margin_bankruptcy_loan_amount_user_data_error_mapper,
)
from ..errors.portfolio_margin_bankruptcy_loan_repay_user_data_error import (
    PortfolioMarginBankruptcyLoanRepayUserDataErrorBody,
    portfolio_margin_bankruptcy_loan_repay_user_data_error_mapper,
)
from ..errors.portfolio_margin_collateral_rate_market_data_error import (
    PortfolioMarginCollateralRateMarketDataErrorBody,
    portfolio_margin_collateral_rate_market_data_error_mapper,
)
from ..errors.portfolio_margin_pro_tiered_collateral_rate_user_data_error import (
    PortfolioMarginProTieredCollateralRateUserDataErrorBody,
    portfolio_margin_pro_tiered_collateral_rate_user_data_error_mapper,
)
from ..errors.query_classic_portfolio_margin_negative_balance_interest_history_user_data_error import (
    QueryClassicPortfolioMarginNegativeBalanceInterestHistoryUserDataErrorBody,
    query_classic_portfolio_margin_negative_balance_interest_history_user_data_error_mapper,
)
from ..errors.query_portfolio_margin_asset_index_price_market_data_error import (
    QueryPortfolioMarginAssetIndexPriceMarketDataErrorBody,
    query_portfolio_margin_asset_index_price_market_data_error_mapper,
)
from ..errors.repay_futures_negative_balance_user_data_error import (
    RepayFuturesNegativeBalanceUserDataErrorBody,
    repay_futures_negative_balance_user_data_error_mapper,
)
from ..models.enums.transfer_side import TransferSideOrStr
from ..models.sapi_v1_portfolio_account_response import SapiV1PortfolioAccountResponse
from ..models.sapi_v1_portfolio_asset_collection_response import SapiV1PortfolioAssetCollectionResponse
from ..models.sapi_v1_portfolio_asset_index_price_response import SapiV1PortfolioAssetIndexPriceResponse
from ..models.sapi_v1_portfolio_auto_collection_response import SapiV1PortfolioAutoCollectionResponse
from ..models.sapi_v1_portfolio_bnb_transfer_response import SapiV1PortfolioBnbTransferResponse
from ..models.sapi_v1_portfolio_collateral_rate_response import SapiV1PortfolioCollateralRateResponse
from ..models.sapi_v1_portfolio_interest_history_response import SapiV1PortfolioInterestHistoryResponse
from ..models.sapi_v1_portfolio_margin_asset_leverage_response import SapiV1PortfolioMarginAssetLeverageResponse
from ..models.sapi_v1_portfolio_pm_loan_response import SapiV1PortfolioPmLoanResponse
from ..models.sapi_v1_portfolio_repay_futures_negative_balance_response import (
    SapiV1PortfolioRepayFuturesNegativeBalanceResponse,
)
from ..models.sapi_v1_portfolio_repay_futures_switch_response import SapiV1PortfolioRepayFuturesSwitchResponse
from ..models.sapi_v1_portfolio_repay_futures_switch_response1 import SapiV1PortfolioRepayFuturesSwitchResponse1
from ..models.sapi_v1_portfolio_repay_response import SapiV1PortfolioRepayResponse
from ..models.sapi_v2_portfolio_collateral_rate_response import SapiV2PortfolioCollateralRateResponse
from ..server.server import Server


class PortfolioMargin:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = PortfolioMarginWithRawResponse(client, server, auth)

    def bnb_transfer_user_data(
        self,
        transfer_side: TransferSideOrStr,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1PortfolioBnbTransferResponse:
        """BNB transfer can be between Margin Account and USDM Account

        Weight(IP): 1500

        Args:
            transfer_side: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.bnb_transfer_user_data(
            transfer_side, amount, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def change_auto_repay_futures_status_user_data(
        self,
        auto_repay: bool,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1PortfolioRepayFuturesSwitchResponse:
        """Change Auto-repay-futures Status

        Weight(IP): 1500

        Args:
            auto_repay: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.change_auto_repay_futures_status_user_data(
            auto_repay, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def fund_auto_collection_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1PortfolioAutoCollectionResponse:
        """Transfers all assets from Futures Account to Margin account

        Weight(IP): 1500

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.fund_auto_collection_user_data(
            timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def fund_collection_by_asset_user_data(
        self,
        asset: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1PortfolioAssetCollectionResponse:
        """Transfers specific asset from Futures Account to Margin account

        Weight(IP): 60

        Args:
            asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.fund_collection_by_asset_user_data(
            asset, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def get_auto_repay_futures_status_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1PortfolioRepayFuturesSwitchResponse1:
        """Query Auto-repay-futures Status

        Weight(IP): 30

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_auto_repay_futures_status_user_data(
            timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def get_portfolio_margin_asset_leverage_user_data(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[SapiV1PortfolioMarginAssetLeverageResponse]:
        """Weight(IP): 50

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Classic Portfolio Margin Collateral Rate

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_portfolio_margin_asset_leverage_user_data(
            request_options=request_options
        ).unwrap()

    def portfolio_margin_account_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1PortfolioAccountResponse:
        """Get the account info

        'Weight(IP): 1'

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Portfolio account.

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.portfolio_margin_account_user_data(
            timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def portfolio_margin_bankruptcy_loan_amount_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1PortfolioPmLoanResponse:
        """Query Portfolio Margin Bankruptcy Loan Amount.

        Weight(UID): 500

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Portfolio Margin Bankruptcy Loan Amount.

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.portfolio_margin_bankruptcy_loan_amount_user_data(
            timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def portfolio_margin_bankruptcy_loan_repay_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        from_: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1PortfolioRepayResponse:
        """Repay Portfolio Margin Bankruptcy Loan.

        Weight(UID): 3000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            from_: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Transaction.

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.portfolio_margin_bankruptcy_loan_repay_user_data(
            timestamp, signature, from_=from_, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def portfolio_margin_collateral_rate_market_data(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[SapiV1PortfolioCollateralRateResponse]:
        """Portfolio Margin Collateral Rate.

        Weight(IP): 50

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Portfolio Margin Collateral Rate.

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.portfolio_margin_collateral_rate_market_data(
            request_options=request_options
        ).unwrap()

    def portfolio_margin_pro_tiered_collateral_rate_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV2PortfolioCollateralRateResponse]:
        """Portfolio Margin PRO Tiered Collateral Rate

        Weight(IP): 50

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Portfolio Margin Collateral Rate.

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.portfolio_margin_pro_tiered_collateral_rate_user_data(
            timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def query_classic_portfolio_margin_negative_balance_interest_history_user_data(
        self,
        asset: str,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1PortfolioInterestHistoryResponse]:
        """Query interest history of negative balance for portfolio margin.

        Weight(IP): 50

        Args:
            asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Balance interest history

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_classic_portfolio_margin_negative_balance_interest_history_user_data(
            asset,
            timestamp,
            signature,
            start_time=start_time,
            end_time=end_time,
            size=size,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def query_portfolio_margin_asset_index_price_market_data(
        self, *, asset: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> list[SapiV1PortfolioAssetIndexPriceResponse]:
        """Query Portfolio Margin Asset Index Price

        Weight(IP):
        - 1 if send asset
        - 50 if not send asset

        Args:
            asset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            asset price index

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.query_portfolio_margin_asset_index_price_market_data(
            asset=asset, request_options=request_options
        ).unwrap()

    def repay_futures_negative_balance_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1PortfolioRepayFuturesNegativeBalanceResponse:
        """Repay futures Negative Balance

        Weight(IP): 1500

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.repay_futures_negative_balance_user_data(
            timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> PortfolioMarginWithRawResponse:
        return self._with_raw_response


class AsyncPortfolioMargin:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncPortfolioMarginWithRawResponse(client, server, auth)

    async def bnb_transfer_user_data(
        self,
        transfer_side: TransferSideOrStr,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1PortfolioBnbTransferResponse:
        """BNB transfer can be between Margin Account and USDM Account

        Weight(IP): 1500

        Args:
            transfer_side: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.bnb_transfer_user_data(
                transfer_side, amount, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def change_auto_repay_futures_status_user_data(
        self,
        auto_repay: bool,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1PortfolioRepayFuturesSwitchResponse:
        """Change Auto-repay-futures Status

        Weight(IP): 1500

        Args:
            auto_repay: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.change_auto_repay_futures_status_user_data(
                auto_repay, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def fund_auto_collection_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1PortfolioAutoCollectionResponse:
        """Transfers all assets from Futures Account to Margin account

        Weight(IP): 1500

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.fund_auto_collection_user_data(
                timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def fund_collection_by_asset_user_data(
        self,
        asset: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1PortfolioAssetCollectionResponse:
        """Transfers specific asset from Futures Account to Margin account

        Weight(IP): 60

        Args:
            asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.fund_collection_by_asset_user_data(
                asset, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def get_auto_repay_futures_status_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1PortfolioRepayFuturesSwitchResponse1:
        """Query Auto-repay-futures Status

        Weight(IP): 30

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_auto_repay_futures_status_user_data(
                timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def get_portfolio_margin_asset_leverage_user_data(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[SapiV1PortfolioMarginAssetLeverageResponse]:
        """Weight(IP): 50

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Classic Portfolio Margin Collateral Rate

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_portfolio_margin_asset_leverage_user_data(request_options=request_options)
        ).unwrap()

    async def portfolio_margin_account_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1PortfolioAccountResponse:
        """Get the account info

        'Weight(IP): 1'

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Portfolio account.

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.portfolio_margin_account_user_data(
                timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def portfolio_margin_bankruptcy_loan_amount_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1PortfolioPmLoanResponse:
        """Query Portfolio Margin Bankruptcy Loan Amount.

        Weight(UID): 500

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Portfolio Margin Bankruptcy Loan Amount.

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.portfolio_margin_bankruptcy_loan_amount_user_data(
                timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def portfolio_margin_bankruptcy_loan_repay_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        from_: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1PortfolioRepayResponse:
        """Repay Portfolio Margin Bankruptcy Loan.

        Weight(UID): 3000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            from_: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Transaction.

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.portfolio_margin_bankruptcy_loan_repay_user_data(
                timestamp, signature, from_=from_, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def portfolio_margin_collateral_rate_market_data(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[SapiV1PortfolioCollateralRateResponse]:
        """Portfolio Margin Collateral Rate.

        Weight(IP): 50

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Portfolio Margin Collateral Rate.

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.portfolio_margin_collateral_rate_market_data(request_options=request_options)
        ).unwrap()

    async def portfolio_margin_pro_tiered_collateral_rate_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV2PortfolioCollateralRateResponse]:
        """Portfolio Margin PRO Tiered Collateral Rate

        Weight(IP): 50

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Portfolio Margin Collateral Rate.

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.portfolio_margin_pro_tiered_collateral_rate_user_data(
                timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def query_classic_portfolio_margin_negative_balance_interest_history_user_data(
        self,
        asset: str,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SapiV1PortfolioInterestHistoryResponse]:
        """Query interest history of negative balance for portfolio margin.

        Weight(IP): 50

        Args:
            asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Balance interest history

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_classic_portfolio_margin_negative_balance_interest_history_user_data(
                asset,
                timestamp,
                signature,
                start_time=start_time,
                end_time=end_time,
                size=size,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def query_portfolio_margin_asset_index_price_market_data(
        self, *, asset: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> list[SapiV1PortfolioAssetIndexPriceResponse]:
        """Query Portfolio Margin Asset Index Price

        Weight(IP):
        - 1 if send asset
        - 50 if not send asset

        Args:
            asset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            asset price index

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.query_portfolio_margin_asset_index_price_market_data(
                asset=asset, request_options=request_options
            )
        ).unwrap()

    async def repay_futures_negative_balance_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1PortfolioRepayFuturesNegativeBalanceResponse:
        """Repay futures Negative Balance

        Weight(IP): 1500

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Result

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.repay_futures_negative_balance_user_data(
                timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncPortfolioMarginWithRawResponse:
        return self._with_raw_response


class PortfolioMarginWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def bnb_transfer_user_data(
        self,
        transfer_side: TransferSideOrStr,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1PortfolioBnbTransferResponse, BnbTransferUserDataErrorBody]:
        """BNB transfer can be between Margin Account and USDM Account

        Weight(IP): 1500

        Args:
            transfer_side: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/portfolio/bnb-transfer"),
            query_params=[
                param[TransferSideOrStr]("transferSide", transfer_side),
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1PortfolioBnbTransferResponse],
            error_mapper=bnb_transfer_user_data_error_mapper,
            request_options=request_options,
        )

    def change_auto_repay_futures_status_user_data(
        self,
        auto_repay: bool,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1PortfolioRepayFuturesSwitchResponse, ChangeAutoRepayFuturesStatusUserDataErrorBody]:
        """Change Auto-repay-futures Status

        Weight(IP): 1500

        Args:
            auto_repay: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/portfolio/repay-futures-switch"),
            query_params=[
                param[bool]("autoRepay", auto_repay),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1PortfolioRepayFuturesSwitchResponse],
            error_mapper=change_auto_repay_futures_status_user_data_error_mapper,
            request_options=request_options,
        )

    def fund_auto_collection_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1PortfolioAutoCollectionResponse, FundAutoCollectionUserDataErrorBody]:
        """Transfers all assets from Futures Account to Margin account

        Weight(IP): 1500

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/portfolio/auto-collection"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1PortfolioAutoCollectionResponse],
            error_mapper=fund_auto_collection_user_data_error_mapper,
            request_options=request_options,
        )

    def fund_collection_by_asset_user_data(
        self,
        asset: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1PortfolioAssetCollectionResponse, FundCollectionByAssetUserDataErrorBody]:
        """Transfers specific asset from Futures Account to Margin account

        Weight(IP): 60

        Args:
            asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/portfolio/asset-collection"),
            query_params=[
                param[str]("asset", asset),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1PortfolioAssetCollectionResponse],
            error_mapper=fund_collection_by_asset_user_data_error_mapper,
            request_options=request_options,
        )

    def get_auto_repay_futures_status_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1PortfolioRepayFuturesSwitchResponse1, GetAutoRepayFuturesStatusUserDataErrorBody]:
        """Query Auto-repay-futures Status

        Weight(IP): 30

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/portfolio/repay-futures-switch"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1PortfolioRepayFuturesSwitchResponse1],
            error_mapper=get_auto_repay_futures_status_user_data_error_mapper,
            request_options=request_options,
        )

    def get_portfolio_margin_asset_leverage_user_data(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[SapiV1PortfolioMarginAssetLeverageResponse], GetPortfolioMarginAssetLeverageUserDataErrorBody]:
        """Weight(IP): 50

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/portfolio/margin-asset-leverage"),
            decoder=json_decoder[list[SapiV1PortfolioMarginAssetLeverageResponse]],
            error_mapper=get_portfolio_margin_asset_leverage_user_data_error_mapper,
            request_options=request_options,
        )

    def portfolio_margin_account_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1PortfolioAccountResponse, PortfolioMarginAccountUserDataErrorBody]:
        """Get the account info

        'Weight(IP): 1'

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/portfolio/account"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1PortfolioAccountResponse],
            error_mapper=portfolio_margin_account_user_data_error_mapper,
            request_options=request_options,
        )

    def portfolio_margin_bankruptcy_loan_amount_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1PortfolioPmLoanResponse, PortfolioMarginBankruptcyLoanAmountUserDataErrorBody]:
        """Query Portfolio Margin Bankruptcy Loan Amount.

        Weight(UID): 500

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/portfolio/pmLoan"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1PortfolioPmLoanResponse],
            error_mapper=portfolio_margin_bankruptcy_loan_amount_user_data_error_mapper,
            request_options=request_options,
        )

    def portfolio_margin_bankruptcy_loan_repay_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        from_: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1PortfolioRepayResponse, PortfolioMarginBankruptcyLoanRepayUserDataErrorBody]:
        """Repay Portfolio Margin Bankruptcy Loan.

        Weight(UID): 3000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            from_: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/portfolio/repay"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("from", from_),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1PortfolioRepayResponse],
            error_mapper=portfolio_margin_bankruptcy_loan_repay_user_data_error_mapper,
            request_options=request_options,
        )

    def portfolio_margin_collateral_rate_market_data(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[SapiV1PortfolioCollateralRateResponse], PortfolioMarginCollateralRateMarketDataErrorBody]:
        """Portfolio Margin Collateral Rate.

        Weight(IP): 50

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/portfolio/collateralRate"),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1PortfolioCollateralRateResponse]],
            error_mapper=portfolio_margin_collateral_rate_market_data_error_mapper,
            request_options=request_options,
        )

    def portfolio_margin_pro_tiered_collateral_rate_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        list[SapiV2PortfolioCollateralRateResponse], PortfolioMarginProTieredCollateralRateUserDataErrorBody
    ]:
        """Portfolio Margin PRO Tiered Collateral Rate

        Weight(IP): 50

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v2/portfolio/collateralRate"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV2PortfolioCollateralRateResponse]],
            error_mapper=portfolio_margin_pro_tiered_collateral_rate_user_data_error_mapper,
            request_options=request_options,
        )

    def query_classic_portfolio_margin_negative_balance_interest_history_user_data(
        self,
        asset: str,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        list[SapiV1PortfolioInterestHistoryResponse],
        QueryClassicPortfolioMarginNegativeBalanceInterestHistoryUserDataErrorBody,
    ]:
        """Query interest history of negative balance for portfolio margin.

        Weight(IP): 50

        Args:
            asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/portfolio/interest-history"),
            query_params=[
                param[str]("asset", asset),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1PortfolioInterestHistoryResponse]],
            error_mapper=query_classic_portfolio_margin_negative_balance_interest_history_user_data_error_mapper,
            request_options=request_options,
        )

    def query_portfolio_margin_asset_index_price_market_data(
        self, *, asset: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[
        list[SapiV1PortfolioAssetIndexPriceResponse], QueryPortfolioMarginAssetIndexPriceMarketDataErrorBody
    ]:
        """Query Portfolio Margin Asset Index Price

        Weight(IP):
        - 1 if send asset
        - 50 if not send asset

        Args:
            asset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/portfolio/asset-index-price"),
            query_params=[param[str | None]("asset", asset)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1PortfolioAssetIndexPriceResponse]],
            error_mapper=query_portfolio_margin_asset_index_price_market_data_error_mapper,
            request_options=request_options,
        )

    def repay_futures_negative_balance_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1PortfolioRepayFuturesNegativeBalanceResponse, RepayFuturesNegativeBalanceUserDataErrorBody]:
        """Repay futures Negative Balance

        Weight(IP): 1500

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/portfolio/repay-futures-negative-balance"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1PortfolioRepayFuturesNegativeBalanceResponse],
            error_mapper=repay_futures_negative_balance_user_data_error_mapper,
            request_options=request_options,
        )


class AsyncPortfolioMarginWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def bnb_transfer_user_data(
        self,
        transfer_side: TransferSideOrStr,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1PortfolioBnbTransferResponse, BnbTransferUserDataErrorBody]:
        """BNB transfer can be between Margin Account and USDM Account

        Weight(IP): 1500

        Args:
            transfer_side: Value sent with the request.
            amount: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/portfolio/bnb-transfer"),
            query_params=[
                param[TransferSideOrStr]("transferSide", transfer_side),
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1PortfolioBnbTransferResponse],
            error_mapper=bnb_transfer_user_data_error_mapper,
            request_options=request_options,
        )

    async def change_auto_repay_futures_status_user_data(
        self,
        auto_repay: bool,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1PortfolioRepayFuturesSwitchResponse, ChangeAutoRepayFuturesStatusUserDataErrorBody]:
        """Change Auto-repay-futures Status

        Weight(IP): 1500

        Args:
            auto_repay: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/portfolio/repay-futures-switch"),
            query_params=[
                param[bool]("autoRepay", auto_repay),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1PortfolioRepayFuturesSwitchResponse],
            error_mapper=change_auto_repay_futures_status_user_data_error_mapper,
            request_options=request_options,
        )

    async def fund_auto_collection_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1PortfolioAutoCollectionResponse, FundAutoCollectionUserDataErrorBody]:
        """Transfers all assets from Futures Account to Margin account

        Weight(IP): 1500

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/portfolio/auto-collection"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1PortfolioAutoCollectionResponse],
            error_mapper=fund_auto_collection_user_data_error_mapper,
            request_options=request_options,
        )

    async def fund_collection_by_asset_user_data(
        self,
        asset: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1PortfolioAssetCollectionResponse, FundCollectionByAssetUserDataErrorBody]:
        """Transfers specific asset from Futures Account to Margin account

        Weight(IP): 60

        Args:
            asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/portfolio/asset-collection"),
            query_params=[
                param[str]("asset", asset),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1PortfolioAssetCollectionResponse],
            error_mapper=fund_collection_by_asset_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_auto_repay_futures_status_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1PortfolioRepayFuturesSwitchResponse1, GetAutoRepayFuturesStatusUserDataErrorBody]:
        """Query Auto-repay-futures Status

        Weight(IP): 30

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/portfolio/repay-futures-switch"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1PortfolioRepayFuturesSwitchResponse1],
            error_mapper=get_auto_repay_futures_status_user_data_error_mapper,
            request_options=request_options,
        )

    async def get_portfolio_margin_asset_leverage_user_data(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[SapiV1PortfolioMarginAssetLeverageResponse], GetPortfolioMarginAssetLeverageUserDataErrorBody]:
        """Weight(IP): 50

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/portfolio/margin-asset-leverage"),
            decoder=json_decoder[list[SapiV1PortfolioMarginAssetLeverageResponse]],
            error_mapper=get_portfolio_margin_asset_leverage_user_data_error_mapper,
            request_options=request_options,
        )

    async def portfolio_margin_account_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1PortfolioAccountResponse, PortfolioMarginAccountUserDataErrorBody]:
        """Get the account info

        'Weight(IP): 1'

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/portfolio/account"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1PortfolioAccountResponse],
            error_mapper=portfolio_margin_account_user_data_error_mapper,
            request_options=request_options,
        )

    async def portfolio_margin_bankruptcy_loan_amount_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1PortfolioPmLoanResponse, PortfolioMarginBankruptcyLoanAmountUserDataErrorBody]:
        """Query Portfolio Margin Bankruptcy Loan Amount.

        Weight(UID): 500

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/portfolio/pmLoan"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1PortfolioPmLoanResponse],
            error_mapper=portfolio_margin_bankruptcy_loan_amount_user_data_error_mapper,
            request_options=request_options,
        )

    async def portfolio_margin_bankruptcy_loan_repay_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        from_: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1PortfolioRepayResponse, PortfolioMarginBankruptcyLoanRepayUserDataErrorBody]:
        """Repay Portfolio Margin Bankruptcy Loan.

        Weight(UID): 3000

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            from_: Value sent with the request.
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/portfolio/repay"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("from", from_),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1PortfolioRepayResponse],
            error_mapper=portfolio_margin_bankruptcy_loan_repay_user_data_error_mapper,
            request_options=request_options,
        )

    async def portfolio_margin_collateral_rate_market_data(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[SapiV1PortfolioCollateralRateResponse], PortfolioMarginCollateralRateMarketDataErrorBody]:
        """Portfolio Margin Collateral Rate.

        Weight(IP): 50

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/portfolio/collateralRate"),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1PortfolioCollateralRateResponse]],
            error_mapper=portfolio_margin_collateral_rate_market_data_error_mapper,
            request_options=request_options,
        )

    async def portfolio_margin_pro_tiered_collateral_rate_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        list[SapiV2PortfolioCollateralRateResponse], PortfolioMarginProTieredCollateralRateUserDataErrorBody
    ]:
        """Portfolio Margin PRO Tiered Collateral Rate

        Weight(IP): 50

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v2/portfolio/collateralRate"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV2PortfolioCollateralRateResponse]],
            error_mapper=portfolio_margin_pro_tiered_collateral_rate_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_classic_portfolio_margin_negative_balance_interest_history_user_data(
        self,
        asset: str,
        timestamp: int,
        signature: str,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        size: int | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        list[SapiV1PortfolioInterestHistoryResponse],
        QueryClassicPortfolioMarginNegativeBalanceInterestHistoryUserDataErrorBody,
    ]:
        """Query interest history of negative balance for portfolio margin.

        Weight(IP): 50

        Args:
            asset: Value sent with the request.
            timestamp: UTC timestamp in ms
            signature: Signature
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            size: Default:10 Max:100
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/portfolio/interest-history"),
            query_params=[
                param[str]("asset", asset),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("size", size),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1PortfolioInterestHistoryResponse]],
            error_mapper=query_classic_portfolio_margin_negative_balance_interest_history_user_data_error_mapper,
            request_options=request_options,
        )

    async def query_portfolio_margin_asset_index_price_market_data(
        self, *, asset: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[
        list[SapiV1PortfolioAssetIndexPriceResponse], QueryPortfolioMarginAssetIndexPriceMarketDataErrorBody
    ]:
        """Query Portfolio Margin Asset Index Price

        Weight(IP):
        - 1 if send asset
        - 50 if not send asset

        Args:
            asset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/portfolio/asset-index-price"),
            query_params=[param[str | None]("asset", asset)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[list[SapiV1PortfolioAssetIndexPriceResponse]],
            error_mapper=query_portfolio_margin_asset_index_price_market_data_error_mapper,
            request_options=request_options,
        )

    async def repay_futures_negative_balance_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1PortfolioRepayFuturesNegativeBalanceResponse, RepayFuturesNegativeBalanceUserDataErrorBody]:
        """Repay futures Negative Balance

        Weight(IP): 1500

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/portfolio/repay-futures-negative-balance"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1PortfolioRepayFuturesNegativeBalanceResponse],
            error_mapper=repay_futures_negative_balance_user_data_error_mapper,
            request_options=request_options,
        )
