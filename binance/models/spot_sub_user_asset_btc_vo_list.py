from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SpotSubUserAssetBtcVoList(SdkBaseModel):
    email: str
    total_asset: str = Field(alias="totalAsset")


class SpotSubUserAssetBtcVoListDict(TypedDict):
    email: str
    total_asset: str
