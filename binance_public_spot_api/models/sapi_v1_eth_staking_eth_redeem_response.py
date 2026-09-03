from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1EthStakingEthRedeemResponse(SdkBaseModel):
    success: bool
    arrival_time: int = Field(alias="arrivalTime")
    eth_amount: str = Field(alias="ethAmount")
    conversion_ratio: str = Field(alias="conversionRatio")


class SapiV1EthStakingEthRedeemResponseDict(TypedDict):
    success: bool
    arrival_time: int
    eth_amount: str
    conversion_ratio: str
