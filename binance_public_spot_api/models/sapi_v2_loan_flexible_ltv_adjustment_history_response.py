from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row28 import Row28, Row28Dict


class SapiV2LoanFlexibleLtvAdjustmentHistoryResponse(SdkBaseModel):
    rows: list[Row28]
    total: int


class SapiV2LoanFlexibleLtvAdjustmentHistoryResponseDict(TypedDict):
    rows: list[Row28 | Row28Dict]
    total: int
