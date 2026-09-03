from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .hashrate_data import HashrateData, HashrateDataDict


class Data11(SdkBaseModel):
    worker_name: str = Field(alias="workerName")
    """Mining Account name"""

    type_: str = Field(alias="type")
    """Type of hourly hashrate"""

    hashrate_datas: list[HashrateData] = Field(alias="hashrateDatas")


class Data11Dict(TypedDict):
    worker_name: str
    type_: str
    hashrate_datas: list[HashrateData | HashrateDataDict]
