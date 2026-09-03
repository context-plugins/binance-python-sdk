from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row4 import Row4, Row4Dict


class SapiV1MarginForceLiquidationRecResponse(SdkBaseModel):
    rows: list[Row4]
    total: int


class SapiV1MarginForceLiquidationRecResponseDict(TypedDict):
    rows: list[Row4 | Row4Dict]
    total: int
