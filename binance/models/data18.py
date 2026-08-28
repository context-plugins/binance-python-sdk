from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .list import List, ListDict


class Data18(SdkBaseModel):
    type_: str = Field(alias="type")
    user_name: str = Field(alias="userName")
    list_: list[List] = Field(alias="list")


class Data18Dict(TypedDict):
    type_: str
    user_name: str
    list_: list[List | ListDict]
