from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row46 import Row46, Row46Dict


class SapiV1SimpleEarnFlexibleHistoryRewardsRecordResponse(SdkBaseModel):
    rows: list[Row46]
    total: int


class SapiV1SimpleEarnFlexibleHistoryRewardsRecordResponseDict(TypedDict):
    rows: list[Row46 | Row46Dict]
    total: int
