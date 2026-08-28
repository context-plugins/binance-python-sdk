from __future__ import annotations

from typing import TypeAlias

from ..canceled_margin_order_detail import CanceledMarginOrderDetail, CanceledMarginOrderDetailDict
from ..margin_oco_order import MarginOcoOrder, MarginOcoOrderDict

SapiV1MarginOpenOrdersResponse: TypeAlias = CanceledMarginOrderDetail | MarginOcoOrder

SapiV1MarginOpenOrdersResponseDict: TypeAlias = CanceledMarginOrderDetailDict | MarginOcoOrderDict
