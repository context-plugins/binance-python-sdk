from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row28(SdkBaseModel):
    loan_coin: str = Field(alias="loanCoin")
    collateral_coin: str = Field(alias="collateralCoin")
    direction: str
    collateral_amount: str = Field(alias="collateralAmount")
    pre_ltv: str = Field(alias="preLTV")
    after_ltv: str = Field(alias="afterLTV")
    adjust_time: int = Field(alias="adjustTime")


class Row28Dict(TypedDict):
    loan_coin: str
    collateral_coin: str
    direction: str
    collateral_amount: str
    pre_ltv: str
    after_ltv: str
    adjust_time: int
