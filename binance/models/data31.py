from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Data31(SdkBaseModel):
    symbol: str
    base_asset: str = Field(alias="baseAsset")
    quote_asset: str = Field(alias="quoteAsset")


class Data31Dict(TypedDict):
    symbol: str
    base_asset: str
    quote_asset: str
