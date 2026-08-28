from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row29 import Row29, Row29Dict


class SapiV2LoanFlexibleLoanableDataResponse(SdkBaseModel):
    rows: list[Row29]
    total: int


class SapiV2LoanFlexibleLoanableDataResponseDict(TypedDict):
    rows: list[Row29 | Row29Dict]
    total: int
