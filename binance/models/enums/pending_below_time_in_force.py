from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PendingBelowTimeInForce(str, Enum):
    GTC = "GTC"
    IOC = "IOC"
    FOK = "FOK"

    __str__ = str.__str__


PendingBelowTimeInForceOrStr: TypeAlias = Annotated[
    PendingBelowTimeInForce | str, open_enum_validator(PendingBelowTimeInForce)
]
