from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1AlgoFuturesNewOrderTwapResponse(SdkBaseModel):
    client_algo_id: str = Field(alias="clientAlgoId")
    success: bool
    code: int
    msg: str


class SapiV1AlgoFuturesNewOrderTwapResponseDict(TypedDict):
    client_algo_id: str
    success: bool
    code: int
    msg: str
