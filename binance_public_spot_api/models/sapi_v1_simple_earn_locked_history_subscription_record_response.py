from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row43 import Row43, Row43Dict


class SapiV1SimpleEarnLockedHistorySubscriptionRecordResponse(SdkBaseModel):
    rows: list[Row43]
    total: int


class SapiV1SimpleEarnLockedHistorySubscriptionRecordResponseDict(TypedDict):
    rows: list[Row43 | Row43Dict]
    total: int
