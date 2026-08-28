from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1LendingAutoInvestHistoryListResponse(SdkBaseModel):
    id: int
    target_asset: str = Field(alias="targetAsset")
    plan_type: str = Field(alias="planType")
    plan_name: str = Field(alias="planName")
    plan_id: int = Field(alias="planId")
    transaction_date_time: int = Field(alias="transactionDateTime")
    transaction_status: str = Field(alias="transactionStatus")
    failed_type: str = Field(alias="failedType")
    source_asset: str = Field(alias="sourceAsset")
    source_asset_amount: str = Field(alias="sourceAssetAmount")
    target_asset_amount: str = Field(alias="targetAssetAmount")
    source_wallet: str = Field(alias="sourceWallet")
    flexible_used: str = Field(alias="flexibleUsed")
    transaction_fee: str = Field(alias="transactionFee")
    transaction_fee_unit: str = Field(alias="transactionFeeUnit")
    execution_price: str = Field(alias="executionPrice")
    execution_type: str = Field(alias="executionType")
    subscription_cycle: str = Field(alias="subscriptionCycle")


class SapiV1LendingAutoInvestHistoryListResponseDict(TypedDict):
    id: int
    target_asset: str
    plan_type: str
    plan_name: str
    plan_id: int
    transaction_date_time: int
    transaction_status: str
    failed_type: str
    source_asset: str
    source_asset_amount: str
    target_asset_amount: str
    source_wallet: str
    flexible_used: str
    transaction_fee: str
    transaction_fee_unit: str
    execution_price: str
    execution_type: str
    subscription_cycle: str
