from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ExpiredType(str, Enum):
    _1_D = "1_D"
    _3_D = "3_D"
    _7_D = "7_D"
    _30_D = "30_D"

    __str__ = str.__str__


ExpiredTypeOrStr: TypeAlias = Annotated[ExpiredType | str, open_enum_validator(ExpiredType)]
