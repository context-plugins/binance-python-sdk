from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SapiV1MarginDelistScheduleResponse(SdkBaseModel):
    delist_time: Optional[int] = Field(default=UNSET, alias="delistTime")
    cross_margin_assets: Optional[list[str]] = Field(default=UNSET, alias="crossMarginAssets")
    isolated_margin_symbols: Optional[list[str]] = Field(default=UNSET, alias="isolatedMarginSymbols")


class SapiV1MarginDelistScheduleResponseDict(TypedDict):
    delist_time: NotRequired[int]
    cross_margin_assets: NotRequired[list[str]]
    isolated_margin_symbols: NotRequired[list[str]]
