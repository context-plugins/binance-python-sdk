from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SubAccountList1(SdkBaseModel):
    email: str
    total_margin_balance: str = Field(alias="totalMarginBalance")
    total_unrealized_profit: str = Field(alias="totalUnrealizedProfit")
    total_wallet_balance: str = Field(alias="totalWalletBalance")
    asset: str


class SubAccountList1Dict(TypedDict):
    email: str
    total_margin_balance: str
    total_unrealized_profit: str
    total_wallet_balance: str
    asset: str
