from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1PortfolioPmLoanResponse(SdkBaseModel):
    asset: str
    amount: str


class SapiV1PortfolioPmLoanResponseDict(TypedDict):
    asset: str
    amount: str
