from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .detail3 import Detail3, Detail3Dict


class Plan1(SdkBaseModel):
    plan_id: int = Field(alias="planId")
    plan_type: str = Field(alias="planType")
    edit_allowed: str = Field(alias="editAllowed")
    flexible_allowed_to_use: str = Field(alias="flexibleAllowedToUse")
    creation_date_time: int = Field(alias="creationDateTime")
    first_execution_date_time: int = Field(alias="firstExecutionDateTime")
    next_execution_date_time: int = Field(alias="nextExecutionDateTime")
    status: str
    target_asset: str = Field(alias="targetAsset")
    source_asset: str = Field(alias="sourceAsset")
    total_invested_in_usd: str = Field(alias="totalInvestedInUSD")
    plan_value_in_usd: str = Field(alias="planValueInUSD")
    pnl_in_usd: str = Field(alias="pnlInUSD")
    roi: str
    details: list[Detail3]


class Plan1Dict(TypedDict):
    plan_id: int
    plan_type: str
    edit_allowed: str
    flexible_allowed_to_use: str
    creation_date_time: int
    first_execution_date_time: int
    next_execution_date_time: int
    status: str
    target_asset: str
    source_asset: str
    total_invested_in_usd: str
    plan_value_in_usd: str
    pnl_in_usd: str
    roi: str
    details: list[Detail3 | Detail3Dict]
