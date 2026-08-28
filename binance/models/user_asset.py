from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UserAsset(SdkBaseModel):
    asset: str
    borrowed: str
    free: str
    interest: str
    locked: str
    net_asset: str = Field(alias="netAsset")


class UserAssetDict(TypedDict):
    asset: str
    borrowed: str
    free: str
    interest: str
    locked: str
    net_asset: str
