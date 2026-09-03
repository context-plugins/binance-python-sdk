from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SapiV1LoanVipBorrowResponse(SdkBaseModel):
    loan_account_id: str = Field(alias="loanAccountId")
    request_id: str = Field(alias="requestId")
    loan_coin: str = Field(alias="loanCoin")
    is_flexible_rate: str = Field(alias="isFlexibleRate")
    loan_amount: str = Field(alias="loanAmount")
    collateral_account_id: str = Field(alias="collateralAccountId")
    collateral_coin: str = Field(alias="collateralCoin")
    loan_term: Optional[str] = Field(default=UNSET, alias="loanTerm")


class SapiV1LoanVipBorrowResponseDict(TypedDict):
    loan_account_id: str
    request_id: str
    loan_coin: str
    is_flexible_rate: str
    loan_amount: str
    collateral_account_id: str
    collateral_coin: str
    loan_term: NotRequired[str]
