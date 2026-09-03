from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .base_asset import BaseAsset, BaseAssetDict
from .quote_asset import QuoteAsset, QuoteAssetDict


class Asset(SdkBaseModel):
    base_asset: BaseAsset = Field(alias="baseAsset")
    quote_asset: QuoteAsset = Field(alias="quoteAsset")
    symbol: str
    isolated_created: bool = Field(alias="isolatedCreated")
    enabled: bool
    """true-enabled, false-disabled"""

    margin_level: str = Field(alias="marginLevel")
    margin_level_status: str = Field(alias="marginLevelStatus")
    """"EXCESSIVE", "NORMAL", "MARGIN_CALL", "PRE_LIQUIDATION", "FORCE_LIQUIDATION"
    """

    margin_ratio: str = Field(alias="marginRatio")
    index_price: str = Field(alias="indexPrice")
    liquidate_price: str = Field(alias="liquidatePrice")
    liquidate_rate: str = Field(alias="liquidateRate")
    trade_enabled: bool = Field(alias="tradeEnabled")


class AssetDict(TypedDict):
    base_asset: BaseAsset | BaseAssetDict
    quote_asset: QuoteAsset | QuoteAssetDict
    symbol: str
    isolated_created: bool
    enabled: bool
    margin_level: str
    margin_level_status: str
    margin_ratio: str
    index_price: str
    liquidate_price: str
    liquidate_rate: str
    trade_enabled: bool
