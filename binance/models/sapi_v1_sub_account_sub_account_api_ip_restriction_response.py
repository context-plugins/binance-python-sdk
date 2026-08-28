from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1SubAccountSubAccountApiIpRestrictionResponse(SdkBaseModel):
    ip_restrict: str = Field(alias="ipRestrict")
    ip_list: list[str] = Field(alias="ipList")
    update_time: int = Field(alias="updateTime")
    api_key: str = Field(alias="apiKey")


class SapiV1SubAccountSubAccountApiIpRestrictionResponseDict(TypedDict):
    ip_restrict: str
    ip_list: list[str]
    update_time: int
    api_key: str
