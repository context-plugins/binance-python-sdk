from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1SubAccountSubTransferHistoryResponse(SdkBaseModel):
    from_: str = Field(alias="from")
    to: str
    asset: str
    qty: str
    status: str
    tran_id: int = Field(alias="tranId")
    time: int


class SapiV1SubAccountSubTransferHistoryResponseDict(TypedDict):
    from_: str
    to: str
    asset: str
    qty: str
    status: str
    tran_id: int
    time: int
