from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row37 import Row37, Row37Dict


class SapiV1EthStakingEthHistoryWbethRewardsHistoryResponse(SdkBaseModel):
    est_rewards_in_eth: str = Field(alias="estRewardsInETH")
    rows: list[Row37]
    total: int


class SapiV1EthStakingEthHistoryWbethRewardsHistoryResponseDict(TypedDict):
    est_rewards_in_eth: str
    rows: list[Row37 | Row37Dict]
    total: int
