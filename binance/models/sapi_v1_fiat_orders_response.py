from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data7 import Data7, Data7Dict


class SapiV1FiatOrdersResponse(SdkBaseModel):
    code: str
    message: str
    data: list[Data7]
    total: int
    success: bool


class SapiV1FiatOrdersResponseDict(TypedDict):
    code: str
    message: str
    data: list[Data7 | Data7Dict]
    total: int
    success: bool
