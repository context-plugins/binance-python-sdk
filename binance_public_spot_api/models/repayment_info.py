from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class RepaymentInfo(SdkBaseModel):
    loan_coin: str = Field(alias="loanCoin")
    remaining_principal: str = Field(alias="remainingPrincipal")
    remaining_interest: str = Field(alias="remainingInterest")
    collateral_coin: str = Field(alias="collateralCoin")
    remaining_collateral: str = Field(alias="remainingCollateral")
    current_ltv: str = Field(alias="currentLTV")
    repay_status: str = Field(alias="repayStatus")


class RepaymentInfoDict(TypedDict):
    loan_coin: str
    remaining_principal: str
    remaining_interest: str
    collateral_coin: str
    remaining_collateral: str
    current_ltv: str
    repay_status: str
