from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row34 import Row34, Row34Dict


class SapiV1EthStakingEthHistoryRateHistoryResponse(SdkBaseModel):
    rows: list[Row34]
    total: int


class SapiV1EthStakingEthHistoryRateHistoryResponseDict(TypedDict):
    rows: list[Row34 | Row34Dict]
    total: int
