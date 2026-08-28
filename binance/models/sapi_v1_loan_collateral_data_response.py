from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row23 import Row23, Row23Dict


class SapiV1LoanCollateralDataResponse(SdkBaseModel):
    rows: list[Row23]
    total: int


class SapiV1LoanCollateralDataResponseDict(TypedDict):
    rows: list[Row23 | Row23Dict]
    total: int
