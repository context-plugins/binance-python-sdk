from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class NeedBtcValuation(str, Enum):
    TRUE = "true"
    FALSE = "false"

    __str__ = str.__str__


NeedBtcValuationOrStr: TypeAlias = Annotated[NeedBtcValuation | str, open_enum_validator(NeedBtcValuation)]
