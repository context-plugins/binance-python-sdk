from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1AssetConvertTransferResponse(SdkBaseModel):
    tran_id: int = Field(alias="tranId")
    status: str


class SapiV1AssetConvertTransferResponseDict(TypedDict):
    tran_id: int
    status: str
