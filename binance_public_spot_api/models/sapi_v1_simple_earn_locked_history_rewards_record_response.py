from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row47 import Row47, Row47Dict


class SapiV1SimpleEarnLockedHistoryRewardsRecordResponse(SdkBaseModel):
    rows: list[Row47]
    total: int


class SapiV1SimpleEarnLockedHistoryRewardsRecordResponseDict(TypedDict):
    rows: list[Row47 | Row47Dict]
    total: int
