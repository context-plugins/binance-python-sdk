from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Data10(SdkBaseModel):
    coin_name: str = Field(alias="coinName")
    coin_id: int = Field(alias="coinId")
    pool_index: int = Field(alias="poolIndex")
    algo_id: int = Field(alias="algoId")
    algo_name: str = Field(alias="algoName")


class Data10Dict(TypedDict):
    coin_name: str
    coin_id: int
    pool_index: int
    algo_id: int
    algo_name: str
