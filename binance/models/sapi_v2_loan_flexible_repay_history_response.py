from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row27 import Row27, Row27Dict


class SapiV2LoanFlexibleRepayHistoryResponse(SdkBaseModel):
    rows: list[Row27]
    total: int


class SapiV2LoanFlexibleRepayHistoryResponseDict(TypedDict):
    rows: list[Row27 | Row27Dict]
    total: int
