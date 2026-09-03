from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.auto_invest import AsyncAutoInvest
from .apis.blvt import AsyncBlvt
from .apis.c2_c import AsyncC2C
from .apis.convert import AsyncConvert
from .apis.copy_trading import AsyncCopyTrading
from .apis.crypto_loans import AsyncCryptoLoans
from .apis.dual_investment import AsyncDualInvestment
from .apis.fiat import AsyncFiat
from .apis.futures import AsyncFutures
from .apis.futures_algo import AsyncFuturesAlgo
from .apis.gift_card import AsyncGiftCard
from .apis.isolated_margin_stream import AsyncIsolatedMarginStream
from .apis.margin import AsyncMargin
from .apis.margin_stream import AsyncMarginStream
from .apis.market import AsyncMarket
from .apis.mining import AsyncMining
from .apis.nft import AsyncNft
from .apis.pay import AsyncPay
from .apis.portfolio_margin import AsyncPortfolioMargin
from .apis.rebate import AsyncRebate
from .apis.savings import AsyncSavings
from .apis.simple_earn import AsyncSimpleEarn
from .apis.spot_algo import AsyncSpotAlgo
from .apis.staking import AsyncStaking
from .apis.stream import AsyncStream
from .apis.sub_account_api import AsyncSubAccountApi
from .apis.trade_api import AsyncTradeApi
from .apis.vip_loans import AsyncVipLoans
from .apis.wallet import AsyncWallet
from .auth import AsyncAuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseBinancePublicSpotApiClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    ApiKeyHeaderScheme,
    AsyncHttpClient,
    AsyncHttpxClient,
    AsyncRawClient,
    no_auth,
    param,
)
from .server.environment import Environment


class AsyncBinancePublicSpotApiClient(BaseBinancePublicSpotApiClient[AsyncRawClient]):
    def __init__(
        self,
        *,
        environment: Environment = "production",
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        custom_async_http_client: AsyncHttpClient | None = None,
        api_key_auth: str | None = None,
    ) -> None:
        super().__init__(environment=environment, base_url=base_url, timeout=timeout)
        self._raw_client = AsyncRawClient(
            http_client=(
                custom_async_http_client if custom_async_http_client is not None else AsyncHttpxClient(timeout=timeout)
            ),
            global_headers=[
                param[str]("User-Agent", "BinancePublicSpotApiClient/1.0 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "1.0"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AsyncAuthSchemes(
            api_key_auth=ApiKeyHeaderScheme("X-MBX-APIKEY", api_key_auth) if api_key_auth is not None else no_auth
        )

    @cached_property
    def auto_invest(self) -> AsyncAutoInvest:
        return AsyncAutoInvest(self._raw_client, self._server, self._auth)

    @cached_property
    def blvt(self) -> AsyncBlvt:
        return AsyncBlvt(self._raw_client, self._server, self._auth)

    @cached_property
    def c2_c(self) -> AsyncC2C:
        return AsyncC2C(self._raw_client, self._server, self._auth)

    @cached_property
    def convert(self) -> AsyncConvert:
        return AsyncConvert(self._raw_client, self._server, self._auth)

    @cached_property
    def copy_trading(self) -> AsyncCopyTrading:
        return AsyncCopyTrading(self._raw_client, self._server, self._auth)

    @cached_property
    def crypto_loans(self) -> AsyncCryptoLoans:
        return AsyncCryptoLoans(self._raw_client, self._server, self._auth)

    @cached_property
    def dual_investment(self) -> AsyncDualInvestment:
        return AsyncDualInvestment(self._raw_client, self._server, self._auth)

    @cached_property
    def fiat(self) -> AsyncFiat:
        return AsyncFiat(self._raw_client, self._server, self._auth)

    @cached_property
    def futures(self) -> AsyncFutures:
        return AsyncFutures(self._raw_client, self._server, self._auth)

    @cached_property
    def futures_algo(self) -> AsyncFuturesAlgo:
        return AsyncFuturesAlgo(self._raw_client, self._server, self._auth)

    @cached_property
    def gift_card(self) -> AsyncGiftCard:
        return AsyncGiftCard(self._raw_client, self._server, self._auth)

    @cached_property
    def isolated_margin_stream(self) -> AsyncIsolatedMarginStream:
        return AsyncIsolatedMarginStream(self._raw_client, self._server, self._auth)

    @cached_property
    def margin(self) -> AsyncMargin:
        return AsyncMargin(self._raw_client, self._server, self._auth)

    @cached_property
    def margin_stream(self) -> AsyncMarginStream:
        return AsyncMarginStream(self._raw_client, self._server, self._auth)

    @cached_property
    def market(self) -> AsyncMarket:
        return AsyncMarket(self._raw_client, self._server)

    @cached_property
    def mining(self) -> AsyncMining:
        return AsyncMining(self._raw_client, self._server, self._auth)

    @cached_property
    def nft(self) -> AsyncNft:
        return AsyncNft(self._raw_client, self._server, self._auth)

    @cached_property
    def pay(self) -> AsyncPay:
        return AsyncPay(self._raw_client, self._server, self._auth)

    @cached_property
    def portfolio_margin(self) -> AsyncPortfolioMargin:
        return AsyncPortfolioMargin(self._raw_client, self._server, self._auth)

    @cached_property
    def rebate(self) -> AsyncRebate:
        return AsyncRebate(self._raw_client, self._server, self._auth)

    @cached_property
    def savings(self) -> AsyncSavings:
        return AsyncSavings(self._raw_client, self._server, self._auth)

    @cached_property
    def simple_earn(self) -> AsyncSimpleEarn:
        return AsyncSimpleEarn(self._raw_client, self._server, self._auth)

    @cached_property
    def spot_algo(self) -> AsyncSpotAlgo:
        return AsyncSpotAlgo(self._raw_client, self._server, self._auth)

    @cached_property
    def staking(self) -> AsyncStaking:
        return AsyncStaking(self._raw_client, self._server, self._auth)

    @cached_property
    def stream(self) -> AsyncStream:
        return AsyncStream(self._raw_client, self._server, self._auth)

    @cached_property
    def sub_account_api(self) -> AsyncSubAccountApi:
        return AsyncSubAccountApi(self._raw_client, self._server, self._auth)

    @cached_property
    def trade_api(self) -> AsyncTradeApi:
        return AsyncTradeApi(self._raw_client, self._server, self._auth)

    @cached_property
    def vip_loans(self) -> AsyncVipLoans:
        return AsyncVipLoans(self._raw_client, self._server, self._auth)

    @cached_property
    def wallet(self) -> AsyncWallet:
        return AsyncWallet(self._raw_client, self._server, self._auth)

    async def aclose(self) -> None:
        await self._raw_client.http_client.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        await self.aclose()


AsyncClient = AsyncBinancePublicSpotApiClient
