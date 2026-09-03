from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1MarginPriceIndexResponse(SdkBaseModel):
    calc_time: int = Field(alias="calcTime")
    price: str
    symbol: str


class SapiV1MarginPriceIndexResponseDict(TypedDict):
    calc_time: int
    price: str
    symbol: str
