from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BnbBurnStatus(SdkBaseModel):
    spot_bnb_burn: bool = Field(alias="spotBNBBurn")
    interest_bnb_burn: bool = Field(alias="interestBNBBurn")


class BnbBurnStatusDict(TypedDict):
    spot_bnb_burn: bool
    interest_bnb_burn: bool
