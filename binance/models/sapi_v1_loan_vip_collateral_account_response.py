from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row14 import Row14, Row14Dict


class SapiV1LoanVipCollateralAccountResponse(SdkBaseModel):
    rows: list[Row14]
    total: int


class SapiV1LoanVipCollateralAccountResponseDict(TypedDict):
    rows: list[Row14 | Row14Dict]
    total: int
