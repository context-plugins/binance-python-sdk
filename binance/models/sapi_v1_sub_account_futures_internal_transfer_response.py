from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .transfer import Transfer, TransferDict


class SapiV1SubAccountFuturesInternalTransferResponse(SdkBaseModel):
    success: bool
    futures_type: int = Field(alias="futuresType")
    transfers: list[Transfer]


class SapiV1SubAccountFuturesInternalTransferResponseDict(TypedDict):
    success: bool
    futures_type: int
    transfers: list[Transfer | TransferDict]
