from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .trade_info_vo import TradeInfoVo, TradeInfoVoDict


class SapiV1SubAccountTransactionStatisticsResponse(SdkBaseModel):
    recent30_btc_total: str = Field(alias="recent30BtcTotal")
    recent30_btc_futures_total: str = Field(alias="recent30BtcFuturesTotal")
    recent30_btc_margin_total: str = Field(alias="recent30BtcMarginTotal")
    recent30_busd_total: str = Field(alias="recent30BusdTotal")
    recent30_busd_futures_total: str = Field(alias="recent30BusdFuturesTotal")
    recent30_busd_margin_total: str = Field(alias="recent30BusdMarginTotal")
    trade_info_vos: list[TradeInfoVo] = Field(alias="tradeInfoVos")


class SapiV1SubAccountTransactionStatisticsResponseDict(TypedDict):
    recent30_btc_total: str
    recent30_btc_futures_total: str
    recent30_btc_margin_total: str
    recent30_busd_total: str
    recent30_busd_futures_total: str
    recent30_busd_margin_total: str
    trade_info_vos: list[TradeInfoVo | TradeInfoVoDict]
