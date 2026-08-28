from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data21 import Data21, Data21Dict


class SapiV1C2COrderMatchListUserOrderHistoryResponse(SdkBaseModel):
    code: str
    message: str
    data: list[Data21]
    total: int
    success: bool


class SapiV1C2COrderMatchListUserOrderHistoryResponseDict(TypedDict):
    code: str
    message: str
    data: list[Data21 | Data21Dict]
    total: int
    success: bool
