from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .snapshot_vo2 import SnapshotVo2, SnapshotVo2Dict


class SnapshotFutures(SdkBaseModel):
    code: int
    msg: str
    snapshot_vos: list[SnapshotVo2] = Field(alias="snapshotVos")


class SnapshotFuturesDict(TypedDict):
    code: int
    msg: str
    snapshot_vos: list[SnapshotVo2 | SnapshotVo2Dict]
