from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data31 import Data31, Data31Dict


class SapiV1CopyTradingFuturesLeadSymbolResponse(SdkBaseModel):
    code: str
    message: str
    data: Data31


class SapiV1CopyTradingFuturesLeadSymbolResponseDict(TypedDict):
    code: str
    message: str
    data: Data31 | Data31Dict
