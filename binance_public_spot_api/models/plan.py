from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Plan(SdkBaseModel):
    plan_id: int = Field(alias="planId")
    plan_type: str = Field(alias="planType")
    edit_allowed: str = Field(alias="editAllowed")
    creation_date_time: int = Field(alias="creationDateTime")
    first_execution_date_time: int = Field(alias="firstExecutionDateTime")
    next_execution_date_time: int = Field(alias="nextExecutionDateTime")
    status: str
    last_updated_date_time: int = Field(alias="lastUpdatedDateTime")
    target_asset: str = Field(alias="targetAsset")
    total_target_amount: str = Field(alias="totalTargetAmount")
    source_asset: str = Field(alias="sourceAsset")
    total_invested_in_usd: str = Field(alias="totalInvestedInUSD")
    subscription_amount: str = Field(alias="subscriptionAmount")
    subscription_cycle: str = Field(alias="subscriptionCycle")
    subscription_start_day: str = Field(alias="subscriptionStartDay")
    subscription_start_weekday: str = Field(alias="subscriptionStartWeekday")
    subscription_start_time: str = Field(alias="subscriptionStartTime")
    source_wallet: str = Field(alias="sourceWallet")
    flexible_allowed_to_use: str = Field(alias="flexibleAllowedToUse")
    plan_value_in_usd: str = Field(alias="planValueInUSD")
    pnl_in_usd: str = Field(alias="pnlInUSD")
    roi: str


class PlanDict(TypedDict):
    plan_id: int
    plan_type: str
    edit_allowed: str
    creation_date_time: int
    first_execution_date_time: int
    next_execution_date_time: int
    status: str
    last_updated_date_time: int
    target_asset: str
    total_target_amount: str
    source_asset: str
    total_invested_in_usd: str
    subscription_amount: str
    subscription_cycle: str
    subscription_start_day: str
    subscription_start_weekday: str
    subscription_start_time: str
    source_wallet: str
    flexible_allowed_to_use: str
    plan_value_in_usd: str
    pnl_in_usd: str
    roi: str
