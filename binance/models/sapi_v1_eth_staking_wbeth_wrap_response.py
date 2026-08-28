from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1EthStakingWbethWrapResponse(SdkBaseModel):
    success: bool
    wbeth_amount: str = Field(alias="wbethAmount")
    exchange_rate: str = Field(alias="exchangeRate")


class SapiV1EthStakingWbethWrapResponseDict(TypedDict):
    success: bool
    wbeth_amount: str
    exchange_rate: str
