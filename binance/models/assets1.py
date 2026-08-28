from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Assets1(SdkBaseModel):
    asset: str
    initial_margin: str = Field(alias="initialMargin")
    maintenance_margin: str = Field(alias="maintenanceMargin")
    margin_balance: str = Field(alias="marginBalance")
    max_withdraw_amount: str = Field(alias="maxWithdrawAmount")
    open_order_initial_margin: str = Field(alias="openOrderInitialMargin")
    position_initial_margin: str = Field(alias="positionInitialMargin")
    unrealized_profit: str = Field(alias="unrealizedProfit")
    wallet_balance: str = Field(alias="walletBalance")


class Assets1Dict(TypedDict):
    asset: str
    initial_margin: str
    maintenance_margin: str
    margin_balance: str
    max_withdraw_amount: str
    open_order_initial_margin: str
    position_initial_margin: str
    unrealized_profit: str
    wallet_balance: str
