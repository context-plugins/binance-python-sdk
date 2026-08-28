from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data30 import Data30, Data30Dict


class SapiV1CopyTradingFuturesUserStatusResponse(SdkBaseModel):
    code: str
    message: str
    data: Data30
    success: bool


class SapiV1CopyTradingFuturesUserStatusResponseDict(TypedDict):
    code: str
    message: str
    data: Data30 | Data30Dict
    success: bool
