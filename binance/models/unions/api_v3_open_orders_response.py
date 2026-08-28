from __future__ import annotations

from typing import TypeAlias

from ..oco_order import OcoOrder, OcoOrderDict
from ..order import Order, OrderDict

ApiV3OpenOrdersResponse: TypeAlias = Order | OcoOrder

ApiV3OpenOrdersResponseDict: TypeAlias = OrderDict | OcoOrderDict
