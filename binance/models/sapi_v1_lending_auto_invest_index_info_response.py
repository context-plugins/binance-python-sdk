from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .asset_allocation import AssetAllocation, AssetAllocationDict


class SapiV1LendingAutoInvestIndexInfoResponse(SdkBaseModel):
    index_id: int = Field(alias="indexId")
    index_name: str = Field(alias="indexName")
    status: str
    asset_allocation: list[AssetAllocation] = Field(alias="assetAllocation")


class SapiV1LendingAutoInvestIndexInfoResponseDict(TypedDict):
    index_id: int
    index_name: str
    status: str
    asset_allocation: list[AssetAllocation | AssetAllocationDict]
