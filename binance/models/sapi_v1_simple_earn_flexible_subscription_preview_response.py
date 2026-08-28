from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1SimpleEarnFlexibleSubscriptionPreviewResponse(SdkBaseModel):
    total_amount: str = Field(alias="totalAmount")
    reward_asset: str = Field(alias="rewardAsset")
    air_drop_asset: str = Field(alias="airDropAsset")
    est_daily_bonus_rewards: str = Field(alias="estDailyBonusRewards")
    est_daily_real_time_rewards: str = Field(alias="estDailyRealTimeRewards")
    est_daily_airdrop_rewards: str = Field(alias="estDailyAirdropRewards")


class SapiV1SimpleEarnFlexibleSubscriptionPreviewResponseDict(TypedDict):
    total_amount: str
    reward_asset: str
    air_drop_asset: str
    est_daily_bonus_rewards: str
    est_daily_real_time_rewards: str
    est_daily_airdrop_rewards: str
