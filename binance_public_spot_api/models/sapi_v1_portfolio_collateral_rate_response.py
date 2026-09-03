from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1PortfolioCollateralRateResponse(SdkBaseModel):
    asset: str
    collateral_rate: str = Field(alias="collateralRate")


class SapiV1PortfolioCollateralRateResponseDict(TypedDict):
    asset: str
    collateral_rate: str
