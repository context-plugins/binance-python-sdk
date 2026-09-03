from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AssetAllocation(SdkBaseModel):
    target_asset: str = Field(alias="targetAsset")
    allocation: str


class AssetAllocationDict(TypedDict):
    target_asset: str
    allocation: str
