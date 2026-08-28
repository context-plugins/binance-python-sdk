from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .account_profit import AccountProfit, AccountProfitDict


class Data13(SdkBaseModel):
    account_profits: list[AccountProfit] = Field(alias="accountProfits")
    total_num: int = Field(alias="totalNum")
    """Total Rows"""

    page_size: int = Field(alias="pageSize")
    """Rows per page"""


class Data13Dict(TypedDict):
    account_profits: list[AccountProfit | AccountProfitDict]
    total_num: int
    page_size: int
