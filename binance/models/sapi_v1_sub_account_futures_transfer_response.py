from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1SubAccountFuturesTransferResponse(SdkBaseModel):
    txn_id: str = Field(alias="txnId")


class SapiV1SubAccountFuturesTransferResponseDict(TypedDict):
    txn_id: str
