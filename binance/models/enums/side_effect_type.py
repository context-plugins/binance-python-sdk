from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SideEffectType(str, Enum):
    NO_SIDE_EFFECT = "NO_SIDE_EFFECT"
    MARGIN_BUY = "MARGIN_BUY"
    AUTO_REPAY = "AUTO_REPAY"

    __str__ = str.__str__


SideEffectTypeOrStr: TypeAlias = Annotated[SideEffectType | str, open_enum_validator(SideEffectType)]
