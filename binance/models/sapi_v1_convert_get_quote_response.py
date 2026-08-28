from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1ConvertGetQuoteResponse(SdkBaseModel):
    quote_id: str = Field(alias="quoteId")
    ratio: str
    inverse_ratio: str = Field(alias="inverseRatio")
    valid_timestamp: int = Field(alias="validTimestamp")
    to_amount: str = Field(alias="toAmount")
    from_amount: str = Field(alias="fromAmount")


class SapiV1ConvertGetQuoteResponseDict(TypedDict):
    quote_id: str
    ratio: str
    inverse_ratio: str
    valid_timestamp: int
    to_amount: str
    from_amount: str
