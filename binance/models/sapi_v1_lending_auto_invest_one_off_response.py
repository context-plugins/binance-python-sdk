from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1LendingAutoInvestOneOffResponse(SdkBaseModel):
    transaction_id: int = Field(alias="transactionId")
    wait_second: int = Field(alias="waitSecond")


class SapiV1LendingAutoInvestOneOffResponseDict(TypedDict):
    transaction_id: int
    wait_second: int
