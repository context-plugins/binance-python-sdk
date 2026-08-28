from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Interval(str, Enum):
    _1S = "1s"
    _1M = "1m"
    _3M = "3m"
    _5M = "5m"
    _15M = "15m"
    _30M = "30m"
    _1H = "1h"
    _2H = "2h"
    _4H = "4h"
    _6H = "6h"
    _8H = "8h"
    _12H = "12h"
    _1D = "1d"
    _3D = "3d"
    _1W = "1w"
    _1_M = "1M"

    __str__ = str.__str__


IntervalOrStr: TypeAlias = Annotated[Interval | str, open_enum_validator(Interval)]
