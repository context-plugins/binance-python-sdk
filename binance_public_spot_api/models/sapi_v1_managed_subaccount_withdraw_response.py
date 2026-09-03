from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1ManagedSubaccountWithdrawResponse(SdkBaseModel):
    tran_id: int = Field(alias="tranId")


class SapiV1ManagedSubaccountWithdrawResponseDict(TypedDict):
    tran_id: int
