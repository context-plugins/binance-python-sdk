from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .margin_trade_coeff_vo import MarginTradeCoeffVo, MarginTradeCoeffVoDict
from .margin_user_asset_vo_list import MarginUserAssetVoList, MarginUserAssetVoListDict


class SapiV1SubAccountMarginAccountResponse(SdkBaseModel):
    email: str
    margin_level: str = Field(alias="marginLevel")
    total_asset_of_btc: str = Field(alias="totalAssetOfBtc")
    total_liability_of_btc: str = Field(alias="totalLiabilityOfBtc")
    total_net_asset_of_btc: str = Field(alias="totalNetAssetOfBtc")
    margin_trade_coeff_vo: MarginTradeCoeffVo = Field(alias="marginTradeCoeffVo")
    margin_user_asset_vo_list: list[MarginUserAssetVoList] = Field(alias="marginUserAssetVoList")


class SapiV1SubAccountMarginAccountResponseDict(TypedDict):
    email: str
    margin_level: str
    total_asset_of_btc: str
    total_liability_of_btc: str
    total_net_asset_of_btc: str
    margin_trade_coeff_vo: MarginTradeCoeffVo | MarginTradeCoeffVoDict
    margin_user_asset_vo_list: list[MarginUserAssetVoList | MarginUserAssetVoListDict]
