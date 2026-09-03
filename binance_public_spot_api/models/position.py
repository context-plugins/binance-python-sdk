from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Position(SdkBaseModel):
    entry_price: str = Field(alias="entryPrice")
    mark_price: str = Field(alias="markPrice")
    position_amt: str = Field(alias="positionAmt")
    symbol: str
    un_realized_profit: str = Field(alias="unRealizedProfit")


class PositionDict(TypedDict):
    entry_price: str
    mark_price: str
    position_amt: str
    symbol: str
    un_realized_profit: str
