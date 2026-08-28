from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row6(SdkBaseModel):
    id: int
    amount: str
    asset: str
    div_time: int = Field(alias="divTime")
    en_info: str = Field(alias="enInfo")
    tran_id: int = Field(alias="tranId")


class Row6Dict(TypedDict):
    id: int
    amount: str
    asset: str
    div_time: int
    en_info: str
    tran_id: int
