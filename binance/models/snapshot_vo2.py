from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data2 import Data2, Data2Dict


class SnapshotVo2(SdkBaseModel):
    data: Data2
    type_: str = Field(alias="type")
    update_time: int = Field(alias="updateTime")


class SnapshotVo2Dict(TypedDict):
    data: Data2 | Data2Dict
    type_: str
    update_time: int
