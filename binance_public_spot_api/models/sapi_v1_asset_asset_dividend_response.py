from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row6 import Row6, Row6Dict


class SapiV1AssetAssetDividendResponse(SdkBaseModel):
    rows: list[Row6]
    total: int


class SapiV1AssetAssetDividendResponseDict(TypedDict):
    rows: list[Row6 | Row6Dict]
    total: int
