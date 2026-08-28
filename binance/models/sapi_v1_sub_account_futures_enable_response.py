from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1SubAccountFuturesEnableResponse(SdkBaseModel):
    email: str
    is_futures_enabled: bool = Field(alias="isFuturesEnabled")


class SapiV1SubAccountFuturesEnableResponseDict(TypedDict):
    email: str
    is_futures_enabled: bool
