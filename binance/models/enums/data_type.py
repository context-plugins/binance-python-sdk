from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DataType(str, Enum):
    T_DEPTH = "T_DEPTH"
    S_DEPTH = "S_DEPTH"

    __str__ = str.__str__


DataTypeOrStr: TypeAlias = Annotated[DataType | str, open_enum_validator(DataType)]
