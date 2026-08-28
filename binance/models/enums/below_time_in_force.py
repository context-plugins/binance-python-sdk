from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BelowTimeInForce(str, Enum):
    GTC = "GTC"
    IOC = "IOC"
    FOK = "FOK"

    __str__ = str.__str__


BelowTimeInForceOrStr: TypeAlias = Annotated[BelowTimeInForce | str, open_enum_validator(BelowTimeInForce)]
