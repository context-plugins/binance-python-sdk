from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1ConvertAssetInfoResponse(SdkBaseModel):
    asset: str
    fraction: int


class SapiV1ConvertAssetInfoResponseDict(TypedDict):
    asset: str
    fraction: int
