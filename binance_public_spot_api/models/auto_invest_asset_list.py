from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .roi_and_dimension_type_list import RoiAndDimensionTypeList, RoiAndDimensionTypeListDict


class AutoInvestAssetList(SdkBaseModel):
    target_asset: str = Field(alias="targetAsset")
    roi_and_dimension_type_list: list[RoiAndDimensionTypeList] = Field(alias="roiAndDimensionTypeList")


class AutoInvestAssetListDict(TypedDict):
    target_asset: str
    roi_and_dimension_type_list: list[RoiAndDimensionTypeList | RoiAndDimensionTypeListDict]
