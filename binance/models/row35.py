from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row35(SdkBaseModel):
    time: int
    from_asset: str = Field(alias="fromAsset")
    from_amount: str = Field(alias="fromAmount")
    to_asset: str = Field(alias="toAsset")
    to_amount: str = Field(alias="toAmount")
    exchange_rate: str = Field(alias="exchangeRate")
    """BETH amount per 1 WBETH"""

    status: str
    """PENDING, SUCCESS, FAILED"""


class Row35Dict(TypedDict):
    time: int
    from_asset: str
    from_amount: str
    to_asset: str
    to_amount: str
    exchange_rate: str
    status: str
