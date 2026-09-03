from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row9(SdkBaseModel):
    create_time: int = Field(alias="createTime")
    tran_id: int = Field(alias="tranId")
    type_: int = Field(alias="type")
    asset: str
    amount: str
    status: str


class Row9Dict(TypedDict):
    create_time: int
    tran_id: int
    type_: int
    asset: str
    amount: str
    status: str
