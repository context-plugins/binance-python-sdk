from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Balance(SdkBaseModel):
    asset: str
    free: str
    locked: str


class BalanceDict(TypedDict):
    asset: str
    free: str
    locked: str
