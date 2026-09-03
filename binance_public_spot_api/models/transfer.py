from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Transfer(SdkBaseModel):
    from_: str = Field(alias="from")
    to: str
    asset: str
    qty: str
    tran_id: int = Field(alias="tranId")
    time: int


class TransferDict(TypedDict):
    from_: str
    to: str
    asset: str
    qty: str
    tran_id: int
    time: int
