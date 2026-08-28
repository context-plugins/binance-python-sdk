from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1BlvtRedeemRecordResponse(SdkBaseModel):
    id: int
    token_name: str = Field(alias="tokenName")
    amount: str
    """Redemption amount"""

    nav: str
    """NAV of redemption"""

    fee: str
    """Reemption fee"""

    net_proceed: str = Field(alias="netProceed")
    """Net redemption value in usdt"""

    timestamp: int


class SapiV1BlvtRedeemRecordResponseDict(TypedDict):
    id: int
    token_name: str
    amount: str
    nav: str
    fee: str
    net_proceed: str
    timestamp: int
