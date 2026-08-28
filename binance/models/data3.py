from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Data3(SdkBaseModel):
    coin: Optional[str] = UNSET
    daily_interest: Optional[str] = Field(default=UNSET, alias="dailyInterest")
    borrow_limit: Optional[str] = Field(default=UNSET, alias="borrowLimit")


class Data3Dict(TypedDict):
    coin: NotRequired[str]
    daily_interest: NotRequired[str]
    borrow_limit: NotRequired[str]
