from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1SpotDelistScheduleResponse(SdkBaseModel):
    delist_time: int = Field(alias="delistTime")
    symbol: list[str]


class SapiV1SpotDelistScheduleResponseDict(TypedDict):
    delist_time: int
    symbol: list[str]
