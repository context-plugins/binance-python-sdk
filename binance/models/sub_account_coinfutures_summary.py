from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .delivery_account_summary_resp import DeliveryAccountSummaryResp, DeliveryAccountSummaryRespDict


class SubAccountCoinfuturesSummary(SdkBaseModel):
    delivery_account_summary_resp: DeliveryAccountSummaryResp = Field(alias="deliveryAccountSummaryResp")


class SubAccountCoinfuturesSummaryDict(TypedDict):
    delivery_account_summary_resp: DeliveryAccountSummaryResp | DeliveryAccountSummaryRespDict
