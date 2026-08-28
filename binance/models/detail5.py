from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Detail5(SdkBaseModel):
    target_asset: Optional[str] = Field(default=UNSET, alias="targetAsset")
    percentage: Optional[int] = UNSET


class Detail5Dict(TypedDict):
    target_asset: NotRequired[str]
    percentage: NotRequired[int]
