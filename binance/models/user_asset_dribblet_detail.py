from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UserAssetDribbletDetail(SdkBaseModel):
    trans_id: int = Field(alias="transId")
    service_charge_amount: str = Field(alias="serviceChargeAmount")
    amount: str
    operate_time: int = Field(alias="operateTime")
    transfered_amount: str = Field(alias="transferedAmount")
    from_asset: str = Field(alias="fromAsset")


class UserAssetDribbletDetailDict(TypedDict):
    trans_id: int
    service_charge_amount: str
    amount: str
    operate_time: int
    transfered_amount: str
    from_asset: str
