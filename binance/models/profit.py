from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Profit(SdkBaseModel):
    amount_from_wbeth: str = Field(alias="amountFromWBETH")
    amount_from_beth: str = Field(alias="amountFromBETH")


class ProfitDict(TypedDict):
    amount_from_wbeth: str
    amount_from_beth: str
