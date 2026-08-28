from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Token(SdkBaseModel):
    network: str
    token_id: str = Field(alias="tokenId")
    contract_address: str = Field(alias="contractAddress")


class TokenDict(TypedDict):
    network: str
    token_id: str
    contract_address: str
