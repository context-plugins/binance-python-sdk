from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SourceType(str, Enum):
    MAIN_SITE = "MAIN_SITE"
    TR = "TR"

    __str__ = str.__str__


SourceTypeOrStr: TypeAlias = Annotated[SourceType | str, open_enum_validator(SourceType)]
