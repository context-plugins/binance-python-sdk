from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .delivery_position_risk_vo import DeliveryPositionRiskVo, DeliveryPositionRiskVoDict


class SubAccountCoinfuturesPositionRisk(SdkBaseModel):
    delivery_position_risk_vos: list[DeliveryPositionRiskVo] = Field(alias="deliveryPositionRiskVos")


class SubAccountCoinfuturesPositionRiskDict(TypedDict):
    delivery_position_risk_vos: list[DeliveryPositionRiskVo | DeliveryPositionRiskVoDict]
