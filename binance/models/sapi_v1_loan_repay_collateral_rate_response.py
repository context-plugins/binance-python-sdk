from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1LoanRepayCollateralRateResponse(SdkBaseModel):
    loan_coin: str = Field(alias="loanCoin")
    collateral_coin: str = Field(alias="collateralCoin")
    repay_amount: str = Field(alias="repayAmount")
    rate: str
    """rate of collateral coin/loan coin"""


class SapiV1LoanRepayCollateralRateResponseDict(TypedDict):
    loan_coin: str
    collateral_coin: str
    repay_amount: str
    rate: str
