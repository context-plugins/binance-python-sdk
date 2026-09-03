from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1PortfolioRepayFuturesSwitchResponse1(SdkBaseModel):
    auto_repay: bool = Field(alias="autoRepay")


class SapiV1PortfolioRepayFuturesSwitchResponse1Dict(TypedDict):
    auto_repay: bool
