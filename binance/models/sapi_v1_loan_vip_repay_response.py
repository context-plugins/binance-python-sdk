from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1LoanVipRepayResponse(SdkBaseModel):
    loan_coin: str = Field(alias="loanCoin")
    repay_amount: str = Field(alias="repayAmount")
    remaining_principal: str = Field(alias="remainingPrincipal")
    remaining_interest: str = Field(alias="remainingInterest")
    collateral_coin: str = Field(alias="collateralCoin")
    current_ltv: str = Field(alias="currentLTV")
    repay_status: str = Field(alias="repayStatus")
    """Repaid, Repaying, Failed"""


class SapiV1LoanVipRepayResponseDict(TypedDict):
    loan_coin: str
    repay_amount: str
    remaining_principal: str
    remaining_interest: str
    collateral_coin: str
    current_ltv: str
    repay_status: str
