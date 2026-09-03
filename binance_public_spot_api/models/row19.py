from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row19(SdkBaseModel):
    order_id: int = Field(alias="orderId")
    loan_coin: str = Field(alias="loanCoin")
    total_debt: str = Field(alias="totalDebt")
    residual_interest: str = Field(alias="residualInterest")
    collateral_coin: str = Field(alias="collateralCoin")
    collateral_amount: str = Field(alias="collateralAmount")
    current_ltv: str = Field(alias="currentLTV")
    expiration_time: int = Field(alias="expirationTime")


class Row19Dict(TypedDict):
    order_id: int
    loan_coin: str
    total_debt: str
    residual_interest: str
    collateral_coin: str
    collateral_amount: str
    current_ltv: str
    expiration_time: int
