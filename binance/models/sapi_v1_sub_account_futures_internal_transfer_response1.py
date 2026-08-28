from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1SubAccountFuturesInternalTransferResponse1(SdkBaseModel):
    success: bool
    txn_id: str = Field(alias="txnId")


class SapiV1SubAccountFuturesInternalTransferResponse1Dict(TypedDict):
    success: bool
    txn_id: str
