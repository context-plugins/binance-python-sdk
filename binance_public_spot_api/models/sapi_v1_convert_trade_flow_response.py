from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .list2 import List2, List2Dict


class SapiV1ConvertTradeFlowResponse(SdkBaseModel):
    list_: list[List2] = Field(alias="list")
    start_time: int = Field(alias="startTime")
    end_time: int = Field(alias="endTime")
    limit: int
    more_data: bool = Field(alias="moreData")


class SapiV1ConvertTradeFlowResponseDict(TypedDict):
    list_: list[List2 | List2Dict]
    start_time: int
    end_time: int
    limit: int
    more_data: bool
