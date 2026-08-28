from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ApiV3MyPreventedMatchesResponse(SdkBaseModel):
    symbol: str
    prevented_match_id: int = Field(alias="preventedMatchId")
    taker_order_id: int = Field(alias="takerOrderId")
    maker_order_id: int = Field(alias="makerOrderId")
    trade_group_id: int = Field(alias="tradeGroupId")
    self_trade_prevention_mode: str = Field(alias="selfTradePreventionMode")
    price: str
    maker_prevented_quantity: str = Field(alias="makerPreventedQuantity")
    transact_time: int = Field(alias="transactTime")


class ApiV3MyPreventedMatchesResponseDict(TypedDict):
    symbol: str
    prevented_match_id: int
    taker_order_id: int
    maker_order_id: int
    trade_group_id: int
    self_trade_prevention_mode: str
    price: str
    maker_prevented_quantity: str
    transact_time: int
