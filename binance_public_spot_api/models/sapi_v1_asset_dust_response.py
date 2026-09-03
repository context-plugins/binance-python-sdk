from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .transfer_result import TransferResult, TransferResultDict


class SapiV1AssetDustResponse(SdkBaseModel):
    total_service_charge: str = Field(alias="totalServiceCharge")
    total_transfered: str = Field(alias="totalTransfered")
    transfer_result: list[TransferResult] = Field(alias="transferResult")


class SapiV1AssetDustResponseDict(TypedDict):
    total_service_charge: str
    total_transfered: str
    transfer_result: list[TransferResult | TransferResultDict]
