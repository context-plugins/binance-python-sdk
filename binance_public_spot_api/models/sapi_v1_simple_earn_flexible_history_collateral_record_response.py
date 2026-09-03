from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row49 import Row49, Row49Dict


class SapiV1SimpleEarnFlexibleHistoryCollateralRecordResponse(SdkBaseModel):
    rows: list[Row49]
    total: int


class SapiV1SimpleEarnFlexibleHistoryCollateralRecordResponseDict(TypedDict):
    rows: list[Row49 | Row49Dict]
    total: int
