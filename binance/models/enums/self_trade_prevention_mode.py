from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SelfTradePreventionMode(str, Enum):
    EXPIRE_TAKER = "EXPIRE_TAKER"
    EXPIRE_MAKER = "EXPIRE_MAKER"
    EXPIRE_BOTH = "EXPIRE_BOTH"
    NONE = "NONE"

    __str__ = str.__str__


SelfTradePreventionModeOrStr: TypeAlias = Annotated[
    SelfTradePreventionMode | str, open_enum_validator(SelfTradePreventionMode)
]
