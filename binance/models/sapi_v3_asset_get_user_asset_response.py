from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV3AssetGetUserAssetResponse(SdkBaseModel):
    asset: str
    free: str
    locked: str
    freeze: str
    withdrawing: str
    ipoable: str
    btc_valuation: str = Field(alias="btcValuation")


class SapiV3AssetGetUserAssetResponseDict(TypedDict):
    asset: str
    free: str
    locked: str
    freeze: str
    withdrawing: str
    ipoable: str
    btc_valuation: str
