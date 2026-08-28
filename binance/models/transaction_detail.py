from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TransactionDetail(SdkBaseModel):
    asset: str
    transaction_date_time: int = Field(alias="transactionDateTime")
    rebalance_direction: str = Field(alias="rebalanceDirection")
    rebalance_amount: str = Field(alias="rebalanceAmount")


class TransactionDetailDict(TypedDict):
    asset: str
    transaction_date_time: int
    rebalance_direction: str
    rebalance_amount: str
