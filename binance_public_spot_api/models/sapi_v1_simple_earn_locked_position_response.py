from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row41 import Row41, Row41Dict


class SapiV1SimpleEarnLockedPositionResponse(SdkBaseModel):
    rows: list[Row41]
    total: int


class SapiV1SimpleEarnLockedPositionResponseDict(TypedDict):
    rows: list[Row41 | Row41Dict]
    total: int
