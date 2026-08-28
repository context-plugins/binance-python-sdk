from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .list4 import List4, List4Dict


class SapiV1NftHistoryDepositResponse(SdkBaseModel):
    total: int
    list_: list[List4] = Field(alias="list")


class SapiV1NftHistoryDepositResponseDict(TypedDict):
    total: int
    list_: list[List4 | List4Dict]
