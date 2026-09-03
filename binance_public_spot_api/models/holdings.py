from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Holdings(SdkBaseModel):
    wbeth_amount: str = Field(alias="wbethAmount")
    beth_amount: str = Field(alias="bethAmount")


class HoldingsDict(TypedDict):
    wbeth_amount: str
    beth_amount: str
