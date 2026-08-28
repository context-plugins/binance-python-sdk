from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TierAnnualPercentageRate(SdkBaseModel):
    _5_btc0: float = Field(alias="0-5BTC")
    _10_btc5: float = Field(alias="5-10BTC")


class TierAnnualPercentageRateDict(TypedDict):
    _5_btc0: float
    _10_btc5: float
