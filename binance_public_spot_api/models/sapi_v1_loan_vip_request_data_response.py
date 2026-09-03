from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row17 import Row17, Row17Dict


class SapiV1LoanVipRequestDataResponse(SdkBaseModel):
    total: int
    rows: list[Row17]


class SapiV1LoanVipRequestDataResponseDict(TypedDict):
    total: int
    rows: list[Row17 | Row17Dict]
