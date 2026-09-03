from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row27(SdkBaseModel):
    loan_coin: str = Field(alias="loanCoin")
    repay_amount: str = Field(alias="repayAmount")
    collateral_coin: str = Field(alias="collateralCoin")
    collateral_return: str = Field(alias="collateralReturn")
    repay_status: str = Field(alias="repayStatus")
    repay_time: int = Field(alias="repayTime")


class Row27Dict(TypedDict):
    loan_coin: str
    repay_amount: str
    collateral_coin: str
    collateral_return: str
    repay_status: str
    repay_time: int
