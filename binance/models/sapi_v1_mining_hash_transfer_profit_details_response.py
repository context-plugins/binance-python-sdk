from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data16 import Data16, Data16Dict


class SapiV1MiningHashTransferProfitDetailsResponse(SdkBaseModel):
    code: int
    msg: str
    data: Data16


class SapiV1MiningHashTransferProfitDetailsResponseDict(TypedDict):
    code: int
    msg: str
    data: Data16 | Data16Dict
