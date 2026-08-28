from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ApiV3DepthResponse(SdkBaseModel):
    last_update_id: int = Field(alias="lastUpdateId")
    bids: list[list[str]]
    asks: list[list[str]]


class ApiV3DepthResponseDict(TypedDict):
    last_update_id: int
    bids: list[list[str]]
    asks: list[list[str]]
