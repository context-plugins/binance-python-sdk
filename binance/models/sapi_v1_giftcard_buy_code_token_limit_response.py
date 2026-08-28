from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data29 import Data29, Data29Dict


class SapiV1GiftcardBuyCodeTokenLimitResponse(SdkBaseModel):
    code: str
    message: str
    data: Data29
    success: bool


class SapiV1GiftcardBuyCodeTokenLimitResponseDict(TypedDict):
    code: str
    message: str
    data: Data29 | Data29Dict
    success: bool
