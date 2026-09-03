from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row5(SdkBaseModel):
    asset: str
    amount: str
    target_asset: str = Field(alias="targetAsset")
    target_amount: str = Field(alias="targetAmount")
    biz_type: str = Field(alias="bizType")
    timestamp: int


class Row5Dict(TypedDict):
    asset: str
    amount: str
    target_asset: str
    target_amount: str
    biz_type: str
    timestamp: int
