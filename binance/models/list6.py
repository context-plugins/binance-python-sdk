from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class List6(SdkBaseModel):
    network: str
    contract_address: str = Field(alias="contractAddress")
    token_id: str = Field(alias="tokenId")


class List6Dict(TypedDict):
    network: str
    contract_address: str
    token_id: str
