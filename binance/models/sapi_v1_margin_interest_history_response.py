from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row3 import Row3, Row3Dict


class SapiV1MarginInterestHistoryResponse(SdkBaseModel):
    rows: list[Row3]
    total: int


class SapiV1MarginInterestHistoryResponseDict(TypedDict):
    rows: list[Row3 | Row3Dict]
    total: int
