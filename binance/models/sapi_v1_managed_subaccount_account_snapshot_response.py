from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .snapshot_vo import SnapshotVo, SnapshotVoDict


class SapiV1ManagedSubaccountAccountSnapshotResponse(SdkBaseModel):
    code: int
    msg: str
    snapshot_vos: list[SnapshotVo] = Field(alias="snapshotVos")


class SapiV1ManagedSubaccountAccountSnapshotResponseDict(TypedDict):
    code: int
    msg: str
    snapshot_vos: list[SnapshotVo | SnapshotVoDict]
