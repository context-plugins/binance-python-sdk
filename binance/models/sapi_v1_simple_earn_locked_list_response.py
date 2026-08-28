from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row39 import Row39, Row39Dict


class SapiV1SimpleEarnLockedListResponse(SdkBaseModel):
    rows: list[Row39]
    total: int


class SapiV1SimpleEarnLockedListResponseDict(TypedDict):
    rows: list[Row39 | Row39Dict]
    total: int
