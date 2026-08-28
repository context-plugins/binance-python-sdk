from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .sub_account_list3 import SubAccountList3, SubAccountList3Dict


class SapiV1SubAccountFuturesAccountSummaryResponse(SdkBaseModel):
    total_initial_margin: str = Field(alias="totalInitialMargin")
    total_maintenance_margin: str = Field(alias="totalMaintenanceMargin")
    total_margin_balance: str = Field(alias="totalMarginBalance")
    total_open_order_initial_margin: str = Field(alias="totalOpenOrderInitialMargin")
    total_position_initial_margin: str = Field(alias="totalPositionInitialMargin")
    total_unrealized_profit: str = Field(alias="totalUnrealizedProfit")
    total_wallet_balance: str = Field(alias="totalWalletBalance")
    asset: str
    sub_account_list: list[SubAccountList3] = Field(alias="subAccountList")


class SapiV1SubAccountFuturesAccountSummaryResponseDict(TypedDict):
    total_initial_margin: str
    total_maintenance_margin: str
    total_margin_balance: str
    total_open_order_initial_margin: str
    total_position_initial_margin: str
    total_unrealized_profit: str
    total_wallet_balance: str
    asset: str
    sub_account_list: list[SubAccountList3 | SubAccountList3Dict]
