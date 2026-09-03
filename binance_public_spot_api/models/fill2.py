from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Fill2(SdkBaseModel):
    match_type: str = Field(alias="matchType")
    price: str
    qty: str
    commission: str
    commission_asset: str = Field(alias="commissionAsset")
    trade_id: int = Field(alias="tradeId")
    alloc_id: int = Field(alias="allocId")


class Fill2Dict(TypedDict):
    match_type: str
    price: str
    qty: str
    commission: str
    commission_asset: str
    trade_id: int
    alloc_id: int
