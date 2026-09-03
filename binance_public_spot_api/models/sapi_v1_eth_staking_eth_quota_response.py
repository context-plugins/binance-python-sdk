from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1EthStakingEthQuotaResponse(SdkBaseModel):
    left_staking_personal_quota: str = Field(alias="leftStakingPersonalQuota")
    """Show min(Daily available limit, total personal staking quota)"""

    left_redemption_personal_quota: str = Field(alias="leftRedemptionPersonalQuota")
    """Show min(Daily personal redeem quota, total redemption limit)"""


class SapiV1EthStakingEthQuotaResponseDict(TypedDict):
    left_staking_personal_quota: str
    left_redemption_personal_quota: str
