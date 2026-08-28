from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .collateral import Collateral, CollateralDict


class SapiV1MarginCrossMarginCollateralRatioResponse(SdkBaseModel):
    collaterals: list[Collateral]
    asset_names: list[str] = Field(alias="assetNames")


class SapiV1MarginCrossMarginCollateralRatioResponseDict(TypedDict):
    collaterals: list[Collateral | CollateralDict]
    asset_names: list[str]
