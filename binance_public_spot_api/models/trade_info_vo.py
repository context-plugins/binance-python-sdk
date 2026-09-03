from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TradeInfoVo(SdkBaseModel):
    user_id: Optional[int] = Field(default=UNSET, alias="userId")
    btc: Optional[float] = UNSET
    btc_futures: Optional[float] = Field(default=UNSET, alias="btcFutures")
    btc_margin: Optional[float] = Field(default=UNSET, alias="btcMargin")
    busd: Optional[float] = UNSET
    busd_futures: Optional[float] = Field(default=UNSET, alias="busdFutures")
    busd_margin: Optional[float] = Field(default=UNSET, alias="busdMargin")
    date: Optional[int] = UNSET


class TradeInfoVoDict(TypedDict):
    user_id: NotRequired[int]
    btc: NotRequired[float]
    btc_futures: NotRequired[float]
    btc_margin: NotRequired[float]
    busd: NotRequired[float]
    busd_futures: NotRequired[float]
    busd_margin: NotRequired[float]
    date: NotRequired[int]
