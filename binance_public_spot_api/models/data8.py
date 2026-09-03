from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Data8(SdkBaseModel):
    order_no: str = Field(alias="orderNo")
    source_amount: str = Field(alias="sourceAmount")
    """Fiat trade amount"""

    fiat_currency: str = Field(alias="fiatCurrency")
    """Fiat token"""

    obtain_amount: str = Field(alias="obtainAmount")
    """Crypto trade amount"""

    crypto_currency: str = Field(alias="cryptoCurrency")
    """Crypto token"""

    total_fee: str = Field(alias="totalFee")
    """Trade fee"""

    price: str
    status: str
    """Processing, Completed, Failed, Refunded"""

    create_time: int = Field(alias="createTime")
    update_time: int = Field(alias="updateTime")


class Data8Dict(TypedDict):
    order_no: str
    source_amount: str
    fiat_currency: str
    obtain_amount: str
    crypto_currency: str
    total_fee: str
    price: str
    status: str
    create_time: int
    update_time: int
