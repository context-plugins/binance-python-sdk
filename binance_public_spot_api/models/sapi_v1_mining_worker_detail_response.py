from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data11 import Data11, Data11Dict


class SapiV1MiningWorkerDetailResponse(SdkBaseModel):
    code: int
    msg: str
    data: list[Data11]


class SapiV1MiningWorkerDetailResponseDict(TypedDict):
    code: int
    msg: str
    data: list[Data11 | Data11Dict]
