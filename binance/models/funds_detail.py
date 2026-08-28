from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class FundsDetail(SdkBaseModel):
    currency: str
    amount: str


class FundsDetailDict(TypedDict):
    currency: str
    amount: str
