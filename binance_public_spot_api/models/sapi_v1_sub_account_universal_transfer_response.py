from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1SubAccountUniversalTransferResponse(SdkBaseModel):
    tran_id: int = Field(alias="tranId")
    from_email: str = Field(alias="fromEmail")
    to_email: str = Field(alias="toEmail")
    asset: str
    amount: str
    from_account_type: str = Field(alias="fromAccountType")
    to_account_type: str = Field(alias="toAccountType")
    status: str
    create_time_stamp: int = Field(alias="createTimeStamp")
    client_tran_id: str = Field(alias="clientTranId")


class SapiV1SubAccountUniversalTransferResponseDict(TypedDict):
    tran_id: int
    from_email: str
    to_email: str
    asset: str
    amount: str
    from_account_type: str
    to_account_type: str
    status: str
    create_time_stamp: int
    client_tran_id: str
