from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CollateralInfo(SdkBaseModel):
    tier_floor: str = Field(alias="tierFloor")
    tier_cap: str = Field(alias="tierCap")
    collateral_rate: str = Field(alias="collateralRate")


class CollateralInfoDict(TypedDict):
    tier_floor: str
    tier_cap: str
    collateral_rate: str
