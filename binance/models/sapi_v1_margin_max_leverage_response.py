from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1MarginMaxLeverageResponse(SdkBaseModel):
    success: bool


class SapiV1MarginMaxLeverageResponseDict(TypedDict):
    success: bool
