from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1AlgoSpotOrderResponse(SdkBaseModel):
    algo_id: int = Field(alias="algoId")
    success: bool
    code: int
    msg: str


class SapiV1AlgoSpotOrderResponseDict(TypedDict):
    algo_id: int
    success: bool
    code: int
    msg: str
