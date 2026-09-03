from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1AssetGetFundingAssetResponse(SdkBaseModel):
    asset: str
    free: str
    locked: str
    freeze: str
    withdrawing: str
    btc_valuation: str = Field(alias="btcValuation")


class SapiV1AssetGetFundingAssetResponseDict(TypedDict):
    asset: str
    free: str
    locked: str
    freeze: str
    withdrawing: str
    btc_valuation: str
