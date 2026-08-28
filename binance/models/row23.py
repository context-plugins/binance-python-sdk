from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row23(SdkBaseModel):
    collateral_coin: str = Field(alias="collateralCoin")
    initial_ltv: str = Field(alias="initialLTV")
    margin_call_ltv: str = Field(alias="marginCallLTV")
    liquidation_ltv: str = Field(alias="liquidationLTV")
    max_limit: str = Field(alias="maxLimit")
    vip_level: int = Field(alias="vipLevel")


class Row23Dict(TypedDict):
    collateral_coin: str
    initial_ltv: str
    margin_call_ltv: str
    liquidation_ltv: str
    max_limit: str
    vip_level: int
