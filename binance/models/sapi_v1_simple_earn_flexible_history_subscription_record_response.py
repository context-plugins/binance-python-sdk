from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row42 import Row42, Row42Dict


class SapiV1SimpleEarnFlexibleHistorySubscriptionRecordResponse(SdkBaseModel):
    rows: list[Row42]
    total: int


class SapiV1SimpleEarnFlexibleHistorySubscriptionRecordResponseDict(TypedDict):
    rows: list[Row42 | Row42Dict]
    total: int
