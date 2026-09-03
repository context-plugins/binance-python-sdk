from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .balance import Balance, BalanceDict
from .commission_rates import CommissionRates, CommissionRatesDict


class Account(SdkBaseModel):
    maker_commission: int = Field(alias="makerCommission")
    taker_commission: int = Field(alias="takerCommission")
    buyer_commission: int = Field(alias="buyerCommission")
    seller_commission: int = Field(alias="sellerCommission")
    commission_rates: CommissionRates = Field(alias="commissionRates")
    can_trade: bool = Field(alias="canTrade")
    can_withdraw: bool = Field(alias="canWithdraw")
    can_deposit: bool = Field(alias="canDeposit")
    brokered: bool
    require_self_trade_prevention: bool = Field(alias="requireSelfTradePrevention")
    prevent_sor: bool = Field(alias="preventSor")
    update_time: int = Field(alias="updateTime")
    account_type: str = Field(alias="accountType")
    balances: list[Balance]
    permissions: list[str]
    uid: int


class AccountDict(TypedDict):
    maker_commission: int
    taker_commission: int
    buyer_commission: int
    seller_commission: int
    commission_rates: CommissionRates | CommissionRatesDict
    can_trade: bool
    can_withdraw: bool
    can_deposit: bool
    brokered: bool
    require_self_trade_prevention: bool
    prevent_sor: bool
    update_time: int
    account_type: str
    balances: list[Balance | BalanceDict]
    permissions: list[str]
    uid: int
