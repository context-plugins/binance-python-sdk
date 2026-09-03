from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ApiV3TimeResponse(SdkBaseModel):
    server_time: int = Field(alias="serverTime")


class ApiV3TimeResponseDict(TypedDict):
    server_time: int
