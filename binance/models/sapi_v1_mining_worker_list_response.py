from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data12 import Data12, Data12Dict


class SapiV1MiningWorkerListResponse(SdkBaseModel):
    code: int
    msg: str
    data: Data12


class SapiV1MiningWorkerListResponseDict(TypedDict):
    code: int
    msg: str
    data: Data12 | Data12Dict
