from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row10 import Row10, Row10Dict


class SapiV1AssetCustodyTransferHistoryResponse(SdkBaseModel):
    total: int
    rows: list[Row10]


class SapiV1AssetCustodyTransferHistoryResponseDict(TypedDict):
    total: int
    rows: list[Row10 | Row10Dict]
