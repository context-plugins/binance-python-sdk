from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row31(SdkBaseModel):
    time: int
    asset: str
    amount: str
    status: str
    """PENDING, SUCCESS, FAILED"""

    distribute_amount: str = Field(alias="distributeAmount")
    conversion_ratio: str = Field(alias="conversionRatio")


class Row31Dict(TypedDict):
    time: int
    asset: str
    amount: str
    status: str
    distribute_amount: str
    conversion_ratio: str
