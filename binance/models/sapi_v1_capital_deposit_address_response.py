from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1CapitalDepositAddressResponse(SdkBaseModel):
    address: str
    coin: str
    tag: str
    url: str


class SapiV1CapitalDepositAddressResponseDict(TypedDict):
    address: str
    coin: str
    tag: str
    url: str
