from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1LendingAutoInvestPlanEditStatusResponse(SdkBaseModel):
    plan_id: int = Field(alias="planId")
    next_execution_date_time: int = Field(alias="nextExecutionDateTime")
    status: str


class SapiV1LendingAutoInvestPlanEditStatusResponseDict(TypedDict):
    plan_id: int
    next_execution_date_time: int
    status: str
