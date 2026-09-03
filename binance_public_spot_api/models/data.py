from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .balance import Balance, BalanceDict


class Data(SdkBaseModel):
    balances: list[Balance]
    total_asset_of_btc: str = Field(alias="totalAssetOfBtc")


class DataDict(TypedDict):
    balances: list[Balance | BalanceDict]
    total_asset_of_btc: str
