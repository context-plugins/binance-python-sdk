from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1LendingAutoInvestRedeemHistoryResponse(SdkBaseModel):
    index_id: int = Field(alias="indexId")
    index_name: str = Field(alias="indexName")
    redemption_id: int = Field(alias="redemptionId")
    status: str
    asset: str
    amount: str
    redemption_date_time: int = Field(alias="redemptionDateTime")
    transaction_fee: str = Field(alias="transactionFee")
    transaction_fee_unit: str = Field(alias="transactionFeeUnit")


class SapiV1LendingAutoInvestRedeemHistoryResponseDict(TypedDict):
    index_id: int
    index_name: str
    redemption_id: int
    status: str
    asset: str
    amount: str
    redemption_date_time: int
    transaction_fee: str
    transaction_fee_unit: str
