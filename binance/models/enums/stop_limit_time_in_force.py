from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StopLimitTimeInForce(str, Enum):
    GTC = "GTC"
    FOK = "FOK"
    IOC = "IOC"

    __str__ = str.__str__


StopLimitTimeInForceOrStr: TypeAlias = Annotated[StopLimitTimeInForce | str, open_enum_validator(StopLimitTimeInForce)]
