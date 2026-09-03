from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Data24(SdkBaseModel):
    asset: str
    type_: int = Field(alias="type")
    """rebate type：1 is commission rebate，2 is referral kickback"""

    amount: str
    update_time: int = Field(alias="updateTime")


class Data24Dict(TypedDict):
    asset: str
    type_: int
    amount: str
    update_time: int
