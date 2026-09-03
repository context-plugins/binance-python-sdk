from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .plan1 import Plan1, Plan1Dict


class SapiV1LendingAutoInvestPlanIdResponse(SdkBaseModel):
    plan_value_in_usd: Optional[str] = Field(default=UNSET, alias="planValueInUSD")
    plan_value_in_btc: Optional[str] = Field(default=UNSET, alias="planValueInBTC")
    pnl_in_usd: Optional[str] = Field(default=UNSET, alias="pnlInUSD")
    roi: Optional[str] = UNSET
    plan: Optional[list[Plan1]] = UNSET


class SapiV1LendingAutoInvestPlanIdResponseDict(TypedDict):
    plan_value_in_usd: NotRequired[str]
    plan_value_in_btc: NotRequired[str]
    pnl_in_usd: NotRequired[str]
    roi: NotRequired[str]
    plan: NotRequired[list[Plan1 | Plan1Dict]]
