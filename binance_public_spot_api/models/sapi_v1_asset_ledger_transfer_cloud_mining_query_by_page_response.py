from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row9 import Row9, Row9Dict


class SapiV1AssetLedgerTransferCloudMiningQueryByPageResponse(SdkBaseModel):
    total: int
    rows: list[Row9]


class SapiV1AssetLedgerTransferCloudMiningQueryByPageResponseDict(TypedDict):
    total: int
    rows: list[Row9 | Row9Dict]
