from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1PortfolioRepayFuturesNegativeBalanceResponse(SdkBaseModel):
    msg: str


class SapiV1PortfolioRepayFuturesNegativeBalanceResponseDict(TypedDict):
    msg: str
