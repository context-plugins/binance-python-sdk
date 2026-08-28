from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OptionType(str, Enum):
    CALL = "CALL"
    PUT = "PUT"

    __str__ = str.__str__


OptionTypeOrStr: TypeAlias = Annotated[OptionType | str, open_enum_validator(OptionType)]
