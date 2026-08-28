from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1SimpleEarnLockedSubscribeResponse(SdkBaseModel):
    purchase_id: int = Field(alias="purchaseId")
    position_id: str = Field(alias="positionId")
    success: bool


class SapiV1SimpleEarnLockedSubscribeResponseDict(TypedDict):
    purchase_id: int
    position_id: str
    success: bool
