from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class StandardCommission(SdkBaseModel):
    """Standard commission rates on trades from the order."""

    maker: str
    taker: str
    buyer: str
    seller: str


class StandardCommissionDict(TypedDict):
    maker: str
    taker: str
    buyer: str
    seller: str
