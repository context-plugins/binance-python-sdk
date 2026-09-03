from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PlanType(str, Enum):
    SINGLE = "SINGLE"
    PORTFOLIO = "PORTFOLIO"
    INDEX = "INDEX"

    __str__ = str.__str__


PlanTypeOrStr: TypeAlias = Annotated[PlanType | str, open_enum_validator(PlanType)]
