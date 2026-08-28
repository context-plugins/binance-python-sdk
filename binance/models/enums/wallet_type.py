from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WalletType(str, Enum):
    SPOT = "SPOT"
    FUNDING = "FUNDING"
    SPOT_FUNDING = "SPOT_FUNDING"

    __str__ = str.__str__


WalletTypeOrStr: TypeAlias = Annotated[WalletType | str, open_enum_validator(WalletType)]
