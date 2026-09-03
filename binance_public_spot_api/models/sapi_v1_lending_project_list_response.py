from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1LendingProjectListResponse(SdkBaseModel):
    asset: str
    display_priority: int = Field(alias="displayPriority")
    duration: int
    interest_per_lot: str = Field(alias="interestPerLot")
    interest_rate: str = Field(alias="interestRate")
    lot_size: str = Field(alias="lotSize")
    lots_low_limit: int = Field(alias="lotsLowLimit")
    lots_purchased: int = Field(alias="lotsPurchased")
    lots_up_limit: int = Field(alias="lotsUpLimit")
    max_lots_per_user: int = Field(alias="maxLotsPerUser")
    need_kyc: bool = Field(alias="needKyc")
    project_id: str = Field(alias="projectId")
    project_name: str = Field(alias="projectName")
    status: str
    type_: str = Field(alias="type")
    with_area_limitation: bool = Field(alias="withAreaLimitation")


class SapiV1LendingProjectListResponseDict(TypedDict):
    asset: str
    display_priority: int
    duration: int
    interest_per_lot: str
    interest_rate: str
    lot_size: str
    lots_low_limit: int
    lots_purchased: int
    lots_up_limit: int
    max_lots_per_user: int
    need_kyc: bool
    project_id: str
    project_name: str
    status: str
    type_: str
    with_area_limitation: bool
