from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1LoanIncomeResponse(SdkBaseModel):
    asset: str
    type_: str = Field(alias="type")
    amount: str
    timestamp: int
    tran_id: str = Field(alias="tranId")


class SapiV1LoanIncomeResponseDict(TypedDict):
    asset: str
    type_: str
    amount: str
    timestamp: int
    tran_id: str
