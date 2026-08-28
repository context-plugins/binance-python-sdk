from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Data29(SdkBaseModel):
    coin: Optional[str] = UNSET
    from_min: Optional[str] = Field(default=UNSET, alias="fromMin")
    from_max: Optional[str] = Field(default=UNSET, alias="fromMax")


class Data29Dict(TypedDict):
    coin: NotRequired[str]
    from_min: NotRequired[str]
    from_max: NotRequired[str]
