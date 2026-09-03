from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row37(SdkBaseModel):
    time: int
    amount_in_eth: str = Field(alias="amountInETH")
    """Estimated rewards accrued within WBETH"""

    holding: str
    """WBETH holding balance"""

    holding_in_eth: str = Field(alias="holdingInETH")
    annual_percentage_rate: str = Field(alias="annualPercentageRate")


class Row37Dict(TypedDict):
    time: int
    amount_in_eth: str
    holding: str
    holding_in_eth: str
    annual_percentage_rate: str
