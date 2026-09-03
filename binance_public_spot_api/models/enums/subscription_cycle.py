from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SubscriptionCycle(str, Enum):
    H1 = "H1"
    H4 = "H4"
    H8 = "H8"
    H12 = "H12"
    WEEKLY = "WEEKLY"
    DAILY = "DAILY"
    MONTHLY = "MONTHLY"
    BI_WEEKLY = "BI_WEEKLY"

    __str__ = str.__str__


SubscriptionCycleOrStr: TypeAlias = Annotated[SubscriptionCycle | str, open_enum_validator(SubscriptionCycle)]
