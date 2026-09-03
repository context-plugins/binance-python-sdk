from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row45 import Row45, Row45Dict


class SapiV1SimpleEarnLockedHistoryRedemptionRecordResponse(SdkBaseModel):
    rows: list[Row45]
    total: int


class SapiV1SimpleEarnLockedHistoryRedemptionRecordResponseDict(TypedDict):
    rows: list[Row45 | Row45Dict]
    total: int
