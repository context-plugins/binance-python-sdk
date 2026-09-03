from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SapiV1PortfolioMarginAssetLeverageResponse(SdkBaseModel):
    asset: Optional[str] = UNSET
    collateral_rate: Optional[str] = Field(default=UNSET, alias="collateralRate")


class SapiV1PortfolioMarginAssetLeverageResponseDict(TypedDict):
    asset: NotRequired[str]
    collateral_rate: NotRequired[str]
