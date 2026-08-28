from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1AccountStatusResponse(SdkBaseModel):
    data: str


class SapiV1AccountStatusResponseDict(TypedDict):
    data: str
