from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Btcusdt(SdkBaseModel):
    i: str
    """Unfilled Ratio (UFR)"""

    c: int
    """Count of all orders"""

    v: float
    """Current UFR value"""

    t: float
    """Trigger UFR value"""


class BtcusdtDict(TypedDict):
    i: str
    c: int
    v: float
    t: float
