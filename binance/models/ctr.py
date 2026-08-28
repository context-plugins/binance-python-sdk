from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Ctr(SdkBaseModel):
    min_withdraw_amount: str = Field(alias="minWithdrawAmount")
    deposit_status: bool = Field(alias="depositStatus")
    """deposit status (false if ALL of networks' are false)"""

    withdraw_fee: int = Field(alias="withdrawFee")
    withdraw_status: bool = Field(alias="withdrawStatus")
    """withdrawStatus status (false if ALL of networks' are false)"""

    deposit_tip: str = Field(alias="depositTip")


class CtrDict(TypedDict):
    min_withdraw_amount: str
    deposit_status: bool
    withdraw_fee: int
    withdraw_status: bool
    deposit_tip: str
