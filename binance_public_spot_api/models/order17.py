from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Order17(SdkBaseModel):
    algo_id: int = Field(alias="algoId")
    symbol: str
    side: str
    total_qty: str = Field(alias="totalQty")
    executed_qty: str = Field(alias="executedQty")
    executed_amt: str = Field(alias="executedAmt")
    avg_price: str = Field(alias="avgPrice")
    client_algo_id: str = Field(alias="clientAlgoId")
    book_time: int = Field(alias="bookTime")
    end_time: int = Field(alias="endTime")
    algo_status: str = Field(alias="algoStatus")
    algo_type: str = Field(alias="algoType")
    urgency: str


class Order17Dict(TypedDict):
    algo_id: int
    symbol: str
    side: str
    total_qty: str
    executed_qty: str
    executed_amt: str
    avg_price: str
    client_algo_id: str
    book_time: int
    end_time: int
    algo_status: str
    algo_type: str
    urgency: str
