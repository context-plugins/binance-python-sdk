from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SapiV2LoanFlexibleBorrowResponse(SdkBaseModel):
    loan_coin: str = Field(alias="loanCoin")
    loan_amount: str = Field(alias="loanAmount")
    collateral_coin: Optional[str] = Field(default=UNSET, alias="collateralCoin")
    collateral_amount: str = Field(alias="collateralAmount")
    status: str


class SapiV2LoanFlexibleBorrowResponseDict(TypedDict):
    loan_coin: str
    loan_amount: str
    collateral_coin: NotRequired[str]
    collateral_amount: str
    status: str
