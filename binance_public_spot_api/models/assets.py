from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Assets(SdkBaseModel):
    matic: str = Field(alias="MATIC")
    stpt: str = Field(alias="STPT")
    tvk: str = Field(alias="TVK")
    shib: str = Field(alias="SHIB")


class AssetsDict(TypedDict):
    matic: str
    stpt: str
    tvk: str
    shib: str
