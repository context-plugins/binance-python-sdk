from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DeliveryPositionRiskVo(SdkBaseModel):
    entry_price: str = Field(alias="entryPrice")
    mark_price: str = Field(alias="markPrice")
    leverage: str
    isolated: str
    isolated_wallet: str = Field(alias="isolatedWallet")
    isolated_margin: str = Field(alias="isolatedMargin")
    is_auto_add_margin: str = Field(alias="isAutoAddMargin")
    position_side: str = Field(alias="positionSide")
    position_amount: str = Field(alias="positionAmount")
    symbol: str
    unrealized_profit: str = Field(alias="unrealizedProfit")


class DeliveryPositionRiskVoDict(TypedDict):
    entry_price: str
    mark_price: str
    leverage: str
    isolated: str
    isolated_wallet: str
    isolated_margin: str
    is_auto_add_margin: str
    position_side: str
    position_amount: str
    symbol: str
    unrealized_profit: str
