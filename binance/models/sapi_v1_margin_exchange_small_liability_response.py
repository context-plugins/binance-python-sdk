from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1MarginExchangeSmallLiabilityResponse(SdkBaseModel):
    asset: str
    interest: str
    principal: str
    liability_asset: str = Field(alias="liabilityAsset")
    liability_qty: float = Field(alias="liabilityQty")


class SapiV1MarginExchangeSmallLiabilityResponseDict(TypedDict):
    asset: str
    interest: str
    principal: str
    liability_asset: str
    liability_qty: float
