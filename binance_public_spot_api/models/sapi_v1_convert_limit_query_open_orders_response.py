from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .list1 import List1, List1Dict


class SapiV1ConvertLimitQueryOpenOrdersResponse(SdkBaseModel):
    list_: list[List1] = Field(alias="list")


class SapiV1ConvertLimitQueryOpenOrdersResponseDict(TypedDict):
    list_: list[List1 | List1Dict]
