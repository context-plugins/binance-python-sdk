from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row42(SdkBaseModel):
    amount: str
    asset: str
    time: int
    purchase_id: int = Field(alias="purchaseId")
    product_id: str = Field(alias="productId")
    type_: str = Field(alias="type")
    """AUTO for auto subscribe, NORMAL for normal subscription, CONVERT for Locked to Flexible, LOAN for flexible loan
    collateral, AI for Auto Invest subscribe, TRANSFER for Locked Savings to Flexible"""

    source_account: str = Field(alias="sourceAccount")
    """SPOT, FUNDING, SPOTANDFUNDING"""

    amt_from_spot: str = Field(alias="amtFromSpot")
    """Display if sourceAccount is SPOTANDFUNDING"""

    amt_from_funding: str = Field(alias="amtFromFunding")
    """Display if sourceAccount is SPOTANDFUNDING"""

    status: str
    """PURCHASING/SUCCESS/FAILED"""


class Row42Dict(TypedDict):
    amount: str
    asset: str
    time: int
    purchase_id: int
    product_id: str
    type_: str
    source_account: str
    amt_from_spot: str
    amt_from_funding: str
    status: str
