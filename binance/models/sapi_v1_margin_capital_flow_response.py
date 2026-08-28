from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1MarginCapitalFlowResponse(SdkBaseModel):
    id: int
    tran_id: int = Field(alias="tranId")
    timestamp: int
    asset: str
    symbol: str
    type_: str = Field(alias="type")
    amount: str


class SapiV1MarginCapitalFlowResponseDict(TypedDict):
    id: int
    tran_id: int
    timestamp: int
    asset: str
    symbol: str
    type_: str
    amount: str
