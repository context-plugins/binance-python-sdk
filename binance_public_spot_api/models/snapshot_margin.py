from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .snapshot_vo1 import SnapshotVo1, SnapshotVo1Dict


class SnapshotMargin(SdkBaseModel):
    code: int
    msg: str
    snapshot_vos: list[SnapshotVo1] = Field(alias="snapshotVos")


class SnapshotMarginDict(TypedDict):
    code: int
    msg: str
    snapshot_vos: list[SnapshotVo1 | SnapshotVo1Dict]
