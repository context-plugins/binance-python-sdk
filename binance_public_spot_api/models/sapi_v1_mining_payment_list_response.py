from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data13 import Data13, Data13Dict


class SapiV1MiningPaymentListResponse(SdkBaseModel):
    code: int
    msg: str
    data: Data13


class SapiV1MiningPaymentListResponseDict(TypedDict):
    code: int
    msg: str
    data: Data13 | Data13Dict
