from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .current_basket import CurrentBasket, CurrentBasketDict


class SapiV1BlvtTokenInfoResponse(SdkBaseModel):
    token_name: str = Field(alias="tokenName")
    description: str
    underlying: str
    token_issued: str = Field(alias="tokenIssued")
    basket: str
    current_baskets: list[CurrentBasket] = Field(alias="currentBaskets")
    nav: str
    real_leverage: str = Field(alias="realLeverage")
    funding_rate: str = Field(alias="fundingRate")
    daily_management_fee: str = Field(alias="dailyManagementFee")
    purchase_fee_pct: str = Field(alias="purchaseFeePct")
    daily_purchase_limit: str = Field(alias="dailyPurchaseLimit")
    redeem_fee_pct: str = Field(alias="redeemFeePct")
    daily_redeem_limit: str = Field(alias="dailyRedeemLimit")
    timestamp: int


class SapiV1BlvtTokenInfoResponseDict(TypedDict):
    token_name: str
    description: str
    underlying: str
    token_issued: str
    basket: str
    current_baskets: list[CurrentBasket | CurrentBasketDict]
    nav: str
    real_leverage: str
    funding_rate: str
    daily_management_fee: str
    purchase_fee_pct: str
    daily_purchase_limit: str
    redeem_fee_pct: str
    daily_redeem_limit: str
    timestamp: int
