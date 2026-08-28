from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1FuturesTransferResponse(SdkBaseModel):
    tran_id: int = Field(alias="tranId")


class SapiV1FuturesTransferResponseDict(TypedDict):
    tran_id: int
