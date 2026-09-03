from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .user_asset import UserAsset, UserAssetDict


class SapiV1MarginAccountResponse(SdkBaseModel):
    created: bool
    borrow_enabled: bool = Field(alias="borrowEnabled")
    margin_level: str = Field(alias="marginLevel")
    collateral_margin_level: str = Field(alias="collateralMarginLevel")
    total_asset_of_btc: str = Field(alias="totalAssetOfBtc")
    total_liability_of_btc: str = Field(alias="totalLiabilityOfBtc")
    total_net_asset_of_btc: str = Field(alias="totalNetAssetOfBtc")
    total_collateral_value_in_usdt: str = Field(alias="TotalCollateralValueInUSDT")
    trade_enabled: bool = Field(alias="tradeEnabled")
    transfer_in_enabled: bool = Field(alias="transferInEnabled")
    transfer_out_enabled: bool = Field(alias="transferOutEnabled")
    account_type: str = Field(alias="accountType")
    user_assets: list[UserAsset] = Field(alias="userAssets")


class SapiV1MarginAccountResponseDict(TypedDict):
    created: bool
    borrow_enabled: bool
    margin_level: str
    collateral_margin_level: str
    total_asset_of_btc: str
    total_liability_of_btc: str
    total_net_asset_of_btc: str
    total_collateral_value_in_usdt: str
    trade_enabled: bool
    transfer_in_enabled: bool
    transfer_out_enabled: bool
    account_type: str
    user_assets: list[UserAsset | UserAssetDict]
