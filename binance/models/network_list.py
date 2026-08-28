from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class NetworkList(SdkBaseModel):
    address_regex: str = Field(alias="addressRegex")
    coin: str
    deposit_desc: str = Field(alias="depositDesc")
    """shown only when "depositEnable" is false."""

    deposit_enable: bool = Field(alias="depositEnable")
    is_default: bool = Field(alias="isDefault")
    memo_regex: str = Field(alias="memoRegex")
    min_confirm: int = Field(alias="minConfirm")
    """min number for balance confirmation."""

    name: str
    network: str
    special_tips: str = Field(alias="specialTips")
    un_lock_confirm: int = Field(alias="unLockConfirm")
    """confirmation number for balance unlock."""

    withdraw_desc: str = Field(alias="withdrawDesc")
    """shown only when "withdrawEnable" is false"""

    withdraw_enable: bool = Field(alias="withdrawEnable")
    withdraw_fee: str = Field(alias="withdrawFee")
    withdraw_integer_multiple: str = Field(alias="withdrawIntegerMultiple")
    withdraw_max: str = Field(alias="withdrawMax")
    withdraw_min: str = Field(alias="withdrawMin")
    same_address: bool = Field(alias="sameAddress")


class NetworkListDict(TypedDict):
    address_regex: str
    coin: str
    deposit_desc: str
    deposit_enable: bool
    is_default: bool
    memo_regex: str
    min_confirm: int
    name: str
    network: str
    special_tips: str
    un_lock_confirm: int
    withdraw_desc: str
    withdraw_enable: bool
    withdraw_fee: str
    withdraw_integer_multiple: str
    withdraw_max: str
    withdraw_min: str
    same_address: bool
