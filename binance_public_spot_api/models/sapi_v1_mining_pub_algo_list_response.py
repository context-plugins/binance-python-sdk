from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data9 import Data9, Data9Dict


class SapiV1MiningPubAlgoListResponse(SdkBaseModel):
    code: int
    msg: str
    data: list[Data9]


class SapiV1MiningPubAlgoListResponseDict(TypedDict):
    code: int
    msg: str
    data: list[Data9 | Data9Dict]
