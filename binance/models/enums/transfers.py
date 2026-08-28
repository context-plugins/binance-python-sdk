from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Transfers(str, Enum):
    FROM = "FROM"
    TO = "TO"

    __str__ = str.__str__


TransfersOrStr: TypeAlias = Annotated[Transfers | str, open_enum_validator(Transfers)]
