from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AccountProfit1(SdkBaseModel):
    time: int
    coin_name: str = Field(alias="coinName")
    type_: int = Field(alias="type")
    """0:Referral 1:Refund 2:Rebate"""

    puid: int
    """puid"""

    sub_name: str = Field(alias="subName")
    """Mining account"""

    amount: float


class AccountProfit1Dict(TypedDict):
    time: int
    coin_name: str
    type_: int
    puid: int
    sub_name: str
    amount: float
