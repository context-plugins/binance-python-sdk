from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1SubAccountVirtualSubAccountResponse(SdkBaseModel):
    email: str


class SapiV1SubAccountVirtualSubAccountResponseDict(TypedDict):
    email: str
