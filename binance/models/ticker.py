from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Ticker(SdkBaseModel):
    symbol: str
    price_change: str = Field(alias="priceChange")
    price_change_percent: str = Field(alias="priceChangePercent")
    prev_close_price: str = Field(alias="prevClosePrice")
    last_price: str = Field(alias="lastPrice")
    bid_price: str = Field(alias="bidPrice")
    bid_qty: str = Field(alias="bidQty")
    ask_price: str = Field(alias="askPrice")
    ask_qty: str = Field(alias="askQty")
    open_price: str = Field(alias="openPrice")
    high_price: str = Field(alias="highPrice")
    low_price: str = Field(alias="lowPrice")
    volume: str
    quote_volume: str = Field(alias="quoteVolume")
    open_time: int = Field(alias="openTime")
    close_time: int = Field(alias="closeTime")
    first_id: int = Field(alias="firstId")
    last_id: int = Field(alias="lastId")
    count: int


class TickerDict(TypedDict):
    symbol: str
    price_change: str
    price_change_percent: str
    prev_close_price: str
    last_price: str
    bid_price: str
    bid_qty: str
    ask_price: str
    ask_qty: str
    open_price: str
    high_price: str
    low_price: str
    volume: str
    quote_volume: str
    open_time: int
    close_time: int
    first_id: int
    last_id: int
    count: int
