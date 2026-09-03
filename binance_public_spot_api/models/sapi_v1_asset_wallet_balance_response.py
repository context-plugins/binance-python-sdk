from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1AssetWalletBalanceResponse(SdkBaseModel):
    activate: bool
    balance: str
    wallet_name: str = Field(alias="walletName")


class SapiV1AssetWalletBalanceResponseDict(TypedDict):
    activate: bool
    balance: str
    wallet_name: str
