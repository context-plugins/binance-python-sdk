from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1CapitalDepositSubHisrecResponse(SdkBaseModel):
    amount: str
    coin: str
    network: str
    status: int
    address: str
    address_tag: str = Field(alias="addressTag")
    tx_id: str = Field(alias="txId")
    insert_time: int = Field(alias="insertTime")
    transfer_type: int = Field(alias="transferType")
    confirm_times: str = Field(alias="confirmTimes")


class SapiV1CapitalDepositSubHisrecResponseDict(TypedDict):
    amount: str
    coin: str
    network: str
    status: int
    address: str
    address_tag: str
    tx_id: str
    insert_time: int
    transfer_type: int
    confirm_times: str
