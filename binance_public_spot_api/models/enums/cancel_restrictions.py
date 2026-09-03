from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CancelRestrictions(str, Enum):
    ONLY_NEW = "ONLY_NEW"
    ONLY_PARTIALLY_FILLED = "ONLY_PARTIALLY_FILLED"

    __str__ = str.__str__


CancelRestrictionsOrStr: TypeAlias = Annotated[CancelRestrictions | str, open_enum_validator(CancelRestrictions)]
