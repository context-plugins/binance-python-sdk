from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row12 import Row12, Row12Dict


class SapiV1LoanVipOngoingOrdersResponse(SdkBaseModel):
    rows: list[Row12]
    total: int


class SapiV1LoanVipOngoingOrdersResponseDict(TypedDict):
    rows: list[Row12 | Row12Dict]
    total: int
