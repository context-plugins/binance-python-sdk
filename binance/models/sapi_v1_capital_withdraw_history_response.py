from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SapiV1CapitalWithdrawHistoryResponse(SdkBaseModel):
    address: str
    amount: str
    apply_time: str = Field(alias="applyTime")
    coin: str
    id: str
    withdraw_order_id: str = Field(alias="withdrawOrderId")
    """will not be returned if there's no withdrawOrderId for this withdraw."""

    network: str
    transfer_type: int = Field(alias="transferType")
    """1 for internal transfer, 0 for external transfer"""

    status: int
    transaction_fee: str = Field(alias="transactionFee")
    confirm_no: Optional[int] = Field(default=UNSET, alias="confirmNo")
    info: Optional[str] = UNSET
    """Reason for withdrawal failure"""

    tx_id: str = Field(alias="txId")


class SapiV1CapitalWithdrawHistoryResponseDict(TypedDict):
    address: str
    amount: str
    apply_time: str
    coin: str
    id: str
    withdraw_order_id: str
    network: str
    transfer_type: int
    status: int
    transaction_fee: str
    confirm_no: NotRequired[int]
    info: NotRequired[str]
    tx_id: str
