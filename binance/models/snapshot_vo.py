from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data import Data, DataDict


class SnapshotVo(SdkBaseModel):
    data: Data
    type_: str = Field(alias="type")
    update_time: int = Field(alias="updateTime")


class SnapshotVoDict(TypedDict):
    data: Data | DataDict
    type_: str
    update_time: int
