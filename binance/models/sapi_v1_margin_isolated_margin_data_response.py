from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .data3 import Data3, Data3Dict


class SapiV1MarginIsolatedMarginDataResponse(SdkBaseModel):
    vip_level: Optional[int] = Field(default=UNSET, alias="vipLevel")
    symbol: Optional[str] = UNSET
    leverage: Optional[str] = UNSET
    data: Optional[list[Data3]] = UNSET


class SapiV1MarginIsolatedMarginDataResponseDict(TypedDict):
    vip_level: NotRequired[int]
    symbol: NotRequired[str]
    leverage: NotRequired[str]
    data: NotRequired[list[Data3 | Data3Dict]]
