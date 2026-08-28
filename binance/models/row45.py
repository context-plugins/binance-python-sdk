from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row45(SdkBaseModel):
    position_id: str = Field(alias="positionId")
    redeem_id: int = Field(alias="redeemId")
    time: int
    asset: str
    lock_period: str = Field(alias="lockPeriod")
    amount: str
    original_amount: str = Field(alias="originalAmount")
    type_: str = Field(alias="type")
    """MATURE for redeem to Spot Wallet, NEW_TRANSFERRED for redeem to Flexible product, AHEAD for early redemption"""

    deliver_date: str = Field(alias="deliverDate")
    loss_amount: str = Field(alias="lossAmount")
    """Loss of profit on early redemption"""

    is_complete: bool = Field(alias="isComplete")
    reward_asset: str = Field(alias="rewardAsset")
    reward_amt: str = Field(alias="rewardAmt")
    extra_reward_asset: str = Field(alias="extraRewardAsset")
    est_extra_reward_amt: str = Field(alias="estExtraRewardAmt")
    status: str


class Row45Dict(TypedDict):
    position_id: str
    redeem_id: int
    time: int
    asset: str
    lock_period: str
    amount: str
    original_amount: str
    type_: str
    deliver_date: str
    loss_amount: str
    is_complete: bool
    reward_asset: str
    reward_amt: str
    extra_reward_asset: str
    est_extra_reward_amt: str
    status: str
