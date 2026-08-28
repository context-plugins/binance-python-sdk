from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .other_profit import OtherProfit, OtherProfitDict


class Data14(SdkBaseModel):
    other_profits: list[OtherProfit] = Field(alias="otherProfits")
    total_num: int = Field(alias="totalNum")
    """Total Rows"""

    page_size: int = Field(alias="pageSize")
    """Rows per page"""


class Data14Dict(TypedDict):
    other_profits: list[OtherProfit | OtherProfitDict]
    total_num: int
    page_size: int
