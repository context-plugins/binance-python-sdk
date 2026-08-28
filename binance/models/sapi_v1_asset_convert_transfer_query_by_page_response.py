from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row8 import Row8, Row8Dict


class SapiV1AssetConvertTransferQueryByPageResponse(SdkBaseModel):
    total: int
    rows: list[Row8]


class SapiV1AssetConvertTransferQueryByPageResponseDict(TypedDict):
    total: int
    rows: list[Row8 | Row8Dict]
