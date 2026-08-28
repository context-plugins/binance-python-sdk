from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row18 import Row18, Row18Dict


class SapiV1LoanBorrowHistoryResponse(SdkBaseModel):
    rows: list[Row18]
    total: int


class SapiV1LoanBorrowHistoryResponseDict(TypedDict):
    rows: list[Row18 | Row18Dict]
    total: int
