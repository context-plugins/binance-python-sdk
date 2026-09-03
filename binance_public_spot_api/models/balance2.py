from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Balance2(SdkBaseModel):
    asset: str
    free: int
    locked: int


class Balance2Dict(TypedDict):
    asset: str
    free: int
    locked: int
