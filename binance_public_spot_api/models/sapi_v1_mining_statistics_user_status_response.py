from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data17 import Data17, Data17Dict


class SapiV1MiningStatisticsUserStatusResponse(SdkBaseModel):
    code: int
    msg: str
    data: Data17


class SapiV1MiningStatisticsUserStatusResponseDict(TypedDict):
    code: int
    msg: str
    data: Data17 | Data17Dict
