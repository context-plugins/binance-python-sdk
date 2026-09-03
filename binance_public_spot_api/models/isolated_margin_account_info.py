from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .asset import Asset, AssetDict


class IsolatedMarginAccountInfo(SdkBaseModel):
    assets: list[Asset]
    total_asset_of_btc: str = Field(alias="totalAssetOfBtc")
    total_liability_of_btc: str = Field(alias="totalLiabilityOfBtc")
    total_net_asset_of_btc: str = Field(alias="totalNetAssetOfBtc")


class IsolatedMarginAccountInfoDict(TypedDict):
    assets: list[Asset | AssetDict]
    total_asset_of_btc: str
    total_liability_of_btc: str
    total_net_asset_of_btc: str
