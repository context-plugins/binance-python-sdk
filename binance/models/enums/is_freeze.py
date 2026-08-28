from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IsFreeze(str, Enum):
    TRUE = "true"
    FALSE = "false"

    __str__ = str.__str__


IsFreezeOrStr: TypeAlias = Annotated[IsFreeze | str, open_enum_validator(IsFreeze)]
