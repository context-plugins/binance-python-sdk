from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status2(str, Enum):
    PENDING = "PENDING"
    PURCHASE_SUCCESS = "PURCHASE_SUCCESS"
    SETTLED = "SETTLED"
    PURCHASE_FAIL = "PURCHASE_FAIL"
    REFUNDING = "REFUNDING"
    REFUND_SUCCESS = "REFUND_SUCCESS"
    SETTLING = "SETTLING"

    __str__ = str.__str__


Status2OrStr: TypeAlias = Annotated[Status2 | str, open_enum_validator(Status2)]
