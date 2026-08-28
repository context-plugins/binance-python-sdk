from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FromAccountType(str, Enum):
    SPOT = "SPOT"
    USDT_FUTURE = "USDT_FUTURE"
    COIN_FUTURE = "COIN_FUTURE"
    MARGIN = "MARGIN"
    ISOLATED_MARGIN = "ISOLATED_MARGIN"

    __str__ = str.__str__


FromAccountTypeOrStr: TypeAlias = Annotated[FromAccountType | str, open_enum_validator(FromAccountType)]
