from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row20 import Row20, Row20Dict


class SapiV1LoanRepayHistoryResponse(SdkBaseModel):
    rows: list[Row20]
    total: int


class SapiV1LoanRepayHistoryResponseDict(TypedDict):
    rows: list[Row20 | Row20Dict]
    total: int
