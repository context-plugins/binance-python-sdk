from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1PortfolioAccountResponse(SdkBaseModel):
    uni_mmr: str = Field(alias="uniMMR")
    """Classic Portfolio margin account maintenance margin rate"""

    account_equity: str = Field(alias="accountEquity")
    """Account equity, unit is USD"""

    actual_equity: str = Field(alias="actualEquity")
    """Actual equity, unit is USD"""

    account_maint_margin: str = Field(alias="accountMaintMargin")
    """Classic Portfolio margin account maintenance margin, unit is USD"""

    account_status: str = Field(alias="accountStatus")
    """Classic Portfolio margin account status:"NORMAL", "MARGIN_CALL", "SUPPLY_MARGIN", "REDUCE_ONLY",
    "ACTIVE_LIQUIDATION", "FORCE_LIQUIDATION", "BANKRUPTED"
    """

    account_type: str = Field(alias="accountType")
    """PM_1 for classic PM, PM_2 for PM"""


class SapiV1PortfolioAccountResponseDict(TypedDict):
    uni_mmr: str
    account_equity: str
    actual_equity: str
    account_maint_margin: str
    account_status: str
    account_type: str
