from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class QuoteAsset(SdkBaseModel):
    asset: str
    borrow_enabled: bool = Field(alias="borrowEnabled")
    borrowed: str
    free: str
    interest: str
    locked: str
    net_asset: str = Field(alias="netAsset")
    net_asset_of_btc: str = Field(alias="netAssetOfBtc")
    repay_enabled: bool = Field(alias="repayEnabled")
    total_asset: str = Field(alias="totalAsset")


class QuoteAssetDict(TypedDict):
    asset: str
    borrow_enabled: bool
    borrowed: str
    free: str
    interest: str
    locked: str
    net_asset: str
    net_asset_of_btc: str
    repay_enabled: bool
    total_asset: str
