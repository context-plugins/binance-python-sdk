from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1CapitalDepositAddressListResponse(SdkBaseModel):
    coin: str
    address: str
    is_default: int = Field(alias="isDefault")


class SapiV1CapitalDepositAddressListResponseDict(TypedDict):
    coin: str
    address: str
    is_default: int
