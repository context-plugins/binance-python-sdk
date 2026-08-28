from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PlanType1(str, Enum):
    SINGLE = "SINGLE"
    PORTFOLIO = "PORTFOLIO"
    INDEX = "INDEX"
    ALL = "ALL"

    __str__ = str.__str__


PlanType1OrStr: TypeAlias = Annotated[PlanType1 | str, open_enum_validator(PlanType1)]
