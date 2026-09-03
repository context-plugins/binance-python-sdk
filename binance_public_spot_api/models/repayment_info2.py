from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class RepaymentInfo2(SdkBaseModel):
    loan_coin: str = Field(alias="loanCoin")
    collateral_coin: str = Field(alias="collateralCoin")
    repay_status: str = Field(alias="repayStatus")


class RepaymentInfo2Dict(TypedDict):
    loan_coin: str
    collateral_coin: str
    repay_status: str
