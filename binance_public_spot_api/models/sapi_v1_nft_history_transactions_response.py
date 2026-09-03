from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .list3 import List3, List3Dict


class SapiV1NftHistoryTransactionsResponse(SdkBaseModel):
    total: int
    list_: list[List3] = Field(alias="list")


class SapiV1NftHistoryTransactionsResponseDict(TypedDict):
    total: int
    list_: list[List3 | List3Dict]
