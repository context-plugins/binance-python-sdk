from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PendingTimeInForce(str, Enum):
    GTC = "GTC"
    IOC = "IOC"
    FOK = "FOK"

    __str__ = str.__str__


PendingTimeInForceOrStr: TypeAlias = Annotated[PendingTimeInForce | str, open_enum_validator(PendingTimeInForce)]
