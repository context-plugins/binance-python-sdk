from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class RoiAndDimensionTypeList(SdkBaseModel):
    simulate_roi: str = Field(alias="simulateRoi")
    dimension_value: str = Field(alias="dimensionValue")
    dimension_unit: str = Field(alias="dimensionUnit")


class RoiAndDimensionTypeListDict(TypedDict):
    simulate_roi: str
    dimension_value: str
    dimension_unit: str
