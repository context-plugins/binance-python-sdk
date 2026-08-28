from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1GiftcardCryptographyRsaPublicKeyResponse(SdkBaseModel):
    code: str
    message: str
    data: str
    success: bool


class SapiV1GiftcardCryptographyRsaPublicKeyResponseDict(TypedDict):
    code: str
    message: str
    data: str
    success: bool
