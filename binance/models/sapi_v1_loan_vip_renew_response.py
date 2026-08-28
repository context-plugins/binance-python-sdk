from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1LoanVipRenewResponse(SdkBaseModel):
    loan_account_id: str = Field(alias="loanAccountId")
    loan_coin: str = Field(alias="loanCoin")
    loan_amount: str = Field(alias="loanAmount")
    collateral_account_id: str = Field(alias="collateralAccountId")
    collateral_coin: str = Field(alias="collateralCoin")
    loan_term: str = Field(alias="loanTerm")


class SapiV1LoanVipRenewResponseDict(TypedDict):
    loan_account_id: str
    loan_coin: str
    loan_amount: str
    collateral_account_id: str
    collateral_coin: str
    loan_term: str
