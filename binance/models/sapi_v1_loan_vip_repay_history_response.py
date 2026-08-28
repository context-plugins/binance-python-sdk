from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row13 import Row13, Row13Dict


class SapiV1LoanVipRepayHistoryResponse(SdkBaseModel):
    rows: list[Row13]
    total: int


class SapiV1LoanVipRepayHistoryResponseDict(TypedDict):
    rows: list[Row13 | Row13Dict]
    total: int
