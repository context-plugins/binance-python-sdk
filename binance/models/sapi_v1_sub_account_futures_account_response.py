from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .assets1 import Assets1, Assets1Dict


class SapiV1SubAccountFuturesAccountResponse(SdkBaseModel):
    email: str
    asset: str
    assets: list[Assets1]
    can_deposit: bool = Field(alias="canDeposit")
    can_trade: bool = Field(alias="canTrade")
    can_withdraw: bool = Field(alias="canWithdraw")
    fee_tier: int = Field(alias="feeTier")
    max_withdraw_amount: str = Field(alias="maxWithdrawAmount")
    total_initial_margin: str = Field(alias="totalInitialMargin")
    total_maintenance_margin: str = Field(alias="totalMaintenanceMargin")
    total_margin_balance: str = Field(alias="totalMarginBalance")
    total_open_order_initial_margin: str = Field(alias="totalOpenOrderInitialMargin")
    total_position_initial_margin: str = Field(alias="totalPositionInitialMargin")
    total_unrealized_profit: str = Field(alias="totalUnrealizedProfit")
    total_wallet_balance: str = Field(alias="totalWalletBalance")
    update_time: int = Field(alias="updateTime")


class SapiV1SubAccountFuturesAccountResponseDict(TypedDict):
    email: str
    asset: str
    assets: list[Assets1 | Assets1Dict]
    can_deposit: bool
    can_trade: bool
    can_withdraw: bool
    fee_tier: int
    max_withdraw_amount: str
    total_initial_margin: str
    total_maintenance_margin: str
    total_margin_balance: str
    total_open_order_initial_margin: str
    total_position_initial_margin: str
    total_unrealized_profit: str
    total_wallet_balance: str
    update_time: int
