from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PositionSide(str, Enum):
    BOTH = "BOTH"
    LONG = "LONG"
    SHORT = "SHORT"

    __str__ = str.__str__


PositionSideOrStr: TypeAlias = Annotated[PositionSide | str, open_enum_validator(PositionSide)]
