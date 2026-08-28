from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ToAccountType(str, Enum):
    SPOT = "SPOT"
    USDT_FUTURE = "USDT_FUTURE"
    COIN_FUTURE = "COIN_FUTURE"
    MARGIN = "MARGIN"
    ISOLATED_MARGIN = "ISOLATED_MARGIN"

    __str__ = str.__str__


ToAccountTypeOrStr: TypeAlias = Annotated[ToAccountType | str, open_enum_validator(ToAccountType)]
