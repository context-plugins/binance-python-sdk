from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1MarginIsolatedAccountLimitResponse(SdkBaseModel):
    enabled_account: int = Field(alias="enabledAccount")
    max_account: int = Field(alias="maxAccount")


class SapiV1MarginIsolatedAccountLimitResponseDict(TypedDict):
    enabled_account: int
    max_account: int
