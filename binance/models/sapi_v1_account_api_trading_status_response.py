from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data4 import Data4, Data4Dict


class SapiV1AccountApiTradingStatusResponse(SdkBaseModel):
    data: Data4


class SapiV1AccountApiTradingStatusResponseDict(TypedDict):
    data: Data4 | Data4Dict
