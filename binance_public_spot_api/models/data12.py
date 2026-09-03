from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .worker_data import WorkerData, WorkerDataDict


class Data12(SdkBaseModel):
    worker_datas: list[WorkerData] = Field(alias="workerDatas")
    total_num: int = Field(alias="totalNum")
    page_size: int = Field(alias="pageSize")


class Data12Dict(TypedDict):
    worker_datas: list[WorkerData | WorkerDataDict]
    total_num: int
    page_size: int
