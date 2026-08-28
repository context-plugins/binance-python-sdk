from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type9(str, Enum):
    BORROW_IN = "borrowIn"
    COLLATERAL_SPENT = "collateralSpent"
    REPAY_AMOUNT = "repayAmount"
    COLLATERAL_RETURN = "collateralReturn"
    ADD_COLLATERAL = "addCollateral"
    REMOVE_COLLATERAL = "removeCollateral"
    COLLATERAL_RETURN_AFTER_LIQUIDATION = "collateralReturnAfterLiquidation"

    __str__ = str.__str__


Type9OrStr: TypeAlias = Annotated[Type9 | str, open_enum_validator(Type9)]
