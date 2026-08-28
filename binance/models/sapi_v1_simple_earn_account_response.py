from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1SimpleEarnAccountResponse(SdkBaseModel):
    total_amount_in_btc: str = Field(alias="totalAmountInBTC")
    total_amount_in_usdt: str = Field(alias="totalAmountInUSDT")
    total_flexible_amount_in_btc: str = Field(alias="totalFlexibleAmountInBTC")
    total_flexible_amount_in_usdt: str = Field(alias="totalFlexibleAmountInUSDT")
    total_locked_in_btc: str = Field(alias="totalLockedInBTC")
    total_locked_in_usdt: str = Field(alias="totalLockedInUSDT")


class SapiV1SimpleEarnAccountResponseDict(TypedDict):
    total_amount_in_btc: str
    total_amount_in_usdt: str
    total_flexible_amount_in_btc: str
    total_flexible_amount_in_usdt: str
    total_locked_in_btc: str
    total_locked_in_usdt: str
