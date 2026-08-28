from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .order17 import Order17, Order17Dict


class SapiV1AlgoSpotHistoricalOrdersResponse(SdkBaseModel):
    total: int
    orders: list[Order17]


class SapiV1AlgoSpotHistoricalOrdersResponseDict(TypedDict):
    total: int
    orders: list[Order17 | Order17Dict]
