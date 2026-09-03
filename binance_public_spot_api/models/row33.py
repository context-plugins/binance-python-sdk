from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row33(SdkBaseModel):
    time: int
    asset: str
    holding: str
    """BETH holding balance"""

    amount: str
    """Distributed rewards"""

    annual_percentage_rate: str = Field(alias="annualPercentageRate")
    """0.5 means 50% here"""

    status: str


class Row33Dict(TypedDict):
    time: int
    asset: str
    holding: str
    amount: str
    annual_percentage_rate: str
    status: str
