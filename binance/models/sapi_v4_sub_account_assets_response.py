from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .balance import Balance, BalanceDict


class SapiV4SubAccountAssetsResponse(SdkBaseModel):
    balances: list[Balance]


class SapiV4SubAccountAssetsResponseDict(TypedDict):
    balances: list[Balance | BalanceDict]
