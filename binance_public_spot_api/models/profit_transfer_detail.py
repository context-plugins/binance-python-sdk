from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ProfitTransferDetail(SdkBaseModel):
    pool_username: str = Field(alias="poolUsername")
    """Transfer out of sub-account"""

    to_pool_username: str = Field(alias="toPoolUsername")
    """Transfer into subaccount"""

    algo_name: str = Field(alias="algoName")
    """Transfer algorithm"""

    hash_rate: int = Field(alias="hashRate")
    """Transferred Hashrate quantity"""

    day: int
    """Transfer date"""

    amount: float
    """Transfer income"""

    coin_name: str = Field(alias="coinName")


class ProfitTransferDetailDict(TypedDict):
    pool_username: str
    to_pool_username: str
    algo_name: str
    hash_rate: int
    day: int
    amount: float
    coin_name: str
