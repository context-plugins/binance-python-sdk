from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row38 import Row38, Row38Dict


class SapiV1SimpleEarnFlexibleListResponse(SdkBaseModel):
    rows: list[Row38]
    total: int


class SapiV1SimpleEarnFlexibleListResponseDict(TypedDict):
    rows: list[Row38 | Row38Dict]
    total: int
