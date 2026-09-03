from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .extend import Extend, ExtendDict


class ReceiverInfo(SdkBaseModel):
    name: str
    type_: str = Field(alias="type")
    email: str
    binance_id: str = Field(alias="binanceId")
    account_id: str = Field(alias="accountId")
    country_code: str = Field(alias="countryCode")
    phone_number: str = Field(alias="phoneNumber")
    mobile_code: str = Field(alias="mobileCode")
    extend: Optional[list[Extend]] = UNSET


class ReceiverInfoDict(TypedDict):
    name: str
    type_: str
    email: str
    binance_id: str
    account_id: str
    country_code: str
    phone_number: str
    mobile_code: str
    extend: NotRequired[list[Extend | ExtendDict]]
