from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .tier_annual_percentage_rate import TierAnnualPercentageRate, TierAnnualPercentageRateDict


class Row38(SdkBaseModel):
    asset: str
    latest_annual_percentage_rate: str = Field(alias="latestAnnualPercentageRate")
    tier_annual_percentage_rate: TierAnnualPercentageRate = Field(alias="tierAnnualPercentageRate")
    air_drop_percentage_rate: str = Field(alias="airDropPercentageRate")
    can_purchase: bool = Field(alias="canPurchase")
    can_redeem: bool = Field(alias="canRedeem")
    is_sold_out: bool = Field(alias="isSoldOut")
    hot: bool
    min_purchase_amount: str = Field(alias="minPurchaseAmount")
    product_id: str = Field(alias="productId")
    subscription_start_time: str = Field(alias="subscriptionStartTime")
    status: str


class Row38Dict(TypedDict):
    asset: str
    latest_annual_percentage_rate: str
    tier_annual_percentage_rate: TierAnnualPercentageRate | TierAnnualPercentageRateDict
    air_drop_percentage_rate: str
    can_purchase: bool
    can_redeem: bool
    is_sold_out: bool
    hot: bool
    min_purchase_amount: str
    product_id: str
    subscription_start_time: str
    status: str
