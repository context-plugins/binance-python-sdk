from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Filter(SdkBaseModel):
    filter_type: str = Field(alias="filterType")
    min_price: str = Field(alias="minPrice")
    max_price: str = Field(alias="maxPrice")
    tick_size: str = Field(alias="tickSize")


class FilterDict(TypedDict):
    filter_type: str
    min_price: str
    max_price: str
    tick_size: str
