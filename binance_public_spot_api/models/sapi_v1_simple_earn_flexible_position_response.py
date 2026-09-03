from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row40 import Row40, Row40Dict


class SapiV1SimpleEarnFlexiblePositionResponse(SdkBaseModel):
    rows: list[Row40]
    total: int


class SapiV1SimpleEarnFlexiblePositionResponseDict(TypedDict):
    rows: list[Row40 | Row40Dict]
    total: int
