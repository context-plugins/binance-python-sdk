from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .spot_sub_user_asset_btc_vo_list import SpotSubUserAssetBtcVoList, SpotSubUserAssetBtcVoListDict


class SapiV1SubAccountSpotSummaryResponse(SdkBaseModel):
    total_count: int = Field(alias="totalCount")
    master_account_total_asset: str = Field(alias="masterAccountTotalAsset")
    spot_sub_user_asset_btc_vo_list: list[SpotSubUserAssetBtcVoList] = Field(alias="spotSubUserAssetBtcVoList")


class SapiV1SubAccountSpotSummaryResponseDict(TypedDict):
    total_count: int
    master_account_total_asset: str
    spot_sub_user_asset_btc_vo_list: list[SpotSubUserAssetBtcVoList | SpotSubUserAssetBtcVoListDict]
