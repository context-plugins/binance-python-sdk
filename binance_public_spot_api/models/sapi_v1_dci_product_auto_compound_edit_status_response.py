from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1DciProductAutoCompoundEditStatusResponse(SdkBaseModel):
    position_id: str = Field(alias="positionId")
    auto_compound_plan: str = Field(alias="autoCompoundPlan")
    """NONE, STANDARD, ADVANCED"""


class SapiV1DciProductAutoCompoundEditStatusResponseDict(TypedDict):
    position_id: str
    auto_compound_plan: str
