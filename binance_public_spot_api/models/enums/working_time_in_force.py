from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WorkingTimeInForce(str, Enum):
    GTC = "GTC"
    IOC = "IOC"
    FOK = "FOK"

    __str__ = str.__str__


WorkingTimeInForceOrStr: TypeAlias = Annotated[WorkingTimeInForce | str, open_enum_validator(WorkingTimeInForce)]
