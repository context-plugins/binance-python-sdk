from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InterestBnbburn(str, Enum):
    TRUE = "true"
    FALSE = "false"

    __str__ = str.__str__


InterestBnbburnOrStr: TypeAlias = Annotated[InterestBnbburn | str, open_enum_validator(InterestBnbburn)]
