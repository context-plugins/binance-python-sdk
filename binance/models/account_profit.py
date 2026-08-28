from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AccountProfit(SdkBaseModel):
    time: int
    """Mining date"""

    type_: int = Field(alias="type")
    """0:Mining Wallet,5:Mining Address,7:Pool Savings,8:Transferred,31:Income Transfer ,32:Hashrate Resale-Mining
    Wallet 33:Hashrate Resale-Pool Savings"""

    hash_transfer: int = Field(alias="hashTransfer")
    """Transferred Hashrate"""

    transfer_amount: float = Field(alias="transferAmount")
    """Transferred Income"""

    day_hash_rate: int = Field(alias="dayHashRate")
    """Daily Hashrate"""

    profit_amount: float = Field(alias="profitAmount")
    """Earnings Amount"""

    coin_name: str = Field(alias="coinName")
    """Coin Type"""

    status: int
    """Status：0:Unpaid, 1:Paying 2：Paid"""


class AccountProfitDict(TypedDict):
    time: int
    type_: int
    hash_transfer: int
    transfer_amount: float
    day_hash_rate: int
    profit_amount: float
    coin_name: str
    status: int
