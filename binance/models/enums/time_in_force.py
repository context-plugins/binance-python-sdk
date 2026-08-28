from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TimeInForce(str, Enum):
    GTC = "GTC"
    IOC = "IOC"
    FOK = "FOK"

    __str__ = str.__str__


TimeInForceOrStr: TypeAlias = Annotated[TimeInForce | str, open_enum_validator(TimeInForce)]
