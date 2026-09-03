from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1BlvtRedeemResponse(SdkBaseModel):
    id: int
    status: str
    """S, P, and F for "success", "pending", and "failure"
    """

    token_name: str = Field(alias="tokenName")
    redeem_amount: str = Field(alias="redeemAmount")
    """Redemption token amount"""

    amount: str
    """Redemption value in usdt"""

    timestamp: int


class SapiV1BlvtRedeemResponseDict(TypedDict):
    id: int
    status: str
    token_name: str
    redeem_amount: str
    amount: str
    timestamp: int
