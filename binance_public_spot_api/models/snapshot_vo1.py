from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data1 import Data1, Data1Dict


class SnapshotVo1(SdkBaseModel):
    data: Data1
    type_: str = Field(alias="type")
    update_time: int = Field(alias="updateTime")


class SnapshotVo1Dict(TypedDict):
    data: Data1 | Data1Dict
    type_: str
    update_time: int
