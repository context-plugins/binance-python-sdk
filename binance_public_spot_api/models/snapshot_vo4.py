from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data6 import Data6, Data6Dict


class SnapshotVo4(SdkBaseModel):
    type_: str = Field(alias="type")
    update_time: int = Field(alias="updateTime")
    data: Data6


class SnapshotVo4Dict(TypedDict):
    type_: str
    update_time: int
    data: Data6 | Data6Dict
