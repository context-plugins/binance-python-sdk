from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV2EthStakingEthStakeResponse(SdkBaseModel):
    success: bool
    wbeth_amount: str = Field(alias="wbethAmount")
    conversion_ratio: str = Field(alias="conversionRatio")
    """ETH amount per 1 WBETH"""


class SapiV2EthStakingEthStakeResponseDict(TypedDict):
    success: bool
    wbeth_amount: str
    conversion_ratio: str
