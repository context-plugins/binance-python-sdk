from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row22 import Row22, Row22Dict


class SapiV1LoanLoanableDataResponse(SdkBaseModel):
    rows: list[Row22]
    total: int


class SapiV1LoanLoanableDataResponseDict(TypedDict):
    rows: list[Row22 | Row22Dict]
    total: int
