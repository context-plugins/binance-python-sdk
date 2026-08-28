from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .snapshot_vo4 import SnapshotVo4, SnapshotVo4Dict


class SapiV1ManagedSubaccountFetchFutureAssetResponse(SdkBaseModel):
    code: int
    message: str
    snapshot_vos: list[SnapshotVo4] = Field(alias="snapshotVos")


class SapiV1ManagedSubaccountFetchFutureAssetResponseDict(TypedDict):
    code: int
    message: str
    snapshot_vos: list[SnapshotVo4 | SnapshotVo4Dict]
