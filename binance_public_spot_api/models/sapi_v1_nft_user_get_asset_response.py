from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .list6 import List6, List6Dict


class SapiV1NftUserGetAssetResponse(SdkBaseModel):
    total: int
    list_: list[List6] = Field(alias="list")


class SapiV1NftUserGetAssetResponseDict(TypedDict):
    total: int
    list_: list[List6 | List6Dict]
