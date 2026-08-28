from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SubscriptionStartWeekday(str, Enum):
    MON = "MON"
    TUE = "TUE"
    WED = "WED"
    THU = "THU"
    FRI = "FRI"
    SAT = "SAT"
    SUN = "SUN"

    __str__ = str.__str__


SubscriptionStartWeekdayOrStr: TypeAlias = Annotated[
    SubscriptionStartWeekday | str, open_enum_validator(SubscriptionStartWeekday)
]
