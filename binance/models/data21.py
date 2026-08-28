from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Data21(SdkBaseModel):
    order_number: str = Field(alias="orderNumber")
    adv_no: str = Field(alias="advNo")
    trade_type: str = Field(alias="tradeType")
    asset: str
    fiat: str
    fiat_symbol: str = Field(alias="fiatSymbol")
    amount: str
    """Quantity (in Crypto)"""

    total_price: str = Field(alias="totalPrice")
    unit_price: str = Field(alias="unitPrice")
    """Unit Price (in Fiat)"""

    order_status: str = Field(alias="orderStatus")
    """PENDING, TRADING, BUYER_PAYED, DISTRIBUTING, COMPLETED, IN_APPEAL, CANCELLED, CANCELLED_BY_SYSTEM"""

    create_time: int = Field(alias="createTime")
    commission: str
    """Transaction Fee (in Crypto)"""

    counter_part_nick_name: str = Field(alias="counterPartNickName")
    advertisement_role: str = Field(alias="advertisementRole")


class Data21Dict(TypedDict):
    order_number: str
    adv_no: str
    trade_type: str
    asset: str
    fiat: str
    fiat_symbol: str
    amount: str
    total_price: str
    unit_price: str
    order_status: str
    create_time: int
    commission: str
    counter_part_nick_name: str
    advertisement_role: str
