from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SapiV1MarginTradeCoeffResponse(SdkBaseModel):
    normal_bar: Optional[str] = Field(default=UNSET, alias="normalBar")
    """Account's currently max borrowable amount with sufficient system availability"""

    margin_call_bar: Optional[str] = Field(default=UNSET, alias="marginCallBar")
    """Max borrowable amount limited by the account level"""

    force_liquidation_bar: Optional[str] = Field(default=UNSET, alias="forceLiquidationBar")
    """Liquidation Margin Ratio"""


class SapiV1MarginTradeCoeffResponseDict(TypedDict):
    normal_bar: NotRequired[str]
    margin_call_bar: NotRequired[str]
    force_liquidation_bar: NotRequired[str]
