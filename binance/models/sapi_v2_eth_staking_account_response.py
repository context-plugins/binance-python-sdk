from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .holdings import Holdings, HoldingsDict
from .profit import Profit, ProfitDict


class SapiV2EthStakingAccountResponse(SdkBaseModel):
    holding_in_eth: str = Field(alias="holdingInETH")
    holdings: Holdings
    thirty_days_profit_in_eth: str = Field(alias="thirtyDaysProfitInETH")
    profit: Profit


class SapiV2EthStakingAccountResponseDict(TypedDict):
    holding_in_eth: str
    holdings: Holdings | HoldingsDict
    thirty_days_profit_in_eth: str
    profit: Profit | ProfitDict
