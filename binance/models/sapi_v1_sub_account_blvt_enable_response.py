from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1SubAccountBlvtEnableResponse(SdkBaseModel):
    email: str
    enable_blvt: bool = Field(alias="enableBlvt")


class SapiV1SubAccountBlvtEnableResponseDict(TypedDict):
    email: str
    enable_blvt: bool
