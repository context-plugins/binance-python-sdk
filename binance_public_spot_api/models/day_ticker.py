from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DayTicker(SdkBaseModel):
    symbol: str
    price_change: str = Field(alias="priceChange")
    """Absolute price change"""

    price_change_percent: str = Field(alias="priceChangePercent")
    """Relative price change in percent"""

    weighted_avg_price: str = Field(alias="weightedAvgPrice")
    """quoteVolume / volume"""

    open_price: str = Field(alias="openPrice")
    high_price: str = Field(alias="highPrice")
    low_price: str = Field(alias="lowPrice")
    last_price: str = Field(alias="lastPrice")
    volume: str
    """Volume in base asset"""

    quote_volume: str = Field(alias="quoteVolume")
    """Volume in quote asset"""

    open_time: int = Field(alias="openTime")
    close_time: int = Field(alias="closeTime")
    first_id: int = Field(alias="firstId")
    """Trade ID of the first trade in the interval"""

    last_id: int = Field(alias="lastId")
    """Trade ID of the last trade in the interval"""

    count: int
    """Number of trades in the interval"""


class DayTickerDict(TypedDict):
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
