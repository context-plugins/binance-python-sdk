from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1SubAccountFuturesPositionRiskResponse(SdkBaseModel):
    entry_price: str = Field(alias="entryPrice")
    leverage: str
    """current initial leverage"""

    max_notional: str = Field(alias="maxNotional")
    """notional value limit of current initial leverage"""

    liquidation_price: str = Field(alias="liquidationPrice")
    mark_price: str = Field(alias="markPrice")
    position_amount: str = Field(alias="positionAmount")
    symbol: str
    unrealized_profit: str = Field(alias="unrealizedProfit")


class SapiV1SubAccountFuturesPositionRiskResponseDict(TypedDict):
    entry_price: str
    leverage: str
    max_notional: str
    liquidation_price: str
    mark_price: str
    position_amount: str
    symbol: str
    unrealized_profit: str
