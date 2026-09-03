from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IsFlexibleRate(str, Enum):
    TRUE = "TRUE"
    FALSE = "FALSE"

    __str__ = str.__str__


IsFlexibleRateOrStr: TypeAlias = Annotated[IsFlexibleRate | str, open_enum_validator(IsFlexibleRate)]
