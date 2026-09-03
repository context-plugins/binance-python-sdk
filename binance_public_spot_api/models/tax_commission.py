from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TaxCommission(SdkBaseModel):
    """Tax commission rates for trades from the order."""

    maker: str
    taker: str
    buyer: str
    seller: str


class TaxCommissionDict(TypedDict):
    maker: str
    taker: str
    buyer: str
    seller: str
