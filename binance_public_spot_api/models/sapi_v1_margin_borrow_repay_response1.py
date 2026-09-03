from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row1 import Row1, Row1Dict


class SapiV1MarginBorrowRepayResponse1(SdkBaseModel):
    rows: list[Row1]
    total: int


class SapiV1MarginBorrowRepayResponse1Dict(TypedDict):
    rows: list[Row1 | Row1Dict]
    total: int
