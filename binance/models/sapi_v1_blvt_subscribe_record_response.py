from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1BlvtSubscribeRecordResponse(SdkBaseModel):
    id: int
    token_name: str = Field(alias="tokenName")
    amount: str
    """Subscription amount"""

    nav: str
    """NAV price of subscription"""

    fee: str
    """Subscription fee in usdt"""

    total_charge: str = Field(alias="totalCharge")
    """Subscription cost in usdt"""

    timestamp: int


class SapiV1BlvtSubscribeRecordResponseDict(TypedDict):
    id: int
    token_name: str
    amount: str
    nav: str
    fee: str
    total_charge: str
    timestamp: int
