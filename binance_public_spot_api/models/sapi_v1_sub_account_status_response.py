from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1SubAccountStatusResponse(SdkBaseModel):
    email: str
    is_sub_user_enabled: bool = Field(alias="isSubUserEnabled")
    is_user_active: bool = Field(alias="isUserActive")
    insert_time: int = Field(alias="insertTime")
    """sub account create time"""

    is_margin_enabled: bool = Field(alias="isMarginEnabled")
    is_future_enabled: bool = Field(alias="isFutureEnabled")
    mobile: int
    """user mobile number"""


class SapiV1SubAccountStatusResponseDict(TypedDict):
    email: str
    is_sub_user_enabled: bool
    is_user_active: bool
    insert_time: int
    is_margin_enabled: bool
    is_future_enabled: bool
    mobile: int
