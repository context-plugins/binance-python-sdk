from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .detail import Detail, DetailDict


class SapiV1AssetDustBtcResponse(SdkBaseModel):
    details: list[Detail]
    total_transfer_btc: str = Field(alias="totalTransferBtc")
    total_transfer_bnb: str = Field(alias="totalTransferBNB")
    dribblet_percentage: str = Field(alias="dribbletPercentage")
    """Commission fee"""


class SapiV1AssetDustBtcResponseDict(TypedDict):
    details: list[Detail | DetailDict]
    total_transfer_btc: str
    total_transfer_bnb: str
    dribblet_percentage: str
