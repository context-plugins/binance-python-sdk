from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .manager_sub_user_info_vo_list import ManagerSubUserInfoVoList, ManagerSubUserInfoVoListDict


class SapiV1ManagedSubaccountInfoResponse(SdkBaseModel):
    total: int
    manager_sub_user_info_vo_list: list[ManagerSubUserInfoVoList] = Field(alias="managerSubUserInfoVoList")


class SapiV1ManagedSubaccountInfoResponseDict(TypedDict):
    total: int
    manager_sub_user_info_vo_list: list[ManagerSubUserInfoVoList | ManagerSubUserInfoVoListDict]
