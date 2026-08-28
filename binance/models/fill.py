from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Fill(SdkBaseModel):
    price: str
    qty: str
    commission: str
    commission_asset: str = Field(alias="commissionAsset")


class FillDict(TypedDict):
    price: str
    qty: str
    commission: str
    commission_asset: str
