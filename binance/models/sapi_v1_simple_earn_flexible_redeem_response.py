from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1SimpleEarnFlexibleRedeemResponse(SdkBaseModel):
    redeem_id: int = Field(alias="redeemId")
    success: bool


class SapiV1SimpleEarnFlexibleRedeemResponseDict(TypedDict):
    redeem_id: int
    success: bool
