from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Discount(SdkBaseModel):
    """Discount commission when paying in BNB."""

    enabled_for_account: Optional[bool] = Field(default=UNSET, alias="enabledForAccount")
    enabled_for_symbol: Optional[bool] = Field(default=UNSET, alias="enabledForSymbol")
    discount_asset: Optional[str] = Field(default=UNSET, alias="discountAsset")
    discount: Optional[str] = UNSET
    """Standard commission is reduced by this rate when paying commission in BNB."""


class DiscountDict(TypedDict):
    enabled_for_account: NotRequired[bool]
    enabled_for_symbol: NotRequired[bool]
    discount_asset: NotRequired[str]
    discount: NotRequired[str]
