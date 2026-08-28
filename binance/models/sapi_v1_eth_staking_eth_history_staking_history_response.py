from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row31 import Row31, Row31Dict


class SapiV1EthStakingEthHistoryStakingHistoryResponse(SdkBaseModel):
    rows: list[Row31]
    total: int


class SapiV1EthStakingEthHistoryStakingHistoryResponseDict(TypedDict):
    rows: list[Row31 | Row31Dict]
    total: int
