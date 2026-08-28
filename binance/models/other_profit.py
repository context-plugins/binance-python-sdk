from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class OtherProfit(SdkBaseModel):
    time: int
    """Mining date"""

    coin_name: str = Field(alias="coinName")
    """Coin Name"""

    type_: int = Field(alias="type")
    """1: Merged Mining, 2: Activity Bonus, 3:Rebate 4:Smart Pool 6:Income Transfer 7:Pool Savings"""

    profit_amount: float = Field(alias="profitAmount")
    status: int
    """0:Unpaid, 1:Paying 2：Paid"""


class OtherProfitDict(TypedDict):
    time: int
    coin_name: str
    type_: int
    profit_amount: float
    status: int
