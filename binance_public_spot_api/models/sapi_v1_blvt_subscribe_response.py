from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1BlvtSubscribeResponse(SdkBaseModel):
    id: int
    status: str
    """S, P, and F for "success", "pending", and "failure"
    """

    token_name: str = Field(alias="tokenName")
    amount: str
    """subscribed token amount"""

    cost: str
    """subscription cost in usdt"""

    timestamp: int


class SapiV1BlvtSubscribeResponseDict(TypedDict):
    id: int
    status: str
    token_name: str
    amount: str
    cost: str
    timestamp: int
