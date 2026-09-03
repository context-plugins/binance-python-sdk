from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Quota(SdkBaseModel):
    total_personal_quota: str = Field(alias="totalPersonalQuota")
    minimum: str


class QuotaDict(TypedDict):
    total_personal_quota: str
    minimum: str
