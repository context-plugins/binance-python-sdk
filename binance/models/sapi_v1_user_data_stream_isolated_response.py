from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1UserDataStreamIsolatedResponse(SdkBaseModel):
    listen_key: str = Field(alias="listenKey")


class SapiV1UserDataStreamIsolatedResponseDict(TypedDict):
    listen_key: str
