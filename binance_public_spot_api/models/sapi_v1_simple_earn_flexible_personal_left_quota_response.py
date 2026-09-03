from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1SimpleEarnFlexiblePersonalLeftQuotaResponse(SdkBaseModel):
    left_personal_quota: str = Field(alias="leftPersonalQuota")


class SapiV1SimpleEarnFlexiblePersonalLeftQuotaResponseDict(TypedDict):
    left_personal_quota: str
