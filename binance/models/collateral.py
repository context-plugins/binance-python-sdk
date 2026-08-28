from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Collateral(SdkBaseModel):
    min_usd_value: str = Field(alias="minUsdValue")
    max_usd_value: str = Field(alias="maxUsdValue")
    discount_rate: str = Field(alias="discountRate")


class CollateralDict(TypedDict):
    min_usd_value: str
    max_usd_value: str
    discount_rate: str
