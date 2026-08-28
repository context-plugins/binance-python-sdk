from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1SimpleEarnFlexibleSetAutoSubscribeResponse(SdkBaseModel):
    success: bool


class SapiV1SimpleEarnFlexibleSetAutoSubscribeResponseDict(TypedDict):
    success: bool
