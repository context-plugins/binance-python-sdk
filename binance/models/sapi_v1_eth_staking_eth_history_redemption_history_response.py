from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row32 import Row32, Row32Dict


class SapiV1EthStakingEthHistoryRedemptionHistoryResponse(SdkBaseModel):
    rows: list[Row32]
    total: int


class SapiV1EthStakingEthHistoryRedemptionHistoryResponseDict(TypedDict):
    rows: list[Row32 | Row32Dict]
    total: int
