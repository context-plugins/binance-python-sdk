from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1CapitalDepositCreditApplyResponse(SdkBaseModel):
    code: str
    message: str
    data: bool
    success: bool


class SapiV1CapitalDepositCreditApplyResponseDict(TypedDict):
    code: str
    message: str
    data: bool
    success: bool
