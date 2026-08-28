from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1LoanBorrowResponse(SdkBaseModel):
    loan_coin: str = Field(alias="loanCoin")
    loan_amount: str = Field(alias="loanAmount")
    collateral_coin: str = Field(alias="collateralCoin")
    collateral_amount: str = Field(alias="collateralAmount")
    hourly_interest_rate: str = Field(alias="hourlyInterestRate")
    order_id: str = Field(alias="orderId")


class SapiV1LoanBorrowResponseDict(TypedDict):
    loan_coin: str
    loan_amount: str
    collateral_coin: str
    collateral_amount: str
    hourly_interest_rate: str
    order_id: str
