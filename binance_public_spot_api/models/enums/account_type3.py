from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AccountType3(str, Enum):
    MAIN = "MAIN"
    CARD = "CARD"

    __str__ = str.__str__


AccountType3OrStr: TypeAlias = Annotated[AccountType3 | str, open_enum_validator(AccountType3)]
