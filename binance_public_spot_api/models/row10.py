from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row10(SdkBaseModel):
    client_tran_id: str = Field(alias="clientTranId")
    transfer_type: str = Field(alias="transferType")
    asset: str
    amount: str
    time: int


class Row10Dict(TypedDict):
    client_tran_id: str
    transfer_type: str
    asset: str
    amount: str
    time: int
