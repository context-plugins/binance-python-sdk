from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CommissionRates(SdkBaseModel):
    maker: str
    taker: str
    buyer: str
    seller: str


class CommissionRatesDict(TypedDict):
    maker: str
    taker: str
    buyer: str
    seller: str
