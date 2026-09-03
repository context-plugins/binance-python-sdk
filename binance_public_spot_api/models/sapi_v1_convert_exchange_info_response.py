from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1ConvertExchangeInfoResponse(SdkBaseModel):
    from_asset: str = Field(alias="fromAsset")
    to_asset: str = Field(alias="toAsset")
    from_asset_min_amount: str = Field(alias="fromAssetMinAmount")
    from_asset_max_amount: str = Field(alias="fromAssetMaxAmount")
    to_asset_min_amount: str = Field(alias="toAssetMinAmount")
    to_asset_max_amount: str = Field(alias="toAssetMaxAmount")


class SapiV1ConvertExchangeInfoResponseDict(TypedDict):
    from_asset: str
    to_asset: str
    from_asset_min_amount: str
    from_asset_max_amount: str
    to_asset_min_amount: str
    to_asset_max_amount: str
