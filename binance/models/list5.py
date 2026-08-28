from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class List5(SdkBaseModel):
    network: str
    tx_id: str = Field(alias="txID")
    contract_adrress: str = Field(alias="contractAdrress")
    token_id: str = Field(alias="tokenId")
    timestamp: int
    fee: float
    fee_asset: str = Field(alias="feeAsset")


class List5Dict(TypedDict):
    network: str
    tx_id: str
    contract_adrress: str
    token_id: str
    timestamp: int
    fee: float
    fee_asset: str
