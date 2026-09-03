from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row44 import Row44, Row44Dict


class SapiV1SimpleEarnFlexibleHistoryRedemptionRecordResponse(SdkBaseModel):
    rows: list[Row44]
    total: int


class SapiV1SimpleEarnFlexibleHistoryRedemptionRecordResponseDict(TypedDict):
    rows: list[Row44 | Row44Dict]
    total: int
