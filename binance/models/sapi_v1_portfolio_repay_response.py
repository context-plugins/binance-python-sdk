from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1PortfolioRepayResponse(SdkBaseModel):
    tran_id: int = Field(alias="tranId")


class SapiV1PortfolioRepayResponseDict(TypedDict):
    tran_id: int
