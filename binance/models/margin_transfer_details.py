from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .row import Row, RowDict


class MarginTransferDetails(SdkBaseModel):
    rows: list[Row]
    total: int


class MarginTransferDetailsDict(TypedDict):
    rows: list[Row | RowDict]
    total: int
