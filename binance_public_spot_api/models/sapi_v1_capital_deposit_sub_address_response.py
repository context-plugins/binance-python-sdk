from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1CapitalDepositSubAddressResponse(SdkBaseModel):
    address: str
    coin: str
    tag: str
    url: str


class SapiV1CapitalDepositSubAddressResponseDict(TypedDict):
    address: str
    coin: str
    tag: str
    url: str
