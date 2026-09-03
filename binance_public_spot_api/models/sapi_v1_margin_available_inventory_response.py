from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .assets import Assets, AssetsDict


class SapiV1MarginAvailableInventoryResponse(SdkBaseModel):
    assets: Assets
    update_time: int = Field(alias="updateTime")


class SapiV1MarginAvailableInventoryResponseDict(TypedDict):
    assets: Assets | AssetsDict
    update_time: int
