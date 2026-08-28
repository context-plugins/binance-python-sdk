from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .list7 import List7, List7Dict


class SapiV1DciProductListResponse(SdkBaseModel):
    total: int
    list_: list[List7] = Field(alias="list")


class SapiV1DciProductListResponseDict(TypedDict):
    total: int
    list_: list[List7 | List7Dict]
