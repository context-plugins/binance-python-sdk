from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .list5 import List5, List5Dict


class SapiV1NftHistoryWithdrawResponse(SdkBaseModel):
    total: int
    list_: list[List5] = Field(alias="list")


class SapiV1NftHistoryWithdrawResponseDict(TypedDict):
    total: int
    list_: list[List5 | List5Dict]
