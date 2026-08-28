from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row15 import Row15, Row15Dict


class SapiV1LoanVipLoanableDataResponse(SdkBaseModel):
    total: int
    rows: list[Row15]


class SapiV1LoanVipLoanableDataResponseDict(TypedDict):
    total: int
    rows: list[Row15 | Row15Dict]
