from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data8 import Data8, Data8Dict


class SapiV1FiatPaymentsResponse(SdkBaseModel):
    code: str
    message: str
    data: list[Data8]
    total: int
    success: bool


class SapiV1FiatPaymentsResponseDict(TypedDict):
    code: str
    message: str
    data: list[Data8 | Data8Dict]
    total: int
    success: bool
