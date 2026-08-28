from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1LoanAdjustLtvResponse(SdkBaseModel):
    loan_coin: str = Field(alias="loanCoin")
    collateral_coin: str = Field(alias="collateralCoin")
    direction: str
    amount: str
    current_ltv: str = Field(alias="currentLTV")


class SapiV1LoanAdjustLtvResponseDict(TypedDict):
    loan_coin: str
    collateral_coin: str
    direction: str
    amount: str
    current_ltv: str
