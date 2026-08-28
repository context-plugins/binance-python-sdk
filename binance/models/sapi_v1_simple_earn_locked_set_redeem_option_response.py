from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1SimpleEarnLockedSetRedeemOptionResponse(SdkBaseModel):
    success: bool


class SapiV1SimpleEarnLockedSetRedeemOptionResponseDict(TypedDict):
    success: bool
