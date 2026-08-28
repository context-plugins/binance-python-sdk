from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row17(SdkBaseModel):
    loan_account_id: str = Field(alias="loanAccountId")
    order_id: str = Field(alias="orderId")
    request_id: str = Field(alias="requestId")
    loan_coin: str = Field(alias="loanCoin")
    loan_amount: str = Field(alias="loanAmount")
    collateral_account_id: str = Field(alias="collateralAccountId")
    collateral_coin: str = Field(alias="collateralCoin")
    loan_term: int = Field(alias="loanTerm")
    status: int


class Row17Dict(TypedDict):
    loan_account_id: str
    order_id: str
    request_id: str
    loan_coin: str
    loan_amount: str
    collateral_account_id: str
    collateral_coin: str
    loan_term: int
    status: int
