from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .order15 import Order15, Order15Dict


class SapiV1AlgoFuturesOpenOrdersResponse(SdkBaseModel):
    total: int
    orders: Optional[list[Order15]] = UNSET


class SapiV1AlgoFuturesOpenOrdersResponseDict(TypedDict):
    total: int
    orders: NotRequired[list[Order15 | Order15Dict]]
