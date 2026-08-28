from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1MiningHashTransferConfigCancelResponse(SdkBaseModel):
    code: int
    msg: str
    data: bool


class SapiV1MiningHashTransferConfigCancelResponseDict(TypedDict):
    code: int
    msg: str
    data: bool
