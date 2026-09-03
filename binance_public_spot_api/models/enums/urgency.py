from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Urgency(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

    __str__ = str.__str__


UrgencyOrStr: TypeAlias = Annotated[Urgency | str, open_enum_validator(Urgency)]
