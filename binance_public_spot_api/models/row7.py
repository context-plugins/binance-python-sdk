from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row7(SdkBaseModel):
    asset: str
    amount: str
    type_: str = Field(alias="type")
    status: str
    tran_id: int = Field(alias="tranId")
    timestamp: int


class Row7Dict(TypedDict):
    asset: str
    amount: str
    type_: str
    status: str
    tran_id: int
    timestamp: int
