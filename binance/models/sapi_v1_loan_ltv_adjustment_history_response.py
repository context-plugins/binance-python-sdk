from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row21 import Row21, Row21Dict


class SapiV1LoanLtvAdjustmentHistoryResponse(SdkBaseModel):
    rows: list[Row21]
    total: int


class SapiV1LoanLtvAdjustmentHistoryResponseDict(TypedDict):
    rows: list[Row21 | Row21Dict]
    total: int
