from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1SimpleEarnLockedSubscriptionPreviewResponse(SdkBaseModel):
    reward_asset: str = Field(alias="rewardAsset")
    total_reward_amt: str = Field(alias="totalRewardAmt")
    extra_reward_asset: str = Field(alias="extraRewardAsset")
    est_total_extra_reward_amt: str = Field(alias="estTotalExtraRewardAmt")
    next_pay: str = Field(alias="nextPay")
    next_pay_date: str = Field(alias="nextPayDate")
    value_date: str = Field(alias="valueDate")
    rewards_end_date: str = Field(alias="rewardsEndDate")
    deliver_date: str = Field(alias="deliverDate")
    next_subscription_date: str = Field(alias="nextSubscriptionDate")


class SapiV1SimpleEarnLockedSubscriptionPreviewResponseDict(TypedDict):
    reward_asset: str
    total_reward_amt: str
    extra_reward_asset: str
    est_total_extra_reward_amt: str
    next_pay: str
    next_pay_date: str
    value_date: str
    rewards_end_date: str
    deliver_date: str
    next_subscription_date: str
