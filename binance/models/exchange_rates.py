from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ExchangeRates(SdkBaseModel):
    usdc: str = Field(alias="USDC")
    tusd: str = Field(alias="TUSD")
    usdp: str = Field(alias="USDP")


class ExchangeRatesDict(TypedDict):
    usdc: str
    tusd: str
    usdp: str
