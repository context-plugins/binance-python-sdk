from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .balance2 import Balance2, Balance2Dict


class SapiV3SubAccountAssetsResponse(SdkBaseModel):
    balances: list[Balance2]


class SapiV3SubAccountAssetsResponseDict(TypedDict):
    balances: list[Balance2 | Balance2Dict]
