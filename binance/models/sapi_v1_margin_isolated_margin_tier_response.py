from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SapiV1MarginIsolatedMarginTierResponse(SdkBaseModel):
    symbol: Optional[str] = UNSET
    tier: Optional[int] = UNSET
    effective_multiple: Optional[str] = Field(default=UNSET, alias="effectiveMultiple")
    initial_risk_ratio: Optional[str] = Field(default=UNSET, alias="initialRiskRatio")
    liquidation_risk_ratio: Optional[str] = Field(default=UNSET, alias="liquidationRiskRatio")
    base_asset_max_borrowable: Optional[str] = Field(default=UNSET, alias="baseAssetMaxBorrowable")
    quote_asset_max_borrowable: Optional[str] = Field(default=UNSET, alias="quoteAssetMaxBorrowable")


class SapiV1MarginIsolatedMarginTierResponseDict(TypedDict):
    symbol: NotRequired[str]
    tier: NotRequired[int]
    effective_multiple: NotRequired[str]
    initial_risk_ratio: NotRequired[str]
    liquidation_risk_ratio: NotRequired[str]
    base_asset_max_borrowable: NotRequired[str]
    quote_asset_max_borrowable: NotRequired[str]
