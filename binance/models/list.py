from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class List(SdkBaseModel):
    time: int
    hashrate: str
    reject: str


class ListDict(TypedDict):
    time: int
    hashrate: str
    reject: str
