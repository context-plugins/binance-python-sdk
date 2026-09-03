from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data22 import Data22, Data22Dict


class SapiV1PayTransactionsResponse(SdkBaseModel):
    code: str
    message: str
    data: list[Data22]
    success: bool


class SapiV1PayTransactionsResponseDict(TypedDict):
    code: str
    message: str
    data: list[Data22 | Data22Dict]
    success: bool
