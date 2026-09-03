from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row2 import Row2, Row2Dict


class SapiV1MarginTransferResponse(SdkBaseModel):
    rows: list[Row2]
    total: int


class SapiV1MarginTransferResponseDict(TypedDict):
    rows: list[Row2 | Row2Dict]
    total: int
