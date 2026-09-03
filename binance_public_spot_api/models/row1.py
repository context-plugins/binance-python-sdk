from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Row1(SdkBaseModel):
    isolated_symbol: Optional[str] = Field(default=UNSET, alias="isolatedSymbol")
    """Isolated symbol, will not be returned for crossed margin"""

    amount: Optional[str] = UNSET
    """Total amount borrowed/repaid"""

    asset: str
    interest: Optional[str] = UNSET
    """Interest repaid"""

    principal: str
    """Principal repaid"""

    status: str
    """one of PENDING (pending execution), CONFIRMED (successfully execution), FAILED (execution failed, nothing
    happened to your account)"""

    timestamp: int
    tx_id: int = Field(alias="txId")


class Row1Dict(TypedDict):
    isolated_symbol: NotRequired[str]
    amount: NotRequired[str]
    asset: str
    interest: NotRequired[str]
    principal: str
    status: str
    timestamp: int
    tx_id: int
