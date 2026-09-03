from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .asset_allocation1 import AssetAllocation1, AssetAllocation1Dict
from .detail4 import Detail4, Detail4Dict


class SapiV1LendingAutoInvestIndexUserSummaryResponse(SdkBaseModel):
    index_id: int = Field(alias="indexId")
    total_invested_in_usd: str = Field(alias="totalInvestedInUSD")
    current_invested_in_usd: str = Field(alias="currentInvestedInUSD")
    """current invest"""

    pnl_in_usd: str = Field(alias="pnlInUSD")
    """PNL of the plan in USD based on current amount"""

    roi: str
    """ROI of the plan based on current amount"""

    asset_allocation: list[AssetAllocation1] = Field(alias="assetAllocation")
    details: list[Detail4]


class SapiV1LendingAutoInvestIndexUserSummaryResponseDict(TypedDict):
    index_id: int
    total_invested_in_usd: str
    current_invested_in_usd: str
    pnl_in_usd: str
    roi: str
    asset_allocation: list[AssetAllocation1 | AssetAllocation1Dict]
    details: list[Detail4 | Detail4Dict]
