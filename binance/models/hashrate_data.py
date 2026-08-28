from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class HashrateData(SdkBaseModel):
    time: int
    hashrate: str
    reject: int
    """Rejection Rate"""


class HashrateDataDict(TypedDict):
    time: int
    hashrate: str
    reject: int
