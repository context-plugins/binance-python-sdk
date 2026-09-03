from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .btcusdt import Btcusdt, BtcusdtDict


class Indicators(SdkBaseModel):
    """The indicators updated every 30 seconds"""

    btcusdt: list[Btcusdt] = Field(alias="BTCUSDT")


class IndicatorsDict(TypedDict):
    btcusdt: list[Btcusdt | BtcusdtDict]
