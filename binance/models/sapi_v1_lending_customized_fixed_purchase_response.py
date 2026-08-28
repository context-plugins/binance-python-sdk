from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1LendingCustomizedFixedPurchaseResponse(SdkBaseModel):
    purchase_id: str = Field(alias="purchaseId")


class SapiV1LendingCustomizedFixedPurchaseResponseDict(TypedDict):
    purchase_id: str
