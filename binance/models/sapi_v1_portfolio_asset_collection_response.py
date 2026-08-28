from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1PortfolioAssetCollectionResponse(SdkBaseModel):
    msg: str


class SapiV1PortfolioAssetCollectionResponseDict(TypedDict):
    msg: str
