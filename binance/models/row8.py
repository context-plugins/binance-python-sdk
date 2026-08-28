from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row8(SdkBaseModel):
    tran_id: int = Field(alias="tranId")
    type_: int = Field(alias="type")
    time: int
    deducted_asset: str = Field(alias="deductedAsset")
    deducted_amount: str = Field(alias="deductedAmount")
    target_asset: str = Field(alias="targetAsset")
    target_amount: str = Field(alias="targetAmount")
    status: str
    account_type: str = Field(alias="accountType")


class Row8Dict(TypedDict):
    tran_id: int
    type_: int
    time: int
    deducted_asset: str
    deducted_amount: str
    target_asset: str
    target_amount: str
    status: str
    account_type: str
