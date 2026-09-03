from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Detail6(SdkBaseModel):
    asset: str
    reward_asset: str = Field(alias="rewardAsset")
    duration: int
    renewable: bool
    is_sold_out: bool = Field(alias="isSoldOut")
    apr: str
    status: str
    subscription_start_time: str = Field(alias="subscriptionStartTime")
    extra_reward_asset: str = Field(alias="extraRewardAsset")
    extra_reward_apr: str = Field(alias="extraRewardAPR")


class Detail6Dict(TypedDict):
    asset: str
    reward_asset: str
    duration: int
    renewable: bool
    is_sold_out: bool
    apr: str
    status: str
    subscription_start_time: str
    extra_reward_asset: str
    extra_reward_apr: str
