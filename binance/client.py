from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.auto_invest import AutoInvest
from .apis.blvt import Blvt
from .apis.c2_c import C2C
from .apis.convert import Convert
from .apis.copy_trading import CopyTrading
from .apis.crypto_loans import CryptoLoans
from .apis.dual_investment import DualInvestment
from .apis.fiat import Fiat
from .apis.futures import Futures
from .apis.futures_algo import FuturesAlgo
from .apis.gift_card import GiftCard
from .apis.isolated_margin_stream import IsolatedMarginStream
from .apis.margin import Margin
from .apis.margin_stream import MarginStream
from .apis.market import Market
from .apis.mining import Mining
from .apis.nft import Nft
from .apis.pay import Pay
from .apis.portfolio_margin import PortfolioMargin
from .apis.rebate import Rebate
from .apis.savings import Savings
from .apis.simple_earn import SimpleEarn
from .apis.spot_algo import SpotAlgo
from .apis.staking import Staking
from .apis.stream import Stream
from .apis.sub_account_api import SubAccountApi
from .apis.trade_api import TradeApi
from .apis.vip_loans import VipLoans
from .apis.wallet import Wallet
from .auth import AuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseBinanceClient
from .core import ApiKeyHeaderScheme, HttpClient, HttpxClient, RawClient, no_auth
from .server.environment import Environment


class BinanceClient(BaseBinanceClient[RawClient]):
    def __init__(
        self,
        *,
        environment: Environment = "production",
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        custom_http_client: HttpClient | None = None,
        api_key_auth: str | None = None,
    ) -> None:
        super().__init__(environment=environment, base_url=base_url, timeout=timeout)
        self._raw_client = RawClient(
            http_client=custom_http_client if custom_http_client is not None else HttpxClient(timeout=timeout)
        )
        self._auth = AuthSchemes(
            api_key_auth=ApiKeyHeaderScheme("X-MBX-APIKEY", api_key_auth) if api_key_auth is not None else no_auth
        )

    @cached_property
    def auto_invest(self) -> AutoInvest:
        return AutoInvest(self._raw_client, self._server, self._auth)

    @cached_property
    def blvt(self) -> Blvt:
        return Blvt(self._raw_client, self._server, self._auth)

    @cached_property
    def c2_c(self) -> C2C:
        return C2C(self._raw_client, self._server, self._auth)

    @cached_property
    def convert(self) -> Convert:
        return Convert(self._raw_client, self._server, self._auth)

    @cached_property
    def copy_trading(self) -> CopyTrading:
        return CopyTrading(self._raw_client, self._server, self._auth)

    @cached_property
    def crypto_loans(self) -> CryptoLoans:
        return CryptoLoans(self._raw_client, self._server, self._auth)

    @cached_property
    def dual_investment(self) -> DualInvestment:
        return DualInvestment(self._raw_client, self._server, self._auth)

    @cached_property
    def fiat(self) -> Fiat:
        return Fiat(self._raw_client, self._server, self._auth)

    @cached_property
    def futures(self) -> Futures:
        return Futures(self._raw_client, self._server, self._auth)

    @cached_property
    def futures_algo(self) -> FuturesAlgo:
        return FuturesAlgo(self._raw_client, self._server, self._auth)

    @cached_property
    def gift_card(self) -> GiftCard:
        return GiftCard(self._raw_client, self._server, self._auth)

    @cached_property
    def isolated_margin_stream(self) -> IsolatedMarginStream:
        return IsolatedMarginStream(self._raw_client, self._server, self._auth)

    @cached_property
    def margin(self) -> Margin:
        return Margin(self._raw_client, self._server, self._auth)

    @cached_property
    def margin_stream(self) -> MarginStream:
        return MarginStream(self._raw_client, self._server, self._auth)

    @cached_property
    def market(self) -> Market:
        return Market(self._raw_client, self._server)

    @cached_property
    def mining(self) -> Mining:
        return Mining(self._raw_client, self._server, self._auth)

    @cached_property
    def nft(self) -> Nft:
        return Nft(self._raw_client, self._server, self._auth)

    @cached_property
    def pay(self) -> Pay:
        return Pay(self._raw_client, self._server, self._auth)

    @cached_property
    def portfolio_margin(self) -> PortfolioMargin:
        return PortfolioMargin(self._raw_client, self._server, self._auth)

    @cached_property
    def rebate(self) -> Rebate:
        return Rebate(self._raw_client, self._server, self._auth)

    @cached_property
    def savings(self) -> Savings:
        return Savings(self._raw_client, self._server, self._auth)

    @cached_property
    def simple_earn(self) -> SimpleEarn:
        return SimpleEarn(self._raw_client, self._server, self._auth)

    @cached_property
    def spot_algo(self) -> SpotAlgo:
        return SpotAlgo(self._raw_client, self._server, self._auth)

    @cached_property
    def staking(self) -> Staking:
        return Staking(self._raw_client, self._server, self._auth)

    @cached_property
    def stream(self) -> Stream:
        return Stream(self._raw_client, self._server, self._auth)

    @cached_property
    def sub_account_api(self) -> SubAccountApi:
        return SubAccountApi(self._raw_client, self._server, self._auth)

    @cached_property
    def trade_api(self) -> TradeApi:
        return TradeApi(self._raw_client, self._server, self._auth)

    @cached_property
    def vip_loans(self) -> VipLoans:
        return VipLoans(self._raw_client, self._server, self._auth)

    @cached_property
    def wallet(self) -> Wallet:
        return Wallet(self._raw_client, self._server, self._auth)

    def close(self) -> None:
        self._raw_client.http_client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.close()


Client = BinanceClient
