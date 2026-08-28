from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .order15 import Order15, Order15Dict


class SapiV1AlgoFuturesHistoricalOrdersResponse(SdkBaseModel):
    total: int
    orders: list[Order15]


class SapiV1AlgoFuturesHistoricalOrdersResponseDict(TypedDict):
    total: int
    orders: list[Order15 | Order15Dict]
