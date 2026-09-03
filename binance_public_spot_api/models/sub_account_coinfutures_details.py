from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .asset2 import Asset2, Asset2Dict


class SubAccountCoinfuturesDetails(SdkBaseModel):
    email: str
    assets: list[Asset2]
    can_deposit: bool = Field(alias="canDeposit")
    can_trade: bool = Field(alias="canTrade")
    can_withdraw: bool = Field(alias="canWithdraw")
    fee_tier: int = Field(alias="feeTier")
    update_time: int = Field(alias="updateTime")


class SubAccountCoinfuturesDetailsDict(TypedDict):
    email: str
    assets: list[Asset2 | Asset2Dict]
    can_deposit: bool
    can_trade: bool
    can_withdraw: bool
    fee_tier: int
    update_time: int
