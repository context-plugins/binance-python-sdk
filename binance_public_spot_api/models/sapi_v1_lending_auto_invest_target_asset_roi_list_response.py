from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1LendingAutoInvestTargetAssetRoiListResponse(SdkBaseModel):
    date: str
    simulate_roi: str = Field(alias="simulateRoi")


class SapiV1LendingAutoInvestTargetAssetRoiListResponseDict(TypedDict):
    date: str
    simulate_roi: str
