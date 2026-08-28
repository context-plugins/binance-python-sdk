from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .user_asset_dribblet import UserAssetDribblet, UserAssetDribbletDict


class SapiV1AssetDribbletResponse(SdkBaseModel):
    total: int
    """Total counts of exchange"""

    user_asset_dribblets: list[UserAssetDribblet] = Field(alias="userAssetDribblets")


class SapiV1AssetDribbletResponseDict(TypedDict):
    total: int
    user_asset_dribblets: list[UserAssetDribblet | UserAssetDribbletDict]
