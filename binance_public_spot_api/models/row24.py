from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row24(SdkBaseModel):
    order_id: str = Field(alias="orderId")
    collateral_coin: str = Field(alias="collateralCoin")
    pre_margin_call: str = Field(alias="preMarginCall")
    after_margin_call: str = Field(alias="afterMarginCall")
    customize_time: int = Field(alias="customizeTime")


class Row24Dict(TypedDict):
    order_id: str
    collateral_coin: str
    pre_margin_call: str
    after_margin_call: str
    customize_time: int
