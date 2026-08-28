from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .token import Token, TokenDict


class List3(SdkBaseModel):
    order_no: str = Field(alias="orderNo")
    """0: purchase order, 1: sell order, 2: royalty income, 3: primary market order, 4: mint fee"""

    tokens: list[Token]
    trade_time: int = Field(alias="tradeTime")
    trade_amount: str = Field(alias="tradeAmount")
    trade_currency: str = Field(alias="tradeCurrency")


class List3Dict(TypedDict):
    order_no: str
    tokens: list[Token | TokenDict]
    trade_time: int
    trade_amount: str
    trade_currency: str
