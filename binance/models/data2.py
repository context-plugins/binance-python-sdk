from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .asset1 import Asset1, Asset1Dict
from .position import Position, PositionDict


class Data2(SdkBaseModel):
    assets: list[Asset1]
    position: list[Position]


class Data2Dict(TypedDict):
    assets: list[Asset1 | Asset1Dict]
    position: list[Position | PositionDict]
