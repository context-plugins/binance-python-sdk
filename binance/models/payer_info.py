from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PayerInfo(SdkBaseModel):
    name: str
    type_: str = Field(alias="type")
    binance_id: str = Field(alias="binanceId")
    account_id: str = Field(alias="accountId")


class PayerInfoDict(TypedDict):
    name: str
    type_: str
    binance_id: str
    account_id: str
