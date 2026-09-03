from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CurrentBasket(SdkBaseModel):
    symbol: str
    amount: str
    notional_value: str = Field(alias="notionalValue")


class CurrentBasketDict(TypedDict):
    symbol: str
    amount: str
    notional_value: str
