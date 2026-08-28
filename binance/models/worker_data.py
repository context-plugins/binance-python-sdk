from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class WorkerData(SdkBaseModel):
    worker_id: str = Field(alias="workerId")
    worker_name: str = Field(alias="workerName")
    status: int
    """Status：1 valid, 2 invalid, 3 no longer valid"""

    hash_rate: int = Field(alias="hashRate")
    """Real-time rate"""

    day_hash_rate: int = Field(alias="dayHashRate")
    """24H Hashrate"""

    reject_rate: int = Field(alias="rejectRate")
    """Real-time Rejection Rate"""

    last_share_time: int = Field(alias="lastShareTime")
    """Last submission time"""


class WorkerDataDict(TypedDict):
    worker_id: str
    worker_name: str
    status: int
    hash_rate: int
    day_hash_rate: int
    reject_rate: int
    last_share_time: int
