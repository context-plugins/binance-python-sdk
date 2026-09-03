from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1SubAccountMarginEnableResponse(SdkBaseModel):
    email: str
    is_margin_enabled: bool = Field(alias="isMarginEnabled")


class SapiV1SubAccountMarginEnableResponseDict(TypedDict):
    email: str
    is_margin_enabled: bool
