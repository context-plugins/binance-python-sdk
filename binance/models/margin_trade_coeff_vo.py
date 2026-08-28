from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class MarginTradeCoeffVo(SdkBaseModel):
    force_liquidation_bar: str = Field(alias="forceLiquidationBar")
    """Liquidation margin ratio"""

    margin_call_bar: str = Field(alias="marginCallBar")
    """Margin call margin ratio"""

    normal_bar: str = Field(alias="normalBar")
    """Initial margin ratio"""


class MarginTradeCoeffVoDict(TypedDict):
    force_liquidation_bar: str
    margin_call_bar: str
    normal_bar: str
