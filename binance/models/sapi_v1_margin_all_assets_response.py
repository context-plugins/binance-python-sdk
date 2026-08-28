from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1MarginAllAssetsResponse(SdkBaseModel):
    asset_full_name: str = Field(alias="assetFullName")
    asset_name: str = Field(alias="assetName")
    is_borrowable: bool = Field(alias="isBorrowable")
    is_mortgageable: bool = Field(alias="isMortgageable")
    user_min_borrow: str = Field(alias="userMinBorrow")
    user_min_repay: str = Field(alias="userMinRepay")


class SapiV1MarginAllAssetsResponseDict(TypedDict):
    asset_full_name: str
    asset_name: str
    is_borrowable: bool
    is_mortgageable: bool
    user_min_borrow: str
    user_min_repay: str
