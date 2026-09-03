from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RedeemTo(str, Enum):
    SPOT = "SPOT"
    FLEXIBLE = "FLEXIBLE"

    __str__ = str.__str__


RedeemToOrStr: TypeAlias = Annotated[RedeemTo | str, open_enum_validator(RedeemTo)]
