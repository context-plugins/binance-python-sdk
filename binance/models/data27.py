from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Data27(SdkBaseModel):
    valid: bool
    token: str
    amount: str


class Data27Dict(TypedDict):
    valid: bool
    token: str
    amount: str
