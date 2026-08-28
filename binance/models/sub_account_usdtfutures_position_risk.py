from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .future_position_risk_vo import FuturePositionRiskVo, FuturePositionRiskVoDict


class SubAccountUsdtfuturesPositionRisk(SdkBaseModel):
    future_position_risk_vos: list[FuturePositionRiskVo] = Field(alias="futurePositionRiskVos")


class SubAccountUsdtfuturesPositionRiskDict(TypedDict):
    future_position_risk_vos: list[FuturePositionRiskVo | FuturePositionRiskVoDict]
