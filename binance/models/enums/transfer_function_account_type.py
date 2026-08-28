from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransferFunctionAccountType(str, Enum):
    SPOT = "SPOT"
    MARGIN = "MARGIN"
    ISOLATED_MARGIN = "ISOLATED_MARGIN"
    USDT_FUTURE = "USDT_FUTURE"
    COIN_FUTURE = "COIN_FUTURE"

    __str__ = str.__str__


TransferFunctionAccountTypeOrStr: TypeAlias = Annotated[
    TransferFunctionAccountType | str, open_enum_validator(TransferFunctionAccountType)
]
