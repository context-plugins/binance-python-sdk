from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data10 import Data10, Data10Dict


class SapiV1MiningPubCoinListResponse(SdkBaseModel):
    code: int
    msg: str
    data: list[Data10]


class SapiV1MiningPubCoinListResponseDict(TypedDict):
    code: int
    msg: str
    data: list[Data10 | Data10Dict]
