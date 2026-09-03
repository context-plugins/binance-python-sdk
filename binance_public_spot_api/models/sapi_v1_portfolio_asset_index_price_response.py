from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1PortfolioAssetIndexPriceResponse(SdkBaseModel):
    asset: str
    asset_index_price: str = Field(alias="assetIndexPrice")
    time: int


class SapiV1PortfolioAssetIndexPriceResponseDict(TypedDict):
    asset: str
    asset_index_price: str
    time: int
