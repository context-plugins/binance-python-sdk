from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row29(SdkBaseModel):
    loan_coin: str = Field(alias="loanCoin")
    flexible_interest_rate: str = Field(alias="flexibleInterestRate")
    flexible_min_limit: str = Field(alias="flexibleMinLimit")
    flexible_max_limit: str = Field(alias="flexibleMaxLimit")


class Row29Dict(TypedDict):
    loan_coin: str
    flexible_interest_rate: str
    flexible_min_limit: str
    flexible_max_limit: str
