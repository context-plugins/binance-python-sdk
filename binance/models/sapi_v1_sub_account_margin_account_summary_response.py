from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .sub_account_list2 import SubAccountList2, SubAccountList2Dict


class SapiV1SubAccountMarginAccountSummaryResponse(SdkBaseModel):
    total_asset_of_btc: str = Field(alias="totalAssetOfBtc")
    total_liability_of_btc: str = Field(alias="totalLiabilityOfBtc")
    total_net_asset_of_btc: str = Field(alias="totalNetAssetOfBtc")
    sub_account_list: list[SubAccountList2] = Field(alias="subAccountList")


class SapiV1SubAccountMarginAccountSummaryResponseDict(TypedDict):
    total_asset_of_btc: str
    total_liability_of_btc: str
    total_net_asset_of_btc: str
    sub_account_list: list[SubAccountList2 | SubAccountList2Dict]
