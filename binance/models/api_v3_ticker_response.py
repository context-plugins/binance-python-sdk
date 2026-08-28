from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ApiV3TickerResponse(SdkBaseModel):
    symbol: str
    price_change: str = Field(alias="priceChange")
    price_change_percent: str = Field(alias="priceChangePercent")
    weighted_avg_price: str = Field(alias="weightedAvgPrice")
    open_price: str = Field(alias="openPrice")
    high_price: str = Field(alias="highPrice")
    low_price: str = Field(alias="lowPrice")
    last_price: str = Field(alias="lastPrice")
    volume: str
    quote_volume: str = Field(alias="quoteVolume")
    open_time: int = Field(alias="openTime")
    close_time: int = Field(alias="closeTime")
    first_id: int = Field(alias="firstId")
    last_id: int = Field(alias="lastId")
    count: int


class ApiV3TickerResponseDict(TypedDict):
    symbol: str
    price_change: str
    price_change_percent: str
    weighted_avg_price: str
    open_price: str
    high_price: str
    low_price: str
    last_price: str
    volume: str
    quote_volume: str
    open_time: int
    close_time: int
    first_id: int
    last_id: int
    count: int
