from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1MarginIsolatedAccountResponse(SdkBaseModel):
    success: bool
    symbol: str


class SapiV1MarginIsolatedAccountResponseDict(TypedDict):
    success: bool
    symbol: str
