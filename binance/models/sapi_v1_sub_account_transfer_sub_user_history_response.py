from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1SubAccountTransferSubUserHistoryResponse(SdkBaseModel):
    counter_party: str = Field(alias="counterParty")
    email: str
    type_: int = Field(alias="type")
    """1 for transfer in, 2 for transfer out"""

    asset: str
    qty: str
    from_account_type: str = Field(alias="fromAccountType")
    to_account_type: str = Field(alias="toAccountType")
    status: str
    tran_id: int = Field(alias="tranId")
    time: int


class SapiV1SubAccountTransferSubUserHistoryResponseDict(TypedDict):
    counter_party: str
    email: str
    type_: int
    asset: str
    qty: str
    from_account_type: str
    to_account_type: str
    status: str
    tran_id: int
    time: int
