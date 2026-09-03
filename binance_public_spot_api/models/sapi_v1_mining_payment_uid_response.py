from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data19 import Data19, Data19Dict


class SapiV1MiningPaymentUidResponse(SdkBaseModel):
    code: int
    msg: str
    data: Data19


class SapiV1MiningPaymentUidResponseDict(TypedDict):
    code: int
    msg: str
    data: Data19 | Data19Dict
