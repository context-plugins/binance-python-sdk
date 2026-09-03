from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1SubAccountTransferSubToMasterResponse(SdkBaseModel):
    txn_id: str = Field(alias="txnId")


class SapiV1SubAccountTransferSubToMasterResponseDict(TypedDict):
    txn_id: str
