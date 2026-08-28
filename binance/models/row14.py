from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row14(SdkBaseModel):
    collateral_account_id: str = Field(alias="collateralAccountId")
    collateral_coin: str = Field(alias="collateralCoin")
    collateral_value: str = Field(alias="collateralValue")
    """locked collateral value shown in USD value"""


class Row14Dict(TypedDict):
    collateral_account_id: str
    collateral_coin: str
    collateral_value: str
