from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data26 import Data26, Data26Dict


class SapiV1GiftcardRedeemCodeResponse(SdkBaseModel):
    code: str
    message: str
    data: Data26
    success: bool


class SapiV1GiftcardRedeemCodeResponseDict(TypedDict):
    code: str
    message: str
    data: Data26 | Data26Dict
    success: bool
