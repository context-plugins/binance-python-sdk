from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .list8 import List8, List8Dict


class SapiV1DciProductPositionsResponse(SdkBaseModel):
    total: int
    list_: list[List8] = Field(alias="list")


class SapiV1DciProductPositionsResponseDict(TypedDict):
    total: int
    list_: list[List8 | List8Dict]
