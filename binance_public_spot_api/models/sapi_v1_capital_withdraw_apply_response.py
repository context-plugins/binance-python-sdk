from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1CapitalWithdrawApplyResponse(SdkBaseModel):
    id: str


class SapiV1CapitalWithdrawApplyResponseDict(TypedDict):
    id: str
