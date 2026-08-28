from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row33 import Row33, Row33Dict


class SapiV1EthStakingEthHistoryRewardsHistoryResponse(SdkBaseModel):
    rows: list[Row33]
    total: int


class SapiV1EthStakingEthHistoryRewardsHistoryResponseDict(TypedDict):
    rows: list[Row33 | Row33Dict]
    total: int
