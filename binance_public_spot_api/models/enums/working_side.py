from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WorkingSide(str, Enum):
    BUY = "BUY"
    SELL = "SELL"

    __str__ = str.__str__


WorkingSideOrStr: TypeAlias = Annotated[WorkingSide | str, open_enum_validator(WorkingSide)]
