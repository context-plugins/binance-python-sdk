from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1PortfolioRepayFuturesSwitchResponse(SdkBaseModel):
    msg: str


class SapiV1PortfolioRepayFuturesSwitchResponseDict(TypedDict):
    msg: str
