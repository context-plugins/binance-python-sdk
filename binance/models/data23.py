from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data24 import Data24, Data24Dict


class Data23(SdkBaseModel):
    page: int
    total_records: int = Field(alias="totalRecords")
    total_page_num: int = Field(alias="totalPageNum")
    data: list[Data24]


class Data23Dict(TypedDict):
    page: int
    total_records: int
    total_page_num: int
    data: list[Data24 | Data24Dict]
