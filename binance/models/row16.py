from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row16(SdkBaseModel):
    collateral_coin: str = Field(alias="collateralCoin")
    st_collateral_ratio1: str = Field(alias="_1stCollateralRatio")
    st_collateral_range1: str = Field(alias="_1stCollateralRange")
    nd_collateral_ratio2: str = Field(alias="_2ndCollateralRatio")
    nd_collateral_range2: str = Field(alias="_2ndCollateralRange")
    rd_collateral_ratio3: str = Field(alias="_3rdCollateralRatio")
    rd_collateral_range3: str = Field(alias="_3rdCollateralRange")
    th_collateral_ratio4: str = Field(alias="_4thCollateralRatio")
    th_collateral_range4: str = Field(alias="_4thCollateralRange")


class Row16Dict(TypedDict):
    collateral_coin: str
    st_collateral_ratio1: str
    st_collateral_range1: str
    nd_collateral_ratio2: str
    nd_collateral_range2: str
    rd_collateral_ratio3: str
    rd_collateral_range3: str
    th_collateral_ratio4: str
    th_collateral_range4: str
