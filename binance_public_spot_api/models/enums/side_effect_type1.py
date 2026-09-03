from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SideEffectType1(str, Enum):
    NO_SIDE_EFFECT = "NO_SIDE_EFFECT"
    MARGIN_BUY = "MARGIN_BUY"

    __str__ = str.__str__


SideEffectType1OrStr: TypeAlias = Annotated[SideEffectType1 | str, open_enum_validator(SideEffectType1)]
