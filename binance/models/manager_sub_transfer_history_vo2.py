from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ManagerSubTransferHistoryVo2(SdkBaseModel):
    from_email: str = Field(alias="fromEmail")
    from_account_type: str = Field(alias="fromAccountType")
    to_email: str = Field(alias="toEmail")
    to_account_type: str = Field(alias="toAccountType")
    asset: str
    amount: str
    scheduled_data: int = Field(alias="scheduledData")
    create_time: int = Field(alias="createTime")
    status: str
    tran_id: int = Field(alias="tranId")


class ManagerSubTransferHistoryVo2Dict(TypedDict):
    from_email: str
    from_account_type: str
    to_email: str
    to_account_type: str
    asset: str
    amount: str
    scheduled_data: int
    create_time: int
    status: str
    tran_id: int
