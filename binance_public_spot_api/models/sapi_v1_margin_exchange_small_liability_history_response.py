from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row5 import Row5, Row5Dict


class SapiV1MarginExchangeSmallLiabilityHistoryResponse(SdkBaseModel):
    total: int
    rows: list[Row5]


class SapiV1MarginExchangeSmallLiabilityHistoryResponseDict(TypedDict):
    total: int
    rows: list[Row5 | Row5Dict]
