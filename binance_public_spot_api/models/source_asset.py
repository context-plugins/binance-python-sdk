from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SourceAsset(SdkBaseModel):
    source_asset: str = Field(alias="sourceAsset")
    asset_min_amount: str = Field(alias="assetMinAmount")
    asset_max_amount: str = Field(alias="assetMaxAmount")
    scale: str
    flexible_amount: str = Field(alias="flexibleAmount")


class SourceAssetDict(TypedDict):
    source_asset: str
    asset_min_amount: str
    asset_max_amount: str
    scale: str
    flexible_amount: str
