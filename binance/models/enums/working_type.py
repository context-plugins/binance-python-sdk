from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WorkingType(str, Enum):
    LIMIT = "LIMIT"
    LIMIT_MAKER = "LIMIT_MAKER"

    __str__ = str.__str__


WorkingTypeOrStr: TypeAlias = Annotated[WorkingType | str, open_enum_validator(WorkingType)]
