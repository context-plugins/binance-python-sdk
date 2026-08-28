from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1MiningHashTransferConfigResponse(SdkBaseModel):
    code: int
    msg: str
    data: int
    """Mining Account"""


class SapiV1MiningHashTransferConfigResponseDict(TypedDict):
    code: int
    msg: str
    data: int
