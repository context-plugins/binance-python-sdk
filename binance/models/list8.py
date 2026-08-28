from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class List8(SdkBaseModel):
    id: str
    invest_coin: str = Field(alias="investCoin")
    exercised_coin: str = Field(alias="exercisedCoin")
    subscription_amount: str = Field(alias="subscriptionAmount")
    strike_price: str = Field(alias="strikePrice")
    duration: int
    settle_date: int = Field(alias="settleDate")
    purchase_status: str = Field(alias="purchaseStatus")
    apr: str
    order_id: int = Field(alias="orderId")
    purchase_end_time: int = Field(alias="purchaseEndTime")
    option_type: str = Field(alias="optionType")
    auto_compound_plan: str = Field(alias="autoCompoundPlan")


class List8Dict(TypedDict):
    id: str
    invest_coin: str
    exercised_coin: str
    subscription_amount: str
    strike_price: str
    duration: int
    settle_date: int
    purchase_status: str
    apr: str
    order_id: int
    purchase_end_time: int
    option_type: str
    auto_compound_plan: str
