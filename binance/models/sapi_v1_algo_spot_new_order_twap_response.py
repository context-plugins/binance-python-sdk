from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1AlgoSpotNewOrderTwapResponse(SdkBaseModel):
    client_algo_id: str = Field(alias="clientAlgoId")
    success: bool
    code: int
    msg: str


class SapiV1AlgoSpotNewOrderTwapResponseDict(TypedDict):
    client_algo_id: str
    success: bool
    code: int
    msg: str
