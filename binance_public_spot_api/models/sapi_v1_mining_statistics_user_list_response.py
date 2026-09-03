from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data18 import Data18, Data18Dict


class SapiV1MiningStatisticsUserListResponse(SdkBaseModel):
    code: int
    msg: str
    data: list[Data18]


class SapiV1MiningStatisticsUserListResponseDict(TypedDict):
    code: int
    msg: str
    data: list[Data18 | Data18Dict]
