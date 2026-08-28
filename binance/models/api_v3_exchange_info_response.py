from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .rate_limit import RateLimit, RateLimitDict
from .symbol import Symbol, SymbolDict


class ApiV3ExchangeInfoResponse(SdkBaseModel):
    timezone: str
    server_time: int = Field(alias="serverTime")
    rate_limits: list[RateLimit] = Field(alias="rateLimits")
    exchange_filters: list[Any] = Field(alias="exchangeFilters")
    symbols: list[Symbol]


class ApiV3ExchangeInfoResponseDict(TypedDict):
    timezone: str
    server_time: int
    rate_limits: list[RateLimit | RateLimitDict]
    exchange_filters: list[Any]
    symbols: list[Symbol | SymbolDict]
