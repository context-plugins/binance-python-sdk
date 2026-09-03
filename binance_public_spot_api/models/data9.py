from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Data9(SdkBaseModel):
    algo_name: str = Field(alias="algoName")
    algo_id: int = Field(alias="algoId")
    pool_index: int = Field(alias="poolIndex")
    unit: str


class Data9Dict(TypedDict):
    algo_name: str
    algo_id: int
    pool_index: int
    unit: str
