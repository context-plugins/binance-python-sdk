from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Transaction(SdkBaseModel):
    tran_id: int = Field(alias="tranId")
    """transaction id"""


class TransactionDict(TypedDict):
    tran_id: int
