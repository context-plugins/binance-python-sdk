from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row16 import Row16, Row16Dict


class SapiV1LoanVipCollateralDataResponse(SdkBaseModel):
    rows: list[Row16]
    total: int


class SapiV1LoanVipCollateralDataResponseDict(TypedDict):
    rows: list[Row16 | Row16Dict]
    total: int
