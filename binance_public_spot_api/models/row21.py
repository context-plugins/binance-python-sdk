from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row21(SdkBaseModel):
    loan_coin: str = Field(alias="loanCoin")
    collateral_coin: str = Field(alias="collateralCoin")
    direction: str
    amount: str
    pre_ltv: str = Field(alias="preLTV")
    after_ltv: str = Field(alias="afterLTV")
    adjust_time: int = Field(alias="adjustTime")
    order_id: int = Field(alias="orderId")


class Row21Dict(TypedDict):
    loan_coin: str
    collateral_coin: str
    direction: str
    amount: str
    pre_ltv: str
    after_ltv: str
    adjust_time: int
    order_id: int
