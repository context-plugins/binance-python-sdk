from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .assets2 import Assets2, Assets2Dict
from .position1 import Position1, Position1Dict


class Data6(SdkBaseModel):
    assets: list[Assets2]
    position: list[Position1]


class Data6Dict(TypedDict):
    assets: list[Assets2 | Assets2Dict]
    position: list[Position1 | Position1Dict]
