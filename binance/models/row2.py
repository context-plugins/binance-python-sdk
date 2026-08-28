from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row2(SdkBaseModel):
    amount: str
    asset: str
    status: str
    timestamp: int
    tx_id: int = Field(alias="txId")
    type_: str = Field(alias="type")


class Row2Dict(TypedDict):
    amount: str
    asset: str
    status: str
    timestamp: int
    tx_id: int
    type_: str
