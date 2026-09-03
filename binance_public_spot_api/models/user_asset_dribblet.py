from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .user_asset_dribblet_detail import UserAssetDribbletDetail, UserAssetDribbletDetailDict


class UserAssetDribblet(SdkBaseModel):
    operate_time: int = Field(alias="operateTime")
    total_transfered_amount: str = Field(alias="totalTransferedAmount")
    """Total transfered BNB amount for this exchange."""

    total_service_charge_amount: str = Field(alias="totalServiceChargeAmount")
    """Total service charge amount for this exchange."""

    trans_id: int = Field(alias="transId")
    user_asset_dribblet_details: list[UserAssetDribbletDetail] = Field(alias="userAssetDribbletDetails")


class UserAssetDribbletDict(TypedDict):
    operate_time: int
    total_transfered_amount: str
    total_service_charge_amount: str
    trans_id: int
    user_asset_dribblet_details: list[UserAssetDribbletDetail | UserAssetDribbletDetailDict]
