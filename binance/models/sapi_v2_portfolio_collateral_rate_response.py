from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .collateral_info import CollateralInfo, CollateralInfoDict


class SapiV2PortfolioCollateralRateResponse(SdkBaseModel):
    asset: str
    collateral_info: list[CollateralInfo] = Field(alias="collateralInfo")


class SapiV2PortfolioCollateralRateResponseDict(TypedDict):
    asset: str
    collateral_info: list[CollateralInfo | CollateralInfoDict]
