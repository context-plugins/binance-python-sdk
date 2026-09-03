from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row34(SdkBaseModel):
    annual_percentage_rate: str = Field(alias="annualPercentageRate")
    """BETH APR"""

    exchange_rate: str = Field(alias="exchangeRate")
    """BETH value per 1 WBETH"""

    time: int


class Row34Dict(TypedDict):
    annual_percentage_rate: str
    exchange_rate: str
    time: int
