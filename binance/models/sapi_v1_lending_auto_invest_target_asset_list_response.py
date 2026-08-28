from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .auto_invest_asset_list import AutoInvestAssetList, AutoInvestAssetListDict


class SapiV1LendingAutoInvestTargetAssetListResponse(SdkBaseModel):
    target_assets: Optional[str] = Field(default=UNSET, alias="targetAssets")
    auto_invest_asset_list: Optional[list[AutoInvestAssetList]] = Field(default=UNSET, alias="autoInvestAssetList")


class SapiV1LendingAutoInvestTargetAssetListResponseDict(TypedDict):
    target_assets: NotRequired[str]
    auto_invest_asset_list: NotRequired[list[AutoInvestAssetList | AutoInvestAssetListDict]]
