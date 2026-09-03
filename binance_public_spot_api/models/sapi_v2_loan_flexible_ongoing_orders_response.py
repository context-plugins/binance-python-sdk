from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row25 import Row25, Row25Dict


class SapiV2LoanFlexibleOngoingOrdersResponse(SdkBaseModel):
    total: int
    rows: list[Row25]


class SapiV2LoanFlexibleOngoingOrdersResponseDict(TypedDict):
    total: int
    rows: list[Row25 | Row25Dict]
