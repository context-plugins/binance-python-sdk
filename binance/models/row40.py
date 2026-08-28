from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .tier_annual_percentage_rate import TierAnnualPercentageRate, TierAnnualPercentageRateDict


class Row40(SdkBaseModel):
    total_amount: str = Field(alias="totalAmount")
    tier_annual_percentage_rate: TierAnnualPercentageRate = Field(alias="tierAnnualPercentageRate")
    latest_annual_percentage_rate: str = Field(alias="latestAnnualPercentageRate")
    yesterday_airdrop_percentage_rate: str = Field(alias="yesterdayAirdropPercentageRate")
    asset: str
    air_drop_asset: str = Field(alias="airDropAsset")
    can_redeem: bool = Field(alias="canRedeem")
    collateral_amount: str = Field(alias="collateralAmount")
    product_id: str = Field(alias="productId")
    yesterday_real_time_rewards: str = Field(alias="yesterdayRealTimeRewards")
    cumulative_bonus_rewards: str = Field(alias="cumulativeBonusRewards")
    cumulative_real_time_rewards: str = Field(alias="cumulativeRealTimeRewards")
    cumulative_total_rewards: str = Field(alias="cumulativeTotalRewards")
    auto_subscribe: bool = Field(alias="autoSubscribe")


class Row40Dict(TypedDict):
    total_amount: str
    tier_annual_percentage_rate: TierAnnualPercentageRate | TierAnnualPercentageRateDict
    latest_annual_percentage_rate: str
    yesterday_airdrop_percentage_rate: str
    asset: str
    air_drop_asset: str
    can_redeem: bool
    collateral_amount: str
    product_id: str
    yesterday_real_time_rewards: str
    cumulative_bonus_rewards: str
    cumulative_real_time_rewards: str
    cumulative_total_rewards: str
    auto_subscribe: bool
