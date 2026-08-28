from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .filter import Filter, FilterDict


class Symbol(SdkBaseModel):
    symbol: str
    status: str
    base_asset: str = Field(alias="baseAsset")
    base_asset_precision: int = Field(alias="baseAssetPrecision")
    quote_asset: str = Field(alias="quoteAsset")
    quote_asset_precision: int = Field(alias="quoteAssetPrecision")
    base_commission_precision: int = Field(alias="baseCommissionPrecision")
    quote_commission_precision: int = Field(alias="quoteCommissionPrecision")
    order_types: list[str] = Field(alias="orderTypes")
    iceberg_allowed: bool = Field(alias="icebergAllowed")
    oco_allowed: bool = Field(alias="ocoAllowed")
    oto_allowed: bool = Field(alias="otoAllowed")
    quote_order_qty_market_allowed: bool = Field(alias="quoteOrderQtyMarketAllowed")
    allow_trailing_stop: bool = Field(alias="allowTrailingStop")
    cancel_replace_allowed: bool = Field(alias="cancelReplaceAllowed")
    is_spot_trading_allowed: bool = Field(alias="isSpotTradingAllowed")
    is_margin_trading_allowed: bool = Field(alias="isMarginTradingAllowed")
    filters: list[Filter]
    permissions: list[str]
    permission_sets: list[list[str]] = Field(alias="permissionSets")
    default_self_trade_prevention_mode: str = Field(alias="defaultSelfTradePreventionMode")
    allowed_self_trade_prevention_modes: list[str] = Field(alias="allowedSelfTradePreventionModes")


class SymbolDict(TypedDict):
    symbol: str
    status: str
    base_asset: str
    base_asset_precision: int
    quote_asset: str
    quote_asset_precision: int
    base_commission_precision: int
    quote_commission_precision: int
    order_types: list[str]
    iceberg_allowed: bool
    oco_allowed: bool
    oto_allowed: bool
    quote_order_qty_market_allowed: bool
    allow_trailing_stop: bool
    cancel_replace_allowed: bool
    is_spot_trading_allowed: bool
    is_margin_trading_allowed: bool
    filters: list[Filter | FilterDict]
    permissions: list[str]
    permission_sets: list[list[str]]
    default_self_trade_prevention_mode: str
    allowed_self_trade_prevention_modes: list[str]
