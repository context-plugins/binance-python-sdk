from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Data20(SdkBaseModel):
    day: str
    url: str


class Data20Dict(TypedDict):
    day: str
    url: str
