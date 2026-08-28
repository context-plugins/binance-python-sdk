from __future__ import annotations

from typing import TypeAlias

from ..margin_order_response_ack import MarginOrderResponseAck, MarginOrderResponseAckDict
from ..margin_order_response_full import MarginOrderResponseFull, MarginOrderResponseFullDict
from ..margin_order_response_result import MarginOrderResponseResult, MarginOrderResponseResultDict

SapiV1MarginOrderResponse: TypeAlias = MarginOrderResponseAck | MarginOrderResponseResult | MarginOrderResponseFull

SapiV1MarginOrderResponseDict: TypeAlias = (
    MarginOrderResponseAckDict | MarginOrderResponseResultDict | MarginOrderResponseFullDict
)
