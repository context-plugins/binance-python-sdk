from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row43(SdkBaseModel):
    position_id: str = Field(alias="positionId")
    purchase_id: int = Field(alias="purchaseId")
    project_id: str = Field(alias="projectId")
    time: int
    asset: str
    amount: str
    lock_period: str = Field(alias="lockPeriod")
    type_: str = Field(alias="type")
    """NORMAL for normal subscription, AUTO for auto-subscription order, ACTIVITY for activity order, TRIAL for trial
    fund order, RESTAKE for restake order"""

    source_account: str = Field(alias="sourceAccount")
    """SPOT, FUNDING, SPOTANDFUNDING"""

    amt_from_spot: str = Field(alias="amtFromSpot")
    """Display if sourceAccount is SPOTANDFUNDING"""

    amt_from_funding: str = Field(alias="amtFromFunding")
    """Display if sourceAccount is SPOTANDFUNDING"""

    status: str
    """PURCHASING/SUCCESS/FAILED"""


class Row43Dict(TypedDict):
    position_id: str
    purchase_id: int
    project_id: str
    time: int
    asset: str
    amount: str
    lock_period: str
    type_: str
    source_account: str
    amt_from_spot: str
    amt_from_funding: str
    status: str
