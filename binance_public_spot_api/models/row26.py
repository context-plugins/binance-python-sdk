from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row26(SdkBaseModel):
    loan_coin: str = Field(alias="loanCoin")
    initial_loan_amount: str = Field(alias="initialLoanAmount")
    collateral_coin: str = Field(alias="collateralCoin")
    initial_collateral_amount: str = Field(alias="initialCollateralAmount")
    borrow_time: int = Field(alias="borrowTime")
    status: str


class Row26Dict(TypedDict):
    loan_coin: str
    initial_loan_amount: str
    collateral_coin: str
    initial_collateral_amount: str
    borrow_time: int
    status: str
