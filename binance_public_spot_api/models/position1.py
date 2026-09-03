from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Position1(SdkBaseModel):
    symbol: str
    entry_price: float = Field(alias="entryPrice")
    mark_price: float = Field(alias="markPrice")
    position_amt: float = Field(alias="positionAmt")


class Position1Dict(TypedDict):
    symbol: str
    entry_price: float
    mark_price: float
    position_amt: float
