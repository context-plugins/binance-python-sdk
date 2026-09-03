from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Data26(SdkBaseModel):
    token: str
    amount: str
    reference_no: str = Field(alias="referenceNo")
    identity_no: str = Field(alias="identityNo")


class Data26Dict(TypedDict):
    token: str
    amount: str
    reference_no: str
    identity_no: str
