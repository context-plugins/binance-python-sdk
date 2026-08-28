from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Detail3(SdkBaseModel):
    target_asset: str = Field(alias="targetAsset")
    average_price_in_usd: str = Field(alias="averagePriceInUSD")
    total_invested_in_usd: str = Field(alias="totalInvestedInUSD")
    purchased_amount: str = Field(alias="purchasedAmount")
    purchased_amount_unit: str = Field(alias="purchasedAmountUnit")
    pnl_in_usd: str = Field(alias="pnlInUSD")
    roi: str
    percentage: str
    asset_status: str = Field(alias="assetStatus")
    available_amount: str = Field(alias="availableAmount")
    available_amount_unit: str = Field(alias="availableAmountUnit")
    redeemed_amout: str = Field(alias="redeemedAmout")
    redeemed_amout_unit: str = Field(alias="redeemedAmoutUnit")
    asset_value_in_usd: str = Field(alias="assetValueInUSD")


class Detail3Dict(TypedDict):
    target_asset: str
    average_price_in_usd: str
    total_invested_in_usd: str
    purchased_amount: str
    purchased_amount_unit: str
    pnl_in_usd: str
    roi: str
    percentage: str
    asset_status: str
    available_amount: str
    available_amount_unit: str
    redeemed_amout: str
    redeemed_amout_unit: str
    asset_value_in_usd: str
