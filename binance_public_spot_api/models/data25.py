from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Data25(SdkBaseModel):
    reference_no: str = Field(alias="referenceNo")
    code: str
    expired_time: int = Field(alias="expiredTime")


class Data25Dict(TypedDict):
    reference_no: str
    code: str
    expired_time: int
