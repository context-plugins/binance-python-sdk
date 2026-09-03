from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Side(str, Enum):
    SELL = "SELL"
    BUY = "BUY"

    __str__ = str.__str__


SideOrStr: TypeAlias = Annotated[Side | str, open_enum_validator(Side)]
