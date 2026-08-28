from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row19 import Row19, Row19Dict


class SapiV1LoanOngoingOrdersResponse(SdkBaseModel):
    rows: list[Row19]
    total: int


class SapiV1LoanOngoingOrdersResponseDict(TypedDict):
    rows: list[Row19 | Row19Dict]
    total: int
