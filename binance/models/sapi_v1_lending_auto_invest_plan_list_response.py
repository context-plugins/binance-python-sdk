from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .plan import Plan, PlanDict


class SapiV1LendingAutoInvestPlanListResponse(SdkBaseModel):
    plan_value_in_usd: str = Field(alias="planValueInUSD")
    plan_value_in_btc: str = Field(alias="planValueInBTC")
    pnl_in_usd: str = Field(alias="pnlInUSD")
    roi: str
    plan: list[Plan]


class SapiV1LendingAutoInvestPlanListResponseDict(TypedDict):
    plan_value_in_usd: str
    plan_value_in_btc: str
    pnl_in_usd: str
    roi: str
    plan: list[Plan | PlanDict]
