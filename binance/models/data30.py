from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Data30(SdkBaseModel):
    is_lead_trader: bool = Field(alias="isLeadTrader")
    time: int


class Data30Dict(TypedDict):
    is_lead_trader: bool
    time: int
