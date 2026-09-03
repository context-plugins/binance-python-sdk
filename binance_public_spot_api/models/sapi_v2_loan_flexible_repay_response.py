from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV2LoanFlexibleRepayResponse(SdkBaseModel):
    loan_coin: str = Field(alias="loanCoin")
    collateral_coin: str = Field(alias="collateralCoin")
    remaining_debt: str = Field(alias="remainingDebt")
    remaining_collateral: str = Field(alias="remainingCollateral")
    full_repayment: bool = Field(alias="fullRepayment")
    current_ltv: str = Field(alias="currentLTV")
    repay_status: str = Field(alias="repayStatus")
    """Repaid, Repaying, Failed"""


class SapiV2LoanFlexibleRepayResponseDict(TypedDict):
    loan_coin: str
    collateral_coin: str
    remaining_debt: str
    remaining_collateral: str
    full_repayment: bool
    current_ltv: str
    repay_status: str
