from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row48(SdkBaseModel):
    product_id: str = Field(alias="productId")
    asset: str
    annual_percentage_rate: str = Field(alias="annualPercentageRate")
    time: int


class Row48Dict(TypedDict):
    product_id: str
    asset: str
    annual_percentage_rate: str
    time: int
