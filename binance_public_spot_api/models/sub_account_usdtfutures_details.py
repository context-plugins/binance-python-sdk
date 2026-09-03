from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .future_account_resp import FutureAccountResp, FutureAccountRespDict


class SubAccountUsdtfuturesDetails(SdkBaseModel):
    future_account_resp: FutureAccountResp = Field(alias="futureAccountResp")


class SubAccountUsdtfuturesDetailsDict(TypedDict):
    future_account_resp: FutureAccountResp | FutureAccountRespDict
