from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1AssetTradeFeeResponse(SdkBaseModel):
    symbol: str
    maker_commission: str = Field(alias="makerCommission")
    taker_commission: str = Field(alias="takerCommission")


class SapiV1AssetTradeFeeResponseDict(TypedDict):
    symbol: str
    maker_commission: str
    taker_commission: str
