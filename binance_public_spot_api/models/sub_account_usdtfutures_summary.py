from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .future_account_summary_resp import FutureAccountSummaryResp, FutureAccountSummaryRespDict


class SubAccountUsdtfuturesSummary(SdkBaseModel):
    future_account_summary_resp: FutureAccountSummaryResp = Field(alias="futureAccountSummaryResp")


class SubAccountUsdtfuturesSummaryDict(TypedDict):
    future_account_summary_resp: FutureAccountSummaryResp | FutureAccountSummaryRespDict
