from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row18(SdkBaseModel):
    order_id: int = Field(alias="orderId")
    loan_coin: str = Field(alias="loanCoin")
    initial_loan_amount: str = Field(alias="initialLoanAmount")
    hourly_interest_rate: str = Field(alias="hourlyInterestRate")
    loan_term: str = Field(alias="loanTerm")
    collateral_coin: str = Field(alias="collateralCoin")
    initial_collateral_amount: str = Field(alias="initialCollateralAmount")
    borrow_time: int = Field(alias="borrowTime")
    status: str


class Row18Dict(TypedDict):
    order_id: int
    loan_coin: str
    initial_loan_amount: str
    hourly_interest_rate: str
    loan_term: str
    collateral_coin: str
    initial_collateral_amount: str
    borrow_time: int
    status: str
