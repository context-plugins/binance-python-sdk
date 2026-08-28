from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AutoCompoundPlan(str, Enum):
    NONE = "NONE"
    STANDARD = "STANDARD"
    ADVANCE = "ADVANCE"

    __str__ = str.__str__


AutoCompoundPlanOrStr: TypeAlias = Annotated[AutoCompoundPlan | str, open_enum_validator(AutoCompoundPlan)]
