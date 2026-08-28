from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TradeType(str, Enum):
    BUY = "BUY"
    SELL = "SELL"

    __str__ = str.__str__


TradeTypeOrStr: TypeAlias = Annotated[TradeType | str, open_enum_validator(TradeType)]
