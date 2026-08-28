from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row25(SdkBaseModel):
    loan_coin: str = Field(alias="loanCoin")
    total_debt: str = Field(alias="totalDebt")
    collateral_coin: str = Field(alias="collateralCoin")
    collateral_amount: str = Field(alias="collateralAmount")
    current_ltv: str = Field(alias="currentLTV")


class Row25Dict(TypedDict):
    loan_coin: str
    total_debt: str
    collateral_coin: str
    collateral_amount: str
    current_ltv: str
