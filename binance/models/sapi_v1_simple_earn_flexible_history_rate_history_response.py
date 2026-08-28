from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row48 import Row48, Row48Dict


class SapiV1SimpleEarnFlexibleHistoryRateHistoryResponse(SdkBaseModel):
    rows: list[Row48]
    total: int


class SapiV1SimpleEarnFlexibleHistoryRateHistoryResponseDict(TypedDict):
    rows: list[Row48 | Row48Dict]
    total: int
