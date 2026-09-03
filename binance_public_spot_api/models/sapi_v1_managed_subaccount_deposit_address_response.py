from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1ManagedSubaccountDepositAddressResponse(SdkBaseModel):
    coin: str
    address: str
    tag: str
    url: str


class SapiV1ManagedSubaccountDepositAddressResponseDict(TypedDict):
    coin: str
    address: str
    tag: str
    url: str
