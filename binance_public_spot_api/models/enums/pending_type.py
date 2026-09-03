from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PendingType(str, Enum):
    LIMIT = "LIMIT"
    MARKET = "MARKET"
    STOP_LOSS = "STOP_LOSS"
    STOP_LOSS_LIMIT = "STOP_LOSS_LIMIT"
    TAKE_PROFIT = "TAKE_PROFIT"
    TAKE_PROFIT_LIMIT = "TAKE_PROFIT_LIMIT"
    LIMIT_MAKER = "LIMIT_MAKER"

    __str__ = str.__str__


PendingTypeOrStr: TypeAlias = Annotated[PendingType | str, open_enum_validator(PendingType)]
