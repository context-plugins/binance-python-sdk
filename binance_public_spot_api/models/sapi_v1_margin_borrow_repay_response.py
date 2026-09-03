from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1MarginBorrowRepayResponse(SdkBaseModel):
    tran_id: int = Field(alias="tranId")


class SapiV1MarginBorrowRepayResponseDict(TypedDict):
    tran_id: int
