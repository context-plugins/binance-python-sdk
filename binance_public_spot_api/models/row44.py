from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row44(SdkBaseModel):
    amount: str
    asset: str
    time: int
    project_id: str = Field(alias="projectId")
    redeem_id: int = Field(alias="redeemId")
    dest_account: str = Field(alias="destAccount")
    """SPOT, FUNDING"""

    status: str


class Row44Dict(TypedDict):
    amount: str
    asset: str
    time: int
    project_id: str
    redeem_id: int
    dest_account: str
    status: str
