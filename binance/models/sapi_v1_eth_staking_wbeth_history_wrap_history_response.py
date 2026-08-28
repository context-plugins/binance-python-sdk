from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row35 import Row35, Row35Dict


class SapiV1EthStakingWbethHistoryWrapHistoryResponse(SdkBaseModel):
    rows: list[Row35]
    total: int


class SapiV1EthStakingWbethHistoryWrapHistoryResponseDict(TypedDict):
    rows: list[Row35 | Row35Dict]
    total: int
