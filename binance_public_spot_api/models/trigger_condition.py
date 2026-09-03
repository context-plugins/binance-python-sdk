from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TriggerCondition(SdkBaseModel):
    gcr: int = Field(alias="GCR")
    """Number of GTC orders"""

    ifer: int = Field(alias="IFER")
    """Number of FOK/IOC orders"""

    ufr: int = Field(alias="UFR")
    """Number of orders"""


class TriggerConditionDict(TypedDict):
    gcr: int
    ifer: int
    ufr: int
