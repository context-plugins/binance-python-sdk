from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Assets2(SdkBaseModel):
    asset: str
    margin_balance: float = Field(alias="marginBalance")
    wallet_balance: float = Field(alias="walletBalance")


class Assets2Dict(TypedDict):
    asset: str
    margin_balance: float
    wallet_balance: float
