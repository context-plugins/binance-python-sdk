from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .sub_account_list1 import SubAccountList1, SubAccountList1Dict


class DeliveryAccountSummaryResp(SdkBaseModel):
    total_margin_balance_of_btc: str = Field(alias="totalMarginBalanceOfBTC")
    total_unrealized_profit_of_btc: str = Field(alias="totalUnrealizedProfitOfBTC")
    total_wallet_balance_of_btc: str = Field(alias="totalWalletBalanceOfBTC")
    asset: str
    sub_account_list: list[SubAccountList1] = Field(alias="subAccountList")


class DeliveryAccountSummaryRespDict(TypedDict):
    total_margin_balance_of_btc: str
    total_unrealized_profit_of_btc: str
    total_wallet_balance_of_btc: str
    asset: str
    sub_account_list: list[SubAccountList1 | SubAccountList1Dict]
