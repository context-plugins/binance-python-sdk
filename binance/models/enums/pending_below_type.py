from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PendingBelowType(str, Enum):
    LIMIT_MAKER = "LIMIT_MAKER"
    STOP_LOSS = "STOP_LOSS"
    STOP_LOSS_LIMIT = "STOP_LOSS_LIMIT"

    __str__ = str.__str__


PendingBelowTypeOrStr: TypeAlias = Annotated[PendingBelowType | str, open_enum_validator(PendingBelowType)]
