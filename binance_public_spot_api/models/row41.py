from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row41(SdkBaseModel):
    position_id: str = Field(alias="positionId")
    parent_position_id: str = Field(alias="parentPositionId")
    project_id: str = Field(alias="projectId")
    asset: str
    amount: str
    purchase_time: str = Field(alias="purchaseTime")
    duration: str
    accrual_days: str = Field(alias="accrualDays")
    reward_asset: str = Field(alias="rewardAsset")
    apy: str = Field(alias="APY")
    reward_amt: str = Field(alias="rewardAmt")
    """Earned amount"""

    extra_reward_asset: str = Field(alias="extraRewardAsset")
    """Rewards assets of extra staking type"""

    extra_reward_apr: str = Field(alias="extraRewardAPR")
    """APR of extra staking type"""

    est_extra_reward_amt: str = Field(alias="estExtraRewardAmt")
    """Rewards of extra staking type, distribute when order expires"""

    next_pay: str = Field(alias="nextPay")
    """Next estimated rewards payment"""

    next_pay_date: str = Field(alias="nextPayDate")
    """Next rewards payment date"""

    pay_period: str = Field(alias="payPeriod")
    """Payment cycle"""

    redeem_amount_early: str = Field(alias="redeemAmountEarly")
    """Early redemption amount"""

    rewards_end_date: str = Field(alias="rewardsEndDate")
    """Rewards accrual end date"""

    deliver_date: str = Field(alias="deliverDate")
    """Redemption arrival time"""

    redeem_period: str = Field(alias="redeemPeriod")
    """Redemption interval"""

    redeeming_amt: str = Field(alias="redeemingAmt")
    """Amount under redemption"""

    redeem_to: str = Field(alias="redeemTo")
    """Redeem to Flexible product or Spot wallet"""

    partial_amt_deliver_date: str = Field(alias="partialAmtDeliverDate")
    """Arrival time of partial redemption amount of order"""

    can_redeem_early: bool = Field(alias="canRedeemEarly")
    """When it is true, early redemption can be operated"""

    can_fast_redemption: bool = Field(alias="canFastRedemption")
    """When it is true, fast redemption can be operated"""

    auto_subscribe: bool = Field(alias="autoSubscribe")
    """When it is true, auto staking can be operated"""

    type_: str = Field(alias="type")
    """Order type is auto subscribe or normal"""

    status: str
    can_re_stake: bool = Field(alias="canReStake")


class Row41Dict(TypedDict):
    position_id: str
    parent_position_id: str
    project_id: str
    asset: str
    amount: str
    purchase_time: str
    duration: str
    accrual_days: str
    reward_asset: str
    apy: str
    reward_amt: str
    extra_reward_asset: str
    extra_reward_apr: str
    est_extra_reward_amt: str
    next_pay: str
    next_pay_date: str
    pay_period: str
    redeem_amount_early: str
    rewards_end_date: str
    deliver_date: str
    redeem_period: str
    redeeming_amt: str
    redeem_to: str
    partial_amt_deliver_date: str
    can_redeem_early: bool
    can_fast_redemption: bool
    auto_subscribe: bool
    type_: str
    status: str
    can_re_stake: bool
