from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1ManagedSubaccountAssetResponse(SdkBaseModel):
    coin: str
    name: str
    total_balance: str = Field(alias="totalBalance")
    available_balance: str = Field(alias="availableBalance")
    in_order: str = Field(alias="inOrder")
    btc_value: str = Field(alias="btcValue")


class SapiV1ManagedSubaccountAssetResponseDict(TypedDict):
    coin: str
    name: str
    total_balance: str
    available_balance: str
    in_order: str
    btc_value: str
