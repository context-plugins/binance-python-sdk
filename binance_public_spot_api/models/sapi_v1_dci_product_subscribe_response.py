from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SapiV1DciProductSubscribeResponse(SdkBaseModel):
    position_id: int = Field(alias="positionId")
    invest_coin: str = Field(alias="investCoin")
    exercised_coin: str = Field(alias="exercisedCoin")
    subscription_amount: str = Field(alias="subscriptionAmount")
    duration: int
    auto_compound_plan: str = Field(alias="autoCompoundPlan")
    """STANDARD, ADVANCED, this field won't display when autocompound is set to None"""

    strike_price: str = Field(alias="strikePrice")
    settle_date: int = Field(alias="settleDate")
    purchase_status: str = Field(alias="purchaseStatus")
    apr: str
    order_id: int = Field(alias="orderId")
    purchase_time: int = Field(alias="purchaseTime")
    option_type: Optional[str] = Field(default=UNSET, alias="optionType\"")


class SapiV1DciProductSubscribeResponseDict(TypedDict):
    position_id: int
    invest_coin: str
    exercised_coin: str
    subscription_amount: str
    duration: int
    auto_compound_plan: str
    strike_price: str
    settle_date: int
    purchase_status: str
    apr: str
    order_id: int
    purchase_time: int
    option_type: NotRequired[str]
