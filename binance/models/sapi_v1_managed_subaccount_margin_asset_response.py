from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .user_asset import UserAsset, UserAssetDict


class SapiV1ManagedSubaccountMarginAssetResponse(SdkBaseModel):
    margin_level: str = Field(alias="marginLevel")
    total_asset_of_btc: str = Field(alias="totalAssetOfBtc")
    total_liability_of_btc: str = Field(alias="totalLiabilityOfBtc")
    total_net_asset_of_btc: str = Field(alias="totalNetAssetOfBtc")
    user_assets: list[UserAsset] = Field(alias="userAssets")


class SapiV1ManagedSubaccountMarginAssetResponseDict(TypedDict):
    margin_level: str
    total_asset_of_btc: str
    total_liability_of_btc: str
    total_net_asset_of_btc: str
    user_assets: list[UserAsset | UserAssetDict]
