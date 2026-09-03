from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data27 import Data27, Data27Dict


class SapiV1GiftcardVerifyResponse(SdkBaseModel):
    code: str
    message: str
    data: Data27
    success: bool


class SapiV1GiftcardVerifyResponseDict(TypedDict):
    code: str
    message: str
    data: Data27 | Data27Dict
    success: bool
