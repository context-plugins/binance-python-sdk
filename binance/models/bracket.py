from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Bracket(SdkBaseModel):
    leverage: Optional[int] = UNSET
    max_debt: Optional[float] = Field(default=UNSET, alias="maxDebt")
    maintenance_margin_rate: Optional[float] = Field(default=UNSET, alias="maintenanceMarginRate")
    initial_margin_rate: Optional[float] = Field(default=UNSET, alias="initialMarginRate")
    fast_num: Optional[float] = Field(default=UNSET, alias="fastNum")


class BracketDict(TypedDict):
    leverage: NotRequired[int]
    max_debt: NotRequired[float]
    maintenance_margin_rate: NotRequired[float]
    initial_margin_rate: NotRequired[float]
    fast_num: NotRequired[float]
