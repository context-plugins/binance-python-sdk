from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class List7(SdkBaseModel):
    id: str
    invest_coin: str = Field(alias="investCoin")
    exercised_coin: str = Field(alias="exercisedCoin")
    strike_price: str = Field(alias="strikePrice")
    duration: int
    settle_date: int = Field(alias="settleDate")
    purchase_decimal: int = Field(alias="purchaseDecimal")
    purchase_end_time: int = Field(alias="purchaseEndTime")
    can_purchase: bool = Field(alias="canPurchase")
    apr: str
    order_id: int = Field(alias="orderId")
    min_amount: str = Field(alias="minAmount")
    max_amount: str = Field(alias="maxAmount")
    create_timestamp: int = Field(alias="createTimestamp")
    option_type: str = Field(alias="optionType")
    is_auto_compound_enable: bool = Field(alias="isAutoCompoundEnable")
    auto_compound_plan_list: list[str] = Field(alias="autoCompoundPlanList")


class List7Dict(TypedDict):
    id: str
    invest_coin: str
    exercised_coin: str
    strike_price: str
    duration: int
    settle_date: int
    purchase_decimal: int
    purchase_end_time: int
    can_purchase: bool
    apr: str
    order_id: int
    min_amount: str
    max_amount: str
    create_timestamp: int
    option_type: str
    is_auto_compound_enable: bool
    auto_compound_plan_list: list[str]
