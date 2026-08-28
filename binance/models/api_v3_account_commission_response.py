from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .discount import Discount, DiscountDict
from .standard_commission import StandardCommission, StandardCommissionDict
from .tax_commission import TaxCommission, TaxCommissionDict


class ApiV3AccountCommissionResponse(SdkBaseModel):
    symbol: str
    standard_commission: StandardCommission = Field(alias="standardCommission")
    """Standard commission rates on trades from the order."""

    tax_commission: TaxCommission = Field(alias="taxCommission")
    """Tax commission rates for trades from the order."""

    discount: Discount
    """Discount commission when paying in BNB."""


class ApiV3AccountCommissionResponseDict(TypedDict):
    symbol: str
    standard_commission: StandardCommission | StandardCommissionDict
    tax_commission: TaxCommission | TaxCommissionDict
    discount: Discount | DiscountDict
