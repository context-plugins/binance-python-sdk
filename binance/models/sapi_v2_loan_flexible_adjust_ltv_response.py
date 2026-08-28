from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV2LoanFlexibleAdjustLtvResponse(SdkBaseModel):
    loan_coin: str = Field(alias="loanCoin")
    collateral_coin: str = Field(alias="collateralCoin")
    direction: str
    adjustment_amount: str = Field(alias="adjustmentAmount")
    current_ltv: str = Field(alias="currentLTV")


class SapiV2LoanFlexibleAdjustLtvResponseDict(TypedDict):
    loan_coin: str
    collateral_coin: str
    direction: str
    adjustment_amount: str
    current_ltv: str
