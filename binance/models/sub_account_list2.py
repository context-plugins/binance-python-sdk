from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SubAccountList2(SdkBaseModel):
    email: str
    total_asset_of_btc: str = Field(alias="totalAssetOfBtc")
    total_liability_of_btc: str = Field(alias="totalLiabilityOfBtc")
    total_net_asset_of_btc: str = Field(alias="totalNetAssetOfBtc")


class SubAccountList2Dict(TypedDict):
    email: str
    total_asset_of_btc: str
    total_liability_of_btc: str
    total_net_asset_of_btc: str
