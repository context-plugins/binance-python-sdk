from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data14 import Data14, Data14Dict


class SapiV1MiningPaymentOtherResponse(SdkBaseModel):
    code: int
    msg: str
    data: Data14


class SapiV1MiningPaymentOtherResponseDict(TypedDict):
    code: int
    msg: str
    data: Data14 | Data14Dict
