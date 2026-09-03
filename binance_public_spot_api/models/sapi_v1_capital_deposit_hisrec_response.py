from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1CapitalDepositHisrecResponse(SdkBaseModel):
    amount: str
    coin: str
    network: str
    status: int
    address: str
    address_tag: str = Field(alias="addressTag")
    tx_id: str = Field(alias="txId")
    insert_time: int = Field(alias="insertTime")
    transfer_type: int = Field(alias="transferType")
    unlock_confirm: str = Field(alias="unlockConfirm")
    """confirm times for unlocking"""

    confirm_times: str = Field(alias="confirmTimes")


class SapiV1CapitalDepositHisrecResponseDict(TypedDict):
    amount: str
    coin: str
    network: str
    status: int
    address: str
    address_tag: str
    tx_id: str
    insert_time: int
    transfer_type: int
    unlock_confirm: str
    confirm_times: str
