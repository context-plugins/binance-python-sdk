from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel


class SapiV1LendingProjectPositionListResponse(SdkBaseModel):
    asset: str
    can_transfer: bool = Field(alias="canTransfer")
    create_timestamp: int = Field(alias="createTimestamp")
    duration: int
    end_time: int = Field(alias="endTime")
    interest: str
    interest_rate: str = Field(alias="interestRate")
    lot: int
    position_id: int = Field(alias="positionId")
    principal: str
    project_id: str = Field(alias="projectId")
    project_name: str = Field(alias="projectName")
    purchase_time: int = Field(alias="purchaseTime")
    redeem_date: Date = Field(alias="redeemDate")
    start_time: int = Field(alias="startTime")
    status: str
    type_: str = Field(alias="type")


class SapiV1LendingProjectPositionListResponseDict(TypedDict):
    asset: str
    can_transfer: bool
    create_timestamp: int
    duration: int
    end_time: int
    interest: str
    interest_rate: str
    lot: int
    position_id: int
    principal: str
    project_id: str
    project_name: str
    purchase_time: int
    redeem_date: Date
    start_time: int
    status: str
    type_: str
