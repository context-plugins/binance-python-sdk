from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .profit_transfer_detail import ProfitTransferDetail, ProfitTransferDetailDict


class Data16(SdkBaseModel):
    profit_transfer_details: list[ProfitTransferDetail] = Field(alias="profitTransferDetails")
    total_num: int = Field(alias="totalNum")
    page_size: int = Field(alias="pageSize")


class Data16Dict(TypedDict):
    profit_transfer_details: list[ProfitTransferDetail | ProfitTransferDetailDict]
    total_num: int
    page_size: int
