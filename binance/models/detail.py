from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Detail(SdkBaseModel):
    asset: str
    asset_full_name: str = Field(alias="assetFullName")
    amount_free: str = Field(alias="amountFree")
    """Convertible amount"""

    to_btc: str = Field(alias="toBTC")
    """BTC amount"""

    to_bnb: str = Field(alias="toBNB")
    """BNB amount(Not deducted commission fee"""

    to_bnb_off_exchange: str = Field(alias="toBNBOffExchange")
    """BNB amount(Deducted commission fee"""

    exchange: str
    """Commission fee"""


class DetailDict(TypedDict):
    asset: str
    asset_full_name: str
    amount_free: str
    to_btc: str
    to_bnb: str
    to_bnb_off_exchange: str
    exchange: str
