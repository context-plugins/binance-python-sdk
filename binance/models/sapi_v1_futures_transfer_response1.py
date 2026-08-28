from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row11 import Row11, Row11Dict


class SapiV1FuturesTransferResponse1(SdkBaseModel):
    rows: list[Row11]
    total: int


class SapiV1FuturesTransferResponse1Dict(TypedDict):
    rows: list[Row11 | Row11Dict]
    total: int
