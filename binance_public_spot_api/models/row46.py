from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row46(SdkBaseModel):
    asset: str
    rewards: str
    project_id: str = Field(alias="projectId")
    type_: str = Field(alias="type")
    time: int


class Row46Dict(TypedDict):
    asset: str
    rewards: str
    project_id: str
    type_: str
    time: int
