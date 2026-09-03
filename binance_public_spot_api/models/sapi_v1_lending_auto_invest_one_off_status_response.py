from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1LendingAutoInvestOneOffStatusResponse(SdkBaseModel):
    transaction_id: int = Field(alias="transactionId")
    status: str


class SapiV1LendingAutoInvestOneOffStatusResponseDict(TypedDict):
    transaction_id: int
    status: str
