from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SubAccount(SdkBaseModel):
    email: str
    is_freeze: bool = Field(alias="isFreeze")
    create_time: int = Field(alias="createTime")
    is_managed_sub_account: bool = Field(alias="isManagedSubAccount")
    is_asset_management_sub_account: bool = Field(alias="isAssetManagementSubAccount")


class SubAccountDict(TypedDict):
    email: str
    is_freeze: bool
    create_time: int
    is_managed_sub_account: bool
    is_asset_management_sub_account: bool
