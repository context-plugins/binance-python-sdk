from __future__ import annotations

from typing import TypeAlias

from ..order_response_ack import OrderResponseAck, OrderResponseAckDict
from ..order_response_full import OrderResponseFull, OrderResponseFullDict
from ..order_response_result import OrderResponseResult, OrderResponseResultDict

ApiV3OrderResponse: TypeAlias = OrderResponseAck | OrderResponseResult | OrderResponseFull

ApiV3OrderResponseDict: TypeAlias = OrderResponseAckDict | OrderResponseResultDict | OrderResponseFullDict
