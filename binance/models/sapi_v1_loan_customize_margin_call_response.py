from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row24 import Row24, Row24Dict


class SapiV1LoanCustomizeMarginCallResponse(SdkBaseModel):
    rows: list[Row24]
    total: int


class SapiV1LoanCustomizeMarginCallResponseDict(TypedDict):
    rows: list[Row24 | Row24Dict]
    total: int
