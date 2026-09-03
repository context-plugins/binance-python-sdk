from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ApiV3AvgPriceResponse(SdkBaseModel):
    mins: int
    """Average price interval (in minutes)"""

    price: str
    """Average price"""

    close_time: int = Field(alias="closeTime")
    """Last trade time"""


class ApiV3AvgPriceResponseDict(TypedDict):
    mins: int
    price: str
    close_time: int
