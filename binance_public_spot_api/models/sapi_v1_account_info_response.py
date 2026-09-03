from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1AccountInfoResponse(SdkBaseModel):
    vip_level: int = Field(alias="vipLevel")
    is_margin_enabled: bool = Field(alias="isMarginEnabled")
    """true or false for margin."""

    is_future_enabled: bool = Field(alias="isFutureEnabled")
    """true or false for futures."""


class SapiV1AccountInfoResponseDict(TypedDict):
    vip_level: int
    is_margin_enabled: bool
    is_future_enabled: bool
