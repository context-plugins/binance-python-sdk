from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1BlvtUserLimitResponse(SdkBaseModel):
    token_name: str = Field(alias="tokenName")
    user_daily_total_purchase_limit: str = Field(alias="userDailyTotalPurchaseLimit")
    """USDT"""

    user_daily_total_redeem_limit: str = Field(alias="userDailyTotalRedeemLimit")
    """USDT"""


class SapiV1BlvtUserLimitResponseDict(TypedDict):
    token_name: str
    user_daily_total_purchase_limit: str
    user_daily_total_redeem_limit: str
