from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .transaction_detail import TransactionDetail, TransactionDetailDict


class SapiV1LendingAutoInvestRebalanceHistoryResponse(SdkBaseModel):
    index_id: int = Field(alias="indexId")
    index_name: str = Field(alias="indexName")
    rebalance_id: int = Field(alias="rebalanceId")
    status: str
    rebalance_fee: str = Field(alias="rebalanceFee")
    rebalance_fee_unit: str = Field(alias="rebalanceFeeUnit")
    transaction_details: list[TransactionDetail] = Field(alias="transactionDetails")


class SapiV1LendingAutoInvestRebalanceHistoryResponseDict(TypedDict):
    index_id: int
    index_name: str
    rebalance_id: int
    status: str
    rebalance_fee: str
    rebalance_fee_unit: str
    transaction_details: list[TransactionDetail | TransactionDetailDict]
