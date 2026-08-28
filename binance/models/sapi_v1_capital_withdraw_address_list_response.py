from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1CapitalWithdrawAddressListResponse(SdkBaseModel):
    address: str
    address_tag: str = Field(alias="addressTag")
    coin: str
    name: str
    network: str
    origin: str
    origin_type: str = Field(alias="originType")
    white_status: bool = Field(alias="whiteStatus")


class SapiV1CapitalWithdrawAddressListResponseDict(TypedDict):
    address: str
    address_tag: str
    coin: str
    name: str
    network: str
    origin: str
    origin_type: str
    white_status: bool
