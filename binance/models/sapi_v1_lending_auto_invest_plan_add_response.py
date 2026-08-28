from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1LendingAutoInvestPlanAddResponse(SdkBaseModel):
    plan_id: int = Field(alias="planId")
    next_execution_date_time: int = Field(alias="nextExecutionDateTime")


class SapiV1LendingAutoInvestPlanAddResponseDict(TypedDict):
    plan_id: int
    next_execution_date_time: int
