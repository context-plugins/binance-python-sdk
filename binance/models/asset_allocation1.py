from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AssetAllocation1(SdkBaseModel):
    target_asset: str = Field(alias="targetAsset")
    """for pie chart"""

    allocation: str


class AssetAllocation1Dict(TypedDict):
    target_asset: str
    allocation: str
