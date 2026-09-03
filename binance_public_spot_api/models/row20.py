from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row20(SdkBaseModel):
    loan_coin: str = Field(alias="loanCoin")
    repay_amount: str = Field(alias="repayAmount")
    collateral_coin: str = Field(alias="collateralCoin")
    collateral_used: str = Field(alias="collateralUsed")
    collateral_return: str = Field(alias="collateralReturn")
    repay_type: str = Field(alias="repayType")
    repay_status: str = Field(alias="repayStatus")
    """'repayType': '1' // 1 for 'repay with borrowed coin', 2 for 'repay with collateral' 'repayStatus': 'Repaid' //
    Repaid, Repaying, Failed"""

    repay_time: int = Field(alias="repayTime")
    order_id: int = Field(alias="orderId")


class Row20Dict(TypedDict):
    loan_coin: str
    repay_amount: str
    collateral_coin: str
    collateral_used: str
    collateral_return: str
    repay_type: str
    repay_status: str
    repay_time: int
    order_id: int
