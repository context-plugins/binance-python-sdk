from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .source_asset import SourceAsset, SourceAssetDict


class SapiV1LendingAutoInvestSourceAssetListResponse(SdkBaseModel):
    fee_rate: str = Field(alias="feeRate")
    source_assets: list[SourceAsset] = Field(alias="sourceAssets")


class SapiV1LendingAutoInvestSourceAssetListResponseDict(TypedDict):
    fee_rate: str
    source_assets: list[SourceAsset | SourceAssetDict]
