from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .indicators import Indicators, IndicatorsDict
from .trigger_condition import TriggerCondition, TriggerConditionDict


class Data4(SdkBaseModel):
    is_locked: bool = Field(alias="isLocked")
    """API trading function is locked or not"""

    planned_recover_time: int = Field(alias="plannedRecoverTime")
    """If API trading function is locked, this is the planned recover time"""

    trigger_condition: TriggerCondition = Field(alias="triggerCondition")
    indicators: Indicators
    """The indicators updated every 30 seconds"""

    update_time: int = Field(alias="updateTime")


class Data4Dict(TypedDict):
    is_locked: bool
    planned_recover_time: int
    trigger_condition: TriggerCondition | TriggerConditionDict
    indicators: Indicators | IndicatorsDict
    update_time: int
