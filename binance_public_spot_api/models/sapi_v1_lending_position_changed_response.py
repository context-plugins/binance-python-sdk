from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1LendingPositionChangedResponse(SdkBaseModel):
    daily_purchase_id: int = Field(alias="dailyPurchaseId")
    success: bool
    time: int


class SapiV1LendingPositionChangedResponseDict(TypedDict):
    daily_purchase_id: int
    success: bool
    time: int
