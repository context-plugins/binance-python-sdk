from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SortBy(str, Enum):
    START_TIME = "START_TIME"
    LOT_SIZE = "LOT_SIZE"
    INTEREST_RATE = "INTEREST_RATE"
    DURATION = "DURATION"

    __str__ = str.__str__


SortByOrStr: TypeAlias = Annotated[SortBy | str, open_enum_validator(SortBy)]
