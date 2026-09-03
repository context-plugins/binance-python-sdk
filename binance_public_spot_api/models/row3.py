from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row3(SdkBaseModel):
    isolated_symbol: str = Field(alias="isolatedSymbol")
    asset: str
    interest: str
    interest_accured_time: int = Field(alias="interestAccuredTime")
    interest_rate: str = Field(alias="interestRate")
    principal: str
    type_: str = Field(alias="type")


class Row3Dict(TypedDict):
    isolated_symbol: str
    asset: str
    interest: str
    interest_accured_time: int
    interest_rate: str
    principal: str
    type_: str
