from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .cancel_response import CancelResponse, CancelResponseDict
from .new_order_response import NewOrderResponse, NewOrderResponseDict


class ApiV3OrderCancelReplaceResponse(SdkBaseModel):
    cancel_result: str = Field(alias="cancelResult")
    new_order_result: str = Field(alias="newOrderResult")
    cancel_response: CancelResponse = Field(alias="cancelResponse")
    new_order_response: NewOrderResponse = Field(alias="newOrderResponse")


class ApiV3OrderCancelReplaceResponseDict(TypedDict):
    cancel_result: str
    new_order_result: str
    cancel_response: CancelResponse | CancelResponseDict
    new_order_response: NewOrderResponse | NewOrderResponseDict
