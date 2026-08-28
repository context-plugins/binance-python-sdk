from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Row12(SdkBaseModel):
    order_id: int = Field(alias="orderId")
    loan_coin: str = Field(alias="loanCoin")
    total_debt: str = Field(alias="totalDebt")
    residual_interest: str = Field(alias="residualInterest")
    collateral_account_id: str = Field(alias="collateralAccountId")
    collateral_coin: str = Field(alias="collateralCoin")
    collateral_value: str = Field(alias="collateralValue")
    """locked collateral value shown in USD value"""

    total_collateral_value_after_haircut: Optional[str] = Field(default=UNSET, alias="totalCollateralValueAfterHaircut")
    locked_collateral_value: Optional[str] = Field(default=UNSET, alias="lockedCollateralValue")
    current_ltv: str = Field(alias="currentLTV")
    expiration_time: int = Field(alias="expirationTime")
    loan_date: str = Field(alias="loanDate")
    loan_rate: str = Field(alias="loanRate")
    loan_term: str = Field(alias="loanTerm")


class Row12Dict(TypedDict):
    order_id: int
    loan_coin: str
    total_debt: str
    residual_interest: str
    collateral_account_id: str
    collateral_coin: str
    collateral_value: str
    total_collateral_value_after_haircut: NotRequired[str]
    locked_collateral_value: NotRequired[str]
    current_ltv: str
    expiration_time: int
    loan_date: str
    loan_rate: str
    loan_term: str
