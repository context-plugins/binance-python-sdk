from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data25 import Data25, Data25Dict


class SapiV1GiftcardBuyCodeResponse(SdkBaseModel):
    code: str
    message: str
    data: Data25
    success: bool


class SapiV1GiftcardBuyCodeResponseDict(TypedDict):
    code: str
    message: str
    data: Data25 | Data25Dict
    success: bool
