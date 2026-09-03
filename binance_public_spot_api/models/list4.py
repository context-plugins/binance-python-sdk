from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class List4(SdkBaseModel):
    network: str
    tx_id: int | None = Field(alias="txID")
    contract_adrress: str = Field(alias="contractAdrress")
    token_id: str = Field(alias="tokenId")
    timestamp: int


class List4Dict(TypedDict):
    network: str
    tx_id: int | None
    contract_adrress: str
    token_id: str
    timestamp: int
