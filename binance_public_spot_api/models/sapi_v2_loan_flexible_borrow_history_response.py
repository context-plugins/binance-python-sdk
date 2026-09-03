from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row26 import Row26, Row26Dict


class SapiV2LoanFlexibleBorrowHistoryResponse(SdkBaseModel):
    total: int
    rows: list[Row26]


class SapiV2LoanFlexibleBorrowHistoryResponseDict(TypedDict):
    total: int
    rows: list[Row26 | Row26Dict]
