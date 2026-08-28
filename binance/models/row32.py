from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row32(SdkBaseModel):
    time: int
    arrival_time: int = Field(alias="arrivalTime")
    asset: str
    amount: str
    status: str
    """PENDING, SUCCESS, FAILED"""

    distribute_asset: str = Field(alias="distributeAsset")
    distribute_amount: str = Field(alias="distributeAmount")
    conversion_ratio: str = Field(alias="conversionRatio")


class Row32Dict(TypedDict):
    time: int
    arrival_time: int
    asset: str
    amount: str
    status: str
    distribute_asset: str
    distribute_amount: str
    conversion_ratio: str
