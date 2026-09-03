from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ApiV3UserDataStreamResponse(SdkBaseModel):
    listen_key: str = Field(alias="listenKey")


class ApiV3UserDataStreamResponseDict(TypedDict):
    listen_key: str
