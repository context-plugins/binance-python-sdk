from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IsIsolated(str, Enum):
    TRUE = "TRUE"
    FALSE = "FALSE"

    __str__ = str.__str__


IsIsolatedOrStr: TypeAlias = Annotated[IsIsolated | str, open_enum_validator(IsIsolated)]
