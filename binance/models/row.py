from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Row(SdkBaseModel):
    amount: str
    asset: str
    status: str
    timestamp: int
    tx_id: int = Field(alias="txId")
    type_: Optional[str] = Field(default=UNSET, alias="type")
    trans_from: str = Field(alias="transFrom")
    trans_to: str = Field(alias="transTo")


class RowDict(TypedDict):
    amount: str
    asset: str
    status: str
    timestamp: int
    tx_id: int
    type_: NotRequired[str]
    trans_from: str
    trans_to: str
