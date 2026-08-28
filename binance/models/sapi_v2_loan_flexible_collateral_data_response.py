from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row30 import Row30, Row30Dict


class SapiV2LoanFlexibleCollateralDataResponse(SdkBaseModel):
    rows: list[Row30]
    total: int


class SapiV2LoanFlexibleCollateralDataResponseDict(TypedDict):
    rows: list[Row30 | Row30Dict]
    total: int
