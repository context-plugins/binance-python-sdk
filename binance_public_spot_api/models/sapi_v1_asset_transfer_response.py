from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row7 import Row7, Row7Dict


class SapiV1AssetTransferResponse(SdkBaseModel):
    total: int
    rows: list[Row7]


class SapiV1AssetTransferResponseDict(TypedDict):
    total: int
    rows: list[Row7 | Row7Dict]
