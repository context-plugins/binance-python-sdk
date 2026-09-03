from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row13(SdkBaseModel):
    loan_coin: str = Field(alias="loanCoin")
    repay_amount: str = Field(alias="repayAmount")
    collateral_coin: str = Field(alias="collateralCoin")
    repay_status: str = Field(alias="repayStatus")
    """Repaid, Repaying, Failed"""

    repay_time: str = Field(alias="repayTime")
    order_id: str = Field(alias="orderId")


class Row13Dict(TypedDict):
    loan_coin: str
    repay_amount: str
    collateral_coin: str
    repay_status: str
    repay_time: str
    order_id: str
