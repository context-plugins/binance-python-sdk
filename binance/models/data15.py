from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .config_detail import ConfigDetail, ConfigDetailDict


class Data15(SdkBaseModel):
    config_details: list[ConfigDetail] = Field(alias="configDetails")
    total_num: int = Field(alias="totalNum")
    page_size: int = Field(alias="pageSize")


class Data15Dict(TypedDict):
    config_details: list[ConfigDetail | ConfigDetailDict]
    total_num: int
    page_size: int
