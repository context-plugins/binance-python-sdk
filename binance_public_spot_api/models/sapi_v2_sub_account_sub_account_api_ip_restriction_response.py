from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV2SubAccountSubAccountApiIpRestrictionResponse(SdkBaseModel):
    status: str
    ip_list: list[str] = Field(alias="ipList")
    update_time: int = Field(alias="updateTime")
    api_key: str = Field(alias="apiKey")


class SapiV2SubAccountSubAccountApiIpRestrictionResponseDict(TypedDict):
    status: str
    ip_list: list[str]
    update_time: int
    api_key: str
