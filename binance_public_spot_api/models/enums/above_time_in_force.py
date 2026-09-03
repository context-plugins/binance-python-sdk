from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AboveTimeInForce(str, Enum):
    GTC = "GTC"
    IOC = "IOC"
    FOK = "FOK"

    __str__ = str.__str__


AboveTimeInForceOrStr: TypeAlias = Annotated[AboveTimeInForce | str, open_enum_validator(AboveTimeInForce)]
