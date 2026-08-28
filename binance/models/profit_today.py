from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ProfitToday(SdkBaseModel):
    btc: str = Field(alias="BTC")
    bsv: str = Field(alias="BSV")
    bch: str = Field(alias="BCH")


class ProfitTodayDict(TypedDict):
    btc: str
    bsv: str
    bch: str
