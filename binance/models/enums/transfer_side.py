from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransferSide(str, Enum):
    TO_UM = "TO_UM"
    FROM_UM = "FROM_UM"

    __str__ = str.__str__


TransferSideOrStr: TypeAlias = Annotated[TransferSide | str, open_enum_validator(TransferSide)]
