from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Extend(SdkBaseModel):
    institution_name: str = Field(alias="institutionName")
    card_number: str = Field(alias="cardNumber")
    digital_wallet_id: str = Field(alias="digitalWalletId")


class ExtendDict(TypedDict):
    institution_name: str
    card_number: str
    digital_wallet_id: str
