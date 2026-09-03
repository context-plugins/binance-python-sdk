from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row11(SdkBaseModel):
    asset: str
    tran_id: int = Field(alias="tranId")
    amount: str
    type_: str = Field(alias="type")
    timestamp: int
    status: str
    """one of PENDING (pending to execution), CONFIRMED (successfully transfered), FAILED (execution failed, nothing
    happened to your account);"""


class Row11Dict(TypedDict):
    asset: str
    tran_id: int
    amount: str
    type_: str
    timestamp: int
    status: str
