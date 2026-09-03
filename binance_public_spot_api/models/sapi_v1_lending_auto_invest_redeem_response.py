from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1LendingAutoInvestRedeemResponse(SdkBaseModel):
    redemption_id: int = Field(alias="redemptionId")


class SapiV1LendingAutoInvestRedeemResponseDict(TypedDict):
    redemption_id: int
