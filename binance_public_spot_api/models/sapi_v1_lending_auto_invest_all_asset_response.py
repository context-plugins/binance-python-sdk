from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1LendingAutoInvestAllAssetResponse(SdkBaseModel):
    target_assets: list[str] = Field(alias="targetAssets")
    source_assets: list[str] = Field(alias="sourceAssets")


class SapiV1LendingAutoInvestAllAssetResponseDict(TypedDict):
    target_assets: list[str]
    source_assets: list[str]
