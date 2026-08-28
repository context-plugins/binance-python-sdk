from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1DciProductAccountsResponse(SdkBaseModel):
    total_amount_in_btc: str = Field(alias="totalAmountInBTC")
    """Total BTC amounts in Dual Investment"""

    total_amount_in_usdt: str = Field(alias="totalAmountInUSDT")
    """Total USDT equivalents in BTC in Dual Investment"""


class SapiV1DciProductAccountsResponseDict(TypedDict):
    total_amount_in_btc: str
    total_amount_in_usdt: str
