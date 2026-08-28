from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class NewOrderRespType(str, Enum):
    ACK = "ACK"
    RESULT = "RESULT"
    FULL = "FULL"

    __str__ = str.__str__


NewOrderRespTypeOrStr: TypeAlias = Annotated[NewOrderRespType | str, open_enum_validator(NewOrderRespType)]
