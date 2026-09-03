from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Detail4(SdkBaseModel):
    target_asset: str = Field(alias="targetAsset")
    average_price_in_usd: str = Field(alias="averagePriceInUSD")
    """average price of the asset in USD"""

    total_invested_in_usd: str = Field(alias="totalInvestedInUSD")
    """total source asset invested for this target asset in equivilent of USD"""

    current_invested_in_usd: str = Field(alias="currentInvestedInUSD")
    """current invest"""

    purchased_amount: str = Field(alias="purchasedAmount")
    """purchased amount of target asset"""

    pnl_in_usd: str = Field(alias="pnlInUSD")
    """PNL denominated in USD"""

    roi: str
    """ROI calculated in decimal"""

    percentage: str
    """asset allocation in the plan. If it's single plan, then it's 100"""

    available_amount: str = Field(alias="availableAmount")
    redeemed_amount: str = Field(alias="redeemedAmount")
    asset_value_in_usd: str = Field(alias="assetValueInUSD")


class Detail4Dict(TypedDict):
    target_asset: str
    average_price_in_usd: str
    total_invested_in_usd: str
    current_invested_in_usd: str
    purchased_amount: str
    pnl_in_usd: str
    roi: str
    percentage: str
    available_amount: str
    redeemed_amount: str
    asset_value_in_usd: str
