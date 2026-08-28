from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ApiV3MyAllocationsResponse(SdkBaseModel):
    symbol: str
    allocation_id: int = Field(alias="allocationId")
    allocation_type: str = Field(alias="allocationType")
    order_id: int = Field(alias="orderId")
    order_list_id: int = Field(alias="orderListId")
    price: str
    qty: str
    quote_qty: str = Field(alias="quoteQty")
    commission: str
    commission_asset: str = Field(alias="commissionAsset")
    time: int
    is_buyer: bool = Field(alias="isBuyer")
    is_maker: bool = Field(alias="isMaker")
    is_allocator: bool = Field(alias="isAllocator")


class ApiV3MyAllocationsResponseDict(TypedDict):
    symbol: str
    allocation_id: int
    allocation_type: str
    order_id: int
    order_list_id: int
    price: str
    qty: str
    quote_qty: str
    commission: str
    commission_asset: str
    time: int
    is_buyer: bool
    is_maker: bool
    is_allocator: bool
