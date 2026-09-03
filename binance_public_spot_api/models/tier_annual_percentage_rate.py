from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TierAnnualPercentageRate(SdkBaseModel):
    btc0_5: float = Field(alias="0-5BTC")
    btc5_10: float = Field(alias="5-10BTC")


class TierAnnualPercentageRateDict(TypedDict):
    btc0_5: float
    btc5_10: float
