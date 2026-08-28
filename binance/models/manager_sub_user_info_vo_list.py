from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ManagerSubUserInfoVoList(SdkBaseModel):
    root_user_id: int = Field(alias="rootUserId")
    managersub_user_id: int = Field(alias="managersubUserId")
    bind_parent_user_id: int = Field(alias="bindParentUserId")
    email: Optional[str] = UNSET
    insert_time_stamp: int = Field(alias="insertTimeStamp")
    bind_parent_email: str = Field(alias="bindParentEmail")
    is_sub_user_enabled: bool = Field(alias="isSubUserEnabled")
    is_user_active: bool = Field(alias="isUserActive")
    is_margin_enabled: bool = Field(alias="isMarginEnabled")
    is_future_enabled: bool = Field(alias="isFutureEnabled")
    is_signed_lvt_risk_agreement: bool = Field(alias="isSignedLVTRiskAgreement")


class ManagerSubUserInfoVoListDict(TypedDict):
    root_user_id: int
    managersub_user_id: int
    bind_parent_user_id: int
    email: NotRequired[str]
    insert_time_stamp: int
    bind_parent_email: str
    is_sub_user_enabled: bool
    is_user_active: bool
    is_margin_enabled: bool
    is_future_enabled: bool
    is_signed_lvt_risk_agreement: bool
