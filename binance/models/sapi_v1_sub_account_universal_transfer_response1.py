from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1SubAccountUniversalTransferResponse1(SdkBaseModel):
    tran_id: int = Field(alias="tranId")
    client_tran_id: str = Field(alias="clientTranId")


class SapiV1SubAccountUniversalTransferResponse1Dict(TypedDict):
    tran_id: int
    client_tran_id: str
