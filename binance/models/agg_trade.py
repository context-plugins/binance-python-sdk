from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AggTrade(SdkBaseModel):
    a: int
    """Aggregate tradeId"""

    p: str
    """Price"""

    q: str
    """Quantity"""

    f: int
    """First tradeId"""

    l_: int = Field(alias="l")
    """Last tradeId"""

    t: bool = Field(alias="T")
    """Timestamp"""

    m: bool
    """Was the buyer the maker?"""


class AggTradeDict(TypedDict):
    a: int
    p: str
    q: str
    f: int
    l_: int
    t: bool
    m: bool
