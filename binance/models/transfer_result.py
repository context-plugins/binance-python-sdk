from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TransferResult(SdkBaseModel):
    amount: str
    from_asset: str = Field(alias="fromAsset")
    operate_time: int = Field(alias="operateTime")
    service_charge_amount: str = Field(alias="serviceChargeAmount")
    tran_id: int = Field(alias="tranId")
    transfered_amount: str = Field(alias="transferedAmount")


class TransferResultDict(TypedDict):
    amount: str
    from_asset: str
    operate_time: int
    service_charge_amount: str
    tran_id: int
    transfered_amount: str
