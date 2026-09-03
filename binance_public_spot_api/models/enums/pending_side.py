from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PendingSide(str, Enum):
    BUY = "BUY"
    SELL = "SELL"

    __str__ = str.__str__


PendingSideOrStr: TypeAlias = Annotated[PendingSide | str, open_enum_validator(PendingSide)]
