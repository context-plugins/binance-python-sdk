from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row47(SdkBaseModel):
    position_id: str = Field(alias="positionId")
    time: int
    asset: str
    lock_period: str = Field(alias="lockPeriod")
    amount: str


class Row47Dict(TypedDict):
    position_id: str
    time: int
    asset: str
    lock_period: str
    amount: str
