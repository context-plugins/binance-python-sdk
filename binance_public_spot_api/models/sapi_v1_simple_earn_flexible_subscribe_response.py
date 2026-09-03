from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1SimpleEarnFlexibleSubscribeResponse(SdkBaseModel):
    purchase_id: int = Field(alias="purchaseId")
    success: bool


class SapiV1SimpleEarnFlexibleSubscribeResponseDict(TypedDict):
    purchase_id: int
    success: bool
