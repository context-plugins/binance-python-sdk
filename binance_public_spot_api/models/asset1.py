from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Asset1(SdkBaseModel):
    asset: str
    margin_balance: str = Field(alias="marginBalance")
    wallet_balance: str = Field(alias="walletBalance")


class Asset1Dict(TypedDict):
    asset: str
    margin_balance: str
    wallet_balance: str
